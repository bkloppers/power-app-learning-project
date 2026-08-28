# cmpAppHeader — Current Header Baseline

Status: ACTIVE / MIXED EVIDENCE
Baseline: 2026-08-28
Library: `Burts Power App Components`
Environment: `AI King Env`

## Current implemented component state

The latest user-supplied YAML and Studio screenshots establish the following current `cmpAppHeader` state.

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

Verified/current configuration includes:

- `Width = Parent.Width`
- `Height = Parent.Height`
- horizontal layout
- children vertically centered
- no shadow
- all corner radii zero
- dark/light Fill formula:

```powerfx
If(
    cmpAppHeader.DarkMode,
    RGBA(7, 15, 38, 1),
    Color.White
)
```

## Brand row

A Studio screenshot directly proved:

- Flexible width = On
- Fill portions = 1
- Minimum width = 0

This screenshot is authoritative even when exported YAML omits `FillPortions` for `conHeaderBrandRow`.

Current row spacing was subsequently aligned to the NTT DATA logo clearspace rule:

- `LayoutGap = 16`
- `PaddingLeft = 16`
- `PaddingRight = 16`

## Back button

`btnHeaderBack` currently exists with:

```powerfx
Visible = cmpAppHeader.ShowBackButton
OnSelect = cmpAppHeader.OnBack()
```

Current YAML also showed:

- Modern Button
- `Width = 40`
- `Height = 40`
- transparent appearance
- icon-only layout
- `Icon = "ArrowLeft"`
- theme-aware white/Smart-Navy color
- AccessibleLabel `"Back"`
- Tooltip `"Back"`

Because `ShowBackButton` defaults to `false`, screenshots of the component can legitimately show no back button. This is expected behavior, not a layout defect.

Important iconography correction: the `ArrowLeft` Fluent glyph is the current Power Apps implementation state, but is not yet marked BRAND-FINAL. See `ICONOGRAPHY-DECISION.md`.

## Logo

Current logo formula:

```powerfx
If(
    cmpAppHeader.DarkMode,
    'GlobalLogo_NTTDATA_White_SVG',
    'GlobalLogo_NTTDATA_FutureBlue_SVG'
)
```

Brand reference evidence supplied by the user establishes:

- general digital application minimum logo width = 140 px;
- 60 px exception applies only to space-constrained cases such as mobile ad units;
- minimum clearspace = 0.5X left/right and 0.3X above/below;
- horizontal logo is required for this header;
- white logo on Smart Navy is preferred for dark presentation;
- Future Blue logo on white is preferred for light presentation.

Selected current application-header logo sizing:

- `Width = 140`
- `Height = 38.5`
- `ImagePosition = Fit`
- no border
- AccessibleLabel `"NTT DATA"`

The approximately 38.5 px height preserves the verified ~3.64:1 logo aspect ratio.

## Divider

Current `conHeaderDivider` YAML:

```yaml
Control: GroupContainer@1.5.0
Variant: AutoLayout
Properties:
  DropShadow: =DropShadow.None
  Fill: |-
    =If(
        cmpAppHeader.DarkMode,
        RGBA(255, 255, 255, 0.75),
        RGBA(7, 15, 38, 0.75)
    )
  FillPortions: =0
  Height: =32
  LayoutAlignItems: =LayoutAlignItems.Center
  LayoutDirection: =LayoutDirection.Horizontal
  LayoutMinHeight: =32
  LayoutMinWidth: =1
  RadiusBottomLeft: =1
  RadiusBottomRight: =1
  RadiusTopLeft: =1
  RadiusTopRight: =1
  Width: =1
```

A Studio screenshot proved that setting `Height = 32` alone was not enough: the divider still visually stretched to the full row height because its child alignment inherited Stretch from the parent layout.

Verified fix:

- `conHeaderDivider -> Align in container = Center`

After that change, the divider rendered as intended: 1 px wide, 32 px high, vertically centered in the 72 px header.

This is a superseding correction. `LayoutAlignItems` on the divider controls its own children and does not control how the divider itself is positioned inside `conHeaderBrandRow`.

## App title

Current selected title intent:

- compact modifier/application text, not a large heading;
- `Text = cmpAppHeader.AppTitle`
- Arial is the current environment-supported substitution because Noto Sans is not available as a valid Power Apps Font enum in this environment;
- size 12;
- no wrapping;
- fixed compact height rather than filling the 72 px header;
- flexible horizontal width within the brand row;
- theme-aware white/Smart-Navy text.

The earlier instruction `Font = Font.'Noto Sans'` is superseded because Studio rejected it in this environment.

## User region

Current `conHeaderUserRow` is a fixed-width right-side horizontal container:

- `Width = 56`
- `FillPortions = 0`
- full parent height
- children centered horizontally and vertically

Current Avatar:

- `avtHeaderUser`
- `Width = 40`
- `Height = 40`
- `Name = cmpAppHeader.UserDisplayName`
- `Image = cmpAppHeader.UserPhoto`

## NTT navbar and footer references

User-supplied NTT DATA examples show:

- hamburger/menu glyph at the far right of the navbar;
- Previous navigation on the left of a footer/navigation bar;
- Next navigation on the right of that footer/navigation bar.

Selected architecture, not yet implemented:

- hamburger/menu trigger belongs to `cmpAppHeader`;
- sequential Previous/Next navigation belongs to a separate reusable page-navigation/footer component;
- no menu properties/events/controls have been added yet;
- no footer component has been created yet.

## Next dependency

Before adding any new menu or footer controls, complete the Basecoat iconography-to-Power-Apps mapping recorded in `ICONOGRAPHY-DECISION.md`. Do not silently use Fluent glyphs and call them NTT/Basecoat brand-final.
