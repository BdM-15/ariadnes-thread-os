# Vault harmonize — llm-wiki + Obsidian standards pass (2026-07-05)

**Why:** Capability waves (W2–W5) built pages through the **Ariadne promote pipeline**, not a single **llm-wiki** compile loop. Standards drift: mixed frontmatter, **73** heuristic unresolved wikilinks (lint), stale `auto_generated` tails, index/catalog lag, and **write-tool** timeouts on batch candidates.

**When:** After **capability tail** closes (W5 promote + Viaverse/Wraith) and **before** you declare foundational v1 — can overlap **W8** in the item-4 plan but **must** run once skills are mandatory.

---

## Preconditions (Hephaestus maintenance — same sprint)

| Gate | Action |
|------|--------|
| **Phantom tree** | Remove `C:\c\Users\benma\` after backup (bad `/c/Users/...` writes) |
| **Party cwd** | `python scripts/fix_party_profile_cwds.py` + `verify_party_paths.py` → all green |
| **Wiki path** | `WIKI_PATH` + `OBSIDIAN_VAULT_PATH` = `C:/Users/benma/ariadnes-thread-os/knowledge` in `~/.hermes/.env` (all profiles) |
| **Writes** | Vault batch edits via **one Python script from repo root** (not parallel `write_file`) per `ariadne-thread-os` pitfalls |

---

## Harmonize waves (load **`llm-wiki`** every session)

**Orient every wave:** `ariadne-vault-schema.md` → `index.md` → `log.md` tail → `vault_lint.py`.

### H1 — Lint-driven fixes (automated + Hephaestus)

1. Run full `vault_lint.py`; export missing wikilink targets and orphan pages.
2. Fix **broken `[[links]]`** — create stub entity pages or retarget to existing slugs (no invented facts).
3. Normalize **trust** frontmatter (`trusted` / `candidate` only; no quoted variants).
4. Ensure every **trusted** capability has `citations:` + `retrieved:` + `reviewed_by` where policy requires.

### H2 — Karpathy navigation (index + log)

1. Rebuild **`knowledge/index.md`** sectioned catalog (capabilities, foundation, entities) — skill **`hephaestus`** `karpathy-morning-index-catalog` pattern.
2. Append **`log.md`** batch line: `harmonize | H2 index refresh`.
3. Zone **`INDEX.md`** files aligned with actual file counts.

### H3 — Page shape (Clio + Odysseus sample)

1. Pick **5 trusted pages** (one per zone type) as **gold templates**.
2. Odysseus rubric: min 2 outbound wikilinks, Evidence/Gaps sections, no erase trusted history.
3. Clio **REWRITE** only where pages fail rubric — not mass regen.

### H4 — Obsidian human pass (you)

1. Open graph in Obsidian at connected vault path.
2. Flag islands / wrong link density; return slug list to Hermes.
3. Agents apply H1–H3 fixes; you re-spot-check.

### H5 — Shipley + templates (foundational — not optional)

Runs **after** you supply Capture Guide + template order — separate from H1–H4 capability hygiene.

---

## Definition of done (harmonize slice)

- `vault_lint.py` exit **0**; unresolved wikilinks **trending to 0** (document accepted stubs).
- **0** `auto_generated: true` on capability slugs (post tail promote).
- `index.md` **Last updated** matches last harmonize batch.
- `verify_party_paths.py` **OK**; **no** phantom tree.
- Party delegations cite: load **llm-wiki**, `WIKI_PATH` set, batch writes scripted.

---

## Order vs your roadmap

```
Now     → capability tail (W5 + viaverse/wraith) [in flight]
Next    → Hephaestus file-mutation + env repair (blocking)
Then    → H1–H2 harmonize (can start partial while Shipley blocked)
Parallel→ Shipley guide + templates (foundational v1)
Last    → H3–H4 + W8 sign-off → merge review
```

---

## Related

- `agents/_shared/VAULT_RETRIEVE.md`
- `agents/_shared/FILE_MUTATION.md`
- `knowledge/foundation/reference/obsidian-desktop.md`
- Recalibration: `2026-07-05_vault-recalibration-foundational-v1.md`