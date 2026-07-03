# Vault index vs Karpathy LLM-wiki vs codebase — party brainstorm

**Date:** 2026-07-03  
**Overwatch ask:** Are we mixing two ideas? Should `index.md` be a folder tree for the **repo**, while Karpathy runs the **knowledge vault**? Can we convert the second brain later and plug it into other apps?  
**Hermes:** Brainstorm only — **no vault/git work** until Overwatch says resume.

---

## Checkpoint — where we paused (do not lose)

| Item | State |
|------|--------|
| Branch | `feature/knowledge-vault-v1` @ `5608eb3` (hygiene tail) / `2e99f61` (main hygiene) / `07f2247` (cleanse) |
| Promote freeze | **ON** — candidates only unless you say promote one |
| W2 | Top-5 capability **candidates** in `knowledge/generated-projections/*-rewrite-candidate.md` |
| Pre-W2 | `knowledge/index.md` + wikilinks → `[[ariadne-vault-schema]]`; entities 3b live |
| Next queued (frozen) | push · review candidates · promote one · W2 batch 6–10 |

---

## Short answer (Hermes)

**You are on the right track.** Karpathy’s method **is** what we use **inside `knowledge/`**. Root `knowledge/index.md` is **not** meant to be the Agent OS repo folder tree — and that separation is intentional.

**Do not** turn `knowledge/index.md` into a map of `agents/`, `scripts/`, and `mission-control/`. That belongs to **project rules** (`AGENTS.md`, `REGISTRY.yaml`, `ROUTER.md`, skills). **Do** keep `knowledge/index.md` as the **wiki catalog** (Karpathy) plus **zone `INDEX.md`** files as shallow navigation maps (Wandermist / inspiration doc 02).

**Converting later:** The vault is already a portable Karpathy-shaped wiki (markdown + wikilinks + YAML + `log.md`). “Convert” later means **export, sync, or API-wrap** the same files — not a second rewrite.

---

## Two distinct things (party consensus)

| | **Agent OS codebase** | **Knowledge vault (second brain)** |
|---|------------------------|-------------------------------------|
| **What it is** | Hermes party, MC, scripts, skills, capture loop | Compounding **trusted truth** for capture decisions |
| **Primary location** | Repo root, `agents/`, `scripts/`, `docs/` | `knowledge/` only |
| **How agents navigate** | `AGENTS.md`, `REGISTRY.yaml`, `ROUTER.md`, `FILE_MUTATION.md`, grep with discipline | **Retrieve contract:** `knowledge/index.md` → zone `INDEX.md` → pages + wikilinks |
| **“Index” role** | No single Karpathy `index.md` required; optional future `docs/CODEMAP.md` if pain | **Karpathy `index.md`** = content catalog; **`log.md`** = append-only timeline |
| **Schema / contract** | N/A | `foundation/ariadne-vault-schema.md` (Layer 3) — was named `capture-llm-wiki.md` |
| **Human IDE** | VS Code / Hermes desktop | Obsidian **optional** on `knowledge/` |
| **Trust** | Git + review gates on code | `trust: candidate` → Overwatch promote → `trusted` |

**Mixing happens when one file tries to do both jobs.** Our post-flatten design keeps them apart: schema doc describes vault topology; `knowledge/index.md` points at zones, not at `scripts/board_add_task.py`.

---

## What Karpathy LLM-wiki actually means (not just a filename)

From the [gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and our ratified inspiration doc:

1. **Wiki `.md` files = the program** agents maintain (ingest, query, lint).
2. **`index.md`** = catalog of **wiki content** (what exists, where to start) — updated when trusted material changes.
3. **`log.md`** = greppable history of ingest/lint/promote.
4. **Obsidian** = optional desktop “IDE” for humans; agents can use `read_file` + wikilinks without Obsidian running.
5. **Agents = programmers** of the wiki; raw sources stay read-only (Layer 1).

That is **exactly** `ariadne-vault-schema.md` §1–2 and `docs/inspiration/knowledge-vault-and-compounding-truth.md` §4. We are **not** off-pattern; we renamed Layer 3 from `capture-llm-wiki` → **`ariadne-vault-schema`** so “wiki method” is not confused with “schema file named llm-wiki.”

---

## Party takes

### Hermes (orchestrator)

- **Confirm:** `knowledge/index.md` = Karpathy catalog; repo navigation = shared protocols, not vault index.
- **Risk:** Overwatch or an agent reads `index.md` expecting a full file tree of `knowledge/` — fix with **one paragraph** at top of `index.md` (“This is the wiki catalog, not the repo map”) when we resume — not a re-architecture.
- **Future apps:** Treat `knowledge/` as an **embeddable module**: same tree can back MC Vault tab, Obsidian, a future Postgres sync, or a mobile reader via stable slugs + frontmatter.

### Hephaestus (platform)

- **Current approach is correct.** Zone `INDEX.md` stubs + root catalog = Wandermist “smallest cage” (inspiration §4.1).
- **Codebase tree for agents:** If retrieve pain appears on **repo** work, add **`docs/agent-codebase-map.md`** (or extend `AGENTS.md`) — **never** overload `knowledge/index.md`.
- **Automation:** On promote, refresh root catalog + zone canonical lines (`vault_lint`, promote script) — Karpathy “index maintenance” without hand-editing 200 paths.
- **Portability:** Zip `knowledge/` + `.obsidian/` → open anywhere; or `rsync` to another host. Optional v2: static HTML graph (inspiration §4.2) for demos — agents still use INDEX + wikilinks.

### Clio (reader / narrative)

- **Second brain UX** = follow wikilinks from a **small number of entry pages** (`index.md`, `entities/INDEX`, company hub). A flat folder tree in one file does not help humans or LLMs find “what we believe about LOGCAP.”
- **Karpathy wins** on **compounding pages** (capability, customer, pursuit), not on listing every subdirectory.
- Templates and Shipley waves stay in **write zones**; catalog only **points** to them.

### Odysseus (gates / contract)

- **Retrieve contract is the law:** `VAULT_RETRIEVE.md` — index → zone INDEX → trusted pages. Breaking that to stuff repo paths into `knowledge/index.md` would **increase** hallucination risk (agents think vault paths are code).
- **Schema file ≠ wiki:** `ariadne-vault-schema` is Layer 3 rules; pages in `global/` and `entities/` are Layer 2 truth. Alias `[[capture-llm-wiki]]` → schema is fine for one release; don’t resurrect “llm-wiki” as a second root index.
- **Promote freeze unchanged** by this brainstorm.

### Iris (sources)

- Iris doesn’t maintain `index.md` by hand; she produces **cited** exports and rescout memos in `agents/iris/content/`. Vault pages get **URLs in frontmatter**, not a mirror of SAM folder structure.
- **Separation helps:** intel staging in agent content vs SSOT in `knowledge/` after promote.

---

## Are we mixing them today? Honest scorecard

| Question | Verdict |
|----------|---------|
| Is `knowledge/index.md` acting as repo codebase map? | **No** — it lists vault layers/zones (correct). |
| Is Karpathy applied to the vault? | **Yes** — md corpus, index, log, agent-maintained, Obsidian-optional. |
| Was naming confusing? | **Somewhat** — `capture-llm-wiki` sounded like “the whole wiki” but was Layer 3 schema; **mitigated** by `ariadne-vault-schema` + wikilink pass. |
| Do we need a rethink before W2 promote? | **No** — optional clarity blurb in `index.md` only. |
| Do we lose Obsidian/Karpathy robustness? | **No** — OFM frontmatter, wikilinks, zone INDEXes, `.obsidian/` seed align with kepano/Obsidian skills path in schema. |

---

## “Convert to Karpathy wiki later” — what that really means

You are **already building** a Karpathy-style wiki. Later options (no rush):

| Option | Effort | Notes |
|--------|--------|-------|
| **Obsidian vault** | Low | Point Obsidian at `knowledge/` (already supported in schema reference). |
| **Standalone repo** | Low | Subtree split: `knowledge/` + schema + lint script → own git remote. |
| **Another app (Notion, custom UI)** | Medium | Importers read markdown + frontmatter; trust field maps to “verified” badge. |
| **API / MCP “vault_read”** | Medium | Thin layer over files; content unchanged. |
| **Full re-ingest from gist template** | High / unnecessary | Only if we abandoned zones — **not recommended**. |

**Connect to future apps:** Stable **`id`**, **`type`**, **`trust`**, **`citations`**, slug paths under `entities/` and `global/` are your **integration contract**. Apps come and go; the markdown tree remains SSOT.

---

## Recommendations (when you resume work)

1. **Stay the course** — no split into “two index systems” beyond what we have (root catalog + zone INDEX + schema).
2. **Optional micro-edit** (Overwatch OK): 3–5 lines at top of `knowledge/index.md` stating catalog vs repo navigation explicitly.
3. **If repo navigation pain:** new doc under `docs/` or `agents/_shared/`, not vault index.
4. **Continue** frozen queue: push → review W2 candidates → promote → batch 6–10.

---

## Overwatch — one-line ratification (optional)

Copy if this matches your intent:

```text
Ratified: knowledge/index.md = Karpathy wiki catalog only; repo navigation stays AGENTS/REGISTRY/ROUTER. Vault is already portable markdown SSOT. Resume vault work from checkpoint (no architecture change).
```

---

## Links

- Schema: `knowledge/foundation/ariadne-vault-schema.md`
- Inspiration: `docs/inspiration/knowledge-vault-and-compounding-truth.md` (§4 retrieve + §4.1 Wandermist)
- Retrieve: `agents/_shared/VAULT_RETRIEVE.md`
- Prior rebuild: `agents/hermes/content/2026-07-02_vault-item4-hybrid-rebuild-brainstorm.md`