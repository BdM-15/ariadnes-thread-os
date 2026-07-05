# Morning vault brief — Karpathy foundation (2026-07-05)

**Branch:** `feature/knowledge-vault-v1` · **NOT merged to `main`** (awaiting your review)

---

## Executive summary

Overnight work **materially built** the Karpathy-style LLM wiki under `knowledge/`: cited trusted capability pages, `index.md` catalog, `log.md` audit trail, candidate → promote discipline, and an **Obsidian optional** guide. **W2–W4 are closed** on the capability manifest tail we prioritized. **W5 candidates (10) are written but not yet promoted.** The **06:00 cron brief did not run** (scheduler job list empty); this file is Hermes’s manual delivery.

---

## How the vault is foundationally built (Karpathy gist → Ariadne)

Karpathy’s idea: treat **markdown + wikilinks** as the **codebase** the “programmer” (LLM/agents) reads and edits; an **index** points into zones; **append-only log** records what changed. PolyDAO-style stacks add **Hermes as orchestrator** and **Obsidian as optional human IDE** on the same folder.

### Three layers (adapted)

| Layer | Ariadne location | Role |
|-------|------------------|------|
| **Raw / cite spine** | `citations:` + `retrieved:` on trusted pages; Iris briefs in `agents/iris/content/` | Tier-1 KBR URLs + intel staging — no invented contract IDs |
| **Wiki (content)** | `knowledge/global/`, `entities/`, `pursuits/`, `relationships/` | `[[wikilinks]]`, `trust: trusted`, append-friendly sections |
| **Schema / law** | `knowledge/foundation/ariadne-vault-schema.md`, `VAULT_RETRIEVE.md` | Zones, promote gate, packet mirrors |

### Compounding loop (effective use with Hermes)

1. **Retrieve-first** — `knowledge/index.md` → zone `INDEX.md` → trusted page (`agents/_shared/VAULT_RETRIEVE.md`).
2. **Intel** — Iris rescout → REWRITE/ARCHIVE table (no direct vault overwrite).
3. **Distill** — Clio `*-rewrite-candidate.md` in `generated-projections/`.
4. **Gate** — Odysseus cite discipline (open questions for GWAC/CMMC/clearance counts).
5. **Promote** — Hephaestus in-place trusted replace, archive candidate, `log.md` + `vault_lint`.
6. **Morning** — You read `index.md` + `log.md` tail (Karpathy “what changed”).

**Lint:** `python scripts/vault_lint.py` — green overnight (~258 md files, ~206 `trust: trusted`).

---

## Obsidian desktop (complimentary, optional)

1. Install Obsidian.
2. **Open folder as vault:** `C:\Users\benma\ariadnes-thread-os\knowledge`
3. Same files Mission Control and agents use — graph/backlinks for human review only.

Full steps: `knowledge/foundation/reference/obsidian-desktop.md` (wikilink `[[obsidian-desktop]]` from index).

You **do not** need Obsidian for capture agents; it is a convenience layer.

---

## What completed overnight

| Wave | Status | Evidence |
|------|--------|----------|
| **W2** | **Done** — 11 lighthouse capabilities | `log.md` W2 lines; e.g. `kbr-readiness-and-sustainment`, `kbr-vaault`, LOGCAP |
| **W3** | **Done** — 8 accelerators + Vaault child pages | `40e4271` batch; FedRAMP/IL5 children cited |
| **W4** | **Done** — 12 manifest-tail capabilities | `3d1324e` + `279e926`; **0** active W4 rewrite candidates |
| **W5** | **Candidates only** — 10 slugs | `ed984a1`; Iris `2026-07-05_w5-capabilities-rescout-batch.md` + Clio ship |
| **Catalog** | **Done** | `498a1ba` / cron refresh `dfbc9c6` on `knowledge/index.md` |
| **Obsidian guide** | **Done** | `3ee769c` |
| **06:00 cron brief** | **Missed** | This document |

**Overnight cron** (documented in runbook): verified W4 closed, refreshed index, pull/push attempt — see `agents/hermes/content/2026-07-05_overnight-vault-runbook.md`.

---

## What remains (not “complete” yet)

1. **W5 lighthouse promotes** — 10 candidates (cyber range, KBR Inc, cloud migration proof, sustainment discriminator, QMS, RESAN, safety-critical, Skypath, TTMT, USSF/Iron Stallion).
2. **Manifest tail** — `viaverse-estates-intelligence-platform`, `wraith` (Iris W5 brief lists as next).
3. **EDEN** — `eden-edge-computing-candidate.md` still in morning queue (meeting discovery).
4. **Original item-4 plan tail** — Shipley zone bulk, concepts, templates, full harmonize (~30+ legacy stubs may still carry `auto_generated` markers until next waves).
5. **Git** — local **ahead 1** (`ed984a1`); push when you want remote parity.
6. **Merge** — **blocked until you approve** (per your instruction).

---

## How to use it today

- **Human morning review:** open `knowledge/index.md`, then `knowledge/log.md` (last promote blocks).
- **Hermes / party:** any capture or pursuit question → retrieve trusted pages before strategy claims.
- **MC:** Content tab → `hermes/2026-07-05_morning-vault-karpathy-brief.md` (this file).

---

## Suggested your first actions

1. Skim `knowledge/index.md` wave table.
2. Optional: open Obsidian on `knowledge/` folder.
3. Say **“promote W5 batch”** or **“finish manifest tail (viaverse + wraith)”** if you want the next overnight-style wave while you review.
4. When satisfied: **approve merge** to `main` (not done automatically).

*Generated by Hermes after overnight build; replaces missed cron `vault-morning-brief-0600-cst`.*