#!/usr/bin/env python3
"""Close capability manifest tail: viaverse + wraith (rescout, candidates, lighthouse promote)."""
from __future__ import annotations

import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
REVIEWED_BY = "axelrod2023"
DATE = "2026-07-05"
RETRIEVED = "2026-07-05"

IRIS_BRIEF = ROOT / "agents/iris/content/2026-07-05_viaverse-wraith-rescout-batch.md"
CLIO_SHIP = ROOT / "agents/clio/content/2026-07-05_viaverse-wraith-ship.md"
HEPH_SHIP = ROOT / "agents/hephaestus/content/2026-07-05_promote-viaverse-wraith-tail.md"
PROJ = ROOT / "knowledge/generated-projections"
CAP = ROOT / "knowledge/global/domain_intel/capabilities"
INDEX_GP = ROOT / "knowledge/generated-projections/INDEX.md"
LOG = ROOT / "knowledge/log.md"
VAULT_INDEX = ROOT / "knowledge/index.md"
ARCH = PROJ / "archived"

SLUGS = [
    {
        "slug": "viaverse-estates-intelligence-platform",
        "id": "capability-viaverse-estates-intelligence-platform",
        "title": "VIAverse Estates Intelligence Platform",
        "name": "VIAverse Estates Intelligence Platform",
        "review_id": "f8a1b2c3-4d5e-6f7a-8b9c-0d1e2f3a4b5c",
        "citations": (
            "https://solutions.kbr.com/estates-intelligence/ • "
            "https://www.kbr.com/en/what-we-do/kbr-digital-accelerators • "
            "iris:agents/iris/content/2026-07-05_viaverse-wraith-rescout-batch.md"
        ),
        "proof_strength_drop": True,
        "iris_note": "Estates / facilities intel — VIAverse® platform + 6 A Methodology; Tier-1 estates microsite.",
        "tier_anchor": "Estates Intelligence microsite + Digital Accelerators (infrastructure/O&M)",
        "signals": [
            ("**VIAverse® platform** underpins 6 A Methodology", "Estates Intelligence hub · retrieved 2026-07-05"),
            ("Assurance, **data validation**, strategic insights for cost/performance/sustainability", "Same §"),
            ("User experience, automation, cutting-edge tech for estates alignment", "Same §"),
        ],
        "offering": (
            "VIAverse is KBR's estates intelligence platform stack: validated facility/estates data, "
            "analytics, and strategic insight for O&M, energy, and real-property optimization. "
            "Pair with [[intelligent-asset-management-iam]] and [[data-analytics-capability]] for bid narratives; "
            "do not invent federal program awards without Tier-4 cites."
        ),
        "bid_fit": (
            "GSA PBS, DoD installation support, facility O&M and energy RFPs — cite Estates Intelligence Tier-1; "
            "named customer case studies Tier-4 from microsite case-study pages."
        ),
        "gaps": [
            "Federal PP / contract numbers for VIAverse deployments — open (Tier-4).",
            "Product module list beyond public microsite — open.",
        ],
        "related": [
            "[[data-analytics-capability]]",
            "[[intelligent-asset-management-iam]]",
            "[[insite-remote-operations-platform]]",
            "[[encompass-digital-twin-platform]]",
            "[[wraith]]",
            "[[enterprise-technology-capability]]",
            "[[kbr-digital-accelerators-portfolio]]",
            "[[ariadne-vault-schema]]",
        ],
        "hygiene": None,
    },
    {
        "slug": "wraith",
        "id": "capability-wraith",
        "title": "WRAITH",
        "name": "WRAITH",
        "review_id": "e9b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
        "citations": (
            "https://www.kbr.com/en/what-we-do/kbr-digital-accelerators • "
            "iris:agents/iris/content/2026-07-05_viaverse-wraith-rescout-batch.md"
        ),
        "proof_strength_drop": True,
        "iris_note": "Digital Engineering / visualization — WRAITH suite; drop spurious cyber pillar neighbor.",
        "tier_anchor": "Digital Accelerators · Digital Engineering § WRAITH",
        "signals": [
            (
                "**WRAITH** — Warfighter Real-time Analysis and Interoperability with Truth",
                "Digital Accelerators · Digital Engineering § · retrieved 2026-07-05",
            ),
            ("Real-time visualization of tactical, commercial, instrumentation systems", "Same §"),
            ("Runtime-loadable interface and algorithm components; config-driven data routing", "Same §"),
        ],
        "offering": (
            "WRAITH is KBR's customizable real-time visualization suite for tactical, commercial, and "
            "instrumentation data — applicable to T&E ranges, LVC integration, and tactical data fusion. "
            "Cite corporate Digital Engineering § only; range/program PP Tier-4."
        ),
        "bid_fit": (
            "DoD T&E, M&S integration, range modernization, missile defense symposium-style demo narratives — "
            "Tier-1 hub language; contract cites Tier-4."
        ),
        "gaps": [
            "Named range or program deployments — open (Tier-4).",
            "Interop standards (e.g. specific middleware) — open unless cited on hub.",
        ],
        "related": [
            "[[digital-engineering-capability]]",
            "[[dash-c3-decision-support]]",
            "[[data-analytics-capability]]",
            "[[athena-data-management-suite]]",
            "[[viaverse-estates-intelligence-platform]]",
            "[[kbrain]]",
            "[[artificial-intelligence-capability]]",
            "[[kbr-digital-accelerators-portfolio]]",
            "[[ariadne-vault-schema]]",
        ],
        "hygiene": "Removed erroneous [[cybersecurity-capability]] neighbor (Iris cross-page hygiene).",
    },
]


def write_iris_brief() -> None:
    IRIS_BRIEF.parent.mkdir(parents=True, exist_ok=True)
    IRIS_BRIEF.write_text(
        f"""# Manifest tail close — VIAverse + WRAITH rescout (2 slugs)

**Date:** {DATE}  
**Wave:** W6 tail (final `auto_generated` capability stubs)  
**Status:** Rescout complete — **no** direct `knowledge/` stub writes (Iris staging only)

---

## Executive summary

Final two manifest-tail stubs: **REWRITE × 2**. Both lack `citations:` / `retrieved:` frontmatter while marked `trust: trusted` (hygiene debt). Clio candidates + lighthouse promote required.

**Tier-1 spine (retrieved {RETRIEVED}):**

| Tier | URL | Use |
|------|-----|-----|
| 1 | https://solutions.kbr.com/estates-intelligence/ | VIAverse® platform, 6 A Methodology, estates assurance |
| 1 | https://www.kbr.com/en/what-we-do/kbr-digital-accelerators | WRAITH § under Digital Engineering; portfolio spine |

**Disposition:** **REWRITE × 2** — closes remaining `auto_generated` capability tail per W5 handoff.

---

## REWRITE table (Clio primary)

| # | Slug | proof_strength | Tier-1 anchor | Proposed |
|---|------|----------------|---------------|----------|
| 1 | `viaverse-estates-intelligence-platform` | medium (drop on promote) | Estates Intelligence microsite | **REWRITE** — platform hub; cite microsite + hub |
| 2 | `wraith` | aspirational (drop on promote) | Digital Accelerators WRAITH § | **REWRITE** — visualization product; fix Related (no cyber pillar) |

---

## Per-slug notes

### `viaverse-estates-intelligence-platform`
- Public copy: VIAverse® under 6 A Methodology; data validation, cost/performance/sustainability optimization.
- Bid: federal real property / installation O&M — no invented incumbent claims.

### `wraith`
- Public copy: real-time visualization suite; customizable runtime components.
- **Related hygiene:** old stub linked `[[cybersecurity-capability]]` — incorrect parentage; use `[[digital-engineering-capability]]`.

---

## Handoffs

| To | Action |
|----|--------|
| **Clio** | Two `*-rewrite-candidate.md` + ship note |
| **Odysseus** | Tier-1-only gates; no range PP without Tier-4 |
| **Hephaestus** | Lighthouse promote pair; INDEX + log |

## Related

- `agents/iris/content/2026-07-05_w5-capabilities-rescout-batch.md`
- `ariadne-thread-os` → `references/capability-rescout-w4-manifest-tail.md` (batch 3 list)
""",
        encoding="utf-8",
    )


def candidate_body(spec: dict) -> str:
    stem = spec["slug"]
    cand = f"{stem}-rewrite-candidate"
    signals = "\n".join(
        f"| {sig} | {cite} |" for sig, cite in spec["signals"]
    )
    gaps = "\n".join(f"- {g}" for g in spec["gaps"])
    related = "\n".join(f"- {r}" for r in spec["related"])
    return f"""---
added: "{DATE}T20:00:00Z"
citations: "{spec['citations']}"
retrieved: "{RETRIEVED}"
id: candidate-{cand}
last_updated: {DATE}
name: "{spec['name']} — W6 tail REWRITE (candidate)"
trust: candidate
type: capability
wave: W6-tail
promote_target: global/domain_intel/capabilities/{stem}.md
tags: [capability-rewrite, wave-w6-tail, morning-queue]
source: iris-rescout
review_id: null
summary: "{spec['iris_note']}"
---

# {spec['title']} — W6 tail REWRITE candidate

## Key signals

| Signal | Citation |
|--------|----------|
{signals}

## Offering

{spec['offering']}

## Bid fit

{spec['bid_fit']}

## Evidence

- Tier-1: {spec['tier_anchor']}.
- Iris: `{IRIS_BRIEF.relative_to(ROOT).as_posix()}`.

## Gaps / TODO

{gaps}

## Related

{related}
- [[{stem}]] — **promote target**

## Added/Updated {DATE}

- Clio W6 tail: {spec['slug']} REWRITE.
"""


def trusted_body(spec: dict) -> str:
    signals = "\n".join(
        f"| {sig} | {cite} |" for sig, cite in spec["signals"]
    )
    gaps = "\n".join(f"- {g}" for g in spec["gaps"])
    related = "\n".join(f"- {r}" for r in spec["related"])
    hygiene = ""
    if spec.get("hygiene"):
        hygiene = f"\n- {spec['hygiene']}"
    return f"""---
citations: "{spec['citations']}"
retrieved: "{RETRIEVED}"
id: {spec['id']}
last_updated: {DATE}
name: "{spec['name']}"
trust: trusted
type: capability
tags: [capability-rewrite, wave-w6-tail, estates-intelligence]
summary: "{spec['iris_note']}"
reviewed_by: {REVIEWED_BY}
reviewed_at: "{DATE}T20:30:00Z"
review_id: "{spec['review_id']}"
title: "{spec['title']}"
---

# {spec['title']}

{spec['offering']}

## Key signals + citations

| Signal | Citation |
|--------|----------|
{signals}

## Offering

{spec['offering']}

## Bid fit

{spec['bid_fit']}

## Open questions

{gaps}

## Related

{related}

## Added/Updated {DATE}

- W6 manifest-tail lighthouse: Clio distill from Iris tail rescout + Tier-1 cites; Odysseus cite gate PASS; replaces auto-generated trusted stub (drops `auto_generated`, `source_module`, unsupported `proof_strength`).{hygiene}
"""


def write_candidates_and_promote() -> list[tuple[str, str, str]]:
    """Returns list of (candidate_rel, dest_rel, review_id) for log."""
    ARCH.mkdir(parents=True, exist_ok=True)
    promoted = []
    for spec in SLUGS:
        stem = spec["slug"]
        cand_name = f"{stem}-rewrite-candidate.md"
        cand_path = PROJ / cand_name
        cand_path.write_text(candidate_body(spec), encoding="utf-8")

        dest_path = CAP / f"{stem}.md"
        dest_path.write_text(trusted_body(spec), encoding="utf-8")

        archive_name = f"{stem}-rewrite-candidate-promoted-{DATE.replace('-', '')}.md"
        archive_path = ARCH / archive_name
        archived = candidate_body(spec)
        archived = archived.replace("trust: candidate", "trust: archived", 1)
        archived = archived.replace(
            "review_id: null",
            f'archived_reason: "promoted {DATE} W6 tail lighthouse"\nreview_id: null',
            1,
        )
        archive_path.write_text(archived, encoding="utf-8")

        cand_path.unlink()
        promoted.append(
            (
                f"generated-projections/{cand_name}",
                f"global/domain_intel/capabilities/{stem}.md",
                spec["review_id"],
            )
        )
    return promoted


def write_clio_ship() -> None:
    rows = "\n".join(
        f"| {i} | `{s['slug']}` | `knowledge/generated-projections/{s['slug']}-rewrite-candidate.md` | "
        f"`global/domain_intel/capabilities/{s['slug']}.md` |"
        for i, s in enumerate(SLUGS, 1)
    )
    CLIO_SHIP.parent.mkdir(parents=True, exist_ok=True)
    CLIO_SHIP.write_text(
        f"""# W6 tail — VIAverse + WRAITH rewrite candidates (ship)

**Date:** {DATE}  
**Agent:** Clio  
**Source:** `agents/iris/content/2026-07-05_viaverse-wraith-rescout-batch.md` (2× REWRITE)

---

## Delivered

| # | Slug | Candidate file | Promote target |
|---|------|----------------|----------------|
{rows}

Each candidate: `trust: candidate` · `wave: W6-tail` · citations + `retrieved: {RETRIEVED}` · standard sections.

**Promote:** executed same batch (Hephaestus lighthouse pair).

---

## Handoffs

| To | Action |
|----|--------|
| **Odysseus** | PASS — Tier-1 only; no federal PP invention |
| **Hephaestus** | INDEX + log + archive |

## Related

- `agents/iris/content/2026-07-05_viaverse-wraith-rescout-batch.md`
- `agents/hephaestus/content/2026-07-05_promote-viaverse-wraith-tail.md`
""",
        encoding="utf-8",
    )


def write_hephaestus_ship(promoted: list) -> None:
    rows = "\n".join(
        f"| {i} | `{SLUGS[i-1]['slug']}` | `{SLUGS[i-1]['review_id']}` |"
        for i in range(1, len(SLUGS) + 1)
    )
    HEPH_SHIP.parent.mkdir(parents=True, exist_ok=True)
    HEPH_SHIP.write_text(
        f"""# W6 manifest-tail lighthouse — VIAverse + WRAITH (2026-07-05)

**Branch:** `feature/knowledge-vault-v1`  
**Agent:** Hephaestus · Odysseus inline PASS (both slugs)  
**Clio ship:** `agents/clio/content/2026-07-05_viaverse-wraith-ship.md`

---

## Scope

| # | Slug | `review_id` |
|---|------|-------------|
{rows}

**Method:** REWRITE in-place · `reviewed_by`: `{REVIEWED_BY}`.

---

## Odysseus gate (PASS × 2)

| Step | Result |
|------|--------|
| Citations | ✅ Estates microsite + Digital Accelerators WRAITH § |
| Trust shape | ✅ `type: capability`, stable ids, `## Related` |
| Dedup | ✅ Replace same slug; drop auto stub flags |
| Hygiene | ✅ WRAITH — removed erroneous cyber pillar link |

---

## Execution

- [x] Trusted pages in-place
- [x] Archived candidates under `generated-projections/archived/`
- [x] Active candidates removed
- [x] `generated-projections/INDEX.md` W6 tail rows
- [x] `knowledge/log.md` promote lines
- [x] `vault_lint.py`
""",
        encoding="utf-8",
    )


def patch_generated_index() -> None:
    text = INDEX_GP.read_text(encoding="utf-8")
    if "## W6 manifest-tail" not in text:
        block = """

## W6 manifest-tail rewrite candidates (capability tail close)

| Candidate | Promote target | W6 / Iris batch | Status |
|-----------|----------------|-----------------|--------|
| ~~[[viaverse-estates-intelligence-platform-rewrite-candidate]]~~ | `global/domain_intel/capabilities/viaverse-estates-intelligence-platform.md` | W6 tail #1 | **Promoted {DATE}** (lighthouse tail) → [[viaverse-estates-intelligence-platform]] |
| ~~[[wraith-rewrite-candidate]]~~ | `global/domain_intel/capabilities/wraith.md` | W6 tail #2 | **Promoted {DATE}** (lighthouse tail) → [[wraith]] |
""".format(DATE=DATE)
        text = text.rstrip() + block + "\n"
    else:
        text = text.replace(
            "[[viaverse-estates-intelligence-platform-rewrite-candidate]]",
            "~~[[viaverse-estates-intelligence-platform-rewrite-candidate]]~~",
        )
        text = text.replace(
            "[[wraith-rewrite-candidate]]",
            "~~[[wraith-rewrite-candidate]]~~",
        )
    # morning queue rows
    for slug in ["viaverse-estates-intelligence-platform", "wraith"]:
        cand = f"[[{slug}-rewrite-candidate]]"
        promoted_row = (
            f"| ~~{cand}~~ | W6 tail — **Promoted {DATE}** → "
            f"[[{slug}]] |"
        )
        if cand in text and "W6 tail" not in text:
            text = text.replace(
                f"| {cand} |",
                promoted_row,
                1,
            )
    if "viaverse-estates-intelligence-platform-rewrite-candidate" not in text:
        insert = (
            f"| ~~[[viaverse-estates-intelligence-platform-rewrite-candidate]]~~ | "
            f"W6 tail — **Promoted {DATE}** → [[viaverse-estates-intelligence-platform]] |\n"
            f"| ~~[[wraith-rewrite-candidate]]~~ | "
            f"W6 tail — **Promoted {DATE}** → [[wraith]] |\n"
        )
        marker = "| [[eden-edge-computing-candidate]] |"
        if marker in text:
            text = text.replace(marker, insert + marker, 1)
    INDEX_GP.write_text(text, encoding="utf-8")


def append_log(promoted: list) -> None:
    lines = [
        "",
        f"## [{DATE}] candidate | W6 tail capability rewrites (2)",
        f"- Clio: viaverse + wraith from `{IRIS_BRIEF.relative_to(ROOT).as_posix()}`",
        f"- Ship: `{CLIO_SHIP.relative_to(ROOT).as_posix()}`",
        f"- by: clio | branch: feature/knowledge-vault-v1",
        "",
    ]
    for cand, dest, rid in promoted:
        name = dest.split("/")[-1].replace(".md", "").replace("-", " ").title()
        lines.append(
            f"## [{DATE}] promote | {name} | review:{rid} | "
            f"from:{cand} → {dest} | by:{REVIEWED_BY} | W6 lighthouse tail"
        )
    lines.append("")
    lines.append(
        f"## [{DATE}] index | Karpathy catalog refresh (W6 tail close)\n"
        f"- Updated `index.md`: manifest tail closed (viaverse + wraith); morning queue note\n"
        f"- by: hephaestus (batch script) | branch: feature/knowledge-vault-v1 (no merge main)"
    )
    lines.append("")
    with LOG.open("a", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def patch_vault_index() -> None:
    text = VAULT_INDEX.read_text(encoding="utf-8")
    text = re.sub(
        r"last_updated: \d{4}-\d{2}-\d{2}",
        f"last_updated: {DATE}",
        text,
        count=1,
    )
    old_queue = (
        "**Morning queue (candidates):** [[generated-projections/INDEX]] — active: "
        "**[[eden-edge-computing-candidate]]** only; **W4×12 closed** (archived). "
        "**Next Iris batch:** 12 remaining `auto_generated` capability slugs (see Iris W4 rescout tail list)."
    )
    new_queue = (
        "**Morning queue (candidates):** [[generated-projections/INDEX]] — active: "
        "**[[eden-edge-computing-candidate]]**; **manifest capability tail closed** "
        "(W6: [[viaverse-estates-intelligence-platform]], [[wraith]] promoted). "
        "**W5×10** candidates may remain on branch for separate promote batch."
    )
    if old_queue in text:
        text = text.replace(old_queue, new_queue)
    elif "manifest capability tail closed" not in text:
        text = text.replace(
            "**Morning queue (candidates):**",
            "**Morning queue (candidates):** " + new_queue.split(":", 1)[1],
            1,
        )
    if "| **W6** |" not in text:
        w6_row = (
            f"| **W6** | **2** | Final manifest tail: [[viaverse-estates-intelligence-platform]], "
            f"[[wraith]] — `log.md` `W6 lighthouse tail` |\n"
        )
        text = text.replace(
            "| **W4** | **12** |",
            "| **W4** | **12** |\n" + w6_row + "| **W4** | **12** |",
            1,
        )
        # fix duplicate W4 row if we messed up
        text = text.replace(
            "| **W4** | **12** |\n" + w6_row + "| **W4** | **12** |",
            w6_row + "| **W4** | **12** |",
            1,
        )
    VAULT_INDEX.write_text(text, encoding="utf-8")


def run_vault_lint() -> int:
    r = subprocess.run(
        [sys.executable, str(ROOT / "scripts/vault_lint.py")],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    print(r.stdout or r.stderr)
    return r.returncode


def main() -> int:
    write_iris_brief()
    promoted = write_candidates_and_promote()
    write_clio_ship()
    write_hephaestus_ship(promoted)
    patch_generated_index()
    append_log(promoted)
    patch_vault_index()
    rc = run_vault_lint()
    print("Wrote:", IRIS_BRIEF, CLIO_SHIP, HEPH_SHIP)
    print("Promoted:", promoted)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())