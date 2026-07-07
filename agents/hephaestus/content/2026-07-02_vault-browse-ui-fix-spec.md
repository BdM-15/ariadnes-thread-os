# MC Vault browse sidebar — UI fix spec (Wave A)

**Date:** 2026-07-02  
**DRI:** Hephaestus · **Discipline:** backup before `index.html` edit

## Root cause

Vault browse renders **three rows** per card (`doc-badge`, `doc-title`, `doc-time` with **full path**). Content tab uses two rows only. `.doc-list` has `padding-right: 2px` — insufficient scrollbar gutter; children lack `min-width: 0` / ellipsis.

## CSS (vault-scoped)

```css
#panel-vault .doc-list{
  scrollbar-gutter:stable;
  padding-inline-end:12px;
  overflow-x:hidden;
}
#panel-vault .doc-item{
  min-width:0;
  width:100%;
  box-sizing:border-box;
}
#panel-vault .doc-title,
#panel-vault .doc-time{
  min-width:0;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
}
```

## JS (`renderVaultBrowse`)

- Keep `doc-time` but set `title="${esc(f.path)}"` for tooltip.
- Optional: show **filename only** in `doc-time` (zone filter already set context).

## Acceptance

No overlap with scrollbar at 1080p; queue + browse with 200+ entries.

## Ref

Hermes brainstorm §1 · `deleg_251b596d` task 1.