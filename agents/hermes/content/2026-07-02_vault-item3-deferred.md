# Vault item 3 deferred (Overwatch decision)

**Date:** 2026-07-02  
**Decision:** Ship **items 1–2** (MC browse UI + `knowledge/` flatten). **Park item 3** (MC edit, `vault_schema_lint`, Clio harmonize) until after **ground-up vault overhaul** brainstorm.

## Rationale (Hermes)

- Edit permissions and zone matrix in Clio’s workflow assume **final** concern zones and `ariadne-vault-schema.md` — not capform-era `capture-llm-wiki` + smoke entities.
- Shipping save APIs now creates **throwaway surface** (routes, policies, board hooks) we would rip out or rewrite in a rebuild.
- Read-only Vault tab + agent writes (`promote_vault_candidate.py`, triage B, party `content/`) is enough until SSOT shape is ratified.
- Item 3 becomes a **Wave 1.5** deliverable tied to post-rebuild schema, not doc 02 close.

## Next

1. Hephaestus commit `feat(vault): … items 1-2` (delegated).
2. Brainstorm item 4 / ground-up rebuild with party.
3. Re-scope item 3 against new schema + MC discipline.