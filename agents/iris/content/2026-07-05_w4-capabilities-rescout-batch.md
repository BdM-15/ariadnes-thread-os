# W4 — Manifest-tail capability rescout batch (12 slugs)

**Date:** 2026-07-05  
**Wave:** W4 (overnight vault build — manifest tail after W2 lighthouse + W3 accelerators)  
**Delegation:** Overnight runbook `agents/hermes/content/2026-07-05_overnight-vault-runbook.md`  
**Inventory:** `agents/hephaestus/content/2026-07-02_vault-manifest-inventory.csv` (capabilities zone)  
**Exclusions:** Slugs promoted in W2 (Iris Wave A / lighthouse) and W3 (Digital Accelerators batch) — not rescouted here.  
**Status:** Rescout complete — **no** `knowledge/` writes (Iris staging only; Clio → Odysseus gate for hybrid rebuild)

---

## Executive summary

Rescouted the **next 12** capability stubs that remain `auto_generated: true` in manifest CSV order (lines 12–35, skipping W2/W3-promoted rows). All twelve lack `citations:` / `retrieved:` frontmatter and rely on TODO placeholders or uncited assertions.

**Tier-1 spine (retrieved 2026-07-05):**

| Tier | URL | Use |
|------|-----|-----|
| 1 | https://www.kbr.com/en/what-we-do/kbr-digital-accelerators | Pillars, products, cleared workforce, 100+ initiatives, Vaault, cloud migration |
| 1 | https://www.kbr.com/en | MTS / STS positioning, spin-off banner |
| 1 | https://solutions.kbr.com/readiness-and-sustainment/ | R&S / contingency heritage (AFCAP context) |
| 1 | https://www.kbr.com/en/insights-news/press-release/kbr-lands-seat-64b-air-force-contract-global-contingency-and | AFCAP V IDIQ seat ($6.4B ceiling, 2020) |
| 1 | https://www.kbr.com/en/insights-news/press-release/kbrs-mission-technology-solutions-awarded-two-task-orders-supporting-us-air-force-operations-southwest-asia | AFCAP V task orders (2026) |
| 2 | https://www.kbr.com/sites/default/files/documents/2024-10/KBR-Sustainability-and-Corporate-Responsibility-Report-2023.pdf | CMMC / ISO certifications (compliance artifacts) |

**Disposition (proposed for Clio rewrite queue):**

| Tag | Count | Notes |
|-----|-------|--------|
| **REWRITE** | 12 | All batch slugs |
| **KEEP** (structure only) | 0 | — |
| **ARCHIVE** | 0 | — |

---

## Selection method (W4 manifest tail)

1. Filter `global/domain_intel/capabilities/` where file still has `auto_generated: true` (24 remain repo-wide).  
2. Sort by Hephaestus manifest path order.  
3. Skip slugs already **promoted** with hybrid rewrites: W2 lighthouse set (e.g. `kbrain`, `logcap-v-contract`, `iron-stallion`, …) and W3 eight (`kbr-digital-accelerators-portfolio`, pillar hubs, Athena, ENCOMPASS, HAL, Dash C3).  
4. Take **first 12** remaining rows → this batch.

**W4 batch slugs (in order):**

1. `active-gwac-and-idiq-holdings`  
2. `afcap-contract-heritage`  
3. `artemis-uas`  
4. `artificial-intelligence-capability`  
5. `autonomous-systems-capability`  
6. `cleanspend-carbon-analysis`  
7. `cleared-workforce-at-scale-discriminator`  
8. `cleared-workforce`  
9. `cmmc-certification-status`  
10. `csom-scheduling-optimization-module`  
11. `enterprise-technology-capability`  
12. `hundred-plus-digital-initiatives-proof-point`

**Still auto_generated after W4 (12):** `kbr-cyber-range`, `kbr-inc`, `petabyte-scale-cloud-migration-proof-point`, `proven-sustainment-scale-discriminator`, `quality-management-system-certification`, `resan`, `safety-critical-compliance-proof-point`, `skypath-assured-containment`, `ttmt-tracking-and-targeting`, `u-s-space-force-ssa-performance-iron-stallion`, `viaverse-estates-intelligence-platform`, `wraith` — next Iris batch.

---

## REWRITE table (Clio primary)

| # | Slug | Vault `proof_strength` | Tier-1 anchor | Old vault gaps | Proposed |
|---|------|------------------------|---------------|----------------|----------|
| 1 | `active-gwac-and-idiq-holdings` | aspirational | No public vehicle catalog on kbr.com (Tier-4 SAM/GSA expected) | Entire body is TODO; `type: concept` / `entity_type: program` placeholder | **REWRITE** — honest **open inventory** page; cite Tier-4 only when Iris/SAM appendix added; do not invent OASIS+/SeaPort awards from careers JD text alone |
| 2 | `afcap-contract-heritage` | medium | AFCAP V press (2020 IDIQ seat; 2026 task orders) + R&S hub | Asserts prime heritage without URL; TODO for iteration/CPARS | **REWRITE** — separate **contract facts** (press cites) from **scope marketing** (R&S); state AFCAP **V** explicitly where press does |
| 3 | `artemis-uas` | aspirational | Digital Accelerators § **Artemis UAS** | Substantively aligned to Tier-1 but zero cites; omits ~100 km/h tempo line and GNSS-denied / BVLOS detail from corporate copy | **REWRITE** — product page under `autonomous-systems-capability`; mandatory hub cite |
| 4 | `artificial-intelligence-capability` | aspirational | Digital Accelerators § **Artificial Intelligence** | Thin pillar stub; IAM/NLP/space health/PNT branches missing vs Tier-1; `kbrain` already promoted but pillar not | **REWRITE** — full pillar IA (Generative AI, NLP/ML, IAM) + wikilinks to `kbrain`, `intelligent-asset-management-iam` |
| 5 | `autonomous-systems-capability` | medium | Digital Accelerators § **Autonomous Systems** | Lists platforms without Tier-1 cites; should mirror corporate order (RDT&E, Artemis, Skypath, TTMT, Dash C3) | **REWRITE** — pillar hub; child links to batch-5+ products (`artemis-uas`, `skypath-assured-containment`, `ttmt-tracking-and-targeting`; `dash-c3` promoted W3) |
| 6 | `cleanspend-carbon-analysis` | low | Digital Accelerators § **CleanSpend powered by ENCOMPASS** | Federal caveat in vault is good; understates Tier-1 (scope 3, offshore O&G lead use case, minutes-to-results) | **REWRITE** — product page; tie to `encompass-digital-twin-platform`; retain federal fit **verification needed** block |
| 7 | `cleared-workforce-at-scale-discriminator` | low | Cybersecurity § intro (“highly cleared and skilled workforce”) | Discriminator unsubstantiated; duplicate theme with `cleared-workforce` | **REWRITE** — merge narrative with #8 or cross-link; **no headcount** until Tier-1/HR cite; proposal-use = transition-risk framing only |
| 8 | `cleared-workforce` | medium | Same Cybersecurity § intro | TODO for FSO/facility clearance; `entity_type: compliance_artifact` without artifact cite | **REWRITE** — compliance artifact page with corporate cite; open questions for TS/SCI counts |
| 9 | `cmmc-certification-status` | aspirational | 2023 Sustainability report (CMMC + ISO 27001 mention) | Empty TODO body | **REWRITE** — cite PDF for **existence** of CMMC program; **level / assessment date** = open question until Tier-1 CMMC marketplace or official KBR statement |
| 10 | `csom-scheduling-optimization-module` | aspirational | Digital Accelerators § **CSOM** | One paragraph; missing “entire solution space” / robustness wording from Tier-1 | **REWRITE** — Data Analytics product child; cite hub § |
| 11 | `enterprise-technology-capability` | medium | Digital Accelerators § **Enterprise Technology** (Vaault + Cloud Migration) | Vaault/IL5 claims need cite refresh (W2 promoted `kbr-vaault`); petabyte migration belongs in child `petabyte-scale-cloud-migration-proof-point` | **REWRITE** — pillar hub; wikilink Vaault + cloud proof child; do not duplicate FedRAMP package IDs without Tier-4 |
| 12 | `hundred-plus-digital-initiatives-proof-point` | medium | Hub intro (“catalyst behind more than **100 initiatives**”) | Thematically matches promoted `owned-ip-digital-accelerators-discriminator` / portfolio hub — risk of **triple redundancy** | **REWRITE** — short proof-point only; cite hub once; **require** named program wikilink (e.g. `iron-stallion`) per vault discipline |

---

## Per-slug rescout notes

### 1. `active-gwac-and-idiq-holdings`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/active-gwac-and-idiq-holdings.md` |
| **Tier-1 primary** | *None* — program catalog not published on corporate marketing IA |
| **Tier-2 signal** | Careers posts reference SeaPort-NxG / OASIS+ experience (not award proof) |
| **Rescout extract** | N/A for authoritative vehicle list |
| **Proposed after rescout** | **REWRITE** with explicit Tier-4 dependency |

### 2. `afcap-contract-heritage`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/afcap-contract-heritage.md` |
| **Tier-1 primary** | [AFCAP V $6.4B IDIQ (2020)](https://www.kbr.com/en/insights-news/press-release/kbr-lands-seat-64b-air-force-contract-global-contingency-and) |
| **Tier-1 secondary** | [AFCAP V task orders May 2026](https://www.kbr.com/en/insights-news/press-release/kbrs-mission-technology-solutions-awarded-two-task-orders-supporting-us-air-force-operations-southwest-asia) |
| **Rescout extract** | KBR held AFCAP III/IV since 2005; AFCAP V multiple-award IDIQ; ongoing task orders for transient aircraft + dining (SW Asia / Al Dhafra) |
| **Old vault gap** | No press URLs; “prime contractor heritage” undated |
| **Proposed after rescout** | **REWRITE** |

### 3. `artemis-uas`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/artemis-uas.md` |
| **Tier-1 primary** | [Digital Accelerators — Artemis UAS](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Sub-25 kg multirotor; GNSS-denied; BVLOS radios; in-house EO/IR + 2DOF gimbal; human-portable; rapid launch / ~100 km per hour flight (corporate) |
| **Old vault gap** | No `citations:`; `proof_strength: aspirational` despite named Tier-1 product |
| **Proposed after rescout** | **REWRITE** |

### 4. `artificial-intelligence-capability`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/artificial-intelligence-capability.md` |
| **Tier-1 primary** | [Digital Accelerators — Artificial Intelligence](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | “Strategically integrated… not AI for AI’s sake”; LLM/generative AI; NLP/ML for space health, industrial monitoring, cognitive tactical PNT; IAM cross-pillar |
| **Old vault gap** | Pillar stub only; missing sector branches and corporate tagline |
| **Proposed after rescout** | **REWRITE** |

### 5. `autonomous-systems-capability`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/autonomous-systems-capability.md` |
| **Tier-1 primary** | [Digital Accelerators — Autonomous Systems](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | RDT&E cloud environment; Artemis; Skypath containment; TTMT edge tracking; Dash C3 (promoted separately W3) |
| **Old vault gap** | Third-person “The company”; no cites; platform list not synced to Tier-1 order/wording |
| **Proposed after rescout** | **REWRITE** |

### 6. `cleanspend-carbon-analysis`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/cleanspend-carbon-analysis.md` |
| **Tier-1 primary** | [Digital Accelerators — CleanSpend](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Lifecycle carbon; scope 1/2/3; offshore platform O&G; ENCOMPASS-powered; minutes-level results |
| **Old vault gap** | `proof_strength: low` may be fair for federal but body lacks Tier-1 product copy |
| **Proposed after rescout** | **REWRITE** |

### 7–8. Cleared workforce pair

| Field | Value |
|-------|--------|
| **Vault paths** | `cleared-workforce-at-scale-discriminator.md`, `cleared-workforce.md` |
| **Tier-1 primary** | [Digital Accelerators — Cybersecurity § workforce](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | “Highly cleared and skilled workforce” at forefront of cybersecurity for gov + commercial |
| **Old vault gap** | Duplicate theme; both TODO on quantification |
| **Proposed after rescout** | **REWRITE** both — discriminator stays proposal-framing; artifact page holds compliance wording |

### 9. `cmmc-certification-status`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/cmmc-certification-status.md` |
| **Tier-1 primary** | [KBR Sustainability Report 2023 (PDF)](https://www.kbr.com/sites/default/files/documents/2024-10/KBR-Sustainability-and-Corporate-Responsibility-Report-2023.pdf) |
| **Rescout extract** | Report lists CMMC among certifications (alongside ISO 27001 for US locations) — **level not parsed on marketing site** |
| **Old vault gap** | Empty TODO only |
| **Proposed after rescout** | **REWRITE** with cite + **open questions** for level/C3PAO date |

### 10. `csom-scheduling-optimization-module`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/csom-scheduling-optimization-module.md` |
| **Tier-1 primary** | [Digital Accelerators — CSOM](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Enterprise scheduling; whole solution space; mission asset + infrastructure utilization; large/labor-intensive problems |
| **Proposed after rescout** | **REWRITE** |

### 11. `enterprise-technology-capability`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/enterprise-technology-capability.md` |
| **Tier-1 primary** | [Digital Accelerators — Enterprise Technology](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Vaault SaaS (FedRAMP High + DoD SRG IL5 alignment); petabyte-scale cloud migration incl. power/cooling and DC exit |
| **Old vault gap** | Pillar prose OK thematically; no cites; overlaps W2 `kbr-vaault` — needs hub cite not duplicate authorization package claims |
| **Proposed after rescout** | **REWRITE** |

### 12. `hundred-plus-digital-initiatives-proof-point`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/hundred-plus-digital-initiatives-proof-point.md` |
| **Tier-1 primary** | [Digital Accelerators hub intro](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | “More than 100 initiatives” across defense, national security, space, energy transition, infrastructure, industry-agnostic O&M |
| **Old vault gap** | Sector list narrower than Tier-1; no cite; overlaps portfolio hub / owned-IP discriminator |
| **Proposed after rescout** | **REWRITE** — minimal proof-point; dedupe with promoted portfolio pages |

---

## Cross-cutting gaps (W4 batch)

| Gap | W4 fix |
|-----|--------|
| No `citations:` / `retrieved:` | Mandatory on Clio promote |
| Pillar pages still stub while children promoted (AI, Enterprise, Autonomous) | REWRITE #4, #5, #11 first in Clio ordering |
| Compliance artifacts without Tier-1 (CMMC, GWAC) | PDF or Tier-4 appendix; label open questions |
| Redundant proof themes (100+, owned IP) | Clio dedupe against W3 portfolio + W2 discriminator |
| AFCAP / LOGCAP contract facts | Marketing ≠ registry — press cites OK for heritage; task order $/scope need date-stamped cites |

---

## Handoffs

| To | Action |
|----|--------|
| **Clio** | W4 REWRITE table → `generated-projections/*-rewrite-candidate.md` (12 rows) |
| **Odysseus** | Gate CMMC level claims; GWAC inventory honesty; AFCAP vs LOGCAP PP boundaries |
| **Hephaestus** | Manifest tag updates post-ratification; lint citations on promote |

---

## Sources (retrieved 2026-07-05)

- https://www.kbr.com/en/what-we-do/kbr-digital-accelerators  
- https://www.kbr.com/en  
- https://solutions.kbr.com/readiness-and-sustainment/  
- https://www.kbr.com/en/insights-news/press-release/kbr-lands-seat-64b-air-force-contract-global-contingency-and  
- https://www.kbr.com/en/insights-news/press-release/kbrs-mission-technology-solutions-awarded-two-task-orders-supporting-us-air-force-operations-southwest-asia  
- https://www.kbr.com/sites/default/files/documents/2024-10/KBR-Sustainability-and-Corporate-Responsibility-Report-2023.pdf  
- Prior waves: `agents/iris/content/2026-07-02_wave-a-top10-capability-rescout.md`, `agents/iris/content/2026-07-04_w3-accelerators-rescout-batch.md`

---

## Related

- `agents/hermes/content/2026-07-05_overnight-vault-runbook.md`  
- `agents/hephaestus/content/2026-07-02_vault-manifest-inventory.csv`  
- `ariadne-thread-os` → `references/vault-item4-hybrid-rebuild.md`