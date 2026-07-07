#!/usr/bin/env python3
"""Idempotent stubs for deferred wikilink targets (doc 02 hygiene).

Creates minimal trusted pages so vault_lint unresolved count reaches 0 without
full data-elements/ ontology (see foundation/reference/briefing-packet-data-dictionary.md).
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VAULT = REPO_ROOT / "knowledge" / "thread"

DATA_ELEMENT_KEYS = (
    "acquisition_capture_progress",
    "action_plan_items",
    "award_date",
    "basis_of_evaluated_price",
    "bookable_revenue",
    "bp_funding_request_amount",
    "bp_notes",
    "business_case_rows",
    "business_case_summary",
    "business_unit",
    "business_unit_division",
    "capture_manager",
    "consultants",
    "contract_end_date",
    "contract_start_date",
    "cost_price_evaluation_method",
    "customer_name",
    "customer_need_funding_status",
    "draft_rfp_date",
    "evaluation_document_date",
    "execution_risks",
    "milestone_1",
    "milestone_2",
    "milestone_3",
    "milestone_4",
    "non_us_persons_participate",
    "opportunity_shaping_customer_engagement_current_status",
    "opportunity_shaping_customer_engagement_next_steps",
    "opportunity_shaping_customer_engagement_previous_status",
    "opportunity_shaping_customer_engagement_status_update",
    "other_teaming_capex_facilities_current_status",
    "other_teaming_capex_facilities_next_steps",
    "proposal_risks",
)

TEMPLATE_PLACEHOLDERS = (
    ("agency-name", "agency", "Example agency page name in Related section"),
    ("competitor-name", "competitor", "Example competitor page name in Related section"),
    ("opportunity_name", "data-element", "Briefing packet field key (see data dictionary)"),
)

EXTRA_PAGES: dict[str, tuple[str, str]] = {
    "entities/entities.md": (
        "meta",
        """# Entities zone hub

**Where to start:** Read [[INDEX]] then `agencies/`, `competitors/`, or `company/`.

## Related
- [[INDEX]]
- [[capture-llm-wiki]]
""",
    ),
    "entities/agencies/dhs.md": (
        "agency",
        """# Department of Homeland Security (DHS)

Stub agency page for wikilink graph connectivity. Enrich via Iris intel promote.

## Related
- [[capture-llm-wiki]]
- [[entities/entities]]
""",
    ),
    "global/global_wiki/capture/concepts/usaspending-plain-english.md": (
        "concept",
        """# USAspending — plain English

How agents should interpret USAspending fields when grounding vault claims (Layer 1 cite, wiki synthesizes).

## Related
- [[follow-the-money]]
- [[capture-llm-wiki]]
- [[thread-role]]
""",
    ),
    "data-elements/INDEX.md": (
        "meta",
        """# Data elements (deferred ontology)

**Where to start:** Packet field keys link here as stubs until Wave 2 `data-elements/` depth.

**Canonical reference:** [[briefing-packet-data-dictionary]] in `foundation/reference/`.

## Archive boundary
Stubs only — not bid execution truth; PostgreSQL holds packet values.

## Maintainer
Clio (field semantics) · Hephaestus (stub sync)
""",
    ),
}


def _stub_body(key: str, el_type: str, note: str) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return f"""---
name: "{key}"
type: {el_type}
id: data-element-{key.replace('/', '-')}
trust: trusted
last_updated: {now}
citations: "foundation/reference/briefing-packet-data-dictionary.md"
tags: [data-element, stub, doc-02]
---

# {key}

{note}

**Dictionary:** [[briefing-packet-data-dictionary]]

## Related
- [[capture-llm-wiki]]
"""


def _write_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> int:
    created = 0
    dict_link = "briefing-packet-data-dictionary"

    for key in DATA_ELEMENT_KEYS:
        body = _stub_body(
            key,
            "data-element",
            "Briefing packet field stub (doc 02). Full ontology deferred.",
        )
        if _write_if_missing(VAULT / "data-elements" / f"{key}.md", body):
            created += 1

    for name, (el_type, body) in TEMPLATE_PLACEHOLDERS:
        if name == "opportunity_name":
            path = VAULT / "data-elements" / "opportunity_name.md"
        else:
            path = VAULT / "data-elements" / f"{name}.md"
        fm = _stub_body(name, el_type, "Template placeholder stub for schema examples.")
        if _write_if_missing(path, fm):
            created += 1

    # Path-style link used in capture-llm-wiki prose
    opp_path = VAULT / "data-element" / "opportunity_name.md"
    if _write_if_missing(
        opp_path,
        _stub_body("opportunity_name", "data-element", "Alias path for [[data-element/opportunity_name]]."),
    ):
        created += 1

    for rel, (page_type, body) in EXTRA_PAGES.items():
        now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        content = f"""---
name: "{Path(rel).stem}"
type: {page_type}
id: stub-{Path(rel).stem}
trust: trusted
last_updated: {now}
citations: "scripts/seed_deferred_wikilink_stubs.py"
---

{body}
"""
        if _write_if_missing(VAULT / rel, content):
            created += 1

    # Alias stem `dhs` → same as agencies/dhs (separate file with alias frontmatter)
    dhs_alias = VAULT / "entities" / "agencies" / "dhs.md"
    if dhs_alias.exists():
        dhs_root = VAULT / "dhs.md"
        if _write_if_missing(
            dhs_root,
            """---
name: "DHS"
type: agency
id: entity-agency-dhs-alias
trust: trusted
aliases: [dhs, Department of Homeland Security]
---

# DHS (alias)

See canonical page: [[entities/agencies/dhs]].
""",
        ):
            created += 1

    print(f"Created {created} stub(s). Dictionary anchor: {dict_link}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())