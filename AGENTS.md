# Agent Instructions

This file defines how AI agents must operate in this repository. Read it before making project changes.

## Repository Role

This repository is the durable source of truth for the Power Apps project. Chat history and model memory may provide useful context, but they do not override the tracked project state and locked decisions stored here.

## Required Reading Order

Before changing implementation or project state, read these files in order when they exist:

1. `README.md`
2. `AGENTS.md`
3. `project-management/AI-PROJECT-CONTINUITY-FLOW.md`
4. `project-management/PROJECT-CONTROL.md`
5. `project-management/DECISIONS.md`
6. `project-management/ISSUES.md`
7. The active phase file under `project-management/phases/`
8. Any dedicated technical, naming, variable, responsive-layout, design-system, or architecture document that applies to the task.

If one of the project-management files does not yet exist, do not invent its contents. Create it only when the task requires project tracking to begin or the user explicitly requests it.

## Source-of-Truth Precedence

When information conflicts, use this order:

1. Explicit user instruction in the current session.
2. Locked decisions in `project-management/DECISIONS.md`.
3. Current state in `project-management/PROJECT-CONTROL.md`.
4. Applicable project standards and design documentation.
5. Prior chat or agent context.
6. General model knowledge.

Do not silently override a higher-priority source.

## Required Agent Behaviour

For every technical task:

1. Determine the current phase and active task before proposing implementation work.
2. Check all dependencies first, including screens, controls, variables, connectors, functions, data sources, environments, and prior decisions.
3. Recommend exactly one best-practice implementation unless the user explicitly asks for alternatives.
4. If a required dependency is missing, state exactly what is missing and include its creation in the selected implementation sequence.
5. Do not redesign the selected solution merely because a dependency is missing.
6. Respect locked decisions. A locked decision may only be replaced after explicit user approval.
7. Do not silently advance to another project phase.
8. Do not mark work complete because code, Power Fx, YAML, or configuration merely validates.
9. Validate against the task's acceptance criteria and applicable project standards.
10. Record durable project-state changes before considering project-management work complete.

## Session Start Requirement

At the start of project work, establish:

- current project phase;
- active task and status;
- dependencies;
- locked decisions relevant to the task;
- open blockers and issues;
- acceptance criteria;
- exact next step.

If those records exist in GitHub, use them rather than reconstructing state from conversation history.

## Session End Requirement

When the work changes project state, update the relevant project-management records with:

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

- descriptive, predictable naming for screens, controls, variables, collections, data sources, flows, environment variables, and connection references;
- responsive, container-based Canvas App layouts rather than fixed-position screen designs;
- structured screen roots and meaningful nested layout containers;
- formulas and named formulas for calculated/reusable values where appropriate;
- mutable variables only for state that must be remembered;
- minimal `App.OnStart`, reserved for genuine one-time side effects;
- delegation-safe data access for production-scale datasets;
- security enforced in the data/platform layer rather than through UI visibility alone;
- solution-first ALM, environment variables, connection references, and controlled deployments;
- accessibility, error handling, realistic-volume testing, and validation as part of completion criteria;
- project design-system and brand rules whenever UI work is involved.

Do not replace a project-specific standard with a generic Power Apps convention when a repository standard already exists.

## Decision Discipline

Use stable IDs for durable decisions, for example `DEC-001`.

A decision marked `LOCKED` remains active until the user explicitly approves a replacement. When superseding a decision, retain the original record, mark it `SUPERSEDED`, and reference the replacement decision.

## Issue Discipline

Use stable IDs for tracked issues, for example `ISS-001`.

Do not remove unresolved issues merely because the current task works around them. Close an issue only when its required resolution has been validated.

## Completion Standard

Another agent opening this repository should be able to determine without prior chat history:

- what the project is;
- which phase is active;
- what is complete;
- what is in progress;
- what is blocked;
- which decisions are locked;
- what standards apply;
- what must happen next.

If the repository cannot answer those questions, project continuity is incomplete.
