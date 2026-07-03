---
added: "2026-07-02T20:00:00Z"
citations: "Hermes entities hierarchy design 2026-07-02"
id: entity-customer-us-federal-hub
last_updated: 2026-07-02
name: "US Federal customers (hub)"
trust: trusted
type: customer_root
tags: [customers, hub, federal]
---

# US Federal customer hub

**Outline index** for federal buying-side entities. Individual customers are **flat slugs** under `customers/` — hierarchy is `parent_customer` wikilinks, not nested folders.

## Mental model

```text
Customer (federal market)
  └── Agency (e.g. Department of the Army)
        └── Subagency / Service
              └── Funding office (program / PEO owner)
                    └── Contracting office(s)
                    └── Program (LOGCAP, AFCAP) when capture-relevant
```

## Branches (incremental)

| Branch | Status | Anchor programs |
|--------|--------|-----------------|
| Army | *stub — promote from Iris/USAspending* | LOGCAP (parent slugs TBD at promote) |
| Air Force | *stub — promote from Iris/USAspending* | AFCAP (parent slugs TBD at promote) |

## Customer `type` values

| type | Use for |
|------|---------|
| `customer_root` | This hub only |
| `customer_agency` | Dept / top-tier agency |
| `customer_subagency` | Service, command, PEO-level |
| `customer_office_funding` | Funds requirements / owns program |
| `customer_office_contracting` | Awards contracts |
| `customer_program` | Named program (LOGCAP, AFCAP) |

## Related

- [[entities/INDEX]]
- [[ENTITY_RELATIONSHIPS]]
- [[capture-llm-wiki]]