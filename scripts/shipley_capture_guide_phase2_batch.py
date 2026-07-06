#!/usr/bin/env python3
"""Phase 2 Shipley Capture Guide — additional concepts + hub update. Run from repo root."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = "2026-07-06"
CONCEPTS = REPO / "knowledge/global/domain_intel/concepts"
HUB = CONCEPTS / "shipley-capture-guide-hub.md"


def fm(**kwargs: str) -> str:
    lines = ["---"]
    for k, v in kwargs.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


PAGES = {
    "shipley-capture-plan-templates-checklists.md": (
        "Capture plan templates and checklists",
        "global-shipley-capture-plan-templates",
        "extract pages:189-216, templates/checklists sections",
        """# Capture plan templates and checklists

The guide treats the **capture plan** as a documented, action-oriented plan whose quality depends on planners and sound structure—not a one-size-fits-all form. Templates and checklists standardize repeatable elements (customer understanding, competitive position, win themes, teaming, schedule, risks) while remaining adaptable to opportunity size and market.

**Practice:** When developing or adapting a capture plan template, use the guide's sample templates and checklists as patterns—align fields to your organization's gate reviews and proposal handoff, not to generic boilerplate.

**Links:** [[shipley-capture-planning-overview]] [[shipley-decision-gate-reviews]] [[shipley-win-strategy-development-capture]]

## Related

[[shipley-capture-guide-hub]] [[shipley-capture-planning-overview]] [[shipley-decision-gate-reviews]]
""",
    ),
    "shipley-teaming-partnering-capture.md": (
        "Teaming and partnering in capture",
        "global-shipley-teaming-partnering",
        "extract: teaming, subcontractor, partner sections",
        """# Teaming and partnering in capture

Capture planning includes **teaming strategy**: who fills capability gaps, how work share supports customer preference, and how partners are vetted before commitment. The guide emphasizes early partner engagement aligned with customer perception and competitive reality—not last-minute logo slides.

**Practice:** Document partner roles, discriminators contributed, and governance (who owns customer relationships) in the capture plan before major proposal investment.

**Links:** [[shipley-competitive-intelligence-capture]] [[shipley-customer-alignment-capture]]

## Related

[[shipley-capture-guide-hub]] [[shipley-competitive-intelligence-capture]]
""",
    ),
    "shipley-pricing-cost-capture.md": (
        "Pricing and cost in capture",
        "global-shipley-pricing-cost",
        "extract: cost, price-to-win, affordability sections",
        """# Pricing and cost in capture

**Price-to-win** and affordability analysis belong in capture—not only in proposal pricing volumes. The guide ties cost realism to win strategy: understanding customer budget signals, competitor cost posture (where knowable), and your own cost discriminators without undermining deliverability.

**Practice:** Integrate cost/capture leads into gate reviews; avoid optimistic pricing that collapses at Blue/Pink team or post-award.

**Links:** [[shipley-win-strategy-development-capture]] [[shipley-decision-gate-reviews]]

## Related

[[shipley-capture-guide-hub]] [[shipley-win-strategy-development-capture]]
""",
    ),
    "shipley-proposal-handoff-capture.md": (
        "Proposal handoff from capture",
        "global-shipley-proposal-handoff",
        "extract: proposal transition, handoff, proposal manager sections",
        """# Proposal handoff from capture

A disciplined **handoff** transfers capture intelligence—win themes, customer hot buttons, competitive assessment, risks, and solution intent—to the proposal team. The guide positions capture managers and proposal managers as partners with a shared customer preference goal; weak handoff produces generic proposals.

**Practice:** Use structured handoff meetings and annotated capture plans; align with [[shipley-color-team-reviews-capture]] schedule.

**Links:** [[shipley-capture-planning-overview]] [[shipley-color-team-reviews-capture]]

## Related

[[shipley-capture-guide-hub]] [[shipley-color-team-reviews-capture]]
""",
    ),
    "shipley-risk-capture.md": (
        "Risk in capture planning",
        "global-shipley-risk-capture",
        "extract: risk identification, mitigation in capture plan",
        """# Risk in capture planning

Capture plans should surface **technical, programmatic, competitive, and customer risks** with mitigations and triggers—not only proposal-phase risk registers. Gate reviews use risk posture to decide pursue/hold/no-bid.

**Practice:** Pair with Ariadne pursuit gates; escalate compliance or eligibility risks to Odysseus lane before MS investment.

**Links:** [[shipley-decision-gate-reviews]] [[pursuit-decision-phase]]

## Related

[[shipley-capture-guide-hub]] [[shipley-decision-gate-reviews]]
""",
    ),
    "shipley-lessons-learned-capture.md": (
        "Lessons learned in capture",
        "global-shipley-lessons-learned",
        "extract: lessons learned, continuous improvement",
        """# Lessons learned in capture

Effective organizations institutionalize **lessons learned** from wins and losses: what influenced customer preference, what gate decisions were right or wrong, and what capture artifacts were missing. The guide treats this as compounding effectiveness—not a post-mortem checkbox.

**Practice:** Feed outcomes back into templates, checklists, and [[shipley-competitive-intelligence-capture]] sources.

## Related

[[shipley-capture-guide-hub]] [[shipley-capture-plan-templates-checklists]]
""",
    ),
}


def main() -> None:
    for fname, (title, vid, cites, body) in PAGES.items():
        path = CONCEPTS / fname
        text = fm(
            name=title,
            type="synthesis",
            id=vid,
            trust="trusted",
            reviewed_by="axelrod2023",
            reviewed_at=NOW,
            added=NOW,
            last_updated=TODAY,
            citations=f"source:Shipley Capture Guide.pdf | extract:Shipley-Capture-Guide-extract.md | {cites}",
            tags="[shipley, capture, doctrine]",
        ) + "\n" + body
        path.write_text(text, encoding="utf-8")
        print("wrote", path.relative_to(REPO))

    hub = HUB.read_text(encoding="utf-8")
    if "Phase 2 topics" not in hub:
        insert = """
## Major topics (phase 2 concepts)

| Topic | Vault page |
|-------|------------|
| Capture plan templates & checklists | [[shipley-capture-plan-templates-checklists]] |
| Teaming & partnering | [[shipley-teaming-partnering-capture]] |
| Pricing & cost | [[shipley-pricing-cost-capture]] |
| Proposal handoff | [[shipley-proposal-handoff-capture]] |
| Risk in capture | [[shipley-risk-capture]] |
| Lessons learned | [[shipley-lessons-learned-capture]] |

"""
        hub = hub.replace("## Ariadne capture loop", insert + "## Ariadne capture loop")
        hub = hub.replace("last_updated: 2026-07-06", f"last_updated: {TODAY}")
        if "## Added/Updated" in hub:
            hub += "\nPhase 2 concepts (templates, teaming, pricing, handoff, risk, lessons learned).\n"
        HUB.write_text(hub, encoding="utf-8")
        print("updated hub")

    log = REPO / "knowledge/log.md"
    entry = f"\n| {TODAY} | shipley | phase2 | hub + 6 concepts (Hermes in-session retry after deleg OAuth fail) |\n"
    if "shipley | phase2" not in log.read_text(encoding="utf-8"):
        log.write_text(log.read_text(encoding="utf-8") + entry, encoding="utf-8")
        print("appended log")


if __name__ == "__main__":
    main()