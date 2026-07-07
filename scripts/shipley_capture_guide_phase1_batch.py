#!/usr/bin/env python3
"""Phase 1 Shipley Capture Guide foundational ingest - single batch write from repo root."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
TODAY = "2026-07-06"


def fm(**kwargs: str) -> str:
    lines = ["---"]
    for k, v in kwargs.items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def write_all() -> list[Path]:
    written: list[Path] = []

    def w(rel: str, body: str) -> None:
        p = REPO / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
        written.append(p)

    w(
        "knowledge/foundation/reference/shipley-capture-guide-source.md",
        fm(
            name="Shipley Capture Guide - source citation",
            type="reference",
            id="foundation-shipley-capture-guide-source",
            trust="trusted",
            reviewed_by="axelrod2023",
            reviewed_at=NOW,
            added=NOW,
            last_updated=TODAY,
            citations=(
                "source:docs/shipley guides/Shipley Capture Guide.pdf"
                " | extract:knowledge/foundation/raw/shipley/Shipley-Capture-Guide-extract.md"
                " | edition:Fifth Edition | author:Larry Newman | publisher:Shipley Associates"
                " | isbn:978-0-9990168-7-9"
            ),
            tags="[shipley, capture, reference, foundation]",
        )
        + """

# Shipley Capture Guide - locked source citation

**Purpose:** Cite the Overwatch-provided PDF and the immutable raw extract. Vault writers paraphrase from the extract; do not paste full chapters into trusted pages.

## Primary source

| Field | Value |
|-------|-------|
| Title | Shipley Capture Guide (Fifth Edition) |
| Author | Larry Newman, CPP APMP Fellow |
| Publisher | Shipley Associates (2022) |
| PDF path | `docs/shipley guides/Shipley Capture Guide.pdf` |
| Raw extract | `knowledge/foundation/raw/shipley/Shipley-Capture-Guide-extract.md` (~197 pages, trust: raw) |
| Ingested (raw) | 2026-07-06 |

## Copyright notice

No part of this publication may be reproduced, stored in a retrieval system, or transmitted in any form without prior written permission from Shipley Associates. Trademarked names appear in an editorial fashion to the benefit of the trademark owner. 2022 Shipley Associates, Fifth Edition, ISBN 978-0-9990168-7-9.

**Agent rule:** Summarize and cite page references from the extract; do not reproduce extended copyrighted passages.

## Trusted synthesis entry points

- Hub: [[shipley-capture-guide-hub]]
- Schema: [[ariadne-vault-schema]]

## Related

[[shipley-capture-guide-hub]] [[ariadne-vault-schema]] [[shipley-business-development-lifecycle]]

## Added/Updated """
        + TODAY
        + """

Phase 1 foundational cite locked; raw extract remains trust: raw in foundation/raw/shipley/.
""",
    )

    hub_fm = fm(
        name="Shipley Capture Guide - hub",
        type="synthesis",
        id="global-shipley-capture-guide-hub",
        trust="trusted",
        reviewed_by="axelrod2023",
        reviewed_at=NOW,
        added=NOW,
        last_updated=TODAY,
        citations="source:docs/shipley guides/Shipley Capture Guide.pdf | extract:Shipley-Capture-Guide-extract.md | pages:preface-iv,contents-vii",
        tags="[shipley, capture, hub, doctrine]",
        aliases='[Shipley Capture Guide hub]',
    )
    w(
        "knowledge/global/domain_intel/concepts/shipley-capture-guide-hub.md",
        hub_fm
        + """

# Shipley Capture Guide - hub (Fifth Edition)

Quick-reference capture doctrine from Larry Newman's Shipley Capture Guide (5th ed.). Full text lives in the raw extract; this hub orients Ariadne agents to objectives, principles, and phase-1 concept pages.

**Source lock:** [[shipley-capture-guide-source]] | raw: `knowledge/foundation/raw/shipley/Shipley-Capture-Guide-extract.md`

## Three guide objectives (preface)

1. Help individuals and organizations capture competitive business opportunities more effectively, economically, and consistently.
2. Guide capture and sales roles to understand and adapt best practices for opportunities in any market.
3. Document best-practice capture management and planning guidelines (companion to Proposal Guide and Business Development Lifecycle Guide).

## Five fundamental principles (preface)

1. Align capture activities with the customer's needs and selection process.
2. Influence the customer to prefer your organization and solution early, and maintain that preference through selection, award, and delivery.
3. Base strategy on the customer's perspective of reality.
4. Align actions and messages throughout the business development cycle.
5. Use decision gate reviews of potential opportunities to determine how best to proceed.

## Major topics (phase 1 concepts)

| Topic | Vault page |
|-------|------------|
| Capture planning overview | [[shipley-capture-planning-overview]] |
| Customer alignment | [[shipley-customer-alignment-capture]] |
| Decision gate reviews | [[shipley-decision-gate-reviews]] |
| Color team reviews | [[shipley-color-team-reviews-capture]] |
| Win strategy development | [[shipley-win-strategy-development-capture]] |
| Competitive intelligence | [[shipley-competitive-intelligence-capture]] |

## Ariadne capture loop

Hermes supervises the nine-step capture loop (intake through ratify). Operational spec: `agents/CAPTURE_LOOP_SUPERVISOR.md` (triggers: Run capture loop on ..., `/capture-loop`).

Doctrine alignment: [[capture-planning-phase]] | [[pursuit-decision-phase]] | [[shipley-business-development-lifecycle]]

## Vault contract

Read [[ariadne-vault-schema]] before ingest or append.

## Related

[[ariadne-vault-schema]] [[shipley-capture-guide-source]] [[capture-planning-phase]] [[color-team-reviews]] [[black-hat-review]] [[win-theme-development]]

## Added/Updated """
        + TODAY
        + """

Phase 1 hub from Capture Guide preface and TOC.
""",
    )

    concepts = {
        "shipley-capture-planning-overview.md": (
            "Shipley capture planning - overview",
            "global-shipley-capture-planning-overview",
            "extract:Shipley-Capture-Guide-extract.md | pages:9-11,23-24",
            "[shipley, capture, capture-planning]",
            """# Shipley capture planning - overview

## Key signals + citations

- Capture planning progresses the seller from an unknown to a favored customer position by influencing the customer through the sales cycle (extract pp. 9-11).
- Iterative progression: research and customer interaction, then strategy/tactics, validation, and relationship depth (pp. 9-11).
- Overview defines identifying opportunities, assessing the environment, and devising/implementing winning strategies with documented action-oriented capture plans (pp. 23-24).
- Often 40-60 percent of the time customers prefer a vendor before proposals are submitted (p. 24).

## Synthesis

Core of [[capture-planning-phase]]; pair with [[shipley-customer-alignment-capture]] and [[shipley-decision-gate-reviews]].

## Open questions

- Map KBR TAM MS1-MS4 to Shipley decision gates per pursuit.

## Related

[[shipley-capture-guide-hub]] [[capture-planning-phase]] [[shipley-decision-gate-reviews]] [[ariadne-vault-schema]]""",
        ),
        "shipley-customer-alignment-capture.md": (
            "Shipley customer alignment (capture)",
            "global-shipley-customer-alignment-capture",
            "extract:Shipley-Capture-Guide-extract.md | pages:4-5,61-63",
            "[shipley, capture, customer-interface]",
            """# Shipley customer alignment (capture)

## Key signals + citations

- Align capture with customer needs; influence early preference; base strategy on the customer's view of reality (pp. 4-5).
- Customer interface needs listening, trust, collaboration, and persuasive communication (p. 61).
- Customers buy from trusted experts who deliver perceived value; match how each customer buys (pp. 62-63).

## Synthesis

Operational face of Shipley preface principles; Iris/Clio outputs should cite customer-facing evidence.

## Related

[[shipley-capture-guide-hub]] [[shipley-capture-planning-overview]] [[win-theme-development]] [[ariadne-vault-schema]]""",
        ),
        "shipley-decision-gate-reviews.md": (
            "Shipley decision gate reviews",
            "global-shipley-decision-gate-reviews",
            "extract:Shipley-Capture-Guide-extract.md | pages:4-5,72-75",
            "[shipley, capture, gates, decision-gates]",
            """# Shipley decision gate reviews

## Key signals + citations

- Decision gates control progression through the BD lifecycle and improve win probability (pp. 73-74).
- Typical four to seven phases; example questions from interest through final offer (Figure 2, pp. 74-75).

## Synthesis

Go/no-go at phase boundaries; distinct from [[shipley-color-team-reviews-capture]].

## Related

[[shipley-capture-guide-hub]] [[pursuit-decision-phase]] [[shipley-color-team-reviews-capture]] [[gate-review-process]] [[ariadne-vault-schema]]""",
        ),
        "shipley-color-team-reviews-capture.md": (
            "Shipley color team reviews (capture)",
            "global-shipley-color-team-reviews-capture",
            "extract:Shipley-Capture-Guide-extract.md | pages:43-44",
            "[shipley, capture, color-team, reviews]",
            """# Shipley color team reviews (capture)

## Key signals + citations

- Milestones to improve Pwin between decision gates (pp. 43-44).
- Blue, Black Hat, Pink, Red, Green, Gold, White reviews - scale to opportunity size (pp. 43-44).

## Synthesis

Link to [[color-team-reviews]], [[black-hat-review]], and related global_wiki shipley pages.

## Related

[[shipley-capture-guide-hub]] [[shipley-decision-gate-reviews]] [[color-team-reviews]] [[black-hat-review]] [[ariadne-vault-schema]]""",
        ),
        "shipley-win-strategy-development-capture.md": (
            "Shipley win strategy development (capture)",
            "global-shipley-win-strategy-development-capture",
            "extract:Shipley-Capture-Guide-extract.md | pages:149-151",
            "[shipley, capture, win-strategy, win-themes]",
            """# Shipley win strategy development (capture)

## Key signals + citations

- Strategy is position; tactics implement and convey it (pp. 149-150).
- Requires competitive position and discriminators; misaligned messages erode trust (pp. 149-150).
- Bidder comparison, buyer issues, price-to-win, trade-offs, action plan (pp. 150-151).

## Synthesis

Feeds [[win-theme-development]] and Clio packet themes.

## Related

[[shipley-capture-guide-hub]] [[win-theme-development]] [[shipley-competitive-intelligence-capture]] [[ariadne-vault-schema]]""",
        ),
        "shipley-competitive-intelligence-capture.md": (
            "Shipley competitive intelligence (capture)",
            "global-shipley-competitive-intelligence-capture",
            "extract:Shipley-Capture-Guide-extract.md | pages:43-44,56-59",
            "[shipley, capture, competitive-intelligence, black-hat]",
            """# Shipley competitive intelligence (capture)

## Key signals + citations

- Black Hat anticipates competitor strategies and solution gaps (pp. 43-44).
- Competitive analysis in costing informs proposal targeting (pp. 56-59).

## Synthesis

Iris intel feeds Black Hat and [[shipley-win-strategy-development-capture]]; see [[black-hat-review]].

## Related

[[shipley-capture-guide-hub]] [[black-hat-review]] [[price-to-win-analysis]] [[ariadne-vault-schema]]""",
        ),
    }

    for fname, (name, id_, cites, tags, body) in concepts.items():
        w(
            f"knowledge/global/domain_intel/concepts/{fname}",
            fm(
                name=name,
                type="concept",
                id=id_,
                trust="trusted",
                reviewed_by="axelrod2023",
                reviewed_at=NOW,
                added=NOW,
                last_updated=TODAY,
                citations=cites,
                tags=tags,
            )
            + "\n\n"
            + body
            + "\n\n## Added/Updated "
            + TODAY
            + "\n\nParaphrase from Shipley Capture Guide extract.\n",
        )

    w(
        f"agents/clio/content/{TODAY}_shipley-capture-guide-phase1.md",
        f"""---
quest_slug: shipley-capture-guide-phase1
from_agent: clio
status: shipped
---

# Shipley Capture Guide - phase 1 ingest (Clio)

Branch: feature/knowledge-vault-v1 (no merge to main).

## Shipped

- `knowledge/foundation/reference/shipley-capture-guide-source.md`
- `knowledge/global/domain_intel/concepts/shipley-capture-guide-hub.md`
- Five concept pages under `knowledge/global/domain_intel/concepts/`
- Batch: `scripts/shipley_capture_guide_phase1_batch.py`

## Review

reviewed_by axelrod2023; vault_lint after write.

## Next

Additional TOC topics in later waves; dedup with `global/global_wiki/shipley/`.
""",
    )

    return written


def append_log() -> None:
    log = REPO / "knowledge" / "log.md"
    marker = "Shipley Capture Guide phase 1"
    text = log.read_text(encoding="utf-8")
    if marker in text:
        return
    entry = f"""
## [{TODAY}] ingest | Shipley Capture Guide phase 1

- Cite: knowledge/foundation/reference/shipley-capture-guide-source.md
- Hub + 5 concepts: knowledge/global/domain_intel/concepts/shipley-*
- Script: scripts/shipley_capture_guide_phase1_batch.py
- Clio: agents/clio/content/{TODAY}_shipley-capture-guide-phase1.md
- reviewed_by: axelrod2023
"""
    log.write_text(text.rstrip() + "\n" + entry, encoding="utf-8")


def patch_index() -> None:
    index = REPO / "knowledge" / "index.md"
    text = index.read_text(encoding="utf-8")
    if "shipley-capture-guide-hub" in text:
        return
    rows = (
        "| [[shipley-capture-guide-source]] | Locked PDF + extract citation (Shipley Capture Guide 5th ed.) |\n"
        "| [[shipley-capture-guide-hub]] | Hub: objectives, five principles, phase-1 capture concepts |\n"
    )
    needle = "| [[briefing-packet-data-dictionary]] | Packet key explanations |"
    if needle in text:
        text = text.replace(needle, needle + "\n" + rows)
    text = text.replace("last_updated: 2026-07-05", f"last_updated: {TODAY}")
    index.write_text(text, encoding="utf-8")


def main() -> None:
    paths = write_all()
    append_log()
    patch_index()
    for p in paths:
        print("wrote", p.relative_to(REPO))
    print("updated knowledge/log.md and knowledge/index.md")


if __name__ == "__main__":
    main()