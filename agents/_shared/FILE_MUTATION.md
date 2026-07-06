# File mutation (party-wide)

**Project root:** `C:/Users/benma/ariadnes-thread-os`  
**Hermes `terminal.cwd`:** must be project root (not `agents/<name>/` alone). If cwd drifted, run `python scripts/fix_party_profile_cwds.py` or switch the desktop project to `ariadnes-thread-os` (`project_switch`).

## Wrong `resolved_path` (cwd guard)

If `write_file` / `patch` reports `resolved_path` under `C:\Users\benma\agents` **without** `ariadnes-thread-os` in the path, you are writing outside the repo:

1. `project_switch` to the `ariadnes-thread-os` project (or set profile `terminal.cwd` to `C:/Users/benma/ariadnes-thread-os`).
2. Retry with an explicit absolute path: `C:/Users/benma/ariadnes-thread-os/agents/...` or repo-relative `agents/...` from project root.
3. Do not continue editing phantom paths under `C:\c\Users\...`.

## Write tools (`write_file`, `patch`)

**Before writing:** optional sanity check — `python scripts/normalize_write_path.py "your/path"` → use printed absolute path if unsure.

| ✅ Do | ❌ Don't |
|------|--------|
| `agents/hermes/content/foo.md` | `/c/Users/benma/...` → phantom `C:\c\Users\...` |
| `C:/Users/benma/ariadnes-thread-os/knowledge/...` | `agents/other/...` when cwd is `agents/hermes` |
| Read `resolved_path` in tool response | Assume relative path without checking cwd |

### `write_file` timeout (~60s)

Large writes or slow disks may hit Hermes `write_file` timeouts. Prefer:

- `patch` for small targeted edits.
- Shell pipe: `python scripts/safe_repo_write.py agents/foo/bar.md` with body on **stdin** (prints absolute path on success).
- Sanity check first: `python scripts/normalize_write_path.py "your/path"`.

## Vault paths

- SSOT: `knowledge/` (repo root relative).
- Triage candidates: `knowledge/generated-projections/`.
- Board tasks: `board.db` via `scripts/board_add_task.py` or `POST /api/board` — **not** only quest markdown.

## Phantom tree

If `C:\c\Users\benma\` exists from bad writes, do not edit there — delete after backup (Hephaestus maintenance).

## Verification

- `python scripts/verify_party_paths.py`
- `python scripts/fix_party_profile_cwds.py` if profiles drifted
- Mission Control: `bash start.sh` (replaces stale server if `/api/cron` missing); `bash start.sh --force` to always restart

See `agents/REGISTRY.yaml` → `write_path_rule`.

**Build discipline:** `agents/_shared/DELIBERATE_BUILD.md` — Overwatch ideas ≠ same-session implementation.
