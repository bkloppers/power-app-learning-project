# Power Apps Learning Solution Design

## Document Purpose

This is the living physical design specification for the Power Apps learning project. It will describe the solution from initial concept through production-ready implementation and will grow as each learning phase is designed, built, demonstrated, validated, and understood.

The document is intentionally cumulative. Later phases extend the same application and do not replace earlier learning labs with disconnected examples.

## Learning Delivery Model

Every hierarchy level follows the same cycle:

**Learning Phase -> Lab -> Demonstration -> Understanding**

Each phase must therefore contain:

1. **Learning Phase** - concepts, hierarchy level, purpose, dependencies, and design rules.
2. **Lab** - the exact implementation work added to the real application.
3. **Demonstration** - observable behaviour proving how the level functions.
4. **Understanding** - validation criteria and explanation of why the implementation is structured this way.

A phase is not complete until the demonstration and understanding criteria are satisfied.

## Solution Principles

The application will be built using production-oriented Power Platform practices from the first phase:

- solution-first development;
- descriptive and consistent naming;
- responsive container-based Canvas App layouts;
- modern controls and themes where supported;
- reusable components for structural UI;
- named formulas for calculated and reusable values;
- mutable variables only for remembered application state;
- minimal `App.OnStart`;
- delegation-safe data access;
- data-layer security rather than UI-only security;
- accessibility and explicit error handling;
- environment variables and connection references for deployable configuration;
- controlled ALM and deployment;
- realistic testing before a phase is considered complete.

## Brand and Design System

The application uses the approved NTT DATA Canvas App design system already maintained in the project.

Core design rules include:

- no raw colour, typography, spacing, or sizing values in production UI formulas when a named token exists;
- reusable Header and Sidebar components;
- container-based responsive layout;
- Light and Dark modes only;
- Dark Mode as the default for this internal registered-user application;
- approved NTT DATA logo and icon assets only;
- Noto Sans as the primary UI font and Noto Serif only for approved headline/call-out usage;
- Future Blue as the primary brand action colour;
- the documented spacing, gutter, semantic-colour, accessibility, and responsive rules.

## Naming Standard

The project uses descriptive object names and predictable prefixes.

Examples:

- Screens: plain-language purpose ending in `Screen`.
- Containers: `con<Purpose>`.
- Components: `cmp<Purpose>`.
- Buttons: `btn<Purpose>`.
- Labels: `lbl<Purpose>`.
- Text inputs: `txt<Purpose>`.
- Galleries: `gal<Purpose>`.
- Forms: `frm<Purpose>`.
- Global state: `gbl<Purpose>`.
- Screen context state: `loc<Purpose>`.
- Collections: `col<PluralPurpose>`.
- Data sources: PascalCase business names.

Control names must remain unique across the application. Screen suffixes will be used where a repeated control purpose exists on multiple screens.

## Responsive Screen Architecture

Every production screen will follow the same structural model:

```text
Screen
└── conScreenRoot
    ├── conPageFlowCol
    │   ├── conAppHeaderRow
    │   ├── conAppBodyRow
    │   │   ├── conSideNavCol
    │   │   └── conMainCol
    │   └── conAppFooterRow (when required)
    └── conOverlayHost
```

The normal page flow uses auto-layout containers. `conScreenRoot` acts as the full-screen layer host so dialogs, toasts, busy states, and drawers can be layered without forcing the normal UI into absolute positioning.

## Application-Level Architecture

The App object will be treated as an application-level configuration layer rather than a dumping ground for initialization logic.

Selected use:

- `App.StartScreen` - determines the first screen declaratively.
- `App.Formulas` - reusable calculated values, constants, design tokens, and read-only configuration.
- `App.OnStart` - only genuine one-time side effects and mutable session-state initialization.
- `App.OnError` - global fallback error reporting after expected errors have been handled locally.
- screen `OnVisible` - screen-entry behaviour only.
- control event properties - user-driven state transitions.

## State Management Rule

Use this decision order:

1. Direct formula when the value can be calculated where it is used.
2. `App.Formulas` for reusable calculated values.
3. `With()` for calculations local to one formula.
4. Context variables for screen-specific state.
5. Global variables only for mutable state shared across screens.
6. Collections only for small mutable tables, drafts, or explicitly required local caches.
7. `App.OnStart` only when the action genuinely needs to occur once at startup.

## Brand Shell Baseline

The initial application shell will eventually contain:

- sticky Header component;
- responsive Sidebar component;
- main content region;
- overlay host;
- application-wide Light/Dark theme support;
- approved NTT DATA logo variant switching;
- responsive desktop/tablet/mobile behaviour;
- standard error, loading, toast, and dialog patterns.

The shell will not all be introduced in the first learning phase. Each part will be added when its hierarchy level becomes the active learning subject.

## Proposed Repository Structure

```text
power-app-learning-project/
├── README.md
├── AGENTS.md
├── docs/
│   ├── solution-design/
│   │   └── POWER-APPS-LEARNING-SOLUTION-DESIGN.md
│   ├── standards/
│   │   ├── naming/
│   │   ├── variables/
│   │   ├── responsive-layout/
│   │   └── design-system/
│   ├── architecture/
│   ├── data-model/
│   ├── security/
│   ├── integrations/
│   ├── testing/
│   └── deployment/
├── project-management/
│   ├── AI-PROJECT-CONTINUITY-FLOW.md
│   ├── PROJECT-CONTROL.md
│   ├── DECISIONS.md
│   ├── ISSUES.md
│   └── phases/
│       ├── PHASE-01.md
│       ├── PHASE-02.md
│       └── ...
├── power-platform/
│   ├── solutions/
│   ├── canvas-app/
│   ├── power-automate/
│   ├── dataverse/
│   └── environment-configuration/
├── assets/
│   ├── brand/
│   ├── icons/
│   └── screenshots/
└── evidence/
    ├── labs/
    ├── demonstrations/
    ├── tests/
    └── release-validation/
```

Folders are introduced when they gain real content; empty placeholder folders are not required in Git.

## Design Document Structure

As the end application is defined, this document will grow to include the following sections:

1. Vision and business outcome.
2. Users, roles, personas, and permissions.
3. End-to-end business process.
4. Power Apps hierarchy learning map.
5. Solution architecture.
6. Environment and ALM architecture.
7. Publisher, solution, and naming design.
8. Data model and relationships.
9. Security model.
10. Canvas App screen architecture.
11. App object and application state.
12. Components and reusable UI.
13. Responsive behaviour.
14. Brand and design-system application.
15. Navigation architecture.
16. Forms, validation, and user interactions.
17. Delegation and data-access strategy.
18. Power Automate flows.
19. Integrations and connectors.
20. Error handling and observability.
21. Accessibility.
22. Testing strategy and evidence.
23. Deployment and release management.
24. Learning Phase + Lab + Demonstration + Understanding records.
25. Decision log references.
26. Open issue references.
27. Definition of done.

## Current Status

The solution architecture cannot yet be finalized because the end application and business process have not yet been described. This is intentionally recorded as a dependency rather than guessed.

### Information still required

The next design input is the end application concept, including:

- business problem;
- intended users and roles;
- core process from beginning to end;
- key records/data involved;
- approvals or decisions;
- integrations or external systems already known;
- reporting or dashboard requirements;
- mobile, tablet, desktop, and offline expectations;
- security or confidentiality considerations.

Once that information is supplied, the hierarchy learning phases will be mapped directly to the final application so every lab adds a real production-relevant capability.

## Governance

This document is a living design specification. Durable architectural choices must also be entered in `project-management/DECISIONS.md`. Current phase, active task, blockers, and exact next step must be maintained in `project-management/PROJECT-CONTROL.md`. Detailed phase acceptance and exit criteria belong under `project-management/phases/`.

GitHub is the durable source of truth. Chat history may explain context but must not silently override the approved design and locked project decisions stored here.
