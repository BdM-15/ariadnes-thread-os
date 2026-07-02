# Knowledge vault and compounding truth (Wave 1 · doc 02 — DRAFT for Overwatch review)

**Status:** Review draft only — **not** merged to `docs/inspiration/` until Overwatch approves.  
**Branch target:** `docs/capform-inspiration`  
**Sources read:** capform `docs/PLAN.md` (two-store doctrine), `docs/reference/vault/capture-llm-wiki.md`, `OBSIDIAN_DESKTOP.md`, `backend/src/thread/api/knowledge_routes.py`, `services/vault_write.py` (zones/gate), `docs/BACKLOG.md` (knowledge lane).

---

## 1. Operator job (one sentence)

Give Overwatch one **compounding knowledge base**—trusted prose that gets smarter each pursuit—while agents do ingest, lint, and indexing; Overwatch only **ratifies** promotions and edits in Obsidian when they want to.

---

## 2. Why capform built it (scaffold honesty)

Capform treats knowledge as **Layer 2 synthesis** in a three-layer model: immutable raw intel in PostgreSQL (Layer 1), Karpathy-style LLM wiki in `knowledge/thread/` (Layer 2), schema contract in `foundation/capture-llm-wiki.md` (Layer 3). PLAN non-negotiable **#5**: *two-store knowledge that compounds*—vault holds narrative + entity graph; Postgres holds execution truth (packet fields, review records, intel slices).

**What shipped in capform (honest):**

| Capability | State |
|------------|--------|
| Vault seed + `/knowledge` HTMX browser | ✅ |
| API `/knowledge/vault/*` list, page, candidate write, lint, repair | ✅ |
| `vault_write.py` (~1k LOC) zones, promote, review queue hooks | ✅ (heavy) |
| Capture studio + idea dump → vault candidate + review | ✅ |
| Auto index/log on every ingest | 🟡 partial (17b backlog) |
| pgvector semantic vault search | 📋 parked (17c) |
| Clew → vault trusted ingest | 📋 parked |

Capform **did not** solve “zero operator maintenance”—it solved **structure + gate + API**. Maintenance is meant to be **agent + skills** (`vault_maintainer`, `obsidian-markdown`), with Obsidian as optional IDE.

---

## 3. True intent (decision enabled)

**Intent:** After each intel pass, fill pass, or pursuit decision, durable **synthesis** (who the customer is, what we learned, what we believe) lives in one place, **linked**, **cited**, and **reused** on the next opportunity—without re-asking Grok for the same agency story.

**Decisions enabled:**

- “Do we already trust this entity narrative?” → read vault `trust: trusted` pages, not agent chat memory.
- “What did we learn on the last KBR-style pursuit?” → `pursuits/<slug>/` + `log.md` timeline.
- “Is this new intel duplicate?” → dedup on `award_key` / `review_id` before append.
- “What’s ready for me this morning?” → **candidate** queue (inbox), not silent promotion.

**Differentiator (keep from capform):** Every borrowed pattern (research, Clew, packet fill) must land as **candidate + provenance** and promote only via **review**—then compound into vault. Not auto-trusted.

---

## 4. Mission Control / Agent OS fit

### Two text layers in thread-os (no third brain)

| Layer | Role | Location (recommended) |
|-------|------|-------------------------|
| **Work staging** | Handoffs, loop drafts, session output | `agents/<agent>/content/*.md` → MC **Content** tab (unchanged) |
| **Compounding SSOT** | Trusted + candidate wiki | **`vault/`** at project root (see below) |
| **Hermes profile memory** | Prefs, conventions | Not the knowledge base |

**Content tab ≠ vault.** Content is “what the party just wrote”; vault is “what we believe after ratification.” Agents **propose** vault candidates from staging; they do not treat Content files as trusted SSOT.

### Mission Control (minimal v1 — no new tab yet)

- **Today:** No vault UI on MC (Ponytail). Overwatch uses Obsidian and/or file paths; agents report inbox path in chat.
- **Wave 1 inspiration only:** Document paths, conventions, promote ritual.
- **Later (Wave 2–3):** Optional MC **Knowledge** tab or Content tab “Promote to vault candidate” action—only after this doc is approved and one real opp tests the flow.

### Canonical vault root (recommendation)

```
C:/Users/benma/ariadnes-thread-os/vault/
```

**Why not `knowledge/thread/`?** Parity with capform is nice, but `vault/` is clearer in a repo that is **not** a Postgres monolith. Obsidian opens **`vault/`** as the folder. Capform’s schema doc can be seeded as `vault/foundation/capture-llm-wiki.md` (slimmed for thread-os).

**Git:** Track `vault/foundation/` + empty structure seeds; **gitignore** operator pages under `vault/entities/`, `vault/pursuits/`, `vault/generated-projections/` (same posture as capform: local compounding truth, not shipped in repo). Hephaestus documents `.gitignore` rules in implementation phase—not in this inspiration merge unless Overwatch wants tracked seed-only vault.

### Adapted three layers (thread-os, no Postgres in Wave 1)

| Layer | thread-os v1 | Who writes |
|-------|----------------|------------|
| **1 Raw** | `vault/raw/` or Iris exports in `agents/iris/content/` + URLs in citations | Iris ingest; **read-only** for vault writers |
| **2 Wiki** | `vault/` Karpathy layout (below) | Agents after candidate; trusted after Overwatch promote |
| **3 Schema** | `vault/foundation/capture-llm-wiki.md` | Seed from capform reference; version bumps rare |

**PostgreSQL:** Capform couples review records to PG. thread-os **defers** PG until Wave 2 opportunity record. **v1 promote record:** frontmatter `trust`, `reviewed_by`, `reviewed_at` + optional `vault/inbox/review-log.md` append—enough for solo Overwatch without a second database.

### Folder layout (v1 subset — grow only when needed)

```
vault/
  index.md
  log.md
  foundation/
    capture-llm-wiki.md      # Layer 3 contract (seed)
  inbox/
    candidates/              # New writes land here (trust: candidate)
  entities/
    agencies/
    competitors/
  global/
    domain_intel/
  pursuits/<slug>/           # Created when an opp is “tracked”
  generated-projections/     # LLM drafts pre-inbox (optional)
```

**Defer until pursuit forces:** `data-elements/` (141 field pages), `milestones/`, `training/`, full `relationships/` graph—capform weight, not Wave 1.

### Page format (carry forward)

Keep capform OFM frontmatter: `name`, `type`, `id`, `trust`, `citations`, `tags`, `aliases`, dated append sections (`## Added/Updated YYYY-MM-DD`), `## Related` wikilinks. **Append-only** on trusted bodies.

### Obsidian

**Optional IDE**—open folder `vault/`. Not required for Agent OS. Overwatch edits manually; agents do bulk lint/index. Reference: capform `docs/reference/vault/OBSIDIAN_DESKTOP.md`.

---

## 5. Minimal v1 — what agents automate this month

**Goal:** Overwatch life = dump ideas in chat or staging → review **short candidate list** → say approve/reject → vault compounds without running scripts.

| Step | Owner | Mechanism |
|------|--------|-----------|
| Seed vault skeleton + foundation doc | Hephaestus | One-time script or copy; idempotent |
| Idea / intel → candidate note | Iris, Clio, Hermes | Write `vault/inbox/candidates/<slug>.md` with `trust: candidate` + citations |
| Dedup check before write | Hephaestus skill | Grep `award_key` / title in `vault/` (no pgvector yet) |
| Weekly lint + index refresh | Hephaestus cron | Skill-guided: orphans, missing Related, stale `last_updated` → append `log.md` |
| Promote to trusted | **Overwatch approves** | Hephaestus moves file to proper zone OR flips `trust: trusted` + moves out of inbox |
| Reject | Overwatch | Delete or `trust: rejected` in `generated-projections/` |
| Staging cleanup | Agents | After promote, link from `agents/*/content/` handoff to vault path (one line) |

**Overwatch does not:** run `sync_party_profiles`, lint, normalize, backup MC, or edit index.md by hand.

**Promote ritual (v1, explicit):** Overwatch replies “promote `<path>`” in Hermes → Odysseus checks citations present → Hephaestus executes promote → Hermes confirms path. No silent promote.

---

## 6. Later — parked capform backlog pointers

- **17b-vault** full auto index/log on ingest  
- **17c** pgvector / semantic vault search  
- **16e** completed task → vault checklist candidate  
- **17b-vault** Clew trusted → wiki ingest  
- MC Knowledge tab / vault browser API in `server.py`  
- Closed learning loop → `training/examples/` (BACKLOG)  
- Full `data-elements/` mirror of briefing packet dictionary (Wave 2+ with Living Packet)

---

## 7. Anti-patterns — what not to port

| Anti-pattern | Why |
|--------------|-----|
| Port `vault_write.py` or 3k-line `ui/routes.py` wholesale | Violates Ponytail; thread-os uses agents + thin Python later |
| Add Postgres “because capform had it” before opportunity record | Two stores without workflow = dead weight |
| Use Hermes **memory** as vault | Not searchable, not review-gated, not compounding |
| Treat **Content tab** files as trusted SSOT | Staging only; pollutes graph |
| Auto-promote candidates from cron or LLM | Breaks doctrine; Overwatch ratifies |
| Ship vault UI + semantic search in Wave 1 | Inspiration doc only; implement when opp hurts |
| Third wiki (Notion, separate repo) | Two-layer text rule |

---

## 8. Party RACI

| Activity | R | A | C | I |
|----------|---|---|---|---|
| Vault schema / foundation seed | Hephaestus | Hermes | Odysseus | Overwatch |
| Candidate writes from intel | Iris | Hermes | Clio | Odysseus |
| Candidate writes from packet prose | Clio | Hermes | Odysseus | Iris |
| Promote gate / citation quality | Odysseus | **Overwatch** | Hermes | Hephaestus |
| Lint, index, inbox hygiene | Hephaestus | Hermes | — | Overwatch |
| Index doc + merge to `docs/inspiration/` | Hermes | **Overwatch** | Hephaestus | Party |
| Obsidian optional setup | Overwatch | Overwatch | Hephaestus | — |

---

## 9. Efficiency choices for Overwatch (explicit)

1. **Single promote inbox** — `vault/inbox/candidates/`; morning review is one folder (or one Hermes summary), not scattered Content files.  
2. **No Postgres in Wave 1** — review metadata in frontmatter + log until opportunity record exists.  
3. **Agents maintain index.md/log.md** — you never hand-edit catalog lines.  
4. **Obsidian optional** — use when you want graph view; otherwise approve via chat + path.  
5. **Slim vault tree** — no `data-elements/` until Living Packet Wave 2.  
6. **Capform as read-only recipe** — copy schema essay, not services monolith.

---

## 10. Parked related desire (not Wave 1)

**Desktop launcher for Agent OS:** Local today = `bash start.sh` / `python server.py` → `http://127.0.0.1:51763`. Future VPS = PowerShell SSH tunnel script (Overwatch snippet). Hephaestus implements when asked; separate from vault doc.

---

## Overwatch review checklist

Before merge to `docs/inspiration/knowledge-vault-and-compounding-truth.md`:

- [ ] Vault root `vault/` vs `knowledge/thread/` — preference?  
- [ ] Gitignore posture — seed-only in repo vs local-only vault?  
- [ ] v1 promote ritual (chat “promote”) — sufficient or want a markdown inbox queue file?  
- [ ] Defer `data-elements/` until Wave 2 — agree?  
- [ ] Any section too heavy / missing?

**On approve:** Hermes merges to `docs/inspiration/`, updates `00-INSPIRATION-INDEX.md` status (Wave 1 in progress), commits on `docs/capform-inspiration` — not before.