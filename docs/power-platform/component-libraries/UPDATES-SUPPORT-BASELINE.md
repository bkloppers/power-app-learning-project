# Component Library Updates and Support Baseline — Burts Power App Components

Status: ACTIVE / SNAPSHOT-VERIFIED
Environment: `AI King Env`
Library: `Burts Power App Components`
Observed: August 2026 session
Authoring version observed in Studio: `3.26083.5`

This file records the Updates and Support surfaces verified from the user's uploaded snapshots. It records observed state; it does not imply that every enabled Preview/Experimental feature is approved for production use.

Sensitive session, tenant, app, object, and correlation identifiers shown in Support/session details are intentionally not persisted in this knowledge base.

## UI-010 — Updates > New: top section

Exact path:

`Settings -> Updates -> New`

Snapshot directly proves:

- `Coauthoring` is Off.
- `Modern controls and themes` is Off.
- `New analysis engine and User defined functions` is visible below and its state is captured in UI-011.

Microsoft-verified guidance applicable in August 2026 states that the supported modern control/theme enablement path is `Settings -> Updates -> New -> Modern controls and themes -> On`.

## UI-011 — Updates > New: analysis engine, SaveData media, SharePoint

Snapshot directly proves:

- `New analysis engine and User defined functions` is On.
- `Expanded media support for SaveData on Power Apps mobile apps` is On.
- `Explicit column selection for SharePoint online` is On.
- `Enable delegation for UpdateIf and RemoveIf` is visible below and its state is captured in UI-012.

Current Microsoft guidance confirms enhanced `UpdateIf` / `RemoveIf` behavior is enabled by default for new apps, although the functions still do not become fully server-delegated; the feature simulates broader delegation by retrieving/evaluating additional records and remains subject to documented limits.

## UI-012 — Updates > New: delegation, StartScreen defer loading, enhanced component properties

Snapshot directly proves:

- `Enable delegation for UpdateIf and RemoveIf` is On.
- `Enable defer loading unused screens with App.StartScreen` is On.
- `Enhanced component properties` is On.
- `User-defined types` is visible below, but the snapshot does not prove its toggle state.

Project interpretation:

- Keep `Enable delegation for UpdateIf and RemoveIf` On.
- Keep `Enable defer loading unused screens with App.StartScreen` On.
- `Enhanced component properties` being On explains the current custom-property UI with Data / Function / Event / Action. This observed availability does not by itself mean every enhanced behavior/event pattern is approved for production; each use must still be checked against current Microsoft support status before implementation.

## UI-013 — Updates > Preview: top section

Exact path:

`Settings -> Updates -> Preview`

Snapshot directly proves:

- Preview features are explicitly described by Studio as subject to change.
- `Keep recently visited screens in memory` is Off.
- `Edit in Copilot Studio` is On.
- `Optimize for devices` is Off.

No Preview feature is being changed for the current component-library build.

## UI-014 — Updates > Preview: lower section

Snapshot directly proves:

- `Keep recently visited screens in memory` remains Off.
- `Edit in Copilot Studio` remains On.
- `Optimize for devices` remains Off.
- `Proactive control rename` is On.

No Preview feature is required for `cmpAppHeader`.

## UI-015 — Updates > Experimental: top section

Exact path:

`Settings -> Updates -> Experimental`

Snapshot directly proves:

- Studio explicitly warns that Experimental features may change, break, or be removed and should not be used in production apps.
- `Optimize embedding appearance` is Off.
- `Pass errors to Azure Application Insights` is Off.
- `Enable Azure Application Insights correlation tracing` is visible below; its state is captured in UI-016.

Project rule: do not enable Experimental features merely because they exist. Production implementation must avoid depending on Experimental capabilities unless the user explicitly changes the project standard after review.

## UI-016 — Updates > Experimental: modern controls legacy/experimental toggle

Snapshot directly proves:

- `Enable Azure Application Insights correlation tracing` is Off.
- `Web barcode scanner` is Off.
- `Record scope one-to-many and many-to-many relationships` is Off.
- `Modern controls` is On.
- `Improved canvas keyboard navigation` is visible below.

Important distinction:

`Experimental -> Modern controls = On` is **not** the same setting as `New -> Modern controls and themes = Off`.

The current supported Microsoft enablement path for the modern controls/themes experience is the **New** tab switch. Therefore this project will enable `New -> Modern controls and themes` and will not treat the Experimental `Modern controls` toggle as a substitute.

## UI-017 — Updates > Experimental: keyboard navigation, PDF, email validation

Snapshot directly proves:

- `Improved canvas keyboard navigation` is Off.
- `PDF function` is On.
- `Smart email address validation` is On.
- `Faster offline synchronization` is visible below.

No Experimental feature in this section is required for the current component-library work.

## UI-018 — Updates > Experimental: faster offline synchronization

Snapshot directly proves:

- `Improved canvas keyboard navigation` remains Off.
- `PDF function` remains On.
- `Smart email address validation` remains On.
- `Faster offline synchronization` is Off.

No change is required for the current component-library build.

## UI-019 — Settings > Support

Exact path:

`Settings -> Support`

Snapshot directly proves:

- Environment displayed: `AI King Env`.
- Authoring version: `3.26083.5`.
- `Edit` is available for authoring-version selection/configuration.
- `Session details` is available.
- Helpful links include Documentation, Terms of use, Open-source licenses, and Privacy statement.

The user also supplied session-detail text showing Power Apps client/server version information. The version is relevant to the UI baseline; unique session, tenant, app, object, and correlation identifiers are not stored.

## Selected settings decision for current work

For the `Burts Power App Components` library, make exactly one feature change now:

`Settings -> Updates -> New -> Modern controls and themes -> On`

Leave Preview and Experimental settings unchanged. After Studio refreshes, return to `cmpAppHeader` and continue the supported custom-property contract.
