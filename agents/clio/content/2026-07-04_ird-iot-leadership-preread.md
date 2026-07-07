# IR&D IoT Sensors — leadership pre-read (sensor data capture)

**Audience:** Emily Buckman, Kevin Gaudette  
**Meeting:** IR&D IoT leadership sync — Thu 9 Jul or Fri 10 Jul 2026  
**Companion:** `agents/hermes/content/2026-07-04_ird-iot-leadership-sync.md`  
**Agent:** Clio · **Date:** 2026-07-04  
**Vault spine:** INSITE 3.0 (soft sensors), IAM, EDEN℠, Quantum Pantheon — Tier-1 public cites only; **no invented contract past performance**

---

## Why this note (30 seconds)

- IR&D IoT effort needs a **credible replacement use case** after the prior thread stopped.
- This one-pager frames **sensor data capture** as a KBR-shaped problem — not “more hardware” — and where **EDEN℠** sits in the stack.
- **Ask today:** relationship-led hypotheses and intros, not a final product pitch.

---

## Sensor data capture — value proposition (KBR lens)

**Customer pain (generic, relationship-led discovery):**

- **Too much raw telemetry, too little decision-quality signal** at the edge and in the back office.
- **Gaps in physical instrumentation** (cost, safety, legacy plants, denied environments) — need **inferred** state, not only new sensors.
- **DDIL / disconnected ops** break the assumption that cloud analytics always sees live streams.
- **Vendor lock-in and integration tax** when every site ships a different IoT stack.

**What “good” looks like for a replacement use case** (align to leadership sync criteria):

| Criterion | Question for warm intros |
|-----------|---------------------------|
| **Customer / mission** | Who owns the asset or training mission and feels the pain in **O&M dollars or readiness**? |
| **Pain** | Is the bottleneck **capture**, **fusion**, **inference**, or **action**? |
| **Data** | What is already sensored vs what must be **soft-sensed** or **edge-processed**? |
| **Deploy path** | Pilot scope: brownfield hook-up, tactical kit, or training/LVC edge — and who signs the IR&D → program bridge? |

**KBR capability story (vault — public language only):**

| Layer | Capability | Capture / sense narrative |
|-------|------------|---------------------------|
| **Infer when you cannot instrument** | **INSITE 3.0** | Physics-informed AI and **soft sensors** for anomaly prediction and explainable guidance — industrial asset operations (refining, petrochemicals, ammonia, etc.) per microsite. |
| **Predict and optimize estates** | **IAM** | Cloud intelligent asset management — predictive analytics across greenfield/brownfield facilities; lead with corporate accelerator claims; **federal PP verification needed** before primary discriminator use. |
| **Extract and act at the edge** | **EDEN℠** | **Edge Data Extraction Node** — process, analyze, and act on mission data in **DDIL**; disconnected **LVC** training; platform-agnostic, open/modular integration; public POC Jason Gray. |
| **Contextualize at creation** | **Quantum Pantheon** | Tactical edge HPC to process and contextualize **sensor and mission data where it is created** — adjacent to EDEN/transport fabric; pair only when RFP needs compute + mesh. |

**One-line value prop for leadership conversations:**

> KBR can help customers move from **noisy IoT feeds** to **trusted operational signal** — using **soft sensors and asset AI** where instrumentation is thin, and **edge extraction (EDEN)** where connectivity is not guaranteed — without claiming a federal contract line we have not verified.

---

## Where EDEN℠ fits (stack picture)

```
[ Physical IoT / platform sensors ]
           ↓
[ Edge: EDEN℠ — extract, buffer, process in DDIL; LVC/training workloads ]
           ↓ optional fusion
[ INSITE 3.0 soft sensors / IAM analytics — estate-level prediction & optimization ]
           ↓
[ Enterprise / cloud when link is available ]
```

- **EDEN is not “the sensor.”** It is the **edge data extraction and resilience layer** — stakeholder-owned edge, anti–vendor-lock-in positioning per public microsite.
- **Natural adjacency:** EDEN (DDIL extraction) + **Quantum Pantheon** (onboard/sensor contextualization) + **INSITE** (soft sensors when direct measurement is impractical).
- **Honest gap:** USAspending search by **“EDEN” name not found** (Iris rescout §10) — use IR&D and leader intros to **earn** pilot evidence; do not cite contract PP in customer meetings until Tier-4 confirmed.

**POC / gate:** Confirm BU ownership and deliverable mix (hardware / software / services) with **Jason Gray** before EDEN leads every IoT thread.

---

## Likely objections — rebuttal framing (no over-claim)

| Objection | Rebuttal angle (stay cite-safe) |
|-----------|----------------------------------|
| **“We already picked an IoT platform.”** | EDEN public positioning emphasizes **open/modular COTS/GOTS** and **mission-owner edge** — integration and extraction, not rip-and-replace mandate. Pilot = **interoperability slice**, not enterprise swap. |
| **“Sensors are commodity; our SI handles it.”** | Differentiate on **soft sensors + physics-informed AI** (INSITE 3.0) and **DDIL edge extraction** (EDEN) — where commodity stacks fail on **inference quality** and **disconnected ops**. |
| **“Show me DoD past performance for this exact stack.”** | Acknowledge gap explicitly: IAM and EDEN lead with **Tier-1 marketing**; **federal PP verification needed** (vault open questions). IR&D purpose is **validated pilot** on a leader-sponsored thread — not a fabricated award narrative. |
| **“We’ll drown in data.”** | Frame IAM + INSITE as **signal over volume** — predictive maintenance, explainable recommendations, top-quartile performance language (IAM corporate §) where customer cares about **working capital and downtime**. |
| **“Security / export / partner rules block a pilot.”** | Defer to **IR&D guardrails** (funding bucket, disclosure, export, partner rules) — Odysseus checklist; design pilot scope **with** compliance up front, not after demo. |
| **“Why KBR vs Parsons / Norseman / integrators?”** | Use Iris competitor set for **battle prep only** — Parsons tactical edge nodes, Norseman DDIL edge AI, etc. (`agents/iris/content/2026-07-02_eden-intel-brief.md`). KBR angle to validate: **LVC-at-edge**, KBR analytics portfolio adjacency, **integrated RS + digital accelerators** story — **not** invented win themes. |

---

## Federal / market context — Iris placeholders

*Sections below to be populated when parallel Iris research lands. Until then, do not read stats aloud as verified in customer meetings.*

### Market and demand signals
<!-- IRIS_PLACEHOLDER: agents/iris/content/2026-07-04_ird-iot-market-demand.md (or equivalent) -->
- **Placeholder:** Military/tactical edge market sizing, Army Project Convergence–style edge trials, JADC2 / 5G-at-edge demand — cite Iris primary sources.
- **Vault seed (not a substitute):** Federal tactical edge demand notes in `agents/iris/content/2026-07-02_eden-intel-brief.md` § Market / customer demand signals.

### Account / program intelligence
<!-- IRIS_PLACEHOLDER: SAM / USAspending / named customer threads from leadership map -->
- **Placeholder:** Named targets from Emily/Kevin relationship map — contract vehicles, incumbents, sensor/edge keywords.
- **Discipline:** No award claims by product name without Iris Tier-4 pull (EDEN name search: **not found** to date).

### Competitor / alternative offeror snapshot
<!-- IRIS_PLACEHOLDER: agents/iris/content/2026-07-04_ird-iot-competitor-edge.md -->
- **Placeholder:** Short table — tactical edge vendors, DDIL IoT stacks, soft-sensor/analytics peers.
- **Vault seed:** EDEN intel brief § Competitor / alternative-offeror signals.

---

## Compliance / engagement guardrails — Odysseus placeholder

<!-- ODYSSEUS_PLACEHOLDER: agents/odysseus/content/2026-07-04_ird-iot-guardrails-checklist.md -->
- **Placeholder:** IR&D funding bucket, customer disclosure, export-controlled data paths, partner/teaming rules before pilot LOI.
- **Meeting ask:** Emily/Kevin flag non-negotiables in the sync so capture does not over-promise in intros.

---

## Suggested leadership talking points (relationship-led)

1. **Pivot honesty:** Prior IoT use case is **no longer viable** — we are seeking **one credible sponsor-led pilot hypothesis**, not internal ideation only.
2. **Problem class:** “**Sensor data capture**” = physical sensing **plus** soft sensing **plus** edge extraction when the network is wrong.
3. **KBR hooks to test:** INSITE soft sensors (industrial), IAM estate analytics, **EDEN for DDIL extraction** — stack depends on customer vertical; do not lead every intro with EDEN until POC confirms fit.
4. **Next 14 days:** 2–3 priority threads, **≥2 brokered intros**, Iris pulls on named accounts, Clio one-pager per warm intro if helpful.

---

## Sources (this document)

| Artifact | Role |
|----------|------|
| `knowledge/global/domain_intel/capabilities/insite-remote-operations-platform.md` | INSITE 3.0, soft sensors |
| `knowledge/global/domain_intel/capabilities/intelligent-asset-management-iam.md` | IAM cloud analytics |
| `knowledge/global/domain_intel/capabilities/eden-edge-data-extraction-node.md` | EDEN℠ trusted capability |
| `knowledge/global/domain_intel/capabilities/quantum-pantheon.md` | Edge sensor contextualization |
| `agents/iris/content/2026-07-02_eden-intel-brief.md` | Edge demand + competitor seeds |
| `agents/iris/content/2026-07-02_wave-a-top10-capability-rescout.md` | Rescout discipline |
| `agents/hermes/content/2026-07-04_ird-iot-leadership-sync.md` | Meeting frame and asks |

---

## Related party outputs (expected same date prefix)

| Agent | Expected path | Status |
|-------|---------------|--------|
| Iris | `agents/iris/content/2026-07-04_ird-iot-*.md` | Pending — fill placeholders above |
| Odysseus | `agents/odysseus/content/2026-07-04_ird-iot-*.md` | Pending — guardrails placeholder |