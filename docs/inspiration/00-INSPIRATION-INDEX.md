# Capform → Mission Control inspiration index

**Branch:** `docs/capform-inspiration` · **Status:** Wave 1 in progress (doc **02** merged)  
**Source essence:** `C:/Users/benma/ariadne-capform` (read-only reference; do not port monolith)  
**Target system:** Ariadne's Thread **Agent OS** — Mission Control + five persistent party agents

## Why this library exists

The **Agent OS MVP** on `main` is protected. Capture depth from capform is **intent**, not code to merge wholesale. These documents record **why** each surface was built, **what decision** it enables, and **minimal v1** in an agent-operated OS—before we add UI or plumbing.

## Operator model

| Role | Responsibility |
|------|----------------|
| **Overwatch** | Intent, approve/reject, ideas |
| **Hermes** | Orchestration, merge, consistency |
| **Party** | Drafts, implementation, maintenance, vault hygiene, profile/skill wiring |

Overwatch does **not** run sync scripts, backups, or routine cleanup—agents do.

## Build waves (quality-first)

| Wave | Scope | Gate |
|------|--------|------|
| **0** | Index + program principles | ✅ this file |
| **1** | Knowledge SSOT · Task/capture funnel · Tools/MCP/skills | One doc per session; party brainstorm → Hermes merge · **02 ✅** |
| **2** | Living Packet (boss fight) · Review gate · Capture/opp record | After Wave 1 merged |
| **3** | Data Insights · Clew · Command cockpit | Intent only until Wave 2 used on a real opp |
| **4** | Education · Studio/Win · Tavern→MC | Parked depth explicit |
| **5** | PLAN north star · Backlog/continuous improvement · Reference corpus | Meta |

## Document registry

| ID | File | Capform anchor | MC / OS fit | Primary owner | Wave |
|----|------|----------------|-------------|---------------|------|
| 00 | `00-INSPIRATION-INDEX.md` | — | Program map | Hermes | 0 |
| 01 | `01-PROGRAM-PRINCIPLES.md` | doctrine | Cross-cutting rules | Hermes | 0 |
| 02 | `knowledge-vault-and-compounding-truth.md` | `/knowledge`, Obsidian | Vault SSOT + agent curation | Hephaestus | 1 |
| 03 | `task-management-and-capture-funnel.md` | `/tasks` | Inbox → promote (agents) | Hermes | 1 |
| 04 | `tools-mcp-and-skills.md` | `/tools/*`, `skills/`, `mcps/` | Executable capture tooling | Hephaestus + Iris | 1 |
| 05 | `living-briefing-packet-boss-fight.md` | packet model, `/capture` | One opp = one campaign | Clio + Odysseus | 2 |
| 06 | `review-gate-and-trust.md` | `/review`, candidate/trusted | Ratification layer | Odysseus | 2 |
| 07 | `capture-lane-and-opportunity-record.md` | `/opportunities/*` | Single opp record | Clio | 2 |
| 08 | `data-insights.md` | `/insights` | Identify / go-no-go | Iris | 3 |
| 09 | `clew-money-and-relationship-trace.md` | `/clew` | Trace → artifact | Iris | 3 |
| 10 | `command-center-cockpit.md` | `/` | ≤2-click actions (future capture tab) | Hermes | 3 |
| 11 | `education-lane.md` | `/education` | Tier 1–2 tooltips only for MVP | Clio | 4 |
| 12 | `studio-win-lane.md` | Studio (planned) | Artifacts/decks — post-MVP | Clio | 4 |
| 13 | `tavern-to-mission-control.md` | `tavern/` | What transferred to thread-os MC | Hephaestus | 4 |
| 14 | `plan-north-star-three-lanes.md` | `docs/PLAN.md` | Identify · Capture · Win | Hermes | 5 |
| 15 | `backlog-continuous-improvement.md` | `BACKLOG.md`, `HERMES_INTEGRATION.md` | Overnight prep, human ratify | Hermes | 5 |
| 16 | `reference-corpus-packet-call-plan-risk-shipley.md` | `docs/reference/` | Domain dictionaries | Odysseus | 5 |

## Capform route → inspiration doc (quick lookup)

| Capform route / area | Inspiration doc(s) |
|----------------------|-------------------|
| `/` Command center | `command-center-cockpit.md`, `plan-north-star-three-lanes.md` |
| `/insights` | `data-insights.md` |
| `/clew` | `clew-money-and-relationship-trace.md` |
| `/capture`, `/opportunities/{id}` | `capture-lane-and-opportunity-record.md`, `living-briefing-packet-boss-fight.md` |
| `/review` | `review-gate-and-trust.md` |
| `/knowledge` | `knowledge-vault-and-compounding-truth.md` |
| `/tasks` | `task-management-and-capture-funnel.md` |
| `/tools/mcp`, `/tools/skills` | `tools-mcp-and-skills.md` |
| `/education` | `education-lane.md` |
| Studio (planned) | `studio-win-lane.md` |
| Tavern dashboard | `tavern-to-mission-control.md` |
| `docs/PLAN.md`, `BACKLOG.md` | `plan-north-star-three-lanes.md`, `backlog-continuous-improvement.md` |
| `docs/reference/*` | `reference-corpus-packet-call-plan-risk-shipley.md` |

## Current thread-os Mission Control tabs (baseline)

| Tab | Today | Capture-era note |
|-----|--------|------------------|
| Overview | Agent OS health, activity | No pWin/capture UI per canon until explicitly added |
| Agents | Party status + logs | Stays |
| Tasks | Kanban + cron stats | Extend per `task-management-and-capture-funnel.md` |
| Schedule | Cron calendar | Agents create/manage jobs |
| Content | `agents/*/content/*.md` | Staging; vault is separate SSOT |

## Next action

**Wave 1 · Doc 03:** `task-management-and-capture-funnel.md` — Hermes draft → party brainstorm → Overwatch review before merge.