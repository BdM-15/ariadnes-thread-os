#!/usr/bin/env python3
import re
from pathlib import Path
vault = Path(__file__).resolve().parents[1] / "knowledge"
W = re.compile(r"\[\[([^\]|#]+)")
for p in vault.rglob("*.md"):
    if ".obsidian" in p.parts: continue
    t = p.read_text(encoding="utf-8", errors="replace")
    for m in W.finditer(t):
        if m.group(1).strip() in ("department-of-the-army", "slug"):
            print(p.relative_to(vault), m.group(1))