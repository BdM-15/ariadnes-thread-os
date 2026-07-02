# Wandermist / spectral graph — assessment vs Ariadne Thread OS

**Date:** 2026-07-02 · **Requestor:** Overwatch · **Coordinator:** Hermes · **Curator lens:** Hephaestus  
**Sources:** @wandermist (folder scaffolding article), @leopardracer (spectral graph viz thread), capform `capture-llm-wiki.md`, doc 02 revision draft, `01-PROGRAM-PRINCIPLES.md`

---

## Executive summary

| Question | Honest answer |
|----------|----------------|
| Is this relevant to our vault / compounding brain? | **Yes — on navigation scaffolding**, not on replacing vault doctrine. |
| Is spectral graph the right v1 bet? | **No** — viz is optional feedback; **INDEX maps** are the smallest high-leverage fix. |
| Does it conflict with capform / doc 02? | **No** — it **strengthens** retrieve contract + agent-maintained maps. |
| Lazy copy-paste risk? | **Medium** if we renumber entire repo or build viz before measuring; **low** if we add zone INDEX files + Hephaestus upkeep. |

**Recommendation:** Adopt **Wandermist INDEX pattern** at **major vault zones** + optional **agents/*/content/INDEX.md**; park **spectral visualization** as Hephaestus diagnostic (Wave 1.5+); fold one paragraph into doc 02 on **agent navigation scaffolding**. Do **not** reorganize federal ontology folders into “content type” chaos—or into vanity graphs.

---

## What the posts actually claim (evidence, not hype)

### Wandermist (@wandermist)

- **Problem:** Folders organized for **human content types** (articles, research, assets) force agents to **search everywhere**; archived vs current is invisible.
- **Fix (“smallest cage”):** (1) **One folder per concern** (workflow/topic), (2) **Number prefixes** for read order, (3) **`INDEX.md` at root of each major folder** — subfolders, canonical files, **where to start**, archive boundaries.
- **Measured:** Timed tasks before/after — wrong files opened dropped sharply; many tasks **~10–30s** vs **34s–2min**.
- **Philosophy:** Scaffolding > model; add maps only where agent gets lost; **don’t** INDEX every tiny subfolder; **don’t** over-nest.

### Leopardracer (@leopardracer)

- **Spectral layout:** Graph built from note links; **Laplacian eigenvector layout** clusters related notes visually.
- **Practical tie-in:** Same **`index.md` per major folder** story; viz shows **whether** the link graph is coherent after scaffolding fixes.
- **Not shipped as product:** Appears custom viz / Obsidian graph aesthetic — **diagnostic delight**, not retrieval engine.

### Comment signal worth keeping

@met_sun: speed = **smaller working set + clearer map + fewer irrelevant files** — aligns with Ponytail and our retrieve contract.

---

## Fit against **our** plan

### Already aligned

| Our design | Wandermist |
|------------|------------|
| Root `knowledge/thread/index.md` + `log.md` | Same “read map first” idea |
| `foundation/capture-llm-wiki.md` as Layer 3 contract | Their INDEX = per-zone map; we can mirror |
| Hermes triage B | Reduces junk entering vault — **smaller search space** |
| Wikilinks + `## Related` | **Graph** without folder reorg — capform/Karpathy |
| Agents maintain index (Hephaestus) | Answers “who updates site.xml?” — **agents**, not Overwatch |
| Ponytail / smallest fix | Their whole article is that |

### Gap we should close (high value, low cost)

| Gap | Fix |
|-----|-----|
| Only **root** index in doc 02 | Add **`INDEX.md` per major zone**: `entities/`, `pursuits/`, `global/`, `generated-projections/` |
| No “where to start” for capture concerns | Each INDEX: **3-line “For federal capture, start here”** + canonical entity/pursuit files |
| **Archived** vs active unclear | `06.Archived/` or `trust: archived` + INDEX boundary note (wandermist rule) |
| **agents/*/content/** agent retrieval | One **`INDEX.md` per agent `content/`** (optional v1) — map recent handoffs |

### Partial tension (resolve, don’t fork)

| Topic | Capform / doc 02 | Wandermist | Resolution |
|-------|------------------|------------|------------|
| Folder shape | Ontology (`entities/agencies/`) | Concern-based (`05.Brand/`) | **Hybrid:** ontology **is** capture concerns for federal lane; **pursuits/** = per-opp concern; don’t flatten to “Articles/Research” |
| Number prefixes | Not in capform seed | `01.`, `02.` folders | **Optional** for top-level zones only if agent confuses order; not required day one |
| Content-type folders | N/A in vault | Anti-pattern for agents | **Never** use in vault; staging stays per-agent |

### Spectral graph — v1 / v2 / v3 (Hephaestus view)

| Phase | What | Verdict |
|-------|------|---------|
| **v1 (Wave 1)** | Zone `INDEX.md` + retrieve contract + triage | **Do** |
| **v1.5** | Diagnostic: log files opened per agent task (agent-logs or skill) | **Do** when vault has ~20+ pages |
| **v2** | Wikilink export → simple HTML/obsidian graph (force or spectral layout) for **lint/orphans** | **Park** — Hephaestus afternoon project |
| **v3** | Embedding + Laplacian **clustering** to suggest new folders | **Park** — same class as capform 17c pgvector |

**Honest:** Spectral viz is **not** how agents should navigate in production. Agents read **INDEX.md**. Viz helps **you** and Hephaestus see cluster health—bonus, not architecture.

---

## Repo-wide “folder structure” (not just vault)

| Area | Wandermist applies? | Recommendation |
|------|---------------------|----------------|
| `knowledge/thread/` | **Primary** | Zone INDEX files + root index |
| `agents/*/content/` | **Yes** | Lightweight INDEX per agent (auto-append by Hephaestus cron) |
| `docs/inspiration/` | Low churn | Root `00-INSPIRATION-INDEX.md` already acts as INDEX |
| `agents/hermes/` etc. workspace | Low | No renumbering; ROUTER + REGISTRY are the map |
| Mission Control | N/A | Tabs are concerns; don’t duplicate vault tree in UI yet |

**Do not:** Renumber `agents/` or rebuild repo as `01.Capture/02.Intel/` without diagnostic proof.

---

## Five-minute diagnostic (Overwatch or Hermes can run)

Before any spectral toy or big reorg:

1. Pick **3 recurring tasks** (e.g. “what do we know about agency X?”, “summarize pursuit Y vault”, “find latest Iris intel handoff”).
2. Count **files read** and **time to correct answer**.
3. If **>3 wrong files** or **>30s** navigation repeatedly → add/refresh **INDEX.md** in the zone that failed—not new viz.

---

## Path forward (numbered, smallest first)

1. **Approve doc 02 revision** with new subsection: **§4.1 Agent navigation scaffolding (Wandermist pattern)** — zone INDEX files, archive boundaries, agent-maintained.
2. **Wave 1 implementation (Hephaestus):** bootstrap seeds `INDEX.md` stubs in `entities/`, `pursuits/`, `global/`, `generated-projections/` + template (“Where to start”, canonical files, archived note).
3. **Skill patch:** `vault_maintainer` or new `vault-index` — on promote/lint, update zone INDEX + root `index.md` (smallest script).
4. **Optional:** `agents/_shared/content-INDEX-template.md` for party content folders.
5. **Park:** Spectral HTML viz ticket in BACKLOG or Wave 3 inspiration — “vault graph health view” for MC or local HTML.
6. **Do not merge** wandermist **content-type** folder style into vault.

---

## Party brainstorm (condensed)

| Agent | Take |
|-------|------|
| **Hermes** | Triage B already cuts noise; **enforce** “read zone INDEX before grep wander” in retrieve contract. |
| **Hephaestus** | Curator of INDEX stubs + lint; spectral viz = **optional** export from wikilinks later. |
| **Iris** | `entities/agencies/` INDEX lists canonical agency pages—Iris updates on new candidate. |
| **Clio** | `pursuits/<slug>/INDEX.md` = opp concern map. |
| **Odysseus** | INDEX “canonical” line must not point at `trust: candidate` as default start. |

---

## Bottom line for Overwatch

You found the right idea at the right time: **the compounding brain fails if agents wander**. That’s fixable with **maps agents read first**—which is the same spirit as our `index.md`, extended per zone. **Spectral graph** is inspiring proof the **link structure matters**; for our minimalist OS, treat it as **later eye candy + lint**, not the foundation.

**Next decision:** Approve doc 02 **with** scaffolding subsection, or read this assessment first and ask for edits.