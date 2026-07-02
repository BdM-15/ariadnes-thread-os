---
entity_type: capture-signal
id: global-concept-vehicle_concentration
last_updated: 2026-06-08
name: "Top 3 vehicle share"
source_module: capture-insights
trust: trusted
type: concept
tags:
  - capture-insights
  - glossary
---

# Top 3 vehicle share

> One atomic concept page (Karpathy LLM wiki). Hover the **info** icon in the app for the short tip; this page compounds context over time.

## What it means

Percent of market dollars flowing through the three largest contract vehicles. High concentration = a few schedules or contract types gate most work.

## In the app

Capture Insights dashboard (contextual label)

## Key signals from USASpending

- Grounded in the current NAICS-filtered dashboard slice (bulk history + KPI endpoints).
- Re-ingest or widen NAICS to refresh; never treat a single snapshot as permanent truth.

## Synthesis / analysis

Use this signal with vault entries ([[customer-position]], competitive posture, vehicles) before advancing capture resources. Append dated notes below as you learn.

## Open questions / next actions

- What threshold would change your pursue / monitor / defer decision for this signal?
- Which [[entities]] agency or competitor entries should link here after your next +brain action?

## Related


- [[capture-insights-index]]
- [[buying-posture]]
- [[idiq-task-orders]]
- [[vehicle-holders]]
- [[access-lens]]
- [[pricing-buckets]]
- [[shape-target-gate]]
- [[agency-shape-gate]]

## Added/Updated 2026-06-08

- Seeded from `captureGlossary.ts` via `scripts/seed_capture_concepts.py`.
