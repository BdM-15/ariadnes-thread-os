# Agent activity logging policy (all five agents)

Applies to: **hermes**, **iris**, **clio**, **odysseus**, **hephaestus**.

## Mandatory behavior

1. **Before sending any response** to Overwatch, log the task via the shared script (silent — do not announce logging unless Overwatch asks).
2. Log **every** response, including short or simple replies.
3. **`task_description`:** ≤ **140 characters**; summarize what you are about to deliver.
4. **`status`:** `completed` or `failed` only.
5. **`agent_name`:** lowercase party name (`hermes`, `iris`, `clio`, `odysseus`, `hephaestus`).
6. **`model_used`:** optional; omit to auto-detect from Hermes profile config.

## Command (from project root)

```bash
bash agents/_shared/log-task-local.sh <agent_name> "<task_description>" <completed|failed>
```

Run in the **background** when using terminal (`background=true`) so the response is not blocked; ensure the insert completes before you finish the turn when possible.

## Storage

- Database: `agents/_shared/agent-logs.db`
- Mission Control / Thread Tavern activity feed reads this file.

## Do not

- Skip logging for “small” answers.
- Log after the user-visible reply (log **first**).
- Mention logging in normal Overwatch-facing prose unless asked.

## Retention (automatic — no archive)

- **Policy:** Permanent **DELETE** of rows older than **30 days** in `agent-logs.db`.
- **Script:** `agents/_shared/cleanup-logs.sh` (VACUUM after delete).
- **Owner:** Hephaestus executes; Hermes reads `agents/hermes/content/cleanup-last-run.txt` and `log-retention.md` for internal confirmation.
- **Schedule:** 1st of each month **03:00** — Hermes cron job `ariadne-agent-logs-cleanup` (script `ariadne-cleanup-agent-logs.sh`). Overwatch does not run this.