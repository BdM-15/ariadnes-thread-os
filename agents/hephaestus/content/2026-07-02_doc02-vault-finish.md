# Doc 02 vault finish (Hephaestus)

**Date:** 2026-07-02  
**Wave:** 1 · doc 02 · v1 close  

## Delivered

| Item | Result |
|------|--------|
| `scripts/promote_vault_candidate.py` | CLI: `--candidate`, `--dest`, `--dry-run`, citation + `trust: candidate` gates |
| Zone INDEXs | `global/`, `generated-projections/`, `pursuits/` enriched per doc 02 §4.1 |
| Wikilink lint | **41 → 38** unresolved (heuristic); safe stubs/fixes where applied |

## Promote path (proven once)

```bash
python scripts/promote_vault_candidate.py \
  --candidate generated-projections/eden-edge-computing-candidate.md \
  --dest global/domain_intel/capabilities/eden.md \
  --dry-run
```

**Dry-run OK** 2026-07-02 — does not execute without Overwatch + Odysseus gate pass.

## Delegation note

Subagent completion messages returned **HTTP 403** (OAuth token) to parent Hermes; **on-disk artifacts verified** by Hermes after run (`promote_vault_candidate.py` present; lint delta).

## References

- Odysseus gate: `agents/odysseus/content/2026-07-02_vault-promote-gate-checklist.md`
- Party: Iris brief, Clio polish on EDEN candidate

---

*Logged:* `doc02 vault INDEX lint promote` (hephaestus)