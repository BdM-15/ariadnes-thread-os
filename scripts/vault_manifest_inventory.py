#!/usr/bin/env python3
"""Phase 1 machine inventory: all knowledge/**/*.md -> CSV + ship summary."""
from __future__ import annotations

import csv
import re
from collections import Counter
from datetime import date
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VAULT = REPO / "knowledge"
OUT_CSV = REPO / "agents/hephaestus/content/2026-07-02_vault-manifest-inventory.csv"
OUT_SHIP = REPO / "agents/hephaestus/content/2026-07-02_phase1-inventory-ship.md"

SMOKE_ENTITY_PATHS = {
    "entities/agencies/test-agency-xyz.md",
    "entities/competitors/example-competitor-llc.md",
}

KEEP_PATHS = {
    "index.md",
    "log.md",
    "entities/companies/kbr-services-readiness-sustainment.md",
    "generated-projections/eden-edge-computing-candidate.md",
    "global/global_wiki/capture/concepts/sam-live-discovery.md",
}

KEEP_MILESTONE_GLOB = re.compile(
    r"^global/domain_intel/milestones/ms[1-4](-|$)"
)

FM_START = re.compile(r"^---\s*$", re.MULTILINE)


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    block = text[3:end]
    out: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip().strip('"').strip("'")
    return out


def posix_rel(path: Path) -> str:
    return path.relative_to(VAULT).as_posix()


def infer_zone(rel: str) -> str:
    if rel in ("index.md", "log.md", "README.md"):
        return "meta"
    parts = rel.split("/")
    if not parts:
        return "meta"
    top = parts[0]
    if top == "global" and len(parts) >= 2:
        sub = parts[1]
        if sub == "global_wiki" and len(parts) >= 4 and parts[2] == "capture" and parts[3] == "concepts":
            return "concepts"
        if sub == "global_wiki" and len(parts) >= 3 and parts[2] == "shipley":
            return "shipley"
        if sub == "domain_intel" and len(parts) >= 3 and parts[2] == "capabilities":
            return "capabilities"
        if sub == "global_wiki":
            return "global_wiki"
        if sub == "domain_intel":
            return "domain_intel"
    if top == "entities":
        return "entities"
    if top == "foundation":
        return "foundation"
    if top == "generated-projections":
        return "generated-projections"
    if top == "pursuits":
        return "pursuits"
    if top == "relationships":
        return "relationships"
    return top


def is_smoke_test_example(rel: str) -> bool:
    """Entity smoke fixtures (not workload pages like test-and-quality-*)."""
    if rel in SMOKE_ENTITY_PATHS:
        return True
    if not rel.startswith("entities/"):
        return False
    base = Path(rel).stem.lower()
    return base.startswith("test-") or base.startswith("example-")


def proposed_tag(rel: str, zone: str, fm: dict[str, str]) -> str:
    if rel in SMOKE_ENTITY_PATHS or is_smoke_test_example(rel):
        return "ARCHIVE"
    if rel.endswith("INDEX.md") or rel in ("index.md", "log.md"):
        return "KEEP"
    if rel in KEEP_PATHS:
        return "KEEP"
    if KEEP_MILESTONE_GLOB.match(rel):
        return "KEEP"
    if rel == "foundation/capture-llm-wiki.md":
        return "REWRITE"
    if zone == "shipley":
        return "REWRITE"
    if zone == "capabilities":
        return "RESCOUT"
    if zone == "concepts":
        return "RESCOUT"
    if zone == "entities":
        return "RESCOUT"
    if zone == "generated-projections":
        if rel.endswith("INDEX.md"):
            return "KEEP"
        return "KEEP"  # candidates; no promote during freeze
    if zone == "pursuits":
        return "RESCOUT"
    if zone == "foundation":
        return "REWRITE"
    if zone == "global_wiki":
        return "REWRITE"
    if zone == "domain_intel":
        return "REWRITE"
    if zone == "relationships":
        return "KEEP"
    if zone == "meta":
        return "KEEP"
    return "RESCOUT"


def main() -> None:
    rows: list[dict[str, str]] = []
    md_files = sorted(
        p for p in VAULT.rglob("*.md") if ".obsidian" not in p.parts
    )

    for p in md_files:
        rel = posix_rel(p)
        text = p.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        zone = infer_zone(rel)
        trust = fm.get("trust", "")
        auto = fm.get("auto_generated", "").lower()
        auto_yn = "y" if auto in ("true", "yes", "1") else "n"
        cites_yn = "y" if "citations" in fm and fm["citations"] else "n"
        tag = proposed_tag(rel, zone, fm)
        rows.append(
            {
                "path": rel,
                "zone": zone,
                "trust": trust,
                "auto_generated": auto_yn,
                "has_citations_frontmatter": cites_yn,
                "proposed_tag": tag,
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "path",
        "zone",
        "trust",
        "auto_generated",
        "has_citations_frontmatter",
        "proposed_tag",
    ]
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    by_tag = Counter(r["proposed_tag"] for r in rows)
    by_zone = Counter(r["zone"] for r in rows)
    cross: Counter[tuple[str, str]] = Counter()
    for r in rows:
        cross[(r["zone"], r["proposed_tag"])] += 1

    ship_lines = [
        "# Phase 1 vault manifest inventory — ship note",
        "",
        f"**Date:** {date.today().isoformat()}",
        "**Agent:** Hephaestus",
        "**Overwatch ratification:** 2026-07-02 hybrid yes; archive `generated-projections/archived/rebuild-2026/`; KBR-first waves; minimal cleanse; promote freeze on.",
        "",
        "## Deliverables",
        "",
        f"- Machine inventory CSV: `{OUT_CSV.relative_to(REPO).as_posix()}`",
        f"- Total markdown files scanned: **{len(rows)}**",
        "- **No vault files moved or deleted** (manifest only).",
        "",
        "## Row counts by `proposed_tag`",
        "",
        "| proposed_tag | count |",
        "|--------------|------:|",
    ]
    for tag in ("KEEP", "REWRITE", "ARCHIVE", "RESCOUT"):
        ship_lines.append(f"| {tag} | {by_tag.get(tag, 0)} |")
    ship_lines.append(f"| **TOTAL** | **{len(rows)}** |")

    ship_lines.extend(
        [
            "",
            "## Row counts by `zone`",
            "",
            "| zone | count |",
            "|------|------:|",
        ]
    )
    for zone, cnt in sorted(by_zone.items(), key=lambda x: (-x[1], x[0])):
        ship_lines.append(f"| {zone} | {cnt} |")

    ship_lines.extend(
        [
            "",
            "## Cross-tab: zone × proposed_tag",
            "",
            "| zone | KEEP | REWRITE | ARCHIVE | RESCOUT |",
            "|------|-----:|--------:|--------:|--------:|",
        ]
    )
    for zone in sorted(by_zone.keys()):
        ship_lines.append(
            "| {z} | {k} | {rw} | {a} | {rs} |".format(
                z=zone,
                k=cross.get((zone, "KEEP"), 0),
                rw=cross.get((zone, "REWRITE"), 0),
                a=cross.get((zone, "ARCHIVE"), 0),
                rs=cross.get((zone, "RESCOUT"), 0),
            )
        )

    ship_lines.extend(
        [
            "",
            "## Bucket rules applied (machine)",
            "",
            "- Smoke entities → **ARCHIVE**",
            "- `domain_intel/capabilities/` → default **RESCOUT**",
            "- `global_wiki/capture/concepts/` → default **RESCOUT**",
            "- `global_wiki/shipley/` → default **REWRITE**",
            "- Path/basename `test*` / `example*` → **ARCHIVE**",
            "- Odysseus exemplar **KEEP** paths (index chain, KBR hub, eden candidate, ms1–ms4 milestones, sam-live-discovery)",
            "",
            "## Next",
            "",
            "Odysseus signs manifest rows; Phase 3 archive executes **ARCHIVE** rows only after hybrid gate GREEN.",
            "",
            "---",
            "",
            "*hephaestus completed — Phase 1 manifest*",
        ]
    )

    OUT_SHIP.write_text("\n".join(ship_lines) + "\n", encoding="utf-8")
    print(f"Wrote {len(rows)} rows -> {OUT_CSV}")
    print(f"Ship note -> {OUT_SHIP}")
    print("by_tag:", dict(by_tag))


if __name__ == "__main__":
    main()