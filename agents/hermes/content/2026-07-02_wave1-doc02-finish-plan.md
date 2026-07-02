# Wave 1 — doc 02 finish plan (knowledge vault)

**Date:** 2026-07-02  
**Authority:** `docs/inspiration/knowledge-vault-and-compounding-truth.md` (merged)  
**Gate to leave doc 02:** §5 minimal v1 rows **done or explicitly waived** by Overwatch  
**Orchestrator:** Hermes · **Executors:** party per `PARTY_OPERATING_RHYTHM.md`

---

## Already shipped (do not redo)

| Item | Evidence |
|------|----------|
| Foundation + bootstrap | `scripts/bootstrap_knowledge_vault.py`, `knowledge/thread/` |
| Zone INDEX stubs | `entities/`, `global/`, `pursuits/`, `generated-projections/` |
| `entities/company/` SSOT | KBR RS BU page + `entities/INDEX.md` |
| Hermes triage B | `knowledge-triage` skill, `ROUTER.md`, `board_add_task.py` |
| Retrieve contract | `agents/_shared/VAULT_RETRIEVE.md` |
| Weekly lint cron | Hermes job `a6c3233b844e`, `scripts/vault_lint.py` |
| EDEN stress | candidate + board task `triage:eden-jayson` |
| Taxonomy brainstorm | `2026-07-02_vault-intel-taxonomy-brainstorm.md` (draft) |

---

## Remaining — doc 02 §5 (ordered)

| # | Doc 02 requirement | DRI | Deliverable | Hermes action |
|---|-------------------|-----|-------------|---------------|
| 1 | Zone INDEX §4.1 quality (`Where to start`, canonical, archive) | **Hephaestus** | Patch `global/INDEX.md`, `generated-projections/INDEX.md`, `pursuits/INDEX.md` if thin | Brief in `/hephaestus` |
| 2 | Wikilink hygiene (lint: **41** unresolved) | **Hephaestus** | Batch fix or stub pages; lint → **0** or documented allowlist | Delegate; no Hermes patches |
| 3 | **Promote** execution (move + `trust: trusted` + index) | **Hephaestus** | `scripts/promote_vault_candidate.py` or runbook in `hephaestus/content/` | After Odysseus gate |
| 4 | Citation gate on promote | **Odysseus** | `agents/odysseus/content/2026-07-02_vault-promote-gate-checklist.md` | Brief in `/odysseus` |
| 5 | Iris: data → candidate (real slice) | **Iris** | EDEN/Jayson intel brief → candidate or `entities/competitors/` draft in `iris/content/` | Handoff from triage |
| 6 | Clio: candidate readability / template | **Clio** | Polish `eden-edge-computing-candidate.md` or projection template in `clio/content/` | Brief in `/clio` |
| 7 | Taxonomy brainstorm → zone INDEX | **Hermes** facilitates | Merge agreed labels into `entities/INDEX.md` (no new top-level folders) | Party review; Hephaestus applies INDEX |
| 8 | Morning queue (uncertain + promote list) | **Hermes** | v1: manual in reply; v2: cron — **waive automation** for doc 02 gate if Overwatch agrees | Document in quest close |
| 9 | Optional: `agents/*/content/INDEX.md` | **Hephaestus** | 5-line stubs | **Park** unless Overwatch wants |

**Explicitly parked (doc 02 §4.2, §6):** MC Knowledge tab, spectral graph HTML, `data-elements/`, semantic search.

---

## Suggested execution order (credit-efficient)

1. **Odysseus** — promote gate checklist (small, unblocks promote)  
2. **Hephaestus** — promote script + INDEX pass + wikilink batch (one session)  
3. **Iris** — EDEN intel slice  
4. **Clio** — candidate prose pass  
5. **Hermes** — taxonomy merge + doc 02 **close report** to Overwatch  

Then **Wave 1 · doc 03** per index (`task-management-and-capture-funnel.md`).

---

## Doc 02 close report (Hermes, when rows 1–7 done)

Single page: what’s trusted, what’s candidate, lint count, promote path proven once, link to party artifacts.

---

## Delegation briefs (copy to profiles)

### Hephaestus
> Finish doc 02 v1: enrich zone INDEXs per doc §4.1; reduce `vault_lint` unresolved wikilinks; add minimal `promote_vault_candidate.py` (Odysseus gate assumed). Log as hephaestus. Artifact: `agents/hephaestus/content/2026-07-02_doc02-vault-finish.md`.

### Odysseus
> Write vault promote gate checklist per doc 02 candidate→trusted. EDEN candidate optional worked example. Log as odysseus. Artifact: `agents/odysseus/content/2026-07-02_vault-promote-gate-checklist.md`.

### Iris
> EDEN/Jayson follow-up: scout intel brief; if durable, candidate under `generated-projections/` or competitor draft. Retrieve contract first. Log as iris. Artifact: `agents/iris/content/2026-07-02_eden-intel-brief.md`.

### Clio
> Improve EDEN vault candidate readability + optional `generated-projections` template snippet in hephaestus/clio content. Log as clio.

---

*Ratification:* `2026-07-02_party-calibration-ratification.md`