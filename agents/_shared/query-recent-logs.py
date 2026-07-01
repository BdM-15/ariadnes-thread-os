#!/usr/bin/env python3
"""Print recent agent_logs from agents/_shared/agent-logs.db."""
import sqlite3
from pathlib import Path

DB = Path(__file__).resolve().parent / "agent-logs.db"
LIMIT = 20

def main() -> None:
    if not DB.is_file():
        print(f"No database at {DB}")
        return
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        """
        SELECT id, agent_name, task_description, model_used, status, created_at
        FROM agent_logs
        ORDER BY created_at DESC
        LIMIT ?
        """,
        (LIMIT,),
    ).fetchall()
    conn.close()
    print(f"Recent logs (limit {LIMIT}) from {DB}\n")
    for r in rows:
        print(
            f"{r['created_at']} | {r['agent_name']:11} | {r['status']:9} | "
            f"{(r['model_used'] or '-'):28} | {r['task_description'][:60]}"
        )
    print(f"\nTotal shown: {len(rows)}")

if __name__ == "__main__":
    main()