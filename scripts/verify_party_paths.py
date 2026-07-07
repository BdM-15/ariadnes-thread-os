#!/usr/bin/env python3
"""Verify party write paths: project root, phantom tree, profile terminal.cwd."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = Path("C:/Users/benma/ariadnes-thread-os")
HERMES_PROFILES = Path.home() / "AppData/Local/hermes/profiles"
BINDINGS = {
    "minos": "hermes",
    "iris": "iris",
    "clio": "clio",
    "odysseus": "odysseus",
    "hephaestus": "hephaestus",
}


def main() -> int:
    errors: list[str] = []
    if ROOT.resolve() != EXPECTED.resolve():
        errors.append(f"Run from project root (got {ROOT})")

    phantom = Path("C:/c/Users/benma")
    if phantom.exists():
        errors.append(f"Phantom tree exists (bad writes): {phantom} — do not edit; delete after backup")

    for profile, agent in BINDINGS.items():
        cfg = HERMES_PROFILES / profile / "config.yaml"
        if not cfg.is_file():
            errors.append(f"Missing profile config: {cfg}")
            continue
        text = cfg.read_text(encoding="utf-8", errors="replace")
        if "ariadnes-thread-os" not in text:
            errors.append(f"{profile}: terminal.cwd may not point at thread-os")
        if "ariadne-capture-party" in text or "ariadne-capform" in text:
            errors.append(f"{profile}: stale cwd in config.yaml — run scripts/fix_party_profile_cwds.py")

    ws = ROOT / "agents" / "hermes" / "AGENTS.md"
    if not ws.is_file():
        errors.append("missing agents/hermes/AGENTS.md")

    if errors:
        for e in errors:
            print(f"FAIL {e}", file=sys.stderr)
        return 1
    print("OK party paths (root, profiles, no phantom requirement)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())