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

The current web environment could not retrieve the module, so exact shell CSS is not yet available. Current shell-level values remain implementation state, not brand-final values, including header height, shell padding/gaps, accent-border treatment, utility placement, and responsive hamburger placement.

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

These responsive mechanics remain valid, but exact branded spacing is pending Site Header/Logos module verification.

## Back button — behavior retained, visual implementation superseded

Behavior contract:

```powerfx
Visible = cmpAppHeader.ShowBackButton
OnSelect = cmpAppHeader.OnBack()
```

Current implementation had:

- `Width = 40`
- `Height = 40`
- Modern Button
- `Icon = "ArrowLeft"`

The Fluent glyph is SUPERSEDED / NOT APPROVED.

UI-029 and UI-030 now also supersede the 40 x 40 shell-icon sizing. Brand-source evidence establishes a maximum toolbar/utility glyph size of `24 x 24 px` and general clearspace of 50% of icon height. Therefore the selected header-utility baseline is:

- glyph maximum: `24 x 24 px`;
- clearspace: `12 px` around a 24 px glyph;
- nominal interactive/control footprint: `48 x 48 px`;
- exact glyph source: Basecoat Icons module;
- final header placement: Site Header module.

No Power Apps control change has yet been made from this correction.

## Logo + divider + application heading lockup

The user supplied the Basecoat Logos module as the authoritative source for this complete lockup:

- `https://basecoat.nttdata.com/css-modules/logos.html`
- `https://basecoat.nttdata.com/5/css/module.logos.min.css`

Therefore `imgHeaderLogo`, `conHeaderDivider`, and `lblHeaderAppTitle` are treated as one branded pattern rather than independently tuned controls.

### Logo — current implementation state

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

### Divider — current implementation state

- `Width = 1`
- `Height = 32`
- `FillPortions = 0`
- theme-aware Fill
- `Align in container = Center`

Center alignment is a verified Power Apps layout correction. Exact brand dimensions/color/spacing remain Logos-module dependent.

### App title — current implementation state

- `Text = cmpAppHeader.AppTitle`
- `Font = Font.Arial`
- `Size = 12`
- `Height = 24`
- `Wrap = false`
- `VerticalAlign = VerticalAlign.Middle`

Exact branded typography/spacing remains Logos-module dependent.

## User region

Current `conHeaderUserRow`:

- `Width = 56`
- `FillPortions = 0`
- full parent height
- centered child

Current Avatar:

- `avtHeaderUser`
- `Width = 40`
- `Height = 40`
- `Name = cmpAppHeader.UserDisplayName`
- `Image = cmpAppHeader.UserPhoto`

Utility-region sizing and spacing are not brand-final until Site Header module verification.

## UI-028 — Main navigation icon sizing

User-supplied Brand Portal screenshot establishes:

- maximum main-navigation icon container `30 x 30 px`;
- `15 px` additional clearspace around the icon;
- one-word label accompanies the main-navigation icon;
- main-navigation icons are discarded at mobile breakpoints.

This is a main-navigation pattern, not automatically the rule for header utility controls.

## UI-029 — Toolbar icon sizing

User-supplied Brand Portal screenshot establishes:

- toolbar/utility icon maximum `24 x 24 px`;
- icon vertically aligns with its accompanying label;
- `10 px` spacing before accompanying text.

## UI-030 — General icon clearspace

User-supplied Brand Portal screenshot establishes:

- clearspace should be 50% of icon height;
- explicit example: 24 px icon -> 12 px clearspace;
- icon generally should not exceed related content font size, except main navigation or special contextual use.

For header utility glyphs, this yields the selected nominal 48 x 48 control/touch footprint around a maximum 24 x 24 glyph, subject to a more-specific Site Header rule if one is later verified.

Full evidence record: `ICON-SIZING-EVIDENCE.md`.

## Brand-first source hierarchy

1. Basecoat Site Header module -> overall header shell.
2. Basecoat Logos module -> logo/divider/application heading lockup.
3. Basecoat Icons module -> back/hamburger/previous/next and generic UI glyphs.
4. Basecoat Close module -> dedicated Close/X control.
5. NTT DATA Brand Icons library -> content-facing illustrative icons.
6. User-supplied icon sizing screenshots -> main-navigation, toolbar and clearspace sizing constraints.

No shell visual is considered complete when its authoritative brand source has not yet been implemented and validated.
