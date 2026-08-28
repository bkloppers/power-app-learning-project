# Component Library Iconography Decision

Status: ACTIVE / BRAND-FIRST / IMPLEMENTATION-PENDING
Baseline: 2026-08-28

## Source basis

NTT DATA Brand Portal sources supplied by the user:

- Digital Iconography: `https://basecoat.nttdata.com/components.iconography.html#glyphs`
- Close module: `https://basecoat.nttdata.com/css-modules/close.html`
- Close CSS: `https://basecoat.nttdata.com/5/css/module.close.min.css`
- Icons module: `https://basecoat.nttdata.com/css-modules/icons.html`
- Icons CSS: `https://basecoat.nttdata.com/5/css/module.icons.min.css`

The project corpus also contains a verified 2026-08-23 capture of the NTT DATA iconography and Basecoat guidance.

## Brand-first rule

All reusable UI components must be implemented with the approved NTT DATA/Basecoat visual language from the first working version.

There is no temporary-Fluent-then-brand-later phase for shell controls.

If the exact brand-correct glyph or rendering method has not yet been verified for Power Apps, stop that control's implementation at the dependency boundary and verify the brand source first. Do not insert a Fluent approximation merely to keep building.

## Icon source ownership

1. NTT DATA Brand Icons library
   - Primary source for brand-facing/content-facing illustrative icons.
   - Verified library contains 418 SVG assets with the documented NTT DATA stroke system.

2. Basecoat Icons module
   - Source for generic UI/application-shell glyphs such as back, previous, next, hamburger/menu, carets, checks and related interaction chrome.
   - Power Apps Fluent glyphs are not presumed equivalent.

3. Basecoat Close module
   - Dedicated source for Close/X controls.
   - Close/X is not treated as just another general icon.

## Current cmpAppHeader correction

`btnHeaderBack` currently exists with a Modern Button and `Icon = "ArrowLeft"` from an earlier instruction.

That visual implementation is now explicitly marked SUPERSEDED / NOT APPROVED because it violates the brand-first rule.

The behavior contract remains correct:

```powerfx
btnHeaderBack.OnSelect = cmpAppHeader.OnBack()
```

The control must not be considered complete until its visual glyph is replaced with a verified Basecoat Icons-module implementation suitable for Power Apps.

Do not add the hamburger/menu control until its Basecoat Icons-module implementation is verified.

Do not build a sidebar Close/X control until its Basecoat Close-module implementation is verified.

## Footer previous/next

Sequential Previous/Next navigation belongs in a separate reusable page-navigation/footer component, not in `cmpAppHeader`.

Its previous/next glyphs must also use the verified Basecoat Icons-module approach from first implementation.

## Prohibited pattern

Do not use this project pattern:

`temporary Fluent icon -> later replace with brand icon`

Use this pattern instead:

`verify NTT/Basecoat source -> implement brand-correct control -> validate in Power Apps`
