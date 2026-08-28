# cmpAppHeader — Step-by-Step Build Record

Status: ACTIVE
Library: `Burts Power App Components`
Environment: `AI King Env`

This file records the verified build sequence and corrections for the reusable `cmpAppHeader` component.

## UI-021 — `DarkMode` custom property completed

Verified custom property:

- Display name: `DarkMode`
- Name: `DarkMode`
- Description: `Controls light/dark presentation of the header.`
- Property type: Data
- Property definition: Input
- Data type: Boolean
- default: `true`

## UI-022 — `AppTitle` custom property completed

Verified custom property:

- Display name: `AppTitle`
- Name: `AppTitle`
- Description: `Displays the application title in the header.`
- Property type: Data
- Property definition: Input
- Data type: Text
- default: `"Application"`

## User-confirmed state — Allow customization disabled

`cmpAppHeader -> Allow customization = Off`.

## User-confirmed state — `ShowBackButton`

- Data / Input / Boolean
- default `false`
- Description: `Controls whether the back button is shown in the header.`

## User-confirmed state — `OnBack`

- Event
- no parameters
- Description: `Runs the behavior supplied by the hosting app when the back button is selected.`

The component does not contain app-specific `Back()` or `Navigate()` behavior. Internal control behavior calls `cmpAppHeader.OnBack()` and the consuming app supplies the navigation behavior.

## Current additional inputs

Latest user-supplied YAML confirms:

- `UserDisplayName` — Data / Input / Text / default `"User"`
- `UserPhoto` — Data / Input / Image / default `SampleImage`

## Current component size

- `Height = 72`

## Current implemented tree

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

No hamburger/menu control has been added yet. No footer/page-navigation component has been created.

## Root row

`conHeaderRootRow`:

```powerfx
Width = Parent.Width
Height = Parent.Height
```

Dark/light fill:

```powerfx
If(
    cmpAppHeader.DarkMode,
    RGBA(7, 15, 38, 1),
    Color.White
)
```

Root layout is horizontal, children vertically centered, with no drop shadow and zero radii.

## Brand row responsive state

A Studio screenshot directly verifies:

- Flexible width = On
- Fill portions = 1
- Minimum width = 0

Do not infer from exported YAML that Fill portions is missing when Studio directly proves it is enabled.

Current selected spacing:

- `LayoutGap = 16`
- `PaddingLeft = 16`
- `PaddingRight = 16`

Exact brand spacing remains pending Site Header and Logos-module verification.

## Back button

Latest YAML confirms behavior:

```powerfx
Visible = cmpAppHeader.ShowBackButton
OnSelect = cmpAppHeader.OnBack()
```

Current implementation state previously used:

- `Width = 40`
- `Height = 40`
- transparent Modern Button
- icon-only layout
- current icon string `"ArrowLeft"`
- AccessibleLabel `"Back"`
- Tooltip `"Back"`

Because `ShowBackButton` defaults to false, the button is intentionally absent from normal component screenshots until the property is set true.

### Brand-first correction

The Fluent `"ArrowLeft"` glyph is SUPERSEDED / NOT APPROVED. Back must use the verified Basecoat Icons-module glyph from the first completed implementation.

UI-029 and UI-030 further supersede the 40 x 40 shell-icon sizing:

- toolbar/utility glyph maximum = `24 x 24 px`;
- general clearspace = 50% of glyph height;
- 24 px glyph -> 12 px clearspace;
- nominal interactive/control footprint = `48 x 48 px`.

No Power Apps change has yet been made from this sizing correction.

## Logo

Correct media names omit file extensions in the Power Apps formula.

```powerfx
If(
    cmpAppHeader.DarkMode,
    'GlobalLogo_NTTDATA_White_SVG',
    'GlobalLogo_NTTDATA_FutureBlue_SVG'
)
```

Official NTT DATA references supplied by the user establish:

- digital application minimum = 140 px wide;
- 60 px only for constrained cases such as mobile ad units;
- clearspace = 0.5X left/right and 0.3X above/below;
- horizontal logo required in this header;
- white on Smart Navy for dark presentation;
- Future Blue on white for light presentation.

Current implementation:

```powerfx
Width = 140
Height = 38.5
ImagePosition = ImagePosition.Fit
AccessibleLabel = "NTT DATA"
```

## Divider

Current `conHeaderDivider` uses:

```powerfx
Width = 1
Height = 32
FillPortions = 0
LayoutMinWidth = 1
LayoutMinHeight = 32
```

Verified fix:

`conHeaderDivider -> Align in container = Center`

This prevents auto-layout stretch. Exact branded divider dimensions/color/spacing are governed by the Basecoat Logos module and are not final until that module is verified.

## App title

Current implementation intent:

```powerfx
Text = cmpAppHeader.AppTitle
Font = Font.Arial
Size = 12
Height = 24
Wrap = false
VerticalAlign = VerticalAlign.Middle
```

Exact branded heading typography/spacing is governed by the Logos module.

## User region

`conHeaderUserRow` current state:

- fixed `Width = 56`
- `FillPortions = 0`
- full header height
- child centered horizontally and vertically

`avtHeaderUser`:

```powerfx
Width = 40
Height = 40
Name = cmpAppHeader.UserDisplayName
Image = cmpAppHeader.UserPhoto
```

## NTT hamburger and footer references — NOT IMPLEMENTED

User-supplied NTT DATA examples show:

- hamburger/menu glyph at far right of navbar;
- Previous action on left side of footer/navigation bar;
- Next action on right side of footer/navigation bar.

Current truth:

- no `ShowMenuButton` property;
- no `OnMenu` event;
- no menu button;
- no change to `conHeaderUserRow` for a menu button;
- no footer/page-navigation component;
- no Previous/Next events or inputs.

Selected architecture:

- hamburger/menu trigger belongs to `cmpAppHeader`;
- sequential Previous/Next belongs to a separate reusable page-navigation/footer component.

## UI-028 — Main navigation icons

User-supplied NTT DATA Brand Portal screenshot establishes:

- main-navigation icons fit within `30 x 30 px`;
- neither dimension should exceed the 30 px container;
- additional clearspace = `15 px` around the icon;
- a one-word label accompanies the main-navigation icon;
- main-navigation icons are discarded at mobile breakpoints.

This rule is for the main-navigation pattern and is not automatically applied to header utility controls.

## UI-029 — Toolbar icons

User-supplied NTT DATA Brand Portal screenshot establishes:

- tool/utility-bar icon maximum = `24 x 24 px`;
- icon and accompanying label are vertically aligned;
- `10 px` space before accompanying text.

Back and hamburger/menu are treated as header utility controls unless the Site Header module proves a more specific rule.

## UI-030 — General icon size and clearspace

User-supplied NTT DATA Brand Portal screenshot establishes:

- clearspace = 50% of icon height;
- explicit example: 24 px icon -> 12 px clearspace;
- icon generally should not exceed related-content font size, except main navigation or special contextual use.

Selected header-utility baseline:

```text
Glyph maximum: 24 x 24 px
Clearspace: 12 px around glyph
Nominal control/touch footprint: 48 x 48 px
```

Full evidence record: `ICON-SIZING-EVIDENCE.md`.

## Next verified step

Correct `btnHeaderBack` before adding any new shell icon: replace the Fluent visual with the verified Basecoat Icons-module glyph and size the utility control to the 24 px glyph / nominal 48 px footprint rule, while preserving `Visible = cmpAppHeader.ShowBackButton` and `OnSelect = cmpAppHeader.OnBack()`. Final placement remains subject to the Site Header module.
