# PH02-G01 GitHub Issue Package

Status: READY FOR GITHUB ISSUE INSTANTIATION
Phase: PH02 - Solution, Publisher and Environment Foundation
Gate: PH02-G01 - Solution and ALM foundation valid
Prepared: 2026-08-27

## Purpose

This file is a durable phase-owned source package for creating the PH02 live operational Issues. It is not a substitute for the live GitHub Issues. After the Issues are created, live status is controlled in GitHub Issues under `project-management/GITHUB-OPERATIONAL-CONTROL-STANDARD.md`.

## Gate Issue

Title:
`[GATE][PH02-G01] Solution and ALM foundation valid`

Body:

### Gate ID
`PH02-G01`

### Phase
Phase 02 - Solution, Publisher and Environment Foundation

### Objective
Validate the governed Power Platform environment, existing custom publisher, unmanaged development solution, configuration-container strategy and evidence required before application-object implementation begins.

### Entry Criteria
- PH01-G01 passed.
- Development environment `AI King Env` identified and accessible.
- Required maker/solution access confirmed.
- Existing publisher `GCC AI Champions Power Platform` and prefix `aiking` verified.
- Existing unmanaged solution `GCC AI Champions` version `1.0.0.0` verified.
- Future-First ALM freshness check completed.

### Required Tickets
- PH02-G01-T01 - Define solution foundation specification.
- PH02-G01-T02 - Perform Future-First ALM freshness check.
- PH02-G01-T03 - Validate existing publisher and unmanaged development solution.
- PH02-G01-T04 - Establish configuration containers.
- PH02-G01-T05 - Validate solution and publisher foundation.
- PH02-G01-T06 - Formal gate review.

### Required Evidence
- PH02 solution-foundation specification.
- Future-First ALM validation.
- Existing-foundation verification and screenshots.
- T03 validation record.
- Environment-variable/connection-reference configuration evidence.
- Independent T05 validation evidence.
- Formal T06 gate decision.

### Acceptance Criteria
- [ ] All gate entry criteria are satisfied.
- [ ] Existing publisher and stable `aiking` prefix are validated.
- [ ] Existing `GCC AI Champions` solution is validated as the approved unmanaged development solution.
- [ ] Configuration-container strategy is established without unnecessary placeholders.
- [ ] All mandatory PH02-G01 tickets are COMPLETE.
- [ ] Required learning, lab, demonstration and understanding evidence exists.
- [ ] No unresolved blocker violates the gate.
- [ ] Project Control is synchronized from live Issue state.
- [ ] PH03 entry evaluation is the exact next action if the gate passes.

### Gate Decision
`NOT DECIDED`

Suggested labels: `type:gate`, `phase:PH02`, `gate:PH02-G01`, `status:in-progress`, `priority:high`.

---

## PH02-G01-T01

Title:
`[PH02][G01][DESIGN] Define solution foundation specification`

Historical status: `COMPLETE`
Points: 2
Workstream: `01 - Architecture and Solution Design`

Dependencies: PH01-G01 passed; verified existing foundation available.

Selected solution: Document and explain the approved environment -> publisher -> solution hierarchy using the verified existing `AI King Env`, `GCC AI Champions Power Platform`, prefix `aiking`, and `GCC AI Champions` unmanaged solution.

Acceptance criteria:
- [x] Environment, publisher, prefix, solution type and solution ownership are documented.
- [x] No superseded provisional naming is treated as current.
- [x] Duplicate publisher/solution creation is explicitly prohibited.
- [x] Learning evidence explains the hierarchy and downstream role.

Evidence:
- `project-management/phases/PH02/evidence/PH02-G01-T01-SOLUTION-FOUNDATION-SPECIFICATION.md`
- `project-management/phases/PH02/evidence/PH02-LEARNING-UNDERSTANDING-EVIDENCE.md`

Suggested labels: `phase:PH02`, `gate:PH02-G01`, `type:design`, `status:complete`.

---

## PH02-G01-T02

Title:
`[PH02][G01][ALM] Perform Future-First ALM freshness check`

Historical status: `COMPLETE`
Points: 1
Workstream: `08 - Deployment and ALM`

Dependencies: T01 complete; Future-First Standard governing.

Selected solution: Validate the current Microsoft solution/publisher/environment-variable/connection-reference/pipeline direction and confirm that the approved PH02 foundation remains production-suitable.

Acceptance criteria:
- [x] Current Microsoft ALM guidance is dated and referenced.
- [x] Custom solution/publisher and unmanaged-development direction is confirmed.
- [x] Environment variables and connection references remain the configuration portability mechanism.
- [x] No current guidance conflicts with the approved PH02 foundation.

Evidence:
- `project-management/phases/PH02/evidence/PH02-ENTRY-VALIDATION-AND-ALM-FRESHNESS.md`
- `project-management/phases/PH02/evidence/PH02-G01-T02-FUTURE-FIRST-ALM-VALIDATION.md`

Suggested labels: `phase:PH02`, `gate:PH02-G01`, `type:alm`, `status:complete`.

---

## PH02-G01-T03

Title:
`[PH02][G01][ALM] Validate existing publisher and unmanaged development solution`

Status: `READY`
Points: 2
Workstream: `08 - Deployment and ALM`

Dependencies:
- T01 COMPLETE.
- T02 COMPLETE.
- Development environment access confirmed.
- Existing foundation screenshots available.

Selected solution: Validate and adopt the existing `GCC AI Champions Power Platform` publisher, permanent `aiking` prefix, and `GCC AI Champions` unmanaged development solution. Do not create duplicates.

Acceptance criteria:
- [ ] Existing custom publisher is confirmed as `GCC AI Champions Power Platform`.
- [ ] Publisher unique name is confirmed as `GCC_AI_Champions_Power_Platform`.
- [ ] Stable publisher prefix is confirmed as `aiking`.
- [ ] Existing `GCC AI Champions` solution is confirmed as Unmanaged version `1.0.0.0`.
- [ ] Existing foundation aligns with the approved PH02 solution-first approach.
- [ ] No duplicate publisher, solution, Canvas App, flow, environment variable, connection reference, or other application component is created by T03.
- [ ] Validation evidence is recorded at the canonical PH02 path.

Evidence:
- `project-management/phases/PH02/evidence/PH02-EXISTING-FOUNDATION-VERIFICATION.md`
- `project-management/phases/PH02/evidence/PH02-G01-T03-VALIDATION-PLAN.md`
- `project-management/phases/PH02/evidence/screenshots/`
- T03 completion validation record when produced.

Suggested labels: `phase:PH02`, `gate:PH02-G01`, `type:alm`, `status:ready`, `priority:high`.

---

## PH02-G01-T04

Title:
`[PH02][G01][BUILD] Establish configuration containers`

Status: `NOT STARTED`
Points: 2
Workstream: `08 - Deployment and ALM`

Dependencies: T03 COMPLETE.

Selected solution: Establish only the environment-variable and connection-reference structures that have a defined downstream use, inside the approved solution, using project naming standards.

Acceptance criteria:
- [ ] Initial environment-variable strategy is recorded in the solution.
- [ ] Initial connection-reference strategy is recorded in the solution.
- [ ] No unnecessary placeholder connection or variable is created.
- [ ] Naming follows project standards.
- [ ] Evidence identifies ownership inside `GCC AI Champions`.

Evidence: solution component inventory and screenshots/metadata.

Suggested labels: `phase:PH02`, `gate:PH02-G01`, `type:build`, `type:alm`, `status:not-started`.

---

## PH02-G01-T05

Title:
`[PH02][G01][TEST] Validate solution and publisher foundation`

Status: `NOT STARTED`
Points: 2
Workstream: `07 - Testing and Validation`

Dependencies: T03 and T04 COMPLETE.

Selected solution: Independently validate the publisher, solution ownership, configuration components, naming and absence of accidental default-solution dependency.

Acceptance criteria:
- [ ] Publisher prefix is stable and correct.
- [ ] Solution ownership of configuration components is confirmed.
- [ ] Required metadata/naming is correct.
- [ ] No accidental default-solution dependency introduced by PH02 is identified.
- [ ] Evidence is sufficient for an independent reviewer to reproduce the checks.

Evidence: validation checklist and screenshots/exported metadata as appropriate.

Suggested labels: `phase:PH02`, `gate:PH02-G01`, `type:test`, `status:not-started`.

---

## PH02-G01-T06

Title:
`[PH02][G01][VALIDATE] Formal gate review`

Status: `NOT STARTED`
Points: 3
Workstream: `07 - Testing and Validation`

Dependencies: T01-T05 COMPLETE; learning/lab/demonstration/understanding evidence available.

Selected solution: Perform the formal PH02-G01 gate review against the approved phase criteria and record PASSED/FAILED with evidence.

Acceptance criteria:
- [ ] All gate entry criteria were satisfied before implementation.
- [ ] All mandatory tickets are COMPLETE.
- [ ] Required evidence exists.
- [ ] Learning outcome is demonstrated.
- [ ] No unresolved blocker violates the gate.
- [ ] Gate decision and date are recorded.
- [ ] Project Control identifies PH03 entry evaluation as the exact next action if PASSED.

Evidence: formal gate decision record with links to ticket evidence.

Suggested labels: `phase:PH02`, `gate:PH02-G01`, `type:validate`, `status:not-started`.

## Instantiation rule

Create these as live GitHub Issues before PH02-G01-T03 execution continues. T01/T02 are created as historical-complete records; T03 is the single READY ticket; T04-T06 remain NOT STARTED. After Issue creation, do not use this package to change live status.