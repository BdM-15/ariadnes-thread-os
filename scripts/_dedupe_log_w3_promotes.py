"""Remove all W3 lighthouse #5-#8 promote lines from log.md; append one block at EOF."""
from pathlib import Path
import re

REPO = Path(__file__).resolve().parents[1]
LOG = REPO / "knowledge" / "log.md"

PROMOTE_RE = re.compile(
    r"^## \[2026-07-05\] promote \| "
    r"(Athena Data Management Suite|ENCOMPASS Digital Twin Platform|"
    r"HAL Adaptive Learning Framework|Dash C3 Decision Support) \|"
)

BLOCK = """
## [2026-07-05] promote | Athena Data Management Suite | review:e1a4b6c8-2d3f-4e5a-9b7c-8d0e1f2a3b4c | from:generated-projections/athena-data-management-suite-rewrite-candidate.md → global/domain_intel/capabilities/athena-data-management-suite.md | by:axelrod2023 | W3 lighthouse #5

## [2026-07-05] promote | ENCOMPASS Digital Twin Platform | review:f2b5c7d9-3e4f-5a6b-0c8d-9e0f1a2b3c4d | from:generated-projections/encompass-digital-twin-platform-rewrite-candidate.md → global/domain_intel/capabilities/encompass-digital-twin-platform.md | by:axelrod2023 | W3 lighthouse #6

## [2026-07-05] promote | HAL Adaptive Learning Framework | review:a3c6d8e0-4f5a-6b7c-1d9e-0f1a2b3c4d5e | from:generated-projections/hal-adaptive-learning-framework-rewrite-candidate.md → global/domain_intel/capabilities/hal-adaptive-learning-framework.md | by:axelrod2023 | W3 lighthouse #7

## [2026-07-05] promote | Dash C3 Decision Support | review:b4d7e9f1-5a6b-7c8d-2e0f-1a2b3c4d5e6f | from:generated-projections/dash-c3-decision-support-rewrite-candidate.md → global/domain_intel/capabilities/dash-c3-decision-support.md | by:axelrod2023 | W3 lighthouse #8
""".strip()


def main() -> None:
    lines = LOG.read_text(encoding="utf-8").splitlines()
    out = [ln for ln in lines if not PROMOTE_RE.match(ln)]
    text = "\n".join(out).rstrip() + "\n\n" + BLOCK + "\n"
    LOG.write_text(text, encoding="utf-8")
    print("cleaned W3 #5-8 promotes; appended single block at EOF")


if __name__ == "__main__":
    main()