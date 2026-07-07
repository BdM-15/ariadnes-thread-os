#!/usr/bin/env python3
"""Ariadne Mission Control — read-only dashboard backend (stdlib only)."""
from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
import threading
import time
import uuid
from datetime import datetime, timezone, timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parent
HOST = "127.0.0.1"
PORT = 51763
AGENT_LOG_DB = ROOT / "agents" / "_shared" / "agent-logs.db"
BOARD_DB = ROOT / "board.db"
VAULT_THREAD = ROOT / "knowledge" / "thread"
REGISTRY = ROOT / "agents" / "REGISTRY.yaml"
HERMES_HOME = Path.home() / "AppData" / "Local" / "hermes"
GATEWAY_STATE = HERMES_HOME / "gateway_state.json"
HERMES_CRON_JOBS = HERMES_HOME / "cron" / "jobs.json"

PARTY = ["hermes", "iris", "clio", "odysseus", "hephaestus"]
AGENT_META = {
    "hermes": {"code": "HERMES", "display": "Hermes", "role": "Guildmaster / Orchestrator"},
    "iris": {"code": "IRIS", "display": "Iris", "role": "Scout / Intel Researcher"},
    "clio": {"code": "CLIO", "display": "Clio", "role": "Packet Filler / Scribe"},
    "odysseus": {"code": "ODYS", "display": "Odysseus", "role": "Knight / Strategist"},
    "hephaestus": {"code": "HEPH", "display": "Hephaestus", "role": "Artificer / Builder"},
}

SERVER_START = time.time()
_sse_clients: list[threading.Condition] = []
_sse_lock = threading.Lock()


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def safe_json(obj, default=None):
    try:
        return obj
    except Exception:
        return default


def gateway_data() -> dict:
    try:
        if not GATEWAY_STATE.is_file():
            return {
                "ok": True,
                "exists": False,
                "state": "unknown",
                "kind": "hermes-gateway",
                "platforms": {},
                "active_agents": 0,
                "uptime_seconds": time.time() - SERVER_START,
                "updated_at": utc_now_iso(),
            }
        raw = json.loads(GATEWAY_STATE.read_text(encoding="utf-8"))
        platforms = raw.get("platforms") or {}
        start = raw.get("start_time")
        uptime = None
        if isinstance(start, (int, float)) and start > 1e9:
            uptime = max(0, time.time() - float(start))
        elif isinstance(start, (int, float)):
            uptime = max(0, time.time() - float(start))
        return {
            "ok": True,
            "exists": True,
            "state": raw.get("gateway_state") or raw.get("state") or "unknown",
            "kind": raw.get("kind") or "hermes-gateway",
            "pid": raw.get("pid"),
            "platforms": platforms,
            "active_agents": int(raw.get("active_agents") or 0),
            "uptime_seconds": uptime if uptime is not None else (time.time() - SERVER_START),
            "updated_at": raw.get("updated_at") or utc_now_iso(),
            "raw": raw,
        }
    except Exception as exc:
        return {"ok": False, "error": str(exc), "exists": False, "state": "error", "platforms": {}, "active_agents": 0, "uptime_seconds": 0}


def activity_data() -> dict:
    try:
        if not AGENT_LOG_DB.is_file():
            return {"activity": [], "stats": {"total": 0, "completed": 0, "failed": 0}, "activity_by_day": [], "agents": []}
        conn = sqlite3.connect(f"file:{AGENT_LOG_DB}?mode=ro", uri=True)
        conn.row_factory = sqlite3.Row
        try:
            conn.execute("PRAGMA query_only=1")
        except sqlite3.OperationalError:
            pass
        rows = conn.execute(
            """
            SELECT id, agent_name, task_description, model_used, status, created_at
            FROM agent_logs
            ORDER BY created_at DESC, id DESC
            LIMIT 50
            """
        ).fetchall()
        activity = [dict(r) for r in rows]
        stats_row = conn.execute(
            """
            SELECT
              COUNT(*) AS total,
              SUM(CASE WHEN status='completed' THEN 1 ELSE 0 END) AS completed,
              SUM(CASE WHEN status='failed' THEN 1 ELSE 0 END) AS failed
            FROM agent_logs
            """
        ).fetchone()
        stats = {
            "total": int(stats_row["total"] or 0),
            "completed": int(stats_row["completed"] or 0),
            "failed": int(stats_row["failed"] or 0),
        }
        per_agent = {}
        for name in PARTY:
            per_agent[name] = {
                "agent_name": name,
                "total": 0,
                "completed": 0,
                "failed": 0,
                "last_task": "",
                "last_status": "idle",
                "last_seen": "",
                "model": "",
            }
        all_rows = conn.execute(
            "SELECT agent_name, task_description, model_used, status, created_at FROM agent_logs ORDER BY created_at DESC, id DESC"
        ).fetchall()
        for r in all_rows:
            an = str(r["agent_name"] or "").lower()
            if an not in per_agent:
                continue
            pa = per_agent[an]
            pa["total"] += 1
            if r["status"] == "completed":
                pa["completed"] += 1
            elif r["status"] == "failed":
                pa["failed"] += 1
            if not pa["last_seen"]:
                pa["last_seen"] = r["created_at"] or ""
                pa["last_task"] = r["task_description"] or ""
                pa["last_status"] = r["status"] or "unknown"
                pa["model"] = r["model_used"] or ""
        agents_stats = []
        for name in PARTY:
            pa = per_agent[name]
            meta = AGENT_META[name]
            agents_stats.append(
                {
                    "name": name,
                    "agent_name": name,
                    "display": meta["display"],
                    "code": meta["code"],
                    "role": meta["role"],
                    "total": pa["total"],
                    "responses": pa["total"],
                    "completed": pa["completed"],
                    "failed": pa["failed"],
                    "last_task": pa["last_task"],
                    "last_status": pa["last_status"],
                    "status": pa["last_status"],
                    "last_seen": pa["last_seen"],
                    "model": pa["model"],
                }
            )
        cutoff = (datetime.now(timezone.utc) - timedelta(days=6)).strftime("%Y-%m-%d")
        day_rows = conn.execute(
            """
            SELECT substr(created_at, 1, 10) AS day, agent_name, COUNT(*) AS c
            FROM agent_logs
            WHERE substr(created_at, 1, 10) >= ?
            GROUP BY day, agent_name
            ORDER BY day ASC
            """,
            (cutoff,),
        ).fetchall()
        days = []
        for i in range(7):
            d = (datetime.now(timezone.utc) - timedelta(days=6 - i)).strftime("%Y-%m-%d")
            days.append(d)
        by_day = {d: {"day": d, "total": 0, "agents": {n: 0 for n in PARTY}} for d in days}
        for r in day_rows:
            day = r["day"]
            if day not in by_day:
                by_day[day] = {"day": day, "total": 0, "agents": {n: 0 for n in PARTY}}
            an = str(r["agent_name"] or "").lower()
            c = int(r["c"] or 0)
            by_day[day]["total"] += c
            if an in by_day[day]["agents"]:
                by_day[day]["agents"][an] += c
        activity_by_day = [by_day[d] for d in days if d in by_day]
        conn.close()
        return {
            "activity": activity,
            "stats": stats,
            "activity_by_day": activity_by_day,
            "agents": agents_stats,
        }
    except Exception as exc:
        return {"activity": [], "stats": {"total": 0, "completed": 0, "failed": 0, "error": str(exc)}, "activity_by_day": [], "agents": [], "error": str(exc)}


def _parse_registry_agents() -> list[dict]:
    if not REGISTRY.is_file():
        return []
    text = REGISTRY.read_text(encoding="utf-8")
    blocks = re.split(r"\n  - name:", text)
    out = []
    for block in blocks[1:]:
        name_m = re.match(r"\s*(\w+)", block)
        if not name_m:
            continue
        entry = {"name": name_m.group(1)}
        for key in ("role", "workspace", "hermes_profile", "cli_alias"):
            m = re.search(rf"{key}:\s*(.+)", block)
            if m:
                entry[key] = m.group(1).strip()
        out.append(entry)
    return out


def _memory_snippet(agent: str, max_len: int = 240) -> str:
    path = ROOT / "agents" / agent / "MEMORY.md"
    if not path.is_file():
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    parts = [p.strip() for p in text.split("§") if p.strip()]
    if len(parts) > 1:
        snippet = parts[1].replace("\n", " ")[:max_len]
    else:
        snippet = text.replace("\n", " ")[:max_len]
    return snippet


def agents_data(activity_bundle: dict) -> dict:
    try:
        roster_yaml = _parse_registry_agents()
        act_agents = {a["agent_name"]: a for a in activity_bundle.get("agents", []) if "agent_name" in a}
        by_name = {a.get("name", "").lower(): a for a in activity_bundle.get("agents", [])}
        total_all = max(1, activity_bundle.get("stats", {}).get("total", 0))
        roster = []
        for key in PARTY:
            meta = AGENT_META[key]
            reg = next((r for r in roster_yaml if r.get("name", "").lower() == key or r.get("cli_alias") == key), {})
            act = by_name.get(key) or act_agents.get(key) or {}
            total = int(act.get("total") or 0)
            roster.append(
                {
                    "name": key,
                    "display": meta["display"],
                    "code": meta["code"],
                    "role": reg.get("role") or meta["role"],
                    "workspace": reg.get("workspace") or f"agents/{key}",
                    "hermes_profile": reg.get("hermes_profile") or key,
                    "memory_snippet": _memory_snippet(key),
                    "total": total,
                    "responses": total,
                    "completed": int(act.get("completed") or 0),
                    "failed": int(act.get("failed") or 0),
                    "last_task": act.get("last_task") or "",
                    "last_status": act.get("last_status") or "idle",
                    "last_seen": act.get("last_seen") or "",
                    "model": act.get("model") or "",
                    "response_share_pct": round(total / total_all * 100, 1),
                }
            )
        return {"roster": roster, "count": len(roster)}
    except Exception as exc:
        return {"roster": [], "count": 0, "error": str(exc)}


def _parse_simple_yaml_block(text: str) -> dict:
    data: dict = {}
    current_key = None
    indent_stack = []
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        m = re.match(r"^(\s*)([a-zA-Z0-9_]+):\s*(.*)$", line)
        if not m:
            if current_key and line.startswith("  "):
                data[current_key] = (data.get(current_key) or "") + line.strip() + "\n"
            continue
        indent, key, val = m.groups()
        val = val.strip()
        if val == "|" or val == ">":
            current_key = key
            data[key] = ""
            continue
        current_key = None
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        if val.isdigit():
            data[key] = int(val)
        else:
            try:
                data[key] = float(val) if "." in val and val.replace(".", "").isdigit() else val
            except ValueError:
                data[key] = val
    for k, v in list(data.items()):
        if isinstance(v, str):
            data[k] = v.strip()
    return data


def quests_data() -> dict:
    try:
        quests_dir = ROOT / "agents" / "hermes" / "content" / "quests"
        quests = []
        if not quests_dir.is_dir():
            return {"quests": [], "count": 0}
        for child in sorted(quests_dir.iterdir()):
            if not child.is_dir() or child.name.startswith("_"):
                continue
            qf = child / "quest.yaml"
            if not qf.is_file():
                continue
            raw = qf.read_text(encoding="utf-8", errors="replace")
            parsed = _parse_simple_yaml_block(raw)
            artifacts = {}
            for line in raw.splitlines():
                am = re.match(r"^\s{2}([a-z_]+):\s*(.+)$", line)
                if am and "/" in am.group(2):
                    artifacts[am.group(1)] = am.group(2).strip()
            quests.append(
                {
                    "slug": child.name,
                    "path": str(qf.relative_to(ROOT)).replace("\\", "/"),
                    "title": parsed.get("title") or child.name,
                    "status": parsed.get("status") or "unknown",
                    "target_gate": parsed.get("target_gate") or "",
                    "pwin": parsed.get("pwin"),
                    "created": parsed.get("created") or "",
                    "brief": (parsed.get("brief") or "")[:280],
                    "artifacts": artifacts,
                    "gate_progress": parsed.get("target_gate") or parsed.get("status") or "",
                }
            )
        quests.sort(key=lambda q: q.get("created") or "", reverse=True)
        return {"quests": quests, "count": len(quests)}
    except Exception as exc:
        return {"quests": [], "count": 0, "error": str(exc)}


def _title_from_md(text: str) -> str:
    m = re.match(r"^#\s+(.+)$", text, re.M)
    if m:
        return m.group(1).strip()[:120]
    return "Untitled"


def _validate_content_agent(agent: str) -> str:
    a = (agent or "").strip().lower()
    if a not in PARTY:
        raise ValueError("invalid agent")
    return a


def _validate_content_filename(filename: str) -> str:
    fn = (filename or "").strip()
    if not fn or "/" in fn or "\\" in fn or ".." in fn:
        raise ValueError("invalid filename")
    if not fn.lower().endswith(".md"):
        raise ValueError("markdown only")
    return fn


def _content_agent_dir(agent: str) -> Path:
    return ROOT / "agents" / _validate_content_agent(agent) / "content"


def content_list() -> list:
    docs = []
    for agent in PARTY:
        content_dir = ROOT / "agents" / agent / "content"
        if not content_dir.is_dir():
            continue
        for path in sorted(content_dir.glob("*.md")):
            if not path.is_file():
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
            except OSError:
                text = ""
            st = path.stat()
            docs.append(
                {
                    "agent": agent,
                    "filename": path.name,
                    "title": _title_from_md(text) if text else path.stem.replace("-", " ").title(),
                    "modified_at": datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat(),
                }
            )
    docs.sort(key=lambda d: d["modified_at"], reverse=True)
    return docs


def content_read(agent: str, filename: str) -> dict:
    agent = _validate_content_agent(agent)
    fn = _validate_content_filename(filename)
    path = _content_agent_dir(agent) / fn
    if not path.is_file():
        return {"ok": False, "error": "not found"}
    return {"text": path.read_text(encoding="utf-8", errors="replace")}


def content_save(agent: str, filename: str, body: bytes) -> dict:
    agent = _validate_content_agent(agent)
    fn = _validate_content_filename(filename)
    dest = _content_agent_dir(agent)
    dest.mkdir(parents=True, exist_ok=True)
    (dest / fn).write_bytes(body)
    return {"ok": True}


def content_delete(agent: str, filename: str) -> dict:
    agent = _validate_content_agent(agent)
    fn = _validate_content_filename(filename)
    path = _content_agent_dir(agent) / fn
    if not path.is_file():
        raise FileNotFoundError("not found")
    path.unlink()
    return {"ok": True}


def content_data(limit: int = 40) -> dict:
    try:
        docs = []
        for row in content_list()[:limit]:
            path = _content_agent_dir(row["agent"]) / row["filename"]
            rel = path.relative_to(ROOT).as_posix()
            preview = ""
            size = 0
            try:
                text = path.read_text(encoding="utf-8", errors="replace")
                preview = re.sub(r"\s+", " ", text[:400]).strip()
                size = path.stat().st_size
            except OSError:
                pass
            docs.append({**row, "path": rel, "preview": preview, "size": size})
        return {"docs": docs, "count": len(docs)}
    except Exception as exc:
        return {"docs": [], "count": 0, "error": str(exc)}


def cron_data() -> dict:
    try:
        jobs = []
        seen: set[str] = set()

        def add_job(name: str, schedule: str, detail: str, command: str, category: str = "hermes", job_id: str = "") -> None:
            key = f"{name}|{schedule}"
            if key in seen:
                return
            seen.add(key)
            jobs.append(
                {
                    "id": job_id or name,
                    "name": name,
                    "schedule": schedule,
                    "category": category,
                    "detail": detail,
                    "command": command,
                }
            )

        if HERMES_CRON_JOBS.is_file():
            try:
                raw = json.loads(HERMES_CRON_JOBS.read_text(encoding="utf-8"))
                for j in raw.get("jobs") or []:
                    if j.get("enabled") is False or j.get("state") == "paused":
                        continue
                    sched = j.get("schedule_display") or (j.get("schedule") or {}).get("expr") or ""
                    script = j.get("script") or ""
                    prompt = (j.get("prompt") or "")[:120]
                    cmd = script or prompt or "hermes cron job"
                    add_job(
                        str(j.get("name") or j.get("id") or "cron"),
                        str(sched),
                        f"Hermes cron · {cmd}"[:200],
                        str(cmd),
                        "hermes",
                        str(j.get("id") or ""),
                    )
            except (json.JSONDecodeError, OSError):
                pass

        if REGISTRY.is_file() and not jobs:
            text = REGISTRY.read_text(encoding="utf-8")
            m = re.search(r'log_cleanup_schedule:\s*["\']?([^"\']+)', text)
            name_m = re.search(r"log_cleanup_cron_job:\s*(\S+)", text)
            if m:
                add_job(
                    (name_m.group(1) if name_m else "log-cleanup"),
                    m.group(1).strip(),
                    "Permanent delete agent_logs rows older than 30 days",
                    "ariadne-cleanup-agent-logs.sh",
                    "hermes",
                )
        return {"jobs": jobs, "count": len(jobs)}
    except Exception as exc:
        return {"jobs": [], "count": 0, "error": str(exc)}


def _vault_safe_path(rel: str) -> Path | None:
    rel = (rel or "").replace("\\", "/").lstrip("/")
    if not rel or ".." in rel.split("/"):
        return None
    full = (VAULT_THREAD / rel).resolve()
    try:
        full.relative_to(VAULT_THREAD.resolve())
    except ValueError:
        return None
    if not full.is_file() or full.suffix.lower() not in {".md", ".markdown"}:
        return None
    return full


def vault_candidates_data() -> dict:
    zone = VAULT_THREAD / "generated-projections"
    items: list[dict] = []
    if not zone.is_dir():
        return {"candidates": [], "count": 0}
    for path in sorted(zone.glob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        title = path.stem.replace("-", " ")
        trust = "candidate"
        if text.startswith("---"):
            end = text.find("---", 3)
            if end > 0:
                block = text[3:end]
                for line in block.splitlines():
                    if line.strip().lower().startswith("name:"):
                        title = line.split(":", 1)[1].strip().strip('"')
                    if line.strip().lower().startswith("trust:"):
                        trust = line.split(":", 1)[1].strip().strip('"')
        rel = path.relative_to(VAULT_THREAD).as_posix()
        items.append(
            {
                "path": rel,
                "title": title,
                "trust": trust,
                "mtime": utc_now_iso(),
                "size": path.stat().st_size,
            }
        )
    return {"candidates": items, "count": len(items)}


def vault_read_data(rel: str) -> dict:
    full = _vault_safe_path(rel)
    if not full:
        return {"ok": False, "error": "invalid path"}
    return {"ok": True, "path": rel, "text": full.read_text(encoding="utf-8", errors="replace")}


VAULT_ZONES = (
    "entities",
    "foundation",
    "generated-projections",
    "global",
    "pursuits",
    "relationships",
)


def vault_tree_data() -> dict:
    """Shallow listing of vault markdown for MC browser (read-only)."""
    files: list[dict] = []
    for name in ("INDEX.md", "log.md"):
        p = VAULT_THREAD / name
        if p.is_file():
            files.append(
                {
                    "path": name,
                    "zone": "_root",
                    "title": p.stem.upper() if name == "INDEX.md" else "log",
                    "trust": "meta",
                }
            )
    for zone in VAULT_ZONES:
        zdir = VAULT_THREAD / zone
        if not zdir.is_dir():
            continue
        for path in sorted(zdir.rglob("*.md")):
            if path.name.upper() == "README.MD":
                continue
            rel = path.relative_to(VAULT_THREAD).as_posix()
            title = path.stem.replace("-", " ")
            trust = "trusted"
            if zone == "generated-projections" and path.name != "INDEX.md":
                trust = "candidate"
            if path.name == "INDEX.md":
                title = f"{zone} INDEX"
            files.append({"path": rel, "zone": zone, "title": title, "trust": trust})
    return {"ok": True, "files": files, "count": len(files), "zones": list(VAULT_ZONES)}


def vps_data() -> dict:
    """Stub host health until a VPS is wired; only activity DB size is live-local."""
    db_mb = 0.0
    if AGENT_LOG_DB.is_file():
        db_mb = AGENT_LOG_DB.stat().st_size / (1024 * 1024)
    return {
        "ok": True,
        "mode": "stub",
        "label": "No VPS — local Hermes desktop + xAI APIs",
        "cpu_pct": 12.0,
        "mem_pct": 24.0,
        "mem_used_mb": 3840.0,
        "mem_total_mb": 16384.0,
        "disk_pct": 18.0,
        "disk_used_gb": 58.0,
        "disk_total_gb": 512.0,
        "db_size_mb": round(db_mb, 2),
    }


def read_content_file(rel_path: str) -> dict:
    try:
        rel = rel_path.replace("\\", "/").lstrip("/")
        path = (ROOT / rel).resolve()
        if not str(path).startswith(str(ROOT.resolve())):
            return {"ok": False, "error": "invalid path"}
        if not path.is_file():
            return {"ok": False, "error": "not found"}
        return {"ok": True, "path": rel, "text": path.read_text(encoding="utf-8", errors="replace")}
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


def board_init() -> None:
    BOARD_DB.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(BOARD_DB)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            priority TEXT DEFAULT 'medium',
            notes TEXT DEFAULT '',
            source_key TEXT DEFAULT '',
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
        """
    )
    cols = {r[1] for r in conn.execute("PRAGMA table_info(tasks)").fetchall()}
    if "source_key" not in cols:
        conn.execute("ALTER TABLE tasks ADD COLUMN source_key TEXT DEFAULT ''")
    count = conn.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
    if count == 0:
        now = utc_now_iso()
        seeds = [
            ("Sync party profiles after MEMORY charter edits", "done", "high", "Hephaestus: scripts/sync_party_profiles.py after any agent MEMORY.md change."),
            ("Mission Control backend SSE + snapshot API", "in_progress", "high", "server.py on 127.0.0.1:51763 — activity, agents, quests, content."),
            ("Verify monthly agent-logs cleanup cron", "pending", "high", "Hermes job ariadne-agent-logs-cleanup · 0 3 1 * *"),
            ("Overwatch capture-loop quickstart doc", "pending", "medium", "Triggers: Run capture loop / Process new opp / /capture-loop"),
            ("Iris USAspending research playbook in content/", "pending", "medium", "NAICS + agency filters; handoff template to Clio"),
            ("Odysseus MS3 Yellow gate checklist template", "in_progress", "medium", "Shipley-aligned; store under agents/odysseus/content/"),
            ("Run hermes doctor on all five party profiles", "pending", "low", "Delegate Hephaestus; log in sync-log.md"),
            ("Thread Tavern content tab read-only previews", "done", "medium", "Walk agents/*/content; markdown preview in dashboard"),
        ]
        for title, status, priority, notes in seeds:
            tid = str(uuid.uuid4())
            conn.execute(
                "INSERT INTO tasks (id, title, status, priority, notes, source_key, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?)",
                (tid, title, status, priority, notes, "", now, now),
            )
    conn.commit()
    conn.close()


def board_list() -> list[dict]:
    board_init()
    conn = sqlite3.connect(BOARD_DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM tasks ORDER BY updated_at DESC, created_at DESC").fetchall()
    conn.close()
    return [dict(r) for r in rows]


def board_create(payload: dict) -> dict:
    board_init()
    source_key = (payload.get("source_key") or "").strip()
    if source_key:
        conn = sqlite3.connect(BOARD_DB)
        conn.row_factory = sqlite3.Row
        existing = conn.execute(
            "SELECT id FROM tasks WHERE source_key=? LIMIT 1", (source_key,)
        ).fetchone()
        conn.close()
        if existing:
            return {"ok": True, "id": existing["id"], "deduped": True}
    tid = str(uuid.uuid4())
    now = utc_now_iso()
    title = (payload.get("title") or "Untitled").strip()
    conn = sqlite3.connect(BOARD_DB)
    conn.execute(
        "INSERT INTO tasks (id, title, status, priority, notes, source_key, created_at, updated_at) VALUES (?,?,?,?,?,?,?,?)",
        (
            tid,
            title,
            payload.get("status") or "pending",
            payload.get("priority") or "medium",
            payload.get("notes") or "",
            source_key,
            now,
            now,
        ),
    )
    conn.commit()
    conn.close()
    return {"ok": True, "id": tid}


def board_update(task_id: str, payload: dict) -> dict:
    board_init()
    allowed = {"title", "status", "priority", "notes"}
    sets = []
    vals = []
    for k, v in payload.items():
        if k in allowed:
            sets.append(f"{k}=?")
            vals.append(v)
    if not sets:
        return {"ok": False, "error": "no fields"}
    sets.append("updated_at=?")
    vals.append(utc_now_iso())
    vals.append(task_id)
    conn = sqlite3.connect(BOARD_DB)
    cur = conn.execute(f"UPDATE tasks SET {', '.join(sets)} WHERE id=?", vals)
    conn.commit()
    conn.close()
    return {"ok": cur.rowcount > 0}


def board_delete(task_id: str) -> dict:
    board_init()
    conn = sqlite3.connect(BOARD_DB)
    cur = conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()
    return {"ok": cur.rowcount > 0}


def agent_os_data(agents: list, stats: dict, activity_by_day: list) -> dict:
    logs_mb = board_mb = 0.0
    if AGENT_LOG_DB.is_file():
        logs_mb = AGENT_LOG_DB.stat().st_size / (1024 * 1024)
    if BOARD_DB.is_file():
        board_mb = BOARD_DB.stat().st_size / (1024 * 1024)
    total = int(stats.get("total") or 0)
    completed = int(stats.get("completed") or 0)
    success_pct = round(100.0 * completed / total, 2) if total else 100.0
    party_totals = []
    now = datetime.now(timezone.utc)
    active = 0
    for name in PARTY:
        t = 0
        ls = ""
        for a in agents:
            if not isinstance(a, dict):
                continue
            an = str(a.get("name") or a.get("agent_name") or "").lower()
            if an == name:
                t = int(a.get("total") or a.get("responses") or 0)
                ls = str(a.get("last_seen") or "")
                break
        party_totals.append(t)
        try:
            seen = datetime.fromisoformat(ls.replace("Z", "+00:00"))
            if ls and (now - seen).total_seconds() <= 6 * 3600:
                active += 1
        except Exception:
            if t > 0:
                active += 1
    max_t = max(1, max(party_totals))
    response_rate_avg = round(sum(100.0 * x / max_t for x in party_totals) / 5.0, 2)
    responses_today = int(activity_by_day[-1].get("total") or 0) if activity_by_day else 0
    return {
        "response_rate_avg": response_rate_avg,
        "success_rate_pct": success_pct,
        "active_agents": active,
        "active_agents_pct": round(100.0 * active / 5, 2),
        "responses_today": responses_today,
        "db_logs_mb": round(logs_mb, 3),
        "db_board_mb": round(board_mb, 3),
        "db_total_mb": round(logs_mb + board_mb, 3),
        "server_uptime_seconds": round(time.time() - SERVER_START, 1),
    }


def build_snapshot() -> dict:
    snap = {"ok": True, "generated_at": datetime.now(timezone.utc).isoformat(), "project_root": str(ROOT)}
    try:
        snap["gateway"] = gateway_data()
    except Exception as exc:
        snap["gateway"] = {"ok": False, "error": str(exc)}
    try:
        act = activity_data()
        snap["activity"] = act.get("activity", [])
        snap["stats"] = act.get("stats", {})
        snap["activity_by_day"] = act.get("activity_by_day", [])
        snap["agents"] = act.get("agents", [])
    except Exception as exc:
        snap["activity"] = []
        snap["stats"] = {"error": str(exc)}
        snap["activity_by_day"] = []
        snap["agents"] = []
    try:
        agents_bundle = agents_data({"agents": snap.get("agents", []), "stats": snap.get("stats", {})})
        snap["agents_roster"] = agents_bundle.get("roster", [])
    except Exception as exc:
        snap["agents_roster"] = []
        snap["agents_roster_error"] = str(exc)
    try:
        snap["quests"] = quests_data()
    except Exception as exc:
        snap["quests"] = {"quests": [], "error": str(exc)}
    try:
        snap["content"] = content_data()
    except Exception as exc:
        snap["content"] = {"docs": [], "error": str(exc)}
    try:
        snap["cron"] = cron_data()
    except Exception as exc:
        snap["cron"] = {"jobs": [], "error": str(exc)}
    try:
        snap["board"] = {"tasks": board_list(), "total": len(board_list())}
    except Exception as exc:
        snap["board"] = {"tasks": [], "error": str(exc)}
    try:
        snap["vps"] = vps_data()
    except Exception as exc:
        snap["vps"] = {"ok": False, "error": str(exc)}
    board_total = int(snap.get("board", {}).get("total") or 0)
    snap["kanban"] = {"ok": True, "total": board_total}
    snap["sessions"] = {
        "ok": True,
        "exists": False,
        "count": len(snap.get("agents_roster") or PARTY),
        "totals": {"messages": 0, "input_tokens": 0, "cache_read_tokens": 0},
    }
    cron_jobs = snap.get("cron", {}).get("jobs") or []
    snap["crons"] = cron_jobs
    try:
        snap["agent_os"] = agent_os_data(
            snap.get("agents") or [],
            snap.get("stats") or {},
            snap.get("activity_by_day") or [],
        )
    except Exception as exc:
        snap["agent_os"] = {"error": str(exc)}
    snap["server_uptime_seconds"] = round(time.time() - SERVER_START, 1)
    return snap


def sse_broadcast():
    payload = json.dumps(build_snapshot(), default=str).encode("utf-8")
    with _sse_lock:
        dead = []
        for cond in _sse_clients:
            with cond:
                if getattr(cond, "_closed", False):
                    dead.append(cond)
                    continue
                cond._buffer = payload  # type: ignore
                cond.notify_all()
        for d in dead:
            _sse_clients.remove(d)


def sse_loop():
    while True:
        try:
            sse_broadcast()
        except Exception:
            pass
        time.sleep(5)


class Handler(BaseHTTPRequestHandler):
    server_version = "AriadneMissionControl/1.0"

    def log_message(self, fmt, *args):
        return

    def _send(self, code: int, body: bytes, content_type: str):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, code: int, obj):
        self._send(code, json.dumps(obj, default=str).encode("utf-8"), "application/json; charset=utf-8")

    def _read_json(self) -> dict:
        length = int(self.headers.get("Content-Length") or 0)
        if length <= 0:
            return {}
        return json.loads(self.rfile.read(length).decode("utf-8"))

    def _read_body(self) -> bytes:
        length = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(length) if length > 0 else b""

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        if path in ("/", "/index.html"):
            index = ROOT / "index.html"
            if index.is_file():
                self._send(200, index.read_bytes(), "text/html; charset=utf-8")
            else:
                self._send(404, b"index.html missing", "text/plain")
            return
        if path == "/api/snapshot":
            self._json(200, build_snapshot())
            return
        if path == "/api/board":
            self._json(200, board_list())
            return
        if path == "/api/content":
            qs = parse_qs(urlparse(self.path).query)
            rel = (qs.get("path") or [""])[0]
            if rel:
                out = read_content_file(rel)
                self._json(200 if out.get("ok") else 404, out)
                return
            self._json(200, content_list())
            return
        if path == "/api/content/read":
            qs = parse_qs(urlparse(self.path).query)
            agent = (qs.get("agent") or [""])[0]
            file = (qs.get("file") or [""])[0]
            try:
                out = content_read(agent, file)
                if out.get("ok") is False:
                    self._json(404, out)
                else:
                    self._json(200, out)
            except ValueError as exc:
                self._json(400, {"ok": False, "error": str(exc)})
            return
        if path == "/events":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream; charset=utf-8")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            cond = threading.Condition()
            cond._buffer = None  # type: ignore
            cond._closed = False  # type: ignore
            with _sse_lock:
                _sse_clients.append(cond)
            try:
                self.wfile.write(b": connected\n\n")
                self.wfile.flush()
                while True:
                    with cond:
                        if cond._closed:  # type: ignore
                            break
                        if cond._buffer is None:  # type: ignore
                            cond.wait(timeout=30)
                        buf = cond._buffer  # type: ignore
                        cond._buffer = None  # type: ignore
                    if buf:
                        self.wfile.write(b"event: snapshot\ndata: ")
                        self.wfile.write(buf)
                        self.wfile.write(b"\n\n")
                        self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError, OSError):
                pass
            finally:
                cond._closed = True  # type: ignore
                with cond:
                    cond.notify_all()
            return
        if path == "/api/cron":
            self._json(200, cron_data())
            return
        if path == "/api/vault/candidates":
            self._json(200, vault_candidates_data())
            return
        if path == "/api/vault/tree":
            self._json(200, vault_tree_data())
            return
        if path == "/api/vault/read":
            qs = parse_qs(urlparse(self.path).query)
            rel = (qs.get("path") or [""])[0]
            out = vault_read_data(rel)
            self._json(200 if out.get("ok") else 404, out)
            return
        self._send(404, b"not found", "text/plain")

    def do_POST(self):
        path = urlparse(self.path).path
        qs = parse_qs(urlparse(self.path).query)
        try:
            if path == "/api/board":
                self._json(201, board_create(self._read_json()))
                return
            if path == "/api/board/update":
                tid = (qs.get("id") or [""])[0]
                self._json(200, board_update(tid, self._read_json()))
                return
            if path == "/api/board/delete":
                tid = (qs.get("id") or [""])[0]
                self._json(200, board_delete(tid))
                return
            if path == "/api/content/save":
                agent = (qs.get("agent") or [""])[0]
                file = (qs.get("file") or [""])[0]
                self._json(200, content_save(agent, file, self._read_body()))
                return
            if path == "/api/content/delete":
                agent = (qs.get("agent") or [""])[0]
                file = (qs.get("file") or [""])[0]
                try:
                    self._json(200, content_delete(agent, file))
                except FileNotFoundError:
                    self._json(404, {"ok": False, "error": "not found"})
                return
        except ValueError as exc:
            self._json(400, {"ok": False, "error": str(exc)})
            return
        except Exception as exc:
            self._json(500, {"ok": False, "error": str(exc)})
            return
        self._send(404, b"not found", "text/plain")


def main():
    board_init()
    threading.Thread(target=sse_loop, daemon=True).start()
    ThreadingHTTPServer.allow_reuse_address = True
    try:
        httpd = ThreadingHTTPServer((HOST, PORT), Handler)
    except OSError as exc:
        print(
            f"Cannot bind {HOST}:{PORT}: {exc}",
            file=sys.stderr,
        )
        print(
            f"If Mission Control is already running, open http://{HOST}:{PORT}/",
            file=sys.stderr,
        )
        raise SystemExit(1) from exc
    print(f"Ariadne Mission Control http://{HOST}:{PORT}/")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down.")
        httpd.shutdown()


if __name__ == "__main__":
    main()