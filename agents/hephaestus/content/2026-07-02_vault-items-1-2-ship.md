# Vault hardening items 1–2 ship (2026-07-02)

**Branch:** `feature/knowledge-vault-v1`  
**Overwatch:** COMMIT items **1 + 2** only; **defer item 3** until after ground-up vault overhaul brainstorm.

## Shipped

### Item 1 — MC browse UI (read-only)
- `#panel-vault` CSS: `scrollbar-gutter`, browse list overflow fixes
- Vault tab: zone filters, morning queue, browse + markdown reader
- MC v1.3 badge / `VAULT_ROOT` read APIs: `/api/vault/tree`, `/api/vault/candidates`, `/api/vault/read`

### Item 2 — Flatten vault path
- `knowledge/thread/*` → `knowledge/*` (git renames)
- `server.py`: `VAULT_ROOT = knowledge`
- Essential refs: `scripts/vault_lint.py`, `scripts/promote_vault_candidate.py`, `agents/_shared/VAULT_RETRIEVE.md`, root `AGENTS.md`, `agents/_shared/FILE_MUTATION.md`, `index.html` sublabel + board vault path helpers

## Deferred (item 3 — not in this commit)

- MC vault **edit** UI in `index.html`
- `POST /api/vault/save`, `/api/vault/candidate`, `/api/vault/delete`, `/api/vault/validate`
- `_vault_edit_policy`, schema lint on save, Clio harmonize board tasks
- Untracked `scripts/vault_schema_lint.py` — **not** added

## Operator note

Restart Mission Control after pull so `server.py` picks up flattened `VAULT_ROOT`.