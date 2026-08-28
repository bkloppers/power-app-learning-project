# cmpAppHeader — OnBack Event Record

Status: USER-CONFIRMED
Library: `Burts Power App Components`
Environment: `AI King Env`

The user confirmed completion of the following custom property without a new screenshot:

- Display name: `OnBack`
- Name: `OnBack`
- Description: `Runs the behavior supplied by the hosting app when the back button is selected.`
- Property type: `Event`
- Parameters: none

Record type: USER-CONFIRMED / NOT SNAPSHOT-VERIFIED.

## Design intent

The reusable component does not contain app-specific `Back()` or `Navigate()` logic. The hosting app supplies the navigation behavior through the `OnBack` Event contract.

## Current cmpAppHeader contract

- `DarkMode` — Data / Input / Boolean
- `AppTitle` — Data / Input / Text
- `ShowBackButton` — Data / Input / Boolean
- `OnBack` — Event / no parameters
- `Allow customization` — Off

## Next build step

Insert the first structural control for the header only after verifying the exact current Insert experience and control availability in the active authoring version.
