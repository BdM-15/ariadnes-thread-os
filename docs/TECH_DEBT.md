# Tech debt — Mission Control & tasks

| ID | Item | Status |
|----|------|--------|
| MC-CRON-01 | Schedule tab only showed REGISTRY cleanup job, not Hermes `cron/jobs.json` | **Fixed** 2026-07-02 — `server.py` `cron_data()` |
| MC-BOARD-01 | Triage wrote quest `.md` only; Task board uses `board.db` | **Fixed** — `board_add_task.py` + `source_key` dedupe |
| MC-BOARD-02 | Restart MC server after `server.py` change to pick up cron/board | Operator: `bash start.sh` |
| TASK-FLOW-01 | Recurring triage tasks → skills/cron (“research ready at wake”) | **Backlog** — pattern in `TASK_WORKFLOW_LADDER.md` |
| MC-QUEST-01 | Flat `quests/*.md` not ingested (only `quests/<slug>/quest.yaml`) | **Backlog** — optional sync or YAML scaffold |

## Task → workflow ladder (Overwatch vision)

1. **Triage** → board task + vault candidate  
2. **Repeat** same `source_key` class → Hephaestus drafts skill  
3. **Cron** with `attach_to_session` or morning deliver → briefing for Overwatch  

Documented in `agents/_shared/TASK_WORKFLOW_LADDER.md`.