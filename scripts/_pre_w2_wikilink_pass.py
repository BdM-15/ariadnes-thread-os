"""One-off: G2 pre-W2 wikilink alias pass in knowledge/."""
from pathlib import Path

root = Path(__file__).resolve().parents[1] / "knowledge"
skip = {
    root / "foundation" / "capture-llm-wiki.md",
    root / "foundation" / "ariadne-vault-schema.md",
}
old, new = "[[capture-llm-wiki]]", "[[ariadne-vault-schema]]"
changed = []
for p in sorted(root.rglob("*.md")):
    if p in skip:
        continue
    text = p.read_text(encoding="utf-8")
    if old not in text:
        continue
    p.write_text(text.replace(old, new), encoding="utf-8")
    changed.append(p.relative_to(root.parent))
print(f"updated {len(changed)} files")
for c in changed:
    print(c)