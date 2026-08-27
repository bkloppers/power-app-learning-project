# Power Apps Studio Verification Rules

Status: GOVERNING PROJECT RULE
Baseline: August 2026

## Rule 1 — Verify before teaching or instructing

Before providing any Power Apps lesson, click path, implementation step, formula, component instruction, property instruction, control setup, configuration instruction or version-sensitive recommendation, verify that it matches the latest current Microsoft Power Apps / Power Platform guidance applicable in August 2026 or later.

Do not rely on model memory alone for version-sensitive Power Apps guidance.

## Rule 2 — Live observed UI is project evidence

Every user-provided Power Apps screenshot is project evidence.

The agent must inspect it, record the relevant UI facts in `docs/standards/POWER-APPS-2026-STUDIO-HOW-TO-GUIDE.md`, and use those observations in future instructions.

## Rule 3 — Record snapshots in the active section

Do not maintain a detached screenshot dump. Record each snapshot in the guide section corresponding to the task currently being performed, including menu options, selected object, visible properties, working path, corrections, proven completion state and next validated step.

## Rule 4 — Do not make the user rediscover the same UI

Once a menu, panel, command or working click path is verified and recorded, use that recorded baseline. Do not ask the user for another screenshot merely to rediscover information already established unless there is evidence the UI changed or the current state is ambiguous.

## Rule 5 — Correct stale instructions immediately

If a screenshot disproves prior guidance:

1. acknowledge the mismatch;
2. stop using the stale path;
3. verify current Microsoft guidance;
4. update the How-To Guide in the same active section;
5. issue one corrected best-practice sequence only.

## Rule 6 — Reusable-first architecture

Before building app-specific UI, check whether the object or pattern should be reusable across apps.

If a coherent visual or interaction pattern is reusable, build it in the approved Component Library and expose explicit component contracts through supported custom properties.

Do not create hidden component dependencies on consuming-app globals, collections, controls or app-specific data sources.

Do not turn arbitrary single controls into components merely to maximize component count. Reuse must represent a coherent visual or interaction unit.

## Rule 7 — Responsive-first application baseline

New Canvas Apps in this project must use the current Responsive app experience and responsive/container-driven composition. Do not introduce Tablet-first or Phone-first fixed-canvas guidance unless the user explicitly changes the project requirement.

## Rule 8 — Branding must come from project sources

Reusable components must use the approved project branding sources, including `DESIGN.md` and related project design references. Do not invent colors, typography, logo variants, spacing or brand behavior.

## Rule 9 — Distinguish observed facts from inference

The guide must clearly distinguish:

- what the screenshot directly proves;
- what Microsoft documentation confirms;
- what the next implementation step is.

Do not write inferred UI behavior as though it was observed.

## Rule 10 — Update before proceeding

When a new screenshot materially changes or expands the known Studio UI, update the How-To Guide before giving the next implementation instruction whenever repository access permits.

If repository protection temporarily prevents the update, state that explicitly and do not pretend the guide is already synchronized.

## Required agent check

Before answering a Power Apps implementation question, an agent must ask internally:

1. Is this version-sensitive?
2. Did I verify current August 2026-or-later Microsoft guidance?
3. Has the user already shown this UI in a snapshot?
4. What does the How-To Guide currently record?
5. Does the instruction preserve the reusable-first, responsive-first and branding rules?

If any required answer is missing, resolve it before giving the instruction.
