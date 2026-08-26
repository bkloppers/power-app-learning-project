# Phase 02 - Solution, Publisher and Environment Foundation

## Status

NOT STARTED - first implementation phase, pending PH01-G01 passage and entry validation.

## Objective

Establish the governed Power Platform solution and ALM foundation before creating implementation assets that would otherwise become standalone or environment-bound artifacts.

## Hierarchy Level

Power Platform environment, publisher, solution, environment-variable and connection-reference foundation.

## Learning Outcome

The learner can explain the relationship between environment, custom publisher, unmanaged development solution, solution ownership, environment variables, connection references, and downstream managed deployment.

## Prerequisites

- `PH01-G01 - Solution scope and process approved` is formally passed.
- Approved foundation baseline remains current.
- Development Power Platform environment is identified and accessible.
- Required maker/solution permissions are confirmed.
- Project naming standard inputs needed for environment/publisher/solution names are available.
- Current Microsoft documentation/release status for solutions, publishers, environment variables, connection references and deployment tooling has been checked under the Future-First Standard.

## Lab

Create the production-oriented development foundation:

1. confirm the approved Development environment;
2. define the custom publisher and stable prefix;
3. create the unmanaged development solution;
4. establish solution ownership for the future Canvas App and flows;
5. establish the initial environment-variable and connection-reference strategy;
6. record downstream deployment expectations without prematurely creating production assets.

## Demonstration

Show:

- the custom publisher and stable prefix;
- the unmanaged development solution;
- where the future Canvas App, flows, environment variables and connection references will live;
- how the solution is intended to move downstream as a governed unit rather than as manually repaired standalone artifacts.

## Understanding

The learner must explain:

- why a custom publisher is chosen before component creation;
- why the publisher prefix must remain stable;
- why implementation begins inside an unmanaged development solution;
- why environment-specific values should not be hard-coded into the app;
- why development artifacts and production deployment artifacts have different lifecycle states;
- why creating an app first and adding governance later produces avoidable ALM debt.

## Gate

`PH02-G01 - Solution and ALM foundation valid`

### Gate Entry Criteria

- PH01-G01 passed.
- Development environment and access confirmed.
- Required naming inputs confirmed.
- Future-first freshness check completed.
- No unresolved issue blocks solution/publisher creation.

### Required Tickets

#### PH02-G01-T01 - DESIGN - Define solution foundation specification
Status: NOT STARTED
Points: 2
Workstream: `01 - Architecture and Solution Design`
Dependencies: PH01-G01 passed; naming standards; approved application direction.
Acceptance Criteria:
- Development environment naming is documented.
- Publisher display name, unique name and stable prefix are documented.
- Solution display/unique name is documented.
- Ownership of future Canvas App, flows, environment variables and connection references is explicit.
- No environment-specific secrets or mutable deployment values are proposed as hard-coded app constants.
Evidence:
- Reviewed solution-foundation specification linked from the ticket.

#### PH02-G01-T02 - ALM - Perform Future-First ALM freshness check
Status: NOT STARTED
Points: 1
Workstream: `08 - Deployment and ALM`
Dependencies: T01 may be drafted; current Microsoft documentation access.
Acceptance Criteria:
- Current generally available guidance for solutions and custom publishers checked.
- Current environment-variable and connection-reference guidance checked.
- Current deployment/pipeline direction checked.
- Any conflict with repository standards is recorded before build work.
- Preview/planned features are clearly separated from production dependencies.
Evidence:
- Dated references/validation note in the ticket.

#### PH02-G01-T03 - BUILD - Create custom publisher and unmanaged development solution
Status: NOT STARTED
Points: 2
Workstream: `08 - Deployment and ALM`
Dependencies: T01 complete; T02 complete; Development environment access confirmed.
Acceptance Criteria:
- Custom publisher exists with the approved stable prefix.
- Unmanaged development solution exists using the approved naming standard.
- Preferred/working solution configuration is aligned with the approved approach where applicable.
- No implementation component is created outside the approved solution as part of this ticket.
Evidence:
- Publisher screenshot/metadata.
- Solution screenshot/metadata.
- Naming verification.

#### PH02-G01-T04 - BUILD - Establish configuration containers
Status: NOT STARTED
Points: 2
Workstream: `08 - Deployment and ALM`
Dependencies: T03 complete.
Acceptance Criteria:
- Initial environment-variable strategy is recorded in the solution.
- Initial connection-reference strategy is recorded in the solution.
- No unnecessary placeholder connection or variable is created without a defined future use.
- Naming follows project standards.
Evidence:
- Solution component inventory and screenshots/metadata.

#### PH02-G01-T05 - TEST - Validate solution and publisher foundation
Status: NOT STARTED
Points: 2
Workstream: `07 - Testing and Validation`
Dependencies: T03 and T04 complete.
Acceptance Criteria:
- Publisher prefix is confirmed stable and correct.
- Solution ownership of created configuration components is confirmed.
- Required metadata/naming is correct.
- No accidental default-solution dependency introduced by this phase is identified.
- Evidence is sufficient for an independent reviewer to reproduce the checks.
Evidence:
- Validation checklist and screenshots/exported metadata as appropriate.

#### PH02-G01-T06 - VALIDATE - Formal gate review
Status: NOT STARTED
Points: 3
Workstream: `07 - Testing and Validation`
Dependencies: T01-T05 complete; Lab, Demonstration and Understanding evidence available.
Acceptance Criteria:
- All gate entry criteria were satisfied before implementation.
- All mandatory tickets are complete.
- Required evidence exists.
- Learning outcome demonstrated.
- No unresolved blocker violates the gate.
- Project Control identifies PH03 as the exact next phase if gate passes.
Evidence:
- Gate decision record with links to ticket evidence.

## Proposed Session Batches

These are provisional until tickets become READY.

### SES-PH02-G01-ARCH-01
- PH02-G01-T01 - 2 points
Total: 2

### SES-PH02-G01-ALM-01
- PH02-G01-T02 - 1 point
- PH02-G01-T03 - 2 points
- PH02-G01-T04 - 2 points
Total: 5

T03 may activate only after T02 reaches its required handoff state and all T03 dependencies are confirmed.

### SES-PH02-G01-TEST-01
- PH02-G01-T05 - 2 points
Total: 2

### SES-PH02-G01-VALIDATE-01
- PH02-G01-T06 - 3 points
Total: 3

## Exit Criteria

- PH02-G01 formally passed.
- Development solution and custom publisher are validated.
- Environment-variable/connection-reference strategy is established at the level required for the next phase.
- Design/learning evidence is recorded.
- Project Control is synchronized.
- PH03 entry criteria can be evaluated without guessing.

## Implementation Authorization

This phase is **not READY** until PH01-G01 is formally passed and the Phase 02 Gate Entry Criteria above are confirmed.
