# Component Libraries — Step-by-Step Guide

Status: ACTIVE
Library: `Burts Power App Components`
Environment: `AI King Env`

## Purpose

Canonical record for reusable Power Apps component-library work.

## Verified creation route

### UI-001 — Solution menu disproved old creation path

Observed in `GCC AI Champions` -> Objects -> New -> App.

Visible App submenu:
- Canvas app
- Model-driven app
- Page

`Component library` was not present. Therefore do not use `Solution -> New -> App -> Component library` in this tenant/UI.

Working project route: create/open the Component Library from the main Power Apps Component Libraries experience, then add it to the governed solution using the supported Add existing flow when required for ALM.

## Component Library Studio

### UI-002 — Components tree and first component

Observed in `Burts Power App Components`.

First reusable component was renamed to `cmpAppHeader`.

### UI-004 — Settings -> Updates baseline before component build

Current Microsoft guidance was verified in August 2026 for enabling supported Modern controls and themes from `Settings -> Updates -> New -> Modern controls and themes`.

Modern control behavior/property names continue to require verification against the active Studio version before implementation.

## cmpAppHeader

Purpose: reusable branded application header.

### UI-025 — NTT DATA navbar visual reference baseline

User-supplied NTT DATA Brand Portal / Basecoat navbar screenshots established:

- Smart Navy / very dark navy horizontal navbar surface.
- White horizontal NTT DATA logo in dark-header examples.
- Thin vertical divider after the logo when modifier/application text is present.
- Compact modifier text such as `Brand Portal`.
- White utility/navigation glyphs on dark surface.
- Thin Future Blue rule at the bottom edge.
- square/flush shell treatment rather than a rounded floating card.

## Current cmpAppHeader baseline — 2026-08-28

See `CURRENT-HEADER-BASELINE.md` for the detailed state.

Current tree:

```text
cmpAppHeader
└── conHeaderRootRow
    ├── conHeaderBrandRow
    │   ├── btnHeaderBack
    │   ├── imgHeaderLogo
    │   ├── conHeaderDivider
    │   └── lblHeaderAppTitle
    └── conHeaderUserRow
        └── avtHeaderUser
```

No hamburger/menu control has been added. No footer/page-navigation component has been created.

## Basecoat header source hierarchy

Authoritative module ownership for the header is now:

1. `site-header` — overall header shell structure, spacing, presentation and header behavior. See `SITE-HEADER-MODULE-SOURCE.md`.
2. `logos` — NTT DATA logo + divider + modifier/application heading lockup. See `LOGOS-MODULE-SOURCE.md`.
3. `icons` — back, previous, next, hamburger/menu and similar generic UI glyphs.
4. `close` — dedicated Close/X control.
5. NTT DATA Brand Icons library — brand/content illustrative icons.

The current header shell dimensions, padding, spacing, accent-border treatment and utility placement are not considered brand-final until checked against the Site Header module. The logo-divider-heading values are not considered brand-final until checked against the Logos module.

## Brand-first iconography rule

See:

- `ICONOGRAPHY-DECISION.md`
- `ICONOGRAPHY-IMPLEMENTATION-NOTES.md`
- `ICONOGRAPHY-MODULE-SOURCES.md`
- `ICONOGRAPHY-SOURCE-INDEX.md`

Selected project rule:

- NTT DATA Brand Icons library is the source for brand/content illustrative icons.
- Basecoat Icons module is the source for back, previous, next, hamburger/menu and similar UI glyphs.
- Basecoat Close module is the dedicated source for Close/X.
- Power Apps Fluent icons are not accepted as temporary placeholders for controls that are intended to be branded.
- Brand is implemented from the first working version.
- If the Basecoat glyph/rendering is not yet verified for Power Apps, stop and resolve that dependency before inserting the control.
- No emoji UI icons.

### Superseded back-button visual implementation

`btnHeaderBack.OnSelect = cmpAppHeader.OnBack()` remains correct.

The earlier visual configuration `Icon = "ArrowLeft"` is SUPERSEDED / NOT APPROVED because it is a Fluent approximation and violates the brand-first rule.

The back control is not complete until its Basecoat Icons-module glyph is implemented and validated in Power Apps.

## Navbar hamburger and footer navigation references

User-supplied NTT DATA examples show:

- a hamburger/menu glyph at the far right of the navbar;
- Previous navigation on the left side of a footer/navigation bar;
- Next navigation on the right side of that footer/navigation bar.

Selected architecture:

- menu/hamburger trigger belongs in `cmpAppHeader`;
- sequential Previous/Next navigation belongs in a separate reusable page-navigation/footer component;
- no menu/footer changes have yet been made.

Those controls must be implemented brand-correct from the start using the verified Basecoat module approach.

## Reusable-first rules

- Build coherent reusable visual/interaction patterns here rather than duplicating them in individual apps.
- Use explicit component properties as contracts with consuming apps.
- Do not create hidden dependencies on app globals, app collections, app controls or app-specific data sources.
- Use approved project branding sources; do not invent brand values or approximate glyphs.

## Next verified step

Resolve the exact Basecoat Site Header and Logos-module rules before further visual tuning of `cmpAppHeader`. Then translate those verified rules to the current responsive Power Apps structure. Do not add the hamburger or finalize the back glyph until their Basecoat Icons-module rendering is also verified.
