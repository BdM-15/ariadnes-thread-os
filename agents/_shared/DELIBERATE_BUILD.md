# Deliberate build (Ponytail + Pocock)

**Not** “never add features.” **Do** choose **what** and **when** with intent.

## Overwatch input ≠ build order

Ideas, screenshots, and “we need X” are **requirements signals**. Hermes and the party must:

1. **Name the job** — what decision or workflow fails today?
2. **Propose the smallest fit** — extend an existing surface (board, Content, skill, cron) before new MC tabs or frameworks.
3. **Time it** — ship when a pursuit or daily loop is blocked; otherwise log **tech debt** or inspiration doc with a **minimal v1** slice.
4. **Confirm** when scope is ambiguous or crosses agents (Overwatch approves merge / big surface changes).

## Tech debt is intentional parking

Items like **vault ↔ task routing** mean: *we need capability X; find the most advantageous, modern, minimalist fit in the Agent OS* — not “rejected forever” and not “build tonight because it was mentioned once.”

## Architecture bias (Matt Pocock)

- Thin UI / routes → fat services (`server.py`, `scripts/`, skills).
- One source of truth per concept (`board.db`, `knowledge/`, Hermes `jobs.json`).
- Observable seams; Hephaestus owns refactors when delegated.

## Anti-pattern

Taking a single chat thought and implementing a new tab, store, or parallel workflow **in the same session** without the four steps above.

See `docs/inspiration/01-PROGRAM-PRINCIPLES.md` §4–5.