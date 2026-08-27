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

Observed in Power Apps Studio with `cmpAppHeader` selected.

### Snapshot directly proves

- `DarkMode` remains present as a Boolean custom property.
- `AppTitle` exists as a second custom property.
- The `AppTitle` property editor shows:
  - Display name: `AppTitle`
  - Name: `AppTitle`
  - Description: `Displays the application title in the header.`
  - Property type: `Data`
  - Property definition: `Input`
  - Data type: `Text`
- `Raise OnReset when value changes` is unchecked.
- The formula bar shows the default formula/value `"Application"`.
- The component Properties pane shows `Allow customization` is currently On.

### Microsoft-verified interpretation

`AppTitle` is correctly modeled as a Data / Input / Text property because the consuming app supplies the displayed application title to the reusable component.

Component-library guidance states that when `Allow customization` is On, a consuming app can edit the imported component, which creates a local copy and removes its association with the component library. Turning `Allow customization` Off prevents that local-edit path and keeps maintenance centralized in the component library.

### Validation/result

`AppTitle` contract is complete.

### Selected governance setting

For this centrally managed reusable component, set `Allow customization` to Off before adding further contract properties or child controls.

### Next verified step

Turn `cmpAppHeader` -> `Allow customization` Off and verify the component remains selected with the custom properties intact.
