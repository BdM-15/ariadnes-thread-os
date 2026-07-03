# Pre-W2 hygiene (G2) — ship note

**Date:** 2026-07-03  
**Agent:** Hephaestus  
**Follow-up:** `deleg_a71a7b74`  
**Gate:** G2 pre-W2 complete before W2 Clio Wave A candidates land on disk

---

## Delivered

| Item | Result |
|------|--------|
| Wikilink alias pass | `[[capture-llm-wiki]]` → `[[ariadne-vault-schema]]` project-wide in `knowledge/` (schema file retains alias documentation only); idempotent re-run: **0** files |
| Schema §11 3b | `knowledge/foundation/ariadne-vault-schema.md` — **Entities 3b (`customers/`, `companies/`)** marked ✅ Phase 3b live (G2 ack 2026-07-02) |
| Promote gate checklist | `agents/odysseus/content/2026-07-02_vault-promote-gate-checklist.md` — flat `entities/customers/` + `entities/companies/` write zones (tracked) |
| Root catalog | `knowledge/index.md` — zones + `[[ariadne-vault-schema]]` pointer (W2 index row updates on disk prior to this commit) |
| `vault_lint` | **2026-07-03 14:55 UTC** — exit **0**; 231 md files; entities zone **3**; unresolved wikilinks **41** (expected deferred / Wave 2 stubs); logged in `knowledge/log.md` |

---

## Not in this hygiene pass

- Trusted promotes (freeze ON)
- W2 rewrite candidates under `generated-projections/*-rewrite-candidate.md` (Clio ship separate)
- MC Vault tab / `MISSION_CONTROL_DISCIPLINE.md` (parallel Hephaestus track)

---

## Verification

```bash
python scripts/_pre_w2_wikilink_pass.py   # updated 0 files
python scripts/vault_lint.py                # exit 0
```

---

## References

- Odysseus G2 schema review: `agents/odysseus/content/2026-07-02_g2-schema-review.md`
- Phase 3b ship: `agents/hephaestus/content/2026-07-02_phase3b-entities-migration-ship.md`
- Clio W2: `agents/clio/content/2026-07-03_w2-wave-a-candidates-ship.md`

*Logged:* pre-W2 hygiene G2 commit (hephaestus)