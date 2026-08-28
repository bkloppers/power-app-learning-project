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

Tree view tabs:
- Screens
- Components

`Components` selected.

Visible command:
- `+ New component`

First reusable component was renamed to `cmpAppHeader`.

### UI-004 — Settings -> Updates baseline before component build

Current Microsoft guidance was verified in August 2026 for enabling supported Modern controls and themes from `Settings -> Updates -> New -> Modern controls and themes`.

Modern control behavior/property names have continued to change during 2026, so exact properties must still be verified against the active Studio version before implementation.

## cmpAppHeader

Purpose: reusable branded application header.

### UI-003 — Enhanced component custom-property dialog

Observed Property type values:
- Data
- Function
- Event
- Action

For value transfer such as `DarkMode`, select Data; direction and data type are configured in the subsequent fields.

### UI-025 — NTT DATA navbar visual reference baseline

Four user-supplied NTT DATA Brand Portal / Basecoat navbar screenshots established the target visual pattern:

- Smart Navy / very dark navy horizontal navbar surface.
- White horizontal NTT DATA logo in dark-header examples.
- Thin vertical divider after the logo when modifier/application text is present.
- Compact modifier text such as `Brand Portal`.
- White utility/navigation glyphs on dark surface.
- Thin Future Blue rule at the bottom edge.
- square/flush shell treatment rather than a rounded floating card.

## Current cmpAppHeader baseline — 2026-08-28

The detailed current state is recorded in `CURRENT-HEADER-BASELINE.md`.

Current implemented tree:

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

Current custom-property contract:

- `AppTitle` — Data / Input / Text
- `DarkMode` — Data / Input / Boolean
- `ShowBackButton` — Data / Input / Boolean
- `OnBack` — Event / no parameters
- `UserDisplayName` — Data / Input / Text
- `UserPhoto` — Data / Input / Image
- `Allow customization` — Off

No hamburger/menu control has been added. No footer/page-navigation component has been created.

### Verified responsive correction — `conHeaderBrandRow`

A Studio screenshot directly proved:

- Flexible width = On
- Fill portions = 1
- Minimum width = 0

This screenshot is authoritative even when exported YAML does not surface `FillPortions` for this container.

### Verified divider correction

`conHeaderDivider` uses `Width = 1` and `Height = 32`.

A Studio screenshot proved that its height still stretched until the child override was changed to:

`Align in container = Center`

This is the correct fix. `LayoutAlignItems` controls children inside the divider and does not control the divider's own alignment inside `conHeaderBrandRow`.

### Logo sizing and clearspace

User-supplied official NTT DATA logo references establish:

- general digital application minimum logo width = 140 px;
- 60 px is a constrained-use exception, not the normal application-header size;
- clearspace = 0.5X left/right and 0.3X above/below;
- horizontal orientation is required for this header;
- white on Smart Navy is preferred for dark presentation;
- Future Blue on white is preferred for light presentation.

Current selected application-header logo sizing:

- Width = 140
- Height = 38.5
- ImagePosition = Fit

`conHeaderBrandRow` spacing uses 16 px to avoid violating the logo clearspace in the current layout.

## Iconography decision

See `ICONOGRAPHY-DECISION.md`.

Brand-source rule from the verified NTT DATA iconography/Basecoat corpus:

- the 418-icon NTT DATA Brand Icons SVG library is the primary source for brand-facing/content-facing illustrative icons;
- Basecoat explicitly prescribes Font Awesome for generic UI/interaction glyphs such as arrows, carets, checks and other shell chrome;
- generic shell controls such as hamburger/menu, back, previous/next and similar navigation glyphs therefore follow the generic-glyph rule rather than the 418-icon illustration rule;
- do not assume a Power Apps Fluent icon is automatically equivalent to the Basecoat glyph;
- no emoji UI icons.

The current `btnHeaderBack.Icon = "ArrowLeft"` is therefore recorded as the current Power Apps implementation, not yet BRAND-FINAL iconography.

## Navbar hamburger and footer navigation references

User-supplied NTT DATA examples show:

- a hamburger/menu glyph at the far right of the navbar;
- Previous navigation on the left side of a footer/navigation bar;
- Next navigation on the right side of that footer/navigation bar.

Selected architecture:

- menu/hamburger trigger belongs in `cmpAppHeader`;
- sequential Previous/Next navigation belongs in a separate reusable page-navigation/footer component;
- the user explicitly confirmed no menu/footer changes have yet been made.

Do not add menu properties/events/controls or footer properties/events until the Power Apps-compatible Basecoat generic-glyph rendering method is verified.

## Reusable-first rules

- Build coherent reusable visual/interaction patterns here rather than duplicating them in individual apps.
- Use explicit component properties as contracts with consuming apps.
- Do not create hidden dependencies on app globals, app collections, app controls or app-specific data sources.
- App-wide nonvisual configuration and reusable named formulas belong in the consuming app's formula layer unless a component-specific contract requires them.
- Use the approved project branding sources; do not invent brand values.
- For new reusable UI, use current supported controls unless brand or capability requirements justify a specific control choice.

## Next verified step

Freeze the current component structure while the Basecoat generic-glyph-to-Power-Apps implementation is verified. Then continue with the hamburger/menu trigger using the verified glyph method; build Previous/Next navigation separately as a reusable footer/page-navigation component.
