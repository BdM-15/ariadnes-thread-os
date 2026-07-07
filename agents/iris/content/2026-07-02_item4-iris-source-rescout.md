# Item 4 addendum — Iris source-anchored rescout plan

**Date:** 2026-07-02  
**Batch:** `deleg_481f8c63` (hybrid vault rebuild)  
**Parent:** `agents/hermes/content/2026-07-02_vault-item4-hybrid-rebuild-brainstorm.md`  
**Scope:** KBR public sites ↔ `knowledge/global/domain_intel/`; capture concepts ↔ USAspending KEEP criteria  
**Status:** Plan only (manifest Phase 1) — no vault body writes by Iris

---

## Executive summary

Current **46** `domain_intel/capabilities/` pages are overwhelmingly **`auto_generated: true`** / `source_module: company_capabilities` with **no public URL citations** in frontmatter (grep: **0** `citations:` hits). Prose often aligns with [KBR Digital Accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) and R&S marketing, but **audit trail is weak** for Wave A rebuild.

**Rescout spine:** two canonical trees plus product microsites:

| Spine | Canonical URL | Vault targets |
|-------|---------------|---------------|
| **R&S BU** | [solutions.kbr.com/readiness-and-sustainment](https://solutions.kbr.com/readiness-and-sustainment/) | `entities/company/kbr-services-readiness-sustainment.md` + sustainment capability pages |
| **Digital Accelerators** | [kbr.com/.../kbr-digital-accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) | `domain_intel/capabilities/*` + discriminators |

**42** `global_wiki/capture/concepts/` pages share a **USAspending lineage pattern** (`## Key signals from USASpending`). **Do not bulk-archive** — apply manifest KEEP rules below; Iris tags each concept in Wave C.

---

## Canonical rescout URL inventory (fetch order)

### Tier 1 — Company SSOT (every Wave A page must cite ≥1 Tier-1 URL)

1. [Readiness & Sustainment hub](https://solutions.kbr.com/readiness-and-sustainment/)
2. [LOGCAP](https://solutions.kbr.com/readiness-and-sustainment/logcap)
3. [Base Operations](https://solutions.kbr.com/readiness-and-sustainment/base-operations)
4. [Prepositioned Stock](https://solutions.kbr.com/readiness-and-sustainment/prepositioned-stock)
5. [Integrated Productivity Solutions (IPS)](https://solutions.kbr.com/readiness-and-sustainment/integrated-productivity-solutions)
6. [Global Supply Chain](https://solutions.kbr.com/readiness-and-sustainment/global-supply-chain)
7. [Contingency](https://solutions.kbr.com/readiness-and-sustainment/contingency)
8. [Science Support & Logistics](https://solutions.kbr.com/readiness-and-sustainment/science-support-logistics)
9. [KBR Digital Accelerators (corporate)](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators)

### Tier 2 — Named accelerator / product microsites (pair to capability slug)

| Public product | Microsite (when present) | Existing vault slug (indicative) |
|----------------|--------------------------|----------------------------------|
| INSITE | [solutions.kbr.com/insite](https://solutions.kbr.com/insite) | `insite-remote-operations-platform` |
| EDEN℠ | [solutions.kbr.com/eden](https://solutions.kbr.com/eden) | **candidate only** (`eden-edge-computing-candidate`) — **gap** |
| Vaault | corporate page § Enterprise Technology | `kbr-vaault`, FedRAMP/IL5 pages |
| ENCOMPASS / Digital Twin | corporate page § Digital Engineering | `encompass-digital-twin-platform` |
| CleanSpend | corporate page § Data Analytics | `cleanspend-carbon-analysis` |
| IAM, KBRain, RESAN, Iron Stallion®, WRAITH, Athena, HAL, CSOM, CRYSTALVISTA, Quantum Pantheon, Cyber Range, Artemis, Skypath, TTMT, Dash C3 | corporate page sections | matching `domain_intel/capabilities/*` slugs |

### Tier 3 — Corporate context (cite once on company hub, not every capability)

- [MTS spin-off intent (press)](https://www.kbr.com/en/insights-news/press-release/kbr-announces-strategic-intent-spin-off-mission-technology-solutions) — affects “Mission Technology Solutions” branding on R&S site (verified 2026-07-02 on live pages).

### Tier 4 — Federal corroboration (Iris `content/` only until promote)

- [USAspending Advanced Search](https://www.usaspending.gov/search) — recipient **KBR** / **KBR Services**; NAICS clusters for R&S vs digital (see playbook below).
- SAM.gov — vehicle holdings (`active-gwac-and-idiq-holdings`, LOGCAP/AFCAP heritage pages).

---

## domain_intel ↔ public gap matrix (2026-07-02 snapshot)

### Strong name alignment (rewrite with cites, likely KEEP → REWRITE)

Digital accelerator **named IP** pages in vault map cleanly to corporate accelerator copy: `kbrain`, `crystalvista`, `quantum-pantheon`, `iron-stallion`, `wraith`, `athena-data-management-suite`, `hal-adaptive-learning-framework`, `csom-scheduling-optimization-module`, `resan`, `cleanspend-carbon-analysis`, `insite-remote-operations-platform`, `viaverse-estates-intelligence-platform`, `intelligent-asset-management-iam`, `kbr-cyber-range`, `artemis-uas`, `skypath-assured-containment`, `ttmt-tracking-and-targeting`, `dash-c3-decision-support`, `kbr-vaault`, `encompass-digital-twin-platform`.

Pillar **rollup** pages: `digital-engineering-capability`, `artificial-intelligence-capability`, `data-analytics-capability`, `cybersecurity-capability`, `autonomous-systems-capability`, `enterprise-technology-capability`, `kbr-digital-accelerators-portfolio`.

### R&S service lines — public IA vs vault

| Public R&S line (Tier 1) | Vault coverage | Rescout action |
|--------------------------|----------------|----------------|
| LOGCAP | `logcap-v-contract`, RS BU prose | Rescout LOGCAP URL; verify LOGCAP V wording vs vault |
| Base Operations | folded in `kbr-readiness-and-sustainment` | **REWRITE** or split child page; cite base-operations URL |
| Prepositioned Stock | thin / folded | **REWRITE** from URL or new capability stub → candidate |
| IPS | unclear dedicated page | **REWRITE** from IPS URL |
| Global Supply Chain | thin / folded | **REWRITE** from URL |
| Contingency | folded in RS prose | **REWRITE** from contingency URL |
| Science Support & Logistics | thin | **REWRITE** from URL |

### Gaps / risks

| Issue | Evidence | Action |
|-------|----------|--------|
| **No public citations on capabilities** | 0/46 `citations:` in frontmatter | Wave A: mandatory `citations:` + `retrieved:` on promote |
| **EDEN trusted gap** | Public [EDEN microsite](https://solutions.kbr.com/eden); vault = candidate | Prioritize rescout; hand candidate v2 to Clio (`2026-07-02_eden-intel-brief.md`) |
| **Contract / proof pages without single product URL** | `afcap-contract-heritage`, `logcap-v-contract`, GWAC holdings, proof points | Tier 4 USAspending + SAM; cite award/vehicle IDs in Iris note, not invented prose |
| **Discriminators** | `owned-ip-digital-accelerators-discriminator`, cleared workforce, FedRAMP, etc. | KEEP theme; rewrite claims to trace to Tier 1–2 product cites |
| **`domain-intel.md` hub text stale** | Still says “no company names” while `capabilities/` is KBR-specific | **Odysseus** — hub vs company-intel zone split (see taxonomy brainstorm) |

### Suggested Wave A “top 10” capability rescouts (Iris → Clio)

1. `kbr-readiness-and-sustainment` (hub + 7 R&S child URLs)  
2. `logcap-v-contract`  
3. `kbr-vaault` + `fedramp-high-authorization-vaault` / IL5 pair  
4. `kbrain`  
5. `insite-remote-operations-platform`  
6. `iron-stallion`  
7. `crystalvista` + `quantum-pantheon`  
8. `intelligent-asset-management-iam`  
9. `owned-ip-digital-accelerators-discriminator` (meta, cites to 3–8)  
10. **EDEN** — promote path from candidate after microsite rescout  

---

## Capture concepts — USAspending KEEP criteria (unchanged)

Per parent brainstorm **salvage rule** + USAspending subset:

A concept in `global_wiki/capture/concepts/` is **KEEP** (possibly light edit) only if **all** hold:

1. **Defined term** — “What it means” is atomic and non-duplicative of Shipley doctrine in `global_wiki/`.  
2. **USAspending or intel cite** — body includes `## Key signals from USASpending` with field-level mapping **or** explicit federal data lineage (e.g. `follow-the-money`, `pricing-buckets`). Iris adds **1–2 sentence cite** in manifest row: which USASpending dimensions the concept uses.  
3. **Used in agent path** — referenced from `ROUTER.md`, capture skills, `thread-role`, INDEX hubs, or retrieve contract (Hephaestus to confirm).

**Scoring (default):**

| Score | Manifest tag | Meaning |
|-------|--------------|---------|
| 3/3 | **KEEP** | Retain; optional cite refresh |
| 2/3 | **REWRITE** | Re-author from USASpending plain-English + app label |
| ≤1/3 | **DROP** or **ARCHIVE** | Move to `generated-projections/archived/rebuild-2026/` |

**Bias:** Terms in capture OS router/skills → **KEEP candidacy** until Iris disproves USAspending lineage.

**Pre-scan (2026-07-02):** **41/42** files contain `## Key signals from USASpending` or explicit USASpending prose in lede. **`sam-live-discovery`** is SAM-primary but **pairs** USASpending history — tag **KEEP** with dual-source note.

**Deferred stub:** `usaspending-plain-english` (seed in `scripts/seed_deferred_wikilink_stubs.py`) — **Clio/Hephaestus** to materialize for agent field semantics; Iris does not block concept KEEP on stub absence.

### Concept triage deliverable (Wave C)

Iris produces `agents/iris/content/2026-07-02_item4-capture-concepts-manifest.csv` (or `.md` table):

`slug | KEEP|REWRITE|DROP | usaspending_cite_sentence | router_link_y/n | notes`

Odysseus ratifies before archive moves.

---

## USAspending research playbook (company intel corroboration)

Reuse pattern from `agents/iris/content/acme-cloud-services-rfp-intel.md`:

| Use case | Filters | Vault consumer |
|----------|---------|----------------|
| R&S scale / LOGCAP lane | Contracts; recipient KBR family; NAICS **561**/**562**/**928** (validate per opp); DoD; FY2020–FY2025 | `logcap-v-contract`, `proven-sustainment-scale-discriminator` |
| Digital / IT / cyber | NAICS **541512**, **541519**, **541715**; keywords from accelerator name | Product proof points, `petabyte-scale-cloud-migration-proof-point` |
| Vehicle concentration | Award type IDIQ/GWAC; parent award IDs | `active-gwac-and-idiq-holdings`, concepts `vehicle-holders`, `idiq-task-orders` |
| Pricing posture | `pricing-buckets`, extent competed | Concepts layer + Odysseus MS gates |

**Rule:** Raw USAspending tables stay in **`agents/iris/content/`**; vault gets **synthesized** claims with award ID cites — per `vault-intel-taxonomy-brainstorm` (SAM/USAspending raw not mixed into wiki as dumps).

---

## Execution phases (Iris-owned)

| Step | Output | Owner |
|------|--------|-------|
| 1. Fetch Tier 1–2 URLs; store hashes/retrieval dates in rescout log | `agents/iris/content/2026-07-02_kbr-public-rescout-raw.md` (optional appendix) | Iris |
| 2. Complete gap matrix + Wave A top 10 | This document § matrices | Iris |
| 3. Per-capability **source map** (slug → primary URL → REWRITE/KEEP) | Table in raw rescout or CSV | Iris |
| 4. Concept manifest tags | `item4-capture-concepts-manifest` | Iris |
| 5. Candidates with cites | `knowledge/thread/generated-projections/*-candidate.md` | Iris draft → **Clio** distill → **Odysseus** promote |
| 6. Promote freeze until manifest signed | — | Odysseus |

**Iris will not** patch `knowledge/global/domain_intel/` or `global_wiki/` directly (FILE_MUTATION: `agents/iris/` only).

---

## Handoffs

| To | Payload |
|----|---------|
| **Clio** | Wave A rewrite queue; EDEN candidate v2; Shipley-neutral prose on promoted pages |
| **Odysseus** | KEEP/ARCHIVE manifest; MS gate alignment for intel-dependent fields |
| **Hephaestus** | Lint rule: trusted capability requires `citations:`; concept KEEP list for link graph |
| **Hermes** | Ratify manifest; board quests per wave |

---

## Sources (this plan)

- [KBR R&S solutions hub](https://solutions.kbr.com/readiness-and-sustainment/) — retrieved 2026-07-02  
- [KBR Digital Accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) — retrieved 2026-07-02  
- [EDEN microsite](https://solutions.kbr.com/eden) — indexed via search; full rescout queued  
- Vault inventory: `knowledge/global/domain_intel/capabilities/` (46 files); `knowledge/global/global_wiki/capture/concepts/` (42 files)  
- Prior intel: `agents/iris/content/2026-07-02_eden-intel-brief.md`  
- USAspending method: `agents/iris/content/acme-cloud-services-rfp-intel.md`  

---

## Related

- `agents/hermes/content/2026-07-02_vault-item4-hybrid-rebuild-brainstorm.md`  
- `knowledge/entities/company/kbr-services-readiness-sustainment.md`  
- `agents/odysseus/content/2026-07-02_vault-cleanse-program.md`