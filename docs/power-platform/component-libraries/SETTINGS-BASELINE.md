# Component Library Settings Baseline — Burts Power App Components

Status: ACTIVE / SNAPSHOT-VERIFIED
Environment: `AI King Env`
Library: `Burts Power App Components`
Observed: August 2026 session

This file records the Settings state verified from the user's uploaded snapshots while configuring the reusable component library.

## UI-005 — Settings > General: identity and icon

Snapshot directly proves:

- Settings left navigation contains `General`, `Display`, `Updates`, and `Support`.
- Library name is `Burts Power App Components`.
- Description field is currently blank.
- App icon currently uses the `Library` icon.
- Icon background fill is `#fb653c`.
- An `Add image` command is available next to the icon selector.

No change has yet been approved for the name, description, or icon.

## UI-006 — Settings > General: autosave, offline, row limit

Snapshot directly proves:

- `Auto save` is On.
- Studio states autosave saves changes every 2 minutes and is a browser-level setting.
- `Can be used offline` is disabled/unavailable in this library context and shows Off.
- `Data row limit` is set to `500`.
- `Debug published app` is present further down the General settings page.

The row limit is recorded as an observed setting only. It does not define the project's delegation standard.

## UI-007 — Settings > General: debug, environment variables, OnStart

Snapshot directly proves:

- `Debug published app` is Off.
- `Automatically create environment variables when adding data sources` is Off.
- `Enable App.OnStart property` is On.
- Studio displays a caution that App.OnStart can delay app loading and recommends alternatives such as App.StartScreen where appropriate.

Project interpretation:

- Keep `Debug published app` Off for normal work unless a dedicated debugging task requires it.
- Do not automatically enable environment-variable creation merely because the switch exists. This project already uses solution-first ALM with explicitly governed environment variables and connection references.
- App.OnStart being available does not mean it should contain general initialization. Project standard remains minimal App.OnStart, with named formulas/StartScreen used where appropriate.

## UI-008 — Settings > Display: layout and orientation

Snapshot directly proves:

- `App layout` is currently `Fixed`.
- Studio states the fixed layout zooms in and out to fit the screen.
- `Orientation` is `Portrait`.
- `Lock aspect ratio` is On.
- `Lock orientation` is Off.
- The `Show mobile device notifications area` setting is available further down the Display page.

Important project note:

This Settings surface is being observed inside a Component Library. These values are recorded as the library's current editor settings and must not be used as the project-wide Canvas App responsive configuration baseline. The actual consuming Canvas App will use the project's Responsive-first configuration and current Microsoft responsive-layout guidance.

## UI-009 — Settings > Display: mobile notification area

Snapshot directly proves:

- `App layout` remains `Fixed`.
- `Orientation` remains `Portrait`.
- `Lock aspect ratio` remains On.
- `Lock orientation` remains Off.
- `Show mobile device notifications area` is Off.

No change is required to the mobile notification-area setting for the reusable component-library work.

## Current selected baseline for this component library

Keep the observed General/Display settings unchanged unless a later component requirement or current Microsoft guidance requires a specific change.

The only required feature change identified for the current build is:

`Settings -> Updates -> New -> Modern controls and themes -> On`

After that feature is enabled and Studio refreshes, continue the `cmpAppHeader` custom-property contract.
