# Vault retrieve contract (party-wide)

Before pursuit-relevant **strategy, entity, or competitor claims**:

1. Read `knowledge/index.md`
2. Read the zone `INDEX.md` for that concern (`entities/`, `global/`, `pursuits/`, `generated-projections/`)
3. Read trusted pages (`trust: trusted`) or explicit candidates if asked

**Not a substitute:** Hermes profile memory, `agents/*/content/` staging.

**Intake:** Unstructured Overwatch dumps → Hermes triage B (`agents/ROUTER.md`).

**Lint:** `python scripts/vault_lint.py` — weekly via Hephaestus cron.

## Karpathy / llm-wiki skill (Hermes)

When building or querying the vault, load skill **`llm-wiki`** and treat `knowledge/` as `WIKI_PATH`:

1. Read **`foundation/ariadne-vault-schema.md`** (Layer 3; supersedes `capture-llm-wiki` alias)
2. Read **`knowledge/index.md`**
3. Read recent **`knowledge/log.md`** (last promote/lint blocks)

Then ingest, promote, or answer — always append **log.md** and refresh **index.md** on trusted changes. Optional human IDE: skill **`obsidian`** at `OBSIDIAN_VAULT_PATH` = same folder as `WIKI_PATH` (`knowledge/foundation/reference/obsidian-desktop.md`).[H[2J[3J