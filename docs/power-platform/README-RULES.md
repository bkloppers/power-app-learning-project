# Power Platform Documentation Rules

Status: GOVERNING PROJECT RULE
Baseline: August 2026

## Rule 1 — One canonical Power Platform documentation tree

All step-by-step Power Platform build documentation belongs under `docs/power-platform/`.

Each distinct product/technical area has its own subfolder and `README.md` guide. Do not mix unrelated areas into one document.

## Rule 2 — Verify before instructing

Before providing any Power Platform lesson, click path, formula, configuration, component instruction, admin instruction or version-sensitive recommendation, verify it against current Microsoft guidance applicable in August 2026 or later.

Then reconcile the documentation with the latest live UI observed in project snapshots.

## Rule 3 — Every snapshot is evidence

Every user-supplied Power Platform screenshot must be recorded in the active area's guide before proceeding when repository access permits.

Record what the snapshot actually proves: current product surface, selected object, visible menu options, fields, property names, values and state. Do not present inference as observed fact.

## Rule 4 — Document every build action

As work is performed, record every meaningful action, including exact click path, dependency, object name, setting/property, formula/value, result, validation and next step.

The documentation is written during the build, not reconstructed afterwards.

## Rule 5 — Do not make the user rediscover UI

Once a menu, path, option or product behavior has been verified and recorded, use the documented baseline. Do not ask for another screenshot merely to rediscover the same UI unless there is evidence that the product changed or the current state is genuinely ambiguous.

## Rule 6 — Corrections are explicit

When a snapshot disproves earlier guidance, record the old instruction as superseded, document the observed current UI, verify current Microsoft guidance and replace the working sequence. Do not leave contradictory current instructions active.

## Rule 7 — Area placement

Examples:
- Canvas App / Studio work -> `power-apps/`
- Component Library work -> `component-libraries/`
- Power Fx -> `power-fx/`
- Admin Center -> `power-platform-admin-center/`
- Solutions / ALM -> `solutions-alm/`
- Power Automate -> `power-automate/`
- Dataverse -> `dataverse/`
- SharePoint / Microsoft Lists -> `sharepoint-microsoft-lists/`
- Teams hosting -> `microsoft-teams/`
- Copilot / AI -> `copilot-ai/`

Create a new area folder when a genuinely separate Power Platform area is first covered.

## Rule 8 — Reusable-first and responsive-first

Reusable UI/interaction patterns are evaluated for the approved Component Library before app-specific implementation. New Canvas Apps use the current Responsive experience and container-driven layouts.

## Rule 9 — Branding source

Use the approved project branding/design sources. Do not invent colors, typography, logos, spacing or brand behavior.

## Rule 10 — Source priority for UI guidance

1. Explicit current-session user instruction.
2. Current live UI observed in project snapshots.
3. Current Microsoft guidance applicable in August 2026 or later.
4. The active area's latest verified guide.
5. Older project documentation.
6. General model memory.
