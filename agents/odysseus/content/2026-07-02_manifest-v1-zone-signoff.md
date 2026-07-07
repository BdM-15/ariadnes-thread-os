# Manifest v1 — zone-bucket signoff (Odysseus PASS)

**Date:** 2026-07-02  
**Owner:** Odysseus (trust + salvage gate)  
**Status:** **Zone-bucket PASS recorded** — **Overwatch explicit approval still required** per [Hermes manifest v1 review packet](../../hermes/content/2026-07-02_manifest-v1-overwatch-review.md) before Phase 2 smoke archive executes.

**Inputs:**

- Machine inventory: [2026-07-02_vault-manifest-inventory.csv](../../hephaestus/content/2026-07-02_vault-manifest-inventory.csv) (**224** rows)
- Phase 1 ship: [phase1-inventory-ship.md](../../hephaestus/content/2026-07-02_phase1-inventory-ship.md)
- Hybrid gate & taxonomy: [item4-odysseus-hybrid-gate.md](2026-07-02_item4-odysseus-hybrid-gate.md)

**Odysseus action this turn:** Sign **bucket policy** (not 224 row-by-row review). **No vault file moves or deletes.**

---

## Preconditions (G3)

| # | Check | Result |
|---|--------|--------|
| G3 | Manifest v1 filed: zone buckets + exemplar paths tagged `KEEP\|REWRITE\|ARCHIVE\|RESCOUT` | **PASS** — Hephaestus CSV + ship note complete |

---

## Zone-bucket signoff (machine proposal ratified by Odysseus)

Odysseus **PASS** on the following zone defaults. Counts match Phase 1 cross-tab.

| Zone / bucket | Rows | Signed default | Odysseus rationale |
|---------------|-----:|----------------|--------------------|
| **capabilities** (`domain_intel/capabilities/`) | 46 | **RESCOUT** (all) | No bulk trust until Iris maps each page to public KBR URL or explicit `proof_strength` + open question |
| **concepts** (`global_wiki/capture/concepts/`) | 42 | **RESCOUT** 41 · **KEEP** 1 | Capture-router terms need USAspending/intel cite; **KEEP** only `sam-live-discovery.md` pending light verify |
| **shipley** (`global_wiki/shipley/` + related doctrine) | 23 | **REWRITE** (all) | Re-author from Shipley Capture Guide; MS gate alignment in Wave B |
| **global_wiki** (non-shipley doctrine) | 87 | **REWRITE** (machine default) | Clio voice pass in waves; not blind KEEP |
| **entities** | 4 | **KEEP** 2 · **ARCHIVE** 2 | Company hub + INDEX **KEEP**; smoke **ARCHIVE** only |
| **foundation** | 4 | **REWRITE** (all) | Includes `capture-llm-wiki` → `ariadne-vault-schema.md` |
| **domain_intel** (excl. capabilities bucket) | 9 | Mixed per row | Milestones **KEEP**; remainder per CSV |
| **generated-projections** | 2 | **KEEP** per row | Candidate retention; **no promote** during freeze |
| **meta / global / pursuits / relationships** | 9 | **KEEP** per exemplar list | Index chain, `log.md`, README — structural |

**Tag totals (inventory):** KEEP **16** · REWRITE **119** · ARCHIVE **2** · RESCOUT **87**

---

## Exemplar paths — Odysseus signed

### Company hub (KEEP)

| Path | Tag | Signed |
|------|-----|--------|
| `entities/company/kbr-services-readiness-sustainment.md` | **KEEP** | yes — SSOT hub; KBR RS spine |

### Smoke — ARCHIVE now (2 rows)

| Path | Tag | Signed |
|------|-----|--------|
| `entities/agencies/test-agency-xyz.md` | **ARCHIVE** | yes |
| `entities/competitors/example-competitor-llc.md` | **ARCHIVE** | yes |

**Archive destination (Overwatch-ratified):** `generated-projections/archived/rebuild-2026/`  
**Execution:** Hephaestus Phase 2 **only after** Overwatch one-line manifest v1 approval + hybrid gate **GREEN** for smoke rows.

### Structural KEEP chain (machine exemplars — no dispute)

`index.md`, zone `INDEX.md` files, `log.md`, `README.md`, `relationships/*`, `global/domain_intel/milestones/ms1–ms4*.md`, `generated-projections/eden-edge-computing-candidate.md`, `global_wiki/capture/concepts/sam-live-discovery.md` — **KEEP** per inventory; cite gates apply on promote, not on manifest signoff.

---

## Gate verification (manifest v1 slice)

| # | Question | Result |
|---|----------|--------|
| V1 | Any promote during freeze without PASS? | **PASS** — none executed |
| V2 | Smoke entities remain trusted without manifest row? | **PASS** — both smoke rows tagged **ARCHIVE**; move pending Phase 2 |
| V3 | Capability pages cite public KBR or aspirational + open question? | **Conditional** — queued via **RESCOUT** (Wave A) |
| V4 | Capture concepts in router/skills have intel lineage? | **Conditional** — **RESCOUT** default; 1 exemplar **KEEP** |

**Hybrid gate outcome (manifest v1):** **GREEN** for *documented* bucket policy and smoke **ARCHIVE** rows. **YELLOW** carry-forward for trusted retention in **capabilities** and **concepts** until Iris rescout completes.

---

## Promote freeze

**ON** — unchanged.

- No `candidate` → `trusted` promotions except Overwatch emergency + Odysseus cite PASS.
- Manifest signoff does **not** lift freeze.
- Freeze lifts only after post-W2 lint + Overwatch + Odysseus joint lift (per item 4 execution plan).

---

## What Overwatch must do next

1. Review [manifest v1 Overwatch review packet](../../hermes/content/2026-07-02_manifest-v1-overwatch-review.md).
2. Reply with one-line approval **or** dispute zone/path before Phase 2.
3. On approval: Hephaestus moves **only** the 2 smoke **ARCHIVE** rows; Iris opens Wave A rescout.

Suggested approval line (from Hermes packet):

```text
manifest v1 approved — proceed Phase 2 smoke archive + Iris Wave A rescout
```

---

## RACI reminder

| Action | Owner |
|--------|--------|
| Zone-bucket PASS (this doc) | Odysseus |
| Overwatch ratification | Overwatch |
| Smoke archive moves | Hephaestus (post-approval) |
| RESCOUT evidence | Iris |
| REWRITE prose | Clio |
| Board + freeze announcement | Hermes |

---

## References

- `agents/hermes/content/2026-07-02_manifest-v1-overwatch-review.md`
- `agents/hephaestus/content/2026-07-02_phase1-inventory-ship.md`
- `agents/odysseus/content/2026-07-02_item4-odysseus-hybrid-gate.md`
- `agents/odysseus/content/2026-07-02_vault-promote-gate-checklist.md`

---

*odysseus — manifest v1 zone-bucket PASS; awaiting Overwatch explicit approve*