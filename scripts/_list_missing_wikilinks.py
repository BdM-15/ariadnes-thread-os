#!/usr/bin/env python3
"""One-off helper — list missing wikilinks (same heuristic as vault_lint)."""
import re
from pathlib import Path

vault = Path(__file__).resolve().parents[1] / "knowledge" / "thread"
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
md_files = [p for p in vault.rglob("*.md") if ".obsidian" not in p.parts]
names = {p.stem for p in md_files}
for p in md_files:
    names.add(p.relative_to(vault).with_suffix("").as_posix().split("/")[-1])
links: list[tuple[str, Path]] = []
for p in md_files:
    for m in WIKILINK.finditer(p.read_text(encoding="utf-8", errors="replace")):
        links.append((m.group(1).strip(), p))
missing = sorted(
    {ln for ln, _ in links if ln not in names and not (vault / f"{ln}.md").exists()}
)
for m in missing:
    refs = [str(p.relative_to(vault)) for ln, p in links if ln == m][:2]
    print(f"{m}\t{refs}")
print("TOTAL", len(missing))