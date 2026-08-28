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

## Site Header module authority

The user supplied the authoritative Basecoat Site Header module sources:

- `https://basecoat.nttdata.com/css-modules/site-header.html`
- `https://basecoat.nttdata.com/5/css/module.site-header.min.css`

This establishes `site-header` as the governing module for the overall application-header shell. See `SITE-HEADER-MODULE-SOURCE.md`.

The current web environment could not retrieve the module, so the exact shell CSS is not yet available. Therefore current shell-level values are implementation state, not brand-final values, including:

- `cmpAppHeader.Height = 72`;
- root/brand-row padding;
- horizontal gaps;
- background/border treatment;
- bottom Future Blue rule implementation;
- utility region placement;
- mobile/tablet hamburger placement and visibility behavior.

Do not tune those values further by eye. Verify the Site Header module first.

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

These layout mechanics remain valid responsive behavior, but the exact branded spacing values are pending Site Header/Logos module verification.

## Back button — behavior retained, visual implementation superseded

The behavior contract remains correct:

```powerfx
Visible = cmpAppHeader.ShowBackButton
OnSelect = cmpAppHeader.OnBack()
```

The current Modern Button was previously configured with `Icon = "ArrowLeft"`.

That Fluent glyph is SUPERSEDED / NOT APPROVED. Before `btnHeaderBack` is considered complete, its visual glyph must use the verified Basecoat Icons-module implementation suitable for Power Apps.

## Logo + divider + application heading lockup

The user supplied the Basecoat Logos module as the authoritative source for this complete lockup:

- `https://basecoat.nttdata.com/css-modules/logos.html`
- `https://basecoat.nttdata.com/5/css/module.logos.min.css`

Therefore `imgHeaderLogo`, `conHeaderDivider`, and `lblHeaderAppTitle` must be treated as one branded pattern rather than independently tuned controls.

Current values remain recorded implementation state but are not brand-final until checked against the Logos module.

### Logo

Current formula:

```powerfx
If(
    cmpAppHeader.DarkMode,
    'GlobalLogo_NTTDATA_White_SVG',
    'GlobalLogo_NTTDATA_FutureBlue_SVG'
)
```

Current sizing:

- `Width = 140`
- `Height = 38.5`
- `ImagePosition = Fit`
- `AccessibleLabel = "NTT DATA"`
- no border

### Divider

Current divider:

- `Width = 1`
- `Height = 32`
- `FillPortions = 0`
- theme-aware Fill
- rounded 1 px corners
- no shadow
- `Align in container = Center`

The center alignment is a verified Power Apps layout fix preventing stretch. The exact branded divider height/thickness/color/spacing remains pending Logos-module verification.

### App title

Current intent/state:

- `Text = cmpAppHeader.AppTitle`
- Arial environment-supported substitute
- size 12
- no wrapping
- compact fixed height
- flexible horizontal width
- theme-aware white/Smart-Navy text

The earlier `Font = Font.'Noto Sans'` instruction is superseded because Studio rejected it in this environment. Exact branded typography and spacing remain pending Logos-module verification.

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

Utility-region sizing/spacing is not brand-final until Site Header module verification.

## Brand-first source hierarchy

For this shell:

1. Basecoat Site Header module -> overall header shell.
2. Basecoat Logos module -> logo/divider/application heading lockup.
3. Basecoat Icons module -> back/hamburger/previous/next and generic UI glyphs.
4. Basecoat Close module -> dedicated Close/X control.
5. NTT DATA Brand Icons library -> content-facing illustrative icons.

No shell visual is considered final when its authoritative Basecoat module has not yet been verified.
