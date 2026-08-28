# Iconography Implementation Notes

Status: ACTIVE / SOURCE-REFINED / IMPLEMENTATION-PENDING
Baseline: 2026-08-28

This note refines `ICONOGRAPHY-DECISION.md` and `CURRENT-HEADER-BASELINE.md` with the exact Basecoat module split supplied by the user.

## Exact module split

Close/X controls use the dedicated Close module:

- documentation: `https://basecoat.nttdata.com/css-modules/close.html`
- CSS: `https://basecoat.nttdata.com/5/css/module.close.min.css`

Other button/application-shell icons use the Icons module:

- documentation: `https://basecoat.nttdata.com/css-modules/icons.html`
- CSS: `https://basecoat.nttdata.com/5/css/module.icons.min.css`

This supersedes any interpretation that the Close/X control should be treated as just another icon from the general Icons module.

## Current header impact

No Power Apps controls or component properties have changed as a result of this source refinement.

- `btnHeaderBack` still exists with the current Fluent `Icon = "ArrowLeft"` implementation.
- It remains NOT BRAND-FINAL until the corresponding Basecoat Icons-module glyph is verified.
- No hamburger/menu control has been added.
- No `ShowMenuButton` or `OnMenu` custom property has been added.
- `conHeaderUserRow` remains unchanged.

When a sidebar/drawer close control is built, its visual source must be the dedicated Basecoat Close module rather than the general Icons module.

## Verification boundary

The supplied source URLs were attempted through the current web environment on 2026-08-28 but could not be fetched. Therefore this note records the exact user-supplied source locations and the module ownership they establish, without inventing selectors, glyph codes, class names, pseudo-elements, sizing or stroke details not retrieved from those resources.
