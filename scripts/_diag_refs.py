#!/usr/bin/env python3
"""Find refs for specific missing links."""
import re
from pathlib import Path

vault = Path(__file__).resolve().parents[1] / "knowledge"
W = re.compile(r"\[\[([^\]|#]+)")
targets = {"create a link", "wikilinks", "army-logcap-funding-office"}
for p in vault.rglob("*.md"):
    if ".obsidian" in p.parts:
        continue
    t = p.read_text(encoding="utf-8", errors="replace")
    for m in W.finditer(t):
        if m.group(1).strip() in targets:
            print(p.relative_to(vault), m.group(1))