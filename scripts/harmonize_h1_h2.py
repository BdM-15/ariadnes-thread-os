#!/usr/bin/env python3
"""H1-H2 vault harmonize: capabilities wikilinks, trust YAML, index + log refresh.

Single-writer batch pass from repo root. Run: python scripts/harmonize_h1_h2.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VAULT = REPO_ROOT / "knowledge"
CAPABILITIES = VAULT / "global" / "domain_intel" / "capabilities"

WIKILINK = re.compile(r"\[\[([^\]|#]+)")
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
TRUST_LINE = re.compile(r"^(trust:\s*)(.+)$", re.MULTILINE)
SUFFIX = "-rewrite-candidate"

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
    "opportunity_name",
    "agency-name",
    "competitor-name",
)


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _md_files() -> list[Path]:
    return [p for p in VAULT.rglob("*.md") if ".obsidian" not in p.parts]


def _normalize_trust_value(raw: str) -> str:
    v = raw.strip()
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        v = v[1:-1]
    if v in ("trusted", "candidate", "archived"):
        return v
    return raw.strip()


def normalize_trust_in_text(text: str) -> tuple[str, int]:
    if not text.startswith("---"):
        return text, 0
    end = text.find("\n---", 3)
    if end < 0:
        return text, 0
    fm = text[: end + 4]
    body = text[end + 4 :]
    changes = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal changes
        prefix, val = m.group(1), m.group(2)
        new = _normalize_trust_value(val)
        if new != val.strip():
            changes += 1
        return f"{prefix}{new}"

    return TRUST_LINE.sub(repl, fm) + body, changes


def promoted_slug_for_candidate(link: str) -> str | None:
    if not link.endswith(SUFFIX):
        return None
    slug = link[: -len(SUFFIX)]
    if (CAPABILITIES / f"{slug}.md").is_file():
        return slug
    return None


def fix_rewrite_candidate_links(text: str) -> tuple[str, int]:
    changes = 0

    def repl(m: re.Match[str]) -> str:
        nonlocal changes
        link = m.group(1).strip()
        promoted = promoted_slug_for_candidate(link)
        if promoted:
            changes += 1
            return f"[[{promoted}]]"
        return m.group(0)

    return WIKILINK.sub(repl, text), changes


def _stub_fm(name: str, page_type: str, stub_id: str, citations: str) -> str:
    return (
        f"---\nname: \"{name}\"\ntype: {page_type}\nid: {stub_id}\n"
        f"trust: trusted\nlast_updated: {_now()}\ncitations: \"{citations}\"\n"
        f"tags: [stub, harmonize-h1-h2]\n---\n\n"
    )


def ensure_stubs(stats: dict[str, int]) -> None:
    dict_cite = "foundation/reference/briefing-packet-data-dictionary.md"
    stubs: list[tuple[Path, str]] = []

    for key in DATA_ELEMENT_KEYS:
        body = (
            _stub_fm(key, "data-element", f"data-element-{key}", dict_cite)
            + f"# {key}\n\nBriefing packet field stub. See [[briefing-packet-data-dictionary]].\n\n"
            + "## Related\n- [[briefing-packet-data-dictionary]]\n- [[ariadne-vault-schema]]\n"
        )
        stubs.append((VAULT / "data-elements" / f"{key}.md", body))

    stubs.extend(
        [
            (
                VAULT / "data-elements" / "INDEX.md",
                _stub_fm("data-elements-index", "meta", "data-elements-index", dict_cite)
                + "# Data elements (deferred ontology)\n\n"
                + "Packet field keys. Canonical: [[briefing-packet-data-dictionary]].\n",
            ),
            (
                VAULT / "foundation" / "reference" / "wikilinks.md",
                _stub_fm("wikilinks", "reference", "ref-wikilinks", "foundation/reference/obsidian-desktop.md")
                + "# Wikilinks (Obsidian)\n\n"
                + "Vault pages connect via Obsidian double-bracket link syntax. "
                + "See [[obsidian-desktop]] and [[ariadne-vault-schema]].\n",
            ),
            (
                VAULT / "entities" / "customers" / "department-of-the-army.md",
                _stub_fm("Department of the Army", "customer_agency", "customer-agency-army", "ariadne-vault-schema")
                + "# Department of the Army\n\nStub customer agency page.\n\n"
                + "## Related\n- [[army-logcap-funding-office]]\n- [[logcap]]\n",
            ),
            (
                VAULT / "global" / "global_wiki" / "capture" / "concepts" / "usaspending-plain-english.md",
                _stub_fm("USAspending plain English", "concept", "concept-usaspending-plain-english", "iris")
                + "# USAspending - plain English\n\n"
                + "## Related\n- [[ariadne-vault-schema]]\n",
            ),
            (
                VAULT / "entities" / "entities.md",
                _stub_fm("entities hub", "meta", "entities-hub", "entities/INDEX.md")
                + "# Entities zone hub\n\nRead zone INDEX under entities/.\n",
            ),
            (
                VAULT / "entities" / "customers" / "army-logcap-funding-office.md",
                _stub_fm(
                    "Army LOGCAP funding office",
                    "customer_office_funding",
                    "customer-army-logcap-funding-office",
                    "ariadne-vault-schema",
                )
                + "# Army LOGCAP funding office\n\n## Related\n- [[logcap]]\n- [[department-of-the-army]]\n",
            ),
            (
                VAULT / "entities" / "customers" / "logcap.md",
                _stub_fm("LOGCAP", "customer_program", "customer-program-logcap", "ariadne-vault-schema")
                + "# LOGCAP\n\n## Related\n- [[army-logcap-funding-office]]\n- [[logcap-v-contract]]\n",
            ),
            (
                VAULT / "entities" / "customers" / "dhs.md",
                _stub_fm("Department of Homeland Security", "customer_agency", "customer-agency-dhs", "stub")
                + "# Department of Homeland Security (DHS)\n\nStub agency page.\n",
            ),
            (
                VAULT / "entities" / "agencies" / "dhs.md",
                _stub_fm("DHS (legacy path)", "customer_agency", "customer-agency-dhs-legacy-path", "entities/customers/dhs.md")
                + "# DHS (legacy path)\n\nCanonical: [[dhs]].\n",
            ),
            (
                VAULT / "dhs.md",
                _stub_fm("DHS alias", "customer_agency", "customer-agency-dhs-root-alias", "entities/customers/dhs.md")
                + "# DHS (alias)\n\nSee [[entities/customers/dhs]].\n",
            ),
        ]
    )

    for path, content in stubs:
        if path.exists():
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        stats["stubs_created"] = stats.get("stubs_created", 0) + 1


def patch_welcome(text: str) -> str:
    return text.replace("[[create a link]]", "create a link")


def refresh_index_md(md_count: int, trusted_count: int) -> None:
    index_path = VAULT / "index.md"
    text = index_path.read_text(encoding="utf-8")
    text = re.sub(
        r">\s*\*\*Last refreshed:\*\*[^\n]+",
        (
            f"> **Last refreshed:** {_now()} (H1-H2 harmonize) | **~{md_count}** markdown files "
            f"| **~{trusted_count}** `trust: trusted` (see latest `log.md` lint block)"
        ),
        text,
        count=1,
    )
    index_path.write_text(text, encoding="utf-8", newline="\n")


def count_trusted() -> int:
    n = 0
    for p in _md_files():
        t = p.read_text(encoding="utf-8", errors="replace")
        for m in TRUST_LINE.finditer(t):
            if _normalize_trust_value(m.group(2)) == "trusted":
                n += 1
    return n


def lint_missing_count() -> int:
    md_files = _md_files()
    stems: set[str] = set()
    for p in md_files:
        stems.add(p.stem)
        rel = p.relative_to(VAULT).with_suffix("").as_posix()
        stems.add(rel.split("/")[-1])
        stems.add(rel)

    def resolves(link: str) -> bool:
        link = link.strip()
        if link in stems:
            return True
        if (VAULT / f"{link}.md").is_file():
            return True
        n = link.replace("\\", "/")
        return (VAULT / f"{n}.md").is_file()

    links: list[str] = []
    for p in md_files:
        scan = FENCE.sub("", p.read_text(encoding="utf-8", errors="replace"))
        for m in WIKILINK.finditer(scan):
            links.append(m.group(1).strip())
    return len({ln for ln in links if not resolves(ln)})


def append_log(summary: str) -> None:
    log = VAULT / "log.md"
    with log.open("a", encoding="utf-8") as f:
        f.write(f"\n## [{_now()}] harmonize | H1-H2 capabilities + index\n")
        f.write(summary)
        f.write("\n")


def main() -> int:
    stats: dict[str, int] = {}
    ensure_stubs(stats)

    wl = VAULT / "foundation" / "reference" / "wikilinks.md"
    if wl.is_file():
        fixed = wl.read_text(encoding="utf-8").replace(
            "Vault pages connect via `[[slug]]`.",
            "Vault pages connect via Obsidian double-bracket link syntax.",
        )
        if fixed != wl.read_text(encoding="utf-8"):
            wl.write_text(fixed, encoding="utf-8", newline="\n")

    for p in _md_files():
        text = p.read_text(encoding="utf-8", errors="replace")
        original = text
        t1, c1 = normalize_trust_in_text(text)
        t2, c2 = fix_rewrite_candidate_links(t1)
        if p.name == "Welcome.md":
            t2 = patch_welcome(t2)
        if t2 != original:
            p.write_text(t2, encoding="utf-8", newline="\n")
            stats["files_patched"] = stats.get("files_patched", 0) + 1
            stats["trust_fixes"] = stats.get("trust_fixes", 0) + c1
            stats["link_retargets"] = stats.get("link_retargets", 0) + c2

    md_count = len(_md_files())
    trusted_count = count_trusted()
    refresh_index_md(md_count, trusted_count)

    missing = lint_missing_count()
    stats["missing_wikilinks"] = missing
    stats["markdown_files"] = md_count
    stats["trusted_hits"] = trusted_count

    summary_lines = [f"- {k}: {v}" for k, v in sorted(stats.items())]
    append_log("\n".join(summary_lines) + "\n")

    subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "vault_lint.py"), "--no-append-log"],
        cwd=REPO_ROOT,
        check=False,
    )
    subprocess.run([sys.executable, str(REPO_ROOT / "scripts" / "vault_lint.py")], cwd=REPO_ROOT, check=False)

    print("harmonize_h1_h2 complete:", stats)
    if missing != 0:
        print(f"ERROR: unresolved wikilinks still {missing}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())