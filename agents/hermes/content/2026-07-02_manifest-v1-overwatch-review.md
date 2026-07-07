# Manifest v1 — Overwatch review (Phase 1)

**Date:** 2026-07-02  
**Inventory:** Hephaestus `deleg_02e67951` · **224** paths · no moves yet  
**CSV:** [vault-manifest-inventory.csv](http://127.0.0.1:51763/#content/hephaestus/2026-07-02_vault-manifest-inventory.csv)  
**Ship:** [phase1-inventory-ship.md](http://127.0.0.1:51763/#content/hephaestus/2026-07-02_phase1-inventory-ship.md)

---

## Machine proposal (zone-level — approve this, not 224 rows)

| Zone / bucket | Count | Proposed default | Meaning |
|---------------|------:|------------------|---------|
| **capabilities** | 46 | **RESCOUT** (all) | Iris refresh KBR URLs + cites before trust |
| **concepts** | 42 | **RESCOUT** 41 · KEEP 1 | USAspending salvage; Iris triage per 3/3 |
| **shipley** | 23 | **REWRITE** | Re-author from Capture Guide (W4–W5) |
| **global_wiki** (non-shipley) | ~64 | **REWRITE** / mixed | Doctrine pages; Clio voice pass in waves |
| **entities** | 4 | **KEEP** 2 · **ARCHIVE** 2 | KEEP company hub + INDEX; ARCHIVE smoke only |
| **foundation** | 4 | **REWRITE** | Includes schema → `ariadne-vault-schema.md` |
| **generated-projections** | 2 | per row | EDEN candidate etc. — no promote until rescout |
| **ARCHIVE now (smoke)** | **2** | **ARCHIVE** | `test-agency-xyz`, `example-competitor-llc` |

**Tag totals:** KEEP 16 · REWRITE 119 · ARCHIVE 2 · RESCOUT 87

---

## What happens after you approve manifest v1

1. **Odysseus** records PASS on zone defaults + 2 smoke ARCHIVE rows.  
2. **Phase 2 (minimal):** Hephaestus moves **only** the 2 smoke files → `generated-projections/archived/rebuild-2026/` (no mass archive).  
3. **Iris** opens Wave A rescout (top-10 capabilities + gap notes).  
4. **Promote freeze** stays on until post-W2 lint + your lift.

---

## One-line approval (reply in chat)

```
manifest v1 approved — proceed Phase 2 smoke archive + Iris Wave A rescout
```

**Odysseus formal signoff (G3 PASS, promote freeze ON):** [2026-07-02_manifest-v1-zone-signoff.md](http://127.0.0.1:51763/#content/odysseus/2026-07-02_manifest-v1-zone-signoff.md)

**Overwatch 2026-07-02:** Manifest v1 **approved** — Phase 2 + Iris Wave A proceed. **Entities caveat:** [entities hierarchy design](http://127.0.0.1:51763/#content/hermes/2026-07-02_entities-hierarchy-design.md) (flat `customers/` + `organizations/`, SAM/USAspending as metadata not folders).

**Dispute?** Name zone or path (e.g. “force KEEP concept X”) before approving.

---

## Re-run inventory

`python scripts/vault_manifest_inventory.py` (from repo root)