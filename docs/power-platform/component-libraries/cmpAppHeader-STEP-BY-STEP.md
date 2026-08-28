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

This spacing was selected after the official logo clearspace reference was supplied.

## Back button

Latest YAML confirms `btnHeaderBack`:

```powerfx
Visible = cmpAppHeader.ShowBackButton
OnSelect = cmpAppHeader.OnBack()
```

and:

- `Width = 40`
- `Height = 40`
- transparent appearance
- icon-only layout
- AccessibleLabel `"Back"`
- Tooltip `"Back"`
- current icon string `"ArrowLeft"`

Because `ShowBackButton` defaults to false, the button is intentionally absent from normal component screenshots until the property is set true.

### Iconography correction

The current `"ArrowLeft"` icon is a Power Apps Fluent glyph and is not yet marked BRAND-FINAL.

Verified NTT DATA project iconography guidance distinguishes:

- brand-facing/content-facing icons -> NTT DATA Brand Icons SVG library;
- generic UI/interaction glyphs -> Basecoat-prescribed Font Awesome glyphs.

Back, hamburger/menu, previous and next are generic shell/navigation glyphs. See `ICONOGRAPHY-DECISION.md`.

## Logo

Correct media names omit file extensions in the Power Apps formula.

```powerfx
If(
    cmpAppHeader.DarkMode,
    'GlobalLogo_NTTDATA_White_SVG',
    'GlobalLogo_NTTDATA_FutureBlue_SVG'
)
```

The earlier formula using media filenames with `.svg` was incorrect and is superseded.

Official NTT DATA references supplied by the user establish:

- digital application minimum = 140 px wide;
- 60 px only for constrained cases such as mobile ad units;
- clearspace = 0.5X left/right and 0.3X above/below;
- horizontal logo required in this header;
- white on Smart Navy for dark presentation;
- Future Blue on white for light presentation.

Current selected logo:

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

Fill:

```powerfx
If(
    cmpAppHeader.DarkMode,
    RGBA(255, 255, 255, 0.75),
    RGBA(7, 15, 38, 0.75)
)
```

### Verified stretch correction

A Studio screenshot showed the divider still filling the 72 px header despite `Height = 32`.

Cause: the divider itself inherited cross-axis Stretch from its parent layout.

Verified fix:

`conHeaderDivider -> Align in container = Center`

After this change the divider rendered 1 px by 32 px, vertically centered.

Do not confuse this with `LayoutAlignItems`: that property controls children inside the divider container, not the divider's position inside its parent.

## App title

The NTT navbar reference establishes compact modifier text rather than a large page-heading treatment.

Current selected title intent:

```powerfx
Text = cmpAppHeader.AppTitle
Font = Font.Arial
Size = 12
Height = 24
Wrap = false
VerticalAlign = VerticalAlign.Middle
```

Arial is the environment-supported substitution. The earlier `Font.'Noto Sans'` instruction is superseded because Power Apps Studio rejected it in this environment.

Title color should follow dark/light presentation.

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

User explicitly confirmed no changes were made after this design discussion.

Therefore current truth is:

- no `ShowMenuButton` property;
- no `OnMenu` event;
- no menu button;
- no change to `conHeaderUserRow` for a menu button;
- no footer/page-navigation component;
- no Previous/Next events or inputs.

Selected architecture for later implementation:

- hamburger/menu trigger belongs to `cmpAppHeader`;
- sequential Previous/Next belongs to a separate reusable page-navigation/footer component.

## Next verified step

Do not alter the component for menu/footer yet. First verify the Power Apps-compatible rendering method for the Basecoat-prescribed generic UI glyphs. Then implement the hamburger in the header and Previous/Next in a separate reusable footer/page-navigation component using that verified glyph method.
