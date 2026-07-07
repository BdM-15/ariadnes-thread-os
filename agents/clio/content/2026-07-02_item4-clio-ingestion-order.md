# Item 4 — Clio vault ingestion order & page standards

**Date:** 2026-07-02  
**Party batch:** `deleg_481f8c63` · **Parent:** [Item 4 hybrid rebuild brainstorm](http://127.0.0.1:51763/#content/hermes/2026-07-02_vault-item4-hybrid-rebuild-brainstorm.md)  
**DRI:** Clio (wave plan + prose standards) · **Gate:** Odysseus promote · **Spine cites:** Iris rescout

---

## Clio scope (this artifact)

| In scope | Out of scope |
|----------|----------------|
| Ingestion **wave order** for Shipley, KBR, templates | Odysseus KEEP/ARCHIVE manifest rows |
| **Page standards** (frontmatter, sections, voice) | Hephaestus schema file / lint automation |
| Re-author plan from **primary sources**, not copy-paste salvage | Iris URL rescout lists (parallel deliverable) |
| Candidate + trusted **templates** (snippets) | MC edit / harmonize cron (item 3 — post-rebuild) |

**SSOT path:** `knowledge/{zones}/` (flatten committed; never `knowledge/thread/` in new writes).

**Schema:** Read `foundation/capture-llm-wiki.md` until **`foundation/ariadne-vault-schema.md`** lands (Wave 3); standards below align with both.

---

## Ingestion waves (Clio execution order)

Waves run **after** manifest ratification + promote freeze (`vault:cleanse`). Clio does **not** skip waves; Iris→Clio handoff is required for KBR URL waves.

```
W0  Prerequisites (party)     Odysseus manifest signed · Iris rescout sheet · schema rename draft
W1  Company hub refresh       entities/companies/kbr-services-readiness-sustainment.md (light v2)
W2  KBR capabilities (top N) domain_intel/capabilities/ — public URL spine
W3  KBR accelerators map     domain_intel/capabilities/ + discriminators — dedupe vs W2
W4  Shipley — lifecycle core global/global_wiki/shipley/ — 1 hub + phase pages
W5  Shipley — reviews & tools shipley/ + cross-links to capture/evaluation
W6  Salvage concepts         REWRITE only rows Odysseus marked REWRITE — Clio voice pass
W7  Templates (one-at-a-time) global/global_wiki/capture/ OR foundation/reference/ — Overwatch picks
W8  Harmonize backlog        Format pass on any trusted page touched in W1–W7 without promote script
```

### Wave detail — what Clio does each step

| Wave | Input | Clio output | Promote path |
|------|--------|-------------|--------------|
| **W1** | Existing company hub + Iris RS URL | Hub v2: hub stays **short**; capability depth only via wikilinks | In-place trusted edit (post item 3) or candidate `*-hub-v2-candidate.md` until edit API |
| **W2** | Iris brief per capability URL | **New** trusted page or `generated-projections/*-candidate.md` per capability | Odysseus cite gate → `domain_intel/capabilities/<slug>.md` |
| **W3** | [Digital Accelerators](https://www.kbr.com/en/what-we-do/kbr-digital-accelerators) map | One page per accelerator **or** merge into existing capability — **no** second catalog index | Dedup `id` + `capabilities-catalog` link |
| **W4** | Shipley Capture Guide (primary) | Re-author `shipley-business-development-lifecycle.md` first, then phase pages in lifecycle order | `trust: trusted` in `global/global_wiki/shipley/` |
| **W5** | Same guide + color-team doctrine | Pink/Red/Gold/Black hat, win themes, compliance matrix, annotated outline — **chunked**, not one mega-page | Cross-link `[[milestones-overview]]`, `[[ms1-qualification]]` etc. |
| **W6** | Manifest REWRITE list | Strip capform voice; USAspending cite block per Iris; keep defined term in opening paragraph | KEEP pages get `## Added/Updated <date>` only |
| **W7** | Overwatch-named template (1) | Single template page + “how to use” section; MS gates co-reviewed with Odysseus | `foundation/reference/` if immutable shape; else `global_wiki/capture/` |
| **W8** | Lint soft failures | `agents/clio/content/YYYY-MM-DD_vault-lint-<slug>.md` notes + optional patch list for Hephaestus/Overwatch | No trust promotion |

### Recommended **first** wave after manifest (Overwatch choice)

Hermes brainstorm default: **W2 (KBR capabilities)** before **W4 (Shipley)** so bid-fit pages ground on public cites before doctrine refresh. Clio accepts either order if Overwatch picks **B-first** — do not run W4 and W2 in parallel on the same capability names (namespace collision).

### Shipley internal chunk order (W4 → W5)

1. `shipley-business-development-lifecycle.md` (hub — 7 phases summary)
2. Phase pages (existing filenames OK): opportunity identification → pursuit decision → capture planning → proposal planning → proposal development
3. Color teams: `color-team-reviews.md` hub → pink / red / gold / orange / black hat
4. Execution tools: compliance matrix, proposal schedule, storyboard, win themes, ghost strategy, executive summary rules
5. **Last:** section L/M mapping, government cover letter (proposal-specific — link from proposal development)

Each chunk: **one primary source section** → one vault page; max **2 screens** of synthesis before bullets.

### KBR capability priority (W2 starter set — Iris confirms URLs)

| Priority | Topic | Target slug | Notes |
|----------|--------|-------------|-------|
| 1 | RS BU positioning | `kbr-readiness-and-sustainment.md` | Link from company hub |
| 2 | Cleared workforce | `cleared-workforce.md` | REWRITE if TODO-only |
| 3 | Cyber / Crystalvista / range | existing slugs | Merge duplicate stubs |
| 4 | EDEN / edge | promote path from `eden-edge-computing-candidate.md` | After Jayson gate |
| 5 | GWAC / IDIQ holdings | `active-gwac-and-idiq-holdings.md` | Candidate until catalog filled |
| 6+ | Remaining ~40 capabilities | Manifest order | Batch 5 pages per sprint max |

---

## Page standards

### A. Global rules (all zones)

**Frontmatter (required keys):**

```yaml
---
name: "<Human title>"
type: <ontology type>
id: <stable-kebab-id>
trust: candidate | trusted
added: "<ISO8601>"
last_updated: <YYYY-MM-DD>
citations: "<machine-greppable provenance — see zone rules>"
tags: [<zone-relevant>]
---
```

**Body sections (trusted — append-only history):**

| Section | Required | Notes |
|---------|----------|-------|
| Title `#` | Yes | Matches `name` |
| Lead | Yes | 1–3 sentences: what this page is for **agents** |
| `## Key signals + citations` | Entity/capability/candidate | Table or bullets with cite keys |
| `## Synthesis` | Trusted intel & doctrine | Evidence-based; no invented contracts |
| `## Open questions` | Candidate & in-flight trusted | Empty section OK if none |
| `## Related` | Yes | ≥3 wikilinks to INDEX neighbors |
| `## Added/Updated <date>` | On every ingest pass | Never delete prior dated blocks |

**Voice:** Capture professional, Shipley-aligned, **no capform UI jargon**, no “the platform will…” — write for an agent reading before a customer call or Pink review.

**Dedup:** Same `id` or same capability name → merge into existing page; Clio does not create `*-v2.md` beside trusted twin.

---

### B. Shipley doctrine pages (`global/global_wiki/shipley/`)

| Field | Standard |
|-------|----------|
| `type` | `concept` |
| `trust` | `trusted` (doctrine — not candidate) |
| `citations` | `source:shipley-capture-guide • section:<chapter/phase>` |
| `tags` | include `shipley`, phase tag e.g. `capture-planning` |
| `auto_generated` | **Remove** on rewrite — set `authored_by: clio` optional |

**Body:**

- Open with **agent use line**: “Use when … (gate, outline, review type).”
- Phase pages: link **upstream** `[[shipley-business-development-lifecycle]]` and **downstream** MS pages `[[ms2-pursuit]]` etc.
- Color-team pages: table **When / Who / Outcome / Artifacts**
- No RFP-specific customer names in doctrine pages (those belong in `pursuits/<slug>/`)

**Ingestion:** Re-author from guide; treat existing 23 pages as **outline only** until W4/W5 passes Odysseus “primary source still true” check.

---

### C. KBR company hub (`entities/companies/`)

| Field | Standard |
|-------|----------|
| `type` | `company` |
| `id` | `entity-company-kbr-services-readiness-sustainment` (immutable) |
| `citations` | `https://solutions.kbr.com/readiness-and-sustainment/ • company SSOT hub` |
| `roles` | `[prime, offeror]` |

**Body:**

- **Canonical company entity** callout in first paragraph
- `## Capability catalog (trusted)` — wikilink list only, no long prose
- `## Capability discoveries (candidates)` — links to `generated-projections/`
- **Forbidden:** Duplicate capability paragraphs (depth lives in `domain_intel/capabilities/`)

---

### D. KBR capability pages (`global/domain_intel/capabilities/`)

| Field | Standard |
|-------|----------|
| `type` | `capability` |
| `trust` | `trusted` only after Odysseus promote |
| `citations` | **Required** public URL and/or `award_key:` / contract cite — no bare TODO promoted |
| `summary` | YAML one-liner ≤ 140 chars for MC/vault browse |

**Body:**

- `## Offering` — what we sell (public language)
- `## Bid fit` — RFP types / agencies / NAICS where applicable
- `## Evidence` — PP, certs, programs (cited)
- `## Gaps / TODO` — explicit; **TODO blocks promote** unless Overwatch waives
- Link **up** `[[kbr-services-readiness-sustainment]]` and **sideways** related capabilities

**Candidate path:** Use snippet in [eden-candidate-polish](http://127.0.0.1:51763/#content/clio/2026-07-02_eden-candidate-polish.md) until Iris confirms cites.

---

### E. Templates (W7 — one per Overwatch approval)

| Template kind | Home | Clio delivers |
|---------------|------|----------------|
| Call plan | `foundation/reference/call-plan-template.md` | Sections: objective, attendees, questions, outcomes, next steps |
| Risk register row | `foundation/reference/risk-register-template.md` | Shipley risk fields + cite to pursuit |
| MS1–MS4 gate slide outline | `global/global_wiki/capture/` or `odysseus/content/` until promoted | Odysseus owns gate **criteria**; Clio owns readable outline |

**Template frontmatter:**

```yaml
type: template
trust: trusted
tags: [template, shipley, ms<N>]
citations: source:overwatch-approved • template:wave7-<slug>
```

**Rule:** One template per W7 sprint; no bulk drop of capform `foundation/reference/` mirrors.

---

### F. Generated-projections candidates

Standard: [2026-07-02_eden-candidate-polish.md](http://127.0.0.1:51763/#content/clio/2026-07-02_eden-candidate-polish.md) — morning-queue block, decision table, `capability_status: unverified` when meeting-sourced.

---

## Handoffs

| To | When |
|----|------|
| **Hermes** | Wave complete → board note `vault:wave-<N>-clio-done`; morning queue for open candidates |
| **Odysseus** | Before any `trust: trusted` move from candidate |
| **Iris** | Missing URL / award cite — return REWRITE row to Iris, not filler prose |
| **Hephaestus** | INDEX canonical lists + `log.md` line format: `## [date] ingest \| <name> \| clio:wave<N>` |

---

## Acceptance (Clio item 4 done)

- [ ] This doc on disk (ingestion order + standards A–F)
- [ ] W2–W5 chunk tables agreed with Hermes (no execution until manifest)
- [ ] Shipley + KBR standards referenced in future `ariadne-vault-schema.md` § Page format (Hephaestus patch)
- [ ] EDEN candidate remains reference implementation for capability **candidate** standard

---

## Related

- [vault-edit-workflow](http://127.0.0.1:51763/#content/clio/2026-07-02_vault-edit-workflow.md) (item 3 — deferred)
- [vault-intel-taxonomy brainstorm](http://127.0.0.1:51763/#content/hermes/2026-07-02_vault-intel-taxonomy-brainstorm.md)
- [Odysseus cleanse program](http://127.0.0.1:51763/#content/odysseus/2026-07-02_vault-cleanse-program.md)
- `agents/_shared/VAULT_RETRIEVE.md`