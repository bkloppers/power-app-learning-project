# PH02-G01-T01 - Verified Solution Foundation Specification

Date: 2026-08-27
Phase: PH02 - Solution, Publisher and Environment Foundation
Gate: PH02-G01 - Solution and ALM foundation valid
Ticket: PH02-G01-T01 - DESIGN
Workstream: 01 - Architecture and Solution Design
Status: COMPLETE

## Authoritative foundation

- Environment: `AI King Env`
- Environment type: `Developer`
- Existing publisher: `GCC AI Champions Power Platform`
- Publisher unique name: `GCC_AI_Champions_Power_Platform`
- Publisher prefix: `aiking`
- Existing solution: `GCC AI Champions`
- Solution type: `Unmanaged`
- Solution version: `1.0.0.0`

This foundation was verified from maker-portal evidence and approved for reuse by the Project Owner. No replacement publisher or development solution is to be created.

## Environment -> publisher -> solution relationship

`AI King Env` is the development environment in which the governed Power Platform application family is developed. The custom publisher `GCC AI Champions Power Platform` owns the stable customization identity used by solution components. Its prefix `aiking` is therefore a durable technical namespace and must remain stable. The unmanaged solution `GCC AI Champions` is the development source container in which the Canvas App, flows, environment-variable definitions, connection references, and other solution-aware components will be added when their tickets authorize creation.

The development solution is intentionally unmanaged because unmanaged solutions are the editable development source. Downstream non-development environments are expected to receive managed build artifacts produced from the development solution under the later ALM design.

## Component ownership rule

Future solution-aware implementation assets for this application family must be created inside `GCC AI Champions` unless a later locked decision explicitly changes the solution boundary. This includes, when their phases authorize them:

- Canvas App;
- Power Automate flows;
- environment-variable definitions;
- connection references;
- other solution-aware Power Platform components.

No application/component creation is authorized by T01 itself.

## Environment-specific configuration rule

Environment-specific mutable deployment values must not be embedded as hard-coded application constants when supported solution configuration mechanisms exist. Environment-variable definitions and connection references are the approved ALM mechanisms to be designed/introduced only when a real dependency exists.

## Superseded provisional values

The following values must not be used:

- `Burt Kloppers's Environment`
- `NTT DATA Power Platform`
- `NTTDataPowerPlatform`
- `nttd`
- `AI - Prompt Tools`
- `NTT_AI_PromptTools`

## Learning / understanding result

The verified hierarchy is:

`Developer environment -> custom publisher/stable prefix -> unmanaged development solution -> solution components -> managed downstream artifact`

The publisher is selected before component creation because its prefix becomes part of component technical identity. The prefix must remain stable to avoid namespace fragmentation. The unmanaged solution is the editable source container; downstream managed deployment is a separate lifecycle state. Environment-specific values are separated from component logic so the same solution can move between environments without manual formula rewrites.

## Acceptance criteria

- [x] Development environment is documented.
- [x] Publisher display name, unique name and stable prefix are documented.
- [x] Solution display name and solution lifecycle state are documented.
- [x] Ownership of future Canvas App, flows, environment variables and connection references is explicit.
- [x] No environment-specific secrets or mutable deployment values are proposed as hard-coded app constants.
- [x] Existing approved foundation is reused rather than duplicated.

## Outcome

PH02-G01-T01 is COMPLETE. PH02-G01-T02 may formally consume the dated Future-First ALM freshness evidence. PH02-G01-T03 remains a validation ticket for the existing publisher and unmanaged solution; it is not a creation task.
