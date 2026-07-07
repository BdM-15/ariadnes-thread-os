# Item 4 — execution plan & Overwatch inputs

**Date:** 2026-07-02  
**Status:** Awaiting Overwatch ratification before Phase 0 execution  
**Master refs:** [hybrid brainstorm](2026-07-02_vault-item4-hybrid-rebuild-brainstorm.md) · Odysseus gate · Clio waves · Iris rescout

---

## Part A — What Hermes needs from you (checklist)

Provide **once** before we move files or promote during cleanse:

| # | Your input | Required? | Notes |
|---|------------|-----------|--------|
| 1 | **Ratify hybrid model** (sources + manifest salvage, not full wipe) | **Yes** | One line: e.g. `hybrid yes` |
| 2 | **Archive path OK** | **Yes** | Default: `generated-projections/archived/rebuild-2026/` |
| 3 | **First content wave after manifest** | **Yes** | Default recommended: **KBR-first** (Clio W1→W3), then Shipley W4–W5, concepts W6 |
| 4 | **Cleanse depth** | **Yes** | **Minimal** = smoke + un-cited auto caps archived, spine rebuilt · **Full** = archive most seeded trusted, rebuild only from spine |
| 5 | **Promote freeze ack** | **Yes** | No candidate→trusted during cleanse except you + Odysseus emergency PASS |
| 6 | **Shipley Capture Guide** | **When W4 opens** | Path or drop zone: PDF/DOCX/markdown you trust as SSOT (if not already in repo) |
| 7 | **Templates (call plan, risk register, MS1–4 slides)** | **Per W7+ wave** | One file at a time when we open that wave — you pick order |
| 8 | **Company facts that are NOT on public web** | **As needed** | Cleared program names, internal discriminators, UEI-sensitive notes → paste or `content/` handoff; Iris won’t invent |
| 9 | **Manifest v1 sign-off** | **After Phase 1** | Hephaestus CSV + Odysseus bucket tags — you approve KEEP list at zone level (not 224 clicks) |
| 10 | **MC restart** | **After each MC commit** | Local: restart Mission Control so `server.py` matches `knowledge/` |

**You do NOT need to:** run CLI, edit vault folders by hand, review every page before archive of smoke files, or provide API keys in chat (local Hermes profiles only).

---

## Part B — Execution steps (Hermes order)

### Phase 0 — Gate (Hermes, ~same day you ratify)

1. Record your Part A answers in board notes on `vault:cleanse`.
2. Set `vault:cleanse` → **in_progress**; announce **promote freeze** on board.
3. Confirm G1 done: flatten + commit `23eb023` (already shipped).
4. Open child tasks (board): manifest inventory, schema rename, archive smoke.

### Phase 1 — Manifest (party parallel, no trusted deletes yet)

| Step | Owner | Output |
|------|-------|--------|
| 1.1 Machine inventory | **Hephaestus** | CSV: every `knowledge/**/*.md` → proposed `KEEP\|REWRITE\|ARCHIVE\|RESCOUT` |
| 1.2 Rescout sheet merge | **Iris** | Tier-1 URL appendix + top-10 capability gap notes vs current files |
| 1.3 Bucket policy sign | **Odysseus** | Manifest v1: zone defaults + exemplar paths |
| 1.4 **Overwatch** | **You** | Approve manifest v1 (zones + exemplars; escalate disputes only) |

### Phase 2 — Archive smoke (Hephaestus executes, Odysseus gate)

1. Move **ARCHIVE** rows: smoke entities, agreed placeholders → `generated-projections/archived/rebuild-2026/`.
2. Run `vault_lint`; fix broken wikilinks in INDEX stubs only.
3. Odysseus mini-gate → GREEN before Wave W1.

### Phase 3 — Schema (Hephaestus + Odysseus)

1. Draft `foundation/ariadne-vault-schema.md` (Agent OS; no capform UI mandate).
2. **§ Entities** must embed [entities hierarchy design](2026-07-02_entities-hierarchy-design.md) — flat `customers/` + `organizations/`, typed frontmatter, no deep program/office folders.
3. Alias pass for `[[capture-llm-wiki]]` → new name (one release).
4. You **ack** schema intent (no need to line-edit unless you want).

### Phase 3b — Entities migration (after schema ack)

1. Hephaestus: one script `agencies/` → `customers/`, `competitors/` + `company/` → `organizations/` with frontmatter `type` / `org_role` updates.
2. `vault_lint` + fix `entities/INDEX.md` (remove stale `knowledge/thread/` paths).
3. Odysseus **E1–E3** gate before new customer pages in waves.

### Phase 4 — Content waves (scout → compare → author)

Order per **Clio W0–W8** (default KBR before Shipley):

| Wave | Party | Overwatch provides |
|------|-------|-------------------|
| **W1** Company hub | Iris rescout → Clio rewrite | Nothing if public RS hub enough |
| **W2–W3** KBR capabilities + accelerators | Iris **model uplift** rescout → Clio trusted pages | Internal discriminators only if public pages insufficient |
| **W4–W5** Shipley | Clio from **Capture Guide** | **Guide file/path** (item 6 above) |
| **W6** Concepts salvage | Iris re-query USAspending where active → Clio REWRITE rows | Flag any concept you want **forced KEEP** |
| **W7+** Templates | Clio one page per wave | **One template** per approval |
| **W8** Harmonize backlog | Clio + board tasks | Your ratify on promotes |

Each wave: Odysseus mini-gate → lint → you notified in MC Content + board.

### Phase 5 — Exit cleanse

1. `vault_lint` green; promote freeze **lifted** by you + Odysseus.
2. Re-scope **item 3** (MC edit + Clio harmonize) against **new** schema zones.
3. Hermes closes `vault:cleanse`; doc 03 / inspiration wave when you direct.

---

## Part C — What runs without you in the room

- Hephaestus inventory CSV, archive moves, lint, schema draft, MC read-only fixes (delegated).
- Iris public URL / USAspending rescout → `iris/content/`.
- Clio drafts → candidates or trusted per manifest (not before freeze rules).
- Odysseus gate docs and manifest rows.

**Always needs you:** ratify Part A, manifest v1, promote freeze lift, each **template** wave, any **non-public** company fact, merge to `main` if you keep branch protection.

---

## Part D — Suggested one-message ratification (copy/paste)

```
hybrid yes
archive: generated-projections/archived/rebuild-2026/
wave order: KBR-first (W1–W3), then Shipley, then concepts
cleanse: minimal
promote freeze: acknowledged
proceed Phase 0–1
```

Optional same message:

```
Shipley guide at: <path or "in repo at …">
```

---

## Part E — Current blockers

- Part A not yet recorded → **no archive moves**, no manifest execution.
- Party brainstorm + addenda on disk; **not** committed to git (optional doc commit when you want).

**Next Hermes action after your ratification:** Phase 0 board + delegate Hephaestus Phase 1 inventory CSV.