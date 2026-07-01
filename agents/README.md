# Agent workspaces (agentic OS — for the party, not Overwatch)

**Canonical project root:** `C:/Users/benma/ariadnes-thread-os`

## File mutation (fixes errors/warnings)

| Rule | Why |
|------|-----|
| **Never** `/c/Users/...` in `write_file` / `patch` | Creates phantom `C:\c\Users\...` |
| **Repo-relative** `agents/<name>/...` | Requires `terminal.cwd` = **project root** (all party profiles) |
| **Or absolute** `C:/Users/benma/ariadnes-thread-os/...` | Always safe |
| Check tool **`resolved_path`** | Confirms the real file touched |

**Scripts (Hephaestus):**
- `python scripts/fix_party_profile_cwds.py` — reset profile cwd to project root if drift
- `python scripts/verify_party_paths.py` — workspace + phantom tree check
- `python scripts/sync_party_profiles.py` — SOUL/MEMORY/USER → profiles

## Content delivery (Mission Control Library tab)

All agents: long-form `.md` in **own** `agents/<name>/content/` only. Canonical policy: `agents/_shared/CONTENT_DELIVERY_POLICY.md` (filename `YYYY-MM-DD_kebab-title.md`, `#` title line, confirm path in chat after save).

## Workspace files per agent
`SOUL.md`, `IDENTITY.md`, `USER.md`, `AGENTS.md`, `MEMORY.md`, `content/`.

## Hermes session per agent
| Agent | Profile | `terminal.cwd` (all) |
|-------|---------|----------------------|
| Hermes | `ariadne-guildmaster` | `C:/Users/benma/ariadnes-thread-os` |
| Iris | `iris` | same |
| Clio | `clio` | same |
| Odysseus | `odysseus` | same |
| Hephaestus | `hephaestus` | same |

**Isolation** = separate profile, memory, and `agents/<name>/content/` — not a per-agent terminal cwd.

**Overwatch does not run maintenance scripts.**