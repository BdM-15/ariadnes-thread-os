#!/usr/bin/env python3
"""Weekly vault lint — orphans, candidates, zone counts. Appends summary to log.md."""
from __future__ import annotations

import argparse
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VAULT = REPO_ROOT / "knowledge" / "thread"
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
TRUST = re.compile(r"^trust:\s*(\S+)", re.MULTILINE)


def lint(vault: Path, append_log: bool) -> str:
    if not vault.is_dir():
        return f"ERROR: vault missing: {vault}"

    md_files = [p for p in vault.rglob("*.md") if ".obsidian" not in p.parts]
    names = {p.stem for p in md_files}
    names.update(p.relative_to(vault).with_suffix("").as_posix().split("/")[-1] for p in md_files)

    links: list[str] = []
    trust_counts: Counter[str] = Counter()
    candidates = 0
    for p in md_files:
        text = p.read_text(encoding="utf-8", errors="replace")
        for m in TRUST.finditer(text):
            trust_counts[m.group(1)] += 1
        if "generated-projections" in p.as_posix() and p.name != "INDEX.md":
            candidates += 1
        for m in WIKILINK.finditer(text):
            links.append(m.group(1).strip())

    missing = sorted({ln for ln in links if ln not in names and not (vault / f"{ln}.md").exists()})

    zones = Counter()
    for p in md_files:
        rel = p.relative_to(vault).parts
        zones[rel[0] if rel else "?"] += 1

    lines = [
        f"Vault lint {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}",
        f"  markdown files: {len(md_files)}",
        f"  zone counts: {dict(zones)}",
        f"  trust frontmatter hits: {dict(trust_counts)}",
        f"  projection files (non-INDEX): {candidates}",
        f"  unresolved wikilinks (heuristic): {len(missing)}",
    ]
    if missing[:15]:
        lines.append("  sample missing: " + ", ".join(missing[:15]))

    report = "\n".join(lines)
    if append_log:
        log = vault / "log.md"
        if log.exists():
            with log.open("a", encoding="utf-8") as f:
                f.write(f"\n```\n{report}\n```\n")
    return report


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    ap.add_argument("--append-log", action="store_true", default=True)
    ap.add_argument("--no-append-log", action="store_false", dest="append_log")
    args = ap.parse_args()
    print(lint(args.vault, args.append_log))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())