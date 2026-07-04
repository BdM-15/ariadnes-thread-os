# W2 lighthouse promote — Iron Stallion (2026-07-04)

**Branch:** `feature/knowledge-vault-v1`  
**Agent:** Hephaestus (execute) · Odysseus gate (inline)  
**Overwatch:** single lighthouse promote OK during promote freeze (2026-07-04)

---

## Scope

| Field | Value |
|-------|-------|
| Candidate (was) | `knowledge/generated-projections/iron-stallion-rewrite-candidate.md` |
| Trusted target | `knowledge/global/domain_intel/capabilities/iron-stallion.md` |
| Iris item | Wave A rescout #6 |
| `reviewed_by` | `axelrod2023` |
| `review_id` | `a3c8e1f2-4d6b-4a9e-8c0d-1e2f3a4b5c6d` |

---

## Odysseus gate (inline — PASS)

Checklist: `agents/odysseus/content/2026-07-02_vault-promote-gate-checklist.md`

| Step | Result |
|------|--------|
| 1. Path / trust | ✅ Candidate under `generated-projections/`, `trust: candidate` |
| 2. Citations | ✅ Non-empty `citations:` — Tier-1 KBR Digital Accelerators URL + Iris rescout §6; signal table aligned |
| 3. Trust shape | ✅ `type: capability`, `## Related`, stable id on promote → `capability-iron-stallion` |
| 4. Dedup | ✅ Replace-in-place over existing trusted stub; capability vs proof-point split via [[u-s-space-force-ssa-performance-iron-stallion]] |
| 5. Write zone | ✅ `global/domain_intel/capabilities/iron-stallion.md` |
| 6. Index plan | ✅ `generated-projections/INDEX.md` + `knowledge/log.md` promote line |

**Outcome:** **PASS** — Hephaestus authorized to move.

**Caveats:** Tier-4 contract/registry not asserted; dropped unsupported `proof_strength: medium` from prior auto-stub. USSF deployment narrative stays on proof-point page.

---

## Hephaestus execution

- [x] Replaced trusted stub with Clio distill; `trust: trusted`, `citations` + `retrieved` retained
- [x] Preserved stable id `capability-iron-stallion`
- [x] Archived candidate → `generated-projections/archived/iron-stallion-rewrite-candidate-promoted-20260704.md`
- [x] Removed active candidate file from `generated-projections/`
- [x] Refreshed `generated-projections/INDEX.md` (lighthouse #2 status)
- [x] Appended `knowledge/log.md` promote line
- [x] `python scripts/vault_lint.py` (post-commit verify)

---

## Related

- `agents/clio/content/2026-07-03_w2-wave-a-candidates-ship.md`
- `agents/iris/content/2026-07-02_wave-a-top10-capability-rescout.md`
- `knowledge/global/domain_intel/capabilities/iron-stallion.md`
- `agents/hephaestus/content/2026-07-04_promote-kbr-rs-lighthouse.md` (lighthouse #1 pattern)