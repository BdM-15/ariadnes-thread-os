# Vault hardening — party brainstorm (pre–doc 02 acceptance)

**Date:** 2026-07-02  
**Overwatch blockers:** UI browse layout · path flatten · editable SSOT with Clio guardrails · clean-slate cleanse  
**Inspiration (current):** [@wandermist agent vault scaffolding](https://x.com/i/status/2071930382581195105) — concern-based folders, numbered priority, **INDEX.md maps**, active vs archived; structure > model size.

**Party delegation:** `deleg_251b596d` (Hephaestus UI, Clio edit workflow, Odysseus cleanse RACI) — Hermes will merge subagent detail into this doc when complete.

---

## 1. UI — browse cards vs scrollbar

**Symptom:** Vault browse list items (badge + title + full `generated-projections/...` path) visually overlap the sidebar vertical scrollbar.

**Likely cause (Hephaestus preview):**
- `.doc-item` / `.doc-time` show **full relative path** in monospace without `overflow: hidden; text-overflow: ellipsis`
- `.content-left` scroll region lacks right **padding** for scrollbar gutter (`scrollbar-gutter: stable` or `padding-inline-end`)
- Fixed-width badges + long paths on one row exceed inner width

**Proposed fix (minimal, Hephaestus DRI):**
- Scope CSS: `#panel-vault .content-left` or `.vault-doc-list`
- `doc-time`: ellipsis single line; **title** = human label; path in `title` tooltip only
- `doc-item`: `box-sizing: border-box; max-width: 100%`; optional two-line stack (badge row / path row)
- `scrollbar-gutter: stable` on `.doc-list` scroll container

**Acceptance:** No overlap at 1080p; queue + browse usable with 200+ entries.

---

## 2. Flatten `knowledge/thread/` → `knowledge/{zones}/`

**Intent:** Drop redundant `thread/` segment — repo **is** Ariadne’s Thread.

| Today | Proposed |
|-------|----------|
| `knowledge/thread/INDEX.md` | `knowledge/INDEX.md` |
| `knowledge/thread/entities/...` | `knowledge/entities/...` |
| `knowledge/thread/global/...` | `knowledge/global/...` |
| (same for foundation, generated-projections, pursuits, relationships) | |

**Touch matrix (Hephaestus migration):**
- `server.py` `VAULT_THREAD` path
- `scripts/bootstrap_knowledge_vault.py`, `vault_lint.py`, `promote_vault_candidate.py`, `seed_deferred_wikilink_stubs.py`
- `agents/_shared/VAULT_RETRIEVE.md`, `AGENTS.md`, inspiration doc 02
- MC copy: “read-only · knowledge” not `knowledge/thread`
- Board notes `vault:` paths
- Git: **one migration commit** + wikilink pass

**Risk:** Broken wikilinks and agent muscle memory — run `vault_lint` before/after; freeze promotes during cutover.

**Wandermist alignment:** Flat root `knowledge/` + zone folders = **concern folders**; keep zone `INDEX.md` “Where to go” sections (upgrade during cleanse).

---

## 3. Overwatch edit + Clio consistency

**Principle:** You edit **truth**; Clio enforces **shape** — not Hermes rewriting in chat.

| Trust | Overwatch in MC | Clio role |
|-------|-----------------|-----------|
| **candidate** (`generated-projections/`) | Full edit OK | Optional format pass on save |
| **trusted** (entities, global, pursuits, …) | Edit with warning banner | **Required** async “format harmonize” after save (frontmatter, headings, wikilinks, citations block) |
| **promote** | Not in UI v1 | Still Odysseus gate + script |

**Proposed flow:**
1. Hephaestus: `POST /api/vault/save` (path sandbox like read), Vault reader **Edit** like Content tab (trusted = read-only default toggle “Overwatch edit mode”).
2. On save: append `knowledge/log.md`; enqueue board task `vault:clio-harmonize:<path>` or cron slice.
3. Clio skill **`vault-format-harmonize`**: read `foundation/ariadne-vault-schema.md` (renamed schema); patch file; never delete trusted narrative without Odysseus flag.
4. Hermes morning queue surfaces “pending Clio harmonize” if drift detected.

**Anti-pattern:** Raw trusted edits without Clio pass → lint debt and production packet conflicts.

---

## 4. Clean-slate cleanse (production-grade SSOT)

**Goal:** Remove capform vestiges; one schema story aligned with doc 02 + wandermist scaffolding.

### Rename / replace

| Vestige | Action |
|---------|--------|
| `capture-llm-wiki` (name, id, prose) | → **`ariadne-vault-schema.md`** (or `foundation/vault-schema.md`) — Karpathy ingest retained, capform paths removed |
| `foundation/reference/obsidian-desktop.md` | Trim capform/gitignore assumptions; optional IDE only |
| Seeded stubs from capform merge | Audit `entities/`, `global/` for placeholder competitors/customers — Iris validates intel |
| `docs/reference/vault/capture-llm-wiki.md` (missing) | Do not recreate; pointer only in archive note |

### Wandermist mapping (not a full re-org day one)

| Wandermist | Ariadne zone |
|------------|--------------|
| Numbered concern folders | Optional **prefix** on pursuits/active opps only (e.g. `pursuits/01-active-...`) — pilot one folder |
| INDEX.md maps | **Required** at `knowledge/INDEX.md` + each zone root |
| `06.Archived` | New `knowledge/archive/` or `global/archive/` — move stale seed, not delete |
| Agent reads INDEX first | Already in `VAULT_RETRIEVE.md` — strengthen after flatten |

### Party RACI (cleanse program)

| Phase | Owner | Output |
|-------|--------|--------|
| **0 Freeze** | Hermes | No promotes; board quest `vault:cleanse` |
| **1 Inventory** | Hephaestus | Machine list + capform fingerprint grep |
| **2 Intel truth** | Iris | Entity/company pages — keep/fix/stub/archive |
| **3 Prose + FM** | Clio | Templates, harmonize, remove capform voice |
| **4 Trust + gates** | Odysseus | What stays trusted post-reset; citation minimum |
| **5 Migrate paths** | Hephaestus | flatten + schema rename + scripts |
| **6 MC** | Hephaestus | UI fix + vault save API + edit UX |
| **7 Lint green** | Hephaestus | `vault_lint` wikilinks → acceptable threshold |
| **8 Ratify** | Overwatch | Doc 02 acceptance + doc 03 |

**EDEN:** Stays candidate until cleanse confirms citations; no promote during reset without explicit gate.

---

## Recommended wave order (Overwatch approval)

| Wave | Scope | DRI |
|------|--------|-----|
| **A** | UI browse fix | Hephaestus (small, same day) |
| **B** | Schema rename draft + `ariadne-vault-schema.md` | Clio + Odysseus review |
| **C** | Path flatten migration | Hephaestus |
| **D** | Cleanse party pass (inventory → archive junk) | Hermes coordinates parallel Iris/Clio/Odysseus |
| **E** | Vault edit + Clio harmonize | Hephaestus + Clio |
| **F** | INDEX “Where to go” wandermist pass | Clio |

**Doc 02 acceptance** = after **A + C + D + lint threshold** (E can follow immediately after if you want edit same sprint).

---

## Decisions needed from Overwatch

1. **Flatten:** Approve `knowledge/{zones}` (no `thread/`) as SSOT path?  
2. **Cleanse depth:** **Hard reset** (archive all seeded trusted, rebuild from candidates + KBR SSOT) vs **surgical** (rename schema + delete known capform stubs only)?  
3. **Edit:** Trusted pages editable by you in MC with mandatory Clio harmonize — OK?  
4. **Wave order:** A→C→D→E or UI-only first?

Reply with choices (e.g. `flatten yes, surgical cleanse, edit yes, waves A+C+D`) and Hermes opens board quests + **delegate_task** per wave — **no Hermes MC/vault file implementation**.