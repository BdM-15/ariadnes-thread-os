# Entities zone (v2)

**Layout:** Two flat folders — `customers/` (federal buying side) and `companies/` (KBR, primes, subs, JVs). Hierarchy lives in **frontmatter** (`parent_customer`, `parent_company`), not nested directories.

## Subfolders

| Folder | Who | Example |
|--------|-----|---------|
| `customers/` | Federal customers, offices, programs | `us-federal-customer-hub.md` |
| `companies/` | One page per company name (roles in frontmatter) | `kbr-services-readiness-sustainment.md` |

**Retired (Phase 3b):** `agencies/` → `customers/`; `competitors/` + `company/` → `companies/`.

## Canonical files (trusted)

- `companies/kbr-services-readiness-sustainment.md` — **Overwatch company SSOT** (`org_role: self`)
- `customers/us-federal-customer-hub.md` — federal customer outline (incremental population)
- `customers/` — agency/office/program pages as Iris promotes

Smoke templates (`test-agency-xyz`, `example-competitor-llc`) archived Phase 2 → `generated-projections/archived/rebuild-2026/entities/`.

## Frontmatter patterns

**Customers:** `type` ∈ `customer_agency` | `customer_subagency` | `customer_office_funding` | `customer_office_contracting` | `customer_program`; use `parent_customer` to walk the chain.

**Companies:** `type: company`; `relationship_to_us` (competitor, teammate, etc.) on one page — do not split competitor/partner folders.

## Deep company knowledge

Capability depth lives in `global/domain_intel/capabilities/` — **linked from** the company entity, not duplicated.

## Archive boundary

Candidates → `generated-projections/` until promote. **Promote freeze:** on until Overwatch lifts (Item 4).

## Maintainer

Iris (external entities) · Clio (pursuit links) · Hephaestus (index/lint) · Overwatch (company entity)