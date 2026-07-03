---
id: domain-intel-thread-role
last_updated: 2026-06-18
name: "Domain Intel — Thread Role"
trust: trusted
type: meta
tags:
  - domain-intel
  - bid-no-bid
  - uei
---

# Domain Intel in Ariadne's Thread

**Tier purpose:** Company-specific bid fit — not generic doctrine (`global_wiki/`) and not per-RFP (`pursuits/`).

## LLM uses this for
- **Bid / no-bid** — match opportunity signals (USAspending, SAM.gov, web research) against `capabilities/`
- **Past performance awareness** — crosswalk recipient UEI / award history to what we can credibly claim (`uei/`)
- **Focus** — filter noise; large orgs cannot manually digest all contract history

## Rules
- Append new capability or UEI synthesis; do not overwrite trusted entries without review
- Cite Layer 1: `award_key`, SAM notice ID, scrape URL, PG row
- Promote packet fields via review gate — wiki informs, PostgreSQL executes

## Related

- [[ariadne-vault-schema]]
- [[usaspending-plain-english]]
- [[domain-intel]]
- [[follow-the-money]]
- [[capture-intensity]]
- [[market-concentration]]
- [[entities]]
- [[strategy-lens]]
