---
id: global-capture-insights-index
last_updated: 2026-06-08
name: "Capture Insights Concepts Index"
source_module: capture-insights
tags: 
trust: trusted
type: index
---

# Capture Insights — Concept Index

Map of content (MOC) for dashboard labels and signals. **One concept = one file** under `concepts/` — not a single monolithic glossary. Follows `data/knowledge/schema/capture-llm-wiki.md` (Karpathy LLM wiki pattern).

Click **vault** beside any in-app label to open the matching concept page.

### Market overview

- [[market-tam]]
- [[market-momentum]]
- [[market-concentration]]
- [[future-funding]]
- [[recompete-radar]]
- [[hot-agency-recompete]]
- [[match-lens]]
- [[suitability]]
- [[synergy]]
- [[follow-the-money]]
- [[sam-live-discovery]]
- [[capture-intensity]]
- [[set-aside-mix]]
- [[extent-competed]]

### Agency intelligence

- [[hot-agency]]
- [[qual-gate]]
- [[customer-position]]
- [[relationship-heatmap]]

### Competitive analysis

- [[competitor-posture]]
- [[strategy-lens]]
- [[gap-fill-teaming]]
- [[teaming-fit]]
- [[shared-buyers]]

### Contract vehicles & pricing

- [[buying-posture]]
- [[idiq-task-orders]]
- [[vehicle-concentration]]
- [[vehicle-holders]]
- [[access-lens]]
- [[pricing-buckets]]
- [[firm-fixed-pricing]]
- [[non-fixed-pricing]]
- [[dominant-flexible-type]]
- [[pressure-tier]]
- [[agency-shape-gate]]
- [[shape-target-gate]]
- [[ffp-shaping-radar]]

### Geographic analysis

- [[place-of-performance]]
- [[geo-concentration]]
- [[state-quadrant]]
- [[pursuit-lens]]

### Combo insights

- [[combo-tier]]
- [[combo-signals]]

## How this vault stays organized

1. **Atomic pages** — each signal/concept is its own `.md` with wikilinks.
2. **This index** — LLM and humans navigate from here; update when adding terms.
3. **Schema** — `data/knowledge/schema/capture-llm-wiki.md` defines frontmatter and append-only updates.
4. **Regenerate** — `python scripts/seed_capture_concepts.py` refreshes stubs from `captureGlossary.ts` (won't overwrite your appended sections).

## Added/Updated 2026-06-08

- Reorganized from monolithic glossary into `concepts/` + this index.

## Related
- [[capture-llm-wiki]]
- [[bid-no-bid-decision-framework]]
- [[entities]]
