# Power Platform Studio and Documentation Verification Rules

Status: GOVERNING PROJECT RULE
Baseline: August 2026

## Canonical documentation location

All current step-by-step Power Platform documentation lives under:

`docs/power-platform/`

Before providing any lesson, click path, formula, component instruction, admin instruction, configuration step or version-sensitive recommendation:

1. Read `docs/power-platform/README-RULES.md`.
2. Read `docs/power-platform/INDEX.md`.
3. Read the active area's `README.md`.
4. Verify the instruction against current Microsoft guidance applicable in August 2026 or later.
5. Check whether a user snapshot already proves the current UI.
6. Prefer the observed live project UI for the exact tenant click path when it differs from stale remembered UI, while recording the discrepancy.
7. Never rely on model memory alone for version-sensitive Power Platform guidance.

## Snapshot rule

Every user-provided Power Platform screenshot is project evidence. Record it in the active area's guide, not in a detached screenshot dump.

Record at minimum:
- snapshot ID;
- date/session;
- product area;
- environment/resource;
- exact screen/editor;
- selected object;
- visible menus/options/properties relevant to the step;
- exact working path proved;
- values/formulas visible or entered;
- correction to earlier guidance if applicable;
- proven result;
- next verified step.

Use `docs/power-platform/README-SNAPSHOT-TEMPLATE.md` as the recording format.

## No repeated rediscovery

Once a menu, path, option or product behavior is verified and recorded, use the documented baseline. Do not ask the user for another screenshot merely to rediscover the same UI unless there is evidence the product changed or the state is genuinely ambiguous.

## Correction rule

If a snapshot disproves prior guidance:
1. acknowledge the mismatch;
2. stop using the stale path;
3. verify current Microsoft guidance;
4. record the observed UI and corrected sequence in the active area guide;
5. issue one corrected best-practice sequence only.

## Architecture rules

- Reusable-first: coherent reusable visual/interaction patterns belong in the approved Component Library.
- Responsive-first: new Canvas Apps use the current Responsive experience and container-driven composition.
- Branding: use approved project design sources; do not invent branding values.
- Power Fx: document exact formulas where they are implemented and validated.
- Security: UI visibility is not authorization.

## Required agent check

Before answering a Power Platform implementation question, confirm internally:
- current area;
- current guide;
- current August 2026-or-later Microsoft guidance;
- existing snapshot evidence;
- dependencies;
- one selected best-practice sequence.

If any required element is missing, resolve it before instructing the user.
