# IR&D IoT sensor pilots — customer objection playbook (EDEN framing)

**Date:** 2026-07-04  
**Board / quest:** `ird-iot-leadership-sync-2026-07-04` · IR&D IoT customer engagement  
**Agent:** Odysseus (strategy / gates)  
**Vault retrieve:** `knowledge/global/domain_intel/capabilities/eden-edge-data-extraction-node.md` · `agents/iris/content/2026-07-02_eden-intel-brief.md` · `knowledge/global/domain_intel/capabilities/intelligent-asset-management-iam.md`  
**Upstream:** Hermes `agents/hermes/content/2026-07-04_ird-iot-leadership-sync.md`

---

## Executive summary

IR&D IoT sensor pilots stall on three recurring objections: **legacy or dated plant/equipment**, **fear of sensor data leaving the facility**, and **skepticism of off-prem or public cloud**. Public KBR positioning for **EDEN℠ (Edge Data Extraction Node)** — DDIL-capable, **stakeholder-owned edge**, open/modular integration, and cyber resilience — maps cleanly to those fears **without** claiming federal contract past performance for EDEN (Tier-4 USAspending by **“EDEN”** name **not found** per Iris §10 and trusted capability page).

Use this playbook for **relationship-led discovery calls** and leader-brokered intros. Pair **IAM** (predictive maintenance, brownfield) only as **corporate Tier-1 language** when the customer wants fleet/asset outcomes; do **not** cite DoD IAM deployments without Iris Tier-4 verification.

**Gate recommendation:** **Conditional proceed** on customer conversations — **Green** for talk tracks grounded in Tier-1 EDEN microsite; **Yellow** until POC (Jason Gray) confirms BU ownership, pilot artifacts, and any customer-specific proof; **Red** if capture invents EDEN or IAM federal PP.

---

## Cite gate (mandatory before external use)

| Claim | Allowed? | Source tier | Gate |
|-------|----------|-------------|------|
| EDEN℠ = Edge Data Extraction Node; DDIL; LVC-at-edge; stakeholder-owned edge; anti–vendor lock-in; platform agnostic; open/modular COTS/GOTS | **Yes** | Tier-1 [KBR EDEN microsite](https://solutions.kbr.com/eden) | Green |
| Public POC Jason Gray; I/ITSEC / Analytics & Cloud placement | **Yes** | Tier-1 microsite + [KBR I/ITSEC 2023](https://www.kbr.com/en/insights-news/event/interserviceindustry-training-simulation-and-education-conference-iitsec) | Green |
| EDEN federal contract award / past performance by product name | **No** | Tier-4 not found | **Red — do not state** |
| IAM predictive maintenance; greenfield/brownfield; cloud platform | **Yes** (corporate) | Tier-1 [KBR Digital Accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) | Green |
| IAM DoD / federal deployments as primary discriminator | **No** until verified | Iris §8 | **Red — do not state** |
| “Our EDEN pilot at [Agency X]” or implied sole-source proof | **No** | None | **Red — POC + legal review** |

---

## Objection → mitigation matrix

| # | Customer objection (voice) | Underlying fear | EDEN-aligned mitigation | IAM pairing (optional) | Risk gate |
|---|----------------------------|-----------------|-------------------------|------------------------|-----------|
| O1 | “Our equipment is **20–40 years old** — sensors won’t talk to it / not worth instrumenting.” | Sunk cost, integration risk, pilot embarrassment | **Edge-first extraction**: process and act on **telemetry at the edge** without requiring a full rip-and-replace or cloud-native estate. **Open/modular COTS/GOTS** framing — attach to existing SCADA/PLC/export paths where feasible; edge normalizes and buffers before any uplink. | **Brownfield** IAM language: improve asset performance on **existing estates** (corporate claim only); edge layer handles **time-critical** alarms locally. | **Yellow** — validate actual interfaces on site; no promised adapters without engineering assessment |
| O2 | “We **can’t let sensor data** leave the building / go to your network.” | Data exfiltration, OPSEC, ITAR/EAR, audit exposure | **Stakeholder-owned edge**: mission owner retains custody; analytics and **first-line decisions** on **premises or tactical enclave**. **DDIL** design — meaningful operation when **intermittent or denied** connectivity; transmit **aggregates, alerts, or policy-approved slices** only when connected. Cyber resilience per public EDEN themes. | IAM as **optional downstream** when customer approves connectivity — not the default pilot architecture. | **Green** for architecture story; **Yellow** for data classification — Odysseus + customer ISSO/AO sign-off before demo data flows |
| O3 | “**No cloud** — we need **on-prem** only / we don’t trust vendor SaaS.” | Sovereignty, latency, continuity of operations | **Platform agnostic** (bare metal + cloud-**ready**, not cloud-**required**). Position pilot as **edge node on customer metal** or approved enclave; cloud as **future option**, not pilot gate. Anti–vendor lock-in supports **exportable** stacks and customer-operated lifecycle. | Do **not** lead with IAM cloud platform for O3-heavy buyers; mention IAM only if they accept **hybrid** (edge infer + periodic sync). | **Green** for EDEN on-prem story; **Red** if talk track implies mandatory KBR-hosted multi-tenant cloud |

---

## Shipley-safe talk tracks (by objection)

### O1 — Legacy / dated equipment

**Do say:**

- “We’re not asking you to replace the plant first. The pilot question is: **what signal already exists** — vibration, temperature, pressure, runtime counters — and can we **extract and interpret it at the edge** so you get actionable insight on **your** timeline?”
- “EDEN is positioned for **denied, degraded, intermittent, limited** environments — that includes **messy industrial estates**, not only greenfield sites.”
- “We’ll scope **one line or one asset class** with your maintainers in the room so integration risk is visible week one.”

**Do not say:**

- “We’ve deployed EDEN on dozens of federal contracts.” (No Tier-4 EDEN PP.)
- “Plug-and-play on any legacy system.” (Over-promise.)

**Proof ask (internal, before customer meeting):** POC confirms reference architectures, handout PDF, and any **sanitized** demo or lab story — not contract numbers unless verified.

---

### O2 — Fear of data transmission

**Do say:**

- “**Default posture: process locally, transmit minimally.** Your edge, your rules — we align to your **data handling and classification** before any sensor ships.”
- “EDEN public positioning emphasizes **stakeholder-owned edge** — you decide what leaves, when, and to whom.”
- “If the link is down, the pilot should still prove **local alerting and logging** — that’s the DDIL value proposition.”

**Do not say:**

- “All data is encrypted so it’s fine to stream everything to the cloud.” (Dismisses sovereignty concern.)
- “KBR will host your operational data.” (Unless explicitly scoped and approved.)

**Escalation:** Customer AO / cybersecurity — document **data flow diagram** (sensor → edge → optional egress) as MS2-style artifact for Clio if pursuit formalizes.

---

### O3 — Off-prem / cloud concerns

**Do say:**

- “Pilot success criteria can be **100% on-prem inference and dashboard** inside your boundary. EDEN is **platform agnostic** — bare metal in your rack is in-bounds.”
- “Cloud-ready means **if** you later want a hybrid model, you’re not locked in — not that you must use cloud now.”
- “Open and modular integration reduces **vendor lock-in** — you retain operational control.”

**Do not say:**

- “Our IAM cloud will ingest all your sensors.” (Wrong lead for cloud-averse buyers; IAM federal PP unverified.)
- “Edge is just a stepping stone to our SaaS.” (Undermines trust.)

**IAM bridge (only when customer opens the door):** “For **enterprise asset performance** across many sites, KBR also markets **Intelligent Asset Management** as a **corporate** analytics platform — we’d only bring that in **after** edge pilot success and **your** connectivity policy allows.”

---

## Pilot design guardrails (IR&D + customer engagement)

| ID | Risk | Mitigation | Owner |
|----|------|------------|-------|
| R1 | **Invented past performance** for EDEN or IAM | Cite gate table; Iris re-run USAspending if POC supplies contract keywords | Odysseus + Iris |
| R2 | **ITAR/EAR/export** or CUI mishandling on sensor telemetry | Early customer compliance contact; no live gov data in IR&D demo without approval | Odysseus |
| R3 | **Over-scoped integration** on legacy kit | Time-boxed discovery; single-asset MVP; engineering spike before executive promise | Hermes + technical lead |
| R4 | **Implied sole-source** via trademarked product pitch | Use “public KBR capability”; confirm BU/RS alignment with Jason Gray before branded pursuit | Hermes + POC |
| R5 | **Cloud-first IAM** mismatch with O3 customers | Lead EDEN edge architecture; IAM optional and corporate-cited only | Odysseus |

---

## Competitive framing (discovery only — not battlecard)

If customer compares to **tactical edge boxes** (e.g., Parsons SN/GN, Norseman Odin's Edge), stay on **differentiation hypotheses** from Iris brief — **LVC/disconnected training**, **open/modular ownership model**, KBR analytics portfolio adjacency — and **validate with POC** before written capture. Do not disparage competitors; anchor on **customer-owned edge** and **pilot fit**.

---

## Recommended follow-ups

| Lane | Agent | Action |
|------|--------|--------|
| POC / product | Hermes → Jason Gray | Confirm RS BU ownership, pilot collateral, integration patterns for industrial IoT (not only LVC) |
| Federal evidence | Iris | USAspending/SAM sweep **only** with internal contract numbers or program names — not “EDEN” name alone |
| Customer one-pager | Clio | Living Briefing slice: one objection + one talk track per target account |
| Tooling | Hephaestus | **No build** until pilot scope and data gate signed |

---

## Handback to Hermes

- Use this playbook in **leader-brokered intro** prep (Emily / Kevin sync outcomes).
- **pWin impact:** Improves **story fit** for edge-averse industrial/facility buyers; **does not** raise evidence tier until POC + Tier-4 paths exist.
- **MS analog:** Treat as **pre–Phase 0 discovery** enablement — not a gate pass for a specific SAM notice.

---

## Sources (authoritative for this doc)

1. `knowledge/global/domain_intel/capabilities/eden-edge-data-extraction-node.md`  
2. `agents/iris/content/2026-07-02_eden-intel-brief.md`  
3. `knowledge/global/domain_intel/capabilities/intelligent-asset-management-iam.md`  
4. https://solutions.kbr.com/eden  
5. Hermes: `agents/hermes/content/2026-07-04_ird-iot-leadership-sync.md`