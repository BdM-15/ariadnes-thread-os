#!/usr/bin/env python3
"""Sync workspace identity + memory into Hermes profile dirs. Run from project root."""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
HERMES_PROFILES = Path.home() / "AppData/Local/hermes/profiles"

BINDINGS = {
    "hermes": "minos",
    "iris": "iris",
    "clio": "clio",
    "odysseus": "odysseus",
    "hephaestus": "hephaestus",
}

REQUIRED = ("SOUL.md", "IDENTITY.md", "USER.md", "AGENTS.md", "MEMORY.md")


def _copy(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    text = src.read_text(encoding="utf-8")
    dest.write_text(text, encoding="utf-8")
    if dest.read_text(encoding="utf-8") != text:
        raise RuntimeError(f"sync mismatch: {dest}")


def main() -> int:
    errors: list[str] = []
    for agent, profile in BINDINGS.items():
        ws = PROJECT_ROOT / "agents" / agent
        content = ws / "content"
        if not content.is_dir():
            errors.append(f"missing content/: {content}")
        for name in REQUIRED:
            if not (ws / name).is_file():
                errors.append(f"missing workspace file: {ws / name}")
        prof = HERMES_PROFILES / profile
        try:
            _copy(ws / "SOUL.md", prof / "SOUL.md")
            mem_dir = prof / "memories"
            _copy(ws / "MEMORY.md", mem_dir / "MEMORY.md")
            _copy(ws / "USER.md", mem_dir / "USER.md")
            print(f"OK {agent} -> {profile} (SOUL + MEMORY + USER)")
        except (OSError, RuntimeError) as exc:
            errors.append(str(exc))

    if errors:
        for e in errors:
            print(f"ERROR {e}", file=sys.stderr)
        return 1
    print("All five agents: workspace complete; profile SOUL + dedicated memory synced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())