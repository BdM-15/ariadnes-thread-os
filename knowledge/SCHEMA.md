---
title: "Ariadne Vault Schema (LLM Wiki)"
created: 2026-07-06
updated: 2026-07-06
type: schema
tags: [karpathy-wiki, schema, vault, agent-os, ariadne, llm-wiki]
aliases: [ariadne-vault-schema, capture-llm-wiki]
sources: [foundation/ariadne-vault-schema.md]
---

# Wiki Schema — Ariadne Thread OS Knowledge Vault (Foundational v1)

**Primary reference:** [[ariadne-vault-schema]] (foundation/ariadne-vault-schema.md) — this file is the executable Layer 3 contract.

**Domain:** Agent OS knowledge vault following Karpathy LLM Wiki pattern + Ariadne trust/promote gates. Foundational Vault v1 scope only.

**Conventions (llm-wiki + Obsidian compatible):**
- File names: lowercase, hyphens, no spaces.
- Every wiki page starts with YAML frontmatter (title, created, updated, type, tags, trust, sources).
- Use `[[wikilinks]]` (minimum 2 outbound per page where applicable).
- When updating, bump `updated` date.
- Every new trusted page added to appropriate zone `INDEX.md` and root `index.md`.
- Every action appended to `log.md`.
- Obsidian: wikilinks render natively; .obsidian/ folder present for graph/Dataview.
- Raw sources cited; never modify raw/.

**Frontmatter (required):**
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary | schema | meta
tags: [from taxonomy in ariadne-vault-schema]
trust: candidate | trusted | archived
sources: [paths or urls]
---
```

**Tag Taxonomy & Zones:** See [[ariadne-vault-schema]] §2-3 (entities/, global/, pursuits/, generated-projections/, foundation/, relationships/).

**Page Thresholds & Update Policy:** Per ariadne-vault-schema.md (Overwatch promote only for trusted; no auto-promote).

**Obsidian Compatibility:** Vault opens directly in Obsidian. Attachments in raw/assets/ (deferred). Enable wikilinks and Dataview for queries.

**Lint:** `python scripts/vault_lint.py` (unresolved wikilinks: 0 as of latest).

**Provenance:** Claims synthesized from multiple sources use ^[source] markers where applicable.

This SCHEMA.md enables full llm-wiki orientation and Obsidian structure compliance within Foundational Vault v1.
