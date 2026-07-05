# W4 — Manifest-tail capability rewrite candidates (ship)

**Date:** 2026-07-05  
**Agent:** Clio  
**Gate:** Promote freeze ON — **candidates only**, no trusted promote  
**Source:** `agents/iris/content/2026-07-05_w4-capabilities-rescout-batch.md` (12× REWRITE)

---

## Delivered

| # | Slug | Candidate file | Promote target |
|---|------|----------------|----------------|
| 1 | `active-gwac-and-idiq-holdings` | `knowledge/generated-projections/active-gwac-and-idiq-holdings-rewrite-candidate.md` | `global/domain_intel/capabilities/active-gwac-and-idiq-holdings.md` |
| 2 | `afcap-contract-heritage` | `knowledge/generated-projections/afcap-contract-heritage-rewrite-candidate.md` | `global/domain_intel/capabilities/afcap-contract-heritage.md` |
| 3 | `artemis-uas` | `knowledge/generated-projections/artemis-uas-rewrite-candidate.md` | `global/domain_intel/capabilities/artemis-uas.md` |
| 4 | `artificial-intelligence-capability` | `knowledge/generated-projections/artificial-intelligence-capability-rewrite-candidate.md` | `global/domain_intel/capabilities/artificial-intelligence-capability.md` |
| 5 | `autonomous-systems-capability` | `knowledge/generated-projections/autonomous-systems-capability-rewrite-candidate.md` | `global/domain_intel/capabilities/autonomous-systems-capability.md` |
| 6 | `cleanspend-carbon-analysis` | `knowledge/generated-projections/cleanspend-carbon-analysis-rewrite-candidate.md` | `global/domain_intel/capabilities/cleanspend-carbon-analysis.md` |
| 7 | `cleared-workforce-at-scale-discriminator` | `knowledge/generated-projections/cleared-workforce-at-scale-discriminator-rewrite-candidate.md` | `global/domain_intel/capabilities/cleared-workforce-at-scale-discriminator.md` |
| 8 | `cleared-workforce` | `knowledge/generated-projections/cleared-workforce-rewrite-candidate.md` | `global/domain_intel/capabilities/cleared-workforce.md` |
| 9 | `cmmc-certification-status` | `knowledge/generated-projections/cmmc-certification-status-rewrite-candidate.md` | `global/domain_intel/capabilities/cmmc-certification-status.md` |
| 10 | `csom-scheduling-optimization-module` | `knowledge/generated-projections/csom-scheduling-optimization-module-rewrite-candidate.md` | `global/domain_intel/capabilities/csom-scheduling-optimization-module.md` |
| 11 | `enterprise-technology-capability` | `knowledge/generated-projections/enterprise-technology-capability-rewrite-candidate.md` | `global/domain_intel/capabilities/enterprise-technology-capability.md` |
| 12 | `hundred-plus-digital-initiatives-proof-point` | `knowledge/generated-projections/hundred-plus-digital-initiatives-proof-point-rewrite-candidate.md` | `global/domain_intel/capabilities/hundred-plus-digital-initiatives-proof-point.md` |

Each candidate includes:

- `trust: candidate` · `wave: W4`
- `citations:` + `retrieved: 2026-07-05` (Tier-1 hub/press/PDF + Iris rescout brief)
- `promote_target:` path to existing capability slug
- Sections per W2/W3 standard: Key signals, Offering, Bid fit, Evidence, Gaps/TODO, Related

**Promote:** explicitly **not** executed this pass.

---

## Ingestion order (Iris handoff)

1. Pillar hubs first: #4 AI, #5 Autonomous, #11 Enterprise Technology  
2. Contract/compliance: #1 GWAC, #2 AFCAP, #8–9 cleared/CMMC  
3. Products + proof points: #3 Artemis, #6 CleanSpend, #10 CSOM, #7 discriminator, #12 100+ proof  
4. Dedupe: #12 vs W3 portfolio + W2 owned-IP discriminator; Vaault auth on `[[kbr-vaault]]` only

---

## Handoffs

| To | Action |
|----|--------|
| **Odysseus** | CMMC level gate; GWAC inventory honesty; AFCAP vs LOGCAP boundaries; no clearance headcount without cite |
| **Hermes** | Morning queue — twelve W4 candidates on disk |
| **Hephaestus** | `generated-projections/INDEX.md` W4 rows; `log.md` on promote |

---

## Related

- `agents/iris/content/2026-07-05_w4-capabilities-rescout-batch.md`
- `agents/clio/content/2026-07-04_w3-accelerators-candidates-ship.md` (W3 template)
- `agents/hermes/content/2026-07-05_overnight-vault-runbook.md`

*Logged:* Clio W4 manifest-tail capability rewrite candidates ship