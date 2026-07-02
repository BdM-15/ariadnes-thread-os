# Party calibration quest — operating rhythm before v1 continues

**Status:** ✅ Ratified 2026-07-02 — see `2026-07-02_party-calibration-ratification.md`  
**Next:** `2026-07-02_wave1-doc02-finish-plan.md` (Wave 1 doc 02, then doc 03 per index)  

---

## 1. Why this quest exists

Activity logs show **~79% of tasks on Hermes** while charters assign **implementation** to Hephaestus and **domain work** to Iris, Clio, and Odysseus. That was acceptable for an initial plumbing sprint; it is **not** the steady state.

**Your intent (confirmed):**

- You talk to **Hermes** in raw NLP — trust him to orchestrate, not micromanage.
- **Specialists** execute in their lanes so the OS is exercised by the people who will live in it.
- **Composer 2.5** on party profiles for build execution; **Grok 4.3** on Hermes for planning — **credit-efficient** delegation.

This quest sets **rhythm** and a **backlog brainstorm by specialty** — no new MC tabs, no implementation in this document.

---

## 2. Steady-state rhythm (Overwatch → party)

```
Overwatch (NLP)
    → Hermes: classify · deliberate-build check · plan · assign DRI
    → Specialist(s): execute · artifact in agents/<name>/content/
    → Hermes: ratify · board/quest update · short summary + links to Overwatch
```

| Step | Hermes | Specialists |
|------|--------|----------------|
| Intake | Parse intent; reject same-session bolt-ons per `DELIBERATE_BUILD.md` | — |
| Route | Name DRI; optional parallel research (Iris) + gate sketch (Odysseus) | Accept handoff |
| Execute | **No** code/patch unless emergency + explicit “Hermes acting as builder” | Build, write, log as **self** |
| Close | pWin/quest/board; preview links | — |

**Canon:** `agents/_shared/PARTY_OPERATING_RHYTHM.md`

---

## 3. Ownership matrix — open build themes (v1 / near v1)

| Theme | DRI | Hermes role | Minimal v1 outcome |
|-------|-----|-------------|----------------------|
| Mission Control (`server.py`, `index.html`, `start.sh`) | **Hephaestus** | Prioritize; accept PR-style summary | Stable cron/board; no new tabs without deliberate gate |
| Vault tooling (`bootstrap`, `vault_lint`, scripts) | **Hephaestus** | Schedule; ratify | Lint cron owned; bootstrap idempotent |
| Profile sync / `verify_party_paths` | **Hephaestus** | Delegate after SOUL/AGENTS edits | Party cwd verified post-change |
| `MC-TASK-VAULT-ROUTING` design | **Hermes facilitates** | Brainstorm → decision doc | Party proposal: board + Content + skill (not tab) |
| Quest ingest (`quest.yaml` vs flat `.md`) | **Hephaestus** | Scope from `TECH_DEBT` MC-QUEST-01 | One chosen path + doc |
| Knowledge triage B | **Hermes** | Execute triage; delegate promote | Candidate + board task |
| Vault promote / trust | **Odysseus** | Route after triage | Citation + gate note in `content/` |
| Entity / competitor intel (e.g. EDEN follow-up) | **Iris** | Handoff from Hermes triage | Intel brief path in `agents/iris/content/` |
| Vault prose / taxonomy readability | **Clio** | Request after structure exists | INDEX blurbs, projection templates |
| Capture loop slices | **Hermes supervises** | Steps 1–9 per `CAPTURE_LOOP_SUPERVISOR.md` | Artifacts per agent per step |
| Skills from repeat tasks | **Hephaestus** | Hermes identifies pattern | Draft skill; Hermes approves |
| Inspiration / data-elements wave | **Hermes + Clio** | One doc per session rule | Doc in `docs/inspiration/` |

---

## 4. Specialty brainstorm — what each agent should own next

### Hephaestus (Artificer)

- **MC hardening:** health checks, snapshot freshness, board API edge cases.
- **File mutation guardrails:** wire `normalize_write_path` into maint docs; optional pre-commit hook (park if heavy).
- **Vault lint:** interpret lint output; wikilink fixes in `knowledge/thread/` (batch, not Hermes).
- **Quest YAML:** minimal schema aligned with capture loop step 1.
- **Cron:** attach_to_session patterns for `TASK_WORKFLOW_LADDER.md`.

### Iris (Scout)

- **EDEN / edge computing:** competitor and customer signals; USAspending/SAM hooks when pursuit is real.
- **Entity graph inputs:** who competes on which pursuits; feed `entities/competitors/` with citations.
- **Post-triage:** when Hermes tags `is this competitor intel?` — Iris owns the brief.

### Clio (Scribe)

- **Vault voice:** candidate pages readable for Overwatch morning queue.
- **Living Packet:** when loop runs, field mapping from Iris intel.
- **Taxonomy:** short operator-facing labels on zones (not developer jargon).

### Odysseus (Knight)

- **Trust ladder:** what “promote” means for candidates vs entities vs packet claims.
- **EDEN gate:** is candidate sufficient for pursuit tracking without over-trusting?
- **Shipley on inspiration docs** before merge to `main` when capture doctrine changes.

### Hermes (Guildmaster)

- **Orchestration only by default:** plans, board, quests, triage, deliberate-build, Overwatch summaries.
- **Party calibration reviews** monthly or when log skew >60% Hermes again.
- **Delegate_task / profile sessions** instead of inline patches.

---

## 5. Anti-patterns (stop doing)

| Anti-pattern | Instead |
|--------------|---------|
| Hermes patches MC during “quick fix” | File Hephaestus task; Hermes waits for artifact |
| All logs `agent_name=hermes` | DRI logs under own name |
| Smoke tasks only for Iris/Clio/Odysseus | One real vertical slice per sprint |
| New MC tab on Overwatch mention | Tech debt + party brainstorm |
| Overwatch runs `sync_party_profiles` | Hephaestus |

---

## 6. Ratification checklist (Overwatch)

- [x] Agree: Hermes = touchpoint, not default implementer  
- [x] Agree: Composer 2.5 on party profiles for execution work  
- [x] Agree: roadmap = inspiration **waves**; finish **doc 02** before doc 03  
- [x] First slice: **doc 02 finish plan** (Odysseus gate → Hephaestus vault → Iris/Clio EDEN)

---

## 7. After ratification (Hermes actions — no code until approved)

1. Post **three** board tasks (or one quest folder) with DRIs from §3 picks.  
2. Open **Hephaestus** profile with a written brief (not Hermes session patches).  
3. Re-run log skew check after ~10 tasks; target **Hermes <40%** on build-heavy weeks.

---

*Related:* `agents/TEAM_AWARENESS.md` · `agents/ROUTER.md` · `agents/_shared/DELIBERATE_BUILD.md` · `docs/TECH_DEBT.md`