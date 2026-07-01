#!/usr/bin/env python3
"""Verify party workspaces and detect phantom MSYS path trees. Exit 1 on problems."""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
CANONICAL = Path(r"C:/Users/benma/ariadnes-thread-os")
PHANTOM = Path(r"C:/c/Users/benma")

AGENTS = ("hermes", "iris", "clio", "odysseus", "hephaestus")
REQUIRED = ("SOUL.md", "IDENTITY.md", "USER.md", "AGENTS.md", "MEMORY.md")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    if PROJECT_ROOT.resolve() != CANONICAL.resolve():
        warnings.append(f"script root {PROJECT_ROOT} != canonical {CANONICAL}")

    if PHANTOM.is_dir():
        warnings.append(
            f"phantom MSYS tree exists: {PHANTOM} — safe to remove after confirming no needed files"
        )

    mc = PROJECT_ROOT / "index.html"
    srv = PROJECT_ROOT / "server.py"
    for p in (mc, srv):
        if not p.is_file():
            errors.append(f"missing mission control file {p}")

    bad_roots = [
        Path(r"C:/c/Users/benma/ariadnes-thread-os"),
        PROJECT_ROOT / "c" / "Users" / "benma" / "ariadnes-thread-os",
    ]
    for bad in bad_roots:
        if bad.is_dir():
            warnings.append(
                f"phantom project copy under wrong path: {bad} — do not edit; remove via Hephaestus maintenance"
            )

    for name in AGENTS:
        ws = PROJECT_ROOT / "agents" / name
        for f in REQUIRED:
            p = ws / f
            if not p.is_file():
                errors.append(f"missing {p}")
        if not (ws / "content").is_dir():
            errors.append(f"missing {ws / 'content'}")

    if errors:
        for e in errors:
            print(f"ERROR {e}", file=sys.stderr)
        return 1

    for w in warnings:
        print(f"WARN {w}", file=sys.stderr)

    print(f"OK party workspaces under {PROJECT_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())