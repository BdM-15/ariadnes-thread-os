---
name: "ariadne-vault-schema"
type: schema
id: foundation-ariadne-vault-schema
schema_version: 3
tags: [karpathy-wiki, schema, vault, agent-os, ariadne]
aliases: [capture-llm-wiki]
supersedes: foundation-capture-llm-wiki
---

# Ariadne vault schema (Agent OS contract)

**Layer 3 contract** for how party agents maintain `knowledge/`. Read this before any vault write.

**Alias (one release):** `[[capture-llm-wiki]]` resolves here. New wikilinks use `[[ariadne-vault-schema]]`.

**Karpathy pattern** ([llm-wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)):
- Obsidian = optional human IDE (desktop not required)
- Agents = programmers (Hermes party, skills, retrieve-before-answer)
- Wiki `.md` = codebase — persistent, compounding artifact

**Ariadne addition:** trusted wiki writes only after **Overwatch ratify** at the trust boundary (`candidate` → `trusted`). The vault **informs** capture decisions; execution artifacts (packets, board tasks, MC Content handoffs) live outside this tree.

**Not required in thread-os:** capform UI, PostgreSQL as mandatory Layer 1, or `/knowledge` API monolith. Raw sources are cited paths (URLs, exports, docs, meeting notes labeled honestly) — agents read them; they are not a second writable brain inside Postgres.

---

## 1. Layers (Agent OS v1)

| Layer | Location | Who writes | Rule |
|-------|----------|------------|------|
| **Raw** | Cited URLs, Iris exports, `docs/`, MCP snapshots, Overwatch-provided files | Ingest, Iris, humans | **Read-only** for vault writers — cite, never invent |
| **Wiki** | `knowledge/` (zones below) | Party agents after promote | **Append** trusted sections; never erase trusted history |
| **Schema** | `foundation/ariadne-vault-schema.md` (this file) | Humans + platform seed | Co-evolve; `schema_version` bumps on platform updates |

**Staging (not SSOT):** `agents/<agent>/content/` — session handoffs for Mission Control; triage durable facts into `generated-projections/` or promote into write zones.

---

## 2. Topology — flattened `knowledge/`

No `knowledge/thread/` prefix. Repo root:

```
knowledge/
  index.md                     # Catalog — update on every trusted ingest / promote
  log.md                       # Append-only timeline (ingest, promote, lint)
  foundation/
    ariadne-vault-schema.md    # This file
    reference/                 # Packet mirrors, Obsidian notes (read-mostly)
  entities/
    INDEX.md
    customers/                 # Federal buying-side units (flat slugs) — see § Entities
    companies/                 # Primes, subs, JVs, our BU hub (flat slugs)
  global/
    INDEX.md
    global_wiki/               # Evergreen doctrine (Shipley, FAR, workload)
    domain_intel/              # Bid-fit: capabilities/, milestones/, etc.
  pursuits/<slug>/             # Per-opportunity wiki (created on Track)
  relationships/             # Follow-the-money graph notes
  generated-projections/       # LLM drafts **before** review promotion only
  .obsidian/                   # Optional desktop config
```

**Deferred unless Overwatch promotes:** `data-elements/`, `milestones/` (top-level), `training/`, `education/`.

---

## 3. Zones and navigation

| Zone | Concern | Read first |
|------|---------|------------|
| `entities/` | Customers, companies, programs as pages | `entities/INDEX.md` |
| `global/` | Doctrine + domain intel | `global/INDEX.md` |
| `pursuits/` | Per-opportunity learning | `pursuits/INDEX.md` or `<slug>/` |
| `generated-projections/` | Candidates only | `generated-projections/INDEX.md` |
| `relationships/` | Economic / teaming graph | zone INDEX when present |

**Retrieve contract (party-wide):** Before pursuit-relevant strategy or entity claims, read root `index.md` → zone `INDEX.md` → relevant pages via wikilinks. Chat memory is not a substitute.

**Wandermist rule:** Fix the **zone INDEX** when agents open wrong files — do not deep-reorg the repo without manifest pain data.

---

## 4. Trust and promotion

### Frontmatter `trust`

| Value | Meaning |
|-------|---------|
| `candidate` | Draft; may live only under `generated-projections/` or pre-promote edits |
| `trusted` | Overwatch-ratified SSOT in a write zone |
| `archived` | Historical; INDEX marks “skip unless asked” |

**No auto-promote.** Hermes triage may create candidates; only Overwatch (with Odysseus citation gate + Hephaestus move) promotes to `trusted`.

### Candidate → trusted workflow

1. **Intake** — Hermes triage (vault candidate vs action vs discard).
2. **Candidate write** — `generated-projections/<slug>-<date>.md` (or equivalent) with full frontmatter + `## Related`.
3. **Dedup** — grep `id`, `award_key`, slug, title (Hephaestus assists).
4. **Review** — Overwatch reads candidate; decides promote / reject / edit in place.
5. **Promote** — Overwatch: “promote `<path>`” → **Odysseus** citation + dedup gate → **Hephaestus** move to write zone, `trust: trusted`, update `index.md`, zone `INDEX.md`, append `log.md`.

Gate detail: `agents/odysseus/content/2026-07-02_vault-promote-gate-checklist.md`.

### Write zones (trusted destinations)

After **Phase 3b** entities migration:

| Destination | Typical `type` |
|-------------|------------------|
| `entities/customers/<slug>.md` | `customer_*` (see § Entities) |
| `entities/companies/<slug>.md` | `company` |
| `global/domain_intel/...` | `capability`, domain synthesis |
| `pursuits/<slug>/...` | `opportunity`, pursuit learning |
| `relationships/...` | relationship / follow-the-money |

**Protected (no promote into):** `foundation/`, `.obsidian/`, deferred zones above.

### Promotion freeze (cleanse / Item 4)

During vault cleanse until **flatten complete**, `vault_lint` green, and manifest signed (Odysseus + Overwatch): **freeze** all candidate→trusted promotes except Overwatch + Odysseus **emergency PASS**. Candidates may still be authored; they stay in `generated-projections/`.

Ref: `agents/odysseus/content/2026-07-02_vault-cleanse-program.md`.

---

## 5. Page format (Obsidian Flavored Markdown)

Every wiki page **must** start with YAML frontmatter:

```yaml
---
name: "Exact Entity or Concept Name"
type: "company" | "customer_agency" | "customer_program" | "capability" | "synthesis" | "opportunity" | ...
id: "entity-customer-logcap" | "pursuit-acme-recompete" | ...
trust: "candidate" | "trusted" | "archived"
review_id: "uuid-or-null"
reviewed_by: "overwatch-or-null"
reviewed_at: "ISO-8601-or-null"
added: "2026-07-02T12:00:00Z"
last_updated: "2026-07-02"
citations: "award_key:CONT_AWD_... • agency:Army • source:usa_spending • url:https://..."
tags: [recompete, shipley]
aliases: ["LOGCAP", "Logistics Civil Augmentation Program"]
---
```

**Body sections** (append on re-ingest; never delete trusted history):

```markdown
## Key signals + citations
- Grounded bullets with award_key, NAICS, tool, URL

## Synthesis
Evidence-based analysis (agent or human)

## Open questions
- ...

## Related
[[logcap]] [[kbr-services-readiness-sustainment]] [[capabilities-catalog]]

## Added/Updated 2026-07-02
Append-only section per ingest pass
```

**Dedup rule:** Before append, grep vault for same `award_key`, `id`, or `review_id`. Same identity → merge into existing dated section; do not duplicate claims.

**Provenance:** Every material claim needs traceable citation. Never invent award or contract data. Meeting hearsay → label `unverified` or open questions — not bid truth without evidence.

---

## 6. Entities zone (rev 2 — locked 2026-07-02)

**One sentence:** Two flat folders (`customers/`, `companies/`), **typed frontmatter**, **parent wikilinks** — agents get speed; humans get the tree via INDEX + hub pages + links.

Design source: `agents/hermes/content/2026-07-02_entities-hierarchy-design.md`.

### Why not folder nesting?

```
customers/DoD/Army/ASA-ALT/Funding-Office-X/LOGCAP/   ← avoid
```

- Paths churn when USAspending office names change
- Agents guess wrong path depth
- Same org appears under “customer” and “program” folders
- Duplication when LOGCAP spans multiple contracting offices

**Flat file** `customers/logcap.md` with `parent_customer: "[[army-logcap-funding-office]]"` is stable, grep-friendly, and matches Iris/Clio retrieve (slug + read).

### Layout (v2 — target)

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

### Federal customers — chain as data, not directories

Mental model:

```
Customer (federal market)
  └── Agency (e.g. Department of the Army)
        └── Subagency / Service (e.g. ASA(ALT), AFMC)
              └── Funding office (program / PEO / portfolio owner)
                    └── Contracting office(s) (awarding)
                    └── Program (LOGCAP, AFCAP) — when capture-relevant
```

#### `type` values (frontmatter)

| type | Use for | Example slug |
|------|---------|--------------|
| `customer_root` | Optional umbrella “US Federal customer” index | `us-federal-customers` (hub only) |
| `customer_agency` | Dept / top-tier agency | `department-of-the-army` |
| `customer_subagency` | Service, command, PEO-level org | `army-sustainment-command` |
| `customer_office_funding` | Funds requirements / owns program | `army-logcap-funding-office` |
| `customer_office_contracting` | Awards contracts | `acc-ri-contracting-division` |
| `customer_program` | Named program (LOGCAP, AFCAP) | `logcap`, `afcap` |

#### Required / recommended fields (customers)

```yaml
type: customer_program
name: "LOGCAP"
parent_customer: "[[army-logcap-funding-office]]"
also_related:
  - "[[department-of-the-army]]"
federal_codes:
  agency_code: "..."
  funding_office_code: "..."
  awarding_office_code: "..."
capture_notes: "..."
```

**LOGCAP / AFCAP:** `type: customer_program`, parent = **funding office** under **Dept of Army** or **Dept of Air Force** respectively (Iris proposes parent slugs at promote; Odysseus signs).

**Offices:** separate pages for **funding** vs **contracting** — do not merge unless Overwatch explicitly wants one stub.

#### How humans see the tree

1. **`customers/INDEX.md`** — role table + link to hub
2. **`customers/us-federal-customer-hub.md`** (optional) — markdown outline: Army branch, Air Force branch, top programs
3. **Any page** — “Chain up” section following `parent_customer`
4. **Later:** MC Vault or Obsidian Bases filter `type=customer_agency` — no new folders

**Iris:** when scouting USAspending, fill `federal_codes` + suggest `parent_customer`; never invent folder paths.

### Companies — by name, compounding intel

One file per company **name** (slug from canonical trade name).

```yaml
type: company
name: "KBR Services — Readiness & Sustainment"
org_role: self                    # only on our BU hub page
uei: "..."
parent_company: "[[kbr-inc]]"
sister_companies:
  - "[[kbr-subsidiary-x]]"
relationship_to_us:
  - teammate
  - competitor
pursuit_notes: "Often teams on LOGCAP IV; competes on RS IDIQs"
```

**Competitor ↔ partner nuance:** one page `companies/acme-defense-llc.md` — do **not** split into competitor vs partner folders. Update `relationship_to_us` and pursuit-specific notes in `pursuits/<slug>/` when role changes per opp.

**KBR:** `companies/kbr-services-readiness-sustainment.md` (`org_role: self`) links to `parent_company: [[kbr-inc]]` when that page exists. Capability depth stays in `global/domain_intel/capabilities/` (linked, not duplicated).

### Agent retrieval patterns

| Need | Agent action |
|------|----------------|
| Who funds LOGCAP? | retrieve `logcap` → follow `parent_customer` |
| Contracting office for opp X | pursuit frontmatter `funding_customer`, `contracting_customer` wikilinks |
| Competitor on this award | `companies/<slug>` + pursuit link |
| Don't duplicate agency | single slug; `trust` + manifest |
| SAM hierarchy | fields on **company** page (UEI, legal name) |
| USAspending hierarchy | fields on **customer** page (agency / office codes) |

### Odysseus entity gates (Phase 3b+)

| Gate | Rule |
|------|------|
| E1 | Only `customers/`, `companies/`, `INDEX.md` under entities after 3b |
| E2 | Every new customer page has valid `type` + `parent_customer` (except optional root hub) |
| E3 | Every company page is `type: company`; roles in frontmatter, not folders |
| E4 | No duplicate company under `customers/` |

### Phase 3b migration (after schema ack)

1. `agencies/*` → `customers/*` (retag `type`)
2. `competitors/*` + `company/*` → `companies/*`
3. Regenerate `entities/INDEX.md` + hub stub
4. `vault_lint` + fix wikilinks project-wide for moved slugs

**Not in 3b:** full Army/AF office trees — add incrementally as Iris/Clio promote from pursuits and USAspending.

**Locked Overwatch choices (2026-07-02):** federal hub `customers/us-federal-customer-hub.md` at 3b; LOGCAP/AFCAP parent slugs proposed by Iris, signed at promote; `companies/kbr-inc.md` stub **later**.

---

## 7. Capture ontology (summary)

- **Entities:** customers (typed), companies, programs, NAICS, vehicles — graph via wikilinks + frontmatter
- **Signals** (always cite raw): intensity, money flows, recompete/expiring, vehicles/pricing, geo concentration
- **Capture concepts:** win themes, discriminators, PP, teaming, pricing, risk, customer intimacy
- **Wikilinks:** `[[logcap]]` or `[[entities/customers/logcap]]` — prefer stable slug; set `aliases` for human names

---

## 8. Workflows

### Ingest (trusted promotion or approved automation)

1. Read raw signal (export, research URL, cited doc)
2. Check `review_id` / `award_key` dedup
3. Update 1 primary page + related pages (entity, `domain_intel`, `pursuits/<slug>/`, `relationships/`)
4. Append `## Added/Updated <date>` — never overwrite prior trusted sections
5. Update `index.md` + zone `INDEX.md` for each touched page
6. Append `log.md`: `## [date] ingest | Entity Name | review:<id>`

**Candidate path:** write under `generated-projections/` or `trust: candidate` until Overwatch promote.

### Query

1. Read `index.md` first
2. Open relevant pages via wikilinks
3. Synthesize with citations to wiki + raw sources
4. File valuable answers back as new pages or append sections

### Lint (periodic)

- Contradictions (same `award_key`, conflicting claims)
- Stale `last_updated` vs newer intel
- Orphan pages (no inbound wikilinks)
- Missing `Related` section
- Append lint summary to `log.md`: `## [date] lint | N issues`

---

## 9. Platform skills (use before vault edits)

Vendored under repo `skills/` when available:

| Skill | When |
|-------|------|
| `obsidian-markdown` | Wikilinks, properties, callouts (recommended) |
| `llm-wiki` | Karpathy ingest/query/lint patterns |
| `knowledge-triage` | Hermes intake routing |

**Agent bootstrap:**

> Read `foundation/ariadne-vault-schema.md`. You maintain `knowledge/` per Karpathy ingest/query/lint. Never modify cited raw sources as if they were wiki. Trusted writes only after Overwatch promotion.

---

## 10. Obsidian desktop (optional)

Point vault folder at **`knowledge/`** (absolute path on your machine).

- Graph view for hub/orphan detection
- Desktop edits should **append** and match schema
- Agents use INDEX + retrieve contract; graph view is for Overwatch delight (see doc 02 §4.2)

---

## 11. Implementation status (thread-os)

| Capability | Status |
|------------|--------|
| Flattened `knowledge/` tree | ✅ Item 4 Phase 1 |
| `ariadne-vault-schema.md` | ✅ Phase 3 (this file) |
| Entities 3b (`customers/`, `companies/`) | ✅ Phase 3b live (G2 ack 2026-07-02) |
| Automated lint cron | 📋 skill-guided |
| Semantic vault search | 📋 backlog |

---

**Schema version:** 3 (Ariadne Agent OS: flat `knowledge/`, entities rev 2, no capform-mandatory Layer 1)

**Supersedes:** `foundation/capture-llm-wiki.md` (schema_version 2) — keep `[[capture-llm-wiki]]` alias one release.