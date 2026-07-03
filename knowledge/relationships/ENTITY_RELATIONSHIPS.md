# Entity relationships (party consensus)

**Overwatch rule (2026-07-02):** Never place **company org profiles** under `customers/` (federal buying side). Customers are **funding/contracting orgs and programs only**.

**Phase 3b (2026-07-02):** One folder per side — `customers/` and `companies/`; competitor/partner nuance on **one company page** via `relationship_to_us`, not separate folders.

## One org, one canonical entity page

| `type` | Folder | Example |
|--------|--------|---------|
| `company` (+ `org_role: self` for KBR BU) | `entities/companies/` | KBR RS BU |
| `customer_*` | `entities/customers/` | LOGCAP, Army funding office |

## Roles on opportunities (links, not duplicate pages)

Use **frontmatter + wikilinks**, not a second vault tree:

```yaml
# On entities/companies/acme-defense-llc.md
relationship_to_us: [competitor, teammate]
related_customers: ["dept-of-army-xyz"]
pursuit_roles:
  - pursuit_slug: army-rrad-sustainment-2027
    role: competitor
```

On `pursuits/<slug>/README.md`:

```yaml
entities:
  - id: entity-company-acme-defense
    role: competitor
  - id: entity-company-kbr-services-readiness-sustainment
    role: prime
```

**Graph / relationships/** — optional future `relationships/` edges mirroring the same facts.

## Party views

- **Hermes:** Triage enforces folder by `type`; uncertain org → morning queue.
- **Iris:** Enriches customer/company pages; never files a prime under `customers/`.
- **Clio:** Pursuit README holds opp-specific role matrix; links entity pages.
- **Odysseus:** Promote requires role clarity + citation; no trusted claim without source.
- **Hephaestus:** Lint duplicate entity names across folders; INDEX lists by zone layout.