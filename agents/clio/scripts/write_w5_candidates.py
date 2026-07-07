#!/usr/bin/env python3
"""Generate W5 capability rewrite candidates (Clio batch)."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "knowledge" / "generated-projections"
OUT.mkdir(parents=True, exist_ok=True)

IRIS = "iris:agents/iris/content/2026-07-05_w5-capabilities-rescout-batch.md"
HUB = "https://www.kbr.com/en/what-we-do/kbr-digital-accelerators"
DATE = "2026-07-05"

CANDIDATES = [
    ("kbr-cyber-range", "candidate-kbr-cyber-range-rewrite", "KBR Cyber Range — W5 REWRITE (candidate)",
     f"{HUB} • {IRIS}", "global/domain_intel/capabilities/kbr-cyber-range.md",
     "Secure virtual cyber range for incident response, tactic development, and tool testing without impacting mission systems.",
     """# KBR Cyber Range — W5 REWRITE candidate

> **Morning queue (30s scan)**  
> **Trust:** `candidate` · **Promote?** Odysseus cite gate — mandatory Cybersecurity § Cyber Range.

**Status:** Freeze-safe projection — **not** trusted until promoted over `[[kbr-cyber-range]]`.

## Key signals

| Signal | Citation |
|--------|----------|
| Secure **virtual platform** for real-world cyber testing and defense tactic development | Digital Accelerators · Cyber Range § · retrieved 2026-07-05 |
| Simulations **without impacting mission-critical systems** | Same § |
| **Incident response** practice and cybersecurity tool testing | Same § |

## Offering

KBR Cyber Range is a secure virtual environment for cyber defense exercises, tactic development, and validation of security tools—decoupled from production mission networks.

## Bid fit

Cyber training, blue/red team exercises, certification ranges, DoD/IC cyber workforce development—cite Tier-1; contract PP Tier-4 only.

## Evidence

- Tier-1: Digital Accelerators Cyber Range subsection.
- Old vault: no `citations:`; `auto_generated: true`.

## Gaps

- Parent `[[cybersecurity-capability]]` on promote.
- Named customer programs—open until Tier-4.

## Related

- [[kbr-cyber-range]] — **promote target**
- [[cybersecurity-capability]] · [[crystalvista]] · [[quantum-pantheon]]

## Added/Updated 2026-07-05

- Clio W5: slug 1 — KBR Cyber Range REWRITE."""),

    ("kbr-inc", "candidate-kbr-inc-rewrite", "KBR Inc. — W5 REWRITE (candidate)",
     "https://www.kbr.com/en • https://investors.kbr.com/news-and-events/spin-off-information • " + IRIS,
     "global/domain_intel/capabilities/kbr-inc.md",
     "Corporate entity for federal proposals—MTS vs STS segments; strategic MTS spin intent.",
     """# KBR Inc. — W5 REWRITE candidate

**Status:** Freeze-safe projection — **not** trusted until promoted over `[[kbr-inc]]`.

## Key signals

| Signal | Citation |
|--------|----------|
| Global engineering, technology, **government services** (NYSE: KBR) | kbr.com/en · retrieved 2026-07-05 |
| **Mission Technology Solutions spin-off** strategic intent | Investors spin-off page + site banner |

## Offering

Parent legal entity for corporate representations, certifications, and segment-aware past performance citations.

## Bid fit

Teaming, OCI, corporate qualifications—track spin status; not contract-specific PP.

## Evidence

- Tier-1: kbr.com/en; Tier-3: investors spin-off notice.
- Old vault: `auto_generated: true`, no cites.

## Gaps

- Post-spin entity naming—open until transaction closes.

## Related

- [[kbr-inc]] — **promote target**
- [[kbr-digital-accelerators-portfolio]] · [[kbr-readiness-and-sustainment]]

## Added/Updated 2026-07-05

- Clio W5: slug 2 — KBR Inc. REWRITE."""),

    ("petabyte-scale-cloud-migration-proof-point", "candidate-petabyte-scale-cloud-migration-proof-point-rewrite",
     "Petabyte-scale cloud migration — W5 REWRITE (candidate)", f"{HUB} • {IRIS}",
     "global/domain_intel/capabilities/petabyte-scale-cloud-migration-proof-point.md",
     "Proof point for petabyte-scale migration, archives, power/cooling, data-center exit.",
     """# Petabyte-scale cloud migration proof point — W5 REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
| **Petabyte-scale** cloud migrations | Enterprise Technology § Cloud Migration · retrieved 2026-07-05 |
| Legacy archives; **AI/ML** and latency benefits | Same § |
| **Power and cooling** engineering; reduce aging DC reliance | Same § |

## Offering

Enterprise-scale cloud migration proof under Enterprise Technology pillar.

## Bid fit

IT modernization, data center exit—pair `[[enterprise-technology-capability]]`; named mission Tier-4.

## Evidence

- Tier-1: Cloud Migration subsection.
- Old vault: TODO customer/volume.

## Gaps

- Customer, volume, window—open for proposals.

## Related

- [[petabyte-scale-cloud-migration-proof-point]] — **promote target**
- [[enterprise-technology-capability]] · [[kbr-vaault]]

## Added/Updated 2026-07-05

- Clio W5: slug 3 — petabyte migration proof REWRITE."""),

    ("proven-sustainment-scale-discriminator", "candidate-proven-sustainment-scale-discriminator-rewrite",
     "Proven sustainment scale — W5 REWRITE (candidate)",
     "https://solutions.kbr.com/readiness-and-sustainment/ • iris:agents/iris/content/2026-07-05_w4-capabilities-rescout-batch.md • " + IRIS,
     "global/domain_intel/capabilities/proven-sustainment-scale-discriminator.md",
     "LOGCAP/AFCAP-scale sustainment discriminator for contingency and large O&M bids.",
     """# Proven sustainment scale discriminator — W5 REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
| **Readiness & Sustainment** global contingency positioning | solutions.kbr.com R&S hub · retrieved 2026-07-05 |
| Scale heritage via `[[afcap-contract-heritage]]` / LOGCAP family | W4 contract cites + R&S |

## Offering

Proposal theme for BOS/contingency scale—only when RFP is in sustainment lane.

## Bid fit

LOGCAP/AFCAP-style competitions—cross-link heritage pages; not for niche IT.

## Evidence

- Tier-1: R&S hub; contract facts on AFCAP pages.
- Old vault: high proof_strength without award table—calibrate on promote.

## Gaps

- No public competitor matrix—framing only.

## Related

- [[proven-sustainment-scale-discriminator]] — **promote target**
- [[kbr-readiness-and-sustainment]] · [[afcap-contract-heritage]]

## Added/Updated 2026-07-05

- Clio W5: slug 4 — sustainment scale discriminator REWRITE."""),

    ("quality-management-system-certification", "candidate-quality-management-system-certification-rewrite",
     "Quality management system certification — W5 REWRITE (candidate)",
     "https://www.kbr.com/sites/default/files/documents/2024-10/KBR-Sustainability-and-Corporate-Responsibility-Report-2023.pdf • " + IRIS,
     "global/domain_intel/capabilities/quality-management-system-certification.md",
     "QMS compliance artifact—Sustainability Report cite; open ISO/CMMI dates.",
     """# Quality management system certification — W5 REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
| Certifications in **Sustainability Report 2023** (ISO 27001, CMMC program) | PDF · retrieved 2026-07-05 |
| Federal RFP **QMS** evaluation factors | Proposal practice |

## Offering

Vault index for quality/management-system certifications—appendix certs Tier-4.

## Bid fit

ISO 9001/20000-1, CMMI when RFP requires—list only PDF-named certs.

## Evidence

- Tier-1: Sustainability PDF.
- Old vault: empty TODO.

## Gaps

- ISO 9001/20000-1/CMMI **levels and dates**—open questions.

## Related

- [[quality-management-system-certification]] — **promote target**
- [[cmmc-certification-status]]

## Added/Updated 2026-07-05

- Clio W5: slug 5 — QMS certification REWRITE."""),

    ("resan", "candidate-resan-rewrite", "RESAN — W5 REWRITE (candidate)", f"{HUB} • {IRIS}",
     "global/domain_intel/capabilities/resan.md",
     "Proprietary compliance platform linking requirement updates to constraint models and 3D engineering models.",
     """# RESAN — W5 REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
| **Requirement update** → constraints-based system model → **3D engineering model** | Digital Engineering § RESAN · retrieved 2026-07-05 |
| Visual review indicators; **nuclear** and safety-critical environments | Same § |

## Offering

RESAN keeps assets compliant through constraint changes across requirements and engineering models.

## Bid fit

Nuclear sustainment, aerospace certification, NRC/FAA/NNSA traceability gates.

## Evidence

- Tier-1: RESAN subsection on Digital Accelerators.
- Old vault: aligned body, no cites; `auto_generated: true`.

## Gaps

- Named program references—Tier-4 before external PP claims.

## Related

- [[resan]] — **promote target**
- [[digital-engineering-capability]] · [[encompass-digital-twin-platform]] · [[safety-critical-compliance-proof-point]]

## Added/Updated 2026-07-05

- Clio W5: slug 6 — RESAN REWRITE."""),

    ("safety-critical-compliance-proof-point", "candidate-safety-critical-compliance-proof-point-rewrite",
     "Safety-critical compliance proof — W5 REWRITE (candidate)", f"{HUB} • {IRIS}",
     "global/domain_intel/capabilities/safety-critical-compliance-proof-point.md",
     "Proof point tying RESAN deployment in nuclear/safety-critical traceability environments.",
     """# Safety-critical compliance proof point — W5 REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
| RESAN **proven value** in **nuclear** and critical safety parameters | Digital Engineering § RESAN · retrieved 2026-07-05 |
| Requirement-to-model traceability under changing constraints | Same § + `[[resan]]` |

## Offering

Short proof-point for safety-critical compliance narratives—points to RESAN product page.

## Bid fit

Nuclear sustainment, formal requirements management gates—do not duplicate RESAN body.

## Evidence

- Tier-1: RESAN nuclear mention.
- Old vault: links `[[resan]]` but no cites.

## Gaps

- Specific NNSA/naval reactor program—open until Tier-4.

## Related

- [[safety-critical-compliance-proof-point]] — **promote target**
- [[resan]] · [[quality-management-system-certification]]

## Added/Updated 2026-07-05

- Clio W5: slug 7 — safety-critical compliance proof REWRITE."""),

    ("skypath-assured-containment", "candidate-skypath-assured-containment-rewrite",
     "Skypath assured containment — W5 REWRITE (candidate)", f"{HUB} • {IRIS}",
     "global/domain_intel/capabilities/skypath-assured-containment.md",
     "Onboard autonomy assurance for UAS/maritime—geofencing, heartbeat, propulsion interrupt, KERS.",
     """# Skypath assured containment — W5 REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
| **Assured containment** for UAS and maritime platforms | Autonomous Systems § Skypath · retrieved 2026-07-05 |
| **Encrypted heartbeat**, assurable/dynamic **geofencing** | Same § |
| Propulsion interruption, **KERS**; platform/bearer agnostic | Same § |

## Offering

Skypath onboard enabler for safe BVLOS and hazardous-environment autonomous operations.

## Bid fit

UAS safety assurance, BVLOS waivers, maritime autonomy—cite Tier-1; flight test PP Tier-4.

## Evidence

- Tier-1: Skypath subsection.
- Old vault: strong thematic match, no cites.

## Gaps

- Specific platform certifications—open.

## Related

- [[skypath-assured-containment]] — **promote target**
- [[autonomous-systems-capability]] · [[artemis-uas]] · [[ttmt-tracking-and-targeting]]

## Added/Updated 2026-07-05

- Clio W5: slug 8 — Skypath REWRITE."""),

    ("ttmt-tracking-and-targeting", "candidate-ttmt-tracking-and-targeting-rewrite",
     "TTMT tracking and targeting — W5 REWRITE (candidate)", f"{HUB} • {IRIS}",
     "global/domain_intel/capabilities/ttmt-tracking-and-targeting.md",
     "Closed-loop offboard UAS control; CNN + classical CV; GNSS-denied edge tracking.",
     """# TTMT tracking and targeting — W5 REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
| **TTMT** — heart of autonomous systems; **8DOF** closed-loop offboard UAS control | Autonomous Systems § TTMT · retrieved 2026-07-05 |
| **CNN + classical CV** multitarget tracking at the edge | Same § |
| **GNSS-denied** object ID; fast movers land/sea | Same § |

## Offering

Proprietary tracking and targeting stack for autonomous ISR and manned-unmanned teaming payloads.

## Bid fit

Edge-AI tracking, autonomous ISR, offboard control—cite Tier-1 product copy.

## Evidence

- Tier-1: TTMT subsection.
- Old vault: detailed stub, no cites.

## Gaps

- Deployment program names—Tier-4.

## Related

- [[ttmt-tracking-and-targeting]] — **promote target**
- [[autonomous-systems-capability]] · [[artemis-uas]] · [[dash-c3-decision-support]]

## Added/Updated 2026-07-05

- Clio W5: slug 9 — TTMT REWRITE."""),

    ("u-s-space-force-ssa-performance-iron-stallion", "candidate-u-s-space-force-ssa-performance-iron-stallion-rewrite",
     "U.S. Space Force SSA performance (Iron Stallion) — W5 REWRITE (candidate)", f"{HUB} • {IRIS}",
     "global/domain_intel/capabilities/u-s-space-force-ssa-performance-iron-stallion.md",
     "Past-performance reference for USSF SSA C2—public Iron Stallion deployment cite.",
     """# U.S. Space Force SSA performance (Iron Stallion) — W5 REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
| **Iron Stallion®** enterprise SSA C2 for **U.S. Space Force** | Data Analytics § Iron Stallion · retrieved 2026-07-05 |
| Data integration, workflow-aiding, analytics, visualization | Same § |
| Coalition/commercial SSA users (corporate wording) | Same § |

## Offering

Past-performance reference page for USSF/SDA/SSC SSA software bids—capability detail on `[[iron-stallion]]`.

## Bid fit

Space situational awareness, SDA, space C2 software—**do not duplicate** `[[iron-stallion]]` product body; link only.

## Evidence

- Tier-1: Iron Stallion subsection (USSF).
- Old vault: `entity_type: past_performance_reference`, TODO contract #.

## Gaps

- Contract numbers, $, performance period—**open questions** (Tier-4/SAM).

## Related

- [[u-s-space-force-ssa-performance-iron-stallion]] — **promote target**
- [[iron-stallion]] · [[data-analytics-capability]]

## Added/Updated 2026-07-05

- Clio W5: slug 10 — USSF Iron Stallion PP REWRITE."""),
]

def fm(slug, cid, name, cites, target, summary, body):
    return f"""---
added: "2026-07-05T18:00:00Z"
citations: "{cites}"
retrieved: "{DATE}"
id: {cid}
last_updated: {DATE}
name: "{name}"
trust: candidate
type: capability
wave: W5
promote_target: {target}
tags: [capability-rewrite, wave-w5, morning-queue]
source: iris-rescout
review_id: null
summary: "{summary}"
---

{body}
"""

for slug, cid, name, cites, target, summary, body in CANDIDATES:
    path = OUT / f"{slug}-rewrite-candidate.md"
    path.write_text(fm(slug, cid, name, cites, target, summary, body), encoding="utf-8")
    print("wrote", path.relative_to(ROOT))

print("done", len(CANDIDATES))[H[2J[3J