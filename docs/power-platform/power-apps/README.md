# Power Apps — Step-by-Step Guide

Status: ACTIVE
Baseline: August 2026

## Scope

Canvas Apps, Power Apps Studio, App object, screens, controls, responsive layout, properties, navigation, accessibility and app-level configuration.

## Current project baseline

- New production Canvas Apps use the current Responsive experience, not a Tablet-first or Phone-first fixed canvas.
- Responsive/container-driven composition is required.
- App.StartScreen is used for declarative startup screen selection.
- App.Formulas is used for reusable calculated and immutable app configuration.
- App.OnStart remains minimal and is reserved for genuine one-time mutable startup state or side effects.
- App.OnError is the application-level final error handler after expected errors are handled locally.
- Reusable UI is evaluated for Component Library placement before being built app-specific.

## Verified Maker Portal observation

### UI-001 — Solution `New -> App` submenu

Environment: `AI King Env`
Solution: `GCC AI Champions`
Location: Objects -> New -> App

Observed entries:
- Canvas app
- Model-driven app
- Page

This snapshot also proved that Component Library creation is not exposed in this submenu in the current tenant UI; that procedure is documented under `../component-libraries/`.

## Responsive app creation

The project requires the current Responsive blank-app experience. Before the exact click path is used in the build, verify the current August 2026-or-later Maker Portal UI and record the working sequence here from the observed UI.

## Documentation pattern for future Power Apps steps

For every screen/control/property build step record:
- dependency state;
- exact Studio location;
- exact object name;
- property selected;
- formula/value entered;
- visible menu/options;
- screenshot evidence ID;
- result;
- validation;
- next step.
