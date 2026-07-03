# Pre-W2 hygiene ship (G2 fixes #1–4)

**Date:** 2026-07-03  
**Agent:** Hephaestus  
**Gate:** [G2 schema review](../../odysseus/content/2026-07-02_g2-schema-review.md) — required fixes before W2 content waves

## Delivered

| # | G2 fix | Result |
|---|--------|--------|
| 1 | `knowledge/index.md` schema + zones | Schema row → `foundation/ariadne-vault-schema.md`; zones → `customers/` + `companies/`; wikilink `[[ariadne-vault-schema]]` |
| 2 | Wikilink alias pass in `knowledge/` | 170 files: `[[capture-llm-wiki]]` → `[[ariadne-vault-schema]]` (skipped alias stub + schema doc) |
| 3 | Schema §11 entities 3b | `✅ Phase 3b live (G2 ack 2026-07-02)` |
| 4 | Promote gate checklist paths | `knowledge/thread/` → flat `knowledge/`; schema refs → `ariadne-vault-schema.md`; write zones → `customers/` + `companies/` |

## Extra (retrieve integrity)

- `knowledge/foundation/reference/obsidian-desktop.md` — flat `knowledge/` vault path + schema filename

## Verification

```text
python scripts/vault_lint.py
Vault lint 2026-07-03 — exit 0; 231 md files; unresolved wikilinks 41 (expected deferred)
```

## Git

- Branch: `feature/knowledge-vault-v1`
- Commit: `feat(vault): pre-W2 hygiene (G2)`

## Not in this pass (G2 #5)

- Clio W1 path: `entities/company/` → `entities/companies/kbr-services-readiness-sustainment.md` — Clio ingestion order

## Promote freeze

**Still ON** per Item 4 cleanse — W2 uses candidates + in-place trusted edits until Overwatch lifts freeze.

## Related

- [Phase 3b entities migration](2026-07-02_phase3b-entities-migration-ship.md)
- [Promote gate checklist](../../odysseus/content/2026-07-02_vault-promote-gate-checklist.md)