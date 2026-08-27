# Agent Instructions

This file defines how AI agents must operate in this repository. Read it before making project changes.

## Repository Role

This repository is the durable source of truth for the Power Apps project. Chat history and model memory may provide useful context, but they do not override the tracked project state and locked decisions stored here.

## Repository Layers

Use these ownership boundaries:

- `.github/` — GitHub-native workflow controls, Issue forms, PR template and automation.
- `docs/` — solution architecture, technical standards and solution-design documentation.
- `project-management/control/` — current project snapshot and AI continuity process.
- `project-management/governance/` — rules governing how project work is executed and controlled.
- `project-management/planning/` — cross-phase plans and roadmaps.
- `project-management/registers/` — durable project-wide decisions, issues and approvals.
- `project-management/phases/PHxx/` — phase-owned specifications, gates, evidence, approvals and handoffs.
- `scripts/` — repository validation and support automation.

## Required Reading Order

Before changing implementation or project state, read these files/resources in order when they exist:

1. `README.md`
2. `AGENTS.md`
3. `project-management/control/PROJECT-CONTROL.md`
4. Current gate GitHub Issue.
5. Active/next ticket GitHub Issue.
6. `project-management/registers/DECISIONS.md`
7. `project-management/registers/ISSUES.md`
8. The active phase file at `project-management/phases/PHxx/PHASE-xx.md`.
9. `docs/standards/POWER-APPS-STUDIO-VERIFICATION-RULES.md` before any Power Apps lesson or implementation instruction.
10. `docs/standards/POWER-APPS-2026-STUDIO-HOW-TO-GUIDE.md` before giving any Maker Portal or Studio click path.
11. Only the additional technical, naming, variable, responsive-layout, design-system, architecture or governance documents relevant to the current task.

For governance work, also read `project-management/governance/GITHUB-OPERATIONAL-CONTROL-STANDARD.md` and any other applicable governance standard. For cross-session continuity questions, read `project-management/control/AI-PROJECT-CONTINUITY-FLOW.md`.

If one of these files does not yet exist, do not invent its contents. Create it only when the task requires it or the user explicitly authorizes it.

## Source-of-Truth Precedence

When information conflicts, use this order:

1. Explicit user instruction in the current session.
2. Locked decisions in `project-management/registers/DECISIONS.md`.
3. Live GitHub gate/ticket Issue state for operational workflow status.
4. `project-management/control/PROJECT-CONTROL.md` as the derived project snapshot.
5. Applicable project standards and design documentation.
6. Prior chat or agent context.
7. General model knowledge.

If live GitHub Issue state conflicts with Project Control, stop execution and reconcile the discrepancy before advancing work. Do not silently override a higher-priority source.

## GitHub Operational Control

All agents must comply with `project-management/governance/GITHUB-OPERATIONAL-CONTROL-STANDARD.md`.

- GitHub Issues are the transactional source of truth for gate/ticket state.
- Pull Requests are the controlled repository-change boundary.
- Evidence proves completion.
- `project-management/control/PROJECT-CONTROL.md` summarizes live state; it does not independently advance a ticket or gate.
- A merged PR does not by itself complete a ticket or pass a gate.
- Repository-changing ticket work uses one working branch per active ticket unless an approved governance change explicitly applies across phases.

## Phase Artifact Placement

Every phase-specific artifact must live inside its canonical phase folder under `project-management/phases/PHxx/` and comply with `project-management/governance/PHASE-FOLDER-STANDARD.md`.

Do not create phase-specific evidence, gate packages, screenshots, approvals, handoffs or phase documents in shared project-management folders. Shared locations are reserved for artifacts that genuinely govern multiple phases or the whole project.

When moving or creating a phase artifact, update all known repository references in the same change and do not leave duplicate compatibility copies behind.

## Required Agent Behaviour

For every technical task:

1. Determine the current phase and active ticket from GitHub operational state before proposing implementation work.
2. Check all dependencies first, including screens, controls, variables, connectors, functions, data sources, environments and prior decisions.
3. Recommend exactly one best-practice implementation unless the user explicitly asks for alternatives.
4. If a required dependency is missing, state exactly what is missing and include its creation in the selected implementation sequence.
5. Do not redesign the selected solution merely because a dependency is missing.
6. Respect locked decisions. A locked decision may only be replaced after explicit user approval.
7. Do not silently advance to another project phase.
8. Do not mark work complete because code, Power Fx, YAML or configuration merely validates.
9. Validate against the ticket's acceptance criteria and applicable project standards.
10. Record durable evidence and synchronize GitHub operational state before considering work complete.

## Mandatory August 2026 Power Apps Verification

Before providing the user with any Power Apps lesson, click path, formula, component instruction, control setup, property configuration, Maker Portal instruction, Studio instruction or version-sensitive recommendation:

1. Verify the guidance against current Microsoft Power Apps / Power Platform guidance applicable in August 2026 or later.
2. Read `docs/standards/POWER-APPS-STUDIO-VERIFICATION-RULES.md`.
3. Read the relevant section of `docs/standards/POWER-APPS-2026-STUDIO-HOW-TO-GUIDE.md`.
4. Check whether the user has already supplied a snapshot that proves the current UI.
5. Prefer the live observed project UI for the exact click path when it differs from stale remembered UI, while recording the discrepancy with current Microsoft guidance.
6. Never rely on general model memory alone for a version-sensitive Power Apps instruction.

Every Power Apps screenshot uploaded by the user must be treated as project evidence. Record its relevant contents in the active section of the How-To Guide before proceeding when repository access permits. Do not force the user to repeatedly supply screenshots to rediscover menus already recorded.

## Session Start Requirement

At the start of project work, establish:

- current project phase;
- current gate Issue;
- active/next ticket Issue and status;
- dependencies;
- locked decisions relevant to the task;
- open blockers and issues;
- acceptance criteria;
- exact next step.

If those records exist in GitHub, use them rather than reconstructing state from conversation history.

## Session End Requirement

When work changes project state, update the relevant GitHub Issue/PR/evidence records and then synchronize `project-management/control/PROJECT-CONTROL.md` with:

- completed work;
- task status;
- new or changed dependencies;
- approved decisions;
- blockers or issues;
- validation results;
- current phase status;
- exact next action.

Record enough detail that another agent can continue in a new session without needing the previous transcript.

## Power Apps Guardrails

Agents working on the Power Apps implementation must preserve these project standards:

- descriptive, predictable naming for screens, controls, variables, collections, data sources, flows, environment variables and connection references;
- reusable-first architecture: coherent reusable visual/interaction patterns belong in the approved Component Library rather than being duplicated across apps;
- responsive-first Canvas App creation using the current Responsive experience, not a Tablet-first or Phone-first baseline;
- responsive, container-based Canvas App layouts rather than fixed-position screen designs;
- structured screen roots and meaningful nested layout containers;
- formulas and named formulas for calculated/reusable values where appropriate;
- mutable variables only for state that must be remembered;
- minimal `App.OnStart`, reserved for genuine one-time side effects;
- delegation-safe data access for production-scale datasets;
- security enforced in the data/platform layer rather than through UI visibility alone;
- solution-first ALM, environment variables, connection references and controlled deployments;
- accessibility, error handling, realistic-volume testing and validation as part of completion criteria;
- project design-system and brand rules whenever UI work is involved.

Do not replace a project-specific standard with a generic Power Apps convention when a repository standard already exists.

## Decision Discipline

Use stable IDs for durable decisions, for example `DEC-001`.

A decision marked `LOCKED` remains active until the user explicitly approves a replacement. When superseding a decision, retain the original record, mark it `SUPERSEDED`, and reference the replacement decision.

## Issue Discipline

Use stable IDs for durable project issues, for example `ISS-001`.

Do not remove unresolved issues merely because the current task works around them. Close an issue only when its required resolution has been validated.

Operational gate/ticket Issues use the canonical IDs defined by their phase/gate/ticket, for example `PH02-G01` and `PH02-G01-T03`.

## Completion Standard

Another agent opening this repository should be able to determine without prior chat history:

- what the project is;
- which phase is active;
- which gate Issue controls the phase;
- which ticket Issue is active/next;
- what is complete;
- what is blocked;
- which decisions are locked;
- what standards apply;
- what evidence exists;
- what must happen next.

If the repository and live GitHub operational records cannot answer those questions consistently, project continuity is incomplete.
