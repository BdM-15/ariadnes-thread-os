# H3 harmonize — gold templates (ship)

**Date:** 2026-07-06  
**Agent:** Hephaestus (delegated H3 batch, retry)  
**Program:** `agents/hermes/content/2026-07-05_vault-llm-wiki-harmonize-program.md` § H3  
**Branch:** `feature/knowledge-vault-v1` — **no merge to `main`**

---

## Delivered

| Item | Result |
|------|--------|
| Gold templates (5 zones) | `scripts/harmonize_h3_gold_templates.py` batch |
| Pages updated | kbr-cyber-range, shipley-capture-guide-hub, shipley-capture-guide-source, kbr-services-readiness-sustainment, shipley-decision-gate-reviews |
| Rubric | `## Evidence` + `## Gaps`, min 2 outbound wikilinks, normalized trusted frontmatter |
| log.md + index.md | H3 batch append + Last updated bump |
| vault_lint | 2026-07-06 15:10 UTC exit 0; unresolved wikilinks 0 |

---

## Verification

```bash
python scripts/harmonize_h3_gold_templates.py
python scripts/vault_lint.py
```

**Commit:** `feat(vault): harmonize H3` — `af923b81c8e8a1d9a6bf01c793bcf22ec03dc69d`

*Logged:* H3 harmonize gold templates ship (hephaestus retry)[H[2J[3J