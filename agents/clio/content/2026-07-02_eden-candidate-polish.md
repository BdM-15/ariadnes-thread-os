# EDEN vault candidate polish (Wave 1 doc02)

**Quest:** doc02 EDEN candidate polish · **Agent:** Clio · **Date:** 2026-07-02

## Summary

Polished `knowledge/thread/generated-projections/eden-edge-computing-candidate.md` for **Overwatch morning queue** readability: 30-second scan block, citation table, explicit promote/hold/reject decision row, and sections aligned with `foundation/capture-llm-wiki.md` (Key signals, Synthesis, Open questions, Related, Added/Updated).

## Changes to candidate page

| Area | Before | After |
|------|--------|--------|
| Frontmatter | Single-line `citations` string | Structured provenance keys (`source:`, `fleeting:`, `poc_named:`); `review_id: null`; `morning-queue` tag |
| Top of body | Status paragraph only | **Morning queue** callout: trust, promote gate, today's action |
| Evidence | Bullet list under "What we know" | **Key signals + citations** table |
| Analysis | Implicit | **Synthesis** paragraph (matrix placeholder language) |
| Actions | "Open actions" only | Split **Open questions** vs **Open actions**; archive path on reject |
| Review UX | None | **Overwatch decision** table (promote / edit & hold / reject) |
| Related | Bare wikilinks | Same links + one-line role per target |
| Audit | None | **Added/Updated** append-only stamp |

**File touched:** `knowledge/thread/generated-projections/eden-edge-computing-candidate.md`

## Rationale (morning queue)

Per `docs/inspiration/knowledge-vault-and-compounding-truth.md`, Hermes summarizes **new candidates** for Overwatch — not full vault dumps. This page now surfaces:

1. Trust boundary and promote precondition in the first screen.
2. Grounded signals separated from interpretation.
3. A single decision table matching candidate → trusted workflow §4.

## Reusable snippet — `generated-projections` capability candidate

Copy into `knowledge/thread/generated-projections/<slug>-candidate.md` when triage lands a **capability discovery** (unverified internal mention).

```markdown
---
added: "<ISO8601>"
citations: "source:<meeting|intel|chat> • fleeting:<one-line> • poc_named:<Name or unknown>"
id: candidate-<slug>
last_updated: <YYYY-MM-DD>
name: "<DISPLAY NAME> — capability (discovery)"
trust: candidate
type: capability
capability_status: unverified
poc: "<Name or TBD>"
tags: [capability-discovery, follow-up, morning-queue]
source: <meeting|iris|hermes>
review_id: null
---

# <Short title> — candidate capability

> **Morning queue (30s scan)**  
> **Trust:** `candidate` · **Promote?** <one-line gate>.  
> **Today:** <single next action for Overwatch>.

**Status:** Unverified — **not** trusted until promoted after <gate>.

## Key signals + citations

| Signal | Citation |
|--------|----------|
| <fact> | `<provenance>` |

## Synthesis

<2–4 sentences — evidence only, no invented offering detail.>

## Open questions

1. <question>

## Open actions

1. <follow-up>
2. On confirmation → promote to `global/domain_intel/capabilities/<slug>.md` and link from [[kbr-services-readiness-sustainment]].
3. If duplicate/noise → `generated-projections/archived/` + `log.md` line.

## Overwatch decision

| Option | When |
|--------|------|
| **Promote** | <condition> |
| **Edit & hold** | Partial detail; append `## Added/Updated <date>` |
| **Reject** | Duplicate, noise, or superseded |

## Related

- [[kbr-services-readiness-sustainment]] — RS BU hub
- [[capabilities-catalog]] — trusted index
- [[capture-llm-wiki]] — schema

## Added/Updated <date>

- <who>: <what changed>
```

### Template notes

- Keep **citations** in frontmatter machine-greppable; human-readable table in body.
- Never set `trust: trusted` in `generated-projections/` without Overwatch-approved promote.
- Prefer wikilinks that already exist in vault; add new pages only on promote path.

## Handoff

- **Hermes:** include in morning candidate summary if still `trust: candidate`.
- **Odysseus:** citation check on any promote request.
- **Hephaestus:** optional INDEX line under `generated-projections/INDEX.md` when candidate count grows.