# Tech debt — Mission Control & tasks

| ID | Item | Status |
|----|------|--------|
| MC-CRON-02 | Schedule UI used stale snapshot only; `/api/cron` route missing | **Fixed** 2026-07-02 — GET `/api/cron` + `loadCron()` |
| MC-VAULT-UI | Dedicated Vault Candidates tab | **Deferred** — v1 uses task board `vault:` notes + disk path; promote via Hermes, not new MC tab |
| MC-BOARD-01 | Triage wrote quest `.md` only; Task board uses `board.db` | **Fixed** — `board_add_task.py` + `source_key` dedupe |
| MC-BOARD-02 | Restart MC after `server.py` change | Use `bash start.sh` (auto-restarts stale) or `bash start.sh --force` |
| MC-STALE-01 | `start.sh` reused old process when port answered but `/api/cron` missing | **Fixed** — `mc_ready()` health check |
| MC-TASK-VAULT-ROUTING | Task card shows vault path on hover only; no click-through to vault/agent routing | **Backlog** — party to design minimal Overwatch↔agent handoff (not a Vault tab) |
| TASK-FLOW-01 | Recurring triage tasks → skills/cron (“research ready at wake”) | **Backlog** — pattern in `TASK_WORKFLOW_LADDER.md` |
| MC-QUEST-01 | Flat `quests/*.md` not ingested (only `quests/<slug>/quest.yaml`) | **Backlog** — optional sync or YAML scaffold |

## Task → workflow ladder (Overwatch vision)

1. **Triage** → board task + vault candidate  
2. **Repeat** same `source_key` class → Hephaestus drafts skill  
3. **Cron** with `attach_to_session` or morning deliver → briefing for Overwatch  

Documented in `agents/_shared/TASK_WORKFLOW_LADDER.md`.