---
name: "Obsidian Desktop"
type: reference
id: foundation-reference-obsidian-desktop
trust: trusted
added: "2026-07-06T12:00:00Z"
last_updated: 2026-07-06
citations: "harmonize:H3-gold-template • path:foundation/reference/obsidian-desktop.md"
---

# Obsidian desktop (optional complement)

**SSOT:** `knowledge/` at repo root — same files Hermes party and Mission Control browse.

## Karpathy pattern (aligned with PolyDAO / Hermes stack)

| Role | Tool |
|------|------|
| **Programmer** | Hermes party (Iris → Clio → Odysseus gate → Hephaestus promote) |
| **IDE (optional)** | Obsidian desktop — graph, manual append, human review |
| **Codebase** | Flat markdown + `[[wikilinks]]` under `knowledge/` |

You do **not** need Obsidian for agents to compound the vault. Use it when you want graph view, quick human edits, or offline reading.

## Open vault in Obsidian

1. Install [Obsidian](https://obsidian.md/) (local-first).
2. **Open folder as vault:** `C:\Users\benma\ariadnes-thread-os\knowledge`
3. Enable **Properties** (YAML frontmatter) in settings if not default.
4. Recommended: **Graph view**, **Outgoing links**, **Backlinks**.

**Overwatch (2026-07-05):** Vault opened in Obsidian at this path — same SSOT as agents.

## Hermes skills (same vault)

| Skill | Use |
|-------|-----|
| **`llm-wiki`** | Karpathy compile loop: orient (`ariadne-vault-schema` + `index.md` + `log.md` tail) → ingest/update → index + log append → lint |
| **`obsidian`** | Read/search/edit notes at resolved vault path (filesystem = Obsidian) |

**Env (recommended in `~/.hermes/.env`):**

```bash
WIKI_PATH=C:/Users/benma/ariadnes-thread-os/knowledge
OBSIDIAN_VAULT_PATH=C:/Users/benma/ariadnes-thread-os/knowledge
```

Ariadne maps Karpathy **Layer 3** to `[[ariadne-vault-schema]]` (not generic `SCHEMA.md`). **Layer 1 raw** for capture = Postgres/intel + cited URLs on pages, not necessarily `raw/` subtree yet.

## Wikilinks

Same as agent OS: `[[kbr-vaault]]`, `[[ariadne-vault-schema]]`, `[[global/INDEX]]`.

## Rules

- `agents/*/content/` = staging only, not vault SSOT.
- Append trusted sections; do not erase history per `[[ariadne-vault-schema]]`.
- Large rewrites: candidate → lighthouse promote.

## Git

Branch `feature/knowledge-vault-v1` until Overwatch approves merge to `main`.

## Evidence
- Trusted page; cite Layer 1 sources in `citations` and bullets below.
- Harmonize H3 gold template — append dated evidence; do not erase prior trusted history.

## Gaps
- Open questions and unverified claims belong here until Iris/Overwatch closes them.

## Related

- [[ariadne-vault-schema]]
- `docs/inspiration/knowledge-vault-and-compounding-truth.md`[H[2J[3J
