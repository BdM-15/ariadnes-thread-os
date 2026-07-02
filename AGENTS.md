# Ariadne Thread OS — project rules (injected for sessions at repo root)

## File mutation (mandatory — fixes wrong-directory writes)

**Canonical project root:** `C:/Users/benma/ariadnes-thread-os`

| Do | Don't |
|----|--------|
| `agents/<name>/file.md` (repo-relative from **project root** cwd) | `/c/Users/benma/...` in `write_file` / `patch` → lands in `C:\c\Users\...` |
| `C:/Users/benma/ariadnes-thread-os/agents/<name>/...` (absolute) | `agents/other/...` when cwd is `agents/hermes` (resolves under wrong folder) |
| Read tool `resolved_path` in the response | Assume relative paths without checking cwd |

**Party profiles** use `terminal.cwd` = this repo root so `agents/iris/...` resolves correctly. Each agent still **writes only** under their own `agents/<self>/` and `content/` unless Hermes delegates cross-agent doc maintenance to Hephaestus.

**Phantom tree:** If `C:\c\Users\benma\` exists from old bad writes, do not edit there — delete via Hephaestus maintenance quest after backup check.

**Profile sync:** Hephaestus runs `python scripts/sync_party_profiles.py` (not Overwatch).

**Team:** Roster and handoff rules in `agents/TEAM_AWARENESS.md` (Overwatch → any agent; name colleague when off-lane).

**Activity log:** All party agents log via `agents/_shared/log-task-local.sh` per `agents/_shared/LOGGING_POLICY.md`.

**Long-form content:** Save to own `agents/<self>/content/` per `agents/_shared/CONTENT_DELIVERY_POLICY.md` (Content tab reads these files).

**Chat file names:** When citing a path to Overwatch, include a preview link per `agents/_shared/CHAT_FILE_LINK_POLICY.md`.

See also: `agents/README.md`, `agents/REGISTRY.yaml` (`write_path_rule`).