# Vault intel taxonomy — party brainstorm (post v1 bootstrap)

**Date:** 2026-07-02 · **Status:** Discussion draft — **no reorg executed**  
**Context:** Vault v1 live at `knowledge/thread/` (222 md files seeded). Overwatch asked how to avoid confusion as we add competitor, opportunity, customer, company, and general research intel.

---

## North star (all agents)

**One compounding brain, multiple concerns** — not five separate vaults. Use **zones + trust + pursuit slug**, not content-type folders (Articles/Research).

| Your label | Primary zone (v1) | Secondary / staging |
|------------|-------------------|---------------------|
| **Competitor intel** | `entities/competitors/<name>.md` | `generated-projections/` until promote |
| **Customer / agency intel** | `entities/agencies/<name>.md` | Iris exports in `agents/iris/content/` first |
| **Opportunity intel** | `pursuits/<slug>/` (README + dated notes) | SAM/USAspending raw stays out of vault |
| **My company intel** | `global/domain_intel/` (capabilities, UEI, PP) | Not mixed into competitor pages |
| **General research** | `global/global_wiki/` (doctrine) OR `global/domain_intel/` if bid-fit | Web dumps → Hermes triage |

---

## Hermes — routing & triage

- **Every dump** → classify: vault candidate / task / capture / discard / uncertain queue (preference B).
- **Competitor vs customer:** named org → `entities/`; if both roles, one canonical page + `## Roles` section, not two trees.
- **Opportunity-specific** → must include `pursuit_slug` in frontmatter or path under `pursuits/<slug>/`; never orphan “opp intel” in global root.
- **Do not** create parallel top-level folders (`01-Competitors/`) until diagnostic proves INDEX failure.

---

## Iris — scout / ingest

- **Competitor:** awards, NAICS, teaming signals → candidate page `entities/competitors/` with `award_key` / URL citations.
- **Customer/agency:** SAM notices, org hierarchy, funding office → `entities/agencies/`.
- **General research:** market scans that are **not** company-specific → `global/global_wiki/` subfolder (existing `capture/`, `evaluation/`).
- **Company (us):** capability gaps, contract history fit → `global/domain_intel/capabilities/`, `uei/` — not competitor folder.
- Raw JSON/CSV stays **outside** vault; wiki holds synthesis only.

---

## Clio — packet & narrative

- Opportunity intel that feeds **Living Packet** → `pursuits/<slug>/` notes + link to entities; packet field values stay future Wave 2 (`data-elements/` parked).
- Win themes / discriminators: pull from `global/global_wiki/capture/` + pursuit folder; cite sources.
- After MS gate work, **promote** reusable lessons to `global/global_wiki/lessons_learned/` (when that subtree exists) — not buried in one pursuit.

---

## Odysseus — trust & gates

- **Promote gate:** competitor claims need award or primary source; agency claims need SAM/FBO/official cite; company PP claims need UEI-level evidence.
- **Bid/no-bid** reads `domain_intel` + entities + pursuit — never `generated-projections` as default.
- Shipley artifacts in `agents/odysseus/content/` until promoted synthesis is trusted.

---

## Hephaestus — curator / lint / maps

- Maintain zone `INDEX.md` canonical lists on promote.
- **Weekly lint** (`scripts/vault_lint.py`): orphan wikilinks (41 expected until `data-elements/` Wave 2), candidate backlog count, zone growth.
- **Spectral graph v2:** wikilink export for Overwatch demo — not agent navigation.
- New pursuit folder scaffold on Hermes request: `pursuits/<slug>/README.md` stub.

---

## Open decisions (Overwatch)

1. **Company intel:** ✅ `entities/company/kbr-services-readiness-sustainment.md` + depth in `global/domain_intel/capabilities/`.
2. **Pursuit slug:** ✅ Human slug folders + `display_name` + `sam_notice_id` in README frontmatter (`pursuits/INDEX.md`).
3. **Same org competitor + customer:** see Hermes explanation in chat 2026-07-02 — default **one page, two roles** when same legal entity.

## Smallest next step (no reorg)

Update zone INDEX “Canonical files” sections as first **trusted** promotes land; run weekly lint; use this table in Hermes triage skill.

**Preview:** [Vault intel taxonomy brainstorm](http://127.0.0.1:51763/#content/hermes/2026-07-02_vault-intel-taxonomy-brainstorm.md)