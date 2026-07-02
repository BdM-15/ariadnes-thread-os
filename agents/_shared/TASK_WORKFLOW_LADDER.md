# Task workflow ladder (Overwatch)

When Hermes triage creates a **task**:

1. **Board** — `python scripts/board_add_task.py --title "..." --source-key triage:<slug> --notes "vault: ..."`
2. **Quest note** (optional) — `agents/hermes/content/quests/<slug>.md` for narrative
3. **Vault** — candidate path in notes

## When the same task repeats

- Hephaestus: propose **skill** (e.g. `jayson-capability-followup`)
- Hermes: propose **cron** — `no_agent` script or agent briefing with `deliver` to Overwatch channel

## Morning-ready pattern

```text
Cron (weekdays 6am) → Iris research draft in agents/iris/content/
                    → deliver summary + MC content link
```

Overwatch approves promote to vault / closes board task.