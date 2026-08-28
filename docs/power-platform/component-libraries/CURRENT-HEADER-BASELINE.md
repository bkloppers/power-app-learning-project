# cmpAppHeader — Current Header Baseline

Status: ACTIVE / MIXED EVIDENCE / BRAND-FIRST CORRECTION APPLIED
Baseline: 2026-08-28
Library: `Burts Power App Components`
Environment: `AI King Env`

## Current implemented component state

Custom properties:

- `AppTitle` — Data / Input / Text / default `"Application"`
- `DarkMode` — Data / Input / Boolean / default `true`
- `OnBack` — Event / no parameters
- `ShowBackButton` — Data / Input / Boolean / default `false`
- `UserDisplayName` — Data / Input / Text / default `"User"`
- `UserPhoto` — Data / Input / Image / default `SampleImage`
- `AllowCustomization = false`

Component height:

- `cmpAppHeader.Height = 72`

Implemented tree:

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

## Root header

`conHeaderRootRow` is a horizontal auto-layout container sized to its component parent.

Current configuration includes:

- `Width = Parent.Width`
- `Height = Parent.Height`
- horizontal layout
- vertically centered children
- no shadow
- zero corner radii
- dark/light Fill formula:

```powerfx
If(
    cmpAppHeader.DarkMode,
    RGBA(7, 15, 38, 1),
    Color.White
)
```

## Brand row

Studio screenshot directly proved:

- Flexible width = On
- Fill portions = 1
- Minimum width = 0

Current spacing:

- `LayoutGap = 16`
- `PaddingLeft = 16`
- `PaddingRight = 16`

## Back button — behavior retained, visual implementation superseded

The behavior contract remains correct:

```powerfx
Visible = cmpAppHeader.ShowBackButton
OnSelect = cmpAppHeader.OnBack()
```

The current Modern Button was previously configured with `Icon = "ArrowLeft"`.

That Fluent glyph is now SUPERSEDED / NOT APPROVED. Project rule is brand-correct from first implementation, not temporary Fluent followed by later brand replacement.

Before `btnHeaderBack` is considered complete, its visual glyph must be replaced with the verified Basecoat Icons-module implementation suitable for Power Apps.

## Logo

Current logo formula:

```powerfx
If(
    cmpAppHeader.DarkMode,
    'GlobalLogo_NTTDATA_White_SVG',
    'GlobalLogo_NTTDATA_FutureBlue_SVG'
)
```

Selected current sizing:

- `Width = 140`
- `Height = 38.5`
- `ImagePosition = Fit`
- `AccessibleLabel = "NTT DATA"`
- no border

Brand evidence establishes the 140 px normal digital minimum, horizontal orientation, the approximately 3.64:1 ratio, and the dark/light logo variants.

## Divider

Current divider:

- `Width = 1`
- `Height = 32`
- `FillPortions = 0`
- theme-aware Fill
- rounded 1 px corners
- no shadow

Verified layout correction:

- `Align in container = Center`

This prevents the divider from stretching to the full 72 px header height.

## App title

Current intent:

- compact modifier/application text
- `Text = cmpAppHeader.AppTitle`
- Arial environment-supported substitute
- size 12
- no wrapping
- compact fixed height rather than full header height
- flexible horizontal width
- theme-aware white/Smart-Navy text

The earlier `Font = Font.'Noto Sans'` instruction is superseded because Studio rejected it in this environment.

## User region

Current `conHeaderUserRow`:

- `Width = 56`
- `FillPortions = 0`
- full parent height
- centered children

Current Avatar:

- `avtHeaderUser`
- `Width = 40`
- `Height = 40`
- `Name = cmpAppHeader.UserDisplayName`
- `Image = cmpAppHeader.UserPhoto`

## Brand-first iconography dependency

NTT DATA/Basecoat source ownership:

- brand/content illustrations -> NTT DATA Brand Icons library
- back/previous/next/hamburger and similar UI glyphs -> Basecoat Icons module
- Close/X -> Basecoat Close module

No new menu, footer or close control may be implemented using a temporary Fluent approximation.

Required sequence:

`verify Basecoat glyph/rendering -> implement brand-correct control -> validate in Power Apps`

See `ICONOGRAPHY-DECISION.md` and `ICONOGRAPHY-IMPLEMENTATION-NOTES.md`.
