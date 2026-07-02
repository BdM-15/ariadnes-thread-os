# File mutation (party-wide)

**Project root:** `C:/Users/benma/ariadnes-thread-os`  
**Hermes `terminal.cwd`:** must be project root (not `agents/<name>/` alone).

## Write tools (`write_file`, `patch`)

| ✅ Do | ❌ Don't |
|------|--------|
| `agents/hermes/content/foo.md` | `/c/Users/benma/...` → phantom `C:\c\Users\...` |
| `C:/Users/benma/ariadnes-thread-os/knowledge/thread/...` | `agents/other/...` when cwd is `agents/hermes` |
| Read `resolved_path` in tool response | Assume relative path without checking cwd |

## Vault paths

- SSOT: `knowledge/thread/` (repo root relative).
- Triage candidates: `knowledge/thread/generated-projections/`.
- Board tasks: `board.db` via `scripts/board_add_task.py` or `POST /api/board` — **not** only quest markdown.

## Phantom tree

If `C:\c\Users\benma\` exists from bad writes, do not edit there — delete after backup (Hephaestus maintenance).

## Verification

- `python scripts/verify_party_paths.py`
- `python scripts/fix_party_profile_cwds.py` if profiles drifted
- Mission Control: `bash start.sh` (replaces stale server if `/api/cron` missing); `bash start.sh --force` to always restart

See `agents/REGISTRY.yaml` → `write_path_rule`.