# Phase 3b entities v2 migration — ship note

**Date:** 2026-07-02  
**Agent:** Hephaestus  
**Gate:** Entities hierarchy design locked 2026-07-02; **promote freeze remains on** (no auto-promote via scripts without Overwatch).

## Scope delivered

| Step | Action | Result |
|------|--------|--------|
| 1 | `agencies/*` → `customers/` | Empty `agencies/` removed; smoke `test-agency-xyz` already archived Phase 2 |
| 2 | `competitors/*` + `company/*` → `companies/` | Smoke competitor archived; **git mv** `company/kbr-services-readiness-sustainment.md` → `companies/` |
| 3 | Frontmatter | KBR page: `type: company`, **`org_role: self`**; hub: `type: customer_root` |
| 4 | Hub stub | `customers/us-federal-customer-hub.md` (Army/AF branches stub per design) |
| 5 | `entities/INDEX.md` | Rewritten for v2 (`customers/` + `companies/`); no `knowledge/thread/` paths |
| 6 | `vault_lint` | Run 2026-07-03 00:55 UTC — 226 md files; entities zone count 3 |
| 7 | Tooling | `promote_vault_candidate.py`, `bootstrap_knowledge_vault.py`, `vault_manifest_inventory.py` write zones updated |
| 8 | Relationships | `knowledge/relationships/ENTITY_RELATIONSHIPS.md` aligned to v2 |

## Files touched (vault)

- `knowledge/entities/INDEX.md`
- `knowledge/entities/customers/us-federal-customer-hub.md` (new)
- `knowledge/entities/companies/kbr-services-readiness-sustainment.md` (renamed + frontmatter)
- `knowledge/relationships/ENTITY_RELATIONSHIPS.md`
- `knowledge/pursuits/INDEX.md` (path string)

## Git moves

```
renamed: entities/company/kbr-services-readiness-sustainment.md → entities/companies/...
deleted: entities/agencies/test-agency-xyz.md (staged from Phase 2)
deleted: entities/competitors/example-competitor-llc.md (staged from Phase 2)
```

## Not in 3b (per design)

- Full Army/AF office trees — incremental via Iris/Clio promote
- `companies/kbr-inc.md` parent stub — **later**
- Project-wide wikilink rewrite for historical agent `content/` artifacts (paths documented in ship only)

## Odysseus gates (post-3b)

| Gate | Status |
|------|--------|
| E1 | Only `customers/`, `companies/`, `INDEX.md` under `entities/` |
| E2 | New customer pages need `type` + `parent_customer` (hub exempt as `customer_root`) |
| E3 | Company pages `type: company`; roles in frontmatter |
| E4 | No duplicate company under `customers/` |

## Related

- [Entities hierarchy design](../../hermes/content/2026-07-02_entities-hierarchy-design.md)
- [Phase 2 smoke archive ship](2026-07-02_phase2-smoke-archive-ship.md)