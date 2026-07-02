---
entity_type: capture-signal
id: global-concept-buying_posture
last_updated: 2026-06-08
name: "Buying posture"
source_module: capture-insights
trust: trusted
type: concept
tags:
  - capture-insights
  - glossary
---

# Buying posture

> One atomic concept page (Karpathy LLM wiki). Hover the **info** icon in the app for the short tip; this page compounds context over time.

## What it means

Whether this market buys mainly through task orders on existing vehicles, standalone contracts, or a mix. Drives whether you invest in schedule access, open competition, or both.

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
- [[idiq-task-orders]]
- [[vehicle-concentration]]
- [[vehicle-holders]]
- [[access-lens]]
- [[pricing-buckets]]
- [[shape-target-gate]]

## Added/Updated 2026-06-08

- Seeded from `captureGlossary.ts` via `scripts/seed_capture_concepts.py`.
