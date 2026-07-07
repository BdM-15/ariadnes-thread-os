#!/usr/bin/env python3
"""Deterministic vault page schema lint — hard (block save) vs soft (Clio harmonize)."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VAULT = REPO_ROOT / "knowledge"

FM_BLOCK = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
TRUST_LINE = re.compile(r"^trust:\s*(\S+)", re.MULTILINE)
ID_LINE = re.compile(r"^id:\s*(\S+)", re.MULTILINE)
NAME_LINE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
CITATIONS_LINE = re.compile(r"^citations:\s*(.+)$", re.MULTILINE)
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)

HARD_CODES = frozenset(
    {
        "NO_FRONTMATTER",
        "INVALID_YAML",
        "MISSING_TRUST",
        "TRUST_ESCALATION",
        "ID_CHANGED_TRUSTED",
    }
)


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = FM_BLOCK.match(text)
    if not m:
        return {}, text
    body = text[m.end() :]
    meta: dict[str, str] = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip().lower()] = v.strip().strip('"').strip("'")
    return meta, body


def _strip_fenced(text: str) -> str:
    return FENCE.sub("", text)


def _wikilink_resolves(vault: Path, link: str, stems: set[str]) -> bool:
    link = link.strip()
    if link in stems:
        return True
    normalized = link.replace("\\", "/")
    if (vault / f"{normalized}.md").is_file():
        return True
    if (vault / f"{link}.md").is_file():
        return True
    return False


def _zone_for_rel(rel: str) -> str:
    parts = rel.replace("\\", "/").split("/")
    return parts[0] if len(parts) > 1 else "_root"


def lint_file(
    vault: Path,
    rel: str,
    *,
    old_text: str | None = None,
    new_text: str | None = None,
    all_ids: Counter[str] | None = None,
    stems: set[str] | None = None,
) -> dict:
    path = vault / rel
    text = new_text if new_text is not None else path.read_text(encoding="utf-8", errors="replace")
    hard: list[dict] = []
    soft: list[dict] = []

    meta, body = _parse_frontmatter(text)
    if not meta:
        hard.append({"code": "NO_FRONTMATTER", "message": "YAML frontmatter required"})
        return {"hard": hard, "soft": soft}

    trust = (meta.get("trust") or "").lower()
    if not trust:
        hard.append({"code": "MISSING_TRUST", "message": "trust: required in frontmatter"})
    if trust == "trusted" and old_text is not None:
        old_meta, _ = _parse_frontmatter(old_text)
        if (old_meta.get("trust") or "").lower() != "trusted":
            hard.append(
                {
                    "code": "TRUST_ESCALATION",
                    "message": "trust: trusted only via promote_vault_candidate.py",
                }
            )
        old_id = (old_meta.get("id") or "").strip()
        new_id = (meta.get("id") or "").strip()
        if old_id and new_id and old_id != new_id:
            hard.append({"code": "ID_CHANGED_TRUSTED", "message": "id is immutable on trusted pages"})

    if not (meta.get("id") or "").strip():
        soft.append({"code": "MISSING_ID", "message": "id: recommended in frontmatter"})

    if not (meta.get("name") or "").strip():
        soft.append({"code": "MISSING_NAME", "message": "name: recommended in frontmatter"})

    zone = _zone_for_rel(rel)
    if zone == "generated-projections" and trust == "candidate":
        if not CITATIONS_LINE.search(text):
            soft.append(
                {
                    "code": "MISSING_CITATIONS_CANDIDATE",
                    "message": "citations: recommended for candidate pages",
                }
            )
    elif zone in ("entities", "global", "pursuits", "relationships") and trust == "candidate":
        soft.append(
            {
                "code": "ZONE_TRUST_MISMATCH",
                "message": f"candidate trust unusual in zone {zone}",
            }
        )

    page_id = (meta.get("id") or "").strip()
    if page_id and all_ids is not None and all_ids[page_id] > 1:
        soft.append({"code": "DUPLICATE_ID", "message": f"duplicate id: {page_id}"})

    if stems is not None:
        scan = _strip_fenced(body)
        for m in WIKILINK.finditer(scan):
            ln = m.group(1).strip()
            if not _wikilink_resolves(vault, ln, stems):
                soft.append(
                    {"code": "UNRESOLVED_WIKILINK", "message": f"unresolved wikilink: [[{ln}]]"}
                )

    return {"hard": hard, "soft": soft}


def lint_vault(vault: Path, *, rel: str | None = None, old_text: str | None = None, new_text: str | None = None) -> dict:
    if not vault.is_dir():
        return {"ok": False, "error": f"vault missing: {vault}", "hard": [], "soft": []}

    md_files = [p for p in vault.rglob("*.md") if ".obsidian" not in p.parts]
    stems: set[str] = set()
    ids: Counter[str] = Counter()
    for p in md_files:
        r = p.relative_to(vault).with_suffix("").as_posix()
        stems.add(r)
        stems.add(r.split("/")[-1])
        stems.add(p.stem)
        t = p.read_text(encoding="utf-8", errors="replace")
        im = ID_LINE.search(t)
        if im:
            ids[im.group(1).strip().strip('"').strip("'")] += 1

    if rel:
        out = lint_file(vault, rel, old_text=old_text, new_text=new_text, all_ids=ids, stems=stems)
        out["ok"] = not out["hard"]
        return out

    hard: list[dict] = []
    soft: list[dict] = []
    for p in md_files:
        r = p.relative_to(vault).as_posix()
        one = lint_file(vault, r, all_ids=ids, stems=stems)
        hard.extend(one["hard"])
        soft.extend(one["soft"])
    return {"ok": not hard, "hard": hard, "soft": soft, "file_count": len(md_files)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    ap.add_argument("--path", default="", help="Vault-relative .md path for single-file lint")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fail-on-hard", action="store_true")
    ap.add_argument("--fail-on-soft", action="store_true")
    args = ap.parse_args()
    rel = (args.path or "").replace("\\", "/").lstrip("/")
    if rel:
        out = lint_vault(args.vault, rel=rel)
    else:
        out = lint_vault(args.vault)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        for h in out.get("hard", []):
            print(f"HARD {h['code']}: {h['message']}")
        for s in out.get("soft", []):
            print(f"SOFT {s['code']}: {s['message']}")
    if args.fail_on_hard and out.get("hard"):
        return 2
    if args.fail_on_soft and out.get("soft"):
        return 3
    return 0 if out.get("ok", True) else 2


if __name__ == "__main__":
    sys.exit(main())