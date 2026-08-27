# PH02-G01-T04 - Configuration Container Plan

Date: 2026-08-27
Phase: PH02 - Solution, Publisher and Environment Foundation
Gate: PH02-G01 - Solution and ALM foundation valid
Ticket: PH02-G01-T04
Workstream: 08 - Deployment and ALM
Status: IN PROGRESS

## Selected solution

Establish only configuration containers with a confirmed downstream use inside the existing `GCC AI Champions` unmanaged solution. Do not create placeholder configuration merely to populate the solution.

## Dependencies

- PH02-G01-T03 / Issue #15: COMPLETE.
- Development environment: `AI King Env`.
- Publisher: `GCC AI Champions Power Platform` / prefix `aiking`.
- Solution: `GCC AI Champions` / Unmanaged / `1.0.0.0`.
- Tool 01 data platform: Microsoft Lists / SharePoint Lists.
- Source template location confirms the Tool 01 SharePoint site: `https://nttlimited.sharepoint.com/teams/GCCProfessionalServices-Z1-PS2.0AutomationUseCases`.

## Future-First freshness check

Checked 2026-08-27 against current Microsoft Learn guidance.

- Environment variables remain solution components for environment-specific configuration and support SharePoint site/list data-source parameters.
- Canvas apps can bind SharePoint site/list parameters through data-source environment variables.
- Connection references remain solution components that bind solution-aware flows/apps to environment-specific connections.
- Solution-aware cloud flows use connection references; current guidance supports explicitly keeping the reference in the same solution as the flow.
- No preview/planned capability is required for T04.

References:
- Microsoft Learn - Use environment variables in Power Platform solutions.
- Microsoft Learn - Use data source environment variables in canvas apps.
- Microsoft Learn - Use a connection reference in a solution with Microsoft Dataverse.

## Authorized components

### 1. Tool 01 SharePoint Site environment variable

Purpose: allow the same future Canvas App / solution-aware flow design to resolve the Tool 01 SharePoint site per environment without hard-coding the development site.

Create inside `GCC AI Champions`:

- Display name: `evnTool01SharePointSite`
- Schema name: publisher-prefixed `aiking_evnTool01SharePointSite`
- Data type: `Data source`
- Connector: `SharePoint`
- Parameter type: `Site`
- Development current value: `https://nttlimited.sharepoint.com/teams/GCCProfessionalServices-Z1-PS2.0AutomationUseCases`
- Description: `Tool 01 SharePoint site used by solution-aware data sources. Set per environment during deployment.`

This is not a placeholder: Tool 01 is locked to Microsoft Lists / SharePoint Lists and the existing source template identifies the concrete development site.

### 2. Tool 01 SharePoint connection reference

Purpose: provide the governed SharePoint connection binding for future solution-aware cloud flows without embedding a user connection directly in flow logic.

Create inside `GCC AI Champions`:

- Display name: `crSharePointTool01`
- Connector: `SharePoint`
- Connection: reuse the existing authenticated development SharePoint connection that can access the Tool 01 site; do not create a duplicate connection if a suitable one already exists.
- Description: `SharePoint connection reference for Tool 01 solution-aware cloud flows.`

This has a defined downstream use in PH16, where approved Tool 01 solution-aware cloud flows will interact with SharePoint/Microsoft Lists.

## Explicitly deferred components

Do not create any of the following in T04:

- SharePoint List environment variables. PH09 owns List creation and the final governed list identities.
- Additional connection references for Outlook, Teams, Office 365 Users, AI/Copilot, or any other connector. Create them only when an approved downstream component requires them.
- Canvas App, cloud flow, Microsoft List, custom connector, Tool 02 object, or other application component.

## Pre-creation duplicate check

Before creating either authorized component, inspect `GCC AI Champions` -> Objects and confirm an equivalent environment variable or connection reference does not already exist. If an equivalent component exists, reuse it and capture its metadata instead of creating a duplicate.

## Required evidence

Capture maker-portal screenshots showing:

1. `GCC AI Champions` solution object list containing the environment variable and connection reference.
2. Environment variable properties showing name/type/SharePoint Site parameter and development value.
3. Connection reference properties showing `crSharePointTool01`, SharePoint connector and bound development connection.

Canonical screenshot destination:

`project-management/phases/PH02/evidence/screenshots/`

Recommended filenames:

- `PH02-T04-CONFIGURATION-COMPONENTS.png`
- `PH02-T04-EVN-TOOL01-SHAREPOINT-SITE.png`
- `PH02-T04-CR-SHAREPOINT-TOOL01.png`

## Acceptance mapping

- Initial environment-variable strategy recorded in the solution: satisfied when `evnTool01SharePointSite` exists in `GCC AI Champions` with evidence.
- Initial connection-reference strategy recorded in the solution: satisfied when `crSharePointTool01` exists in `GCC AI Champions` with evidence.
- No unnecessary placeholder connection or variable: satisfied by the explicit defer list and duplicate check.
- Naming follows project standards: `evn<Purpose>` and `cr<Connector><Purpose>` conventions applied; publisher prefix remains `aiking`.
- Evidence identifies ownership inside `GCC AI Champions`: satisfied by solution-object inventory screenshot and T04 component inventory record.

## Current result

Repository planning and dependency validation are complete. Power Platform maker-portal component creation/evidence remains required before T04 can enter VALIDATION or COMPLETE.
