# Power Fx — Step-by-Step Guide

Status: ACTIVE
Baseline: August 2026

## Scope

Power Fx formulas, named formulas, variables, With(), collections, user-defined functions, formula reuse, error handling and formula-state boundaries.

## Project rules

- Verify current Microsoft guidance before every lesson or implementation instruction.
- Prefer direct formulas when a value can be calculated where used.
- Use App.Formulas for reusable calculated/immutable values.
- Use With() for formula-local calculations.
- Use context variables for mutable screen-local state.
- Use global variables only for mutable state genuinely shared across screens.
- Keep collections small and purposeful; do not use them as a default substitute for querying data sources.
- Keep App.OnStart minimal.
- Record every formula exactly as implemented and validated.

## Documentation format

For every formula created or changed record:
1. Object/property or App property where the formula lives.
2. Purpose.
3. Dependencies.
4. Exact Power Fx entered.
5. Why this scope was selected.
6. Expected result.
7. Actual validated result.
8. Snapshot/evidence ID when visible in Studio.
9. Any warning, delegation issue or correction.
10. Next step.

## Current known app-state baseline

- `gblDarkMode` — mutable app-wide theme state; current project default is `true`.
- `gblSidebarOpen` — mutable app-wide navigation state; current project default is `false`.

No formula is considered canonical here until it is actually implemented and validated in the current build.
