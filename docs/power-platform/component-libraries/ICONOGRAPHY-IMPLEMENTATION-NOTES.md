# Iconography Implementation Notes

Status: ACTIVE / BRAND-FIRST / IMPLEMENTATION-PENDING
Baseline: 2026-08-28

## Exact Basecoat module split

Close/X controls use the dedicated Close module:

- documentation: `https://basecoat.nttdata.com/css-modules/close.html`
- CSS: `https://basecoat.nttdata.com/5/css/module.close.min.css`

Other button/application-shell icons use the Icons module:

- documentation: `https://basecoat.nttdata.com/css-modules/icons.html`
- CSS: `https://basecoat.nttdata.com/5/css/module.icons.min.css`

Digital iconography reference:

- `https://basecoat.nttdata.com/components.iconography.html#glyphs`

## Brand-first implementation rule

Do not implement temporary Fluent approximations for shell icons.

If the correct Basecoat glyph cannot yet be rendered in Power Apps with verified fidelity, stop that control at the dependency boundary and resolve the rendering method first.

Approved sequence:

`verify brand source -> implement brand-correct glyph -> validate component`

Disallowed sequence:

`insert Fluent approximation -> call it temporary -> replace later`

## Current header impact

`btnHeaderBack` currently contains a Modern Button with `Icon = "ArrowLeft"` from an earlier instruction.

That visual glyph is SUPERSEDED / NOT APPROVED and must be replaced before the back control is considered complete.

The behavior remains correct:

```powerfx
OnSelect = cmpAppHeader.OnBack()
```

No hamburger/menu control has been added.
No `ShowMenuButton` or `OnMenu` property has been added.
No footer/page-navigation component has been created.

When those controls are implemented, they must use the verified Basecoat module approach from the start.

## Verification boundary

The supplied Basecoat URLs were attempted through the current web environment on 2026-08-28 but could not be fetched. Therefore no selectors, class names, Unicode values, pseudo-elements, exact glyph codes, sizing or stroke rules are invented here.

Those details remain a hard dependency before implementation proceeds.
