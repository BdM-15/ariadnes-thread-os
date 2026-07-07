# Item 4 — hybrid ground-up vault rebuild (party brainstorm)

**Date:** 2026-07-02  
**Overwatch:** Rebuild for agentic OS; **hybrid** (sources + selective salvage) vs full wipe  
**Party batch:** `deleg_481f8c63` (Odysseus manifest · Clio ingestion · Iris rescout) — addenda when land

---

## Hermes recommendation (short)

**Yes — hybrid, party-led rebuild.** Do **not** treat the current tree as SSOT. Do **not** delete it blindly either.

Use **primary sources as spine**, current vault as **salvage inventory**, agents as **authors** (not migrators). Overwatch ratifies **manifest + waves**, not 200 file-by-file clicks.

---

## Why hybrid beats “clean wipe” or “keep seeding”

| Approach | Problem |
|----------|---------|
| **Keep mass seeding** | Capform/bootstrap noise (smoke entities, thin cites, duplicate capability stubs) compounds lint debt and wrong agent beliefs. |
| **Full wipe, no salvage** | You lose **42** `capture/concepts` pages and **46** capability pages that may encode real USAspending / capture logic — expensive to rediscover. |
| **Hybrid (recommended)** | Rebuild **narrative and structure** from Shipley + KBR public + your templates; **promote-by-exception** only pages that pass a manifest gate. |

Current scale (indicative): **~23** Shipley pages, **~46** domain_intel capabilities, **~42** capture concepts — too large to “remember and recreate” without a manifest.

---

## Source spine (Overwatch canon)

| Source | Vault home (target) | Owner | Notes |
|--------|---------------------|-------|-------|
| **Shipley Capture Guide** | `global/global_wiki/shipley/` (+ linked capture/evaluation) | **Clio** prose · **Odysseus** gate alignment | Majority doctrine — **re-author** from guide, don’t assume current split is final IA |
| **KBR RS** — [readiness-and-sustainment](https://solutions.kbr.com/readiness-and-sustainment/) | `entities/company/` hub + `domain_intel/capabilities/` | **Iris** rescout · **Clio** distill | Public citations required on every capability claim |
| **KBR Digital Accelerators** — [kbr-digital-accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) | `domain_intel/capabilities/` (+ discriminators) | **Iris** · **Clio** | Map accelerators to capability pages; avoid duplicate “catalog” pages |
| **Call plan / risk register / MS1–4 gate slides** | `global/global_wiki/capture/` or `foundation/reference/` (one template at a time) | **Clio** · **Odysseus** for gates | **Deliberate:** one approved template per wave — not bulk import |
| **USAspending-derived concepts** (`global_wiki/capture/concepts/`) | Same zone, **subset** | **Iris** + **Odysseus** | **KEEP** only if manifest shows: defined term, USAspending or intel cite, used in router/retrieve path |

---

## Party roles (steady state)

| Agent | Rebuild job |
|-------|-------------|
| **Hermes** | Waves, board quests, manifest ratification, triage B — **no vault body writes** |
| **Iris** | Rescout URLs; raw intel in `iris/content/`; candidates with cites |
| **Clio** | Shipley + template voice; readable trusted pages; harmonize after promote |
| **Odysseus** | KEEP/ARCHIVE rules; promote freeze; MS gate template alignment |
| **Hephaestus** | `ariadne-vault-schema.md`, lint, promote script, archive folder moves, MC read-only |

**“Party remembers and creates clean”** = each specialist **re-reads sources + manifest**, writes **new** trusted pages (or v2 candidates), not copy-paste of old markdown.

---

## Proposed phases (after items 1–2 committed)

```
0. FREEZE — no promotes; board `vault:cleanse` active
1. MANIFEST — parallel: Odysseus categories + Iris rescout list + Clio wave plan
2. ARCHIVE — move smoke/duplicate to `generated-projections/archived/rebuild-2026/` (git history retains)
3. SCHEMA — `foundation/ariadne-vault-schema.md` (Agent OS, not capform UI)
4. WAVE A — Company SSOT + top 10 capabilities from KBR URLs (Iris→Clio→Odysseus)
5. WAVE B — Shipley core (Clio-led, chunk by lifecycle phase)
6. WAVE C — Salvage concepts (Iris tags each concept KEEP|REWRITE|DROP)
7. WAVE D — Templates one-at-a-time (Overwatch picks order)
8. LINT GREEN — Hephaestus; then item 3 (MC edit) scoped to **new** zones
```

---

## Salvage decision rule (default)

For each existing page:

1. **Primary source still true?** (URL, Shipley section, your slide deck)  
2. **Cited and non-duplicate?**  
3. **Used by agents today?** (retrieve contract, wikilinks from INDEX)

- **3/3** → KEEP (maybe light rewrite)  
- **2/3** → REWRITE from source  
- **≤1** → ARCHIVE or DROP  

Capform **concepts**: bias **KEEP candidacy** if term appears in capture OS skills/router; Iris verifies USAspending lineage in 1–2 sentences of cite.

---

## What we should not do

- Re-import capform Postgres or `data-elements/` as mandatory Layer 1  
- Bulk LLM “summarize entire vault into one folder” (loses audit trail)  
- Ship MC edit (item 3) before schema + manifest signed  
- Let Hermes patch vault bodies in parent session  

---

## Overwatch decisions needed (pick any)

1. **Hybrid confirmed?** (recommended: yes)  
2. **Archive path OK?** `generated-projections/archived/rebuild-2026/`  
3. **First rebuild wave after manifest:** **A** KBR capabilities · **B** Shipley · **C** concepts salvage  
4. **Full vs minimal cleanse:** minimal = schema rename + smoke archive + waves; full = archive most seeded trusted, rebuild only from spine  

---

## Party addenda (`deleg_481f8c63` — on disk)

| Agent | Artifact | Role |
|-------|----------|------|
| Odysseus | [2026-07-02_item4-odysseus-hybrid-gate.md](http://127.0.0.1:51763/#content/odysseus/2026-07-02_item4-odysseus-hybrid-gate.md) | G0–G4 gates, `KEEP\|REWRITE\|ARCHIVE\|RESCOUT`, zone buckets, phases 0–9 |
| Clio | [2026-07-02_item4-clio-ingestion-order.md](http://127.0.0.1:51763/#content/clio/2026-07-02_item4-clio-ingestion-order.md) | Waves W0–W8, Shipley chunk order, KBR W2 priority, page standards A–F |
| Iris | [2026-07-02_item4-iris-source-rescout.md](http://127.0.0.1:51763/#content/iris/2026-07-02_item4-iris-source-rescout.md) | Tier 1–4 URL inventory, 46 caps weak cites → RESCOUT, 42 concepts USAspending bias KEEP |

### Hermes consolidated read (post-party)

1. **Hybrid is the operating model** — party docs align: spine + manifest, not wipe, not keep-all.
2. **Wave order tension resolved:** Clio sequences **W1 company → W2–W3 KBR → W4–W5 Shipley → W6 concepts**; your earlier “A/B/C” maps to **KBR first, then Shipley, then concept salvage** — good default for *bid credibility* before doctrine depth.
3. **Capabilities need RESCOUT before trust** — Iris: zero `citations:` in frontmatter; Wave A must add Tier-1 URLs before any KEEP.
4. **Concepts: don’t bulk-archive** — 41/42 have USAspending sections; Odysseus default bucket RESCOUT/REWRITE, not ARCHIVE.
5. **Blocked until Overwatch ratifies:** G4 archive path, manifest v1 sign-off, promote freeze on board (`vault:cleanse` → **in_progress** when you say go).
6. **Next mechanical step:** Hephaestus Phase 1 machine inventory CSV (paths + proposed tag) — Odysseus signs rows; then archive smoke + Wave W1.

## Model uplift — scout to beat the old vault (Overwatch 2026-07-02)

**Intent:** Iris (and party) should **actively try to outperform** capform/bootstrap vault quality, not parity-migrate. Models and tooling are stronger than at first build; hybrid rebuild is the moment to **re-derive** from primary sources with stricter bars.

| Old vault weakness | New standard (Iris → Clio) |
|--------------------|----------------------------|
| `auto_generated` caps, **0** `citations:` frontmatter | Every trusted capability: **≥1 Tier-1 URL** + retrieval date; Iris export in `content/` before Clio promote |
| Thin / duplicate capability stubs | **One page per discriminating claim**; dedupe pass in W3 accelerators vs W2 |
| USAspending concepts as bulk seed | **Re-query** USAspending (or current public data) where term is still active; update Key signals or mark ARCHIVE |
| Shipley pages split ad hoc | Re-chunk from **Capture Guide** with Clio standards A–F; cross-link lifecycle, don’t orphan concepts |
| “Sounds right” synthesis | **Evidence table** per page (source URL, quote/snippet, confidence); Odysseus rejects promote without row |

**Party pattern:** **Scout → compare → author**

1. **Iris** rescouts URL/PDF/USAspending; writes `agents/iris/content/*-rescout-YYYY-MM-DD.md` with structured extracts (not vault writes until manifest row).
2. **Side-by-side** (lightweight): for each RESCOUT path, Iris notes *old vault gap* (missing cite, stale claim, wrong scope) in rescout doc — no need for automated diff tooling in v1.
3. **Clio** authors **new** trusted body from rescout + Shipley; old file only informs manifest tag, not copy-paste.
4. **Hermes** boards quests per wave; **no** “bulk LLM refresh entire tree” cron — wave-bound quality gates only.

**What not to do:** Trust model fluency without cites; re-run old prompts on old files; let Hermes parent session write `knowledge/` bodies.

**When this runs:** W2–W3 (KBR) and W6 (concepts) are the highest ROI for uplift; W4–W5 Shipley is mostly **structure + voice**, not net-new intel.

## Related

- Odysseus program: `agents/odysseus/content/2026-07-02_vault-cleanse-program.md`  
- Item 3 deferred: `agents/hermes/content/2026-07-02_vault-item3-deferred.md`  
- Commit 1–2: `23eb023`