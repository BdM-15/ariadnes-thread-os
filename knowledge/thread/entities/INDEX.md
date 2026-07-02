# Entities zone

**Where to start:** Named organization → subfolder by **role**.

## Subfolders

| Folder | Who | Example |
|--------|-----|---------|
| `company/` | **Our org** (KBR RS BU) — capability matrix hub | `kbr-services-readiness-sustainment.md` |
| `agencies/` | Customers / funding orgs | DoD, Army contracting offices |
| `competitors/` | Primes, subs, other offerors | Award-based intel |

Same **page pattern** (frontmatter + signals + citations); `type` field distinguishes `company` | `agency` | `competitor`.

## Canonical files (trusted)

- `company/kbr-services-readiness-sustainment.md` — **Overwatch company SSOT**
- `competitors/example-competitor-llc.md` — template competitor
- `agencies/` — agency pages as promoted

## Deep company knowledge

Capability depth lives in `global/domain_intel/capabilities/` — **linked from** company entity, not duplicated.

## Archive boundary

Candidates → `generated-projections/` until promote.

## Maintainer

Iris (external entities) · Clio (pursuit links) · Hephaestus (index/lint) · Overwatch (company entity)