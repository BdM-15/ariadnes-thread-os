# MC Vault tab MVP (v1.2)

**Date:** 2026-07-02  
**Approval:** Option F — [vault-browse-approved](http://127.0.0.1:51763/#content/hermes/2026-07-02_vault-browse-approved.md)

## Shipped

- **Tab:** Vault in Mission Control (badge **v1.2**)
- **API:** `GET /api/vault/tree` — lists all vault `.md` with zone + trust hint
- **UI:** Zone filters, morning queue (`/api/vault/candidates`), browse list, read-only markdown reader
- **Deep links:** `#vault/generated-projections/eden-edge-computing-candidate.md`

## Try it

1. Restart MC if needed: `bash start.sh --force` from repo root  
2. Open [Mission Control Vault](http://127.0.0.1:51763/#vault)  
3. Or [root INDEX](http://127.0.0.1:51763/#vault/INDEX.md)

## Parked (per F)

- Search box, wikilink navigation, graph view, in-UI promote

## Files

- `server.py` — `vault_tree_data()`, route `/api/vault/tree`
- `index.html` — panel + client JS
- Backup: `agents/_shared/backups/*_2026-07-02T13-14.*`