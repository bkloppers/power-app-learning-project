# Power Platform Build Knowledge Base

Status: ACTIVE / LIVING DOCUMENTATION
Baseline: August 2026

## Purpose

This folder is the canonical step-by-step record of everything built, configured, verified and learned across the Power Platform project.

Every covered Power Platform area has its own subfolder and dedicated guide. The guides are updated continuously while the work is performed. They are not end-of-project summaries.

## Documentation rule

For every verified action, record in the relevant area guide:

1. Date/session context.
2. Environment, app, solution, library, flow or resource involved.
3. Exact starting location.
4. Exact click path.
5. Menus, panels, options and property names actually observed.
6. Values, formulas and configuration entered.
7. Dependencies required before the step.
8. What the supplied snapshot directly proves.
9. Any mismatch with prior instructions or older documentation.
10. The corrected working sequence.
11. Result/validation evidence.
12. Next verified step.

Every user-supplied Power Platform screenshot is project evidence and must be recorded in the active area's guide. Once a UI path is proved and recorded, do not make the user reproduce it merely to rediscover the same menu.

Before any new lesson or implementation instruction, verify version-sensitive guidance against current Microsoft documentation applicable in August 2026 or later, then reconcile it with the latest observed tenant UI recorded here.

## Areas

- `power-apps/` — Canvas Apps, Studio, screens, controls, responsive layout, App object and app configuration.
- `component-libraries/` — reusable component libraries, component contracts, custom properties and publishing.
- `power-fx/` — formulas, named formulas, variables, user-defined functions and formula patterns.
- `power-platform-admin-center/` — environments, settings, governance and administration.
- `solutions-alm/` — solutions, publishers, environment variables, connection references, pipelines and deployment.
- `power-automate/` — cloud flows, triggers, actions, error handling and integration.
- `dataverse/` — Dataverse tables, relationships, security and platform data concepts when used.
- `sharepoint-microsoft-lists/` — SharePoint / Microsoft Lists data sources, columns, permissions and delegation-related setup.
- `microsoft-teams/` — Teams hosting, publishing and host-specific behavior.
- `copilot-ai/` — Copilot Studio, AI, agents and approved AI integration work.

Add another subfolder when a genuinely separate Power Platform area becomes part of the project. Do not mix unrelated areas into one guide.

## Evidence identifiers

Snapshots use IDs in the form `UI-###`. Each snapshot is documented under the area and subsection being worked on, not in a detached screenshot dump.
