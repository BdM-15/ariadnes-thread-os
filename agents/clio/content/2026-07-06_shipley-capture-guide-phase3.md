---
quest_slug: shipley-capture-guide-phase3
from_agent: clio
status: shipped
---

# Shipley Capture Guide — phase 3 ingest (Clio)

Branch: feature/knowledge-vault-v1 (no merge to main).

## Shipped

- Six new trusted concept pages under `knowledge/global/domain_intel/concepts/`:
  - `shipley-capture-manager-role-capture.md`
  - `shipley-executive-summary-capture.md`
  - `shipley-oral-presentations-capture.md`
  - `shipley-past-performance-capture.md`
  - `shipley-solution-development-capture.md`
  - `shipley-metrics-kpis-capture.md`
- Hub phase 3 table: `knowledge/global/domain_intel/concepts/shipley-capture-guide-hub.md`
- Batch: `scripts/shipley_capture_guide_phase3_batch.py`
- Activity log entry in `knowledge/log.md` (`shipley | phase3`)

## Review

reviewed_by axelrod2023; paraphrase-only from `knowledge/foundation/raw/shipley/Shipley-Capture-Guide-extract.md` with page cites.

## Verification (2026-07-06)

- Re-ran `python scripts/shipley_capture_guide_phase3_batch.py` from repo root — all six concept pages refreshed; hub phase 3 table already present (idempotent skip).
- `python scripts/vault_lint.py` — **0 unresolved wikilinks** (337 markdown files).

## Next

Remaining TOC chapters (costing, customer interface depth, opportunity qualification, pricing to win, sales communication, teaming, value propositions, supporting proposal) in later waves; dedup with `knowledge/global/global_wiki/shipley/`.
