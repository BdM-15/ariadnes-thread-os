---
auto_generated: true
entity_type: concept
id: global-labor-hour-calculation-methodology
last_updated: 2026-06-18
name: "Labor Hour Calculation Methodology"
source_module: workload
title: "Labor Hour Calculation Methodology"
trust: trusted
type: concept
updated: "'2026-04-22T23:01:17'"
---

> **Entity type:** `concept`

Standard methodology for calculating labor hours from workload: (1) Identify workload drivers (tickets/month, systems, users, deliverables), (2) Determine task time standards (hours per ticket, hours per system), (3) Calculate raw hours (driver × time standard), (4) Apply productivity factors (available hours vs calendar hours), (5) Add supervision/management overhead (typically 10-15%), (6) Apply skill mix (senior vs junior ratios). Formula: FTEs = (Annual Workload × Hours/Unit) ÷ (Annual Available Hours × Utilization). Document all inputs and assumptions for traceability.

## Related
- [[ariadne-vault-schema]]
- [[utilization-rate-standards]]
- [[basis-of-estimate-development]]
- [[service-desk-staffing-model]]
- [[test-and-quality-assurance-staffing]]
- [[system-administration-staffing-ratios]]
- [[software-development-staffing-model]]
- [[agile-capacity-estimation]]
