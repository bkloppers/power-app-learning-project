# Phase Folder Standard

## Status

MANDATORY

## Rule

Every project phase must have one canonical folder under:

`project-management/phases/PHxx/`

Every artifact owned by that phase must be stored inside that phase folder. Phase-specific files must not be stored in the root of `project-management/`, in a shared `project-management/evidence/` hierarchy, or in another phase's folder.

## Canonical Structure

```text
project-management/phases/PHxx/
├── PHASE-xx.md
├── gates/
├── evidence/
│   └── screenshots/
├── approvals/
└── handoffs/
```

Git does not require empty folders to exist. A subfolder is created when the phase first produces an artifact of that type.

## Placement Rules

- `PHASE-xx.md`: phase definition, status, learning, lab, demonstration, understanding, gates, tickets and exit criteria.
- `gates/`: phase-specific gate packages, ticket packages and gate-definition artifacts.
- `evidence/`: phase-specific design, build, test, validation, learning and gate evidence.
- `evidence/screenshots/`: screenshots and other visual proof generated for that phase.
- `approvals/`: approvals that apply only to that phase or one of its gates.
- `handoffs/`: handoffs whose ownership is confined to that phase.

## Global / Cross-Phase Exception

An artifact stays outside a phase folder only when it governs or applies to multiple phases or the project as a whole. Examples include:

- `PROJECT-CONTROL.md`;
- `DECISIONS.md`;
- `ISSUES.md`;
- process and governance standards;
- the Future-First standard;
- cross-phase roadmaps and operational delivery plans;
- shared solution-design documents used by multiple phases;
- approvals whose scope is the whole project;
- handoffs that explicitly cross phase boundaries.

Do not duplicate a global artifact into phase folders merely because a phase references it. Link to the global source instead.

## Creation Rule

Before creating any phase-specific artifact:

1. identify its owning phase;
2. confirm `project-management/phases/PHxx/` exists;
3. place the artifact in the correct phase subfolder;
4. update references to use the canonical path;
5. do not create a second copy elsewhere.

If ownership cannot be assigned to exactly one phase because the artifact genuinely governs several phases, treat it as cross-phase and keep it at the appropriate shared project location.

## Migration Rule

When a phase-specific file is found outside its phase folder, move it into the canonical phase folder and update references in the same change. Do not leave compatibility duplicates behind.

## Current Canonical Examples

```text
project-management/phases/PH01/PHASE-01.md
project-management/phases/PH01/gates/
project-management/phases/PH01/evidence/

project-management/phases/PH02/PHASE-02.md
project-management/phases/PH02/evidence/
```

This standard applies to all existing and future phases.