#!/usr/bin/env python3
"""W5 lighthouse: in-place REWRITE promote for ten capability candidates (ed984a1).

Run from repo root:
  python scripts/_promote_w5_capabilities_in_place.py
  python scripts/_promote_w5_capabilities_in_place.py --dry-run
"""
from __future__ import annotations

import argparse
import re
import shutil
import uuid
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VAULT = REPO / "knowledge"
ARCH = VAULT / "generated-projections" / "archived"
PROJ_INDEX = VAULT / "generated-projections" / "INDEX.md"
LOG = VAULT / "log.md"
ROOT_INDEX = VAULT / "index.md"

REVIEWED_BY = "axelrod2023"
WAVE_COMMIT = "ed984a1"

SLUGS: list[tuple[int, str]] = [
    (1, "kbr-cyber-range"),
    (2, "kbr-inc"),
    (3, "petabyte-scale-cloud-migration-proof-point"),
    (4, "proven-sustainment-scale-discriminator"),
    (5, "quality-management-system-certification"),
    (6, "resan"),
    (7, "safety-critical-compliance-proof-point"),
    (8, "skypath-assured-containment"),
    (9, "ttmt-tracking-and-targeting"),
    (10, "u-s-space-force-ssa-performance-iron-stallion"),
]

DROP_FM_KEYS = {
    "wave",
    "promote_target",
    "source",
    "auto_generated",
    "source_module",
    "proof_strength",
    "agencies",
    "domains",
    "updated",
}

FM_LINE = re.compile(r"^([a-zA-Z0-9_]+):\s*(.*)$")


def review_id_for(slug: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"w5-promote-{WAVE_COMMIT}/{slug}"))


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---"):
        raise ValueError("missing frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("unclosed frontmatter")
    fm_raw, body = parts[1], parts[2]
    fm: dict[str, str] = {}
    for line in fm_raw.splitlines():
        line = line.strip("\r")
        if not line.strip():
            continue
        m = FM_LINE.match(line)
        if m:
            fm[m.group(1)] = m.group(2)
    return fm, body.lstrip("\r\n")


def clean_display_name(name: str) -> str:
    name = name.strip().strip('"')
    for suffix in (
        " — W5 REWRITE (candidate)",
        " — W4 REWRITE (candidate)",
        " — W5 REWRITE candidate",
    ):
        if name.endswith(suffix):
            name = name[: -len(suffix)]
    return name


def read_entity_type(dest_path: Path) -> str | None:
    if not dest_path.is_file():
        return None
    m = re.search(r"^entity_type:\s*(\S+)", dest_path.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else None


def transform_body(body: str, title: str, slug: str, num: int) -> str:
    lines = body.splitlines()
    out: list[str] = []
    skip_block = False
    for line in lines:
        raw = line.rstrip("\r")
        if raw.startswith("# ") and "REWRITE" in raw:
            out.append(f"# {title}")
            continue
        if raw.startswith("> **Morning queue"):
            skip_block = True
            continue
        if skip_block:
            if raw.strip() == "":
                skip_block = False
            continue
        if "**Status:** Freeze-safe projection" in raw:
            continue
        if "— **promote target**" in raw:
            continue
        if raw.strip().startswith("## Key signals") and "+ citations" not in raw:
            out.append("## Key signals + citations")
            continue
        out.append(raw)
    text = "\n".join(out).strip() + "\n"

    if "## Open questions" not in text and "## Gaps" in text:
        text = text.replace("## Gaps", "## Open questions", 1)

    if "## Added/Updated" not in text:
        text += (
            f"\n## Added/Updated 2026-07-05\n\n"
            f"- W5 lighthouse #{num} promote (Odysseus PASS); Clio ship `{WAVE_COMMIT}`.\n"
        )
    else:
        text = re.sub(
            r"(## Added/Updated 2026-07-05\n\n)(.*)$",
            rf"\1\2\n- W5 lighthouse #{num} in-place promote; reviewed_by {REVIEWED_BY}.\n",
            text,
            flags=re.DOTALL,
        )

    if "[[ariadne-vault-schema]]" not in text and "## Related" in text:
        text = text.replace(
            "## Related",
            "## Related\n\n- [[ariadne-vault-schema]]",
            1,
        )

    return text


def build_trusted_frontmatter(
    fm: dict[str, str],
    slug: str,
    title: str,
    now_iso: str,
    review_id: str,
    entity_type: str | None,
) -> str:
    lines: list[str] = ["---"]
    added = fm.get("added", f'"{now_iso}"').strip().strip('"')
    if not added.endswith("Z") and "T" not in added:
        added = now_iso

    citations = fm.get("citations", "").strip()
    if not citations:
        raise ValueError(f"{slug}: missing citations")

    out_map = {
        "added": f'"{now_iso}"',
        "citations": citations,
        "retrieved": fm.get("retrieved", "2026-07-05"),
        "id": f"capability-{slug}",
        "last_updated": "2026-07-05",
        "name": f'"{title}"',
        "trust": "trusted",
        "type": "capability",
        "tags": fm.get("tags", "[capability-rewrite, wave-w5, morning-queue]"),
        "summary": fm.get("summary", '""'),
        "reviewed_by": REVIEWED_BY,
        "reviewed_at": f'"{now_iso}"',
        "review_id": f'"{review_id}"',
        "title": f'"{title}"',
    }
    if entity_type:
        out_map["entity_type"] = entity_type

    order = [
        "added",
        "citations",
        "retrieved",
        "id",
        "last_updated",
        "name",
        "trust",
        "type",
        "entity_type",
        "tags",
        "summary",
        "reviewed_by",
        "reviewed_at",
        "review_id",
        "title",
    ]
    for key in order:
        if key in out_map and out_map[key] is not None:
            val = out_map[key]
            if key in ("tags", "summary") and not val.startswith(("[", '"')):
                val = f'"{val}"' if key == "summary" else val
            lines.append(f"{key}: {val}")
    lines.append("---")
    return "\n".join(lines) + "\n"


def promote_one(num: int, slug: str, now_iso: str, stamp: str, dry_run: bool) -> str:
    cand_name = f"{slug}-rewrite-candidate.md"
    cand_path = VAULT / "generated-projections" / cand_name
    dest_rel = f"global/domain_intel/capabilities/{slug}.md"
    dest_path = VAULT / dest_rel

    if not cand_path.is_file():
        raise SystemExit(f"missing candidate: {cand_path}")

    text = cand_path.read_text(encoding="utf-8")
    if not re.search(r"^trust:\s*candidate\s*$", text, re.M):
        raise SystemExit(f"{cand_name}: expected trust: candidate")

    fm, body = split_frontmatter(text)
    title = clean_display_name(fm.get("name", slug))
    review_id = review_id_for(slug)
    entity_type = read_entity_type(dest_path)
    trusted_fm = build_trusted_frontmatter(fm, slug, title, now_iso, review_id, entity_type)
    trusted_body = transform_body(body, title, slug, num)
    promoted = trusted_fm + "\n" + trusted_body

    log_line = (
        f"\n## [{now_iso.replace('T', ' ').replace('Z', ' UTC')}] promote | "
        f"generated-projections/{cand_name} → {dest_rel} | "
        f"review:{review_id} | by:{REVIEWED_BY} | W5 lighthouse #{num}\n"
    )

    if dry_run:
        return f"[dry-run] {slug} → {dest_rel}"

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_text(promoted, encoding="utf-8")

    ARCH.mkdir(parents=True, exist_ok=True)
    archive_text = text
    if "archived_reason:" not in archive_text:
        archive_text = archive_text.replace(
            "---\nadded:",
            f'---\narchived_reason: "promoted to {dest_rel} (W5 lighthouse #{num})"\nadded:',
            1,
        )
    archived = ARCH / f"{cand_path.stem}-promoted-{stamp}.md"
    archived.write_text(archive_text, encoding="utf-8")
    cand_path.unlink()

    with LOG.open("a", encoding="utf-8") as f:
        f.write(log_line)

    return f"OK {slug}"


def patch_indexes(dry_run: bool) -> None:
    w5_rows_morning = []
    w5_table_rows = []
    for num, slug in SLUGS:
        cand_link = f"[[{slug}-rewrite-candidate]]"
        target = f"[[{slug}]]"
        w5_rows_morning.append(
            f"| ~~{cand_link}~~ | W5 #{num} — **Promoted 2026-07-05** (lighthouse) → {target} |"
        )
        w5_table_rows.append(
            f"| ~~{cand_link}~~ | `global/domain_intel/capabilities/{slug}.md` | W5 #{num} | "
            f"**Promoted 2026-07-05** (lighthouse) → {target} |"
        )

    block_morning = "\n".join(w5_rows_morning)
    block_table = "\n".join(
        [
            "",
            "## W5 manifest-tail rewrite candidates (promote freeze)",
            "",
            "| Candidate | Promote target | W5 / Iris batch | Status |",
            "|-----------|----------------|-----------------|--------|",
            *w5_table_rows,
        ]
    )

    if PROJ_INDEX.is_file():
        idx = PROJ_INDEX.read_text(encoding="utf-8")
        marker = "| [[eden-edge-computing-candidate]] |"
        if marker in idx and "kbr-cyber-range-rewrite-candidate" not in idx:
            idx = idx.replace(
                marker,
                block_morning + "\n" + marker,
                1,
            )
        if "## W5 manifest-tail rewrite candidates" not in idx:
            idx = idx.rstrip() + block_table + "\n"
        else:
            for line in w5_table_rows:
                if line.split("|")[1].strip() not in idx:
                    idx = re.sub(
                        r"(## W5 manifest-tail rewrite candidates.*?\n\|[-| ]+\|\n)",
                        r"\1" + line + "\n",
                        idx,
                        count=1,
                        flags=re.DOTALL,
                    )
        if not dry_run:
            PROJ_INDEX.write_text(idx, encoding="utf-8")

    if ROOT_INDEX.is_file():
        root = ROOT_INDEX.read_text(encoding="utf-8")
        old = "**W5×10** candidates may remain on branch for separate promote batch."
        new = (
            "**W5×10** manifest-tail capabilities — **Promoted 2026-07-05** "
            f"(lighthouse; Clio `{WAVE_COMMIT}`); see `agents/hephaestus/content/2026-07-05_promote-w5.md`."
        )
        if old in root:
            root = root.replace(old, new, 1)
        if not dry_run:
            ROOT_INDEX.write_text(root, encoding="utf-8")

    log_block = (
        "\n## [2026-07-05] promote | W5 lighthouse batch (10 capabilities)\n"
        f"- Hephaestus: in-place REWRITE ×10 — slugs from Clio ship `{WAVE_COMMIT}`\n"
        "- Archived → `generated-projections/archived/*-promoted-20260705.md`\n"
        "- Ship: `agents/hephaestus/content/2026-07-05_promote-w5.md`\n"
        f"- `reviewed_by`: {REVIEWED_BY} | Odysseus PASS (QMS levels, sustainment $, Iron Stallion PP open questions)\n"
        "- by: hephaestus | branch: feature/knowledge-vault-v1\n"
    )
    if not dry_run and "W5 lighthouse batch (10 capabilities)" not in LOG.read_text(encoding="utf-8"):
        with LOG.open("a", encoding="utf-8") as f:
            f.write(log_block)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    now = datetime.now(timezone.utc)
    now_iso = now.strftime("%Y-%m-%dT%H:%M:%SZ")
    stamp = now.strftime("%Y%m%d")

    results = []
    for num, slug in SLUGS:
        results.append(promote_one(num, slug, now_iso, stamp, args.dry_run))

    patch_indexes(args.dry_run)

    for r in results:
        print(r)
    print("index patches:", "skipped" if args.dry_run else "applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())