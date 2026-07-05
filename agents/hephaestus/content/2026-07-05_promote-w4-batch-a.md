# W4 lighthouse promote — batch A (#1–#6 capabilities) (2026-07-05)

**Branch:** `feature/knowledge-vault-v1` (no merge main)  
**Agent:** Hephaestus (execute) · Odysseus gate (inline, W4 batch A)  
**Clio ship:** `agents/clio/content/2026-07-05_w4-capabilities-candidates-ship.md` (73d94cc context)  
**Iris:** `agents/iris/content/2026-07-05_w4-capabilities-rescout-batch.md`  
**Overwatch:** W4 lighthouse #1–#6 — six in-place REWRITE promotes, one commit

---

## Scope

| Lighthouse | Candidate (archived) | Trusted target | `review_id` |
|------------|----------------------|----------------|-------------|
| W4 #1 | `active-gwac-and-idiq-holdings-rewrite-candidate.md` | `global/domain_intel/capabilities/active-gwac-and-idiq-holdings.md` | `a1c3e5f7-8b2d-4a6c-9e0f-1b3d5f7a9c1e` |
| W4 #2 | `afcap-contract-heritage-rewrite-candidate.md` | `global/domain_intel/capabilities/afcap-contract-heritage.md` | `b2d4f6a8-9c3e-5b7d-0f1a-2c4e6f8a0b2d` |
| W4 #3 | `artemis-uas-rewrite-candidate.md` | `global/domain_intel/capabilities/artemis-uas.md` | `c3e5a7b9-0d4f-6c8e-1a2b-3d5f7a9b1c3e` |
| W4 #4 | `artificial-intelligence-capability-rewrite-candidate.md` | `global/domain_intel/capabilities/artificial-intelligence-capability.md` | `d4f6b8c0-1e5a-7d9f-2b3c-4e6a8b0c2d4f` |
| W4 #5 | `autonomous-systems-capability-rewrite-candidate.md` | `global/domain_intel/capabilities/autonomous-systems-capability.md` | `e5a7c9d1-2f6b-8e0a-3c4d-5f7b9c1d3e5a` |
| W4 #6 | `cleanspend-carbon-analysis-rewrite-candidate.md` | `global/domain_intel/capabilities/cleanspend-carbon-analysis.md` | `f6b8d0e2-3a7c-9f1b-4d5e-6a8c0d2e4f6b` |

**`reviewed_by`:** `axelrod2023`

---

## Odysseus gate (inline)

Checklist: `agents/odysseus/content/2026-07-02_vault-promote-gate-checklist.md`

| Step | Result |
|------|--------|
| 1. Path / trust | ✅ Six candidates under `generated-projections/`, `trust: candidate` |
| 2. Citations | ✅ Tier-1 Digital Accelerators / press URLs + Iris W4 batch; **no invented GWAC vehicle awards**; **no invented CMMC level** (N/A on batch A slugs) |
| 3. Trust shape | ✅ `type: capability`, `## Related`, stable `capability-*` ids preserved |
| 4. Dedup | ✅ Replace-in-place REWRITE (dest exists) |
| 5. Write zone | ✅ `global/domain_intel/capabilities/*.md` |
| 6. Index plan | ✅ `generated-projections/INDEX.md` + six `knowledge/log.md` promote lines |

**Outcomes:**

| Slug | Gate |
|------|------|
| `active-gwac-and-idiq-holdings` | **CONDITIONAL PASS** — open inventory; Tier-4 SAM/GSA before named vehicles |
| `afcap-contract-heritage` | **PASS** — press-cited AFCAP V only |
| `artemis-uas` | **PASS** |
| `artificial-intelligence-capability` | **PASS** |
| `autonomous-systems-capability` | **PASS** |
| `cleanspend-carbon-analysis` | **PASS** — federal fit verification retained |

**Index:** root + `generated-projections/INDEX.md` + log lines.

---

## Hephaestus execution

- [x] Replaced six trusted stubs with Clio W4 distills; `trust: trusted`, citations retained
- [x] Preserved stable ids; dropped `auto_generated`, `source_module`, unsupported `proof_strength`
- [x] Archived → `generated-projections/archived/*-promoted-20260705.md`
- [x] `git rm` active candidate files (six)
- [x] Refreshed `generated-projections/INDEX.md` (lighthouse #1–#6)
- [x] Appended `knowledge/log.md` promote lines (W4 lighthouse #1–#6)
- [ ] `python scripts/vault_lint.py`
- [ ] Git commit `feat(vault): promote W4 capabilities batch A (6)`

---

## Related

- `agents/hephaestus/content/2026-07-05_promote-w4-batch-b.md` (W4 #7–#12)
- `knowledge/global/domain_intel/capabilities/active-gwac-and-idiq-holdings.md`
- `knowledge/global/domain_intel/capabilities/afcap-contract-heritage.md`
- `knowledge/global/domain_intel/capabilities/artemis-uas.md`
- `knowledge/global/domain_intel/capabilities/artificial-intelligence-capability.md`
- `knowledge/global/domain_intel/capabilities/autonomous-systems-capability.md`
- `knowledge/global/domain_intel/capabilities/cleanspend-carbon-analysis.md`