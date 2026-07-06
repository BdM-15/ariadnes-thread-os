#!/usr/bin/env python3
"""One-off: zip C:/c/Users/benma phantom tree and remove it."""
from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

PHANTOM = Path("C:/c/Users/benma")
OUT = Path(__file__).resolve().parents[1] / "agents/_shared/backups/phantom-c-users-20260705.zip"


def main() -> int:
    if not PHANTOM.exists():
        print("SKIP no phantom tree")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    files = [p for p in PHANTOM.rglob("*") if p.is_file()]
    if files:
        with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in files:
                zf.write(p, p.relative_to(PHANTOM.parent))
        print(f"OK backup {OUT} ({len(files)} files)")
    else:
        print("SKIP empty phantom tree")
    shutil.rmtree(PHANTOM)
    print(f"OK removed {PHANTOM}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())