# Vault promote gate checklist (doc 02)

**Owner:** Odysseus (citation + trust gate) · **Executor after pass:** Hephaestus (move, index, log)  
**Authority:** Overwatch ratifies promote; agents prepare and execute — no auto-promote.  
**Source:** `docs/inspiration/knowledge-vault-and-compounding-truth.md` § Candidate → trusted workflow; `knowledge/foundation/ariadne-vault-schema.md` § Page format & dedup.

---

## When this gate runs

| Trigger | Who |
|---------|-----|
| Overwatch says **promote** `<repo-relative-candidate-path>` | Hermes routes → **Odysseus** gate → **Hephaestus** on pass |
| Morning queue item: pending promote | Same chain after Overwatch confirm |

**Router:** `agents/ROUTER.md` — promote vault candidate to trusted → Hermes → Odysseus (citations) → Hephaestus (move + index).

---

## Preconditions (Overwatch — before Odysseus opens the file)

- [ ] Candidate path is under `knowledge/generated-projections/` (or explicit `trust: candidate` draft in that zone).
- [ ] Overwatch has reviewed prose in Obsidian or MC preview and **intends** trusted status (not “still editing in place”).
- [ ] Target **write zone** is named or obvious from `type` / body (see § Write zone map).

If any precondition fails → **hold**; candidate stays in `generated-projections/` until fixed.

---

## Odysseus verification (must pass before Hephaestus moves)

Run in order. Any **fail** → return to Overwatch with a one-line reason + fix list; **do not** hand off to Hephaestus.

### 1. Path and trust state

- [ ] File exists at the path Overwatch named.
- [ ] Frontmatter `trust: candidate` (or absent trust on a projections-only draft — treat as candidate).
- [ ] File is **not** already under a trusted write zone with `trust: trusted`.

### 2. Citations (grounding gate)

Per `ariadne-vault-schema.md`: every material claim needs traceable provenance; never invent award or contract data.

- [ ] YAML `citations` field is **non-empty** and lists real sources (Layer 1 pointers: `award_key:…`, `agency:…`, `source:clew_intel`, URL, MCP tool, cited doc path — not “LLM said so”).
- [ ] Body bullets that assert **facts** (dates, dollars, org names, program status) are backed by those citations or inline cite markers.
- [ ] **Meeting notes / hearsay** are labeled (e.g. `capability_status: unverified`, “heard in meeting”) — not promoted as bid truth without follow-up evidence.
- [ ] No contradictory claims vs existing **trusted** pages for the same entity (quick read of zone `INDEX.md` + grep `id` / `award_key`).

**Fail examples:** empty `citations`; “we are the incumbent” with no award_key; competitor win themes with no Iris export reference.

### 3. Trust frontmatter (promote-ready shape)

Required keys per schema (missing → fail or request Hephaestus patch before move):

| Key | Candidate | After promote (Hephaestus sets) |
|-----|-----------|--------------------------------|
| `name` | Human-readable title | Same |
| `type` | ontology type (`agency`, `capability`, `synthesis`, …) | Same |
| `id` | stable slug id | Same (dedup key) |
| `trust` | `candidate` | `trusted` |
| `added` | ISO timestamp | Preserve |
| `last_updated` | date | Bump to promote date |
| `citations` | provenance string | Preserve / extend |
| `reviewed_by` | optional pre-promote | Overwatch handle or `overwatch` |
| `reviewed_at` | optional | ISO date/time of ratification |
| `review_id` | optional UUID | Assign if absent (Wave 1 review artifact) |
| `tags` | recommended | Preserve |

- [ ] `id` is unique and stable (grep vault for duplicate `id:`).
- [ ] `type` matches intended write zone (entity vs global intel vs pursuit).
- [ ] Body includes **`## Related`** with valid wikilinks to existing or planned trusted neighbors.

### 4. Dedup (Hephaestus assists; Odysseus signs off)

Before move, confirm no duplicate **trusted** narrative for the same identity:

- [ ] Grep `knowledge/` for `id: <same-id>`, `award_key` (if present), and title/`name` collisions.
- [ ] If a trusted page already covers this entity → **merge** path (append `## Added/Updated <date>` on existing trusted page) instead of second file — Odysseus specifies merge target.
- [ ] Candidate-only duplicates in `generated-projections/` → note which file to archive after promote.

**Fail:** second trusted customer page when `entities/customers/<slug>.md` already exists with overlapping claims.

### 5. Write zone and filename (handoff spec for Hephaestus)

Odysseus records in gate reply (one block):

- [ ] **Destination path** under an allowed write zone only:
  - `entities/customers/`, `entities/companies/`
  - `global/domain_intel/` (and subfolders e.g. `capabilities/`)
  - `pursuits/<slug>/`
  - `relationships/`
- [ ] **Protected prefixes** untouched: `foundation/`, `data-elements/`, `milestones/`, `training/`, `education/`, `.obsidian/`.
- [ ] Slug/filename is kebab-case, no collision on disk.

### 6. Index update contract (Odysseus verifies plan; Hephaestus executes)

On promote, index work is **mandatory** — not optional cleanup:

- [ ] Root `knowledge/index.md` — new or updated row for the trusted page.
- [ ] Zone `INDEX.md` at destination (e.g. `global/domain_intel/INDEX.md`) — **Canonical files** line includes new path.
- [ ] Append `knowledge/log.md`: `## [YYYY-MM-DD] promote | <name> | review:<review_id> | from:<candidate-path>`.
- [ ] Remove or archive candidate source (`generated-projections/` → `archived/` or delete after copy) per Hephaestus convention.

Odysseus **pass** message must say: “Index: root + `<zone>/INDEX.md` + log line” so Hephaestus cannot skip.

---

## Gate outcomes

| Result | Next step |
|--------|-----------|
| **PASS** | Post checklist block to Hermes thread; Hephaestus moves file, flips `trust: trusted`, runs index + log, archives candidate. |
| **CONDITIONAL** | Overwatch accepts explicit “trusted with caveat” (e.g. discovery stub) — document caveat in `## Open questions` and in log line. |
| **FAIL** | Stay candidate; list failing sections; optional Hermes task for Iris/Clio to strengthen citations. |
| **REJECT** | Overwatch abandons promote; candidate archived or deleted per Overwatch. |

---

## Hephaestus execution checklist (after Odysseus PASS only)

Odysseus does **not** perform the move; verify Hephaestus completed:

- [ ] File at destination with `trust: trusted` and review fields set.
- [ ] Candidate path archived or removed.
- [ ] `index.md` + zone `INDEX.md` updated.
- [ ] `log.md` append present.

---

## Write zone map (quick reference)

| `type` (typical) | Destination |
|------------------|-------------|
| `customer_*` (agency, office, program) | `entities/customers/<slug>.md` |
| `company` | `entities/companies/<slug>.md` |
| `capability`, domain synthesis | `global/domain_intel/...` |
| `opportunity`, pursuit learning | `pursuits/<slug>/...` |
| Relationship / follow-the-money | `relationships/...` |

When in doubt, read zone `INDEX.md` **Where to start** before picking a folder.

---

## Worked example: EDEN edge computing candidate

**Candidate:** `knowledge/generated-projections/eden-edge-computing-candidate.md`  
**Proposed trusted target (per candidate body):** `global/domain_intel/capabilities/eden.md`

| Step | Assessment |
|------|------------|
| Path / trust | ✅ Under `generated-projections/`, `trust: candidate` |
| Citations | ⚠️ **Weak** — `citations` cites “Overwatch meeting note (fleeting) • POC named: Jayson Gray” only; no Layer 1 artifact |
| Grounding | ⚠️ Body correctly states **unverified**; open follow-up with Jayson Gray |
| Dedup | ✅ Grep `candidate-eden-edge-computing` / “EDEN” — no conflicting trusted capability page yet |
| Related | ✅ Wikilinks to `[[kbr-services-readiness-sustainment]]`, `[[capabilities-catalog]]` |
| Index plan | On pass: root `index.md`, `global/domain_intel/INDEX.md` (capabilities), `log.md` promote line |

**Odysseus recommendation today:** **FAIL** or **hold** until follow-up adds citations (email summary, capability one-pager, or explicit Overwatch **conditional** promote as *discovery stub* with `capability_status: unverified` retained in trusted frontmatter.

**If Overwatch conditionally promotes** after Jayson confirms scope:

1. Odysseus PASS with caveat in gate note.  
2. Hephaestus moves to `global/domain_intel/capabilities/eden.md`, sets `trust: trusted`, `reviewed_by` / `reviewed_at` / `review_id`.  
3. Update `[[capabilities-catalog]]` and `[[kbr-services-readiness-sustainment]]` trusted pages in a follow-on ingest (same promote session if edits are ready).

---

## References

- Doc 02: `docs/inspiration/knowledge-vault-and-compounding-truth.md`
- Schema: `knowledge/foundation/ariadne-vault-schema.md`
- Retrieve before advice: `agents/_shared/VAULT_RETRIEVE.md`
- Bootstrap / INDEX stubs: `scripts/bootstrap_knowledge_vault.py`