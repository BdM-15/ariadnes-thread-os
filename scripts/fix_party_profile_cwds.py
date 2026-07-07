#!/usr/bin/env python3
"""Set terminal.cwd to project root in all five capture profiles."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = "C:/Users/benma/ariadnes-thread-os"
PROFILES = ("minos", "iris", "clio", "odysseus", "hephaestus")
HERMES = Path.home() / "AppData/Local/hermes/profiles"


def fix_config(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    new, n = re.subn(
        r"(?m)^(\s*cwd:\s*).*$",
        rf"\g<1>{ROOT}",
        text,
        count=1,
    )
    if n == 0:
        return False
    if new != text:
        path.write_text(new, encoding="utf-8")
    return True


def main() -> int:
    ok = 0
    for name in PROFILES:
        cfg = HERMES / name / "config.yaml"
        if not cfg.is_file():
            print(f"SKIP missing {cfg}", file=sys.stderr)
            continue
        if fix_config(cfg):
            print(f"OK {name} cwd -> {ROOT}")
            ok += 1
        else:
            print(f"WARN no cwd line updated in {cfg}", file=sys.stderr)
    return 0 if ok == len(PROFILES) else 1


if __name__ == "__main__":
    raise SystemExit(main())