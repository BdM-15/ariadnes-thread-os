#!/usr/bin/env python3
"""Normalize a write path to an absolute path under the project root (file mutation guard)."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path("C:/Users/benma/ariadnes-thread-os").resolve()


def normalize(raw: str) -> Path:
    s = (raw or "").strip().replace("\\", "/")
    if not s:
        raise ValueError("empty path")
    if s.startswith("/c/") or s.startswith("/C/"):
        s = "C:" + s[2:]
    if s.startswith("~/"):
        s = str(Path.home() / s[2:])
    p = Path(s)
    if not p.is_absolute():
        p = (ROOT / p).resolve()
    else:
        p = p.resolve()
    try:
        p.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError(f"path escapes project root: {p}") from exc
    return p


def main() -> int:
    ap = argparse.ArgumentParser(description="Normalize write path for Hermes write_file/patch")
    ap.add_argument("path", help="Relative, absolute, or MSYS /c/Users/... path")
    ap.add_argument("--check", action="store_true", help="Exit 1 if path is outside root")
    args = ap.parse_args()
    try:
        out = normalize(args.path)
        print(out.as_posix())
        return 0
    except ValueError as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())