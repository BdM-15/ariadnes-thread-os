#!/usr/bin/env python3
"""Idempotent knowledge vault bootstrap for ariadnes-thread-os (doc 02 v1).

Creates knowledge/thread/ layout, zone INDEX stubs, foundation seeds from
ariadne-capform reference corpus, and merges trusted starter content from
capform live vault (global_wiki, domain_intel, entities) — never overwrites
existing files. Skips data-elements/ and pursuit smoke folders.
"""
from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CAPFORM = Path(r"C:/Users/benma/ariadne-capform")

V1_DIRS = (
    "foundation",
    "foundation/reference",
    "entities",
    "entities/customers",
    "entities/companies",
    "global",
    "global/domain_intel",
    "global/global_wiki",
    "pursuits",
    "generated-projections",
    "generated-projections/archived",
    "relationships",
)

REFERENCE_COPIES: tuple[tuple[str, str], ...] = (
    ("vault/capture-llm-wiki.md", "foundation/capture-llm-wiki.md"),
    ("vault/OBSIDIAN_DESKTOP.md", "foundation/reference/obsidian-desktop.md"),
    ("briefing_packet/BRIEFING_PACKET_DATA_DICTIONARY.md", "foundation/reference/briefing-packet-data-dictionary.md"),
    ("briefing_packet/BRIEFING_PACKET_MODEL.md", "foundation/reference/briefing-packet-model.md"),
)

LIVE_VAULT_MERGE: tuple[tuple[str, str], ...] = (
    ("global/global_wiki", "global/global_wiki"),
    ("global/domain_intel", "global/domain_intel"),
    ("entities/customers", "entities/customers"),
    ("entities/companies", "entities/companies"),
)

ZONE_INDEX: dict[str, str] = {
    "entities/INDEX.md": """# Entities zone

**Where to start:** Agency or competitor name → `agencies/` or `competitors/` canonical `trust: trusted` page.

## Subfolders
- `agencies/` — customers / funding orgs (Iris maintains candidates)
- `competitors/` — primes, subs, recipients (Iris)

## Canonical files
_(Hephaestus refreshes on promote — grep `trust: trusted` in this zone.)_

## Archive boundary
Candidates live in `generated-projections/` until promote. Do not treat candidate prose as bid truth.

## Maintainer
Iris (intel) · promote via Odysseus gate · Hephaestus (index)
""",
    "global/INDEX.md": """# Global zone

**Where to start:** Evergreen doctrine → `global_wiki/`; bid fit / capabilities → `domain_intel/`.

## Subfolders
- `global_wiki/` — Shipley, FAR, workload, third-party patterns
- `domain_intel/` — company-specific capabilities, UEI/PP awareness

## Archive boundary
Historical notes marked `trust: archived` — INDEX lists them; agents skip unless asked.

## Maintainer
Iris + Clio (synthesis) · Hephaestus (lint/index)
""",
    "pursuits/INDEX.md": """# Pursuits zone

**Where to start:** One folder per tracked opportunity: `pursuits/<slug>/README.md`.

## Rules
- Pursuit-specific narrative only — not company-wide doctrine (use `global/`).
- Smoke/test folders may exist; prefer real slugs for production work.

## Maintainer
Clio (packet narrative) · Hermes (routing) · Hephaestus (scaffold new slug on request)
""",
    "generated-projections/INDEX.md": """# Generated projections (candidates)

**Where to start:** All LLM drafts land here with `trust: candidate` until Overwatch promotes.

## Subfolders
- `archived/` — rejected or superseded candidates

## Archive boundary
**Default agent path ends here** for unreviewed synthesis. Promoted pages move to `entities/`, `global/`, or `pursuits/`.

## Maintainer
Hermes (triage intake) · Hephaestus (dedup/lint)
""",
}


def _rel(vault: Path, path: Path) -> str:
    return str(path.relative_to(vault)).replace("\\", "/")


@dataclass
class Report:
    vault: Path
    created: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        return bool(self.created)


def _write_if_missing(path: Path, content: str, report: Report) -> None:
    if path.exists():
        report.skipped.append(_rel(report.vault, path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    report.created.append(_rel(report.vault, path))


def _copy_if_missing(src: Path, dest: Path, report: Report) -> None:
    if not src.is_file():
        return
    if dest.exists():
        report.skipped.append(_rel(report.vault, dest))
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dest)
    report.created.append(_rel(report.vault, dest))


def _merge_tree(src: Path, dest: Path, report: Report) -> None:
    if not src.is_dir():
        return
    for item in src.rglob("*"):
        if item.is_dir():
            continue
        target = dest / item.relative_to(src)
        if target.exists():
            report.skipped.append(_rel(report.vault, target))
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(item, target)
        report.created.append(_rel(report.vault, target))


def _build_root_index() -> str:
    return """---
name: "Ariadne Thread OS Knowledge Vault"
type: meta
id: vault-index
tags: [index, karpathy-wiki, thread-os]
---

# Knowledge vault (compounding SSOT)

**Doc:** `docs/inspiration/knowledge-vault-and-compounding-truth.md`

| Layer | Location | Rule |
|-------|----------|------|
| Staging | `agents/*/content/` | Session handoffs — not SSOT |
| Wiki | This tree | Candidate → Overwatch promote → trusted |
| Schema | `foundation/capture-llm-wiki.md` | Read before vault writes |

## Zones (read zone `INDEX.md` first)

- [[entities/INDEX]] — agencies, competitors
- [[global/INDEX]] — doctrine + domain intel
- [[pursuits/INDEX]] — per-opportunity
- [[generated-projections/INDEX]] — candidates only

## Catalog maintenance
Hephaestus rebuilds trusted lists on promote. Append lint lines to `log.md`.

Read [[capture-llm-wiki]] before maintaining this vault.
"""


def _build_log() -> str:
    return """---
name: Vault Activity Log
type: meta
id: vault-log
---

# Vault activity log

Append-only (ingest, lint, promote). Never delete history.
"""


def bootstrap(capform: Path, vault: Path, dry_run: bool = False) -> Report:
    report = Report(vault=vault)
    ref_root = capform / "docs" / "reference"
    live_vault = capform / "knowledge" / "thread"

    if dry_run:
        print(f"[dry-run] vault={vault} capform={capform}")
        return report

    vault.mkdir(parents=True, exist_ok=True)

    for name in V1_DIRS:
        d = vault / name
        if not d.exists():
            d.mkdir(parents=True, exist_ok=True)
            report.created.append(_rel(vault, d))

    for src_rel, dest_rel in REFERENCE_COPIES:
        _copy_if_missing(ref_root / src_rel, vault / dest_rel, report)

    if live_vault.is_dir():
        for src_rel, dest_rel in LIVE_VAULT_MERGE:
            _merge_tree(live_vault / src_rel, vault / dest_rel, report)

    _write_if_missing(vault / "index.md", _build_root_index(), report)
    _write_if_missing(vault / "log.md", _build_log(), report)

    for rel_path, body in ZONE_INDEX.items():
        _write_if_missing(vault / rel_path, body.strip() + "\n", report)

    _write_if_missing(
        vault / "relationships" / "README.md",
        "# Relationships\n\nFuture graph edges + wikilinks to entities.\n",
        report,
    )

    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    log = vault / "log.md"
    if log.exists():
        with log.open("a", encoding="utf-8") as f:
            f.write(f"\n- {ts} bootstrap_knowledge_vault.py — created {len(report.created)} paths\n")

    return report


def main() -> int:
    p = argparse.ArgumentParser(description="Bootstrap knowledge/thread (doc 02 v1)")
    p.add_argument("--capform", type=Path, default=DEFAULT_CAPFORM)
    p.add_argument("--vault", type=Path, default=REPO_ROOT / "knowledge" / "thread")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    if not args.capform.is_dir():
        print(f"capform root not found: {args.capform}", file=sys.stderr)
        return 1

    report = bootstrap(args.capform, args.vault, dry_run=args.dry_run)
    print(f"vault: {report.vault}")
    print(f"created: {len(report.created)}")
    for c in report.created[:40]:
        print(f"  + {c}")
    if len(report.created) > 40:
        print(f"  ... and {len(report.created) - 40} more")
    print(f"skipped (existing): {len(report.skipped)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())