# cmpAppHeader — Step-by-Step Build Record

Status: ACTIVE / SNAPSHOT-VERIFIED
Library: `Burts Power App Components`
Environment: `AI King Env`

This file records the verified build of the reusable `cmpAppHeader` component.

## UI-021 — `DarkMode` custom property completed

Observed in Power Apps Studio after the supported modern-controls refresh.

### Snapshot directly proves

- `cmpAppHeader` is selected in the Component Library.
- Custom property `DarkMode` exists in the Properties pane.
- The custom-property editor shows:
  - Display name: `DarkMode`
  - Name: `DarkMode`
  - Description: `Controls light/dark presentation of the header.`
  - Property type: `Data`
  - Property definition: `Input`
  - Data type: `Boolean`
- `Raise OnReset when value changes` is unchecked.
- The formula bar is displaying the `DarkMode` property with formula/default value `true`.

### Microsoft-verified interpretation

A Data property configured as Input is the supported mechanism for the hosting app to provide a value to a canvas component. `DarkMode` is therefore correctly modeled as an app-to-component Boolean input.

The `Raise OnReset when value changes` option causes a change to the input property to trigger the component's OnReset behavior. `DarkMode` is a presentation input and does not require reset behavior, so this option remains unchecked.

### Validation/result

`DarkMode` contract is complete and ready for use by the component's internal formulas.

## UI-022 — `AppTitle` custom property completed

Snapshot directly proves:

- `AppTitle` exists in the component's Custom properties list.
- Display name: `AppTitle`.
- Name: `AppTitle`.
- Description: `Displays the application title in the header.`
- Property type: `Data`.
- Property definition: `Input`.
- Data type: `Text`.
- `Raise OnReset when value changes` is unchecked.
- Default formula is `"Application"`.
- The component-level `Allow customization` switch was visible as On at the time of the snapshot.

### Validation/result

`AppTitle` contract is complete and ready for use by the component's internal controls.

## User-confirmed state — Allow customization disabled

After UI-022, the user disabled `cmpAppHeader -> Allow customization` and confirmed completion without another screenshot.

Record type: USER-CONFIRMED / NOT SNAPSHOT-VERIFIED.

Selected project state:

- `Allow customization = Off`.
- The reusable header remains centrally maintained by the component library.

## User-confirmed state — `ShowBackButton` completed

The user created and confirmed the following property without another screenshot:

- Display name: `ShowBackButton`.
- Name: `ShowBackButton`.
- Description: `Controls whether the back button is shown in the header.`
- Property type: `Data`.
- Property definition: `Input`.
- Data type: `Boolean`.
- `Raise OnReset when value changes`: unchecked.
- Default formula: `false`.

Record type: USER-CONFIRMED / NOT SNAPSHOT-VERIFIED.

### Validation/result

The header now has the initial presentation contract needed for title, dark-mode state, and optional back-button visibility.

### Next verified step

Create an `OnBack` Event property so the consuming app supplies the behavior that should run when the header's back button is selected. This keeps navigation logic outside the reusable component and avoids app-specific navigation dependencies inside the library.