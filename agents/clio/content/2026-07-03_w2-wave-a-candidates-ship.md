# W2 — Wave A top-5 capability candidates (ship)

**Date:** 2026-07-03  
**Agent:** Clio  
**Gate:** G2 PASS · promote freeze ON — **candidates only**, no trusted promote  
**Source:** `agents/iris/content/2026-07-02_wave-a-top10-capability-rescout.md` items **#1–#5** (REWRITE set)

---

## Delivered

| # | Iris rescout item | Candidate file | Promote target slug |
|---|-------------------|----------------|---------------------|
| 1 | `kbr-readiness-and-sustainment` | `knowledge/generated-projections/kbr-readiness-and-sustainment-rewrite-candidate.md` | `global/domain_intel/capabilities/kbr-readiness-and-sustainment.md` |
| 2 | `logcap-v-contract` | `knowledge/generated-projections/logcap-v-contract-rewrite-candidate.md` | `global/domain_intel/capabilities/logcap-v-contract.md` |
| 3 | `kbr-vaault` + FedRAMP/IL5 pair | `knowledge/generated-projections/kbr-vaault-rewrite-candidate.md` | `global/domain_intel/capabilities/kbr-vaault.md` (+ child cite refresh) |
| 4 | `kbrain` | `knowledge/generated-projections/kbrain-rewrite-candidate.md` | `global/domain_intel/capabilities/kbrain.md` |
| 5 | `insite-remote-operations-platform` | `knowledge/generated-projections/insite-remote-operations-platform-rewrite-candidate.md` | `global/domain_intel/capabilities/insite-remote-operations-platform.md` |

Each candidate includes:

- `trust: candidate`
- `citations:` + `retrieved: 2026-07-02` (Iris Tier-1 spine)
- `promote_target:` wikilink path to existing trusted capability slug
- Sections per ingestion standard F + Clio page standards (Offering / Evidence / Gaps where applicable)

**Promote:** explicitly **not** executed this pass.

---

## Side fix (#5 task item)

Patched `agents/clio/content/2026-07-02_item4-clio-ingestion-order.md`:

- `entities/company/` → `entities/companies/` (W1 wave line + §C heading) — aligns with G2 schema review and live vault path `knowledge/entities/companies/kbr-services-readiness-sustainment.md`.

---

## Handoffs

| To | Action |
|----|--------|
| **Odysseus** | REWRITE sign-off; LOGCAP marketing vs contract split; INSITE 3.0 generational split; Vaault FedRAMP ID gap |
| **Hermes** | Morning queue — five new W2 candidates + existing EDEN |
| **Hephaestus** | Optional `generated-projections/INDEX.md` rows; `log.md` ingest lines on promote |

---

## Remaining Wave A queue (not in W2 top-5)

Iris rescout **#6–#10** (Iron Stallion, CrystalVista/Quantum Pantheon, IAM, owned-IP discriminator, EDEN) — separate Clio sprint.

---

## Related

- `agents/iris/content/2026-07-02_wave-a-top10-capability-rescout.md`
- `agents/clio/content/2026-07-02_item4-clio-ingestion-order.md`
- `agents/odysseus/content/2026-07-02_g2-schema-review.md`