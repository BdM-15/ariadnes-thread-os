# Knowledge vault and compounding truth

**Wave 1 inspiration doc 02** · Primary owner: Hephaestus · **Merged:** 2026-07-02 (Overwatch approved)

Capform anchors (read-only intent): `docs/PLAN.md` two-store doctrine, `docs/reference/vault/capture-llm-wiki.md`, `knowledge_routes.py` / `vault_write.py` (zones only—do not port), `bootstrap/vault.py`, `docs/BACKLOG.md` § Knowledge.

---

## 0. Overwatch north star — compounding decision brain

**Operator desire:** An automated, **living** knowledge system that works like external memory: absorb information from data, documents, and your actions; convert it into **truth you can trust**; surface **connections** you cannot hold in biological working memory while juggling competing priorities and limited time.

**System promise:**

| Human limit | Agent OS answer |
|-------------|-----------------|
| Cannot recall everything across pursuits | **Trusted vault pages** + retrieve-before-answer |
| Cannot maintain consistency alone | **Stable entity/pursuit narratives** with citations |
| Fleeting thoughts lost | **Hermes triage** → knowledge, action, or discard |
| No time to organize | Agents **build foundation**, **compound**, **lint**, **index** |
| Must not trust unverified AI output | **Candidate → Overwatch ratify → trusted** (execution confirm, not memory recall) |

**Not the goal:** A static wiki, a capform UI port, or Obsidian as a product requirement. **The goal:** compounding truth that **informs the next decision** without you reconstructing the graph each Monday.

**Overwatch role:** Confirm execution at the **trust boundary**—approve promotes, reject bad synthesis, dump raw input freely. You do **not** maintain folders, indexes, or link graphs by hand.

---

## 1. Operator job (one sentence)

Give Overwatch a **compounding knowledge brain** agents feed and maintain; you **ratify** what becomes trusted truth and **confirm** triage into valuable actions—without carrying the full graph in your head.

---

## 2. Why capform built it (scaffold honesty)

Capform separated **execution truth** (PostgreSQL) from **compounding synthesis** (`knowledge/thread/`) under review-gated promotion. That solved a real capture problem: raw intel and chat are poor substitutes for **linked, cited, reusable** narratives.

**What shipped vs parked in capform** is documented in prior research: browser + API + heavy write services ✅; full auto-compound + semantic search 🟡/📋. thread-os **inherits intent**, not the monolith.

**Why we still use a filesystem wiki in thread-os:** Agents already read/write markdown; diffs are auditable; promotion is a **file state change** without Postgres on day one. This follows **agentic OS** fit, not lazy clone—see §7 anti-patterns.

---

## 3. True intent (decision enabled)

- **Absorb:** Intel, PDFs, URLs, packet work, your notes and ideas.  
- **Synthesize:** Entities, pursuits, relationships, grounded bullets + citations.  
- **Compound:** Append-only trusted history; related pages updated on each ingest.  
- **Retrieve:** Before major intel/fill/strategy answers, agents **query the vault** (index → pages → wikilinks).  
- **Act:** Not everything becomes a page—some inputs become **tasks**, **capture loop steps**, or **cron** (Hermes triage).

**Decisions enabled:** “What do we already believe about this agency?” “What did pursuit A teach for pursuit B?” “Is this duplicate?” “What needs my confirm today?”

---

## 4. Mission Control / agent fit

### Two text layers (no third brain)

| Layer | Role | Location |
|-------|------|----------|
| Work staging | Session handoffs | `agents/<agent>/content/*.md` → MC **Content** |
| Compounding SSOT | Candidate + trusted wiki | `knowledge/thread/` |
| Hermes memory | Prefs only | Not the knowledge base |

### Canonical root

`<repo-root>/knowledge/thread/` — matches capform schema seed, Obsidian-optional, agent tooling. Obsidian is a **human IDE**, not the brain.

### Layers (thread-os v1, no Postgres)

| Layer | v1 | Rule |
|-------|-----|------|
| Raw | Iris exports, cited URLs/files | Read-only for vault writers |
| Wiki | `knowledge/thread/` | Candidates in `generated-projections/`; trusted in write zones |
| Schema | `foundation/capture-llm-wiki.md` | Idempotent seed |

**Review without PG:** frontmatter `trust`, `reviewed_by`, `reviewed_at`, `review_id` + append-only `log.md`.

### Hermes intake triage (default — Overwatch preference **B**)

**All** unstructured Overwatch input (chat dump, idea, “remember this”, doc reference, voice→text later) goes to **Hermes first**. Hermes classifies and routes; Overwatch does **not** sort into vault vs task manually.

| Triage outcome | When | What happens |
|----------------|------|----------------|
| **Vault candidate** | Durable fact, entity, doctrine, pursuit learning | Write `generated-projections/<slug>-<date>.md`, `trust: candidate`; cite sources |
| **Action** | Task, follow-up, maintenance, delegate | Route to Tasks/capture loop / `delegate_task` / board—**not** vault |
| **Capture artifact** | Opp-specific, packet-shaped | Clio/Odysseus path; may **later** promote synthesis to vault |
| **Discard** | Duplicate, noise, already trusted | Log one line in Hermes reply; no file |
| **Uncertain** | Ambiguous or high-stakes | **Overwatch queue**: Hermes presents 2–3 line recommendation + “confirm A/B/C?” |

**Principles:**

- LLM reasoning **prepares**; Overwatch **ratifies** at trust boundary and on uncertain triage.  
- **No auto-promote** to `trust: trusted`.  
- Hermes **summarizes** morning queue: new candidates + uncertain items + pending promotes (not full vault dump).

**Retrieve contract (party-wide):** Before Iris/Clio/Odysseus/Hermes produces pursuit-relevant strategy or entity claims, they **read** root `index.md`, then the **zone `INDEX.md`** for that concern, then relevant pages (or ask Hephaestus grep skill). **No grep wander** across the vault without a map. Chat memory is not a substitute.

### 4.1 Agent navigation scaffolding (Wandermist pattern)

**Problem:** Folders built for human memory force agents to open wrong or archived files—wasting capability on navigation, not compounding truth.

**Smallest cage (Ponytail):** Shallow maps at **major zones only**—not every subfolder, not content-type chaos (Articles/Research), not deep renumbering of the repo.

| Rule | thread-os application |
|------|------------------------|
| One concern per major zone | `entities/`, `pursuits/`, `global/`, `generated-projections/` are capture concerns; federal ontology stays |
| `INDEX.md` at zone root | Lists subfolders, **canonical** trusted files, **Where to start**, archive boundary |
| Read INDEX first | Enforced in retrieve contract (agents); same win as timed Wandermist/leopardracer fixes (~10–30s vs minutes) |
| Archive explicit | Candidates vs trusted; `generated-projections/archived/` or `trust: archived`; INDEX says “historical only unless asked” |
| Measure before reorg | >3 wrong files or >30s on a recurring task → fix **that zone’s INDEX**, not global renumbering |

**Zone INDEX template (Hephaestus seeds at bootstrap):**

- **Where to start** — one entry path per common task (e.g. agency lookup → `entities/agencies/INDEX.md` → canonical page).
- **Canonical files** — trusted paths only (Odysseus: never default-start on `trust: candidate`).
- **Archive boundary** — where stale material lives; agents skip by default.
- **Maintainer** — party agent (Iris/entities, Clio/pursuits, Hephaestus/index refresh).

**Optional Wave 1:** Lightweight `INDEX.md` per `agents/<agent>/content/` (5–10 lines, recent handoffs); Hephaestus refreshes after long-form saves per `CONTENT_DELIVERY_POLICY`.

**Anti-patterns (Wandermist):** INDEX on every tiny folder; five-level nesting; numbered prefixes repo-wide before pain; flattening vault to personal “brand/editorial” trees.

### 4.2 Vault graph view (spectral layout) — Overwatch delight, not agent retrieval

**Operator intent:** A **visual** of how the compounding brain connects—fun to use, compelling when demoing the Agent OS in production. **Agents do not navigate via this view** in production; they use zone `INDEX.md` + wikilinks + read_file.

| Phase | Scope |
|-------|--------|
| **v1** | Zone INDEX stubs + root catalog only (production navigation) |
| **v2 (Wave 1.5–2)** | Hephaestus: export wikilinks from `knowledge/thread/` → local **HTML** (or Obsidian graph) with **spectral or force layout**—cluster health, orphans, demo/screenshot-friendly |
| **v3** | Embedding/Laplacian **folder suggestions**—park with semantic search backlog |

**Delivery options (pick smallest when building):** static HTML opened from MC link or `scripts/open-vault-graph.sh`; optional MC **Knowledge** tab embed later. No dependency on cloud APIs for v2 if links-only.

**RACI:** Build/maintain export **Hephaestus**; use for lint + storytelling **Overwatch**; agents **I** only.

### Candidate → trusted workflow

1. **Intake** — triaged per table above.  
2. **Candidate write** — `generated-projections/` only; OFM frontmatter + `## Related`.  
3. **Dedup** — grep `award_key`, slug, title (Hephaestus).  
4. **Review** — Overwatch: promote / reject / edit via Obsidian (stays candidate until promote).  
5. **Promote** — “promote `<path>`” → Odysseus citation check → Hephaestus moves to write zone, `trust: trusted`, updates `index.md` + `log.md`.

**Write zones:** `entities/agencies/`, `entities/competitors/`, `global/domain_intel/`, `pursuits/<slug>/`, `relationships/`.  
**Protected:** `foundation/`, `data-elements/`, `milestones/`, `training/`, `education/`, `.obsidian/`.

### v1 layout

```
knowledge/thread/
  index.md
  log.md
  foundation/capture-llm-wiki.md
  entities/agencies/
  entities/competitors/
  global/domain_intel/
  pursuits/<slug>/
  generated-projections/
```

Defer: `data-elements/`, pgvector, MC Knowledge tab until pursuit pain.

### Hephaestus automation

| Job | v1 |
|-----|-----|
| Bootstrap | Idempotent `scripts/bootstrap_knowledge_vault.py` — seed foundation + **zone `INDEX.md` stubs** (§4.1) |
| Lint | Weekly cron → report + `log.md` append |
| Index | Rebuild root `index.md` + refresh zone INDEX canonical lines on promote |
| Promote | On Overwatch-approved path only |

---

## 5. Minimal v1 — what agents automate this month

**Goal:** You dump anything to Hermes → triage runs → you see **short confirm list** (uncertain + promote) → vault compounds.

| Step | Owner |
|------|--------|
| Foundation seed | Hephaestus |
| Triage all Overwatch dumps | **Hermes** |
| Data → candidates | Iris (+ Hermes) |
| Packet prose → candidates | Clio |
| Citation gate on promote | Odysseus |
| Promote execution, lint, index | Hephaestus |
| Retrieve before advice | All party |

**Implementation note:** Hermes skill `knowledge-triage` or `ROUTER.md` lane—Hephaestus wires after this doc is merged.

---

## 6. Later — parked

17b-vault ingest automation, 17c semantic search, Clew→wiki, MC Knowledge API, `data-elements/` with Living Packet, closed learning loop / training exports, Postgres review records with Wave 2 opp record.

**Vault graph view (§4.2):** wikilink → spectral/force HTML for Overwatch demo and orphan lint—not agent navigation.

---

## 7. Anti-patterns

Port `vault_write.py` / knowledge UI monolith; Postgres “because capform”; Hermes memory as vault; Content tab as SSOT; auto-promote; force Obsidian; third wiki (Notion); **Overwatch manual sort** of every dump (replaced by Hermes triage B).

---

## 8. Party RACI

| Activity | R | A |
|----------|---|---|
| Intake triage | Hermes | Hermes |
| Vault candidates from data | Iris | Hermes |
| Vault candidates from capture | Clio | Hermes |
| Promote / trust gate | Odysseus | **Overwatch** |
| Bootstrap, lint, index, promote exec | Hephaestus | Hermes |
| Inspiration merge | Hermes | **Overwatch** |

---

## 9. Parked (not Wave 1)

Desktop launcher: local `start.sh` today; VPS SSH tunnel later (Hephaestus on request).

Spectral vault graph (§4.2): after INDEX scaffolding exists; Hephaestus builds; Overwatch-facing fun + demo.