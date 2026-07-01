# Ariadne's Thread OS

Lightweight, agent-first Mission Control for a solo capture professional managing Shipley-aligned opportunities.

**Core artifact:** Living Briefing Packet — a dynamic, review-gated, AI-fillable capture roadmap with milestone gates.

**Party agents:** Five persistent Greek-myth themed agents (Hermes, Iris, Clio, Odysseus, Hephaestus) with isolated workspaces do the work under Guildmaster coordination.

**Dashboard:** Glassmorphism Mission Control (overview radar, party status, quests/packet workspace, schedule/gates, vault/library) with live SSE, kanban, activity logging, and stdlib-only Python backend.

## Quick start

**Requirements:** Python 3.10+ and Bash (Git Bash on Windows works).

```bash
git clone https://github.com/BdM-15/ariadnes-thread-os.git
cd ariadnes-thread-os
bash start.sh
```

Opens Mission Control at [http://127.0.0.1:51763/](http://127.0.0.1:51763/).

## Project layout

| Path | Purpose |
|------|---------|
| `server.py` | Dashboard API (stdlib HTTP server, SQLite, SSE) |
| `index.html` | Mission Control UI |
| `start.sh` | One-command launcher |
| `agents/` | Party agent workspaces (`SOUL.md`, `MEMORY.md`, `content/`, etc.) |
| `agents/REGISTRY.yaml` | Agent roster and Hermes profile bindings |
| `scripts/` | Profile sync, path verification, dashboard build helpers |
| `IDEA.md` | Product vision and build discipline |

## Party roster

| Agent | Role |
|-------|------|
| **Hermes** | Guildmaster / orchestrator |
| **Iris** | Scout / intel researcher |
| **Clio** | Packet filler / scribe |
| **Odysseus** | Knight / strategist (gates & compliance) |
| **Hephaestus** | Artificer / builder (scripts & maintenance) |

See `agents/README.md` and `agents/TEAM_AWARENESS.md` for workspace rules and handoffs.

## Build discipline

Start minimal: core capture loop + dashboard shell only. Add complexity only when real usage demands it. Agents co-build the system; routine maintenance goes to a local small model; frontier models reserved for high-stakes planning.

## Local setup notes

After cloning, update hardcoded paths in `agents/REGISTRY.yaml` and maintenance scripts if your checkout is not at the documented canonical root. Run:

```bash
python scripts/verify_party_paths.py
python scripts/sync_party_profiles.py   # after editing party identity files
```

Runtime databases (`board.db`, `agent-logs.db`, `snap.json`) are created locally and gitignored.

## License

MIT — see [LICENSE](LICENSE).