# Mission Control implementation discipline

**Effective:** 2026-07-02 (restored after Hermes routing slip on Vault tab v1.2)  
**Authority:** Overwatch + `agents/ROUTER.md`

## Rule (non-negotiable)

| Actor | `index.html` / `server.py` / MC scripts |
|-------|----------------------------------------|
| **Hephaestus** | **Sole implementer** — design, patch, backup, verify, document in `agents/hephaestus/content/` |
| **Hermes** | **Orchestrate only** — board tasks, `delegate_task`, acceptance criteria, Overwatch comms. **No direct MC code edits.** |
| **Iris / Clio / Odysseus** | No MC implementation unless Overwatch explicitly assigns a one-off with Hermes ack |

## Required workflow

1. Overwatch or Hermes approves scope (quest doc in `agents/hermes/content/` or board).
2. Hermes creates board task → **`delegate_task` to Hephaestus** (never implements in parent session).
3. Hephaestus runs `bash agents/_shared/backup-mission-control.sh` **before** any MC file change.
4. Hephaestus ships + writes build log; Hermes marks board **done** after verify (curl/API smoke or Overwatch sign-off).

## Violations

If Hermes (or any non-Hephaestus profile) patches MC without delegation:

1. Log incident in `agents/hermes/content/` (routing slip note).
2. Hephaestus **retroactive review** — audit diff, document ownership, fix gaps, no silent rewrites unless review finds defects.
3. Do not treat the slip as precedent.

## Retroactive quest (2026-07-02)

**Subject:** Vault tab MVP v1.2 (Hermes in-session build).  
**Owner:** Hephaestus — review against [vault-browse-approved](../hermes/content/2026-07-02_vault-browse-approved.md), confirm backup `*_2026-07-02T13-14.*`, API `/api/vault/tree`, UI tab `#vault`, deliver `agents/hephaestus/content/2026-07-02_mc-vault-tab-retro-review.md`.

## v1.1+ MC features (search, wikilinks)

Hephaestus DRI only; Hermes opens quest after Overwatch priority.