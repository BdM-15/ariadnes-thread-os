#!/usr/bin/env python3
"""Set all five capture OS Hermes profiles terminal.cwd to project root (fixes relative path mutations)."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ROOT = "C:/Users/benma/ariadnes-thread-os"
PROFILES = (
    "ariadne-guildmaster",
    "iris",
    "clio",
    "odysseus",
    "hephaestus",
)


def main() -> int:
    if Path(r"C:/Users/benma/ariadnes-thread-os").resolve() != PROJECT_ROOT.resolve():
        print(f"WARN project root mismatch: {PROJECT_ROOT}", file=sys.stderr)
    err = 0
    for profile in PROFILES:
        r = subprocess.run(
            ["hermes", "-p", profile, "config", "set", "terminal.cwd", ROOT],
            capture_output=True,
            text=True,
            timeout=60,
        )
        if r.returncode != 0:
            print(f"ERROR {profile}: {r.stderr or r.stdout}", file=sys.stderr)
            err = 1
        else:
            print(f"OK {profile} terminal.cwd -> {ROOT}")
    return err


if __name__ == "__main__":
    raise SystemExit(main())