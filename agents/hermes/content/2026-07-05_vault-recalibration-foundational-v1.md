# Vault recalibration — foundational v1 vs “ready to use” (2026-07-05)

**Overwatch correction:** Overnight progress was **KBR capability spine (Clio waves W2–W5 candidates)**, not **foundational v1 complete**. Do **not** treat the vault as production-ready until Shipley guide review, templates, and exit criteria below are done.

**Branch:** `feature/knowledge-vault-v1` · **No merge to `main`** until you sign off foundational v1.

---

## What we actually finished (narrow slice)

| Clio wave (original plan) | What happened | Honest status |
|---------------------------|---------------|---------------|
| **W2–W3** KBR capabilities + accelerators | Iris rescout → Clio candidates → lighthouse promotes | **Done** (31 capability promotes + Vaault children) |
| **W5 (mislabeled)** | We used “W5” for **next manifest capability batch** (cyber range, RESAN, etc.) | **Candidates only** (`ed984a1`) — **not promoted** |
| **W4–W5 Shipley** | Not started from **your Capture Guide** | **Not started** (one legacy `shipley-business-development-lifecycle.md` exists; not guide-driven) |
| **W6** Concepts salvage | Not run | **Not started** |
| **W7** Company templates | Not run | **Not started** (needs you: one template at a time) |
| **W8** Harmonize | Not run | **Not started** |
| **W1** Company hub v2 | Unclear / light | **Likely incomplete** vs Clio W1 spec |

**Karpathy shell:** `index.md`, `log.md`, schema, Obsidian optional doc, retrieve contract — **good scaffolding**, not full content foundation.

---

## Immediate backlog (capability tail — ~1–2 sessions)

| # | Work | Notes |
|---|------|--------|
| 1 | **Promote W5 batch A** | 10 candidates → trusted (covers 10 of 12 `auto_generated: true` capability stubs) |
| 2 | **Viaverse + Wraith** | Iris rescout (2) → Clio candidates → promote (no W5 candidates yet for these two) |
| 3 | **EDEN** | `eden-edge-computing-candidate.md` — meeting-driven; promote only after your/Odysseus gate |

After #1–2: **capability zone** should have **0** `auto_generated: true` stubs (47 slug files).

---

## Foundational v1 still required (before “we use it daily”)

Per [item 4 execution plan](http://127.0.0.1:51763/#content/hermes/2026-07-02_vault-item4-execution-plan.md) and [Clio ingestion order](http://127.0.0.1:51763/#content/clio/2026-07-02_item4-clio-ingestion-order.md):

### A — Overwatch inputs (blocking)

| Input | Why |
|--------|-----|
| **Shipley Capture Guide** path or drop (PDF/DOCX/MD) | **W4–W5** cannot be authoritative without your SSOT |
| **Template order** (call plan, risk register, MS1–4 slides, etc.) | **W7** one-at-a-time |
| **Manifest v1 zone sign-off** (if never formal) | Odysseus bucket policy + exemplars |
| **Promote freeze lift** | When foundational v1 is ready, you + Odysseus lift freeze for routine promotes |

### B — Party work (no substitute for A)

| Phase / wave | Owner | Deliverable |
|--------------|-------|-------------|
| **W1** Company hub | Iris + Clio | `entities/companies/kbr-services-readiness-sustainment.md` v2 (short hub, wikilinks) |
| **W4** Shipley lifecycle | Clio from **your guide** | Hub + phase pages under `global/global_wiki/shipley/` |
| **W5** Shipley tools/reviews | Clio | Pink/Red/Gold/Black, win themes, compliance matrix chunks + links to milestones |
| **W6** Concepts | Iris + Clio | REWRITE rows from manifest — USAspending cites, strip capform voice |
| **W7** Templates | Clio + you | One trusted template page per approval |
| **W8** Harmonize | Clio | Format pass on all pages touched in W1–W7 |
| **Entities migration** (if pending) | Hephaestus | `customers/` / `organizations/` per entities hierarchy design |
| **Phase 5 exit cleanse** | Hermes + Odysseus | Lint green, freeze lifted, re-scope MC vault item 3 |

### C — Hygiene (parallel, lower drama)

- `vault_lint` green; reduce unresolved wikilinks (stubs or links)
- Commit untracked party `content/` docs when useful (execution plan, ingestion order, cleanse program)
- **Item 3** Mission Control vault edit/harmonize — **after** schema + foundational content stable

---

## Suggested sequence (recalibrated)

```
Now     → Promote W5 (10) + Viaverse/Wraith (2)     [close capability stubs]
Next    → You provide Shipley Capture Guide          [unblocks W4–W5]
Then    → Odysseus: guide intake + outline gate     [what to author vs skip]
Then    → Clio W4 → W5 Shipley pages                [trusted, cited to guide]
Then    → W1 hub + W6 concepts + W7 templates (your order)
Then    → W8 harmonize + freeze lift + your foundational v1 review
Then    → Merge `main` (only when you approve)
```

---

## What “vault complete” should mean (your bar)

1. **Retrieve-first** works on **company + capabilities + Shipley + templates**, not just KBR product pages.  
2. **Shipley** reflects **your** capture guide, not seeded wiki stubs.  
3. **Templates** you actually use are in vault with “how to use” sections.  
4. **Promote discipline** documented; freeze lifted for normal capture ops.  
5. **Obsidian optional** on `knowledge/` — same SSOT Hermes uses.

---

## Your next decision (pick one or more)

1. **“Promote W5 + viaverse/wraith”** — Hermes runs capability tail only.  
2. **“Park capabilities; start Shipley”** — you drop guide path in chat or `agents/hermes/content/`.  
3. **“Ratify manifest + W1 hub first”** — Odysseus/Clio before more promotes.

*Hermes will not call foundational v1 complete until you agree this checklist (or a revised one) is satisfied.*