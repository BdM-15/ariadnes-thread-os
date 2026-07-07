#!/usr/bin/env bash
# Log a capture-party task to agents/_shared/agent-logs.db
# Usage: log-task-local.sh <agent_name> <task_description> <status> [model_used]
#   agent_name: hermes | iris | clio | odysseus | hephaestus
#   status: completed | failed

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DB_PATH="${SCRIPT_DIR}/agent-logs.db"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

AGENT_NAME="${1:?agent_name required (hermes|iris|clio|odysseus|hephaestus)}"
TASK_DESC="${2:?task_description required}"
STATUS="${3:?status required (completed|failed)}"
MODEL_OVERRIDE="${4:-}"

case "${AGENT_NAME}" in
  hermes|iris|clio|odysseus|hephaestus) ;;
  *) echo "error: invalid agent_name '${AGENT_NAME}'" >&2; exit 1 ;;
esac

case "${STATUS}" in
  completed|failed) ;;
  *) echo "error: invalid status '${STATUS}' (use completed|failed)" >&2; exit 1 ;;
esac

export DB_PATH AGENT_NAME TASK_DESC STATUS MODEL_OVERRIDE PROJECT_ROOT

python - <<'PY'
import os
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

DB_PATH = os.environ["DB_PATH"]
AGENT_NAME = os.environ["AGENT_NAME"]
TASK_DESC = os.environ["TASK_DESC"]
STATUS = os.environ["STATUS"]
MODEL_OVERRIDE = os.environ.get("MODEL_OVERRIDE", "").strip()
PROJECT_ROOT = Path(os.environ["PROJECT_ROOT"])

PROFILE_BY_AGENT = {
    "hermes": "minos",
    "iris": "iris",
    "clio": "clio",
    "odysseus": "odysseus",
    "hephaestus": "hephaestus",
}


def detect_model(agent: str) -> str | None:
    if MODEL_OVERRIDE:
        return MODEL_OVERRIDE
    profile = PROFILE_BY_AGENT.get(agent)
    if not profile:
        return None
    home = Path.home()
    candidates = [
        home / "AppData" / "Local" / "hermes" / "profiles" / profile / "config.yaml",
        home / ".hermes" / "profiles" / profile / "config.yaml",
    ]
    cfg_path = next((p for p in candidates if p.is_file()), None)
    if not cfg_path:
        return None
    text = cfg_path.read_text(encoding="utf-8", errors="replace")
    if yaml:
        try:
            data = yaml.safe_load(text) or {}
            block = data.get("model")
            if isinstance(block, dict):
                default = block.get("default") or block.get("name")
                provider = block.get("provider") or ""
                if isinstance(default, str) and default.strip():
                    d = default.strip()
                    if provider and provider not in d:
                        return f"{provider}/{d}" if "/" not in d else d
                    return d
            if isinstance(block, str) and block.strip():
                return block.strip()
        except Exception:
            pass
    # fallback: model.default in flat scan
    in_model = False
    for line in text.splitlines():
        s = line.strip()
        if s == "model:":
            in_model = True
            continue
        if in_model:
            if s.startswith("default:"):
                return s.split(":", 1)[1].strip().strip("'\"")
            if s and not s[0].isspace() and ":" in s and not s.startswith("default:"):
                if not line.startswith(" "):
                    in_model = False
    return None


def ensure_schema(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS agent_logs (
            id TEXT PRIMARY KEY,
            agent_name TEXT NOT NULL,
            task_description TEXT NOT NULL,
            model_used TEXT,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_agent_logs_created ON agent_logs(created_at DESC)"
    )
    conn.execute(
        "CREATE INDEX IF NOT EXISTS idx_agent_logs_agent ON agent_logs(agent_name)"
    )
    conn.commit()


row_id = str(uuid.uuid4())
created_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
model_used = detect_model(AGENT_NAME)

Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(DB_PATH)
try:
    ensure_schema(conn)
    conn.execute(
        """
        INSERT INTO agent_logs (id, agent_name, task_description, model_used, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (row_id, AGENT_NAME, TASK_DESC, model_used, STATUS, created_at),
    )
    conn.commit()
finally:
    conn.close()

print(f"OK logged task id={row_id}")
print(f"  db: {DB_PATH}")
print(f"  agent: {AGENT_NAME}")
print(f"  status: {STATUS}")
print(f"  model_used: {model_used or '(none)'}")
print(f"  created_at: {created_at}")
print(f"  project_root: {PROJECT_ROOT}")
PY