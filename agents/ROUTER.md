# Capture OS — natural-language router cheat sheet

**Default coordinator:** Hermes (cross-agent, ambiguous, or multi-step quests).  
**Visibility:** Mission Control dashboard (single pane) will surface each agent's `content/` outputs — not separate human-run consoles.

## Routing table

### Hermes — Guildmaster / coordination
| Say something like… | Route to |
|---------------------|----------|
| orchestrate new opp intake | Hermes |
| update pWin radar in dashboard | Hermes (may delegate Hephaestus for implementation) |
| who should own this quest? | Hermes |
| decompose this into party tasks | Hermes |
| run review gate on the whole opportunity | Hermes (coordinates Odysseus + Clio) |
| sync the party after identity changes | Hermes → Hephaestus |
| remember this / dump idea / triage to vault | Hermes (**skill: `knowledge-triage`**, preference B) |
| promote vault candidate to trusted | Hermes → Odysseus (citations) → Hephaestus (move + index) |

### Hermes — knowledge intake (doc 02)
| Say something like… | Route to |
|---------------------|----------|
| remember this for the vault | Hermes triage → `generated-projections/` or discard |
| is this competitor or customer intel? | Hermes → Iris lane after triage |
| what needs my confirm in the vault? | Hermes morning queue (candidates + uncertain) |

Spec: `docs/inspiration/knowledge-vault-and-compounding-truth.md` · Retrieve: `agents/_shared/VAULT_RETRIEVE.md`

### Iris — Scout / research
| Say something like… | Route to |
|---------------------|----------|
| analyze new SAM opportunity | Iris |
| research USAspending for this agency | Iris |
| find competitor awards on this NAICS | Iris |
| pull federal signals for this customer | Iris |
| what changed on SAM notice XYZ | Iris |
| intel brief for opportunity ABC | Iris |

### Clio — Packet fill / scribe
| Say something like… | Route to |
|---------------------|----------|
| fill packet section on win themes | Clio |
| map this evidence into the Living Briefing Packet | Clio |
| draft executive summary for MS2 | Clio |
| synthesize Iris findings into packet fields | Clio |
| tighten prose on discriminators slide | Clio |
| boss-fight roadmap for this opp | Clio |

### Odysseus — Strategy / Shipley gates
| Say something like… | Route to |
|---------------------|----------|
| review MS3 gate risks and evidence | Odysseus |
| synthesize evidence for compliance | Odysseus |
| run Shipley Pink/Red on this section | Odysseus |
| stakeholder strategy for this customer | Odysseus |
| risk register for capture phase | Odysseus |
| can we promote this gate? | Odysseus |

### Hephaestus — Build / tools / dashboard
| Say something like… | Route to |
|---------------------|----------|
| build MCP for packet pull | Hephaestus |
| wire dashboard tile for agent status | Hephaestus |
| fix profile sync script | Hephaestus |
| add skill for SAM polling | Hephaestus |
| Mission Control shell component | Hephaestus |
| maintain Hermes profile bindings | Hephaestus |
| vault bootstrap / lint / zone INDEX | Hephaestus (`scripts/bootstrap_knowledge_vault.py`, `scripts/vault_lint.py`) |

## Capture loop supervisor (Hermes — full or slice)

**Spec:** `agents/CAPTURE_LOOP_SUPERVISOR.md` · **Skill:** `capture-loop-supervisor` · **Slash:** `/capture-loop`

| Overwatch says… | Mode |
|-----------------|------|
| `Run capture loop on [name or brief]` | Full pipeline (steps 1–9) |
| `Process new opp: [details]` | Full pipeline (intake emphasis) |
| `Advance packet to MS3 gate for [opp]` | Slice: Clio → Odysseus → Hermes ratify (+ Hephaestus if tools) |

Handoffs: Iris → Clio → Odysseus → (Hephaestus) → Hermes; artifacts in each `content/`.

## Slash-command shortcuts

Syntax: **`/<agent> <task in natural language>`** (args after the command are the quest).

| Command | Role | Example |
|---------|------|---------|
| `/hermes` | Coordinator | `/hermes orchestrate new opp intake for notice 12345` |
| `/iris` | Research | `/iris research USAspending for DoD agency X last 3 FY` |
| `/clio` | Packet | `/clio fill packet section on win themes from latest intel` |
| `/odysseus` | Gates/strategy | `/odysseus review MS3 gate risks and evidence` |
| `/hephaestus` | Build | `/hephaestus build MCP for packet pull from Ariadne` |

Also: **`/capture-router`** — loads this routing table into context for Hermes or any agent.

**`/capture-loop`** — Hermes runs the 9-step capture supervisor (same as “Run capture loop on …”).

## Fallback behavior

1. **Low confidence (single domain):** Ask Overwatch one clarifying question with **2–3 labeled options** (e.g. "Research (Iris) vs packet fill (Clio)?").
2. **Multi-domain or unclear scope:** Route to **Hermes** to decompose and assign.
3. **Never** ask Overwatch to run CLI; Hermes delegates execution to the party.

## Agent duties (router)

- **Hermes:** Interprets natural language and slash dispatches; uses `delegate_task` or profile-appropriate handoffs; owns fallback routing.
- **Iris / Clio / Odysseus / Hephaestus:** Accept quests in-lane; decline with redirect phrases from `AGENTS.md`.
- **Hephaestus:** Keeps slash skills and `ROUTER.md` in sync when router changes (no Overwatch ops).