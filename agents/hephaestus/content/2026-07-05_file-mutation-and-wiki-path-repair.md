# File mutation and wiki path repair (2026-07-05)

**Owner:** Hephaestus maintenance  
**Scope:** Phantom tree hygiene, party profile `terminal.cwd`, vault env vars.

## Actions

1. **Phantom tree (`C:\c\Users\benma`)** — Listed 1 file (`ariadnes-thread-os/agents/_shared/agent-logs.db`). Backed up to `agents/_shared/backups/phantom-c-users-20260705.zip`, then removed the tree via `scripts/backup_phantom_tree.py`.
2. **Profile `ariadne-guildmaster`** — Created with `hermes profile create ariadne-guildmaster --clone-from iris`, synced workspace identity via `scripts/sync_party_profiles.py`, cwd set to project root.
3. **Party cwd** — `python scripts/fix_party_profile_cwds.py` for `ariadne-guildmaster`, `iris`, `clio`, `odysseus`, `hephaestus` → `C:/Users/benma/ariadnes-thread-os`.
4. **`~/.hermes/.env`** — Appended `WIKI_PATH` and `OBSIDIAN_VAULT_PATH` = `C:/Users/benma/ariadnes-thread-os/knowledge` (when missing).
5. **Verification** — `python scripts/verify_party_paths.py` → **OK**.

## Follow-up

- Do not write with `/c/Users/...` paths in `write_file` / `patch`; use repo-relative from project root or `C:/Users/benma/ariadnes-thread-os/...`.
- Re-run `scripts/backup_phantom_tree.py` only if phantom tree reappears.
- `ariadne-guildmaster` may need `ariadne-guildmaster setup` for dedicated API keys if not inheriting from shell.

## Not done

- No merge to `main` (per quest).