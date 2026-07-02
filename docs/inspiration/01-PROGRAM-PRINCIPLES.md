# Program principles — capform essence in Agent OS

How we translate capture **desires** into **ariadnes-thread-os** without recreating capform weight.

## 1. Desires vs direction

Overwatch states **outcomes** (compounding truth, fast capture, agents that maintain quality). Hermes and the party choose **mechanisms** (paths, skills, MCPs, MC modules) using Hermes architecture and Ponytail / Matt Pocock discipline. Feature names from capform or chat are hints, not requirements.

## 2. Protected `main`

- **main** = working Agent OS MVP.
- All inspiration docs and future capture features land on **feature branches**; merge after review.
- Inspiration library lives in `docs/inspiration/` on branch `docs/capform-inspiration` until merged.

## 3. Agent-operated operations

| Work type | Owner |
|-----------|--------|
| File writes, branches, commits (when directed) | Party via Hermes delegation |
| `sync_party_profiles.py`, MC backups | Hephaestus |
| Skill/MCP wiring, server/dashboard code | Hephaestus |
| Intel, packet prose, gate reviews | Iris, Clio, Odysseus |
| Coordination, merge, index consistency | Hermes |

Overwatch **does not** run routine scripts, vault lint, or profile sync. If a step requires a human-only action (secret, legal sign-off), docs must say so explicitly.

## 4. Ponytail minimalism

- Add **no** tab, store, or framework until a **real pursuit** or daily workflow fails without it.
- "Route exists" or "scaffold" = **not done** (capform honesty rule).
- Prefer deepening one module over new surfaces.

## 5. Matt Pocock architecture

- Thin routes / UI → fat **services** (Python stdlib first in thread-os).
- One opportunity record concept before duplicating state across SQLite, PG, and vault.
- Observable, testable seams; agents refactor via Hephaestus, not drive-by rewrites.

## 6. Two layers of text (not three brains)

| Layer | Role | Location (convention) |
|-------|------|------------------------|
| **Work staging** | Handoffs, drafts, loop output | `agents/<agent>/content/*.md` → Mission Control **Content** tab |
| **Compounding SSOT** | Trusted, structured, growing truth | `knowledge/thread/` (Wave 1 doc 02)—agents curate |
| **Hermes memory** | Compact prefs & conventions | Profile memory only—not the knowledge base |

Avoid a third parallel wiki unless it clearly subsumes vault + search; interlinking is an implementation choice, not a product pillar.

## 7. Review gate everywhere (doctrine)

**Intake → candidate → trusted.** Autonomous **preparation**; human **ratification**. Applies to vault pages, packet fields, skills, cron that affects capture, and promoted inbox items. Nothing silently auto-promotes to trusted or external send.

## 8. Living Briefing Packet = boss fight

One opportunity = one campaign. MS1–MS4 gates are phases; packet fields and evidence are objectives; gate approval is the "boss clear." Details in Wave 2 inspiration docs—not UI scope for Wave 0–1.

## 9. Inspiration doc template

Every topic doc in this folder must include:

1. Operator job (one sentence)
2. Why capform built it (incl. scaffold honesty)
3. True intent (decision enabled)
4. Mission Control / agent fit
5. **Minimal v1** — what **agents** automate this month
6. **Later** — parked capform backlog pointers
7. **Anti-patterns** — what not to port
8. **Party RACI**

## 10. Quality cadence

- **One primary inspiration doc per session** (party brainstorm → Hermes merge).
- No mass parallel doc dumps.
- No capture UI implementation until Wave 1–2 artifacts are merged and at least one doc (Living Packet) is validated against operator mental model.

## 11. Continuous improvement (end state)

Agents stack **candidate** work overnight (intel, drafts, fill suggestions); Overwatch morning = **review queue**, not empty fields. Implemented via capture loop supervisor + cron + skills—not a second agent runtime inside capform.

## 12. Reference repos

| Repo | Use |
|------|-----|
| `ariadne-capform` | Intent, dictionaries, route map—read only |
| `ariadnes-thread-os` | Ship target |

---

*Wave 0 complete. Proceed to Wave 1 doc 02 on explicit Overwatch **go**.*