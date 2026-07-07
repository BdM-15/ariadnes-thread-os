# Vault browse for Overwatch — brainstorm & recommendation

**Date:** 2026-07-02  
**Trigger:** Doc 02 is not “complete” for Overwatch until `knowledge/thread/` is **visible inside Mission Control** — single production UI/UX.  
**Status:** For direction / approval only (no build until Overwatch picks).

---

## Gap (verified today)

| Layer | State |
|-------|--------|
| **SSOT** | `knowledge/thread/` — 225+ `.md` pages, zones, INDEX chain |
| **MC backend** | `/api/vault/read?path=` and `/api/vault/candidates` **work** (local probe OK) |
| **MC UI** | **No Vault tab** — only **Content** (`agents/*/content/`) is browsable |
| **Workaround** | Obsidian on disk, or raw API — not agent-OS-native |

Overwatch cannot walk trusted wiki + morning queue in the same glass shell as tasks, agents, and party content. That blocks doc 02 **acceptance** from a product standpoint even if promote script and party artifacts shipped.

---

## Design principles (party)

| Agent | View |
|-------|------|
| **Hermes** | One UI in production: MC + Hermes chat; vault is not a second app unless we explicitly fork UX. |
| **Hephaestus** | Reuse `server.py` + `index.html` patterns (Content tab); minimal new deps; read-only v1. |
| **Clio** | Readable markdown preview, wikilink navigation, morning-queue layout for candidates. |
| **Odysseus** | **Trust badges** (candidate vs trusted); no edit in v1 without gate story. |
| **Iris** | Fast path: `global/domain_intel/`, entities, pursuits from scout handoffs. |

**Ponytail:** Add the smallest surface that makes SSOT legible. **Deliberate build:** spectral graph = v2 delight, not v1 blocker.

---

## Options (brainstorm)

### A — **Mission Control “Vault” tab (recommended v1)**

Extend MC like Content tab:

- **Left:** zone tree (`INDEX.md` → child INDEXs) + **Morning queue** (`/api/vault/candidates`)
- **Right:** markdown reader (reuse Content renderer / marked)
- **URLs:** `#vault/global/domain_intel/capabilities/eden` (mirror `#content/agent/file`)
- **API additions:** `GET /api/vault/tree` (zones + shallow listing), optional `GET /api/vault/search?q=` (ripgrep or Python walk)
- **Wikilinks:** `[[foo]]` → click resolves under `knowledge/thread/` via `/api/vault/read`

**Pros:** Single UI, APIs mostly exist, matches KomputerMechanic aesthetic, no new service.  
**Cons:** Hephaestus builds UI; search/tree need careful path sandbox (already have `_vault_safe_path`).

**Effort:** ~1 focused Hephaestus quest (MVP tree + read + candidates queue).

---

### B — **“Open in Obsidian” + MC deep links only**

Button opens `knowledge/thread` folder; MC links from board/tasks to `vault:…` paths.

**Pros:** Zero MC build; best editing UX in Obsidian.  
**Cons:** **Not** single UI — fails your production mandate.

---

### C — **Static doc site (MkDocs / mdBook / Docusaurus)**

Build step publishes `knowledge/thread` to `/vault/` on MC or GitHub Pages.

**Pros:** Mature nav, search, OSS (MkDocs, mdBook — jamstack generators list).  
**Cons:** Second rendering pipeline, stale until rebuild, heavier than Ponytail; splits “live” MC from wiki.

---

### D — **Separate markdown wiki (Otter Wiki, Gollum, Wiki.js, LeafWiki)**

| Tool | Fit |
|------|-----|
| **Otter Wiki** | Python + markdown + git; minimal; **second app** on another port |
| **Gollum** | Git-backed; Ruby stack |
| **Wiki.js** | Feature-rich; DB + AGPL — heavy for Agent OS |
| **LeafWiki** | Go single binary; engineer wiki — still parallel UI |

**Pros:** Battle-tested wiki UX, git history.  
**Cons:** Two UIs, sync/confusion with `knowledge/thread` SSOT, extra ops on Windows desktop.

**Verdict:** Good **reference** for features (dark UI, git-backed pages), poor fit for **one** Overwatch shell unless we demote MC to ops-only (not desired).

---

### E — **Hermes-only retrieval (“ask the guildmaster”)**

Vault always via chat + `VAULT_RETRIEVE.md`.

**Pros:** Already works for agents.  
**Cons:** Overwatch cannot **browse** structure, compare pages, or morning-queue scan without asking — wrong for compounding truth review.

---

### F — **Hybrid (recommended roadmap)**

1. **v1 (doc 02 completion):** **Option A** — MC Vault tab, read-only, candidates queue, zone INDEX navigation.  
2. **v1.1:** Full-text search in MC; board task → vault deep link (partially started in tasks UI).  
3. **v2+:** Spectral vault graph (delight); optional Obsidian sync for power editing.

---

## Open-source patterns worth stealing (not necessarily deploying)

- **Otter Wiki / Gollum:** markdown-on-disk + git — we already have disk SSOT; steal **page list + git history** ideas later, not the server.  
- **MkDocs / mdBook:** INDEX hierarchy — mirror with zone `INDEX.md` chain in MC tree.  
- **Raneto / flat-file wikis:** no DB — aligns with our vault model.

---

## Doc 02 gate redefinition (proposal)

Close doc 02 **engineering** when promote script + party artifacts done (**current**).  
Close doc 02 **Overwatch acceptance** when **Option A MVP** is live in MC (or Overwatch explicitly accepts Obsidian-only interim).

---

## Decision requested

Pick one:

1. **Approve A (MC Vault tab MVP)** — Hephaestus quest, Hermes coordinates acceptance test with you.  
2. **Approve F** — A now, graph later (default recommendation).  
3. **Interim B** — Obsidian-only until VPS (document as explicit debt).  
4. **Pilot D** — e.g. Otter Wiki on side port (only if you want dual UI).

Reply with **1 / 2 / 3 / 4** or constraints (read-only only, search required day one, edit in MC later, etc.).

---

*Research:* Otter Wiki, Wiki.js, MkDocs, mdBook, Gollum, LeafWiki, awesome-selfhosted wikis tag (2026-07-02 pass).