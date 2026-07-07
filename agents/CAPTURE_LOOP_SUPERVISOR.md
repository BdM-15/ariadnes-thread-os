# Capture loop — supervisor flow (Hermes-owned)

Hermes **supervises** this pipeline. Specialists execute their step, write artifacts to **`agents/<agent>/content/`**, and pass **handoff manifests** (below). Overwatch triggers full loop or **slices** via natural language or `/capture-loop`.

## Sequence (steps 1–9)

| Step | Owner | Action | Output path |
|------|--------|--------|-------------|
| 1 | **Hermes** | Receive/initiate quest; create quest folder + `quest.yaml` | `agents/minos/content/quests/<slug>/` |
| 2 | **Hermes** | Route research to Iris (`delegate_task`, profile mindset Iris) | Update `quest.yaml` status |
| 3 | **Iris** | Research intel; structured findings + citations | `agents/iris/content/<slug>-intel.md` (+ optional JSON) |
| 4 | **Iris → Clio** | Handoff via Hermes: point Clio at intel path | `agents/iris/content/<slug>-handoff-clio.md` |
| 5 | **Clio** | Synthesize LBP; fields, prose, win themes | `agents/clio/content/<slug>-packet.md` |
| 6 | **Clio → Odysseus** | Handoff updated packet | `agents/clio/content/<slug>-handoff-odysseus.md` |
| 7 | **Odysseus** | Gaps, risks, compliance, gate readiness; strategy | `agents/odysseus/content/<slug>-gate-review.md` |
| 7b | **Odysseus → Hephaestus** | If tools/MCP/dashboard needed | Note in gate review + Hermes delegates |
| 8 | **Hephaestus** | Build MCP/tools/dashboard deltas | `agents/hephaestus/content/<slug>-build.md` |
| 9 | **Hermes** | Ratify; update pWin; coordinate gate review; surface for Overwatch / Mission Control | `agents/minos/content/quests/<slug>/ratification.md` |

## Handoff manifest (minimal)

Each handoff file includes:

```yaml
quest_slug: example-opp
from_agent: iris
to_agent: clio
artifact_paths:
  - agents/iris/content/example-opp-intel.md
status: ready
notes: ""
```

## Overwatch trigger phrases (Hermes must recognize)

| Phrase | Mode |
|--------|------|
| `Run capture loop on [name or brief]` | **Full** pipeline (1–9) |
| `Process new opp: [details]` | **Full** (emphasis intake + intel + packet) |
| `Advance packet to MS3 gate for [opp]` | **Slice** — Clio refresh (5) → Odysseus MS3 (7) → Hermes ratify (9) |
| `/capture-loop [brief]` | Same as full loop (slash skill) |

### Optional slices (Hermes interprets)

- **Intel only:** Iris steps 2–3  
- **Packet only:** Clio step 5 (requires prior intel path)  
- **Gate only:** Odysseus step 7  
- **Build only:** Hephaestus step 8  

## Automatic vs manual

- **Manual:** Overwatch says a trigger phrase → Hermes runs supervisor (this doc + skill `capture-loop-supervisor`).
- **Automatic:** Hermes treats any multi-step opp intake as this pipeline unless Overwatch names a single-agent owner.

## Mission Control

All `content/` artifacts + `quests/<slug>/` are the feed for the unified dashboard (Thread Tavern). No separate per-agent consoles.

## Models

- Routine fills/builds: Orinth/local where appropriate.  
- Planning, gate strategy, multi-agent coordination: frontier (Grok).