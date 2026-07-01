# Agent activity log (local SQLite)

**Database:** `agents/_shared/agent-logs.db`  
**Script:** `agents/_shared/log-task-local.sh`

## Schema (`agent_logs`)

| Column | Type | Notes |
|--------|------|--------|
| id | TEXT PK | UUID |
| agent_name | TEXT | hermes, iris, clio, odysseus, hephaestus |
| task_description | TEXT | |
| model_used | TEXT | optional; auto from Hermes profile `config.yaml` |
| status | TEXT | completed \| failed |
| created_at | TEXT | ISO 8601 UTC |

## Usage (from repo root)

```bash
bash agents/_shared/log-task-local.sh hermes "Ratified quest" completed
bash agents/_shared/log-task-local.sh iris "Intel brief saved" completed grok-composer-2.5-fast
```

## Query (dashboard / CLI)

```bash
python agents/_shared/query-recent-logs.py
```

Mission Control activity feed can read this DB via the query helper or direct SQLite.