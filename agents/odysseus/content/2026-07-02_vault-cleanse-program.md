# Vault clean-slate cleanse program

**Date:** 2026-07-02  
**Accountable:** Hermes · **Sign-off:** Overwatch  
**Design:** `deleg_251b596d` task 3 (no files moved yet)

## North star

`knowledge/{zones}/` — no `thread/` — Ariadne schema **`ariadne-vault-schema.md`**, capform runtime vestiges removed, Wandermist **INDEX maps** strengthened. Clean slate ≠ re-import capform.

## Topology

```
knowledge/
  index.md, log.md
  foundation/ariadne-vault-schema.md
  entities/, global/, pursuits/, generated-projections/, relationships/
```

**Out of v1 tree:** `data-elements/`, `milestones/`, `training/`, `education/` unless Overwatch promotes.

## Schema rename

| From | To |
|------|-----|
| `capture-llm-wiki.md` | `ariadne-vault-schema.md` |
| `[[capture-llm-wiki]]` | `[[ariadne-vault-schema]]` + one-release alias |

Drop capform UI/Postgres-as-mandatory Layer 1 from schema prose.

## Retire / archive examples

- `test-agency-xyz.md`, `example-competitor-llc.md` → `generated-projections/archived/cleanse-2026/` or delete
- Placeholder domain_intel with empty cites → candidate or archive (Iris + Odysseus list)

## Party RACI

| Package | Responsible |
|---------|-------------|
| Entity/intel inventory | Iris |
| Pursuit prose / slugs | Clio |
| Promote freeze + trust rules | Odysseus (Overwatch approves baseline) |
| Path migration + scripts + MC | Hephaestus |
| Schema rewrite draft | Hephaestus → Odysseus gate |

## Promotion during reset

**Freeze** all promotes until: flatten complete, `vault_lint` green, manifest signed by Odysseus + Overwatch.

## Phases

0. Freeze (Hermes board `vault:cleanse`)  
1. Inventory manifest (party parallel)  
2. Archive smoke entities  
3. Flatten `knowledge/thread` → `knowledge/` (Hephaestus single branch)  
4. Schema rename + wikilink pass  
5. INDEX “Where to go” (Clio)  
6. Overwatch ratify baseline → doc 02 acceptance

## Overwatch choice

- **Minimal cleanse:** rename schema + remove known smoke files + flatten  
- **Full cleanse:** archive most seeded trusted; rebuild from KBR SSOT + vetted candidates

## Ref

Hermes brainstorm · Hephaestus UI spec · Clio edit workflow.