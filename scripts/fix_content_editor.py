from pathlib import Path

p = Path(__file__).resolve().parents[1] / "index.html"
t = p.read_text(encoding="utf-8")
old = '<textarea class="editor-area" id="contentEditArea">${esc(selectedText)}</textarea>'
new = '<textarea class="editor-area" id="contentEditArea"></textarea>'
if old not in t:
    raise SystemExit("pattern missing")
t = t.replace(old, new, 1)
needle = "data-content-cancel-edit>Cancel</button></div>`}"
if "ta.value=selectedText" not in t:
    t = t.replace(needle, needle + ";const ta=$('contentEditArea');if(ta)ta.value=selectedText", 1)
p.write_text(t, encoding="utf-8")
print("OK editor")