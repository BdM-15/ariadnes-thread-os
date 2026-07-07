#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict

vault = Path(__file__).resolve().parents[1] / "knowledge"
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
TRUST = re.compile(r"^trust:\s*(.+)$", re.MULTILINE)

def strip_fence(t):
    return FENCE.sub("", t)

md_files = [p for p in vault.rglob("*.md") if ".obsidian" not in p.parts]
stems = set()
for p in md_files:
    stems.add(p.stem)
    rel = p.relative_to(vault).with_suffix("").as_posix()
    stems.add(rel.split("/")[-1])
    stems.add(rel)

def resolves(link):
    link = link.strip()
    if link in stems:
        return True
    if (vault / f"{link}.md").is_file():
        return True
    n = link.replace("\\", "/")
    if (vault / f"{n}.md").is_file():
        return True
    return False

refs = defaultdict(list)
for p in md_files:
    text = strip_fence(p.read_text(encoding="utf-8", errors="replace"))
    for m in WIKILINK.finditer(text):
        ln = m.group(1).strip()
        if not resolves(ln):
            refs[ln].append(str(p.relative_to(vault)))

missing = sorted(refs.keys())
cap_missing = {k: v for k, v in refs.items() if any("domain_intel/capabilities" in x for x in v)}
print("TOTAL", len(missing))
print("CAP_ZONE_REFS", len(cap_missing))
for k in sorted(cap_missing):
    print(k, "->", cap_missing[k][:2])
print("---ALL---")
for k in missing:
    print(k)