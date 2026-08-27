# PH02-G01-T05 - Validation Plan

Date: 2026-08-27
Phase: PH02 - Solution, Publisher and Environment Foundation
Gate: PH02-G01 - Solution and ALM foundation valid
Ticket: PH02-G01-T05 / Issue #17
Workstream: 07 - Testing and Validation
Status: IN PROGRESS

## Selected solution

Independently validate the existing PH02 publisher/solution/configuration foundation. T05 creates no Power Platform components.

## Dependencies

- T03 COMPLETE.
- T04 COMPLETE and evidence reconciled to `main` through PR #23.
- Issue #17 is OPEN / `status:in-progress`.
- Development environment: `AI King Env`.
- Publisher: `GCC AI Champions Power Platform`.
- Publisher unique name: `GCC_AI_Champions_Power_Platform`.
- Publisher prefix: `aiking`.
- Solution: `GCC AI Champions` / Unmanaged / version `1.0.0.0`.
- T04 components: `aiking_evnTool01SharePointSite` and `aiking_crSharePointTool01`.

## Validation sequence

1. Reconfirm the publisher display name, unique name and stable `aiking` prefix.
2. Reconfirm `GCC AI Champions` is the owning unmanaged development solution.
3. Reconfirm both T04 configuration components are inside `GCC AI Champions` and use the expected `aiking_` schema prefix.
4. Inspect the solution/component views for evidence that PH02 introduced no accidental default-solution-only dependency.
5. Capture only the fresh screenshots/metadata required for an independent reviewer to repeat the checks.
6. Record PASS/FAIL against each Issue #17 acceptance criterion.

## Required fresh evidence

Capture maker-portal evidence showing:

- publisher properties with display name, unique name and `aiking` prefix;
- `GCC AI Champions` solution properties showing Unmanaged and version `1.0.0.0`;
- solution Objects list showing the two T04 configuration components and their `aiking_` schema names.

Canonical screenshot destination:

`project-management/phases/PH02/evidence/screenshots/`

Recommended filenames:

- `PH02-T05-PUBLISHER-VALIDATION.png`
- `PH02-T05-SOLUTION-VALIDATION.png`
- `PH02-T05-CONFIGURATION-OWNERSHIP.png`

## Acceptance mapping

- Publisher prefix stable and correct: validate publisher properties against the T03 baseline.
- Solution ownership confirmed: validate both configuration components are listed inside `GCC AI Champions`.
- Metadata/naming correct: validate display/schema names, unmanaged solution type and version.
- No accidental default-solution dependency: validate PH02-owned components are present in the governed solution and no PH02 component exists only outside it.
- Reproducible evidence: record the exact maker-portal paths, observed metadata and screenshots.

## Current result

T05 is authorized and IN PROGRESS. Validation execution remains required. T06 remains NOT STARTED and PH02-G01 remains IN PROGRESS / NOT DECIDED.
