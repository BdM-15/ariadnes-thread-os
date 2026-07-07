#!/usr/bin/env python3
"""Idempotently set WIKI_PATH and OBSIDIAN_VAULT_PATH in ~/.hermes/.env."""
from __future__ import annotations

import re
import sys
from pathlib import Path

WIKI = "C:/Users/benma/ariadnes-thread-os/knowledge"
KEYS = ("WIKI_PATH", "OBSIDIAN_VAULT_PATH")


def main() -> int:
    env_path = Path.home() / ".hermes" / ".env"
    env_path.parent.mkdir(parents=True, exist_ok=True)
    updates = {k: WIKI for k in KEYS}
    text = env_path.read_text(encoding="utf-8") if env_path.is_file() else ""
    lines = text.splitlines()
    out: list[str] = []
    seen: set[str] = set()
    for line in lines:
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)=", line)
        if m and m.group(1) in updates:
            k = m.group(1)
            out.append(f"{k}={updates[k]}")
            seen.add(k)
        else:
            out.append(line)
    for k in KEYS:
        if k not in seen:
            out.append(f"{k}={updates[k]}")
    new_text = "\n".join(out).rstrip() + "\n"
    env_path.write_text(new_text, encoding="utf-8")
    for k in KEYS:
        ok = any(l.startswith(f"{k}=") and WIKI in l for l in new_text.splitlines())
        print(f"{'OK' if ok else 'FAIL'} {k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())