#!/usr/bin/env bash
# Permanent retention: DELETE agent_logs rows older than 30 days (no archive).
# Usage: bash agents/_shared/cleanup-logs.sh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DB_PATH="${SCRIPT_DIR}/agent-logs.db"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
HERMES_LOG="${PROJECT_ROOT}/agents/hermes/content/log-retention.md"
RETENTION_DAYS="${RETENTION_DAYS:-30}"

export DB_PATH PROJECT_ROOT HERMES_LOG RETENTION_DAYS

python - <<'PY'
import os
import sqlite3
from datetime import datetime, timezone, timedelta
from pathlib import Path

DB_PATH = os.environ["DB_PATH"]
PROJECT_ROOT = Path(os.environ["PROJECT_ROOT"])
HERMES_LOG = Path(os.environ["HERMES_LOG"])
RETENTION_DAYS = int(os.environ.get("RETENTION_DAYS", "30"))

Path(DB_PATH).parent.mkdir(parents=True, exist_ok=True)
conn = sqlite3.connect(DB_PATH)
conn.execute(
    """
    CREATE TABLE IF NOT EXISTS agent_logs (
        id TEXT PRIMARY KEY,
        agent_name TEXT NOT NULL,
        task_description TEXT NOT NULL,
        model_used TEXT,
        status TEXT NOT NULL,
        created_at TEXT NOT NULL
    )
    """
)
conn.commit()

cutoff = (datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)).strftime("%Y-%m-%dT%H:%M:%SZ")
before = conn.execute("SELECT COUNT(*) FROM agent_logs").fetchone()[0]
deleted = conn.execute(
    "DELETE FROM agent_logs WHERE created_at < ?",
    (cutoff,),
).rowcount
conn.commit()
conn.execute("VACUUM")
remaining = conn.execute("SELECT COUNT(*) FROM agent_logs").fetchone()[0]
conn.close()

summary = (
    f"deleted={deleted} remaining={remaining} cutoff_utc={cutoff} "
    f"retention_days={RETENTION_DAYS} db={DB_PATH}"
)
print("AGENT_LOG_CLEANUP " + summary)

HERMES_LOG.parent.mkdir(parents=True, exist_ok=True)
stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
line = f"- {stamp} | Hephaestus cleanup | {summary}\n"
if HERMES_LOG.is_file():
    prior = HERMES_LOG.read_text(encoding="utf-8")
    if not prior.lstrip().startswith("#"):
        HERMES_LOG.write_text("# Agent log retention (Hermes internal)\n\n" + line, encoding="utf-8")
    else:
        with HERMES_LOG.open("a", encoding="utf-8") as f:
            f.write(line)
else:
    HERMES_LOG.write_text(
        "# Agent log retention (Hermes internal)\n\n"
        "Permanent deletion only — no archive. Hephaestus runs monthly; Hermes reads this for confirmation.\n\n"
        + line,
        encoding="utf-8",
    )

confirm = PROJECT_ROOT / "agents" / "hermes" / "content" / "cleanup-last-run.txt"
confirm.write_text(
    f"Hermes internal: log retention cleanup OK at {stamp}\n{summary}\n",
    encoding="utf-8",
)
PY

echo "Hermes confirmation written: agents/hermes/content/cleanup-last-run.txt"
echo "History: agents/hermes/content/log-retention.md"