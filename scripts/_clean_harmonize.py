#!/usr/bin/env python3
"""Strip ANSI junk from harmonize_h1_h2.py if present."""
from pathlib import Path
p = Path(__file__).resolve().parent / "harmonize_h1_h2.py"
raw = p.read_bytes()
# drop ESC sequences
clean = bytes(b for b in raw if b != 0x1B)
text = clean.decode("utf-8", errors="replace")
# remove any leftover CSI fragments
import re
text = re.sub(r"\[[0-9;]*[A-Za-z]", "", text)
text = text.rstrip() + "\n"
if not text.endswith("raise SystemExit(main())\n"):
    lines = text.splitlines()
    while lines and "raise SystemExit" not in lines[-1]:
        lines.pop()
    if lines:
        lines[-1] = "    raise SystemExit(main())"
    text = "\n".join(lines) + "\n"
p.write_text(text, encoding="utf-8", newline="\n")
print("cleaned", len(text))