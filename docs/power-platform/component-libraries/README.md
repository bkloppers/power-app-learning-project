# Component Libraries — Step-by-Step Guide

Status: ACTIVE
Library: `Burts Power App Components`
Environment: `AI King Env`

## Purpose

Canonical record for reusable Power Apps component-library work.

## Verified creation route

### UI-001 — Solution menu disproved old creation path

Observed in `GCC AI Champions` -> Objects -> New -> App.

Visible App submenu:
- Canvas app
- Model-driven app
- Page

`Component library` was not present. Therefore do not use `Solution -> New -> App -> Component library` in this tenant/UI.

Working project route: create/open the Component Library from the main Power Apps Component Libraries experience, then add it to the governed solution using the supported Add existing flow when required for ALM.

## Component Library Studio

### UI-002 — Components tree and first component

Observed in `Burts Power App Components`.

Tree view tabs:
- Screens
- Components

`Components` selected.

Visible command:
- `+ New component`

Selected component properties pane showed:
- Display
- Advanced
- Description
- Allow customization
- Size / Width / Height
- Fill
- Custom properties
- `+ New custom property`

First reusable component was renamed to `cmpAppHeader`.

### UI-004 — Settings > Updates baseline before component build

Observed in `Burts Power App Components` with `cmpAppHeader` selected.

Exact working path proved by snapshot:

`Settings -> Updates -> New`

Visible update features included:
- Learn more rendering-features entry, currently Off
- Modern controls and themes, currently Off
- New analysis engine and User defined functions, currently On
- Expanded media support for SaveData on Power Apps mobile apps

The Studio description for `Modern controls and themes` states that enabling it provides the latest controls and themes and places modern controls in the Modern tab of the Insert pane.

Current Microsoft guidance verified in August 2026 confirms the enablement path:

`Settings -> Updates -> New -> Modern controls and themes -> On`

This setting is a required project dependency before inserting controls into reusable components because this project uses the current modern-control/theme experience for new Power Apps UI.

After enabling it, Studio refreshes/reloads the authoring experience. Re-check the component editor before continuing.

Microsoft also documents that modern controls use the Fluent 2 design system and provide improved accessibility, performance and usability compared with classic controls. Modern control behavior/property names have continued to change during 2026, so exact control properties must still be verified before implementation.

## cmpAppHeader

Purpose: reusable branded application header.

### UI-003 — Enhanced component custom-property dialog

New custom property dialog visibly contains:
- Display name
- Name
- Description
- Property type

Observed Property type values:
- Data
- Function
- Event
- Action

Correction: do not instruct that the first selector contains Input/Output. For value transfer such as `DarkMode`, select `Data`; direction and data type are configured in the subsequent Data-property fields.

Current property being created:
- Display name: `DarkMode`
- Name: `DarkMode`
- Description: `Controls light/dark presentation of the header.`
- Property type: `Data`
- Intended direction: Input
- Intended data type: Boolean
- Default formula: `true`

### UI-025 — NTT DATA navbar visual reference baseline

Four user-supplied reference screenshots from the NTT DATA Brand Portal / Basecoat navbar examples establish the target visual pattern for `cmpAppHeader`.

Directly observed recurring traits:
- Smart Navy / very dark navy horizontal navbar surface.
- White horizontal NTT DATA logo in the branded dark-header examples.
- Thin vertical divider immediately after the logo when modifier/application text is present.
- Compact modifier text such as `Brand Portal`; it is visually subordinate to the logo and not styled as a large page heading.
- White navigation/utility text and icons on the dark bar.
- Thin Future Blue rule along the bottom edge of the navbar.
- Square, flush application-shell treatment: no card-style rounded corners or floating shadow on the navbar itself.
- Examples vary in surrounding utility/navigation content, but the left brand lockup is consistent.

Project decision derived from these references:
- `cmpAppHeader` should visually follow the dark branded navbar pattern rather than use a large generic 18–26 pt application-title treatment next to the logo.
- The app/modifier title should be compact and separated from the logo with a thin vertical divider.
- The current header implementation remains container-based and responsive; visual fidelity must not reintroduce fixed X/Y layout.

## Reusable-first rules

- Build coherent reusable visual/interaction patterns here rather than duplicating them in individual apps.
- Use explicit component properties as contracts with consuming apps.
- Do not create hidden dependencies on app globals, app collections, app controls or app-specific data sources.
- App-wide nonvisual configuration and reusable named formulas belong in the consuming app's formula layer unless a component-specific contract requires them.
- Use the approved project branding sources; do not invent brand values.
- For new reusable UI, enable and use the current Modern controls and themes experience unless current Microsoft guidance identifies a specific unsupported control/surface.

## Next verified step

Continue `cmpAppHeader` from the UI-025 navbar visual baseline: make the title/modifier compact, add the logo divider, and apply the dark branded navbar surface and Future Blue bottom rule while retaining responsive containers.
