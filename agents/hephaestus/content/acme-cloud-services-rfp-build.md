# Mission Control feed — ACME Cloud Services RFP

**Quest:** acme-cloud-services-rfp  
**Builder:** Hephaestus (triggered by Odysseus dashboard registration)  
**Date:** 2026-06-30

## Artifact manifest (for Thread Tavern / Mission Control)

When dashboard shell is live, index these paths:

```json
{
  "quest_slug": "acme-cloud-services-rfp",
  "title": "ACME Cloud Services RFP",
  "status": "ratified_ms2_conditional",
  "tiles": [
    {"agent": "hermes", "type": "quest", "path": "agents/hermes/content/quests/acme-cloud-services-rfp/"},
    {"agent": "iris", "type": "intel", "path": "agents/iris/content/acme-cloud-services-rfp-intel.md"},
    {"agent": "clio", "type": "packet", "path": "agents/clio/content/acme-cloud-services-rfp-packet.md"},
    {"agent": "odysseus", "type": "gate", "path": "agents/odysseus/content/acme-cloud-services-rfp-gate-review.md"}
  ]
}
```

## Build note

No MCP build required for this pipeline run. Future: USAspending poller MCP → auto-refresh Iris intel tile.