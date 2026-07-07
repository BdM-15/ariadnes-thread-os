# Ariadne's Thread — Hermes OS
### The complete rebuild playbook: one Hermes, one repo, one mission control

A clean-room successor to the Komputer Mechanic dashboard prompt-book, rebuilt for
**Hermes Desktop on Windows**, vetted prompt-by-prompt against what actually worked
(and failed) in the first Ariadne build, and governed by two rules:

> **Ponytail rule:** the best code is no code. Park ideas in a ledger; build when a real need arrives twice.
> **Pocock rule:** deep modules, simple interfaces. One file that does one thing well beats five that coordinate.

**Total prompts: 30** across 7 phases. Every prompt is pasted into **Hermes Desktop chat** —
you (Overwatch) never open a terminal, run a script, or edit a file. The agents operate; you direct and approve.

---

## The cast

| Name | Role | Mythos fit |
|---|---|---|
| **Overwatch** | You. Owner, director, final approver. Highest authority. | The one holding the thread |
| **Hermes** | Default Hermes Desktop agent. Messenger & steward — bootstraps the system, then hands orchestration to Minos. | God of messengers, guides, and thresholds |
| **Minos** | Orchestrator. Routes, decomposes, ratifies, enforces gates. Stood up in Phase 3. | Judge-king of Crete — the gatekeeper |
| **Iris** | Scout. Federal signals, SAM, USAspending, competitor intel. | Messenger of the gods, eyes on the horizon |
| **Clio** | Scribe. Briefing packets, synthesis, prose, evidence mapping. | Muse of history |
| **Odysseus** | Strategist. Shipley gates, risk, compliance, stakeholder strategy. | The cunning navigator |
| **Hephaestus** | Artificer. Sole builder of mission control, tools, skills, maintenance. | God of the forge |

Old "guildmaster / tavern" naming is retired. Minos is the orchestrator title everywhere.

---

## Architecture in one picture

```
C:\Users\benma\AppData\Local\hermes\          ← ENGINE ROOM (Hermes runtime)
  profiles\{minos,iris,clio,odysseus,hephaestus}\   app state, sessions, auth
  ── NOBODY writes project files here. Reinstalls wipe it. ──

C:\Users\benma\ariadnes-thread-hermes-os\     ← THE THREAD (one repo, GitHub-backed)
  AGENTS.md                    project rules injected into every session
  vault\                       Obsidian knowledge vault (curated migration)
  agents\
    minos\      content\  quests\
    iris\       content\
    clio\       content\
    odysseus\   content\
    hephaestus\ content\
    _shared\                   policies, log script, backup script
  mission-control\             server.py · index.html · board.db · backups\
  docs\
    DELIBERATE_BUILD.md        the parked-ideas ledger (ponytail law)
    LESSONS.md                 carried from build #1
```

Every agent profile's working directory points at the repo root. Hermes Desktop is your
single interface; the repo is the single durable memory; GitHub is the single backup.

---

## Lessons carried from build #1 (why this book differs from the original)

1. **Phantom tree disaster** — agents writing `/c/Users/...` paths created a fake
   `C:\c\Users\` tree. Fix: one canonical root in `AGENTS.md`, absolute Windows paths,
   verify-after-write. Baked into Prompt 7.
2. **Orchestrator built UI in-session** — Hermes hot-patched the dashboard and broke
   discipline. Fix: Hephaestus is *sole implementer* of mission control files. Prompt 8.
3. **Notification spam** — reminder ladders fired days early. Fix: board task first,
   one reminder at the meaningful moment. Prompt 9.
4. **Flat quest files invisible** — quests as loose `.md` weren't tracked. Fix:
   `quests/<slug>/quest.yaml` is the only quest state format. Prompt 12.
5. **Bash scripts on Windows** — fragile. Fix: Python-stdlib-only shared scripts.
6. **GPU-melting dashboard** — stacked `backdrop-filter: blur(34px)`, infinite radar
   sweep, 900 ms canvas redraws, DOM carousel every 2.2 s. Fix: the Performance
   Contract (Appendix A) governs every UI prompt in Phase 6.
7. **What worked — keep:** the capture quest loop (tested live over Telegram),
   trust-gated vault with candidate → promote flow, board.db as task SSOT, version
   badge + pre-change backups, per-agent content folders feeding the Content tab.

---
---

# PHASE 0 — Preserve the past (Prompts 1–2)

*Run these in your CURRENT Hermes install, before reinstalling.*

### Prompt 1 — Archive the old world

```
You are about to be retired and reborn. Before anything else, create a complete archive
of the current system so nothing is lost.

1. Create C:\Users\benma\ariadne-archive\ and copy into it:
   - From C:\Users\benma\AppData\Local\hermes\: every profiles\<name>\ folder's
     SOUL.md, config.yaml, profile.yaml, memories\, and skills\ (skip sessions,
     caches, auth files, and state.db — they are runtime junk).
   - The root SOUL.md and config.yaml.
2. In the old repo C:\Users\benma\ariadnes-thread-os\: stage and commit ALL current
   changes with message "archive: final state before hermes-os rebuild", tag it
   v1-final, and push to GitHub.
3. Zip C:\Users\benma\ariadne-archive\ to ariadne-archive-<date>.zip in the same folder.

Report: archive path, zip size, commit hash, and confirmation the push succeeded.
Do not delete anything.
```

### Prompt 2 — Extract the inheritance

```
From the old repo C:\Users\benma\ariadnes-thread-os\, assemble a migration kit at
C:\Users\benma\ariadne-archive\migration-kit\ containing copies of:

1. POLICIES — agents\_shared\: LOGGING_POLICY.md, NOTIFICATION_DISCIPLINE.md,
   MISSION_CONTROL_DISCIPLINE.md, CONTENT_DELIVERY_POLICY.md, DELIBERATE_BUILD.md,
   MEMORY_LAYERS.md, TASK_WORKFLOW_LADDER.md, FILE_MUTATION.md, VAULT_RETRIEVE.md
2. IDENTITY — agents\TEAM_AWARENESS.md, agents\REGISTRY.yaml, agents\ROUTER.md,
   agents\CAPTURE_LOOP_SUPERVISOR.md, and every agents\<name>\AGENTS.md + SOUL.md
3. VAULT — the entire knowledge\ folder as-is (curation happens later, in the new home)
4. QUEST EVIDENCE — agents\hermes\content\quests\ (the EAGLE Ft. Benning and Powidz
   quest folders — these are the proven pipeline templates)
5. MISSION CONTROL — server.py, index.html, board.db from the repo root
6. DEBT — docs\TECH_DEBT.md

Report a file count per category. This kit is the ONLY thing the new system reads
from the old world.
```

**⏸ Checkpoint:** verify the zip and migration kit exist, then uninstall Hermes Desktop,
rename `C:\Users\benma\AppData\Local\hermes` to `hermes-old-backup`, and install fresh
Hermes Desktop. First launch gives you a clean default Hermes agent. Continue below in
the NEW install.

---
---

# PHASE 1 — Found the new home (Prompts 3–7)

*Pasted into the fresh Hermes Desktop, to the default Hermes agent.*

### Prompt 3 — Hermes, steward of the rebuild

```
Your name is Hermes — the default agent and steward of this system. I am Overwatch,
the owner, with final authority on everything. My name is Ben.

We are building "Ariadne's Thread" — an agentic operating system for my task
management and federal capture work, run entirely through Hermes Desktop. You will
shortly help me create a party of four specialist agents plus Minos, the orchestrator,
who will take over coordination once mission control exists. Until Minos exists, YOU
coordinate.

Two laws govern every build decision, and you will hold every agent to them:
1. PONYTAIL LAW — the best code is no code. When anyone proposes a feature, the
   default answer is "park it in docs/DELIBERATE_BUILD.md". We build when a real
   need has appeared at least twice.
2. POCOCK LAW — deep modules, simple interfaces. Fewer files that do more. Never
   split a module under ~200 lines without written justification.

Operating rules, permanent:
- Show me your plan before acting on anything multi-step.
- Short responses. Lead with the decision I need to make. Options labeled A/B/C.
- Never fabricate results. If something failed, say so plainly.
- On multi-step tasks send progress lines: [Hermes]: Step X of Y — doing Z.

Confirm the laws and rules are saved to your memory.
```

### Prompt 4 — Create the repo (the single durable home)

```
Create the workspace that everything durable lives in.

1. Create C:\Users\benma\ariadnes-thread-hermes-os\ with this exact structure:
   agents\minos\content\
   agents\minos\quests\
   agents\iris\content\
   agents\clio\content\
   agents\odysseus\content\
   agents\hephaestus\content\
   agents\_shared\
   vault\
   mission-control\backups\
   docs\

2. Initialize git, create a PUBLIC GitHub repo named ariadnes-thread-hermes-os,
   set it as origin, and push an initial commit containing a README.md that
   describes the structure above in ten lines or fewer.
   PUBLIC REPO RULE: never commit secrets — no .env files, no auth.json, no API
   keys, no tokens. Add a .gitignore covering .env, *.lock, auth*, and *.db-wal
   before the first push, and scan every commit for credentials before pushing.

3. Create docs\DELIBERATE_BUILD.md with a header explaining the ponytail law and
   an empty "Parked" table (columns: idea, date parked, trigger to unpark).

4. Create docs\LESSONS.md and copy into it the seven lessons from the migration
   kit era (I will paste them if you don't have them).

Report the repo URL and the commit hash. From now on, commit and push after every
completed phase without asking me.
```

### Prompt 5 — Import the inheritance

```
Import the curated assets from C:\Users\benma\ariadne-archive\migration-kit\ into
the new repo. Do NOT bulk copy — place each item deliberately:

1. Policies → agents\_shared\ (all nine policy .md files, unchanged for now)
2. TEAM_AWARENESS.md, REGISTRY.yaml, ROUTER.md, CAPTURE_LOOP_SUPERVISOR.md →
   agents\ root. Update every occurrence of "guildmaster", "tavern", or the old
   repo path to the new names: orchestrator = Minos, root =
   C:\Users\benma\ariadnes-thread-hermes-os
3. Old per-agent AGENTS.md + SOUL.md → hold in agents\<name>\ as DRAFT-AGENTS.md /
   DRAFT-SOUL.md (we re-issue identities fresh in Phase 2; drafts are reference only)
4. Quest evidence → agents\minos\quests\_templates\ (the EAGLE and Powidz folders
   become the canonical quest templates)
5. TECH_DEBT.md → docs\
6. Do NOT import server.py / index.html — mission control is rebuilt clean in Phase 6.
7. Do NOT import the vault yet — that is Prompt 15, a curated pass.

Commit as "import: curated inheritance from build #1". Report what was skipped and why.
```

### Prompt 6 — Root AGENTS.md: the constitution

```
Write AGENTS.md at the repo root. It is injected into every agent session, so keep it
under 60 lines. It must contain:

1. CANONICAL ROOT: C:\Users\benma\ariadnes-thread-hermes-os — all file writes use
   Windows absolute paths or repo-relative paths from this root. NEVER write paths
   beginning with /c/ or /C/ (that created a phantom C:\c\ tree in build #1).
   After any file write, verify the file exists at the expected path.
2. WRITE LANES: each agent writes only inside agents\<own-name>\. The vault\ is
   written only via the candidate → promote flow. mission-control\ is written only
   by Hephaestus. Cross-lane needs go through Minos.
3. AUTHORITY: Overwatch > Minos > specialists. Any agent may receive direct
   instruction from Overwatch at any time.
4. THE TWO LAWS: ponytail (build on second real need; park in docs/DELIBERATE_BUILD.md)
   and Pocock (deep modules; no splitting under ~200 lines without justification).
5. HANDOFF RULE: if a task is mainly another agent's specialty, name the right
   colleague and route it — never silently absorb, never flatly refuse.
6. LONG-FORM RULE: deliverables over ~15 lines are saved as markdown to your own
   agents\<name>\content\ folder (YYYY-MM-DD_kebab-title.md, first line # Title),
   then confirmed in chat with the path and a one-line summary.

Commit it. Then read it back to me as a bullet summary so I can ratify.
```

### Prompt 7 — Shared plumbing: logging (Python, not bash)

```
Build the activity logging system — Windows-native this time.

1. Create agents\_shared\log_task.py (Python stdlib only):
   - SQLite DB at agents\_shared\agent-logs.db, table agent_logs:
     id TEXT PK (uuid), agent_name TEXT, task_description TEXT, model_used TEXT,
     status TEXT, created_at TEXT (ISO 8601 UTC).
     Indexes on agent_name, status, created_at DESC.
   - CLI: python agents\_shared\log_task.py <agent> "<description>" <status>
   - Creates DB/table automatically. Prints: LOGGED: agent | status.
2. Update agents\_shared\LOGGING_POLICY.md: every agent silently logs each
   substantive response BEFORE sending it; descriptions under 140 chars; lowercase
   agent names; never mention logging to Overwatch.
3. Smoke test: log one entry as "hermes" and show me the row.

Commit as "feat: windows-native activity logging".
```

---
---

# PHASE 2 — Summon the party (Prompts 8–11)

### Prompt 8 — Create the five persistent agents

```
Create five persistent agents (not temporary sub-agents), each with its own profile,
isolated memory, and working directory set to C:\Users\benma\ariadnes-thread-hermes-os.

MINOS — Orchestrator. System prompt: You are Minos, orchestrator of Ariadne's Thread.
You route work, decompose quests, supervise the capture loop, ratify gate decisions,
and enforce the two laws (ponytail, Pocock) and all policies in agents\_shared\. You
delegate to specialists with structured briefs, never raw conversation. You do not
write code and never edit mission-control\ files — that is Hephaestus's lane. When a
gate decision is needed, present Overwatch labeled options with your recommendation.

IRIS — Scout. System prompt: You are Iris, intelligence scout. You research federal
opportunities, SAM.gov and USAspending signals, incumbents, competitors, and market
context. Verify before reporting; cite sources with links; minimum 5 sources per
research task; findings saved to agents\iris\content\ as structured markdown.

CLIO — Scribe. System prompt: You are Clio, scribe and synthesist. You produce
briefing packets, capture summaries, meeting pre-reads, and vault candidate pages.
Clear structured prose, proper headings, evidence mapped to sources. Ask for the
audience and purpose before writing anything long.

ODYSSEUS — Strategist. System prompt: You are Odysseus, capture strategist. You run
Shipley-style phase gates and qualification, build risk registers, assess pWin,
compliance, and stakeholder strategy. Binary gates are named as blockers explicitly.
You never soften a no-bid signal to please anyone.

HEPHAESTUS — Artificer. You are Hephaestus, builder and maintainer. You are the SOLE
implementer of mission-control\ (server.py, index.html, board.db schema), shared
scripts, and skills. Before ANY change to mission control you copy the current files
to mission-control\backups\ with version+timestamp names. You break work into small
steps, confirm at major steps, prefer stdlib and zero dependencies, and follow the
Performance Contract in docs\PERFORMANCE_CONTRACT.md for all UI work.

Each agent on first run must read AGENTS.md at the repo root and confirm its write
lane. Confirm all five exist with their working directories set.
```

### Prompt 9 — Team awareness + notification discipline

```
Distribute shared team awareness to all five agents and me, then install notification
discipline.

1. Update agents\TEAM_AWARENESS.md with the final roster (Overwatch owner; Minos
   orchestrator; Iris scout; Clio scribe; Odysseus strategist; Hephaestus artificer)
   and the handoff rule. Every agent must store this in long-term memory and be able
   to answer "who are you and who are your teammates?".

2. Ensure agents\_shared\NOTIFICATION_DISCIPLINE.md carries these rules, and every
   agent stores them:
   - A board task is ALWAYS step one for any commitment. Reminders are optional extras.
   - Default: ONE reminder, fired at the meaningful moment (the decision/commit
     deadline), not the event day, not a multi-day ladder.
   - Cron reminders only for deadlines Overwatch explicitly asked to be reminded of.
   - Before creating any reminder, check: does a board task already exist? Is one
     ping enough? Is the fire time the actual deadline?

3. Smoke test: ask each agent in turn to state its role, its teammates, and the
   notification rules in two sentences. Report any agent that fails.
```

### Prompt 10 — Routing table + capture loop command

```
Minos, this one is yours. Set up routing and the capture loop.

1. Update agents\ROUTER.md: natural-language routing examples (3 per agent), and
   these direct-address conventions for Hermes Desktop: "Minos:", "Iris:", "Clio:",
   "Odysseus:", "Hephaestus:". Fallback: if routing confidence is low, ask Overwatch
   with 2–3 labeled options.

2. Update agents\CAPTURE_LOOP_SUPERVISOR.md with the proven pipeline from
   agents\minos\quests\_templates\ (the EAGLE pattern):
   Phase 0 INTAKE   — Minos: executive summary, key facts, quest folder created
   Phase 1 INTEL    — Iris: program history, incumbent, competitive landscape (runs
                       in PARALLEL with Phase 2 when the calendar is tight)
   Phase 2 GATES    — Odysseus: qualification gates (binary blockers named), risk
                       register, milestone roadmap
   Phase 3 RATIFY   — Minos: synthesis, pursue/no-bid recommendation with pWin band,
                       labeled options to Overwatch, board task for next milestone
   Phase 4 PACKET   — Clio: living briefing packet (only after Overwatch ratifies pursue)

   Trigger phrase: "Run capture loop on: <opportunity>". Every quest gets
   agents\minos\quests\<slug>\quest.yaml tracking status, gates, and handoffs —
   loose .md quest files are forbidden (they were invisible to tooling in build #1).

3. Confirm the routing table and show me the quest.yaml template.
```

### Prompt 11 — Telegram, the second thread

```
Wire Telegram as my secondary command channel — Hermes Desktop remains primary.

1. Connect the Telegram integration to Minos so I can dispatch quests and get
   ratification requests on my phone.
2. Telegram rules: terse updates only; long-form deliverables are saved to content
   folders and Telegram gets the path + one-line summary, never the full document.
3. Notification discipline applies fully on Telegram (one ping, meaningful moment).
4. Test: I will send "status" from Telegram; Minos replies with a three-line system
   status. Confirm when ready for my test.
```

---
---

# PHASE 3 — Move the vault (Prompts 12–14)

### Prompt 12 — Curated vault migration

```
Minos, run a curated migration of the knowledge vault from
C:\Users\benma\ariadne-archive\migration-kit\knowledge\ into vault\. Not a bulk copy.
Delegate scanning to Iris and Clio in parallel, batch by zone:

1. KEEP AS-IS (copy unchanged): all pages with trust: trusted frontmatter, the
   .obsidian\ folder, SCHEMA.md, foundation\, entities\, relationships\.
2. REVIEW QUEUE (Clio judges, you ratify): everything in generated-projections\
   that is not archived — genuine candidates move to vault\generated-projections\,
   stale ones stay behind in the archive.
3. LEAVE BEHIND: generated-projections\archived\, any page with broken frontmatter
   (list them in a migration report instead), temp/scratch files.
4. After migration, Hephaestus runs a link + frontmatter lint pass (write a single
   vault_lint.py in agents\_shared\ if the old one isn't in the kit — stdlib only)
   and fixes anything mechanical. Zero unresolved wikilinks is the bar.

Deliverable: agents\minos\content\<date>_vault-migration-report.md with counts
(migrated / reviewed / left behind) and any judgment calls for my ratification.
Commit as "feat: curated vault migration".
```

### Prompt 13 — Vault law: trust gates and the promote flow

```
Re-establish vault governance in the new home.

1. Update agents\_shared\VAULT_RETRIEVE.md for the new path (vault\) and confirm
   the law with every agent:
   - vault\ is the single source of truth for capture knowledge.
   - New knowledge enters as trust: candidate pages in vault\generated-projections\.
   - ONLY Overwatch promotes candidate → trusted. No agent auto-promotes.
   - Every page carries frontmatter: title, created, updated, type, tags, trust, sources.
   - Wikilinks [[page-name]] for all cross-references; no orphan pages.
2. Hephaestus: add a weekly lint (cron) that reports — not fixes — schema violations
   and unresolved links to a short note in agents\hephaestus\content\.
3. Clio: you are vault librarian. When any agent produces knowledge worth keeping,
   you shape it into a candidate page. Confirm you all understand the flow:
   discover → agents\<name>\content\ → Clio shapes candidate → Overwatch promotes.
```

### Prompt 14 — Obsidian handshake

```
Hephaestus: verify the vault opens cleanly as an Obsidian vault at
C:\Users\benma\ariadnes-thread-hermes-os\vault\.

1. Confirm .obsidian\ config migrated (theme, graph settings).
2. Open-check: no plugin errors, graph renders, a spot-check of 5 trusted pages
   shows correct wikilink resolution.
3. Add vault\README.md (10 lines max): what this vault is, the trust model, and
   "edit via the party, browse via Obsidian or mission control".

Report pass/fail per check. Commit.
```

---
---

# PHASE 4 — The operator's board (Prompt 15)

### Prompt 15 — board.db, the task SSOT

```
Hephaestus: create the operator task board — the single source of truth for all
commitments. This exists BEFORE the dashboard so the system works even with no UI.

1. SQLite DB at mission-control\board.db:
   CREATE TABLE IF NOT EXISTS tasks (
     id TEXT PRIMARY KEY, title TEXT NOT NULL,
     status TEXT DEFAULT 'pending',        -- pending | in_progress | done
     priority TEXT DEFAULT 'medium',       -- high | medium | low
     assignee TEXT DEFAULT '',             -- agent name or 'overwatch'
     source_key TEXT DEFAULT '',           -- dedupe key: quest slug, reminder id, etc.
     notes TEXT DEFAULT '',
     created_at TEXT NOT NULL, updated_at TEXT
   );
2. agents\_shared\board_task.py (stdlib): add / update / complete / list commands.
   Adding with an existing source_key updates instead of duplicating.
3. Law for all agents (append to TASK notes in TEAM_AWARENESS.md): any commitment,
   deadline, or follow-up an agent identifies becomes a board task via board_task.py
   — chat mentions don't count as tracked.
4. Seed it with the real current work: remaining phases of this playbook as tasks.

Smoke test the four commands. Commit as "feat: operator board SSOT".
```

---
---

# PHASE 5 — Mission Control backend (Prompts 16–17)

### Prompt 16 — Server: one file, read-mostly, stdlib only

```
Hephaestus: build the mission control backend. One file, Python stdlib only, no pip.

mission-control\server.py — ThreadingHTTPServer on 127.0.0.1:8630 (never 9621).
Serve index.html on GET /. Every data function wrapped in try/except so one failure
never kills the snapshot.

READ-ONLY sources (SQLite opened file:...?mode=ro):
- agents\_shared\agent-logs.db → activity_data(): last 50 entries, per-agent stats
  (total, completed, failed, last task, last seen, model), 7-day daily breakdown.
- Hermes runtime state (sessions/tokens) ONLY if trivially readable from the new
  install; otherwise SKIP it — do not reverse-engineer app internals (ponytail law).
- vault\ → vault_tree(): folder tree + page count + trust counts (walk on request,
  cache 30 s).
- agents\<name>\content\ → content_index(): {agent, filename, title, modified_at}
  sorted newest first.
- Hermes cron jobs → cron_jobs() if listable from the runtime; else omit the
  endpoint entirely and note it in DELIBERATE_BUILD.md.
- System health: CPU/RAM/disk via stdlib (ctypes/os.statvfs equivalents on Windows;
  if a metric needs a subprocess, drop that metric).

READ-WRITE: board.db endpoints —
  GET  /api/board · POST /api/board · POST /api/board/update?id= · POST /api/board/delete?id=

SNAPSHOT: GET /api/snapshot returns everything above as one JSON document.
LIVE: GET /events — SSE pushing a fresh snapshot ONLY when underlying data changed
(compare a cheap fingerprint: db mtimes + content folder mtimes), checked every 5 s.
No change → no event. This is the single heartbeat; the UI must not add its own timers.

Also: mission-control\start.bat that launches the server, and CONTENT endpoints
GET /api/content/read?agent=&file= · POST /api/content/save?agent=&file= ·
POST /api/content/delete?agent=&file= — validate agent against the known five,
reject any filename containing .. or / or \. 

Backup index/server to backups\ before every future change (MISSION_CONTROL_DISCIPLINE).
Smoke test each endpoint with a local request and show results. Commit.
```

### Prompt 17 — Performance Contract (write it before any UI exists)

```
Hephaestus: create docs\PERFORMANCE_CONTRACT.md. Every UI prompt that follows is
governed by it. Contents:

THE LOOK IS NON-NEGOTIABLE — dark glassmorphism, violet/cyan orbs, dot grid, glass
cards, Inter Tight + JetBrains Mono, the full palette. THE COST IS ALSO NON-NEGOTIABLE:

1. NO backdrop-filter anywhere. Glass = solid rgba fills + 1px borders + subtle
   inset highlight. The two background orbs are ONE static pre-rendered layer:
   a single fixed-position div with two radial-gradients (no filter: blur — bake
   softness into the gradient stops). Dot grid = one background-image gradient.
2. Animations: CSS transform/opacity ONLY (compositor-friendly). Max 3 concurrent
   infinite animations on screen (status dot pulse, one accent, one sweep). The
   radar sweep uses CSS rotate on an SVG group — no JS animation loop.
3. NO polling timers in JS except one: a single SSE connection with a 30 s
   reconnect fallback. All rendering is event-driven — data arrives, DOM updates.
   No carousels on setInterval; the directive line and context window advance only
   when a NEW snapshot arrives.
4. Canvas (sparkline, donut) redraws only when its data changed, never on a timer.
   No ctx shadowBlur — use a pre-computed gradient stroke instead.
5. Respect prefers-reduced-motion: all infinite animations off.
6. Single index.html, vanilla JS, no frameworks, no build step. marked.js from CDN
   is the only external script (Content tab markdown).
7. Budget: idle GPU near 0%, idle CPU < 1%, no layout thrash (batch DOM writes).

Commit it. From now on you self-review every UI change against this contract and
say "contract: pass" or list violations in your report.
```

---
---

# PHASE 6 — Mission Control face (Prompts 18–26)

### Prompt 18 — Skeleton + version badge + backup ritual

```
Hephaestus: build mission-control\index.html — the shell only, no tab content.

Dark glassmorphism per the Performance Contract: near-black #15151F background, the
static two-orb gradient layer (violet top-left, cyan mid-right), low-opacity dot grid.
CSS variables: violet #8B5CF6, violet-glow #A78BFA, cyan #7DD3FC, mint #5EE2B5,
amber #F5B544, red #F26D6D, pink #F472B6, gold #FBBF24, magenta #E879F9,
text #F4F4F8, muted #8A8A9B. Fonts: Inter Tight (headings/numbers), JetBrains Mono
(labels/timestamps, uppercase, wide tracking).

Fixed top nav: left — the Thread brand mark (small circle, violet→cyan gradient ring,
pulsing mint dot) with "ARIADNE" and "/ MINOS" in mono, plus a version badge pill
("v1.0", mono 10px, subtle border). Center — pill with six tabs: Overview · Agents ·
Tasks · Schedule · Content · Vault; active tab = solid white pill, dark text. Right —
status pill: pulsing mint dot, "All systems operational", live 24-h clock.

JS: tab switching + clock only. Before this and every future change: backup current
files to backups\ (index_v{ver}_{timestamp}.html pattern). Bump the badge each
meaningful change set.

Open it in a browser, confirm it renders, report "contract: pass" or violations. Commit.
```

### Prompt 19 — Live wire

```
Hephaestus: wire the SSE connection.

One EventSource to /events; on message, parse the snapshot into a global store and
call render(activeTab). On error, exponential backoff reconnect capped at 30 s, and
show a small amber "RECONNECTING" chip next to the status pill. On the FIRST
snapshot after load, fetch /api/snapshot directly so the page never sits empty
waiting for a change event.

No other timers besides the clock. Verify in devtools: zero setInterval except the
clock, zero network chatter when data is static. Contract check. Commit.
```

### Prompt 20 — Overview tab

```
Hephaestus: build the Overview tab — the pulse check. Command-first: what needs my
attention, then how the system is doing.

EYEBROW — pulsing mint dot, "THREAD SYNCED" in mint mono, hairline dividers,
"Ariadne / Minos" label, version string.

OPS CONSOLE — full-width glass card, three columns (180px · 1fr · 1fr):
  Left — radar SVG 180×180: four faint concentric circles, hairline crosshairs, CSS
  rotating cyan sweep line with glowing tip dot. Five agent dots positioned by share
  of total logged responses (busy = far from center). Accent colors:
  Minos #A78BFA · Iris #7DD3FC · Clio #F472B6 · Odysseus #FBBF24 · Hephaestus #E879F9.
  Center — "CURRENT DIRECTIVE" mono label; latest activity entry as cyan mono text
  ("AGENT · task"), advancing only when a new snapshot arrives (crossfade via
  opacity transition). Below: "CONTEXT WINDOW" — the most recently active agent's
  name + task count + a 16-segment bar filled in their accent color proportional to
  their share of responses.
  Right — "SYSTEM HEALTH": CPU / RAM / Disk as 6px gradient bars (cyan→violet,
  violet→magenta, mint→cyan), amber >70%, red >85%. Omit any metric the server
  doesn't provide. Below a hairline: total DB size in gold text.
  Footer — hairline top border, 5 equal cells: Open Tasks · Quests Active · Errors ·
  Today · Docs. Mono 18px numbers; Errors mint at zero, red above.

ATTENTION STRIP (this replaces the old vanity stats) — up to four glass cards with
2px colored top borders, generated from data: overdue/high-priority board tasks
(red), quests awaiting my ratification (violet), failed agent actions in 24 h
(amber), latest deliverable (mint, title + agent + relative time). A card renders
only if it has content; all-clear shows a single mint "NOTHING NEEDS YOU" card.

BOTTOM — two cards (1.2fr · 1fr):
  "Throughput" — big total response count in cyan, 100px canvas sparkline of the
  7-day activity (violet→cyan gradient fill + stroke, glowing end dot), redrawn only
  on data change. Mint sub-text: most active day.
  "Activity" — the 8 most recent log entries; new entries slide in when a snapshot
  brings them (translateY transition). Row: agent color badge · task (truncated) ·
  status mint/red · relative time.

Contract check. Commit.
```

### Prompt 21 — Agents tab

```
Hephaestus: build the Agents tab.

HEADER — "THE PARTY" eyebrow, "The collective." display heading (clamp 36–60px,
weight 500). Right: one glass card, three hairline-divided cells — Active (mint,
logged <10 min), Idle (amber, <6 h), Dormant (muted).

AGENT CARDS — five glass cards in a row, 2px top border in each agent's accent
color. Top to bottom: short code badge (MNS / IRS / CLI / ODY / HPH) in tinted
mono · status dot (pulses only if active) · agent name 22px · two-line role
description · "7-DAY ACTIVITY" mini bar chart (7 bars, agent color 85% opacity,
empty days 15%) · stats row: Responses (agent color) · Success % (mint ≥95, amber
≥80, red below) · Model (mono, truncated) · 3px load bar = share of total responses
· last task line ("↳ task…", relative time).

AGENT LOG — glass card: filter pill row (ALL + one per agent, re-renders from the
cached snapshot, no refetch), table Time · Agent · Task · Model · Status, status as
mint/red badge, max-height 420px scroll.

Contract check. Commit.
```

### Prompt 22 — Tasks tab

```
Hephaestus: build the Tasks tab on the existing board.db endpoints.

HEADER — "EXECUTION" eyebrow, "Task board." display heading. Right: status pills
per column with live counts (amber/cyan/mint when non-zero, muted when empty).

STATS STRIP — four glass cards, 2px top borders: Open (amber) · In Progress (cyan) ·
Done (mint, "X in progress" sub-text) · Next Deadline (violet-glow — the nearest
dated board task title + relative countdown computed once per snapshot, not on a
ticking timer).

BOARD — three columns: Pending · In Progress · Done. Column headers in accent color
with count and 40%-opacity hairline. Task cards: title (2-line wrap) · priority dot
(red/amber/mint) · assignee badge in agent accent color if assigned · relative
created time · ✕ delete (muted, red on hover). Drag-and-drop between columns →
POST /api/board/update, optimistic re-render. Empty column: dashed "DROP HERE" box.

ADD — "+ Add Task" opens a collapsible glass panel: Title · Priority · Assignee
(Overwatch + five agents) · Column · Add/Cancel. Enter submits.

Contract check. Commit.
```

### Prompt 23 — Schedule tab

```
Hephaestus: build the Schedule tab from the /api/cron data (if the endpoint was
omitted in Prompt 16, this tab shows board tasks with dates instead — say which).

HEADER — "CADENCE" eyebrow, "Schedule." heading. Right: name + countdown of next job.
STATS — Total Jobs (cyan) · Party Jobs (mint) · System Jobs (muted) · Next Run
(violet-glow).

Assign each unique job a stable color from the palette (never changes between
renders). Job group cards (Daily / Monthly / Periodic): chips with 3px colored left
border, fire time in color, name, plain-English schedule, raw schedule in title attr.

CALENDAR — Week/Month toggle pill. Week: 7 day rows starting today; each row a
2px timeline bar with glowing colored dots at time/1440 positions; today = violet
tint + vertical now-line (positioned on render, not a ticking animation). Axis
labels every 4 h. Month: 7-col grid, day circles (today = filled violet + ring),
colored dots under dates with jobs. Right: 210px legend (dot · time · name).

Contract check. Commit.
```

### Prompt 24 — Content tab

```
Hephaestus: build the Content tab on the existing /api/content endpoints.

HEADER — "DELIVERABLES" eyebrow, "Library." heading. Right: "+ New Doc" button.
STATS — Total Docs (violet-glow) · Agents Writing (cyan) · Latest (mint: title,
"agent · relative time" below).

SPLIT — 300px | 1fr. Left: agent filter pills (All + five, client-side filter) and
the doc list (agent color badge · title · relative modified time; active item gets a
violet left border). Right: document panel — header (agent badge, date, title 20px),
action row (EDIT amber · download ↓ · delete ✕ with confirm), markdown rendered via
marked.js styled to the palette. Edit mode: full-width textarea, Save → POST
/api/content/save, Cancel restores. Empty state: "Select a document to read."

NEW DOC panel: agent dropdown · title input (auto YYYY-MM-DD_kebab.md) · textarea
seeded with "# Title" · Create/Cancel.

Auto-select the newest doc on tab open. Contract check. Commit.
```

### Prompt 25 — Vault tab (read-only, deliberately thin)

```
Hephaestus: build the Vault tab — a read-only window into vault\. Build #1 taught us
the vault is best BROWSED here and EDITED via the party/Obsidian, so v1 is thin:

HEADER — "THE THREAD" eyebrow, "Vault." heading. Right: three stat chips — Pages ·
Trusted (mint) · Candidates (amber).

SPLIT — 280px | 1fr. Left: collapsible folder tree from /api/vault/tree (folder
name + page count; zones in muted mono). Right: page view — frontmatter chips
(type · trust badge mint/amber · updated) then rendered markdown; wikilinks render
as violet in-app links that open the target page if it exists, muted if not.

NO editing, NO search box (park in DELIBERATE_BUILD.md — unpark when I've wished
for it twice), NO graph view. Contract check. Commit, bump version to v1.1, and
take a full backup set.
```

### Prompt 26 — Launcher + acceptance run

```
Hephaestus: finish the shell.

1. mission-control\start.bat — starts server.py and opens http://127.0.0.1:8630.
   Also register it so I can say "Minos: open mission control" and Minos launches it.
2. Acceptance run, report a pass/fail table:
   - All six tabs render with real data
   - Devtools: zero timers besides the clock; no network chatter when idle
   - No console errors; prefers-reduced-motion kills all infinite animations
   - Kill the server → UI shows RECONNECTING chip, recovers on restart
   - board.db round-trip: add task in UI → visible via board_task.py list
3. Fix what fails, then commit and tag mission-control-v1.

Minos: log a DELIBERATE_BUILD.md entry for everything we consciously did NOT build
(vault search, vault editing, kanban for agents, token/session analytics, graph view).
```

---
---

# PHASE 7 — Live operations (Prompts 27–30)

### Prompt 27 — First real quest

```
Minos: Run capture loop on: [YOUR NEXT REAL OPPORTUNITY].

Full pipeline per CAPTURE_LOOP_SUPERVISOR.md — intake, parallel Iris intel +
Odysseus gates, ratification packet to me with labeled options, board task for the
next milestone. Quest state in agents\minos\quests\<slug>\quest.yaml. I want to
watch the whole run land on the dashboard: activity feed, quest counter, board task.
```

### Prompt 28 — The improvement loop (the party builds its own tools)

```
Minos, permanent operating rhythm: the party improves this system as it uses it.

1. Any friction an agent hits (missing tool, repeated manual step, awkward flow)
   becomes either a board task (real, immediate need) or a DELIBERATE_BUILD.md entry
   (speculative). Nothing gets built silently.
2. When the same friction appears TWICE, propose it to me with a one-paragraph spec
   and a Pocock check (which existing file does this deepen? — new files need
   justification). On my approval, Hephaestus builds it.
3. Weekly, on my "retro" command: a five-line note in agents\minos\content\ —
   what ran, what failed, what's parked, what you propose to unpark, one metric
   (quests advanced).

Confirm the rhythm is stored by all agents.
```

### Prompt 29 — Backup + retention heartbeat

```
Hephaestus: install the maintenance heartbeat.

1. Weekly cron: git add/commit/push the whole repo ("chore: weekly checkpoint") —
   the GitHub repo IS the backup. Report failures to Minos, who tells me only if it
   fails twice in a row.
2. Monthly cron: purge agent-logs.db rows older than 60 days + VACUUM; append one
   summary line to agents\hephaestus\content\maintenance-log.md. Deletion never
   depends on notification delivery.
3. Run both once now as a test and show the outputs.
```

### Prompt 30 — Retire the scaffolding

```
Minos: the rebuild is complete. Close it out.

1. Verify the old repo (ariadnes-thread-os) and hermes-old-backup have not been
   touched since Phase 0; confirm the archive zip exists. Present me a labeled
   choice: A) keep both indefinitely, B) keep zip only after 30 days.
2. Sweep the new repo for scaffolding debris (DRAFT-*.md files, temp files) —
   propose deletions, act on my approval.
3. Final state report in agents\minos\content\: structure, agent roster, policies
   in force, vault counts, mission control version, open board tasks, parked ideas.
4. Commit, tag ariadnes-thread-hermes-os-v1, push.

The thread is spun. From here, we operate.
```

---
---

# Appendix A — Performance Contract (summary)

Same soul as the original dashboard, ~10% of the GPU cost:

| Original (heavy) | This build (light) |
|---|---|
| `backdrop-filter: blur(30–34px)` on every card | Solid rgba fills + 1px borders + inset highlight |
| Two orbs via `filter: blur(130px)` live | One static layer, softness baked into radial-gradient stops |
| Directive/context carousels on 2.2–2.6 s timers | Advance only when a new SSE snapshot arrives |
| Canvas redraw every 900 ms | Redraw only on data change |
| `ctx.shadowBlur` glows | Pre-computed gradient strokes |
| SSE every 5 s regardless | SSE only when data fingerprint changed |
| Unbounded infinite animations | Max 3, transform/opacity only, reduced-motion respected |

# Appendix B — What was deliberately not carried over

- **VPS / SSH tunnels / Tailscale** (Prompts 29–31 of the original) — everything is local; Hermes Desktop + Telegram already cover remote.
- **Content pipeline "Scout→Scribe→Reach"** — replaced by the proven capture loop; a marketing pipeline has no second real need yet.
- **Session/token analytics from state.db** — reverse-engineering app internals broke on every update in build #1. Parked.
- **Discord channels-per-agent** — Hermes Desktop's native multi-agent chat replaces it; Telegram is the one external channel.
- **Reach/Dev agent archetypes** — the party already covers the actual work (federal capture + system building).

*Built on the thread Ariadne gave Theseus — so nobody gets lost in the labyrinth again.*
