# Power Apps 2026 Studio How-To Guide

Status: ACTIVE / LIVING GUIDE
Baseline date: August 2026
Scope: Power Apps Maker Portal, Solutions, Canvas Apps, Component Libraries and Power Apps Studio used by this project.

## Purpose

This guide records the actual Power Apps user interface and working click paths observed during the project. It is updated continuously from user-provided snapshots and verified against current Microsoft guidance before instructions are given.

The purpose is to prevent repeated rediscovery of menus, prevent regression to obsolete UI guidance, and allow future AI sessions to continue from a proven August 2026 Studio baseline.

## Authority and precedence

For version-sensitive UI instructions use this order:

1. Current user instruction.
2. Current live UI observed in a user-provided snapshot from this project.
3. Current Microsoft Learn / release guidance applicable in August 2026 or later.
4. This guide's most recent verified observation.
5. Older project documentation.
6. General model knowledge.

If current Microsoft documentation and the observed tenant UI differ, do not silently choose one. Record the difference here and give instructions that match the live observed UI when it represents the current available product experience in this environment.

## Mandatory snapshot capture rule

Every Power Apps snapshot uploaded by the user must be recorded in the section of this guide corresponding to the work currently in progress.

For each snapshot record:

- sequential snapshot ID;
- date/session context;
- current environment/app/library;
- exact screen/editor and selected object;
- visible menus, tabs, panels and commands relevant to the active task;
- property names/options/formulas visible;
- the working click path proven by the snapshot;
- any correction to earlier guidance;
- completed state proved by the snapshot;
- next validated step.

Do not require the user to re-upload a snapshot merely to rediscover a menu already recorded here unless the UI has changed or the current state cannot be inferred safely.

---

# 1. Solution Maker Portal

## Snapshot UI-001 — Solution `GCC AI Champions`

Observed: 2026-08-28 session.
Environment: `AI King Env`.
Location: Solutions -> `GCC AI Champions` -> Objects.

### Observed `New` menu

Top-level entries visible included:

- Agent
- App
- Automation
- Dashboard
- Report
- Security
- Table
- More

### Observed `New -> App` submenu

The submenu contained:

- Canvas app
- Model-driven app
- Page

**Component library was not present in `New -> App`.**

### Verified correction

Do not instruct this project to create a Component Library using:

`Solution -> New -> App -> Component library`

That path was disproved by the live August 2026 UI.

### Verified component-library creation route

Use the Power Apps main experience to open the Component Libraries area and create the library there. After creation, add the library to the governed solution using the current supported `Add existing` flow when required for ALM.

---

# 2. Component Libraries

## Current library

Library name: `Burts Power App Components`
Environment: `AI King Env`
Purpose: Reusable cross-app component library for NTT DATA branded/shared Power Apps UI.

## Reusable-first project rule

Where a coherent visual or interaction pattern can be reused across apps, build it in this Component Library rather than duplicating it in an individual Canvas App.

Reusable visual components must be isolated from app-specific globals, collections, controls and data sources. Use explicit component custom properties as the contract with consuming apps.

Application-level named formulas, immutable tokens and reusable Power Fx logic that are not visual-component concerns remain in the consuming app's appropriate formula layer.

---

# 3. Component Library Studio — Tree and component creation

## Snapshot UI-002 — Initial component created

Observed: 2026-08-28 session.
Library: `Burts Power App Components`.
Editor: Power Apps Studio, Component Library.

### Tree view

The left Tree view exposes two tabs:

- Screens
- Components

The `Components` tab was selected.

Visible command:

- `+ New component`

### Component state proved

Initial component was created and later renamed to:

`cmpAppHeader`

The Properties pane for a selected component includes:

- Display
- Advanced
- Description
- Allow customization
- Size (Width / Height)
- Fill
- Custom properties
- `+ New custom property`

### Correction captured

A prior temporary name `cmpAppShellFoundation` was replaced with `cmpAppHeader` because nonvisual app-wide design tokens belong in the consuming app's formula/configuration layer; the library component should represent a real reusable UI object.

---

# 4. `cmpAppHeader`

Purpose: reusable branded application header for consuming Canvas Apps.

Brand dependencies are supplied through explicit component properties or approved media/assets, rather than app-specific hidden dependencies.

## Current custom-property work

First property being created:

`DarkMode`

Purpose: Boolean input controlling light/dark presentation of the reusable header.

Approved description:

`Controls light/dark presentation of the header.`

Default design intent: `true`, matching the project's dark-mode default for internal registered-user applications.

## Snapshot UI-003 — New custom property dialog

Observed: 2026-08-28 session.
Selected component: `cmpAppHeader`.
Dialog: `New custom property`.

### Visible fields

- Display name
- Name
- Description
- Property type

### Actual August 2026 `Property type` menu observed

The menu contains:

- Data
- Function
- Event
- Action

Descriptions shown by Studio indicate:

- **Data** — can send or receive values between the app and the component.
- **Function** — callable as a function with parameters.
- **Event** — event the component can trigger and the app can handle.
- **Action** — callable behavior/function that can change state or produce side effects.

### Verified correction

Do not instruct the user that the first Property type selector contains `Input` and `Output`.

For a value such as `DarkMode`, select **Data** first. Direction (`Input`/`Output`) and data type are configured in the subsequent Data-property configuration presented by Studio.

For `DarkMode` the intended contract is:

- Property type: Data
- Direction/definition: Input
- Data type: Boolean
- Default formula: `true`

Do not use Function, Event or Action for `DarkMode`.

---

# 5. Branding baseline relevant to reusable components

The component library must use the approved NTT DATA design-system source maintained by the project.

Current foundation includes:

- Future Blue primary branding;
- Smart Navy dark background;
- approved Future Blue / Black / White logo variants only;
- horizontal logo orientation for the Header;
- native logo aspect ratio preserved;
- Noto Sans primary UI typeface;
- Noto Serif restricted to approved headline/callout use;
- semantic status colors from the project design source;
- responsive design and container-based composition;
- dark/light support, with dark mode default for the current internal app.

Do not redraw or approximate NTT DATA brand marks.

---

# 6. Responsive Canvas App creation

Current project rule: new Canvas Apps for this project use the current **Responsive** blank-app choice, not a fixed Tablet or Phone baseline.

Before giving the exact creation click path, verify the current August 2026 Maker Portal UI and update this section with the observed working route.

---

# 7. Update procedure

Whenever the user uploads a new Power Apps screenshot:

1. Identify the active guide section.
2. Assign the next `UI-###` snapshot ID.
3. Record only what is actually visible/proved.
4. Record any inferred next step separately from observed facts.
5. Reconcile with current Microsoft guidance before issuing the next technical instruction.
6. If an earlier guide entry is obsolete, mark it superseded or correct it explicitly; do not leave contradictory current instructions.
7. Continue using the recorded UI baseline without asking the user to reproduce the same evidence.

This guide is a living project artifact and must be updated during the build, not reconstructed at project end.
