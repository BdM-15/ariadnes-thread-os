# Knowledge vault and compounding truth

Wave 1 inspiration doc **02** · Capform anchors: `docs/PLAN.md` (two-store doctrine), `docs/reference/vault/capture-llm-wiki.md`, `backend/src/thread/api/knowledge_routes.py`, `services/vault_write.py` (zones only—do not port), `bootstrap/vault.py` + `vault_seed.py`, `docs/BACKLOG.md` § Knowledge / vault.

---

## 1. Operator job (one sentence)

Give Overwatch one **compounding knowledge base**—trusted, linked synthesis that improves each pursuit—while agents ingest, lint, and maintain the catalog; Overwatch **ratifies** promotions (and may edit in Obsidian when they want a graph IDE).

---

## 2. Why capform built it (scaffold honesty)

Capform encodes **two-store knowledge that compounds** (PLAN non-negotiable #5): **PostgreSQL** holds execution truth (intel slices, workflow, `review_records`); **`knowledge/thread/`** holds Layer 2 synthesis (entity narratives, pursuits, domain intel). A third contract file, `foundation/capture-llm-wiki.md`, defines how agents maintain the wiki (Karpathy LLM-wiki + Obsidian optional).

**Three layers in capform** (`vault_seed.py` / `capture-llm-wiki.md`):

| Layer | Location | Who writes | Rule |
|-------|----------|------------|------|
| **1 Raw** | PG `intel_*`, `docs/reference/`, MCP/MinerU output | Ingest, humans | Immutable—LLM reads, never edits |
| **2 Wiki** | `knowledge/thread/` | LLM + human after review | Append on trusted pages; candidates in `generated-projections/` |
| **3 Schema** | `foundation/capture-llm-wiki.md` | Platform seed + rare human bumps | `schema_version` on platform updates |

**What actually shipped in capform:**

| Capability | State |
|------------|--------|
| Idempotent vault bootstrap (`bootstrap/vault.py` → `ensure_vault_seed`) | ✅ Never overwrites existing wiki pages |
| `/knowledge` HTMX browser + API `/knowledge/vault/*` (list, page, candidate POST, lint, normalize, repair) | ✅ Read path thin (`knowledge.py`); writes in services |
| `WRITE_ZONES` + `PROTECTED_PREFIXES` + candidate → review → promote | ✅ Logic lives in ~1k LOC `vault_write.py` (monolith—reference only) |
| Capture / idea paths → `write_candidate_note` → optional `queue_vault_candidate_review` (PG) | ✅ |
| Auto index + `log.md` on every ingest | 🟡 Partial; **17b-vault** in backlog |
| Clew trusted → wiki ingest, pgvector semantic search | 📋 Parked (17b, 17c, BACKLOG) |

Capform solved **structure + review gate + API**, not “zero operator maintenance.” Maintenance is intended as **agent + skills** (`vault_maintainer`, `obsidian-markdown`), with Obsidian as optional desktop IDE (`OBSIDIAN_DESKTOP.md`).

---

## 3. True intent (decision enabled)

**Intent:** After each intel pass, fill pass, or pursuit decision, durable **synthesis** (who the customer is, what we learned, what we believe) lives in one place—**wikilinked**, **cited**, **reused** on the next opportunity—without re-deriving the same agency story from chat.

**Decisions enabled:**

- “Do we already trust this narrative?” → vault pages with `trust: trusted`, not Hermes session memory.
- “What did we learn on the last pursuit?” → `pursuits/<slug>/` + greppable `log.md`.
- “Is this duplicate intel?” → dedup on stable keys (`award_key`, `review_id`, title slug) before append.
- “What needs me this morning?” → **candidate** queue under `generated-projections/` (and/or a Hermes summary)—nothing silent-promotes to trusted.

**Compounding loop (doctrine):** use vault on pursuit A → trusted pages inform fill on pursuit B → better fills → richer candidates → Overwatch ratifies → vault grows. Hermes profile memory is **scratch prefs**, not this loop.

---

## 4. Mission Control / agent fit

### Two text layers in thread-os (no third brain)

Per `01-PROGRAM-PRINCIPLES.md`:

| Layer | Role | Location |
|-------|------|----------|
| **Work staging** | Handoffs, loop drafts, session output | `agents/<agent>/content/*.md` → MC **Content** tab |
| **Compounding SSOT** | Candidate + trusted wiki | **`knowledge/thread/`** (canonical root—see below) |
| **Hermes memory** | Compact conventions | Not the knowledge base |

**Content tab ≠ vault.** Staging is disposable handoff prose; vault is ratified truth. Agents may **propose** candidates from staging; they must not treat Content files as trusted SSOT.

### Canonical vault root (thread-os)

```
<repo-root>/knowledge/thread/
```

**Rationale:** Matches capform path, `capture-llm-wiki.md` folder map, and future optional parity with `/knowledge/vault/*` patterns. Obsidian opens this folder as the vault root. MC **Content** stays separate; no new MC tab in Wave 1 (Ponytail)—optional Knowledge surface is Wave 2–3 after a real pursuit tests the flow.

**Git posture:** Track **structure seeds** (`foundation/capture-llm-wiki.md`, empty `index.md` / `log.md` stubs, `.gitignore` rules for operator-grown trees). Operator pages under `entities/`, `pursuits/`, `generated-projections/` follow capform habit: **local compounding truth**, not bulk-shipped in `main`. Hephaestus documents `.gitignore` when implementing bootstrap—not a Wave 1 code commitment in this doc.

### Adapted layers (thread-os Wave 1—no Postgres)

| Layer | thread-os v1 | Who writes |
|-------|----------------|------------|
| **1 Raw** | Iris exports in `agents/iris/content/`, URLs/files in candidate `citations` | Iris; read-only for vault writers |
| **2 Wiki** | `knowledge/thread/` Karpathy layout | Agents write **candidates**; trusted only after Overwatch promote |
| **3 Schema** | `knowledge/thread/foundation/capture-llm-wiki.md` | Idempotent seed from capform reference (slimmed) |

**Without capform Postgres:** capform ties promote to `ReviewRecord` in PG. thread-os **defers PG** until Wave 2 opportunity record. **v1 review artifact:** YAML frontmatter `trust`, `reviewed_by`, `reviewed_at`, `review_id` (UUID) + append-only `knowledge/thread/log.md` (and optional `inbox/review-log.md`). Enough for solo Overwatch ratification without a second database.

### Candidate → trusted workflow (no PG)

Mirror capform **intent**, not `vault_write.py`:

1. **Intake** — chat, Content handoff, or intel skill output.
2. **Candidate write** — agent creates `knowledge/thread/generated-projections/<slug>-<YYYY-MM-DD>.md` with frontmatter: `name`, `type`, `id`, `trust: candidate`, `citations`, `source`; body + `## Related` wikilinks. Only this prefix is freely editable pre-promote (capform Capture Studio rule).
3. **Queue (logical)** — Hermes morning brief lists new candidates; no auto-promote.
4. **Review** — Overwatch approves/rejects in chat (or Obsidian edit stays candidate until promote).
5. **Promote** — on explicit Overwatch “promote `<path>`”: Odysseus checks citations present → Hephaestus moves content to a **write zone** (below), sets `trust: trusted`, appends dated section, updates `index.md` + `log.md`, removes or archives candidate file.

**Write zones (trusted targets—adapted from capform `WRITE_ZONES`):**

- `entities/agencies/`, `entities/competitors/`
- `global/domain_intel/` (and `global/domain_intel/synthesis/` for generic synthesis)
- `pursuits/<slug>/`
- `relationships/`
- `generated-projections/` — **candidates only**; not trusted landing zone

**Protected prefixes (no direct agent trusted write—seed/bootstrap only):**

- `foundation/`, `data-elements/`, `milestones/`, `training/`, `education/`, `.obsidian/`

`index.md` and `log.md` are updated via **helpers** (lint/index scripts), not hand-edited by Overwatch.

### v1 folder layout (subset—grow when pursuit forces)

```
knowledge/thread/
  index.md
  log.md
  foundation/
    capture-llm-wiki.md
  entities/agencies/
  entities/competitors/
  global/domain_intel/
  pursuits/<slug>/          # when an opp is tracked
  generated-projections/    # all pre-trusted drafts
```

**Defer until Living Packet / real opp:** full `data-elements/` (141 field pages), `milestones/`, `training/`, `skills-capabilities/`, semantic repair pipelines.

### Page format

Keep capform OFM habits: required keys `name`, `type`, `id`; `trust`; `citations`; dated append blocks (`## Added/Updated YYYY-MM-DD`); `## Related` with `[[wikilinks]]`. **Append-only** on trusted bodies—never erase prior trusted sections.

### Obsidian (optional)

Optional IDE: open `<repo>/knowledge/thread/`. Bootstrap may seed `.obsidian/` once (idempotent). Overwatch edits manually when they want graph view; agents do bulk lint/index. Not required for Agent OS operation.

### Capform API map (reference—not Wave 1 port)

`knowledge_routes.py` exposes read/list/page, `POST /candidate`, `GET /lint`, `POST /normalize|repair|semantic-link`. thread-os may add a **thin** stdlib read/list in `server.py` later; **do not** port FastAPI router + PG review queue as a bundle.

### Hephaestus automation (lint, index, bootstrap)

| Job | Mechanism (v1) |
|-----|----------------|
| **Bootstrap** | Idempotent `scripts/bootstrap_knowledge_vault.py` (mkdirs + seed `foundation/capture-llm-wiki.md`, stubs—pattern from `vault_seed.py`, not copy-paste) |
| **Lint** | Weekly Hermes cron → skill-guided pass: missing frontmatter keys, broken wikilinks, orphans, candidates older than N days → report in `agents/hephaestus/content/` + append `log.md` |
| **Index** | Rebuild `## Pages` section in `index.md` from trusted `.md` paths (small script or skill—**not** full `vault_lint.py` port) |
| **Dedup** | Before candidate write: grep `award_key` / slug / title in `knowledge/thread/` |
| **Promote execution** | Hephaestus on Overwatch-approved path only; Odysseus gate on citations |

Overwatch does **not** run lint, bootstrap, or index maintenance by hand (`01-PROGRAM-PRINCIPLES.md`).

---

## 5. Minimal v1 — what agents automate this month

**Goal:** Overwatch dumps ideas in chat or staging → reviews a **short candidate list** → approve/reject → vault compounds without Overwatch running scripts.

| Step | Owner | Mechanism |
|------|--------|-----------|
| Seed vault skeleton + foundation doc | Hephaestus | One-time idempotent bootstrap |
| Intel / ideas → candidate note | Iris, Clio, Hermes | `generated-projections/<slug>-<date>.md`, `trust: candidate` |
| Dedup before write | Hephaestus | Grep-based (no pgvector) |
| Weekly lint + index refresh | Hephaestus (cron) | Report + `log.md`; fix only when directed |
| Promote to trusted | **Overwatch approves** | Hephaestus: zone move + frontmatter + index/log |
| Reject | Overwatch | Delete candidate or mark rejected in log (no trusted write) |
| Post-promote link | Agents | One-line vault path in originating `agents/*/content/` handoff |

**Promote ritual (explicit):** Overwatch: “promote `generated-projections/foo-2026-07-01.md`” → Odysseus citation check → Hephaestus promote → Hermes confirms final path. No cron or LLM auto-promote.

---

## 6. Later — parked capform backlog pointers

From `docs/BACKLOG.md` § Knowledge / vault and related:

- **17b-vault** — Clew trusted → Karpathy wiki ingest; fuller auto index/log on ingest
- **17c** — `pgvector` / semantic facet search across PG + vault entities
- **16e** — completed task → vault checklist candidate (review-gated)
- **Deferred knowledge runtime** — bid/no-bid fit service, UEI crosswalk, `training/examples/` JSONL loop
- **20c-b** — bootstrap `foundation/packet-routing-matrix.md`; catalog↔wiki `field_key` sync
- **Semantic vault search** (OpenAI embeddings)—config stub in capform only
- MC **Knowledge** tab or thin `/api/knowledge/vault/*` in `server.py`
- **Closed learning loop** (`HERMES_INTEGRATION.md`) — approved outcomes → training exports
- Full **`data-elements/`** mirror of briefing packet dictionary (with Living Packet, Wave 2)
- Splitting `vault_write.py` into write / promote / index services—only if thread-os grows past skill+script ergonomics

Revisit Postgres as execution store when **one opportunity record** and review gate doc (Wave 2) require it—not “because capform had it.”

---

## 7. Anti-patterns — what not to port

| Anti-pattern | Why |
|--------------|-----|
| Port **`vault_write.py`** (~998 LOC) or **`ui/routes.py`** knowledge monolith wholesale | Violates Ponytail and explicit guidance; use agents + thin scripts + skills |
| Add **Postgres** before opportunity record / real pursuit pain | Two-store without workflow = dead weight in thread-os |
| Use **Hermes MEMORY.md** as vault | Not review-gated, not wikilinked SSOT, not compounding corpus |
| Treat **Content tab** files as trusted | Staging only; pollutes graph and trust model |
| **Auto-promote** from cron or LLM | Breaks intake → candidate → trusted doctrine |
| Ship vault browser + semantic search in Wave 1 | Inspiration only; implement when daily workflow fails without it |
| Third wiki (Notion, separate repo, duplicate DOX tree) | Two-layer text rule |
| Direct trusted writes to **`PROTECTED_PREFIXES`** | Bypasses schema seed and packet dictionary discipline |
| Recommend **porting** `vault_write.py` “for speed” | Creates unmaintained second monolith; copy zones + workflow only |

---

## 8. Party RACI

| Activity | R | A | C | I |
|----------|---|---|---|---|
| Vault schema / foundation seed | Hephaestus | Hermes | Odysseus | Overwatch |
| Candidate writes from intel | Iris | Hermes | Clio | Odysseus |
| Candidate writes from packet / capture prose | Clio | Hermes | Odysseus | Iris |
| Promote gate / citation quality | Odysseus | **Overwatch** | Hermes | Hephaestus |
| Lint, index, bootstrap, inbox hygiene | Hephaestus | Hermes | — | Overwatch |
| Inspiration doc merge + index consistency | Hermes | **Overwatch** | Hephaestus | Party |
| Obsidian optional setup | Overwatch | Overwatch | Hephaestus | — |

---

*Wave 1 doc 02 · Primary owner: Hephaestus · Merge gate: Overwatch on `docs/capform-inspiration`.*