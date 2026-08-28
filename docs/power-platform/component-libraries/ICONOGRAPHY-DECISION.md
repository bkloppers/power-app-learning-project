# Component Library Iconography Decision

Status: ACTIVE / BRAND-SOURCE-VERIFIED / IMPLEMENTATION-PENDING
Baseline: 2026-08-28

## Source basis

User supplied the NTT DATA Brand Portal Digital Iconography page:

`https://basecoat.nttdata.com/components.iconography.html#glyphs`

The live page could not be fetched from the current tool environment on 2026-08-28. The project corpus already contains a verified 2026-08-23 capture of the same NTT DATA Brand Portal iconography guidance and the Basecoat distribution guidance. That verified project source is therefore the basis of this decision.

## Brand iconography rule

The NTT DATA system contains two distinct icon sources with different purposes:

1. NTT DATA Brand Icons library
   - 418 verified SVG assets.
   - 72x72 viewBox.
   - line/stroke style with rounded caps and joins.
   - Future Blue is the native/default stroke color.
   - intended first for brand-facing/content-facing illustrative icons.

2. Basecoat generic UI glyphs
   - Font Awesome is explicitly prescribed by Basecoat for generic UI/interaction glyphs.
   - appropriate examples include arrows, carets, checks and other application-shell chrome.
   - these glyphs coexist with the Brand Icons library; they do not replace it.

## Selected project rule

For Power Apps:

- Brand-facing/content-facing icons must use the verified NTT DATA Brand Icons library when a matching asset exists.
- Generic application-shell controls such as hamburger/menu, previous/next arrows, back arrows, carets and similar utility controls are generic UI glyphs and therefore follow the Basecoat generic-glyph rule rather than the 418-icon brand-illustration rule.
- Do not assume a Power Apps Fluent icon is automatically equivalent to the NTT/Basecoat glyph. The exact Power Apps rendering/asset mapping must be verified before calling the control brand-final.
- Do not use emoji as UI icons.

## Current cmpAppHeader impact

The current component already contains `btnHeaderBack` with `Icon = "ArrowLeft"` in a Modern Button. This remains the current Power Apps implementation state, but its icon glyph is not yet marked BRAND-FINAL because the current Modern Button icon is Fluent rather than a verified Basecoat/Font Awesome glyph.

Do not redesign or remove the back-event contract. `btnHeaderBack.OnSelect = cmpAppHeader.OnBack()` remains correct and independent of the eventual visual glyph source.

## Hamburger/menu reference

User-supplied NTT DATA navbar screenshots show a hamburger/menu glyph at the far right of the navbar. Project design guidance also records the header hamburger as the trigger that toggles the sidebar/drawer.

The user explicitly confirmed that no hamburger/menu changes have yet been made to `cmpAppHeader`.

Therefore:

- no `ShowMenuButton` property has been added;
- no `OnMenu` event has been added;
- no menu button has been inserted;
- no user-row width change has been made for a menu button.

These remain planned, not implemented.

## Footer previous/next reference

User-supplied reference screenshot shows Previous navigation on the left and Next navigation on the right in a footer/navigation bar.

Selected architecture:

- sequential Previous/Next navigation belongs in a separate reusable page-navigation/footer component, not in `cmpAppHeader`;
- no footer/navigation component has yet been created;
- no Previous/Next properties or events have yet been added.

## Next dependency

Before adding the hamburger or page-navigation component, verify the exact Power Apps-compatible rendering method that best preserves the Basecoat generic glyph appearance while retaining accessibility, theming and reusable-component behavior. Do not substitute a Fluent glyph and call it brand-final without that verification.
