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

## Reusable-first rules

- Build coherent reusable visual/interaction patterns here rather than duplicating them in individual apps.
- Use explicit component properties as contracts with consuming apps.
- Do not create hidden dependencies on app globals, app collections, app controls or app-specific data sources.
- App-wide nonvisual configuration and reusable named formulas belong in the consuming app's formula layer unless a component-specific contract requires them.
- Use the approved project branding sources; do not invent brand values.

## Next verified step

Complete the `DarkMode` Data/Input/Boolean property in `cmpAppHeader`, then document the resulting property panel before defining the rest of the header contract.
