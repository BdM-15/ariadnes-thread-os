# Chat file preview links (all agents + Hermes to Overwatch)

When you cite a **filename** or deliverable path in chat to Overwatch, include a **clickable preview link** (not path alone).

## Agent content (`agents/<agent>/content/*.md`)

Mission Control **Content** tab (requires MC running, default `http://127.0.0.1:51763`):

```text
http://127.0.0.1:51763/#content/<agent>/<filename>
```

**Markdown in chat:**

```markdown
[Human-readable title](http://127.0.0.1:51763/#content/hephaestus/2026-07-02_example.md)
```

- `<agent>`: `hermes` | `iris` | `clio` | `odysseus` | `hephaestus`
- `<filename>`: exact `.md` basename (URL-encode if needed)

## Other repo paths (`docs/`, `knowledge/`, scripts, etc.)

No MC preview yet—give repo-relative path **and** absolute path for editor open:

```text
docs/inspiration/knowledge-vault-and-compounding-truth.md
C:/Users/benma/ariadnes-thread-os/docs/inspiration/knowledge-vault-and-compounding-truth.md
```

When a doc is **only** under `docs/`, Hermes may note: *Open in IDE or copy to agent `content/` if you want MC preview.*

## After saving long-form (extends CONTENT_DELIVERY_POLICY)

Confirm with agent, path, one-line summary, **and** preview link when file is under `agents/*/content/`.

## Hermes to Overwatch

Hermes **must** follow this policy on every message that names a file for review or reading.