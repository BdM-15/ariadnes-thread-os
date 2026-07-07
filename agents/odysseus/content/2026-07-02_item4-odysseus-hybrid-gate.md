# Item 4 — hybrid vault rebuild gate & salvage manifest taxonomy

**Date:** 2026-07-02  
**Owner:** Odysseus (trust + salvage gate) · **Ratify:** Overwatch  
**Inputs:** Hermes [item 4 brainstorm](../../hermes/content/2026-07-02_vault-item4-hybrid-rebuild-brainstorm.md), [cleanse program](2026-07-02_vault-cleanse-program.md), [promote gate](2026-07-02_vault-promote-gate-checklist.md)  
**Vault state:** `knowledge/` flattened (~224 `.md`); schema still `foundation/capture-llm-wiki.md` pending rename

---

## Purpose

Hybrid rebuild = **spine from primary sources** (Shipley guide, KBR public URLs, Overwatch templates later) + **salvage-by-exception** from the current tree. This doc defines:

1. **Hybrid gate** — when waves may move/archive/trust pages  
2. **Manifest taxonomy** — `KEEP | REWRITE | ARCHIVE | RESCOUT` per page or bucket  
3. **Phases** — ordered execution with freeze and lint exit

Hermes ratifies waves; Hephaestus executes moves; Iris owns **RESCOUT** evidence; Clio owns **REWRITE** prose; Odysseus signs manifest rows before archive or trusted retention at scale.

---

## Hybrid rebuild gate (master)

Runs **once** before Wave A archive/moves at scale, and **again** after each wave before the next wave opens.

### Preconditions (all required)

| # | Check | Owner |
|---|--------|-------|
| G0 | Board **`vault:cleanse`** active; **promote freeze** (no candidate→trusted except Overwatch emergency + Odysseus PASS) | Hermes |
| G1 | `knowledge/` path flatten complete; MC Vault tab reads flattened paths | Hephaestus |
| G2 | Draft **`foundation/ariadne-vault-schema.md`** exists (Agent OS story; capform UI/Postgres not mandatory Layer 1) | Hephaestus → Odysseus review |
| G3 | **Manifest v1** filed: zone buckets + exemplar paths tagged `KEEP|REWRITE|ARCHIVE|RESCOUT` (this doc § Manifest) | Odysseus + Iris parallel |
| G4 | Archive destination agreed: `generated-projections/archived/rebuild-2026/` | Overwatch |

### Gate verification (Odysseus)

| # | Question | Pass criterion |
|---|----------|----------------|
| V1 | Is any page promoted during freeze without PASS? | **Fail** — rollback promote; log incident |
| V2 | Do smoke entities remain **trusted** without manifest row? | **Fail** — must be ARCHIVE before wave close |
| V3 | Do capability pages cite **public KBR** or explicit `proof_strength: aspirational` + open question? | **Conditional** — RESCOUT queue for gaps |
| V4 | Do capture **concepts** used in router/skills have USAspending or intel lineage in body or cite? | **Conditional** — REWRITE or RESCOUT, not blind KEEP |
| V5 | `python scripts/vault_lint.py` | **Wave exit:** threshold agreed with Hephaestus (no new broken INDEX contract) |

### Outcomes

| Result | Meaning | Next |
|--------|---------|------|
| **GREEN** | Preconditions + V1–V2 pass; V3–V5 acceptable or queued | Hephaestus may execute manifest **ARCHIVE** rows; Clio/Iris may start **REWRITE/RESCOUT** waves |
| **YELLOW** | Salvage proceeds but **trusted** retention frozen for listed zones until RESCOUT clears | Document in `knowledge/log.md` |
| **RED** | Freeze violated or manifest missing | No bulk moves; Hermes reopens inventory |

---

## Manifest taxonomy (four verbs)

Use **exactly one** primary disposition per path (secondary note allowed, e.g. `KEEP (light REWRITE)`).

### Definitions

| Tag | Meaning | Who acts | Trusted after wave? |
|-----|---------|----------|---------------------|
| **KEEP** | Page meets 3/3 salvage rule (below); optional copy-edit only | Clio optional harmonize | **Yes** — stays or returns trusted |
| **REWRITE** | Idea/structure worth keeping; **must** be re-authored from primary source, not migrated prose | Clio (+ Odysseus for gate pages) | **After** rewrite + Odysseus cite gate |
| **ARCHIVE** | Smoke, duplicate, capform vestige, or ≤1/3 salvage rule | Hephaestus move to `archived/rebuild-2026/` | **No** — git history only |
| **RESCOUT** | Truth unknown or stale; **Iris** must refresh cites (KBR URL, USAspending, SAM) before KEEP/REWRITE/ARCHIVE final | Iris → updates manifest row | **No** until rescout → re-tag |

**RESCOUT is not a parking lot forever:** each RESCOUT row needs `due_wave` (A/B/C) and `source_spine` pointer.

### Salvage decision rule (3/3)

For each page:

1. **Primary source still true?** (Shipley section, KBR URL, Overwatch deck, USAspending field definition)  
2. **Cited and non-duplicate?** (YAML `citations` or inline provenance; no second trusted narrative for same `id`)  
3. **Used by agents today?** (`VAULT_RETRIEVE`, INDEX, router, capture skills, wikilink hub)

| Score | Default tag |
|-------|-------------|
| 3/3 | **KEEP** (or light REWRITE if capform voice) |
| 2/3 | **REWRITE** from spine |
| 1/3 | **RESCOUT** if intel gap; else **ARCHIVE** |
| 0/3 | **ARCHIVE** |

**Capture concepts bias:** if term appears in capture OS router/skills, default **RESCOUT** (not ARCHIVE) until Iris confirms USAspending lineage in ≤2 sentences of cite.

---

## Zone manifest (v1 — bucket + exemplars)

Scale: ~152 `global_wiki/`, ~46 `domain_intel/capabilities/`, ~42 `capture/concepts/`. Full machine list = Hephaestus inventory (cleanse phase 1); Odysseus signs **bucket policy** + **exemplars** below.

### Foundation & meta

| Path / bucket | Tag | Rationale |
|---------------|-----|-----------|
| `foundation/capture-llm-wiki.md` | **REWRITE** → `ariadne-vault-schema.md` | Rename + strip capform mandatory Layer 1 |
| `index.md`, zone `INDEX.md` chain | **KEEP** | Upgrade “Where to go” during waves |
| `log.md` | **KEEP** | Append-only audit |

### Entities

| Path | Tag | Rationale |
|------|-----|-----------|
| `entities/company/kbr-services-readiness-sustainment.md` | **KEEP** | SSOT hub; cites KBR RS URL |
| `entities/agencies/test-agency-xyz.md` | **ARCHIVE** | Smoke |
| `entities/competitors/example-competitor-llc.md` | **ARCHIVE** | Smoke |
| Other `entities/agencies/*`, `entities/competitors/*` (if any) | **RESCOUT** | Iris validates before trusted |

### Source spine — KBR (Wave A)

| Spine URL | Target zone | Default bucket tag |
|-----------|-------------|-------------------|
| [readiness-and-sustainment](https://solutions.kbr.com/readiness-and-sustainment/) | `entities/company/` + capability links | Hub **KEEP**; capabilities **RESCOUT** until URL cite per page |
| [kbr-digital-accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) | `domain_intel/capabilities/` | **REWRITE** / **RESCOUT** — no duplicate catalog stubs |

| Capability exemplar | Tag | Note |
|---------------------|-----|------|
| `capabilities/*` with `auto_generated: true`, thin cite | **RESCOUT** | Map to KBR public product pages |
| `capabilities/*` with `proof_strength: aspirational` | **REWRITE** | Keep claim class; add public cite or open question |
| Duplicate capability titles (grep `name:`) | **ARCHIVE** one; **KEEP** canonical |

### Source spine — Shipley (Wave B)

| Bucket | Tag | Note |
|--------|-----|------|
| `global_wiki/` capture + evaluation prose (~23 Shipley-tagged pages per `global-wiki.md`) | **REWRITE** | Re-author from **Shipley Capture Guide**; Odysseus gate alignment to MS1–4 |
| `global/domain_intel/milestones/ms1–ms4*.md` | **KEEP** + light **REWRITE** | MS decision gates; link to new Shipley pages |
| `global_wiki/capture/gate-review-process.md` etc. | **REWRITE** | Must match Overwatch gate slides when templates land (Wave D) |

### USAspending capture concepts (Wave C)

| Bucket | Tag | Note |
|--------|-----|------|
| `global_wiki/capture/concepts/*.md` (42) | **RESCOUT** default | Iris: USAspending field / dashboard lineage in cite block |
| Concepts in `capture-insights-index.md` + router | **RESCOUT** → **KEEP** if cite added | e.g. `qual-gate`, `recompete-radar`, `follow-the-money` |
| Concepts with only “Capture Insights dashboard” and no field cite | **REWRITE** or **ARCHIVE** after rescout fails |

| Concept exemplar | Tag |
|------------------|-----|
| `concepts/qual-gate.md` | **RESCOUT** — Shipley proxy + USAspending slice; strengthen cite |
| `concepts/sam-live-discovery.md` | **KEEP** candidacy — verify SAM vs USASpending wording |

### Generated projections & pursuits

| Path | Tag |
|------|-----|
| `generated-projections/eden-edge-computing-candidate.md` | **KEEP** candidate — no promote during freeze |
| `generated-projections/archived/rebuild-2026/` (destination) | **n/a** — archive target |
| `pursuits/*` smoke | **ARCHIVE** |
| Active pursuit folders (Overwatch-named) | **RESCOUT** per folder |

### Templates (Wave D — deliberate)

| Source | Tag |
|--------|-----|
| Call plan, risk register, MS gate slides | **REWRITE** one template per Overwatch pick — not bulk import |
| Until Wave D approved | **ARCHIVE** capform template stubs without Overwatch owner |

---

## Phases (Odysseus-signed)

Aligned with Hermes item 4; Odysseus adds **gate checkpoints**.

```
Phase 0  FREEZE          promote freeze + vault:cleanse          [G0]
Phase 1  MANIFEST       this doc + Iris rescout list + Clio wave plan [G3]
Phase 2  HYBRID GATE    Odysseus GREEN/YELLOW/RED               [§ Gate]
Phase 3  ARCHIVE        Hephaestus: ARCHIVE rows only           [after GREEN]
Phase 4  SCHEMA         ariadne-vault-schema.md                   [G2]
Phase 5  WAVE A         KBR company + top capabilities            [RESCOUT→REWRITE]
Phase 6  WAVE B         Shipley core (Clio-led)                   [REWRITE]
Phase 7  WAVE C         Concepts salvage (Iris tags each file)    [RESCOUT]
Phase 8  WAVE D         Templates one-at-a-time (Overwatch order) [REWRITE]
Phase 9  LINT GREEN     Hephaestus; then item 3 MC edit scope     [G5]
```

**Between waves:** mini-gate — no new **trusted** pages without Odysseus cite check (same bar as [promote gate](2026-07-02_vault-promote-gate-checklist.md), applied to in-place REWRITE promotions).

---

## Manifest row template (per file)

Hephaestus inventory should emit CSV or md table rows:

```yaml
path: knowledge/global/.../foo.md
disposition: RESCOUT   # KEEP | REWRITE | ARCHIVE | RESCOUT
score_3of3: 2
source_spine: https://solutions.kbr.com/...
owner: iris
due_wave: A
odysseus_signed: false
notes: ""
```

Odysseus sets `odysseus_signed: true` when row is final for Phase 3 archive execution.

---

## RACI (rebuild steady state)

| Action | Responsible |
|--------|-------------|
| Manifest taxonomy & hybrid gate | Odysseus |
| RESCOUT evidence & URL cites | Iris |
| REWRITE trusted prose | Clio |
| ARCHIVE moves, schema, lint | Hephaestus |
| Wave board + Overwatch ratification | Hermes |

---

## Overwatch decisions (unchanged from item 4)

1. **Hybrid confirmed?** (recommended: yes)  
2. **Archive path:** `generated-projections/archived/rebuild-2026/`  
3. **First wave after manifest:** A KBR · B Shipley · C concepts  
4. **Cleanse depth:** minimal vs full archive of seeded trusted  

Odysseus default for (4): **full archive of smoke + auto_generated capabilities without cite**; **RESCOUT** for concepts and KBR-linked pages; **REWRITE** for Shipley doctrine.

---

## References

- `agents/hermes/content/2026-07-02_vault-item4-hybrid-rebuild-brainstorm.md`
- `agents/odysseus/content/2026-07-02_vault-cleanse-program.md`
- `docs/inspiration/knowledge-vault-and-compounding-truth.md`
- `agents/_shared/VAULT_RETRIEVE.md`