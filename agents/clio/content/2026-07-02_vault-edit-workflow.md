# Vault edit workflow — Clio format guardian (Wave E / doc 17b)

**Date:** 2026-07-02  
**DRI:** Hephaestus (MC + API) · **Format guardian:** Clio · **Promote:** Odysseus + script only

## Summary

MC Vault mirrors **Content** tab: read → EDIT → Save. **Overwatch** = local MC actor. **Never** set `trust: trusted` via save — only `promote_vault_candidate.py`.

## Permissions (Overwatch)

| Zone | Edit | Create | Delete |
|------|------|--------|--------|
| `generated-projections/*.md` (not INDEX) | ✅ full | ✅ new candidate | ✅ reject draft |
| Trusted write zones (`entities/`, `global/domain_intel/`, `pursuits/`, `relationships/`) | ✅ **append-only** body | ❌ promote only | ❌ |
| `foundation/`, capform-only zones | ❌ | ❌ | ❌ |
| `index.md`, `log.md`, zone INDEX | read-only | ❌ | ❌ |

## API (Hephaestus)

- `POST /api/vault/save?path=` — sandbox + `_vault_edit_policy()`
- `POST /api/vault/candidate` — new under `generated-projections/` with slug-date template
- Optional `POST /api/vault/validate` — preview errors

## Server gates

- Valid YAML; `id` immutable on trusted; `trust` locked per zone
- Trusted: reject large body deletions (append-only contract)
- Log line on save → `knowledge/.../log.md` (path updates after flatten)

## Clio harmonize (after save)

1. Deterministic `vault_schema_lint.py` (Hephaestus)
2. Hard fail → block save
3. Soft fail → save + board/cron **Clio** task → `agents/clio/content/YYYY-MM-DD_vault-lint-<slug>.md`

**Clio checklist:** frontmatter ↔ zone; wikilinks; candidate prose cite style; no trusted section deletes; dedup `id`.

## Schema source (until cleanse)

`foundation/capture-llm-wiki.md` → post-cleanse **`ariadne-vault-schema.md`**.

## Ref

`deleg_251b596d` task 2 · Hermes [vault-hardening-brainstorm](http://127.0.0.1:51763/#content/hermes/2026-07-02_vault-hardening-brainstorm.md).