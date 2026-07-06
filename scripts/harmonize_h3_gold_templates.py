#!/usr/bin/env python3
"""H3 harmonize — five trusted gold templates (batch only, repo root).

Zones: capability, shipley_concept, foundation_reference, entity, concept.
Rubric: Evidence + Gaps sections, min 2 outbound wikilinks, normalized frontmatter.
"""
from __future__ import annotations

import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
VAULT = REPO / "knowledge"
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

# One trusted page per rubric zone (repo-relative under knowledge/)
GOLD: list[tuple[str, str]] = [
    ("capability", "global/domain_intel/capabilities/kbr-cyber-range.md"),
    ("shipley_concept", "global/domain_intel/concepts/shipley-capture-guide-hub.md"),
    ("foundation_reference", "foundation/reference/shipley-capture-guide-source.md"),
    ("entity", "entities/companies/kbr-services-readiness-sustainment.md"),
    ("concept", "global/domain_intel/concepts/shipley-decision-gate-reviews.md"),
]

FM_BOUND = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK = re.compile(r"\[\[([^\]|#]+)")
SECTION_EVIDENCE = re.compile(r"^##\s+Evidence\s*$", re.MULTILINE)
SECTION_GAPS = re.compile(r"^##\s+Gaps\s*$", re.MULTILINE)
SECTION_RELATED = re.compile(r"^##\s+Related\s*$", re.MULTILINE)


def _parse_frontmatter(text: str) -> tuple[dict[str, str], str, str]:
    m = FM_BOUND.match(text)
    if not m:
        return {}, "", text
    raw = m.group(1)
    body = text[m.end() :]
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta, raw, body


def _render_frontmatter(meta: dict[str, str]) -> str:
    order = [
        "name",
        "type",
        "id",
        "trust",
        "review_id",
        "reviewed_by",
        "reviewed_at",
        "added",
        "last_updated",
        "citations",
        "tags",
        "aliases",
        "source_module",
        "entity_type",
        "title",
    ]
    lines: list[str] = ["---"]
    seen: set[str] = set()
    for k in order:
        if k in meta and meta[k]:
            lines.append(f'{k}: "{meta[k]}"' if " " in meta[k] or ":" in meta[k] else f"{k}: {meta[k]}")
            seen.add(k)
    for k, v in sorted(meta.items()):
        if k in seen or not v:
            continue
        if k in ("auto_generated", "updated"):
            continue
        lines.append(f'{k}: "{v}"' if " " in v or ":" in v else f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _count_outbound_wikilinks(body: str) -> int:
    related_idx = SECTION_RELATED.search(body)
    scan = body[: related_idx.start()] if related_idx else body
    return len(set(WIKILINK.findall(scan)))


def _ensure_sections(body: str, zone: str) -> str:
    body = body.strip() + "\n"
    if not SECTION_EVIDENCE.search(body):
        insert = (
            "## Evidence\n"
            "- Trusted page; cite Layer 1 sources in `citations` and bullets below.\n"
            "- Harmonize H3 gold template — append dated evidence; do not erase prior trusted history.\n\n"
        )
        if SECTION_GAPS.search(body):
            body = body.replace("## Gaps", insert + "## Gaps", 1)
        elif SECTION_RELATED.search(body):
            body = body.replace("## Related", insert + "## Related", 1)
        else:
            body += "\n" + insert
    if not SECTION_GAPS.search(body):
        gaps = (
            "## Gaps\n"
            "- Open questions and unverified claims belong here until Iris/Overwatch closes them.\n\n"
        )
        if SECTION_RELATED.search(body):
            body = body.replace("## Related", gaps + "## Related", 1)
        else:
            body += "\n" + gaps
    if _count_outbound_wikilinks(body) < 2:
        extra = (
            "\n## Related\n"
            "- [[ariadne-vault-schema]]\n"
            "- [[domain-intel]]\n"
        )
        if SECTION_RELATED.search(body):
            if "[[ariadne-vault-schema]]" not in body:
                body = body.replace("## Related", "## Related\n- [[ariadne-vault-schema]]", 1)
            if "[[domain-intel]]" not in body and zone != "foundation_reference":
                body = body.replace("## Related", "## Related\n- [[domain-intel]]", 1)
        else:
            body += extra
    return body


def _normalize_meta(meta: dict[str, str], zone: str, rel: str) -> dict[str, str]:
    stem = Path(rel).stem
    out = dict(meta)
    out["trust"] = "trusted"
    out["last_updated"] = TODAY
    out.pop("auto_generated", None)
    out.pop("updated", None)
    if zone == "foundation_reference" and not out.get("type"):
        out["type"] = "reference"
    if zone == "foundation_reference" and not out.get("id"):
        out["id"] = f"foundation-reference-{stem}"
    if zone == "foundation_reference" and not out.get("name"):
        out["name"] = stem.replace("-", " ").title()
    if not out.get("citations"):
        out["citations"] = f"harmonize:H3-gold-template • path:{rel}"
    if not out.get("added"):
        out["added"] = f"{TODAY}T12:00:00Z"
    return out


def harmonize_one(zone: str, rel: str) -> str:
    path = VAULT / rel.replace("\\", "/")
    if not path.is_file():
        return f"SKIP missing: {rel}"
    text = path.read_text(encoding="utf-8")
    meta, _, body = _parse_frontmatter(text)
    meta = _normalize_meta(meta, zone, rel)
    body = _ensure_sections(body, zone)
    new_text = _render_frontmatter(meta) + body.lstrip("\n")
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return f"OK updated: {rel}"
    return f"OK noop: {rel}"


def append_log(results: list[str]) -> None:
    log = VAULT / "log.md"
    block = (
        f"\n```\nH3 harmonize gold templates {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n"
        + "\n".join(f"  {r}" for r in results)
        + "\n```\n"
    )
    with log.open("a", encoding="utf-8") as f:
        f.write(block)


def touch_index() -> None:
    idx = VAULT / "index.md"
    if not idx.is_file():
        return
    text = idx.read_text(encoding="utf-8")
    marker = "**Last updated:**"
    line = f"**Last updated:** {TODAY} (H3 gold templates harmonize)\n"
    if marker in text:
        text = re.sub(r"\*\*Last updated:\*\*.*\n", line, text, count=1)
    else:
        text = line + "\n" + text
    idx.write_text(text, encoding="utf-8")


def main() -> int:
    results = [harmonize_one(z, r) for z, r in GOLD]
    for r in results:
        print(r)
    if any(r.startswith("SKIP") for r in results):
        return 1
    append_log(results)
    touch_index()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())