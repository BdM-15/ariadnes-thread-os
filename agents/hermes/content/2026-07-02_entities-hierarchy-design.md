# Entities zone — hierarchy design (Item 4, rev 2)

**Date:** 2026-07-02  
**Overwatch input:** Federal chain agency → subagency → funding office → contracting office; programs (LOGCAP, AFCAP) under funding offices (e.g. Army / Air Force). **Companies** by name (not “organizations”) with parent/sister/teammate links; competitor ↔ partner nuance.  
**Hermes + party recommendation:** **Your hierarchy is correct logically** — store it as a **graph on flat files**, not as nested folders.

---

## One sentence

**Two flat folders** (`customers/`, `companies/`), **typed frontmatter**, **parent wikilinks** — agents get speed; humans get the tree via INDEX + hub pages + links.

---

## Why not folder nesting?

```
customers/DoD/Army/ASA-ALT/Funding-Office-X/LOGCAP/   ← breaks fast
```

- Paths churn when USAspending office names change  
- Agents guess wrong path depth  
- Same org appears under “customer” and “program” folders  
- Duplication when LOGCAP spans multiple contracting offices  

**Flat file** `customers/logcap.md` with `parent_customer: "[[army-sustainment-funding-office]]"` is stable, grep-friendly, and matches how Iris/Clio already work (slug + retrieve).

---

## Layout (v2 — target)

```
knowledge/entities/
  INDEX.md
  customers/          # All federal buying-side units (flat slugs)
  companies/          # KBR, primes, subs, JVs — one page per company name (flat slugs)
```

| Retire (Phase 3b) | Move to |
|-------------------|---------|
| `agencies/` | `customers/` |
| `competitors/` | `companies/` |
| `company/` (singular) | `companies/kbr-services-readiness-sustainment.md` |

---

## Federal **customers** — your chain as data, not directories

Mental model (Overwatch):

```
Customer (federal market)
  └── Agency (e.g. Department of the Army)
        └── Subagency / Service (e.g. ASA(ALT), AFMC)
              └── Funding office (program / PEO / portfolio owner)
                    └── Contracting office(s) (awarding)
                    └── Program (LOGCAP, AFCAP) — when capture-relevant
```

### `type` values (frontmatter)

| type | You use it for | Example slug |
|------|----------------|--------------|
| `customer_root` | Optional umbrella “US Federal customer” index | `us-federal-customers` (hub only) |
| `customer_agency` | Dept / top-tier agency | `department-of-the-army` |
| `customer_subagency` | Service, command, PEO-level org | `army-sustainment-command` |
| `customer_office_funding` | Funds requirements / owns program | `army-logcap-funding-office` |
| `customer_office_contracting` | Awards contracts | `acc-ri contracting division` |
| `customer_program` | Named program (LOGCAP, AFCAP) | `logcap`, `afcap` |

### Required / recommended fields

```yaml
type: customer_program
name: "LOGCAP"
parent_customer: "[[army-logcap-funding-office]]"   # walk up to agency
also_related:
  - "[[department-of-the-army]]"
federal_codes:
  agency_code: "..."
  funding_office_code: "..."    # USAspending when known
  awarding_office_code: "..."
capture_notes: "..."            # why we care in RS BU
```

**LOGCAP / AFCAP:** `type: customer_program`, parent = **funding office** under **Dept of Army** or **Dept of Air Force** respectively (you ratify exact parent slugs when Iris promotes).

**Offices:** separate pages for **funding** vs **contracting** — do not merge into one “office” page unless Overwatch explicitly wants a single stub.

### How you *see* the tree (efficient, not clunky)

1. **`customers/INDEX.md`** — role table + link to hub  
2. **`customers/us-federal-customer-hub.md`** (optional) — markdown outline: Army branch, Air Force branch, top programs  
3. **Any page** — “Chain up” section auto-pattern for Clio: bullet list following `parent_customer`  
4. **Later (Hephaestus):** MC Vault or Obsidian Bases filter `type=customer_agency` — no new folders  

**Iris:** when scouting USAspending, fill `federal_codes` + suggest `parent_customer`; never invent folder paths.

---

## **Companies** — by name, compounding intel

Overwatch preference: **`companies/`**, one file per company **name** (slug from canonical trade name).

```yaml
type: company
name: "KBR Services — Readiness & Sustainment"
org_role: self                    # only on our BU hub page
uei: "..."                        # SAM when applicable
parent_company: "[[kbr-inc]]"
sister_companies:
  - "[[kbr-subsidiary-x]]"
relationship_to_us:               # multi-valued — competitor AND teammate over time
  - teammate
  - competitor
pursuit_notes: "Often teams on LOGCAP IV; competes on RS IDIQs"
```

**Competitor ↔ partner nuance:** one page `companies/acme-defense-llc.md` — do **not** split into `competitors/acme` and `partners/acme`. Update `relationship_to_us` and pursuit-specific notes in `pursuits/<slug>/` when role changes per opp.

**KBR:** `companies/kbr-services-readiness-sustainment.md` (`org_role: self`) links to `parent_company: [[kbr-inc]]` when that page exists. Capability depth stays in `domain_intel/capabilities/` (linked, not duplicated).

---

## Agents: why this is faster/smarter

| Need | Agent action |
|------|----------------|
| “Who funds LOGCAP?” | `search_files` / vault retrieve `logcap` → follow `parent_customer` |
| “Contracting office for opp X” | Pursuit frontmatter `funding_customer`, `contracting_customer` wikilinks |
| “Competitor on this award” | `companies/<slug>` + pursuit link |
| “Don’t duplicate agency” | Single slug; `trust` + manifest |
| SAM hierarchy | Fields on **company** page (UEI, legal name) |
| USAspending hierarchy | Fields on **customer** page (agency / office codes) |

Flat slug = **one retrieval hop**; hierarchy = **metadata** agents parse reliably (better than wrong nested path).

---

## Odysseus gates (unchanged intent)

| Gate | Rule |
|------|------|
| E1 | Only `customers/`, `companies/`, `INDEX.md` under entities after 3b |
| E2 | Every new customer page has valid `type` + `parent_customer` (except optional root hub) |
| E3 | Every company page is `type: company`; roles in frontmatter, not folders |
| E4 | No duplicate company under `customers/` |

---

## Phase 3b migration (when schema ack’d)

1. `agencies/*` → `customers/*` (retag `type`)  
2. `competitors/*` + `company/*` → `companies/*`  
3. Regenerate `entities/INDEX.md` + hub stub  
4. `vault_lint` + fix wikilinks project-wide for moved slugs  

**Not in 3b:** creating full Army/AF office trees — add **incrementally** as Iris/Clio promote from pursuits and USAspending, top-down from LOGCAP/AFCAP anchors if you want.

---

## Open choices for Overwatch (reply when ready)

**LOCKED 2026-07-02** — Overwatch agreed page-over-folder model; **proceed Phase 3 + 3b.**

| # | Decision | Locked value |
|---|----------|----------------|
| 1 | Federal hub at 3b | **Yes** — `customers/us-federal-customer-hub.md` |
| 2 | LOGCAP / AFCAP parent slugs | **Yes** — Iris proposes; Odysseus signs at promote |
| 3 | `companies/kbr-inc.md` stub | **Later** |

---

## Related

- [Execution plan](2026-07-02_vault-item4-execution-plan.md) Phase 3b  
- Manifest approved; Phase 2 smoke + Iris Wave A may proceed in parallel with this design freeze  