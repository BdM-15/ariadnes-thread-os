#!/usr/bin/env python3
"""Promote a vault candidate to a trusted write zone (doc 02 v1).

Requires explicit Overwatch path + Odysseus citation gate (operator confirms).
Does not auto-promote.

Example:
  python scripts/promote_vault_candidate.py \\
    --candidate generated-projections/eden-edge-computing-candidate.md \\
    --dest global/domain_intel/capabilities/eden.md \\
    --reviewed-by overwatch \\
    --review-id $(uuidgen)
"""
from __future__ import annotations

import argparse
import re
import shutil
import uuid
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VAULT = REPO_ROOT / "knowledge"

WRITE_PREFIXES = (
    "entities/agencies/",
    "entities/competitors/",
    "entities/company/",
    "global/domain_intel/",
    "global/global_wiki/",
    "pursuits/",
    "relationships/",
)

CANDIDATE_PREFIX = "generated-projections/"
ARCHIVE_DIR = "generated-projections/archived/"

TRUST_LINE = re.compile(r"^trust:\s*.+$", re.MULTILINE)
CITATIONS_LINE = re.compile(r"^citations:\s*.+$", re.MULTILINE)


def _vault_rel(vault: Path, path: Path) -> str:
    return path.relative_to(vault).as_posix()


def _assert_write_zone(dest_rel: str) -> None:
    if dest_rel.startswith(CANDIDATE_PREFIX):
        raise SystemExit("ERROR: dest must be a trusted write zone, not generated-projections/")
    if not any(dest_rel.startswith(p) for p in WRITE_PREFIXES):
        raise SystemExit(
            f"ERROR: dest not in write zones. Allowed prefixes: {', '.join(WRITE_PREFIXES)}"
        )


def _read_candidate(vault: Path, candidate_rel: str) -> tuple[Path, str]:
    cand = vault / candidate_rel
    if not cand.is_file():
        raise SystemExit(f"ERROR: candidate missing: {cand}")
    if not candidate_rel.startswith(CANDIDATE_PREFIX) or candidate_rel.endswith("/INDEX.md"):
        raise SystemExit("ERROR: --candidate must be a file under generated-projections/")
    text = cand.read_text(encoding="utf-8")
    if not re.search(r"^trust:\s*candidate\s*$", text, re.MULTILINE):
        raise SystemExit("ERROR: candidate must have trust: candidate in frontmatter")
    if not CITATIONS_LINE.search(text):
        raise SystemExit("ERROR: Odysseus gate — citations: frontmatter required")
    return cand, text


def _promote_frontmatter(text: str, reviewed_by: str, review_id: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    text = TRUST_LINE.sub("trust: trusted", text, count=1)
    if not re.search(r"^reviewed_by:", text, re.MULTILINE):
        text = text.replace("trust: trusted", f"trust: trusted\nreviewed_by: {reviewed_by}", 1)
    if not re.search(r"^reviewed_at:", text, re.MULTILINE):
        text = re.sub(
            r"(^reviewed_by:.*$)",
            rf"\1\nreviewed_at: {now}",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    if not re.search(r"^review_id:", text, re.MULTILINE):
        text = re.sub(
            r"(^reviewed_at:.*$)",
            rf"\1\nreview_id: {review_id}",
            text,
            count=1,
            flags=re.MULTILINE,
        )
    return text


def _append_log(vault: Path, line: str) -> None:
    log = vault / "log.md"
    with log.open("a", encoding="utf-8") as f:
        f.write(line)


def promote(
    vault: Path,
    candidate_rel: str,
    dest_rel: str,
    reviewed_by: str,
    review_id: str,
    dry_run: bool,
) -> str:
    _assert_write_zone(dest_rel)
    cand, text = _read_candidate(vault, candidate_rel)
    dest = vault / dest_rel
    promoted = _promote_frontmatter(text, reviewed_by, review_id)

    if dest.exists():
        raise SystemExit(f"ERROR: dest already exists (no overwrite): {dest}")

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    log_line = (
        f"\n## [{stamp}] promote | {_vault_rel(vault, cand)} → {dest_rel} "
        f"| review:{review_id} | by:{reviewed_by}\n"
    )

    if dry_run:
        return (
            f"[dry-run] would write {dest}\n"
            f"[dry-run] would archive {cand.name}\n"
            f"[dry-run] log:{log_line.strip()}"
        )

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(promoted, encoding="utf-8")

    archive_root = vault / ARCHIVE_DIR
    archive_root.mkdir(parents=True, exist_ok=True)
    archived = archive_root / f"{cand.stem}-promoted-{datetime.now(timezone.utc).strftime('%Y%m%d')}.md"
    shutil.move(str(cand), str(archived))

    _append_log(vault, log_line)
    return f"OK promoted → {dest_rel}\nArchived candidate → {_vault_rel(vault, archived)}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Promote vault candidate to trusted write zone")
    ap.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    ap.add_argument("--candidate", required=True, help="Path under knowledge/ (vault root)")
    ap.add_argument("--dest", required=True, help="Trusted destination .md path under vault")
    ap.add_argument("--reviewed-by", default="overwatch")
    ap.add_argument("--review-id", default="", help="UUID; generated if omitted")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    review_id = args.review_id or str(uuid.uuid4())
    cand = args.candidate.replace("\\", "/").lstrip("/")
    dest = args.dest.replace("\\", "/").lstrip("/")
    if not dest.endswith(".md"):
        raise SystemExit("ERROR: --dest must end with .md")

    print(
        promote(
            args.vault,
            cand,
            dest,
            args.reviewed_by,
            review_id,
            args.dry_run,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())