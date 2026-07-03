# Phase 1 vault manifest inventory — ship note

**Date:** 2026-07-02
**Agent:** Hephaestus
**Overwatch ratification:** 2026-07-02 hybrid yes; archive `generated-projections/archived/rebuild-2026/`; KBR-first waves; minimal cleanse; promote freeze on.

## Deliverables

- Machine inventory CSV: `agents/hephaestus/content/2026-07-02_vault-manifest-inventory.csv`
- Total markdown files scanned: **224**
- **No vault files moved or deleted** (manifest only).

## Row counts by `proposed_tag`

| proposed_tag | count |
|--------------|------:|
| KEEP | 16 |
| REWRITE | 119 |
| ARCHIVE | 2 |
| RESCOUT | 87 |
| **TOTAL** | **224** |

## Row counts by `zone`

| zone | count |
|------|------:|
| global_wiki | 87 |
| capabilities | 46 |
| concepts | 42 |
| shipley | 23 |
| domain_intel | 9 |
| entities | 4 |
| foundation | 4 |
| meta | 3 |
| generated-projections | 2 |
| relationships | 2 |
| global | 1 |
| pursuits | 1 |

## Cross-tab: zone × proposed_tag

| zone | KEEP | REWRITE | ARCHIVE | RESCOUT |
|------|-----:|--------:|--------:|--------:|
| capabilities | 0 | 0 | 0 | 46 |
| concepts | 1 | 0 | 0 | 41 |
| domain_intel | 4 | 5 | 0 | 0 |
| entities | 2 | 0 | 2 | 0 |
| foundation | 0 | 4 | 0 | 0 |
| generated-projections | 2 | 0 | 0 | 0 |
| global | 1 | 0 | 0 | 0 |
| global_wiki | 0 | 87 | 0 | 0 |
| meta | 3 | 0 | 0 | 0 |
| pursuits | 1 | 0 | 0 | 0 |
| relationships | 2 | 0 | 0 | 0 |
| shipley | 0 | 23 | 0 | 0 |

## Bucket rules applied (machine)

- Smoke entities → **ARCHIVE**
- `domain_intel/capabilities/` → default **RESCOUT**
- `global_wiki/capture/concepts/` → default **RESCOUT**
- `global_wiki/shipley/` → default **REWRITE**
- Path/basename `test*` / `example*` → **ARCHIVE**
- Odysseus exemplar **KEEP** paths (index chain, KBR hub, eden candidate, ms1–ms4 milestones, sam-live-discovery)

## Next

Odysseus signs manifest rows; Phase 3 archive executes **ARCHIVE** rows only after hybrid gate GREEN.

---

*hephaestus completed — Phase 1 manifest*
