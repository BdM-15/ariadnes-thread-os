# Content delivery policy (all five agents)

Applies to: **hermes**, **iris**, **clio**, **odysseus**, **hephaestus**.

Mission Control **Content** tab reads `agents/<agent>/content/*.md`. Long-form work saved only in chat is invisible there.

## Folders (own folder only)

| Agent | Path |
|-------|------|
| Hermes | `agents/hermes/content/` |
| Iris | `agents/iris/content/` |
| Clio | `agents/clio/content/` |
| Odysseus | `agents/odysseus/content/` |
| Hephaestus | `agents/hephaestus/content/` |

Never write into another agent's `content/`.

## Filename

- **Markdown only:** `.md` (no `.txt`, no chat dumps).
- **Pattern:** `YYYY-MM-DD_short-kebab-case-title.md`
- Example: `2026-07-01_acme-cloud-intel.md` — lowercase, hyphens, no spaces or special characters.

## First line

```markdown
# Human-readable title matching the document purpose
```

The Content tab uses this as the display title (not the filename slug).

## Body

Use proper markdown: `##` / `###`, **bold**, `inline code`, fenced blocks with language tags, bullet lists where helpful.

## Long-form vs inline chat

**Save to folder:** articles, research summaries, scripts, outreach drafts, strategy docs, meeting notes, technical guides, post-mortems, anything meant to be reread or reused (~15+ lines or multi-section).

**Inline in chat:** one-line answers, quick status, confirmations, tool output, conversational replies.

## File rules

1. **One document per file.** Multiple deliverables → multiple files.
2. **No silent overwrite.** On collision, use `-v2`, `-v3`, or a more specific title.
3. **Stay in lane.** Role-fit content only; hand off out-of-scope work (see each agent `AGENTS.md`).

## After saving

Confirm in chat with agent name, full repo-relative path, one-line summary, and **MC preview link** when under `agents/*/content/` (see `CHAT_FILE_LINK_POLICY.md`):

```text
Iris → agents/iris/content/2026-07-01_acme-cloud-intel.md — competitive analysis of six platforms.
Preview: http://127.0.0.1:51763/#content/iris/2026-07-01_acme-cloud-intel.md
```

## Paths

Follow root `AGENTS.md` **file mutation** rules: project-root cwd or `C:/Users/benma/ariadnes-thread-os/...`; never `/c/Users/...` in write tools.

## Related

- Activity logging: `agents/_shared/LOGGING_POLICY.md`
- Roster: `agents/REGISTRY.yaml` → `content_delivery`