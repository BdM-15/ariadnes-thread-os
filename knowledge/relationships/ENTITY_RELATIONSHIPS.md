# Entity relationships (party consensus)

**Overwatch rule (2026-07-02):** Never place **company/competitor org profiles** under `agencies/` (customers). Agencies are **customers/funding orgs only**.

## One org, one canonical entity page

| `type` | Folder | Example |
|--------|--------|---------|
| `company` | `entities/company/` | KBR RS BU |
| `competitor` | `entities/competitors/` | Other offerors |
| `agency` | `entities/agencies/` | DoD customers |

## Roles on opportunities (links, not duplicate pages)

Use **frontmatter + wikilinks**, not a second vault tree:

```yaml
# On entities/competitors/acme-corp.md
related_agencies: ["dept-of-army-xyz"]   # customer relationships
pursuit_roles:
  - pursuit_slug: army-rrad-sustainment-2027
    role: competitor   # or partner, teammate, subcontractor
```

On `pursuits/<slug>/README.md`:

```yaml
entities:
  - id: entity-competitor-acme
    role: competitor
  - id: entity-company-kbr-services-readiness-sustainment
    role: prime
```

**Graph / relationships/** — optional future `relationships/` edges mirroring the same facts.

## Party views

- **Hermes:** Triage enforces folder by `type`; uncertain org → morning queue.
- **Iris:** Enriches competitor/agency pages; never files a prime under `agencies/`.
- **Clio:** Pursuit README holds opp-specific role matrix; links entity pages.
- **Odysseus:** Promote requires role clarity + citation; no trusted claim without source.
- **Hephaestus:** Lint duplicate entity names across folders; INDEX lists by type.