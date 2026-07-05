#!/usr/bin/env python3
"""One-off: archive W3 product candidates after in-place promote (2026-07-05)."""
from pathlib import Path
import shutil
from datetime import datetime, timezone

REPO = Path(__file__).resolve().parents[1]
VAULT = REPO / "knowledge"
ARCH = VAULT / "generated-projections" / "archived"
STAMP = datetime.now(timezone.utc).strftime("%Y%m%d")

MOVES = [
    (
        "athena-data-management-suite-rewrite-candidate.md",
        "global/domain_intel/capabilities/athena-data-management-suite.md",
        "W3 lighthouse #5",
    ),
    (
        "encompass-digital-twin-platform-rewrite-candidate.md",
        "global/domain_intel/capabilities/encompass-digital-twin-platform.md",
        "W3 lighthouse #6",
    ),
    (
        "hal-adaptive-learning-framework-rewrite-candidate.md",
        "global/domain_intel/capabilities/hal-adaptive-learning-framework.md",
        "W3 lighthouse #7",
    ),
    (
        "dash-c3-decision-support-rewrite-candidate.md",
        "global/domain_intel/capabilities/dash-c3-decision-support.md",
        "W3 lighthouse #8",
    ),
]

def main() -> None:
    ARCH.mkdir(parents=True, exist_ok=True)
    for name, dest, lh in MOVES:
        src = VAULT / "generated-projections" / name
        if not src.is_file():
            raise SystemExit(f"missing: {src}")
        text = src.read_text(encoding="utf-8")
        reason = f'archived_reason: "promoted to {dest} ({lh})"'
        if "archived_reason:" not in text:
            text = text.replace("---\nadded:", f"---\n{reason}\nadded:", 1)
        out = ARCH / f"{src.stem}-promoted-{STAMP}.md"
        out.write_text(text, encoding="utf-8")
        src.unlink()
        print(f"archived {name} -> {out.name}")

if __name__ == "__main__":
    main()