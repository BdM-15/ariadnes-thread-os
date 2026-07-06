#!/usr/bin/env python3
"""Phase 3 Shipley Capture Guide — additional concepts + hub update. Run from repo root."""
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
    "shipley-capture-manager-role-capture.md": (
        "Capture manager role in capture",
        "global-shipley-capture-manager-role",
        "extract pages:29-30,35-38 | chapter:Capture Team Selection and Management",
        """# Capture manager role in capture

The **capture manager** is responsible for winning or losing the opportunity. The role is often assigned to sales or business development leads on smaller pursuits; on the largest opportunities it may sit with program, BD, or line management. The person needs customer and market knowledge, sales savvy, proposal experience, leadership, broad technical understanding, and enthusiasm—advocating the customer's position while driving win strategy, competitive analysis, price-to-win, and customer interface within the customer's rules.

**Core duties (adapt to org size):** Own capture plan and strategy; manage customer contact through program start-up; lead competitive and cost targeting analysis; drive decision gate reviews; draft the first executive summary; mentor the proposal core team on win strategy and solution; support color team reviews.

**Practice:** Pair every capture manager with a senior leadership sponsor; define distinct responsibilities versus proposal manager, program manager, and pricing specialist (one person may wear multiple hats on small bids).

**Links:** [[shipley-decision-gate-reviews]] [[shipley-proposal-handoff-capture]] [[shipley-customer-alignment-capture]]

## Related

[[shipley-capture-guide-hub]] [[shipley-win-strategy-development-capture]] [[capture-planning-phase]]
""",
    ),
    "shipley-executive-summary-capture.md": (
        "Executive summaries in capture",
        "global-shipley-executive-summary-capture",
        "extract pages:80-85 | chapter:Executive Summaries",
        """# Executive summaries in capture

In capture, the **executive summary** is a living sales document—not a recycled proposal boilerplate. The capture manager typically develops the first draft; the proposal manager completes and aligns it with the proposal strategy. Content should trace to the capture plan: customer vision, hot buttons in priority order, benefits before features, discriminators, and proof including past performance.

**Practice:** Use the Executive Summary Planning Worksheet and four-box Organizer (hot-button–centric layout) instead of search-and-replace from prior bids. Refresh the draft as strategy and solution evolve during capture.

**Links:** [[shipley-capture-manager-role-capture]] [[shipley-solution-development-capture]] [[executive-summary-writing-rules]]

## Related

[[shipley-capture-guide-hub]] [[shipley-win-strategy-development-capture]] [[storyboard-content-plan]]
""",
    ),
    "shipley-oral-presentations-capture.md": (
        "Oral presentations and customer briefings in capture",
        "global-shipley-oral-presentations-capture",
        "extract pages:18,91-94 | chapter:Presentations to Customers",
        """# Oral presentations and customer briefings in capture

**Customer presentations** advance the same opportunity as the written proposal; inconsistency between what you say and submit erodes credibility. Capture-phase briefings usually persuade toward your solution, convey information, or clarify the offer. The process framework treats oral presentation, draft executive summary, and sales presentation as phase-5/6 artifacts alongside storyboards and color-team drafts.

**Practice:** Align presentation structure with the executive summary to save time and keep one message; state presentation objective and desired next step up front; organize by customer priorities; adjust graphics and emphasis for the medium (live, virtual, video-heavy competitions).

**Links:** [[shipley-executive-summary-capture]] [[shipley-customer-alignment-capture]] [[shipley-color-team-reviews-capture]]

## Related

[[shipley-capture-guide-hub]] [[shipley-executive-summary-capture]] [[proposal-development-phase]]
""",
    ),
    "shipley-past-performance-capture.md": (
        "Past performance in capture",
        "global-shipley-past-performance-capture",
        "extract pages:48-49,83-84,125-127 | past performance in solution development and competitive reviews",
        """# Past performance in capture

**Past performance** is shaped during capture, not invented at proposal writing. Solution development explicitly coordinates relevant examples that align with the offer; executive-summary planning includes proof and experience under each hot button. Competitive reviews (e.g., Black Hat) also assess competitors' past performance to refine win strategy.

**Practice:** Map contracts and outcomes early with the solution team; select examples that substantiate discriminators the customer cares about; feed the same proof into presentations and the executive summary for message alignment.

**Links:** [[shipley-solution-development-capture]] [[shipley-competitive-intelligence-capture]] [[shipley-executive-summary-capture]]

## Related

[[shipley-capture-guide-hub]] [[shipley-win-strategy-development-capture]] [[black-hat-review]]
""",
    ),
    "shipley-solution-development-capture.md": (
        "Technology and solution development in capture",
        "global-shipley-solution-development-capture",
        "extract pages:125-129 | chapter:Solution Development",
        """# Technology and solution development in capture

**Solution development** during capture designs consistent technical and management approaches, coordinates past performance, and bounds a winning price window. The capture manager helps gather customer-informed solution direction; early collaboration with technical leads shares intelligence from customer interactions. Plan five pursuit topics: technical approach, management approach, past performance, price/competitive range, and risk identification and retirement.

**Practice:** Collaborate with the customer on a notional solution (avoid forcing a predetermined product); link solution explicitly to requirements and hot buttons; set a solution freeze date; present the matured solution at proposal kickoff so the final proposal feels familiar.

**Links:** [[shipley-past-performance-capture]] [[shipley-pricing-cost-capture]] [[shipley-risk-capture]]

## Related

[[shipley-capture-guide-hub]] [[shipley-capture-manager-role-capture]] [[capture-planning-phase]]
""",
    ),
    "shipley-metrics-kpis-capture.md": (
        "Metrics and KPIs for capture and business development",
        "global-shipley-metrics-kpis-capture",
        "extract pages:21-22,582-584 | framework principle 10; Figure 3 business development metrics",
        """# Metrics and KPIs for capture and business development

Disciplined capture depends on **metrics** for continuous improvement—cycle times, proposal quality, pipeline value, win/loss, capture budget versus actual, and pre-RFP spend, among others. A designated process owner collects credible metrics as by-products of normal work (e.g., time sheets), balances collection cost against use, and avoids overlapping measures unless comparing which best represents performance.

**Practice:** Before tracking a metric, define how leadership will act on it; skip data on organizations you cannot influence; use before-and-after trends to justify process investment and gate discipline.

**Links:** [[shipley-lessons-learned-capture]] [[shipley-decision-gate-reviews]] [[shipley-business-development-lifecycle]]

## Related

[[shipley-capture-guide-hub]] [[shipley-capture-plan-templates-checklists]] [[shipley-lessons-learned-capture]]
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
    if "Major topics (phase 3 concepts)" not in hub:
        insert = """
## Major topics (phase 3 concepts)

| Topic | Vault page |
|-------|------------|
| Capture manager role | [[shipley-capture-manager-role-capture]] |
| Executive summaries in capture | [[shipley-executive-summary-capture]] |
| Oral presentations & briefings | [[shipley-oral-presentations-capture]] |
| Past performance in capture | [[shipley-past-performance-capture]] |
| Solution / technology development | [[shipley-solution-development-capture]] |
| Metrics & KPIs | [[shipley-metrics-kpis-capture]] |

"""
        hub = hub.replace("## Ariadne capture loop", insert + "## Ariadne capture loop")
        hub = hub.replace("last_updated: 2026-07-06", f"last_updated: {TODAY}")
        if "## Added/Updated" in hub and "Phase 3 concepts" not in hub:
            hub = hub.rstrip() + "\n\nPhase 3 concepts (capture manager, executive summary, oral presentations, past performance, solution development, metrics/KPIs).\n"
        HUB.write_text(hub, encoding="utf-8")
        print("updated hub")

    log = REPO / "knowledge/log.md"
    entry = f"\n| {TODAY} | shipley | phase3 | hub + 6 concepts (capture manager, exec summary, oral, PP, solution dev, metrics) |\n"
    log_text = log.read_text(encoding="utf-8")
    if "shipley | phase3" not in log_text:
        log.write_text(log_text + entry, encoding="utf-8")
        print("appended log")


if __name__ == "__main__":
    main()