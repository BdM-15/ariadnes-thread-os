# W3 — Digital Accelerators rescout batch (first 8 slugs)

**Date:** 2026-07-04  
**Wave:** W3 (Clio ingestion — Digital Accelerators map + pillar hubs)  
**Tier-1 source:** [KBR Digital Accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators)  
**Retrieved:** 2026-07-04 (`web_extract` → `www.kbr.com-342d82fb76.md`)  
**Status:** Rescout complete — **no** `knowledge/` writes (Iris staging only; Odysseus gate + manifest row required for hybrid rebuild)

---

## Executive summary

Compared **8** accelerator/portfolio capability stubs under `knowledge/global/domain_intel/capabilities/` against the live Tier-1 hub. All eight are `auto_generated: true`, lack `citations:` / `retrieved:` frontmatter, and use generic third-person vault voice (“The company…”) where corporate copy is first-party and richer.

**Disposition (proposed for Clio rewrite queue):**

| Tag | Count | Slugs |
|-----|-------|--------|
| **REWRITE** | 8 | All batch slugs below |
| **KEEP** | 0 | — |
| **ARCHIVE** | 0 | — |

**Cross-cutting gaps (all slugs):** No Tier-1 URL cites; stale `last_updated: 2026-06-18`; MTS spin-off banner on hub not footnoted; Explore / brochure tiles (e.g. INSITE 3.0) not reflected on portfolio hub stub.

---

## Tier-1 extract anchors (hub)

- **Positioning:** “Shortening the distance between data and decision”; suite cuts distance between data and decision-making; benefits: speed to market, strategic/cost advantage, risk reduction, operational agility.
- **Scale claim:** Catalyst for **100+ initiatives** across defense, national security, space, energy transition, infrastructure, industry-agnostic O&M, and other areas.
- **Six pillars (public IA):** Digital Engineering · Artificial Intelligence · Data Analytics · Cybersecurity · Autonomous Systems · Enterprise Technology.
- **Context note:** Page header references strategic intent to spin off **Mission Technology Solutions** (investor link) — treat as Tier-3 corporate context, not capability proof.

---

## Per-slug gap table

| Slug | Vault `proof_strength` | Tier-1 alignment | Old vault gaps | Clio action |
|------|------------------------|------------------|----------------|-------------|
| `kbr-digital-accelerators-portfolio` | high | Strong thematic match to six pillars + 100+ initiatives | Missing hub tagline/value bullets; no brochure/Explore IA; no MTS spin footnote; no `citations:` | **REWRITE** — portfolio hub with pillar wikilinks + Tier-1 cite per claim |
| `cybersecurity-capability` | medium | Matches pillar intro + Cyber Range + CRYSTALVISTA / Quantum Pantheon | No verbatim product blurbs (mesh fabric, edge HPC, MOSA); cleared workforce asserted without cite; erroneous related link to `wraith` / `dash-c3` (those are analytics/autonomy products) | **REWRITE** — pillar page + child links to `kbr-cyber-range`, `crystalvista`, `quantum-pantheon` |
| `data-analytics-capability` | medium | Partial — lists Athena, HAL, CSOM, VIAverse, CleanSpend | Tier-1 **Data Analytics** section also names **INSITE**, **Iron Stallion**, **WRAITH** (separate vault pages exist but omitted from pillar inventory); no lifecycle “assess → model → test → deliver” narrative; industrial-origin caveat not on Tier-1 | **REWRITE** — full pillar product list aligned to Tier-1 § order; honest federal-mapping note retained |
| `digital-engineering-capability` | aspirational | Good coverage of ENCOMPASS twin, RESAN, automated engineering, DEE | Omits **Expert Modelling and Simulation Tools** bullet (sensors, BM C2, enterprise systems); `proof_strength` understates named IP on Tier-1 | **REWRITE** — add M&S ecosystem bullet; bump proof where cite-backed |
| `athena-data-management-suite` | aspirational | Core capability text matches Tier-1 Athena paragraph | Missing lead line “turns large, dynamic data sets into confident decision-making”; thin body (~1 para); `entity_type` frontmatter says `technology` but `type: concept`; weak related edges (`afcap-contract-heritage`) | **REWRITE** — product page with Tier-1 quote + team-environment emphasis |
| `encompass-digital-twin-platform` | medium | Aligns with “Digital Twin powered by ENCOMPASS” + lifecycle O&M | Does not tie **CleanSpend powered by ENCOMPASS** explicitly in body (only related link); no RESAN/digital-thread cross-link in prose | **REWRITE** — ENCOMPASS as platform parent for twin + CleanSpend cite |
| `hal-adaptive-learning-framework` | aspirational | Strong match to HAL (Harness for Adaptive Learning) Tier-1 copy | No Tier-1 cite; parent pillar is **Data Analytics** (not AI) — vault OK via `data-analytics-capability` but product page should state placement | **REWRITE** — M&S / black-box simulation use cases with corporate wording |
| `dash-c3-decision-support` | aspirational | Matches Dash C3 GUI / multi-sensor / uncooperative objects | Tier-1 places **Dash C3 under Autonomous Systems**, not Cybersecurity — vault `related` includes `cybersecurity-capability` as primary neighbor; should anchor under `autonomous-systems-capability` | **REWRITE** — fix pillar parentage in prose + links; sensor-fusion C2 framing retained |

---

## Slug detail (rescout notes)

### 1. `kbr-digital-accelerators-portfolio`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/kbr-digital-accelerators-portfolio.md` |
| **Tier-1 anchor** | Hub intro + pillar list (lines 46–66, cached extract) |
| **Rescout extract** | Six named pillars; 100+ client initiatives; sector list broader than vault’s “defense, national security, space, energy, and industrial” (adds energy transition, infrastructure, industry-agnostic O&M). |
| **Proposed after rescout** | **REWRITE** |

### 2. `cybersecurity-capability`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/cybersecurity-capability.md` |
| **Tier-1 anchor** | § Cybersecurity + Cyber Range + CRYSTALVISTA / Quantum Pantheon |
| **Rescout extract** | “Safeguarding critical data, systems and the newest global battlespace”; Cyber Range for incident response/tool testing without impacting mission systems; CRYSTALVISTA global mesh + Quantum Pantheon edge processing; modular open systems / interoperability. |
| **Proposed after rescout** | **REWRITE** |

### 3. `data-analytics-capability`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/data-analytics-capability.md` |
| **Tier-1 anchor** | § Data Analytics (CleanSpend, INSITE, VIAverse, Iron Stallion, WRAITH, Athena, HAL, CSOM) |
| **Rescout extract** | Full analytics pipeline narrative; INSITE expansion to aircraft systems on corporate page (compare INSITE 3.0 microsite in separate W3 pass). |
| **Proposed after rescout** | **REWRITE** |

### 4. `digital-engineering-capability`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/digital-engineering-capability.md` |
| **Tier-1 anchor** | § Digital Engineering (ENCOMPASS twin, RESAN, Automated Engineering, Expert M&S, Digital Engineering Environment) |
| **Rescout extract** | Expert M&S ecosystems for sensors, data processing, real-time battle management C2; hybrid-cloud DEE for MBSE across acquisition lifecycle. |
| **Proposed after rescout** | **REWRITE** |

### 5. `athena-data-management-suite`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/athena-data-management-suite.md` |
| **Tier-1 anchor** | Data Analytics § **Athena** |
| **Rescout extract** | “Large-scale data management, analysis, visualization and reporting suite”; automation + reporting in team environment. |
| **Proposed after rescout** | **REWRITE** |

### 6. `encompass-digital-twin-platform`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/encompass-digital-twin-platform.md` |
| **Tier-1 anchor** | Digital Engineering § **Digital Twin powered by ENCOMPASS** |
| **Rescout extract** | Forefront of digital project and digital twin delivery; insights in planning and O&M phases. |
| **Proposed after rescout** | **REWRITE** |

### 7. `hal-adaptive-learning-framework`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/hal-adaptive-learning-framework.md` |
| **Tier-1 anchor** | Data Analytics § **HAL** |
| **Rescout extract** | Automates exploration/exploitation of M&S tools; experimental design, adaptive sampling, ML for black-box repeatable systems. |
| **Proposed after rescout** | **REWRITE** |

### 8. `dash-c3-decision-support`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/dash-c3-decision-support.md` |
| **Tier-1 anchor** | Autonomous Systems § **Dash C3** (not Cybersecurity pillar) |
| **Rescout extract** | Interactive GUI; real-time SA; coordinates multiple sensing assets observing uncooperative object suites; user-adjustable parameters and display configuration. |
| **Proposed after rescout** | **REWRITE** |

---

## Handoff to Clio (W3)

1. Distill each **REWRITE** row into hybrid vault draft with mandatory `citations:` (Tier-1 URL + `retrieved:`).  
2. Portfolio + four pillar hubs first (`kbr-digital-accelerators-portfolio`, `digital-engineering-capability`, `data-analytics-capability`, `cybersecurity-capability`) then product children in this batch.  
3. Fix wikilink hygiene: `dash-c3-decision-support` → `autonomous-systems-capability`; remove spurious `wraith` / `dash-c3` from cybersecurity related set unless prose justifies cross-pillar reference.

---

## Sources

| Tier | URL | Use |
|------|-----|-----|
| 1 | https://www.kbr.com/en/what-we-do/kbr-digital-accelerators | Primary rescout for all 8 slugs |
| 3 | http://investors.kbr.com/news-and-events/spin-off-information | MTS spin context footnote only |