# Phase 2 minimal smoke archive — ship note

**Date:** 2026-07-02  
**Agent:** Hephaestus  
**Gate:** Manifest v1 approved; Overwatch Phase 2 = **2 ARCHIVE rows only** (no mass archive, no entities hierarchy migration).

## Actions

| Source (was) | Destination |
|--------------|-------------|
| `knowledge/entities/agencies/test-agency-xyz.md` | `knowledge/generated-projections/archived/rebuild-2026/entities/agencies/test-agency-xyz.md` |
| `knowledge/entities/competitors/example-competitor-llc.md` | `knowledge/generated-projections/archived/rebuild-2026/entities/competitors/example-competitor-llc.md` |

- Created archive tree under `generated-projections/archived/rebuild-2026/` preserving `entities/<role>/` relative paths.
- Moves via `git mv` (history retained).
- Updated `knowledge/entities/INDEX.md` — removed live template competitor line; noted archive boundary.

## Not in scope (deferred)

- Phase 3b entities folder structure migration.
- Bulk ARCHIVE / RESCOUT / REWRITE waves.

## vault_lint

- No script changes required; post-move lint run clean (zone shift: 2 files from `entities` → `generated-projections`).
- **Retry** (`deleg_7d16de7f` task 1): `python scripts/vault_lint.py` — exit 0 (2026-07-02 23:55 UTC); 224 markdown files; `entities` zone count 2 (INDEX + company); archive paths under `generated-projections`.

## Manifest rows executed

- `entities/agencies/test-agency-xyz.md` — ARCHIVE ✓  
- `entities/competitors/example-competitor-llc.md` — ARCHIVE ✓  

---

*hephaestus completed — Phase 2 smoke archive*