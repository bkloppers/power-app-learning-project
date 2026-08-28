# NTT DATA Basecoat Icon Module Sources

Status: SOURCE-SUPPLIED / IMPLEMENTATION-PENDING
Baseline: 2026-08-28

## User-supplied authoritative references

### Close button

Reference page:

`https://basecoat.nttdata.com/css-modules/close.html`

CSS module:

`https://basecoat.nttdata.com/5/css/module.close.min.css`

Project interpretation:

- the Basecoat close/X control is governed by the dedicated Close CSS module;
- do not treat the close/X control as just another generic icon from the general Icons module;
- when reproducing the NTT DATA close control in Power Apps, its final visual treatment must be checked against the Close module rather than inferred from a Fluent icon.

### Other button/UI icons

Reference page:

`https://basecoat.nttdata.com/css-modules/icons.html`

CSS module:

`https://basecoat.nttdata.com/5/css/module.icons.min.css`

Project interpretation:

- other generic UI/button glyphs are governed by the Basecoat Icons module;
- this applies to application-shell glyphs such as navigation arrows, menu/hamburger and similar utility controls, subject to the exact glyphs/classes actually exposed by that module;
- do not silently substitute a Power Apps Fluent glyph and call it NTT/Basecoat brand-final.

## Verification boundary

The current web tool could not fetch these Basecoat pages/CSS resources on 2026-08-28, so this file records the exact source locations supplied by the user and does not invent CSS selectors, pseudo-elements, Font Awesome class names, Unicode code points, dimensions or glyph mappings that were not directly retrieved.

The existing project corpus independently verifies that Basecoat uses a dedicated Icons module and a dedicated Close module, and that Font Awesome is prescribed by Basecoat for generic UI glyphs. The exact module-level glyph mapping remains the next implementation dependency.

## Power Apps consequence

The selected implementation sequence is:

1. Keep the current component behavior contracts unchanged.
2. Verify the exact Basecoat close/menu/back glyph appearance and source semantics from the relevant module before replacing or approving any Power Apps icon.
3. Reproduce the verified visual glyph in Power Apps using an implementation that preserves accessibility and dark/light theming.
4. Only then mark the icon BRAND-FINAL.

No hamburger/menu properties, events or controls have been added yet. No page-navigation/footer component has been created yet.
