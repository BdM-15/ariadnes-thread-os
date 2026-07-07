from pathlib import Path
import subprocess
from pathlib import Path as P
ROOT = P(__file__).resolve().parents[1]

def safe_write(rel, body):
    subprocess.run(
        [str(ROOT / "scripts/safe_repo_write.py"), rel],
        input=body.encode("utf-8"),
        cwd=ROOT,
        check=True,
    )

p = ROOT / "agents/hermes/content/2026-07-05_autonomous-pipeline-status.md"
t = p.read_text(encoding="utf-8")
old = (
    "| **Harmonize program** | "
    + chr(96) + "2026-07-05_vault-llm-wiki-harmonize-program.md" + chr(96)
    + " |\n\n## In flight\n\n- **Harmonize H1–H2** — lint + index/log refresh ("
    + chr(96) + "llm-wiki" + chr(96) + " ritual)\n"
)
new = (
    "| **Harmonize program** | "
    + chr(96) + "2026-07-05_vault-llm-wiki-harmonize-program.md" + chr(96)
    + " |\n| **Harmonize H1–H2** | lint + index/log refresh ("
    + chr(96) + "llm-wiki" + chr(96) + " ritual) |\n"
    + "| **Shipley Capture Guide phase3** | "
    + chr(96) + "scripts/shipley_capture_guide_phase3_batch.py" + chr(96)
    + " + Clio log |\n| **H3 gold templates** | "
    + chr(96) + "scripts/harmonize_h3_gold_templates.py" + chr(96)
    + " confirm — Hephaestus "
    + chr(96) + "2026-07-06_harmonize-h3.md" + chr(96) + " |\n"
    + "| **Entities phase3b** | "
    + chr(96) + "scripts/entities_phase3b_migrate.py" + chr(96)
    + " + Odysseus gate |\n| **Phantom repair** | "
    + chr(96) + "deleg_45a91c1f" + chr(96)
    + " verified — no phantom tree; "
    + chr(96) + "vault_lint" + chr(96) + " exit 0 |\n\n## In flight\n\n"
    + "- **Harmonize H4+** — per program after H3 ship\n"
    + "- **EDEN candidate** — Overwatch gate\n"
)
if old not in t:
    raise SystemExit("pattern missing")
t = t.replace(old, new)
t = t.replace(
    "- **Shipley Capture Guide** — drop path TBD under repo (suggest "
    + chr(96) + "docs/reference/shipley/" + chr(96)
    + " or "
    + chr(96) + "knowledge/foundation/raw/shipley/" + chr(96) + ")",
    "- **Shipley Capture Guide (remaining)** — further batches after phase3 ingest",
)
t = t.replace(
    "## Next after H1–H2\n\n- H3 gold templates (5 pages)\n- EDEN candidate (your gate)\n- W1 company hub + W6 concepts when Shipley unblocks foundation",
    "## Next after H3 ship\n\n- W1 company hub + W6 concepts (foundation)\n- Company templates W7 one-at-a-time per Clio order",
)
safe_write("agents/hermes/content/2026-07-05_autonomous-pipeline-status.md", t)
print("OK")
