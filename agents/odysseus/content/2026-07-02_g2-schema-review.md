# G2 schema review — `ariadne-vault-schema.md` (Item 4)

**Date:** 2026-07-02  
**Gate:** Item 4 hybrid rebuild precondition **G2** ([hybrid gate](2026-07-02_item4-odysseus-hybrid-gate.md) § Preconditions)  
**Inputs:** `knowledge/foundation/ariadne-vault-schema.md` (schema_version **3**), [entities hierarchy design rev 2](../../hermes/content/2026-07-02_entities-hierarchy-design.md), cleanse commit context **07f2247**  
**Reviewer:** Odysseus · **Vault edits:** none (this artifact only)

---

## G2 check result

| Gate | Criterion (hybrid gate row) | Result |
|------|-----------------------------|--------|
| **G2** | Draft `foundation/ariadne-vault-schema.md` exists — Agent OS Layer 3 story; capform UI / Postgres **not** mandatory Layer 1 | **PASS** |

**Signed:** Odysseus acknowledges schema v3 as the authoritative Layer 3 contract for Item 4 waves. Hephaestus Phase 3 ship satisfies the G2 **existence** precondition; this review satisfies the **Odysseus review** leg of that row.

**Hybrid gate reference:** Master preconditions table row G2 — *Hephaestus → Odysseus review* — may be recorded **PASS** for manifest / wave progression. **G0–G1, G3–G4** remain independent; overall hybrid **GREEN** is not implied by G2 alone.

---

## Review bullets

### Trust

- Frontmatter `trust` triad (`candidate` | `trusted` | `archived`) and **no auto-promote** are explicit; Overwatch ratify at the boundary is stated.
- Candidate → trusted workflow (intake → dedup → review → Odysseus cite gate → Hephaestus move/index/log) matches [promote gate checklist](2026-07-02_vault-promote-gate-checklist.md) intent.
- Page format, dedup (`id` / `award_key` / `review_id`), append-only trusted history, and provenance rules are sufficient for Clio W2–W8 and Iris rescout handoffs.
- **Gap (non-blocking for G2):** promote checklist prose still cites `knowledge/thread/` paths — must be harmonized to flat `knowledge/` before routine promotes resume post-freeze.

### Promotion freeze (cleanse / Item 4)

- §4 **Promotion freeze** is clear: until flatten complete, `vault_lint` green, and manifest signed (Odysseus + Overwatch), **freeze** all candidate→trusted promotes except **Overwatch + Odysseus emergency PASS**.
- Candidates may still be authored in `generated-projections/` — aligns with Clio W2 default path (candidate first, promote after cite gate).
- `knowledge/entities/INDEX.md` repeats promote freeze — consistent with schema.
- **Operational note:** Freeze remains **ON** at review time; W2 capability work should assume **candidates + in-place trusted edits** per wave table, not bulk promote until freeze lift.

### Entities zones (rev 2)

- Schema §6 matches Hermes design **one sentence**: flat `customers/` + `companies/`, typed frontmatter, `parent_customer` / `parent_company` graph — no folder nesting.
- Customer `type` enum, federal chain mental model, LOGCAP/AFCAP parent rules, company single-page competitor/teammate nuance, KBR hub placement, and **E1–E4** gates are embedded and **locked 2026-07-02** choices are reflected.
- Live tree: `knowledge/entities/{customers,companies}/` present; legacy `agencies/` / `competitors/` / `company/` retired per entities INDEX — consistent with §6 target layout.
- **Minor schema drift:** §11 implementation table still lists entities 3b as “📋 After schema ack”; live INDEX claims 3b folder retirement. Update §11 after this ack (Hephaestus doc pass).

### Flatten topology

- §2 documents flattened `knowledge/` (no `thread/` prefix), zone list, deferred zones, and staging under `agents/<agent>/content/`.
- Layers table (Raw read-only / Wiki append / Schema co-evolve) matches cleanse program north star.
- Retrieve contract (root `index.md` → zone INDEX → pages) and Wandermist INDEX rule are present.
- **Gap:** root `knowledge/index.md` still points schema row at `foundation/capture-llm-wiki.md` and zone copy at pre-3b entity folders — **required fix before W2** (retrieve contract integrity).

---

## Required fixes before W2 content waves

| # | Fix | Owner | Blocks |
|---|-----|-------|--------|
| 1 | Update `knowledge/index.md`: schema link → `[[ariadne-vault-schema]]` / `foundation/ariadne-vault-schema.md`; zones → `customers/` + `companies/` | Hephaestus | Agent retrieve + Clio W0/W2 bootstrap |
| 2 | Project-wide wikilink pass for `[[capture-llm-wiki]]` alias (Phase 3 step 3) | Hephaestus | INDEX / lint consistency |
| 3 | Bump schema §11 implementation row for entities 3b (partial/live) post–G2 ack | Hephaestus | Doc truth only |
| 4 | Harmonize [promote gate checklist](2026-07-02_vault-promote-gate-checklist.md) paths (`knowledge/thread/` → flat) | Hephaestus + Odysseus | Post-freeze promotes |
| 5 | Clio W1 path: `entities/company/` → `entities/companies/kbr-services-readiness-sustainment.md` in ingestion order | Clio (or Hephaestus note) | W1 hub refresh |

**W2 may proceed** once **#1** is done (minimum). **#2–#5** should complete before trusted promotes at scale or freeze lift.

---

## Promote freeze note

Until Overwatch lifts Item 4 cleanse freeze (flatten + lint + manifest sign-off per [vault cleanse program](2026-07-02_vault-cleanse-program.md)):

- **Do not** execute routine candidate→trusted promotes for W2 capability pages.
- **Do** write `generated-projections/*-candidate.md` (or approved in-place trusted edits on existing trusted pages per Clio wave table).
- **Emergency promote** only: Overwatch explicit intent + Odysseus PASS on cite gate — log incident if used.

---

## Related

- [Item 4 hybrid gate](2026-07-02_item4-odysseus-hybrid-gate.md) — G2 row **PASS**
- [Phase 3 schema ship](../../hephaestus/content/2026-07-02_phase3-ariadne-vault-schema-ship.md)
- [Clio ingestion waves](../../clio/content/2026-07-02_item4-clio-ingestion-order.md) — W2 KBR capabilities
- [Entities hierarchy design](../../hermes/content/2026-07-02_entities-hierarchy-design.md)