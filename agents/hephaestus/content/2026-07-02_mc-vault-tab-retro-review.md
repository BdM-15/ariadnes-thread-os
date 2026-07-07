# MC Vault tab v1.2 — Hephaestus retroactive review

**Date:** 2026-07-02  
**Trigger:** Hermes routing slip (in-session MC implementation without `delegate_task` to Hephaestus)  
**Authority:** `agents/_shared/MISSION_CONTROL_DISCIPLINE.md`  
**Acceptance baseline:** [vault-browse-approved](../../hermes/content/2026-07-02_vault-browse-approved.md) (Option F)

## Ownership statement

**Hephaestus** retroactively accepts **implementation ownership** of the Vault tab v1.2 ship in repo-root `index.html` and `server.py`, effective this review. The code is **not** rewritten; it is audited, verified, and documented here. Future MC changes remain Hephaestus-only per discipline.

Hermes retains **orchestration** ownership (approval doc, board, routing slip incident). This review does **not** legitimize direct Hermes MC edits as precedent.

## Backup vs current (audit)

| Artifact | Backup (`*_2026-07-02T13-14.*`) | Current |
|----------|----------------------------------|---------|
| `server.py` | 1035 lines; `/api/vault/candidates`, `/api/vault/read`; **no** `vault_tree_data()` or `/api/vault/tree` | 1080 lines; adds `VAULT_ZONES`, `vault_tree_data()`, route `/api/vault/tree` |
| `index.html` | 345 lines; **no** Vault tab, **no** `loadVault` / `panel-vault`; board-only `vaultPathFromNotes` | 361 lines; Vault tab, stats, zone filters, morning queue, browse, reader, `#vault/<path>` deep links, nav badge **v1.2** |

Backup timestamp matches discipline reference; diff confirms Hermes (or parent session) shipped v1.2 **after** the 13:14 backup, without a post-ship Hephaestus backup (process gap only — no functional defect).

## Pass/fail checklist (Option F v1)

| Requirement | Result | Evidence |
|-------------|--------|----------|
| Mission Control **Vault** tab | **PASS** | Tab `data-tab="vault"`, panel `#panel-vault` |
| UI version **v1.2** | **PASS** | `#mcVersionBadge` → v1.2 |
| `GET /api/vault/tree` | **PASS** | `{"ok":true,"count":221,...}` live curl |
| `GET /api/vault/candidates` | **PASS** | Returns projection candidates incl. `eden-edge-computing-candidate.md` |
| `GET /api/vault/read?path=` | **PASS** | `INDEX.md` and candidate paths return `ok:true`; traversal `..` → **404** |
| Zone filters | **PASS** | all, _root, entities, foundation, generated-projections, global, pursuits, relationships |
| Morning queue (read-only) | **PASS** | UI shows 1 candidate (INDEX excluded client-side) |
| Browse + read-only markdown reader | **PASS** | `markdownHtml` / marked; reader head + body |
| Deep link `#vault/<rel-path>` | **PASS** | `#vault/INDEX.md` → reader title INDEX, body loaded; `#vault/generated-projections/eden-edge-computing-candidate.md` loads |
| Parked: search, wikilinks, graph, promote | **PASS** (correctly absent) | Per approval doc |

## Smoke verification (2026-07-02)

- MC up: `http://127.0.0.1:51763/`
- APIs: tree / candidates / read exercised via curl
- UI: browser snapshot on `#vault` and deep links

## Nits (non-blocking — no code change)

1. **Overview** eyebrow still shows `v1.1` (`#overviewVersion`) while nav badge is `v1.2` — cosmetic only.
2. **`/api/vault/candidates`** includes `generated-projections/INDEX.md`; morning-queue UI correctly filters it out.

## Fixes applied

**None.** No functional defects found; discipline violation was process-only.

## Process follow-up (Hephaestus)

- Next MC touch: run `bash agents/_shared/backup-mission-control.sh` first.
- v1.1+ parked features (search, wikilinks, spectral graph): Hephaestus DRI when Hermes opens quest after Overwatch priority.

## References

- Build log (Hermes-era): [2026-07-02_mc-vault-tab-mvp.md](./2026-07-02_mc-vault-tab-mvp.md)
- Discipline: [MISSION_CONTROL_DISCIPLINE.md](../../_shared/MISSION_CONTROL_DISCIPLINE.md)