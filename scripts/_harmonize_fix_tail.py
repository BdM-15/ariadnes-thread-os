#!/usr/bin/env python3
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
wl = REPO / "knowledge/foundation/reference/wikilinks.md"
t = wl.read_text(encoding="utf-8")
t = t.replace(
    "Vault pages connect via `[[slug]]`.",
    "Vault pages connect via Obsidian double-bracket link syntax.",
)
wl.write_text(t, encoding="utf-8", newline="\n")

now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
army = REPO / "knowledge/entities/customers/department-of-the-army.md"
if not army.exists():
    army.parent.mkdir(parents=True, exist_ok=True)
    army.write_text(
        f"""---
name: Department of the Army
type: customer_agency
id: customer-agency-army
trust: trusted
last_updated: {now}
citations: ariadne-vault-schema
tags: [stub, harmonize-h1-h2]
---

# Department of the Army

Stub customer agency page. Enrich via Iris promote.

## Related
- [[army-logcap-funding-office]]
- [[logcap]]
""",
        encoding="utf-8",
        newline="\n",
    )
print("fix_tail ok")