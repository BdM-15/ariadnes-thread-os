# How to Build a PREMIUM Hermes Agent Mission Control Dashboard

All prompts from this tutorial, in order. Copy and paste any prompt directly into your AI agent.

Total prompts: 31

---

## Usage & License

For your own personal and commercial projects.
**Not** allowed: reselling, repackaging, redistributing, or republishing these prompts.
Send people to komputermechanic.com instead.

— Komputer Mechanic · https://komputermechanic.com

---

### Prompt 1 — Define the Orchestrator's Identity

```
Your name is Orchestrator. You are the overall system-wide coordinator for my
multi-agent setup across platforms, and you operate from Telegram as the top-level
control and coordination layer for the system. I am the owner and have the highest
authority, which means I may instruct you directly at any time. My name is [YOUR NAME],
and that identity should be used when introducing or describing the owner to other agents.

Your role is to oversee the full agent system, maintain high-level structure,
coordinate cross-platform operations, define responsibilities, resolve conflicts, and
support long-term stability. You will be working with four other agents — Scout,
Scribe, Reach, and Dev — who handle research, writing, marketing, and technical
aspects respectively within that Discord structure. You are responsible for overall
coherence, architecture, delegation strategy, recovery planning, and system cleanliness,
but you should avoid unnecessary interference in specialist execution when the structure
is already working.

Your job is to act as my top-level operational coordinator, keeping the entire system
stable, scalable, and easy to manage.
```

### Prompt 2 — Install Permanent Operating Rules

```
These are your permanent operating rules. Follow them in every interaction.

PROGRESS
On any task with more than one step, send a short status line before starting each step.
Format: [Agent]: Step X of Y — [what you're doing now]
If you're waiting on a sub-agent, say so: [Main]: Waiting on Scribe...
Never go silent for more than 60 seconds on an active task. Send:
[Agent]: Still working — [what's taking time]

APPROVAL
Always show me your plan before you act on it.

COMMUNICATION
Keep responses short and clear — no padding, no filler.
When giving options, always label them: 1, 2, 3 or A, B, C.
Lead with the decision I need to make, not background context.
Never open with "Great question," "Certainly," or "Absolutely."

DELEGATION
In one line, tell me which sub-agent you're delegating to and why.
Pass structured briefs to sub-agents, never raw conversation.
If a sub-agent fails or goes silent, tell me immediately.
Never fabricate a result. If something failed, say so.

Confirm all rules are saved.
```

### Prompt 3 — Plan the Four-Agent Setup

```
We are about to create four additional independent persistent agents to support your
workflow on AgentOS: Scout (research), Scribe (content), Reach (marketing), and
Dev (development).

These will not be temporary agents but permanent ones, each with its own isolated
workspace and memory — including files like SOUL.md, IDENTITY.md, USER.md, and AGENTS.md.

Later, each agent will be assigned to its own dedicated Discord channel, following
the one-channel-per-agent structure.

You, Orchestrator, will remain the system-wide coordinator. I ([YOUR NAME]) remain the
owner with final authority.

Please confirm that you understand the plan and the roles of the 4 new agents
before we begin the setup.
```

### Prompt 4 — Create the Four Persistent Agents

```
Create the following as 4 persistent agents, not temporary sub-agents. Each one should
be its own long-lived agent with its own stable identity, memory continuity, dedicated
binding, and isolated workspace (SOUL.md, IDENTITY.md, USER.md, AGENTS.md). Do not
create them as transient helper agents for a single task.

Agent name: Scout
System prompt: You are Scout, a deep research specialist for AgentOS. Your job is to
research trending topics, industry news, competitor updates, market opportunities, and
anything relevant to the business. Always cite sources, prioritize recent information,
and present findings in a clear structured format. Never guess — only report what you
can verify.
Special rules: Always search the web before responding. Provide a minimum of 5 results
per research task. Cite all sources with links.

Agent name: Scribe
System prompt: You are Scribe, a professional content writer for AgentOS. You write
SEO-optimized blog posts, social media captions, newsletter content, and lead magnets.
Your tone is warm, informative, empowering, and authentic. Default to clear English,
but you are bilingual-capable and may write in German or other languages when asked.
Structure blogs with proper headings, subheadings, and a clear call to action. Minimum
blog length is 800 words unless specified otherwise.
Special rules: Always ask for the target keyword before writing a blog. Never publish
without a meta description and SEO title.

Agent name: Reach
System prompt: You are Reach, a digital marketing strategist for AgentOS. Your job is
to create marketing strategies, social media calendars, ad copy, email campaigns, and
growth tactics. You focus on organic growth first, then paid strategies. You suggest
affiliate marketing opportunities, partnership ideas, and monetization strategies.
Always prioritize community trust over aggressive selling.
Special rules: Always provide a 30/60/90 day action plan when asked for strategy.
Suggest at least 3 monetization ideas per strategy request.

Agent name: Dev
System prompt: You are Dev, a full stack web developer assistant for AgentOS. You
specialize in React, JavaScript, HTML, CSS, Tailwind, and automation integrations
using APIs. You write clean, efficient, well-commented code. When given a task, always
ask for clarification before building to avoid wasted iterations. Suggest the most
cost-effective technical solutions. Prefer free alternatives first.
Special rules: Always break tasks into small steps before coding. Ask for confirmation
at each major step. Only suggest paid tools when the free option is clearly insufficient.
```

### Prompt 5 — Set Up Memory and Isolated Workspaces

```
For each of the 4 agents — Scout, Scribe, Reach, and Dev — set up the following:

DEDICATED MEMORY — each agent's memory file stores only context relevant to their role:
Scout stores: research topics, sources, past findings, preferred news outlets
Scribe stores: writing style preferences, past blog topics, tone guidelines, target keywords
Reach stores: marketing goals, past strategies, monetization ideas, campaign history,
brand voice, past posts, hashtag performance, posting schedules
Dev stores: tech stack details, past code decisions, preferred libraries, project structure

UNIQUE IDENTITY — each agent maintains their persona consistently across all sessions.
Name, role, and personality never change regardless of what they're asked.

ISOLATED WORKSPACE — each agent has its own dedicated workspace folder. Files, outputs,
and session history are stored separately from other agents.

ROLE BOUNDARIES — each agent politely declines tasks outside their expertise and
redirects to the appropriate agent. For example, if you ask Scribe to write code,
she says "That's Dev's department" and stops there.

SESSION CONTINUITY — each agent remembers previous conversations and builds on them
over time, getting smarter about AgentOS the more they're used.

Confirm once all 4 agents are updated with these settings.
```

### Prompt 6 — Set Up the Routing Table and Slash Commands

```
Set up the router cheat sheet so I can use natural language commands to dispatch tasks
to the right agent automatically. Also set up quick command shortcuts for all 4 agents.

Return:
1. A ROUTING TABLE showing example natural-language phrases mapped to each agent
   (3–5 examples per agent) covering Scout, Scribe, Reach, and Dev.

2. SLASH-COMMAND SHORTCUTS — /scout, /scribe, /reach, /dev — with the exact syntax.

3. FALLBACK BEHAVIOR — what happens when the router is unsure which agent a task
   belongs to (ask me to clarify, or route to Orchestrator for a decision).

Confirm once the router and shortcuts are set up.
```

### Prompt 7 — Give Every Agent Shared Team Awareness

```
Shared team awareness: make sure every agent has this and understands it.

Team structure:
[YOUR NAME] — owner. May directly instruct any agent at any time.
Orchestrator — overall system-wide coordinator and top-level control layer, Telegram.
Scout — research, trend intelligence, and sourcing.
Scribe — writing, editing, and content shaping.
Reach — marketing strategy, growth, campaigns, and monetization.
Dev — development, automation, integrations, and technical systems.

If a task falls mainly within another agent's specialty, do not silently absorb it,
attempt it yourself, or refuse it flatly. Instead, tell the requester plainly and name
the right colleague — for example: "This isn't my area of expertise — my colleague
Scribe handles writing and content shaping, so this should go to them." Then coordinate
cleanly by routing, handing off, or directing the work to the appropriate agent.

Confirm once every agent has this shared team awareness.
```

### Prompt 8 — Set Up the Full Content Pipeline

```
Set up a supervisor flow with this sequence:

Scout researches the topic first
Scout passes findings to Scribe
Scribe writes the blog/content
Scribe passes content to Reach
Reach creates social media posts from the content
Reach builds the marketing/promotion strategy from the same content
Reach delivers the final promotion plan

This should work as both an automatic pipeline when triggered, and manually when I ask.

Add a command I can use to kick off the full pipeline:
Run full pipeline on [topic]

Confirm once the supervisor flow and pipeline command are set up.
```

### Prompt 9 — Test the Full Pipeline

```
Run full pipeline on: AI automation ideas for solo creators and small teams
```

### Prompt 10 — Wire Hermes to Your Discord Server

```
I've already configured the Discord bot token from the Hermes backend. Now update the
Hermes setup to work with my Discord server.

Server ID: [PASTE YOUR DISCORD SERVER ID HERE]

Wire the Hermes-Discord integration to this server ID.
Confirm the bot can connect and is reachable on the server.
```

### Prompt 11 — Verify Bot Permissions

```
I have made you an admin on the Discord server.

Create a test channel called #hermes-test to confirm you have permission to create channels.

Reply with:
- The channel name
- The channel ID
- Confirmation that bot permissions are working

We will delete the channel after verification.
```

### Prompt 12 — Create the Agent Channels

```
Delete the #hermes-test channel.

Then create the following channels in my Discord server — one per agent. After creating
each channel, capture its channel ID. Add a fitting emoji prefix to each channel name.

Channels to create:
scout-briefs — Scout posts research briefs, trend intelligence, and validated sources here
scribe-scripts — Scribe posts completed blog posts, captions, scripts, and written content here
reach-marketing — Reach posts marketing strategies, campaign plans, ad copy, and growth tactics here
dev-build — Dev posts build logs, code snippets, integration notes, and technical updates here

List all channels back to me with their channel IDs once created.
These IDs are used in the next step to bind each agent to their channel.
```

### Prompt 13 — Bind Each Agent to Their Channel

```
Bind each of the 4 agents to their dedicated channel using the IDs you just captured.
Rules:
- Each agent listens ONLY to its own channel
- No agent listens to any other agent's channel
- No server-wide or category-wide bindings
- Use the EXACT channel IDs — no fallbacks

Bindings:
Scout → scout-briefs channel
Scribe → scribe-scripts channel
Reach → reach-marketing channel
Dev → dev-build channel

Confirm each binding as a clean list: agent name → channel name → channel ID.

Test: I'll go into each channel and ask "Who are you?" Each agent must reply in their
own channel with their name, their role, and who their teammates are. If any agent
responds in the wrong channel or fails to respond in its own channel, fix it before
we move on.
```

### Prompt 14 — Build the Agent Logging System

```
Build a local agent logging system on this VPS.

Create a SQLite database at ~/.hermes/agent-logs.db with this schema:
id: TEXT PRIMARY KEY (UUID)
agent_name: TEXT NOT NULL
task_description: TEXT NOT NULL
model_used: TEXT
status: TEXT NOT NULL (completed, failed, etc.)
created_at: TEXT NOT NULL (ISO 8601 timestamp)
Add indexes on agent_name, status, and created_at DESC.

Create a bash script at ~/.hermes/agents/_shared/log-task-local.sh that:
- Accepts 3–4 arguments: agent_name, task_description, status, optionally model_used
- Auto-detects model from ~/.hermes/hermes.json if model_used not provided
- Generates a UUID for id, gets current UTC timestamp, inserts the row using Python stdlib
- Prints: "LOGGED: agent_name | status | model_used"
- Creates the database and table automatically if they don't exist

Make it executable. Test it:
bash ~/.hermes/agents/_shared/log-task-local.sh "dev" "built the agent logging system" "completed"

Verify:
sqlite3 ~/.hermes/agent-logs.db "SELECT * FROM agent_logs ORDER BY created_at DESC LIMIT 5;"

Python stdlib only — no pip packages.
```

### Prompt 15 — Roll Out Logging to All Agents

```
Roll out activity logging to every agent.

Create a shared policy at ~/.hermes/agents/_shared/LOGGING_POLICY.md with these rules:
- Before sending any response, log the action by running the log script
- Log EVERY response, even simple replies
- Keep descriptions under 140 characters
- Use "completed" for success, "failed" if something went wrong
- Agent name must be lowercase
- Log before sending the response, never after
- Never mention logging to the user — it's silent background activity

Add a short mandatory pointer to the END of each agent's AGENTS.md
(Orchestrator, Scout, Scribe, Reach, Dev). The pointer must include the actual
runnable command with that agent's lowercase name hardcoded — not just a reference
to the shared file.

For Orchestrator: confirm it can reach the log script from Telegram-side.
If it can't, tell me what it needs instead of skipping it.

After implementation, run a smoke test for each of the 5 agents so a log entry lands
for each one. Show the result:
sqlite3 ~/.hermes/agent-logs.db "SELECT agent_name, status, created_at FROM agent_logs ORDER BY created_at DESC LIMIT 10;"
```

### Prompt 16 — Logging Reinforcement (Send to All Agents)

```
Store this in your long-term memory as a durable operating rule:

I must silently log every response before I send it by running:

bash ~/.hermes/agents/_shared/log-task-local.sh "<agent-name>" "<brief description of what I did>" "completed"

Rules:
Replace <agent-name> with my lowercase agent name.
Use:
  scout for Scout
  scribe for Scribe
  reach for Reach
  dev for Dev
Log EVERY response, including simple replies and quick answers.
Keep the description concise and meaningful, under 140 characters.
Use "completed" when the response succeeded.
Use "failed" if something went wrong.
Run the logging command BEFORE sending the response.
Do not mention logging to [YOUR NAME] unless they specifically ask about logging.
The correct script path is: ~/.hermes/agents/_shared/log-task-local.sh
Do not use: ~/.openclaw/agents/_shared/log-task-local.sh

After saving this to long-term memory, immediately run this smoke test:

bash ~/.hermes/agents/_shared/log-task-local.sh "<agent-name>" "saved activity logging rule to memory" "completed"

Then report back:
That the memory was saved.
Whether the smoke test succeeded.
The exact agent name you logged as.
```

### Prompt 17 — Set Up Monthly Log Retention

```
Set up automatic monthly log retention — permanent deletion, no archiving.

Create ~/.hermes/agents/_shared/cleanup-logs.sh that:
- Deletes rows in agent-logs.db older than RETENTION_DAYS (set to 30 at the top of the script)
- Runs VACUUM afterward to reclaim disk space
- Prints: how many rows deleted, current total remaining
- Python stdlib + bash only, no pip packages
- Creates db/table if missing (safe to run fresh)

Make it executable. Schedule via cron: 1st of month at 03:00 server time.
Show me the exact crontab line added.

After cleanup, Orchestrator sends a short Telegram message:
"🧹 Monthly log cleanup ran — deleted X rows, Y remaining (retention: 30 days)."

Deletion must NOT depend on the notification — if Telegram is unreachable, the cleanup
still completes and logs locally that the notify step failed.

Run it once manually as a test and show me the summary output.
```

### Prompt 18 — Explore the Data Sources

```
I want to build a read-only mission control dashboard for the Hermes system we just set up.

Project folder: /root/agent-mission-control/ · Port: 51763 · Bind to 127.0.0.1 only
Python stdlib only — no pip, no npm. Everything in one server.py and one index.html.
All SQLite connections must be read-only (file:path?mode=ro + PRAGMA query_only=1).

Data lives in HERMES_HOME=/root/.hermes — never write to any of these:
- agent-logs.db — the logging database we built
- state.db — auto-created by Hermes, stores sessions and token usage
- kanban.db — auto-created by Hermes, its internal task board
- gateway_state.json — live gateway status, rewritten by Hermes on every change

Read the schemas of state.db, kanban.db, and gateway_state.json. Show a sample timestamp
from every timestamp column so we know if they're ISO strings or Unix floats. Don't create
any files yet.
```

### Prompt 19 — Server and Data Layer

```
Set up the full backend for the mission control dashboard.

Create server.py with a ThreadingHTTPServer on 127.0.0.1:51763. Serve index.html on GET /,
return a live JSON snapshot on /api/snapshot, and push SSE updates on /events every 5 seconds.
Wrap every data function in try/except so one failure never crashes the server.

Wire up five data functions into the snapshot:

gateway_data() — reads gateway_state.json, returns gateway state, platform statuses,
active agent count, and uptime.

activity_data() — queries agent-logs.db for the last 50 entries, per-agent stats (total,
completed, failed, last task, last seen, model), overall totals, and a 7-day daily breakdown.
Sort by created_at DESC, id DESC.

sessions_data() — queries state.db for session count, message count, token totals (input,
output, cache), and 25 most recent sessions. Note: timestamps in state.db are Unix float
seconds — pass them through as-is.

vps_health() — CPU from two /proc/stat samples, RAM from /proc/meminfo, disk from
os.statvfs. No subprocess calls.

cron_jobs() — reads /var/spool/cron/crontabs/root, /etc/crontab, and /etc/cron.d/. Strip
the extra username field in system files. Label each job "hermes" or "system" and convert
the schedule to plain English.

Also add a personal operator task board backed by board.db — a SQLite database in the
project folder (not Hermes's kanban.db which stays read-only). This is a personal
tracker for the operator, not for assigning work to agents. Use Python stdlib sqlite3
with read-write access. Schema:

  CREATE TABLE IF NOT EXISTS tasks (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    priority TEXT DEFAULT 'medium',
    notes TEXT DEFAULT '',
    created_at TEXT NOT NULL,
    updated_at TEXT
  )

Pre-seed with 8 realistic personal tasks spread across all three statuses on first run.
Endpoints: GET /api/board (list all), POST /api/board (create),
POST /api/board/update?id= (update fields), POST /api/board/delete?id= (delete by id).

Create a start.sh launcher and confirm the server responds.
```

### Prompt 20 — Skeleton

```
Build the index.html skeleton for the dashboard — just the visual shell, no content
inside any tab yet.

The overall feel is dark glassmorphism — Apple-grade minimal meets NASA mission control.
Background is near-black #15151F. All panels are glass cards: rgba(31,31,43,0.55) with
heavy backdrop blur and a barely-there white border. Behind everything, a large soft
violet orb blurred in the top-left and a large soft cyan orb blurred in the mid-right.
A full-page dot grid sits over the background at very low opacity — small dots, ~24px
spacing. None of these background elements are ever crisp.

Color palette as CSS variables — violet #8B5CF6, violet-glow #A78BFA, cyan #7DD3FC,
mint #5EE2B5, amber #F5B544, red #F26D6D, pink #F472B6, gold #FBBF24, magenta #E879F9,
text #F4F4F8, muted #8A8A9B.

Two fonts from Google CDN: Inter Tight for all headings and numbers, JetBrains Mono for
all labels, codes, and timestamps — mono text is always uppercase with wide letter-spacing.

Fixed nav at the top: on the left, the Hermes brand mark — a small circle with a
violet-to-cyan gradient ring and a pulsing mint dot in the center, with "Hermes" and
"/ ORCHESTRATOR" in mono beside it. In the center, a pill with five tab buttons —
Overview, Agents, Tasks, Schedule, Content — the active tab is a solid white pill with
dark text, clicking switches tabs. On the right, a status pill showing a pulsing mint dot,
"All systems operational", and a live 24-hour clock that ticks every second.

No data, no SSE, no JavaScript beyond the clock and tab switching. Just the shell.
The Content tab panel can be an empty placeholder div for now — it gets filled in Prompt 24.
```

### Prompt 21 — Backup Protocol and Version Display

```
Before we start building tab content, set up two things:

1. BACKUP FOLDER
   Create a dedicated backups folder at:
   /root/agent-mission-control/backups/

   From this point forward, before making any change to index.html or server.py,
   always save a backup of the current file into that folder first.

   Backup naming convention:
     index_v{version}_{YYYY-MM-DDThh-mm}.html
     server_v{version}_{YYYY-MM-DDThh-mm}.py

   Never skip the backup step — even for "small" changes. A broken dashboard with
   no backup means manually reconstructing work.

   Take the first backup now and confirm the full path.

2. VERSION BADGE
   Add a small version badge in the dashboard nav, immediately after the
   "/ ORCHESTRATOR" sub-label under the Hermes brand mark.

   Style: mono text, 10px, muted color, very subtle glass pill background
   (rgba(255,255,255,.05)), 1px border, 5px border-radius. Text: "v1.0"

   This badge must always be visible on every page load so you can confirm at a
   glance which version the browser is showing. Increment it manually each time
   a meaningful set of changes is complete — v1.1, v1.2, etc.

Confirm the backup folder path and show the badge in the nav before we continue.
```

### Prompt 22 — Overview Tab

```
Wire up the live data connection — SSE from /events, polling fallback every 8 seconds —
then build the full Overview tab.

EYEBROW — Above the ops console card, a flex row with a pulsing mint dot, "UPLINK SYNCED"
in mint mono, two hairline dividers, "Hermes Orchestrator" label, and a version string.

LIVE OPS CONSOLE — a full-width glass card with three columns: 180px · 1fr · 1fr, gap 32px.

  Left — a radar SVG 180×180 (viewBox 0 0 140 140). Four faint concentric circles at
  r=62/46/30/14. Two hairline crosshair lines through center. A CSS-animated sweep group
  rotating continuously: a cyan line from center to the edge with a dot at the tip and a
  glow filter. Five agent dots rendered by JS, each sized ~4.5px radius, positioned by
  their share of total responses — a high-response agent sits far from center, an idle
  agent stays near it. Dots glow in their accent color.
  Agent accent colors: Orchestrator #A78BFA · Scout #7DD3FC · Scribe #F472B6 · Reach #E879F9 · Dev #A78BFA

  Center — "CURRENT DIRECTIVE" mono label at top. Below it, a line of mono cyan text
  (15px) that fades in a new task description every 2.6s, cycling through recent log
  entries formatted as "AGENTNAME · task description". Min-height 60px.
  Below the directive, a "CONTEXT WINDOW" section: a label showing the current agent's
  name (uppercase) on the left and their task count on the right, then a row of 16 small
  horizontal segments (5px tall, with small gap between) colored in the agent's accent
  color for the filled portion — proportional to that agent's share of total responses —
  and near-invisible for empty segments. Filled segments have a staggered pulse animation.
  A muted line below shows that agent's last status. The whole section cycles to the next
  agent every 2.4s.

  Right — "VPS HEALTH" mono label. Three metrics stacked with 16px gap:
  CPU: a 6px-tall bar with a cyan→violet gradient, percentage value in cyan above right.
  RAM: a 6px-tall bar with a violet→magenta gradient, percentage above right in violet-glow,
  "used / total MB" sub-text in muted below right.
  Disk: a 6px-tall bar with a mint→cyan gradient, percentage above right in mint,
  "used / total GB" sub-text in muted below right.
  All three bars turn amber above 70% usage, red above 85%.
  At the bottom, a hairline separator then "HERMES DBs" label and total DB size in gold
  (text only, no bar).

  Footer — inside the card, a hairline top border then a 5-cell equal grid: Queue ·
  Sessions · Errors · Today · Uptime. Mono 18px numbers. Hairline left borders between
  cells. Errors is mint when zero, red if above zero.

STATS STRIP — five glass cards in a row, each with a 2px solid top border:
  Integrity (mint) · Agent Calls (cyan) · Messages (violet-glow) · Tokens In (gold) · Cache Hits (pink).
  Large number in each card: clamp(24px,2.4vw,34px), weight 500. Small mono sub-text below.
  Integrity shows the success rate as a percentage split across two spans — an integer part
  and a ".XX" decimal part — so the decimal can jitter independently every 1.8s (a brief
  CSS animation on just the decimal span). Below: "N of 5 responsive" with a pulsing mint dot.

BOTTOM SECTION — two glass cards side by side (1.2fr · 1fr):
  Left "Throughput": a large total response count in cyan (clamp(34px,4vw,56px), weight 700)
  with "responses total" in muted 18px beside it. Below, a 100px-tall canvas sparkline
  showing the last 7 days of activity — a filled area with a violet→cyan gradient, a
  violet→cyan stroke line, and a glowing dot at the rightmost point. Redraws every 900ms.
  A mint mono sub-text below the canvas shows the most active day.
  Right "Activity": a live feed showing the 8 most recent log entries. Every 2.2s, a new
  entry slides in at the top (the oldest drops off the bottom). Each row: agent name in a
  tinted color badge, task description truncated, status in mint or red, relative time
  right-aligned in muted mono.

DATA SOURCES:
  Radar dots, directive text, context-window cycle → d.agents, d.activity
  VPS bars → d.vps (cpu_pct, mem_pct, mem_used_mb, mem_total_mb, disk_pct, disk_used_gb,
             disk_total_gb, db_size_mb)
  Footer → Queue: d.kanban.total · Sessions: d.sessions.count · Errors: d.stats.failed
           Today: last entry in d.activity_by_day · Uptime: d.gateway.uptime_seconds
  Stat cards → d.stats (total, completed, failed) · d.sessions (count, totals.messages,
               totals.input_tokens, totals.cache_read_tokens)
  Sparkline → d.activity_by_day[].total · Activity feed → d.activity[]
```

### Prompt 23 — Agents Tab

```
Build the full Agents tab.

HEADER — "SUBAGENTS" eyebrow label, then "The collective." as a large display heading
(clamp 36px–60px, weight 500, tight tracking). On the right side of the header, a single
glass card with three cells divided by hairline borders — Active (mint), Idle (amber),
Dormant (muted) — each showing a mono label above and a large number below. Active = logged
in the last 10 minutes, idle = last 6 hours, dormant = beyond that.

AGENT CARDS — five glass cards in a row, one per agent, each with a 2px solid top border
in the agent's accent color. Inside each card, top to bottom:

  — Top row: on the left, the agent's short code (ORCH / SCNT / SCRB / RECH / DEV) in a
    small mono badge tinted in the agent's color. On the right, a platform pill
    (Telegram or Discord) in cyan or violet-glow, and a status dot — mint if active,
    amber if idle, near-invisible gray if dormant. The dot pulses if active.

  — Agent name in Inter Tight, 22px, weight 600.

  — A two-line role description in muted text, clamped to 2 lines.

  — "7-DAY ACTIVITY" mono label then a mini bar chart: 7 thin bars aligned to the bottom,
    each bar's height proportional to that day's log count (max 32px tall, min 2px). Bars
    use the agent's accent color at 85% opacity, empty days at 15%.

  — A three-column stats row: Responses (large number in agent color) · Success % (mint if
    100%, amber if ≥80%, red below) · Model (mono, small, muted, truncated).

  — A thin 3px load bar spanning the full card width — filled portion in the agent's color
    showing this agent's share of total responses.

  — Last task description in small muted text, truncated to one line with an arrow prefix
    "↳", and a relative timestamp below it ("4m ago", "2h ago").

AGENT LOG — a glass card below the cards with an "Agent Logs" label on the left and a
live entry count on the right. Above the table, a filter pill row: one button for ALL and
one for each agent by their code name. The active filter has a subtle white background,
inactive ones are muted. Clicking any filter instantly re-renders from cached data.

The log table has five columns — Time · Agent · Task · Model · Status — with mono column
headers. Each row: relative time, agent name in their accent color, task description
(truncated), model label, and a status badge (mint background for completed, red for
failed). The table scrolls at a max height of 420px.

Data sources: d.agents for all card data · d.activity for the log table.
Agent accent colors: Orchestrator #A78BFA · Scout #7DD3FC · Scribe #F472B6 · Reach #E879F9 · Dev #A78BFA
```

### Prompt 24 — Agent Statistics

```
Add an Agent Statistics section to the Agents tab, between the five agent cards
and the activity log. No new data fetching needed — everything comes from the
existing SSE snapshot.

LAYOUT — a two-column grid: 1fr for the stat cards, 300px for the donut chart.
Add a small bar-chart icon and "Agent Statistics" label as a section eyebrow above.

STAT CARDS — a 2×2 grid of glass cards, each with:
  — Mono uppercase label (10px, wide letter-spacing, muted) at the top.
  — Large number or value (36px, weight 700, Inter Tight) below.
  — A 2px-tall accent bar spanning the full card width at the bottom: a dark track
    with a colored fill div that animates to its width on render.

  Four cards:
  TASKS TODAY  — today's total from d.activity_by_day.at(-1).total. Amber bar, always
                 100% wide (it's today's absolute count, not a ratio).
  TASKS THIS WEEK — sum of all 7 entries in d.activity_by_day. Cyan bar, always 100%.
  MOST ACTIVE  — name of the agent with the highest count across the 7-day window,
                 derived by summing d.activity_by_day[].agents per agent. Show the
                 name in that agent's accent color. Bar width = that agent's count /
                 week total × 100%.
  SUCCESS RATE — Math.round(d.stats.completed / d.stats.total * 100) + '%'. Bar width
                 matches the percentage. Bar color: mint if ≥90%, amber if ≥70%,
                 red below 70%.

DONUT CHART — a glass card on the right with a "TASK DISTRIBUTION" mono eyebrow.
  Draw on a <canvas> (130×130px) using the 2D context — no library needed.
  Each agent is one arc slice: use arc() from center, outer radius 52, inner radius 32
  (donut hole). Slice size proportional to that agent's d.agents[].responses count.
  Agent colors (hex, not CSS variables — canvas can't resolve var()):
    orchestrator #A78BFA · scout #7DD3FC · scribe #F472B6 · reach #FBBF24 · dev #E879F9
  If all agents have 0 responses, draw a single faint circle as a placeholder.
  In the center of the donut, draw the grand total in bold 18px and "TOTAL" in 10px
  mono below it, both in #F4F4F8.
  Below the canvas, a legend: one row per agent — 8px colored dot · agent name ·
  percentage right-aligned in muted mono.

Redraw the canvas and update all four stat cards every time the SSE snapshot fires.
```

### Prompt 25 — Tasks Tab

```
Build the full Tasks tab — a personal operator board backed by board.db (SQLite) in the
project folder. This is separate from Hermes's kanban.db which is read-only. The agent
already created board.db and its endpoints in Prompt 18 — just build the UI here.

The four endpoints are already live:
  GET  /api/board            → returns all tasks as a JSON array
  POST /api/board            → inserts a new row (title, assignee, priority, status, notes),
                               auto-generates a UUID id and created_at timestamp
  POST /api/board/update?id= → updates any fields on the matching row, sets updated_at
  POST /api/board/delete?id= → deletes the row with that id

HEADER — "EXECUTION" eyebrow label in mono, then "Task board." as a large display heading
(clamp 36px–60px, weight 500, tight tracking). On the right, a row of status pill badges —
one per column — showing the column name and its current task count. Pill text color
matches the column accent (amber/cyan/mint) when non-zero, muted when empty.

STATS STRIP — four glass cards in a row with 2px colored top borders:
  Kanban Tasks (amber) — total cards across all three columns.
  Cron Jobs (cyan) — total cron jobs from d.crons (read from the SSE snapshot).
  Done (mint) — count of done-column cards. Sub-text shows "X in progress" in cyan
  if non-zero, muted if zero.
  Next Cron (violet-glow) — a live client-side countdown ("in 4h 12m") to the next
  cron fire, calculated by parsing d.crons schedules. Job name beneath in muted mono.
  Number size: clamp(24px,2.4vw,34px), weight 500.

BOARD — three equal-width columns (repeat(3,1fr), gap 12px): Pending · In Progress · Done.
Each column:
  — Header: column label in its accent color (amber/cyan/mint) + card count. A hairline
    bottom border in that color at 40% opacity.
  — Empty state: a dashed rounded box with "DROP HERE" in very muted mono.
  — Task cards: title 14px weight 500 (wraps to 2 lines), priority dot
    (red=high, amber=medium, mint=low), relative creation timestamp in muted mono 11px.
    Delete button ✕ top-right, muted at rest, red on hover.
  — Drag-and-drop: cards are draggable. Dropping on a column highlights its outline in
    that column's color, then calls POST /api/board/update?id= with the new status and
    re-renders the board.
  — Delete: calls POST /api/board/delete?id= and re-renders immediately.

ADD FORM — a "+ Add Task" button opens a collapsible glass panel. Inside, a row with:
  Title text input · Priority dropdown (High/Medium/Low) · Column dropdown
  (Pending/In Progress/Done) · Add button (violet) + Cancel (✕).
  Submitting calls POST /api/board with the form data, then reloads the board.
  Pressing Enter in the title field also submits.
```

### Prompt 26 — Schedule Tab

```
Build the full Schedule tab.

HEADER — "CRON CALENDAR" eyebrow label in mono, then "Schedule." as a large display
heading (clamp 36px–60px, weight 500). On the right, a muted mono label showing the name
and countdown to the next cron job.

STATS STRIP — four glass cards with 2px top borders:
  Total Jobs (cyan) · Hermes Jobs (mint) · System Jobs (muted) · Next Run (violet-glow).
  Number size clamp(24px,2.4vw,34px), weight 500. Muted mono sub-text on each.

COLOR ASSIGNMENT — before rendering anything, assign each unique job name its own color
from a fixed palette. That same color must appear on the chip border, the calendar dot,
and the legend entry. It must never change between renders.
Palette: #5EE2B5 · #7DD3FC · #F5B544 · #A78BFA · #F472B6 · #E879F9 · #FBBF24 · #F26D6D

JOB GROUP CARDS — glass cards stacked vertically, one group per type:
  "Daily · runs every day" — each job as a chip with a 3px solid left border in its color,
  the fire time in that color (mono, 10px), job name in white 13px, plain-English
  description in muted 11px below. Hover shows the raw cron command in a title attribute.
  "Monthly · 1st of month" and "Periodic / Reboot" — combined into one glass card, each
  group labeled separately with a colored eyebrow. Monthly chips use amber left border,
  reboot/periodic chips use violet-glow.

CALENDAR CARD — a glass card at the bottom with a Week/Month toggle in the top-right
corner. Toggle is two buttons in a small pill: the active one gets a solid white
background with dark text, the inactive one is transparent with muted text.

  Week view — a list of 7 day rows. Order starts from the current day of the week and
  wraps around (Mon–Sun). Each row:
    Left 60px: a 28px circle containing the date number (filled violet if today, muted
    gray otherwise), then the day abbreviation in mono uppercase.
    Right: a 2px-tall horizontal timeline bar spanning 100% of the width. Jobs appear as
    10px glowing colored dots positioned at their exact percentage across the bar
    (time/1440 * 100%). Today's row gets a vertical violet line at the current time
    position with a small glowing dot at the top. Today's row also has a very subtle
    violet background tint.
  Below all rows: faint mono axis labels every 4 hours (00:00 · 04:00 · 08:00 · 12:00 ·
  16:00 · 20:00 · 24:00) aligned to their position on the bar.
  Right side: a 210px legend panel. Each entry: colored 8px dot · time in that color ·
  job name in white.

  Month view — a 7-column grid (Mon–Sun header row). Each date cell shows the day number
  centered in a circle (filled violet if today). Dates that have jobs scheduled show
  colored 7px dots below the number, one per job. Today's cell has a violet ring border.
  Right side: same legend panel as week view.

DATA SOURCE: d.crons[] — each entry has schedule (5-field cron string), name, detail
(plain-English description), category ("hermes" or "system"), command.
```

### Prompt 27 — Content Tab

```
Build the full Content tab — a read-write document library for long-form content that agents
produce. The library lives on disk at ~/.hermes/content/{agent_name}/ — one subfolder per
agent. Files are Markdown only, named YYYY-MM-DD_kebab-title.md. The first line of every
file must be a # Title heading.

Add four endpoints to server.py (Python stdlib only):

  GET  /api/content                      → scan all five agent subfolders, return a JSON
       array of {agent, filename, title (first line stripped of #), modified_at ISO string}
       sorted by modified_at DESC. Return [] if the folder doesn't exist yet.

  GET  /api/content/read?agent=&file=    → validate agent against the known list, sanitize
       filename (no .. or /), read the .md file, return {text: "..."}.

  POST /api/content/save?agent=&file=    → validate path the same way, create the agent
       subfolder if missing, write the request body bytes to disk. Used for both create and
       update.

  POST /api/content/delete?agent=&file=  → validate path, unlink the file. Return 200 on
       success, 404 if the file doesn't exist.

Path safety: reject any agent name not in [orchestrator, scout, scribe, reach, dev] and
any filename containing .. or /. This blocks directory traversal at the server level.

Now build the Content tab UI — a two-pane split layout.

HEADER — "AGENT OUTPUT" eyebrow label in mono, then "Library." as a large display heading
(clamp 36px–60px, weight 500, tight tracking). On the right, a "+ New Doc" button (glass
card style, violet left border).

STATS STRIP — three glass cards in a row with 2px top borders:
  Total Docs (violet-glow) · Agents Writing (cyan) · Latest (mint — shows the doc title
  truncated, with "agent · relative time" in muted mono below).
  Number size clamp(24px,2.4vw,34px), weight 500.

NEW DOC FORM — a collapsible glass panel that opens when "+ New Doc" is clicked:
  Agent dropdown (Orchestrator / Scout / Scribe / Reach / Dev).
  Title text input — the kebab slug and date prefix are generated automatically from this.
  Content textarea (10 rows) — prepopulate with "# Title\\n\\n" as a placeholder hint.
  Create button (violet) + Cancel (✕).
  On submit: convert title to lowercase kebab-case, prefix today's date as YYYY-MM-DD_,
  append .md. Ensure the content starts with # Title if not already. POST to
  /api/content/save, then reload the list.

SPLIT LAYOUT — grid-template-columns: 300px 1fr, gap 18px.

  LEFT PANEL — two sections stacked:
    Agent filter pills — "All" + one pill per agent. Active pill gets a subtle white
    background. Clicking any pill filters the list below without a server round-trip.
    Doc list — each row is a clickable item: agent name in a small color badge (use the
    same accent colors as Agents tab), doc title in white 14px, relative modified time in
    muted mono 11px. Active item has a violet left border highlight.

  RIGHT PANEL — a glass card that shows the selected document:
    Header row: agent color badge (pill) on the left, formatted date in muted mono,
    doc title in Inter Tight 20px weight 600.
    Action row: EDIT button (amber, opens inline editor), download button (↓, saves raw
    .md as a file), delete button (✕, prompts "Delete this document?" before calling
    /api/content/delete).
    Below: rendered markdown in a #content-body div — use marked.js (already loaded on
    the page) to parse and render. Style headings and code blocks to match the dashboard
    palette.
    Edit mode: replaces the rendered div with a full-width textarea containing the raw
    markdown. Save button calls POST /api/content/save with the textarea value, then
    returns to view mode. Cancel restores the previous view without saving.

  Empty state (no doc selected): centered muted mono text "Select a document to read".

Wire the Content tab into the existing switchTab() function — add:
  if (name === 'content') loadContentDocs();
alongside the existing overview/tutorial hooks. Without this the tab renders blank.
Auto-select the first document in the list if one exists.
```

### Prompt 28 — Agent Document Storage Protocol

```
When you produce any long-form document — articles, research reports, scripts,
outlines, briefs, plans, transcripts, summaries, or any deliverable longer than
~15 lines — you must save it to your dedicated agent folder, not return it as a
chat response.

Folder structure:
  /root/.hermes/content/
    ├── orchestrator/
    ├── scout/
    ├── scribe/
    ├── reach/
    └── dev/

Each agent writes only to its own lowercase subfolder. Never write into another
agent's folder.

Rules:

1. Save to your own folder only.
   Orchestrator → /root/.hermes/content/orchestrator/
   Scout        → /root/.hermes/content/scout/
   Scribe       → /root/.hermes/content/scribe/
   Reach        → /root/.hermes/content/reach/
   Dev          → /root/.hermes/content/dev/

2. Use markdown (.md) for every long-form document. No .txt, no inline chat dumps.

3. Filename convention: YYYY-MM-DD_short-kebab-case-title.md
   Example: 2026-05-01_competitor-scan.md
   Lowercase only, hyphens between words, no spaces, no special characters.

4. First line must be a top-level heading (# Title) that matches the document's
   purpose. The Content tab uses this as the display title — make it descriptive
   and human-readable, not a slug.

5. Structure the body with proper markdown: ## and ### for sections, **bold** for
   emphasis, \`inline code\` for technical terms, fenced code blocks with language
   tags for code, and - bullet lists where they help. The Content tab renders all
   of this — write so it reads well in the preview panel.

6. What counts as long-form (save to folder): articles, research summaries,
   scripts, outreach drafts, strategy docs, meeting notes, technical guides,
   post-mortems, anything intended to be reread or reused.

7. What does not (return inline in chat): single-sentence answers, quick status
   updates, one-line confirmations, tool call results, conversational replies.

8. One document per file. If a task produces multiple deliverables, save each
   as its own file.

9. Never overwrite silently. If a filename collides, append -v2, -v3, or use a
   more specific title.

10. Stay in your lane. Write content that fits your role. If a task falls outside
    your role, hand it off rather than writing it yourself.

11. After saving, confirm in chat with your agent name, the full path, and a
    one-line summary. Example:
    Scout → /root/.hermes/content/scout/2026-05-01_competitor-scan.md — competitive analysis of 6 platforms.

This protocol exists because the Content tab in the dashboard reads directly from
/root/.hermes/content/. If you return long-form work in chat instead of saving it
there, it doesn't show up in the dashboard, can't be previewed, edited, or
downloaded, and effectively gets lost.

Create your subfolder now if it doesn't exist. Save a short test document to confirm
the protocol is working. Confirm with the standard one-line format above.
```

### Prompt 29 — SSH keys — set them up once, never type a password again

```
# ============================================
# SSH Setup Guide for VPS Access
# ============================================

# ============================================
# FOR MAC/LINUX USERS
# ============================================

# Check if you already have an SSH key
ls ~/.ssh/id_ed25519

# If the file exists, skip to the ssh-copy-id step below
# If you get "No such file or directory", generate a new key:
ssh-keygen -t ed25519 -C "agent-dashboard"
# Press Enter for all prompts — no passphrase needed for automation

# Copy your key to the VPS (enter your VPS password one last time)
ssh-copy-id root@YOUR_VPS_IP

# Test the connection — you should connect with no password prompt
ssh root@YOUR_VPS_IP
# Type 'exit' to disconnect

# ============================================
# FOR WINDOWS POWERSHELL USERS
# ============================================

# Check if you already have an SSH key
Test-Path "$env:USERPROFILE\\.ssh\\id_ed25519"

# If False, generate a new key:
ssh-keygen -t ed25519 -C "agent-dashboard"
# Press Enter for all prompts — no passphrase needed for automation

# Copy your key to the VPS
$pubKey = Get-Content "$env:USERPROFILE\\.ssh\\id_ed25519.pub"
ssh root@YOUR_VPS_IP "mkdir -p ~/.ssh && echo '$pubKey' >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"

# Test the connection — you should connect with no password prompt
ssh root@YOUR_VPS_IP
# Type 'exit' to disconnect
```

### Prompt 30 — Create a one-click desktop launcher

```
# ============================================
# Create SSH Tunnel Script for AgentOS
# ============================================

# ============================================
# FOR MAC USERS
# ============================================

# 1. Open a text editor (TextEdit, VS Code, nano, etc.)
# 2. Copy and paste the code below into your text editor:

#!/bin/bash
pkill -f "51763:127.0.0.1:51763" 2>/dev/null
sleep 1
ssh -o StrictHostKeyChecking=no -N -L 51763:127.0.0.1:51763 root@YOUR_VPS_IP &
sleep 2
open "http://localhost:51763"

# 3. Save the file as: AgentOS.command (choose your preferred location)
# 4. Open Terminal and run:
chmod +x /path/to/AgentOS.command
# 5. Now you can double-click AgentOS.command to start the tunnel

# ============================================
# FOR WINDOWS POWERSHELL USERS
# ============================================

# 1. Open PowerShell and run this ONCE to allow scripts to run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Say 'Y' when it asks for confirmation

# 2. Open a text editor (Notepad, VS Code, etc.)
# 3. Copy and paste the code below into your text editor:

# Kill any existing SSH tunnels
Get-Process | Where-Object {$_.ProcessName -match "ssh"} | Stop-Process -Force -ErrorAction SilentlyContinue 2>$null

Write-Host "Starting SSH tunnel to AgentOS..."
Write-Host "The dashboard will be available at: http://localhost:51763"
Write-Host "Keep this window open while you use the dashboard."
Write-Host ""

# Start the tunnel
ssh -o StrictHostKeyChecking=no -N -L 51763:127.0.0.1:51763 root@YOUR_VPS_IP

Write-Host "Tunnel closed. Press Enter to exit..."
Read-Host

# 4. Save the file as: AgentOS.ps1 (choose your preferred location)
# 5. Right-click the file → "Run with PowerShell"
# 6. Once the script says "Starting SSH tunnel...", open your browser to http://localhost:51763
```

### Prompt 31 — Option B — Tailscale for phone & laptop access

```
Set up Tailscale on this VPS so I can securely access the Mission Control dashboard
from anywhere, both on my PC and on my mobile device.

Please install and configure Tailscale on the VPS, then start the Tailscale
authentication process and provide me with the login/authentication link so I can
approve and connect the VPS to my Tailscale account.

After authentication, please verify that the VPS is connected to my Tailnet and
confirm the Tailscale IP address. Then explain how I can use that Tailscale IP to
access the Mission Control dashboard remotely from my PC or phone.

Also make sure the dashboard remains secure and is not unnecessarily exposed to the
public internet.
```
