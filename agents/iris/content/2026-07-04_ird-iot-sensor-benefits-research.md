# IR&D IoT sensors — cited benefits research (generators, HVAC, facilities)

**Date:** 2026-07-04  
**Agent:** Iris  
**Audience:** Leadership sync (Emily Buckman, Kevin Gaudette) — IR&D IoT pivot  
**Use:** Fresh, **numbered** claims for customer conversations; pair with `agents/hermes/content/2026-07-04_ird-iot-leadership-sync.md`

---

## How to use this brief

| Tier | Meaning | Rule for slides / talking points |
|------|---------|----------------------------------|
| **Tier 1** | Primary or authoritative source (federal guide, GAO, peer-reviewed review, major consulting primary publication) | **Required citation** beside any percentage, dollar figure, or ROI multiple |
| **Tier 2** | Credible industry / program body (ACEEE, IFMA, vendor-neutral FM research) | Use for directional support; prefer Tier 1 for hard numbers |
| **Tier 3** | Case study, blog, or vendor marketing with a specific site outcome | Illustrate only — label as *single-site / vendor* |

**Scope:** IoT + condition monitoring / predictive maintenance on **generators**, **HVAC**, and **broader facilities infrastructure** (power, steam, BAS/EMIS), with emphasis on **federal-adjacent** FM (GSA, FEMP, deferred maintenance).

---

## Executive summary (leadership one-liner)

Benefits are **real but uneven**: federal O&M guidance and GAO both show **5–20% energy** upside and **8–40% maintenance-cost** upside when moving from reactive/preventive to **condition-based / predictive** programs — but **GSA still lacked portfolio-level quantified ROI** for smart-building sensor stacks as of GAO-18-200, and customers hesitate because **upfront cost, cyber, integration, and weak local business cases** routinely stall installs despite “common knowledge” ROI.

**Strongest federal ammo:** DOE FEMP O&M best practices (PNNL), GSA smart-buildings narrative + GAO findings, deferred-maintenance cost of **inaction** (PBRB/GSA portfolio).

---

## Tier 1 — Quantified claims (cite required)

### Downtime, availability, and unproductive time

| Claim | Equipment / context | Tier 1 source |
|-------|---------------------|---------------|
| Poor maintenance strategies can reduce an asset’s **productive capacity by 5–20%**; unplanned downtime costs industries an estimated **$50 billion/year** | Cross-industry / fixed assets | Deloitte, *Predictive Maintenance: Deloitte’s Approach* (2022) — [PDF](https://www2.deloitte.com/content/dam/Deloitte/us/Documents/process-and-operations/us-predictive-maintenance.pdf) |
| Digital maintenance/reliability transformations can increase **asset availability by 5–15%** | Heavy industry / integrated digital reliability | McKinsey, *Digitally enabled reliability: Beyond predictive maintenance* (2018) — [article](https://www.mckinsey.com/capabilities/operations/our-insights/digitally-enabled-reliability-beyond-predictive-maintenance) |
| **5–15%** reduction in facility downtime (capacity freed) | Predictive maintenance program outcomes | Deloitte PDF (2022), *client-derived ranges* — same link as above |
| Predictive maintenance typically reduces machine downtime by **30–50%** and increases machine life by **20–40%** | Manufacturing (McKinsey manufacturing analytics) | McKinsey, *Manufacturing: Analytics unleashes productivity and profitability* (2017) — cited in McKinsey maintenance corpus; cross-check [digitally enabled reliability](https://www.mckinsey.com/capabilities/operations/our-insights/digitally-enabled-reliability-beyond-predictive-maintenance) for 5–15% / 18–25% maintenance framing |
| Well-orchestrated predictive maintenance **minimizes catastrophic failures**, allows scheduling to **reduce overtime**, and **decreases equipment or process downtime** | Federal facilities O&M | DOE FEMP / PNNL, *O&M Best Practice: Maintenance Approaches* — [PNNL page](https://www.pnnl.gov/projects/om-best-practices/maintenance-approaches) citing FEMP 2010 guide |

### Energy, fuel, and utility spend

| Claim | Equipment / context | Tier 1 source |
|-------|---------------------|---------------|
| O&M programs targeting **energy efficiency can save 5–20%** on energy bills **without significant capital investment** | Whole-building federal/commercial O&M | PNNL / FEMP 2010 (via [maintenance approaches](https://www.pnnl.gov/projects/om-best-practices/maintenance-approaches)); also FEMP guide summary [OandM.pdf](https://www1.eere.energy.gov/femp/pdfs/OandM.pdf) |
| Properly functioning **predictive maintenance: 8–12% cost savings** vs preventive-only; facilities heavy on reactive maintenance may see **>30–40%** savings opportunities | HVAC, rotating equipment, federal sites | PNNL predictive maintenance section — [maintenance approaches](https://www.pnnl.gov/projects/om-best-practices/maintenance-approaches); detailed case economics in FEMP Ch. 6 [om_6.pdf](https://www1.eere.energy.gov/femp/pdfs/om_6.pdf) (e.g., roof IR program **~$2.94M** avoided vs **$3M** replacement; oil-change interval extension **>$20k** in 9 months; air-system ultrasound **~$75,900/yr** energy) |
| Independent surveys cited in FEMP guide: predictive program initiation — **ROI ~10×**, **breakdowns ↓35–45%**, **downtime ↓45–55%**, **maintenance costs ↓25–30%** | Industrial average (FEMP cites survey aggregates) | FEMP O&M Guide excerpt — [om_5.pdf](https://www1.eere.energy.gov/femp/pdfs/om_5.pdf) |
| IoT in smart buildings may decrease **energy consumption up to ~30%** and **operating expenses ~20%**; barriers include **~15% of project budget** upfront IoT cost | Literature synthesis (smart buildings) | MDPI *Buildings* systematic review (2024) — [10.3390/buildings14113446](https://www.mdpi.com/2075-5309/14/11/3446) |
| **~34%** energy savings in a monitored university building case (CO₂ + smart controls) | Higher-ed facilities, HVAC/ventilation | Franco et al., *Sustainability* (2024) — [10.3390/su17010111](https://www.mdpi.com/2071-1050/17/1/111) |
| **Variable frequency drives: 15–50%** pump/motor energy; **smart thermostat: 5–10%** HVAC; integrated smart building **30–50%** savings in otherwise inefficient existing buildings | HVAC & whole-building smart retrofits | ACEEE *Smart Buildings* (2017) — [Report A1701 PDF](https://www.aceee.org/sites/default/files/publications/researchreports/a1701.pdf) |
| **~10%** energy savings from smart building initiative ≈ **$0.25M/year** (single corporate portfolio example) | Office portfolio | ACEEE A1701 case table (Microsoft / Warnick 2016) — same PDF |
| Low-cost sensors + retrofit BAS can reduce consumption **20–30%** in small/medium commercial buildings | SMB commercial | ACEEE A1701 citing Roth et al. 2005 — same PDF |

### Maintenance cost, deferred maintenance, and lifecycle

| Claim | Equipment / context | Tier 1 source |
|-------|---------------------|---------------|
| Digital reliability programs: **maintenance costs ↓18–25%** (with 5–15% availability) | Asset-intensive operations | McKinsey (2018) — [digitally enabled reliability](https://www.mckinsey.com/capabilities/operations/our-insights/digitally-enabled-reliability-beyond-predictive-maintenance) |
| **5–20%** labor productivity gain; **10–30%** inventory reduction → **5–20%** carrying-cost reduction | PdM program ranges | Deloitte PDF (2022) |
| **~25%** of dollar savings in federal **ESPC** M&V reports attributed to **O&M and other non-energy** cost reductions (not just kWh) | Federal facilities ESPC | DOE FEMP M&V guidance — [om_savings_guidance.pdf](https://www.energy.gov/sites/prod/files/2018/03/f49/om_savings_guidance.pdf) |
| GSA **deferred maintenance** forces **emergency stop-gap spend** (example: **>$1.6M** temporary garage repairs) and **tenant exit risk** when assets fail | Federal real property | PBRB, *Deferred Maintenance in GSA's Portfolio* (Mar 2026) — [PDF](https://www.pbrb.gov/files/2026/03/Deferred-Maintenance-in-GSAs-Portfolio-March-5-2026.pdf) |
| Smart building tech install **~$48k–$155k** per building (incremental); **limited quantified portfolio benefits** in GAO review | GSA smart buildings (meters + GSAlink) | GAO **GAO-18-200** (Jan 2018) — [product page](https://www.gao.gov/products/gao-18-200) |
| GSA smart program **perceived** benefits: earlier fault ID, contractor monitoring; **GSAlink “avoided cost” estimates too imprecise** for enterprise ROI | GSA GSAlink / fault detection | GAO-18-200 — same |

### Generators and emergency power (monitoring / fuel / readiness)

| Claim | Equipment / context | Tier 1 source |
|-------|---------------------|---------------|
| Standby generators: **preventive + predictive maintenance + regular testing** required for highest reliability; monitor **oil pressure, coolant, voltage, frequency**, fuel rate, run hours | Federal / critical standby gen | PNNL *Standby Generators* O&M best practice — [standby-generators](https://www.pnnl.gov/projects/om-best-practices/standby-generators) |
| **~70%** of backup generators in critical-infrastructure survey could run **>24 hours**; diesel backup duration **mean ~5 days** (fuel logistics drive mission length) | U.S. critical facilities inventory | ANL / DHS-style facility survey — [Phillips 2016 PDF](https://publications.anl.gov/anlpubs/2016/05/127089.pdf) |
| DoD **~77%** of federal energy use (context for generator/fuel efficiency at scale) | Military / federal energy | CRS / DoD energy cited in public FM commentary — use for *mission fuel* narrative; pair with local site data |

### Safety, IAQ, and risk

| Claim | Equipment / context | Tier 1 source |
|-------|---------------------|---------------|
| Effective O&M **mitigates hazards from deferred maintenance**; reduces **IAQ** legal/productivity risk | Federal buildings | PNNL maintenance approaches / FEMP 2010 |
| PdM: **improved worker and environmental safety** (fewer catastrophic failures) | Predictive vs reactive | PNNL predictive maintenance benefits list — [maintenance approaches](https://www.pnnl.gov/projects/om-best-practices/maintenance-approaches) |
| DNV/Deloitte-style PdM deployments: **safety/health/environmental risks ↓~14%** (solar sector example in secondary summary) | Cited via McKinsey-aligned secondary | Com4 blog summarizing McKinsey + Deloitte — prefer **Deloitte PDF** for 5–15% downtime band |

---

## Tier 2 — Supporting narrative (numbers optional)

| Theme | Source |
|-------|--------|
| GSA deploying **smart sensors** across **70+** buildings for IAQ/environmental monitoring (**$80M** initiative) | Facilities Dive (Jun 2024) — [GSA smart building tech](https://www.facilitiesdive.com/news/gsa-smart-building-tech-upgrades-federal-facilities-buildings/719768/) |
| GSA building systems upgrades: consider **predictive maintenance** (thermography, ultrasonic), **EMIS**, **submetering** | GSA High-Performance Buildings — [building systems upgrades](https://www.gsa.gov/governmentwide-initiatives/federal-highperformance-buildings/highperformance-building-clearinghouse/workplace-strategies/project-guidance/building-systems-upgrades) |
| FEMP **EMIS** / **AFDD** = condition-based maintenance pathway; ties monitoring to **work orders** and persistence of savings | DOE FEMP — [EMIS capabilities](https://www.energy.gov/cmei/femp/energy-management-information-system-capabilities) |
| IFMA: IoT on **HVAC, elevators, electrical**; vibration alerts → work orders before failure | IFMA *FMJ* predictive maintenance (Jul 2025) — [fmj.ifma.org](https://fmj.ifma.org/predictive-maintenance) |
| Leanheat-style IoT heating: **5%** maintenance cost ↓, **10–20%** energy ↓, **15–30%** peak capacity ↑ (multi-family; transferable logic for central plant) | Global ESCO / IEA report — [DWGReport.pdf](https://energyefficiencyhub.org/wp-content/uploads/2022/10/DWGReport.pdf) |

---

## Tier 3 — Illustrative case outcomes (do not generalize without label)

| Outcome | Label |
|---------|--------|
| **28%** energy spend reduction (**$920k/yr**), 45 public buildings | Municipal portfolio — vendor case (Oxmaint, 2026) |
| **12–24 month** payback on IoT sensors; **15–25%** energy optimization; avoided chiller failure **$35k–$85k** | Commercial property Mgmt — Envigilance cost blog (2026) |
| Predictive HVAC monitoring **~25%** maintenance cost ↓, **~50%** downtime ↓ (some case studies) | FM vendor blog — BrandPoint / iiWorld secondary |

---

## Equipment-specific talking points

### Generators

- **Pain:** NFPA/EPA exercise + fuel quality failures are **silent** until outage; fuel and loading inefficiency burn **mission dollars** (DoD-scale energy share).
- **IoT layer:** Continuous **fuel level/flow**, **battery**, **oil pressure/coolant**, **run-hour** and load testing verification (PNNL standby gen); aligns with **condition-based** service vs calendar PM.
- **Cite for leadership:** PNNL standby generator monitoring; ANL backup duration/fuel-type statistics for **resilience** framing.

### HVAC (often **~40%** of office building energy — industry rule-of-thumb; use ACEEE/FEMP ranges in proposals)

- **Pain:** Small faults → **15–25%** efficiency drift (degraded coils, refrigerant, capacitors) — large utility line item.
- **IoT layer:** Supply/return ΔT, amperage, cycle patterns, **AFDD** / EMIS fault rules (FEMP EMIS page).
- **Cite:** ACEEE smart HVAC rows; Franco **34%** case; MDPI **up to 30%** energy synthesis.

### Broader facilities infrastructure (BAS, steam, traps, roofs, compressed air)

- **Pain:** Reactive spend **crowds out** capital; federal **deferred maintenance** spiral (PBRB).
- **IoT layer:** Ultrasonic/thermography/IR — **documented** FEMP case savings (steam traps, roof IR, compressed air).
- **Cite:** FEMP **om_6.pdf** case economics; PBRB GSA deferred maintenance.

---

## Why customers still hesitate (despite “everyone knows” ROI)

Use these in leadership/customer discovery — they appear across **GAO, MDPI, McKinsey, and Deloitte**:

| Barrier | Evidence |
|---------|----------|
| **Weak or missing quantified business case** at portfolio level | GAO-18-200: GSA could not use GSAlink avoided-cost estimates as actual savings; limited enterprise benefit data |
| **Upfront cost & integration** (~**15%** of smart-building project budget; **$48k–$155k** incremental smart stack) | MDPI barriers; GAO install cost range |
| **Cybersecurity** on Internet-connected building OT | GAO-18-200: smart tech cyber risk; GSA moved systems to secured network |
| **Organizational**: limited BAS literacy, contractor **buy-in**, change fatigue | GAO implementation challenges; Deloitte “inadequate change management” / pilot stall |
| **PdM not universal**: ML PdM only economic on **high-impact, well-documented** failure modes or **large identical fleets** | McKinsey 2018: not a panacea; simpler threshold monitoring often enough |
| **Savings offset by analytics cost** on wrong assets | McKinsey: predictive savings can be offset by model cost if mis-scoped |
| **Funding mechanics**: sensors compete with **prospectus/capital** and **service-center O&M** buckets; deferred maintenance eats **emergency** dollars first | PBRB GSA narrative |
| **Contractor incentives**: FM contracts reward **ticket closure**, not **data-driven** maintenance | Industry pattern — validate per account in discovery |

**Customer conversation pivot:** Start with **one critical asset class** (e.g., standby gen + chilled water) tied to **mission outage cost** or **known federal pain** (deferred maintenance, ESPC O&M savings line, FEMP 5–20% energy).

---

## Recommended “slide-ready” Tier-1 bullets (pick 5–7)

1. **5–20%** facility energy from better O&M alone — **FEMP/PNNL**  
2. **8–12%** maintenance cost vs PM-only; **30–40%+** if still reactive-heavy — **FEMP/PNNL**  
3. **5–15%** availability / **18–25%** maintenance cost — **McKinsey** digital reliability  
4. **5–15%** downtime reduction band — **Deloitte** PdM ranges  
5. **$50B/yr** industry unplanned downtime tax — **Deloitte** (context slide)  
6. **Up to ~30%** energy / **~20%** opex — **MDPI Buildings** review (IoT smart buildings)  
7. Federal **ESPC**: **~25%** of verified savings often **O&M-related** — **DOE FEMP M&V**  
8. **Deferred maintenance** → multi-million **stop-gap** spend + tenant loss — **PBRB/GSA**  
9. GSA smart buildings: **proven fault detection**, **enterprise ROI still maturing** — **GAO-18-200** (sets realistic tone)

---

## Bibliography (12 core Tier-1 / Tier-2 citations)

1. Pacific Northwest National Laboratory / DOE FEMP. *O&M Best Practice: Maintenance Approaches* (FEMP 2010). https://www.pnnl.gov/projects/om-best-practices/maintenance-approaches  
2. DOE FEMP. *Operations & Maintenance Best Practices Guide*, Release 3.0 — Ch. 5–6 (predictive technologies & cases). https://www1.eere.energy.gov/femp/pdfs/om_6.pdf  
3. DOE FEMP. *Operations & Maintenance Best Practices Guide* — industrial PdM survey aggregates. https://www1.eere.energy.gov/femp/pdfs/om_5.pdf  
4. DOE FEMP. *Determining and Verifying O&M Savings Guidance*. https://www.energy.gov/sites/prod/files/2018/03/f49/om_savings_guidance.pdf  
5. DOE FEMP. *Energy Management Information System Capabilities* (AFDD / condition-based maintenance). https://www.energy.gov/cmei/femp/energy-management-information-system-capabilities  
6. U.S. GAO. **GAO-18-200**, *Federal Buildings: GSA Should Establish Goals and Performance Measures to Manage the Smart Buildings Program* (2018). https://www.gao.gov/products/gao-18-200  
7. Public Buildings Reform Board. *Deferred Maintenance in GSA's Portfolio* (Mar 2026). https://www.pbrb.gov/files/2026/03/Deferred-Maintenance-in-GSAs-Portfolio-March-5-2026.pdf  
8. McKinsey & Company. *Digitally enabled reliability: Beyond predictive maintenance* (2018). https://www.mckinsey.com/capabilities/operations/our-insights/digitally-enabled-reliability-beyond-predictive-maintenance  
9. Deloitte Development LLC. *Predictive Maintenance: Deloitte's Approach* (2022). https://www2.deloitte.com/content/dam/Deloitte/us/Documents/process-and-operations/us-predictive-maintenance.pdf  
10. American Council for an Energy-Efficient Economy. *Smart Buildings: Using Smart Technology to Save Energy in Existing Buildings*, Report A1701 (2017). https://www.aceee.org/sites/default/files/publications/researchreports/a1701.pdf  
11. Poyyamozhi, M., et al. *IoT—A Promising Solution to Energy Management in Smart Buildings* (systematic review). *Buildings* 14(11):3446 (2024). https://doi.org/10.3390/buildings14113446  
12. Franco, A., et al. University building monitoring case. *Sustainability* 17(1):111 (2024). https://doi.org/10.3390/su17010111  

**Supplemental (generators / resilience):** PNNL standby generators — https://www.pnnl.gov/projects/om-best-practices/standby-generators ; Phillips, J.A. *Onsite and Electric Power Backup Capabilities at Critical Infrastructure Facilities* (ANL, 2016). https://publications.anl.gov/anlpubs/2016/05/127089.pdf

---

## Gaps / next intel (for Iris follow-on)

- Site-specific **outage cost/hour** for target customers (generators + HVAC cascade).  
- Contract vehicle language for **EMIS / IoT / CBM** on LOGCAP, FACILITY, or ESPC task orders.  
- Named **competitor** IoT FM offerings on active RS pursuits (award-based only).

---

## Handoff

- **Clio:** Pull Tier-1 bullets into customer one-pager when warm intros land.  
- **Odysseus:** IR&D + cyber + data-rights checklist for sensor pilots.  
- **Hermes:** Map claims to relationship-led use-case hypotheses from leadership sync.