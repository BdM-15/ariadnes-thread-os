# Knowledge directory (thread-os)

**SSOT vault:** `thread/` — compounding trusted wiki per [doc 02](../docs/inspiration/knowledge-vault-and-compounding-truth.md).

| Path | Purpose |
|------|---------|
| `thread/` | Agents read/write wiki (after triage + review gate) |
| `README.md` | This file |

## Bootstrap (idempotent)

```bash
python scripts/bootstrap_knowledge_vault.py
```

Sources capform `docs/reference` + merges starter `global_wiki`, `domain_intel`, `entities` from capform `knowledge/thread` **only if missing** here. Does **not** import `data-elements/` or pursuit smoke folders.

## Weekly lint

```bash
python scripts/vault_lint.py
```

Hephaestus cron runs this weekly; appends to `thread/log.md`.

## Intel taxonomy (brainstorm)

See [party brainstorm](../agents/hermes/content/2026-07-02_vault-intel-taxonomy-brainstorm.md) — competitor, opportunity, customer, company, general research mapping **onto zones** (not final reorg).