#!/usr/bin/env python3
"""Add or dedupe a Mission Control board task (triage follow-ups)."""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOARD_DB = ROOT / "board.db"
sys.path.insert(0, str(ROOT))


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--title", required=True)
    p.add_argument("--notes", default="")
    p.add_argument("--priority", default="medium", choices=["low", "medium", "high"])
    p.add_argument("--status", default="pending", choices=["pending", "in_progress", "done"])
    p.add_argument("--source-key", default="", help="Idempotent key e.g. triage:eden-jayson")
    args = p.parse_args()
    source_key = (args.source_key or "").strip()

    import server  # noqa: E402 — same repo

    server.board_init()
    payload = {
        "title": args.title,
        "notes": args.notes,
        "priority": args.priority,
        "status": args.status,
        "source_key": source_key,
    }
    out = server.board_create(payload)
    print(json.dumps(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())