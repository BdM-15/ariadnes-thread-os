#!/usr/bin/env python3
"""Phase 3b: migrate entities zone to flat customers/ + companies/ layout.

Run from repo root:
  python scripts/entities_phase3b_migrate.py --dry-run
  python scripts/entities_phase3b_migrate.py --apply

See agents/hermes/content/2026-07-02_entities-hierarchy-design.md (Phase 3b).
"""
from __future__ import annotations

import argparse
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VAULT = REPO_ROOT / "knowledge"
ENTITIES = "entities"

LEGACY_SOURCES: dict[str, tuple[str, str]] = {
    "agencies": ("customers", "customer"),
    "competitors": ("companies", "company"),
    "company": ("companies", "company"),
}

ALLOWED_ENTITIES_ENTRIES = {
    "INDEX.md",
    "entities.md",
    "customers",
    "companies",
}

WIKILINK_PATH_REPLACEMENTS = [
    ("entities/agencies/", "entities/customers/"),
    ("entities/competitors/", "entities/companies/"),
    ("entities/company/", "entities/companies/"),
]

TYPE_FROM_LEGACY = {
    "agency": "customer_agency",
    "customer_agency": "customer_agency",
    "competitor": "company",
    "company": "company",
}

FM_BLOCK = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TYPE_LINE = re.compile(r"^type:\s*(\S+)\s*$", re.MULTILINE)
ORG_ROLE_LINE = re.compile(r"^org_role:\s*.+$", re.MULTILINE)
PARENT_CUSTOMER_LINE = re.compile(r"^parent_customer:\s*.+$", re.MULTILINE)


def _vault_entities(vault: Path) -> Path:
    return vault / ENTITIES


def _rel(vault: Path, path: Path) -> str:
    return path.relative_to(vault).as_posix()


def _update_frontmatter_customer(text: str) -> str:
    m = FM_BLOCK.match(text)
    if not m:
        return text
    fm, rest = m.group(1), text[m.end() :]
    typ_m = TYPE_LINE.search(fm)
    if typ_m:
        raw = typ_m.group(1).strip("\"'")
        if raw.startswith("customer_"):
            new_type = raw
        else:
            new_type = TYPE_FROM_LEGACY.get(raw, "customer_agency")
        fm = TYPE_LINE.sub(f"type: {new_type}", fm, count=1)
    else:
        fm = f"type: customer_agency\n{fm}"
    if not PARENT_CUSTOMER_LINE.search(fm) and "customer_root" not in fm:
        if "customer_agency" in fm or "customer_subagency" in fm:
            fm = fm.rstrip() + '\nparent_customer: "[[us-federal-customer-hub]]"\n'
        elif "customer_office" in fm or "customer_program" in fm:
            pass  # leave to manual / Iris promote
    new_text = f"---\n{fm}\n---\n{rest}"
    return new_text


def _update_frontmatter_company(text: str, from_competitors: bool) -> str:
    m = FM_BLOCK.match(text)
    if not m:
        return text
    fm, rest = m.group(1), text[m.end() :]
    fm = TYPE_LINE.sub("type: company", fm, count=1) if TYPE_LINE.search(fm) else f"type: company\n{fm}"
    if from_competitors and not ORG_ROLE_LINE.search(fm):
        if "relationship_to_us" not in fm:
            fm = fm.rstrip() + "\nrelationship_to_us:\n  - competitor\n"
    new_text = f"---\n{fm}\n---\n{rest}"
    return new_text


def _rewrite_wikilinks_in_text(text: str) -> str:
    for old, new in WIKILINK_PATH_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def _rewrite_vault_wikilinks(vault: Path, dry_run: bool) -> list[str]:
    touched: list[str] = []
    for p in vault.rglob("*.md"):
        if ".obsidian" in p.parts:
            continue
        raw = p.read_text(encoding="utf-8", errors="replace")
        updated = _rewrite_wikilinks_in_text(raw)
        if updated != raw:
            touched.append(_rel(vault, p))
            if not dry_run:
                p.write_text(updated, encoding="utf-8")
    return touched


def _migrate_legacy_files(vault: Path, dry_run: bool) -> list[str]:
    actions: list[str] = []
    ent = _vault_entities(vault)
    if not ent.is_dir():
        raise SystemExit(f"ERROR: missing {ent}")

    for legacy_dir, (dest_dir, kind) in LEGACY_SOURCES.items():
        src_root = ent / legacy_dir
        if not src_root.is_dir():
            continue
        for src in sorted(src_root.rglob("*.md")):
            slug = src.stem
            dest = ent / dest_dir / f"{slug}.md"
            src_rel = _rel(vault, src)
            dest_rel = _rel(vault, dest)
            if dest.exists():
                actions.append(f"skip-move (canonical exists): {src_rel} -> {dest_rel}")
                if not dry_run:
                    src.unlink()
                continue
            text = src.read_text(encoding="utf-8", errors="replace")
            if kind == "customer":
                text = _update_frontmatter_customer(text)
            else:
                text = _update_frontmatter_company(text, from_competitors=legacy_dir == "competitors")
            text = _rewrite_wikilinks_in_text(text)
            actions.append(f"move: {src_rel} -> {dest_rel}")
            if not dry_run:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_text(text, encoding="utf-8")
                src.unlink()
    return actions


def _remove_empty_legacy_dirs(vault: Path, dry_run: bool) -> list[str]:
    removed: list[str] = []
    ent = _vault_entities(vault)
    for legacy_dir in LEGACY_SOURCES:
        d = ent / legacy_dir
        if not d.is_dir():
            continue
        if any(d.rglob("*")):
            raise SystemExit(f"ERROR: legacy dir not empty after migration: {d}")
        removed.append(_rel(vault, d))
        if not dry_run:
            d.rmdir()
    return removed


def _check_e1(vault: Path) -> list[str]:
    violations: list[str] = []
    ent = _vault_entities(vault)
    for child in ent.iterdir():
        name = child.name
        if name in ALLOWED_ENTITIES_ENTRIES:
            continue
        violations.append(f"E1: disallowed entry under entities/: {name}")
    return violations


def _refresh_index(vault: Path, dry_run: bool) -> str:
    ent = _vault_entities(vault)
    index_path = ent / "INDEX.md"
    customers = sorted((ent / "customers").glob("*.md")) if (ent / "customers").is_dir() else []
    companies = sorted((ent / "companies").glob("*.md")) if (ent / "companies").is_dir() else []
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total = len(customers) + len(companies)

    lines = [
        "# Entities zone (v2)",
        "",
        f"**Last updated:** {today} (Phase 3b) | **Pages:** {total} under `customers/` + `companies/`",
        "",
        "**Layout:** Two flat folders — `customers/` (federal buying side) and `companies/` "
        "(KBR, primes, subs, JVs). Hierarchy lives in **frontmatter** "
        "(`parent_customer`, `parent_company`), not nested directories.",
        "",
        "## Subfolders",
        "",
        "| Folder | Who | Example |",
        "|--------|-----|---------|",
        "| `customers/` | Federal customers, offices, programs | `us-federal-customer-hub.md` |",
        "| `companies/` | One page per company name (roles in frontmatter) | "
        "`kbr-services-readiness-sustainment.md` |",
        "",
        "**Retired (Phase 3b):** `agencies/` → `customers/`; `competitors/` + `company/` → `companies/`.",
        "",
        "## Customer pages",
        "",
    ]
    for p in customers:
        lines.append(f"- `customers/{p.name}`")
    lines.extend(["", "## Company pages", ""])
    for p in companies:
        lines.append(f"- `companies/{p.name}`")
    lines.extend(
        [
            "",
            "## Canonical files (trusted)",
            "",
            "- `companies/kbr-services-readiness-sustainment.md` — **Overwatch company SSOT** "
            "(`org_role: self`)",
            "- `customers/us-federal-customer-hub.md` — federal customer outline (incremental population)",
            "",
            "## Frontmatter patterns",
            "",
            "**Customers:** `type` ∈ `customer_agency` | `customer_subagency` | `customer_office_funding` | "
            "`customer_office_contracting` | `customer_program`; use `parent_customer` to walk the chain.",
            "",
            "**Companies:** `type: company`; `relationship_to_us` (competitor, teammate, etc.) on one page — "
            "do not split competitor/partner folders.",
            "",
            "## Deep company knowledge",
            "",
            "Capability depth lives in `global/domain_intel/capabilities/` — **linked from** the company entity, "
            "not duplicated.",
            "",
            "## Archive boundary",
            "",
            "Candidates → `generated-projections/` until promote. **Promote freeze:** on until Overwatch lifts "
            "(Item 4).",
            "",
            "## Maintainer",
            "",
            "Iris (external entities) · Clio (pursuit links) · Hephaestus (index/lint) · Overwatch (company entity)",
            "",
        ]
    )
    body = "\n".join(lines)
    if not dry_run:
        index_path.write_text(body, encoding="utf-8")
    return _rel(vault, index_path)


def _unresolved_wikilink_count(vault: Path) -> int:
    """Reuse vault_lint heuristic."""
    import importlib.util

    spec = importlib.util.spec_from_file_location("vault_lint", REPO_ROOT / "scripts" / "vault_lint.py")
    if spec is None or spec.loader is None:
        raise SystemExit("ERROR: cannot load vault_lint.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    report = mod.lint(vault, append_log=False)
    for line in report.splitlines():
        if "unresolved wikilinks" in line:
            m = re.search(r":\s*(\d+)", line)
            if m:
                return int(m.group(1))
    return -1


def main() -> None:
    ap = argparse.ArgumentParser(description="Entities zone Phase 3b migration")
    ap.add_argument("--vault", type=Path, default=DEFAULT_VAULT)
    ap.add_argument("--dry-run", action="store_true", help="Plan only (default if --apply omitted)")
    ap.add_argument("--apply", action="store_true", help="Write changes")
    args = ap.parse_args()
    dry_run = not args.apply
    vault = args.vault.resolve()

    print(f"Phase 3b entities migration ({'DRY RUN' if dry_run else 'APPLY'})")
    print(f"Vault: {vault}")

    move_actions = _migrate_legacy_files(vault, dry_run=dry_run)
    for a in move_actions:
        print(f"  {a}")

    link_touched = _rewrite_vault_wikilinks(vault, dry_run=dry_run)
    print(f"Wikilink rewrite files: {len(link_touched)}")

    if not dry_run:
        removed = _remove_empty_legacy_dirs(vault, dry_run=False)
        for r in removed:
            print(f"  removed dir: {r}")
    else:
        ent = _vault_entities(vault)
        for legacy_dir in LEGACY_SOURCES:
            d = ent / legacy_dir
            if d.is_dir() and not any(d.rglob("*.md")):
                print(f"  would remove empty dir: {_rel(vault, d)}")

    index_rel = _refresh_index(vault, dry_run=dry_run)
    print(f"INDEX refreshed: {index_rel}")

    if not dry_run:
        e1 = _check_e1(vault)
        if e1:
            for v in e1:
                print(v)
            raise SystemExit(1)
        unresolved = _unresolved_wikilink_count(vault)
        print(f"vault_lint unresolved wikilinks: {unresolved}")
        if unresolved != 0:
            raise SystemExit(f"ERROR: expected 0 unresolved wikilinks, got {unresolved}")
    else:
        print("(E1 / vault_lint check runs on --apply only)")


if __name__ == "__main__":
    main()