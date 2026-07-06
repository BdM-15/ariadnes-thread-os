#!/usr/bin/env python3
"""Write stdin to a repo-relative path under project root (Hermes write_file fallback)."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def resolve_relative(raw: str) -> Path:
    s = (raw or "").strip().replace("\\", "/")
    if not s:
        raise ValueError("empty path")
    if s.startswith("/c/") or s.startswith("/C/"):
        raise ValueError(f"reject MSYS phantom path: {raw!r} — use repo-relative or C:/Users/...")
    if s.startswith("~/"):
        raise ValueError("use repo-relative path, not ~")
    p = Path(s)
    if p.is_absolute():
        raise ValueError(f"reject absolute path: {raw!r} — use repo-relative under ariadnes-thread-os")
    out = (ROOT / p).resolve()
    try:
        out.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise ValueError(f"path escapes project root: {out}") from exc
    return out


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: safe_repo_write.py <repo-relative-path>", file=sys.stderr)
        return 2
    try:
        dest = resolve_relative(sys.argv[1])
    except ValueError as e:
        print(f"ERROR {e}", file=sys.stderr)
        return 1
    data = sys.stdin.buffer.read()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    print(dest.as_posix())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
