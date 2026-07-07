# Wave A — Top 10 capability rescout + vault gap notes

**Date:** 2026-07-02  
**Wave:** A (model uplift / vault item 4 hybrid rebuild)  
**Source inventory:** `agents/hephaestus/content/2026-07-02_vault-manifest-inventory.csv` (`domain_intel/capabilities/`, 46 rows, default **RESCOUT**)  
**Parent plan:** `agents/iris/content/2026-07-02_item4-iris-source-rescout.md`  
**Delegation:** `deleg_7d16de7f` task 2 (Wave A retry)  
**Status:** Rescout complete — **no** `knowledge/` writes (Iris staging only)  
**Live re-verify:** Tier-1 URLs fetched **2026-07-02** (retry pass)

---

## Executive summary

All **46** capability vault pages are `auto_generated: true` with **`has_citations_frontmatter: n`** in Hephaestus manifest. Wave A top 10 were rescouted against **Tier-1 KBR public URLs** (retrieved **2026-07-02**). Public copy is **richer and more current** than vault stubs on R&S IA, INSITE 3.0 branding, Vaault compliance wording, and EDEN (no trusted vault page).

**Post-rescout disposition (proposed):**

| Proposed tag | Count (top 10) | Meaning |
|--------------|----------------|---------|
| **REWRITE** | 9 | Promote after Clio distill + mandatory `citations:` / `retrieved:` |
| **KEEP** (meta only) | 1 | `owned-ip-digital-accelerators-discriminator` — structure OK; refresh cites to children |
| **NEW candidate → REWRITE** | 1 | EDEN — no trusted slug; extend `generated-projections/eden-edge-computing-candidate.md` |

---

## Selection method (from Hephaestus CSV + item4 plan)

1. Filter `path` prefix `global/domain_intel/capabilities/`.  
2. Prioritize **bid/no-bid discriminators**, **named IP**, **R&S LOGCAP lane**, and **compliance artifacts** cited in item4 Wave A queue.  
3. Exclude hub-only `capabilities-catalog.md` from top 10 (meta INDEX — separate REWRITE).  
4. Pair **FedRAMP/IL5** with `kbr-vaault` as one rescout unit (#3).

---

## Top 10 rescout matrix

### 1. `kbr-readiness-and-sustainment`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/kbr-readiness-and-sustainment.md` |
| **Manifest** | RESCOUT · `auto_generated: y` · citations: **n** |
| **Tier-1 primary URL** | [Readiness & Sustainment hub](https://solutions.kbr.com/readiness-and-sustainment/) |
| **Tier-1 child URLs (IA)** | [LOGCAP](https://solutions.kbr.com/readiness-and-sustainment/logcap) · [Base Operations](https://solutions.kbr.com/readiness-and-sustainment/base-operations) · [Prepositioned Stock](https://solutions.kbr.com/readiness-and-sustainment/prepositioned-stock) · [IPS](https://solutions.kbr.com/readiness-and-sustainment/integrated-productivity-solutions) · [Global Supply Chain](https://solutions.kbr.com/readiness-and-sustainment/global-supply-chain) · [Contingency](https://solutions.kbr.com/readiness-and-sustainment/contingency) · [Science Support & Logistics](https://solutions.kbr.com/readiness-and-sustainment/science-support-logistics) |
| **Rescout extract (2026-07-02)** | Hub brands under **Mission Technology Solutions**; lists seven service lines + “next generation asset management” and “digitally-focused logistics” — not fully mirrored in vault one-liner. |
| **Old vault gap** | Single paragraph; no child-page mapping; no `citations:`; empty `agencies` / `contract_vehicles` frontmatter; does not cite public 7-line R&S IA. |
| **Proposed after rescout** | **REWRITE** — hub page with wikilinks to child capability pages (or sections); cite hub + relevant child URL per claim; add MTS spin context footnote (Tier 3 press). |

---

### 2. `logcap-v-contract`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/logcap-v-contract.md` |
| **Manifest** | RESCOUT · `auto_generated: y` · citations: **n** |
| **Tier-1 primary URL** | [LOGCAP — R&S](https://solutions.kbr.com/readiness-and-sustainment/logcap) |
| **Tier-2** | [LOGCAP deep brochure](https://kbr.foleon.com/gs-us/logcap/) (linked from Tier-1) |
| **Rescout extract** | Public page emphasizes **24h mobilization / 72h full footprint**, expeditionary BOS, airfield, construction, food, housing, environmental compliance — **does not** name “LOGCAP V” or Army IDIQ award on this page. |
| **Old vault gap** | Asserts LOGCAP V prime awardee + “largest contingency logistics IDIQ” without URL; **TODO** for CPARS/task orders still open; no SAM/USAspending corroboration in vault. |
| **Proposed after rescout** | **REWRITE** — split **marketing claims** (Tier-1/2) from **contract facts** (Tier-4 USAspending/SAM award IDs in Iris note only until verified); do not invent LOGCAP V status if not on cited page. |

---

### 3. `kbr-vaault` + FedRAMP / IL5 pair

| Field | Value |
|-------|--------|
| **Vault paths** | `kbr-vaault.md`, `fedramp-high-authorization-vaault.md`, `fedramp-high-plus-il5-discriminator.md`, `dod-srg-impact-level-5-authorization-vaault.md` |
| **Manifest** | All RESCOUT · citations: **n** |
| **Tier-1 primary URL** | [KBR Digital Accelerators — Enterprise Technology § Vaault](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Corporate copy: Vaault is **SaaS mission platform**; “aligns with” **FedRAMP® High** and **DoD SRG IL5** baselines; multi-cloud tailoring for defense, national security, science, space, civilian missions. |
| **Old vault gap** | Vault prose matches theme but lacks **verbatim compliance cite** and `retrieved:`; discriminator pages duplicate narrative without `compliance_artifact` cross-refs to authoritative FedRAMP marketplace ID (not fetched this pass — **gap**). |
| **Proposed after rescout** | **REWRITE** — merge compliance claims onto `kbr-vaault` with corporate cite; child pages `fedramp-high-authorization-vaault` + `dod-srg-impact-level-5-authorization-vaault` as **KEEP structure / REWRITE cites**; add FedRAMP.gov package ID when Iris/Odysseus verifies (Tier-4). |

---

### 4. `kbrain`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/kbrain.md` |
| **Manifest** | RESCOUT · `proof_strength: medium` · citations: **n** |
| **Tier-1 primary URL** | [KBR Digital Accelerators — Artificial Intelligence § KBRain](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Positioned under **Generative AI** / LLM streamlining; broader AI section lists NLP/ML for space health, industrial monitoring, cognitive tactical PNT — vault omits these use-case branches. |
| **Old vault gap** | Generic “operational automation” stub; no product image section parity; no `citations:`; `proof_strength` not justified by public proof points. |
| **Proposed after rescout** | **REWRITE** — align to corporate AI section bullets; link `artificial-intelligence-capability` pillar; optional Tier-4 contract keyword search (541715) in separate Iris appendix. |

---

### 5. `insite-remote-operations-platform`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/insite-remote-operations-platform.md` |
| **Manifest** | RESCOUT · citations: **n** |
| **Tier-1 primary URL** | [INSITE 3.0 microsite](https://solutions.kbr.com/insite) |
| **Tier-2** | Corporate tile “INSITE 3.0” on Digital Accelerators page |
| **Rescout extract** | **INSITE 3.0** microsite — physics-informed AI, soft sensors, refining/petrochemicals/ammonia, explainable recommendations. **Corporate** Digital Accelerators § still describes legacy INSITE (remote plant advisory + “expanded to include aircraft systems”) — **split narrative** vs 3.0 microsite. |
| **Old vault gap** | **Stale product generation** (pre-3.0 / federal remote O&M emphasis); vault `proof_strength: medium` unsupported; missing microsite cite; aircraft expansion only on corporate page, not 3.0 landing. |
| **Proposed after rescout** | **REWRITE** — retitle/summary to **INSITE 3.0** where accurate; separate **federal remote O&M** applicability as analyst note if still valid (needs POC); cite microsite + corporate tile. |

---

### 6. `iron-stallion`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/iron-stallion.md` |
| **Manifest** | RESCOUT · citations: **n** |
| **Tier-1 primary URL** | [KBR Digital Accelerators — Data Analytics § Iron Stallion®](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | “Premier enterprise software” for SSA; data integration, workflow-aiding, automated analytics, C2 UX; customers: **USSF, coalition, commercial**. |
| **Old vault gap** | Substantively aligned but **zero citations**; duplicate story in `u-s-space-force-ssa-performance-iron-stallion.md` (not in top 10 — dedupe on REWRITE). |
| **Proposed after rescout** | **REWRITE** — cite corporate section; cross-link proof-point page; add `retrieved:` 2026-07-02. |

---

### 7. `crystalvista` + `quantum-pantheon`

| Field | Value |
|-------|--------|
| **Vault paths** | `crystalvista.md`, `quantum-pantheon.md` |
| **Manifest** | Both RESCOUT · `proof_strength: aspirational` (CrystalVista) · citations: **n** |
| **Tier-1 primary URL** | [KBR Digital Accelerators — Cybersecurity § CRYSTALVISTA and Quantum Pantheon](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Joint section: mesh network / encrypted transport (CRYSTALVISTA) + edge HPC nodes contextualizing data at creation (Quantum Pantheon); modular open systems; standalone or paired. |
| **Old vault gap** | Vault already pairs wikilinks but **inflates JADC2** without cite; Quantum Pantheon one-liner; no corporate § cite; aspirational strength unvalidated. |
| **Proposed after rescout** | **REWRITE** both — shared intro paragraph citing one corporate anchor; tone down uncited JADC2 unless added from cite; consider single “tactical edge fabric” parent with two children (Odysseus taxonomy). |

---

### 8. `intelligent-asset-management-iam`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/intelligent-asset-management-iam.md` |
| **Manifest** | RESCOUT · `proof_strength: low` · citations: **n** |
| **Tier-1 primary URL** | [KBR Digital Accelerators — Data Analytics § IAM](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Scalable cloud platform; AI/ML + domain expertise; greenfield/brownfield; downtime, working capital, top-quartile performance. |
| **Old vault gap** | Vault **understates** corporate copy and **over-cautions** federal fit without evidence; no cite; `proof_strength: low` may be overc conservative post-rescout. |
| **Proposed after rescout** | **REWRITE** — lift corporate claims with cite; retain honest **federal PP gap** as explicit “verification needed” block, not as sole lede. |

---

### 9. `owned-ip-digital-accelerators-discriminator`

| Field | Value |
|-------|--------|
| **Vault path** | `global/domain_intel/capabilities/owned-ip-digital-accelerators-discriminator.md` |
| **Manifest** | RESCOUT · `entity_type: strategic_theme` · citations: **n** |
| **Tier-1 primary URL** | [KBR Digital Accelerators (portfolio)](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) |
| **Rescout extract** | Corporate page claims **100+ initiatives**, six pillars, named brochures — supports “owned IP vs resale” theme. |
| **Old vault gap** | Good **proposal discipline** (“do not list all 19+ products”) but no cite; wikilinks to children without `citations:` on discriminator itself. |
| **Proposed after rescout** | **KEEP** narrative structure · **REWRITE** cites — anchor to portfolio URL + 3–8 child pages from this top-10 set (#3–8). |

---

### 10. EDEN (candidate — no trusted capability slug)

| Field | Value |
|-------|--------|
| **Vault path** | **None trusted** — `knowledge/generated-projections/eden-edge-computing-candidate.md` |
| **Manifest** | N/A in capabilities CSV |
| **Tier-1 primary URL** | [EDEN℠ microsite](https://solutions.kbr.com/eden) |
| **Rescout extract** | **Edge Data Extraction Node**; DDIL; LVC training at edge; cyber resilience; platform agnostic; POC **Jason Gray**; handout PDF on site. |
| **Old vault gap** | **Full gap** — public marketed product with no `domain_intel/capabilities/eden*.md`; prior brief `agents/iris/content/2026-07-02_eden-intel-brief.md` has cites but vault candidate file empty/missing body at retrieve. |
| **Proposed after rescout** | **REWRITE** candidate v2 → Clio → Odysseus promote to `capabilities/eden-edge-data-extraction-node.md` (slug TBD); Tier-4 USAspending by name still **not found** — do not claim contract PP. |

---

## Cross-cutting gaps (all top 10)

| Gap | Evidence | Wave A fix |
|-----|----------|------------|
| No `citations:` frontmatter | Hephaestus CSV `has_citations_frontmatter: n` for 45/46 auto pages | Mandatory on promote |
| LOGCAP V / award facts | Marketing URLs ≠ contract registry | Tier-4 SAM + USAspending appendix in `agents/iris/content/` |
| INSITE generational drift | Vault ≠ INSITE 3.0 microsite | REWRITE #5 |
| MTS branding | R&S site header “Mission Technology Solutions” | Note on #1 hub REWRITE |
| EDEN trusted absence | Only candidate projection | #10 promote path |

---

## Handoffs

| To | Action |
|----|--------|
| **Clio** | Wave A REWRITE queue (rows 1–8, 10); Shipley-neutral distill |
| **Odysseus** | Sign-off on KEEP/REWRITE tags; EDEN promote gate |
| **Hephaestus** | Manifest row updates post-ratification; lint `citations:` on capabilities |

---

## Sources (retrieved 2026-07-02)

- [R&S hub](https://solutions.kbr.com/readiness-and-sustainment/)
- [LOGCAP](https://solutions.kbr.com/readiness-and-sustainment/logcap)
- [KBR Digital Accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators)
- [INSITE 3.0](https://solutions.kbr.com/insite)
- [EDEN℠](https://solutions.kbr.com/eden)
- Inventory: `agents/hephaestus/content/2026-07-02_vault-manifest-inventory.csv`
- Prior: `agents/iris/content/2026-07-02_item4-iris-source-rescout.md`, `agents/iris/content/2026-07-02_eden-intel-brief.md`

---

## Related

- `agents/hermes/content/2026-07-02_vault-item4-execution-plan.md`
- `agents/odysseus/content/2026-07-02_item4-odysseus-hybrid-gate.md`