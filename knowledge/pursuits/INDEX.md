# Pursuits zone

**Where to start:** One folder per tracked opportunity.

## Folder naming (agent-default)

Use **human slug** (lowercase, hyphens, ≤48 chars):

```text
pursuits/<agency-short>-<program-or-title>-<fy>/
  README.md          # pursuit SSOT: status, links, summary
  notes/             # optional dated intel (optional v1)
```

**Examples:** `army-rrad-sustainment-2027`, `dla-it-om-fy26`

When a **SAM notice ID** exists, put it in README frontmatter — do not use raw notice ID as folder name unless no title yet:

```yaml
sam_notice_id: "NOTICE-12345"
display_name: "Army RRAD Sustainment"
pursuit_slug: army-rrad-sustainment-2027
```

Overwatch can read `display_name` + `README.md`; agents use `pursuit_slug` for routing.

## Rules

- Pursuit-specific only — company-wide doctrine stays `entities/companies/` + `global/domain_intel/`.
- Link entities: `[[kbr-services-readiness-sustainment]]`, agencies, competitors in README.

## Maintainer

Clio (narrative) · Hermes (slug on new opp) · Hephaestus (scaffold)