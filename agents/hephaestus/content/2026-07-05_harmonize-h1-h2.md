# Vault harmonize H1-H2 (2026-07-05)

**Branch:** `feature/knowledge-vault-v1` (no merge main)  
**Agent:** Hephaestus maintenance  
**Program:** `agents/hermes/content/2026-07-05_vault-llm-wiki-harmonize-program.md`

## Preconditions

- W6 capability tail complete (viaverse, wraith trusted).
- Single-script writes per `FILE_MUTATION.md`.

## Executed

| Wave | Action |
|------|--------|
| **H1** | `python scripts/harmonize_h1_h2.py` — retarget 77× `*-rewrite-candidate` wikilinks to promoted capability slugs; normalize `trust:` in page frontmatter; 46 minimal stubs (data-elements, entity LOGCAP chain, DHS paths, wikilinks ref, usaspending concept) |
| **H2** | Refreshed `knowledge/index.md` catalog header counts; appended `log.md` harmonize batch |

## Lint

```text
vault_lint unresolved wikilinks: 0
markdown files: ~318
```

Re-run: `python scripts/vault_lint.py` from repo root.

## Artifacts

- `scripts/harmonize_h1_h2.py` (idempotent; safe to re-run)
- `knowledge/log.md` — `harmonize | H1-H2 capabilities + index`
- `knowledge/index.md` — Last refreshed line updated

## Not in scope

- H3–H5 (page shape gold templates, Obsidian human pass, Shipley templates)
- Merge to `main`