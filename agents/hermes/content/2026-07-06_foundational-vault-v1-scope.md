# Foundational vault v1 — scope (2026-07-06)

**Overwatch pivot:** Stop treating harmonize H4+ and opportunistic promotes as the active track. **Foundational v1** is the single in-scope program until Overwatch directs otherwise.

**Branch:** `feature/knowledge-vault-v1` · **No merge to `main`** until foundational v1 sign-off.

**Related:** [Autonomous pipeline status](2026-07-05_autonomous-pipeline-status.md) · [Recalibration note](2026-07-05_vault-recalibration-foundational-v1.md) · [Harmonize program](2026-07-05_vault-llm-wiki-harmonize-program.md)

---

## In scope (foundational v1)

### 1 — Shipley Capture Guide (fully incorporated)

| Requirement | Status / action |
|-------------|-----------------|
| Hub tables phases 1–3 complete | `knowledge/global/domain_intel/concepts/shipley-capture-guide-hub.md` — phase 1–3 topic tables populated |
| Hub repair | Fix hub only if phase 3 table is truncated or contains escape junk (verified 2026-07-06: **OK**, no repair needed) |
| Remaining Shipley batches | **Only if needed** to cover Capture Guide TOC major topics not yet represented as concept pages |
| Source lock | `[[shipley-capture-guide-source]]` + raw extract under `knowledge/foundation/raw/shipley/` |
| Ritual | Append `knowledge/log.md`; refresh `knowledge/index.md` links after each batch |

Doctrine pages live under `knowledge/global/domain_intel/concepts/` with trusted frontmatter, citations, and index/log cross-links per vault contract.

### 2 — Structure polish (vault operability)

| Item | Deliverable |
|------|-------------|
| **llm-wiki ritual** | `knowledge/foundation/capture-llm-wiki.md` — orient → schema → index → log → lint before every vault batch |
| **Retrieve contract** | `agents/_shared/VAULT_RETRIEVE.md` — party retrieve-first behavior |
| **Obsidian desktop** | `knowledge/foundation/reference/obsidian-desktop.md` — connected vault path documented |
| **Party skills** | All agents use **`llm-wiki`** + **`obsidian`** skills with `WIKI_PATH=C:/Users/benma/ariadnes-thread-os/knowledge` |
| **Harmonize depth** | **Stops at H3** (gold templates) — **done** per `2026-07-06_harmonize-h3.md` / Hephaestus close |
| **Lint** | `python scripts/vault_lint.py` exit **0** (verified 2026-07-06) |
| **Entities** | **v2** hierarchy per entities design + phase3b migration gate |
| **Git hygiene** | **No** `.obsidian/` in git |

Writes: repo-relative paths only; batch vault edits via **one Python script from repo root** (`safe_repo_write.py` or dedicated batch scripts), not parallel fragile `write_file` on large trees.

---

## Backlog (until Overwatch directs)

Park these; do **not** spin autonomous delegations without explicit tasking:

| Backlog item | Notes |
|--------------|--------|
| **Company templates W7** | One-at-a-time per Clio order; needs Overwatch template uploads |
| **Harmonize H4+** | Obsidian human graph pass + slug feedback loop (program H4–H5) |
| **EDEN** | `eden-edge-computing-candidate.md` — promote only after Overwatch/Odysseus gate |
| **Arbitrary promotes** | No ad-hoc capability promotes outside foundational v1 checklist |

---

## Definition of done (foundational v1)

1. Shipley Capture Guide **major TOC topics** represented as trusted hub + concept pages with source lock and log/index links.
2. Structure polish checklist above **green** (ritual docs, party paths, H3 harmonize, lint 0, entities v2, no `.obsidian` in git).
3. Overwatch signs off; **then** optional merge to `main` and freeze lift for routine capture ops.

---

## Out of scope for this pivot

- Mission Control vault item 3 deep edit (until foundational v1 stable)
- New capability manifest waves beyond closing stubs already in flight
- H4+ harmonize as an autonomous overnight track

*Hermes coordinates Foundational v1; Iris/Clio/Odysseus/Hephaestus delegate per `agents/TEAM_AWARENESS.md`.*
