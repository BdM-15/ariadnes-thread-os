# Party operating rhythm (Capture OS)

**Overwatch → Hermes (planning) → specialists (execute).** Hermes is the trusted NLP touchpoint; he **orchestrates**, he does **not** default to building.

## Models (build mode)

| Role | Model | Use for |
|------|--------|---------|
| **Hermes** | Grok **4.3** | Decompose intent, routing, deliberate-build gates, ratification summaries |
| **Iris, Clio, Odysseus, Hephaestus** | Grok **Composer 2.5** | Research, prose, gates, code/scripts/skills — saves xAI credits |

Run execution in the agent’s **Hermes profile** (`/iris`, `/hephaestus`, …) or `delegate_task` with explicit owner + `agents/<owner>/content/` deliverable.

## Hermes stops here

After a plan is agreed (or obvious from ROUTER), Hermes **does not**:

- Patch `server.py` / `index.html` (→ **Hephaestus**)
- Bootstrap vault zones or lint scripts (→ **Hephaestus**, Hermes approves merge)
- Draft packet or vault prose (→ **Clio**)
- Intel briefs or competitor research (→ **Iris**)
- Promote/trust/citation gates (→ **Odysseus**)

Hermes **does**: triage B, board tasks, quest state, delegate, conflict resolution, Overwatch summary.

## Handoff minimum

Every delegated build:

1. **DRI** named (one agent).
2. **Acceptance** — one sentence + path under `agents/<dri>/content/`.
3. **Log** — `log-task-local.sh` with **`agent_name` = DRI**, not `hermes`.
4. **Return** — Hermes sends Overwatch a short ratification + preview link(s).

## When to brainstorm as a party

Parked or ambiguous features (e.g. `MC-TASK-VAULT-ROUTING`): **Hermes schedules a specialty brainstorm** — each agent proposes **minimal v1** in their lane; Hermes merges into one deliberate decision (see `DELIBERATE_BUILD.md`).

**Full calibration quest:** `agents/hermes/content/2026-07-02_party-calibration-quest.md`