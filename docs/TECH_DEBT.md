# Tech debt — Mission Control & tasks

| ID | Item | Status |
|----|------|--------|
| MC-CRON-02 | Schedule UI used stale snapshot only; `/api/cron` route missing | **Fixed** 2026-07-02 — GET `/api/cron` + `loadCron()` |
| MC-BOARD-01 | Triage wrote quest `.md` only; Task board uses `board.db` | **Fixed** — `board_add_task.py` + `source_key` dedupe |
| MC-BOARD-02 | Restart MC after `server.py` change | `bash start.sh` or `bash start.sh --force` |
| MC-STALE-01 | `start.sh` reused old process when `/api/cron` missing | **Fixed** — `mc_ready()` |
| MC-VAULT-UI | Vault surfacing in MC | **Parked** — deliberate design: best minimal fit (see `DELIBERATE_BUILD.md`) |
| MC-TASK-VAULT-ROUTING | From board task to vault candidate + agent handoff (actionable, not hover-only) | **Backlog** — party finds modern minimalist routing in existing surfaces (Content, skills, Hermes); log intent, don't bolt tab same day |
| TASK-FLOW-01 | Recurring triage tasks → skills/cron (“research ready at wake”) | **Backlog** — pattern in `TASK_WORKFLOW_LADDER.md` |
| MC-QUEST-01 | Flat `quests/*.md` not ingested (only `quests/<slug>/quest.yaml`) | **Backlog** — optional sync or YAML scaffold |

## Task → workflow ladder (Overwatch vision)

1. **Triage** → board task + vault candidate  
2. **Repeat** same `source_key` class → Hephaestus drafts skill  
3. **Cron** with `attach_to_session` or morning deliver → briefing for Overwatch  

Documented in `agents/_shared/TASK_WORKFLOW_LADDER.md`.