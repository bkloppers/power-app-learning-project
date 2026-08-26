# AI Project Continuity and Phase-Tracking Flow

## Purpose

This document defines how project work must be managed across multiple ChatGPT sessions so that project phases, decisions, dependencies, completed work, open issues, and next actions are not lost between chats.

The GitHub repository is the durable source of truth. ChatGPT Project memory provides conversational continuity, but the tracked project state in GitHub remains authoritative.

## Selected Operating Model

Use one ChatGPT Project for the Power Apps project, with project-only memory enabled, and maintain a structured Project Control record in this GitHub repository.

The model has two layers:

1. **ChatGPT Project** — preserves conversations, project files, instructions, and contextual continuity across chats.
2. **GitHub Project Control** — preserves the authoritative project state, including phases, task status, decisions, blockers, dependencies, and next steps.

Project memory is useful for context. GitHub is the record that must be trusted when a new session starts.

## Repository Structure

```text
project-management/
├── AI-PROJECT-CONTINUITY-FLOW.md
├── PROJECT-CONTROL.md
├── DECISIONS.md
├── ISSUES.md
└── phases/
    ├── PHASE-01.md
    ├── PHASE-02.md
    └── ...
```

Only `AI-PROJECT-CONTINUITY-FLOW.md` is created by this change. The remaining files are the required structure for ongoing project management and should be created when tracking starts.

## ChatGPT Project Structure

Recommended chats inside the ChatGPT Project:

```text
00 - Project Manager
01 - Architecture
02 - Power Apps UI
03 - Power Automate
04 - API / Integration
05 - Agents
06 - Skills
07 - Testing
08 - Deployment
09 - Issues & Decisions
```

Each chat may focus on a different technical area, but every session must use the same authoritative Project Control state.

## Session Start Flow

At the beginning of every new project-related ChatGPT session:

1. Read `project-management/PROJECT-CONTROL.md`.
2. Identify the current project phase.
3. Identify the current active task.
4. Read all dependencies for that task.
5. Read the latest locked decisions in `project-management/DECISIONS.md` that apply to the work.
6. Check `project-management/ISSUES.md` for blockers or unresolved risks affecting the task.
7. Confirm the exact next action from Project Control before proposing implementation work.
8. Do not contradict a locked decision unless the user explicitly approves changing it.

## Work Execution Flow

For each technical task:

1. Check all required dependencies first, including screens, controls, variables, connectors, functions, data sources, environment configuration, and prior project decisions.
2. If something required is missing, identify it explicitly and include creating it within the selected implementation sequence.
3. Recommend exactly one best-practice implementation unless alternatives are explicitly requested.
4. Complete the work in the context of the current project phase and active task.
5. Do not silently move into a later project phase.
6. Do not mark a task complete merely because a formula or configuration validates.
7. Validate the task against its acceptance criteria and applicable project standards.

## Session End Flow

Before a project-related chat is considered complete, update the durable project state:

1. Record what was completed.
2. Record any new or changed decisions.
3. Record newly discovered dependencies.
4. Record blockers and unresolved issues.
5. Update the active task status.
6. Update the current project phase if its exit criteria have been met.
7. Record the exact next action.
8. Record enough implementation detail that a new ChatGPT session can continue without reconstructing the previous conversation.

## Project Control Format

`PROJECT-CONTROL.md` should use the following structure:

```text
# Project Control

Project:
Current Version:
Current Phase:
Overall Status:
Last Updated:

## Current Task
Task ID:
Task:
Status:
Owner:
Dependencies:
Acceptance Criteria:

## Last Completed

## Exact Next Step

## Phase Status

### Phase 1 - <name>
Status:
Entry Criteria:
Exit Criteria:

### Phase 2 - <name>
Status:
Entry Criteria:
Exit Criteria:

## Blockers

## Open Issues

## Locked Decisions

## Change Log
```

## Task Status Values

Use only these task states:

- `NOT STARTED`
- `READY`
- `IN PROGRESS`
- `BLOCKED`
- `VALIDATION`
- `COMPLETE`

A task may only become `COMPLETE` after its acceptance criteria have been validated.

## Decision Management

Every architectural or implementation decision that must survive future chats should receive a stable ID.

Example:

```text
DEC-001
Decision: Use responsive auto-layout containers for Canvas App structure.
Status: LOCKED
Reason: Required project implementation standard.
Date: YYYY-MM-DD
```

A locked decision remains in force until the user explicitly approves a replacement decision.

When a decision changes:

- Do not delete the previous decision.
- Mark it `SUPERSEDED`.
- Reference the new decision ID.
- Record why the decision changed.

## Issue Management

Open project issues should receive stable IDs.

Example:

```text
ISS-001
Issue: Delegation behavior not validated against production-scale data.
Status: OPEN
Severity: HIGH
Affects: Phase 7 - Testing
Required Resolution: Test the affected query with realistic data volume before release.
```

Issues must remain visible until explicitly resolved.

## Phase Management

Each project phase must define:

- objective;
- prerequisites;
- tasks;
- dependencies;
- acceptance criteria;
- blockers;
- exit criteria.

A phase must not be marked complete until all exit criteria are satisfied.

## Power Apps Project Guardrails

The project currently follows these core implementation standards:

- Descriptive and consistent names for screens, controls, variables, collections, data sources, flows, environment variables, and connection references.
- Screen-specific controls use predictable prefixes and screen suffixes where needed.
- Responsive Canvas App structure uses containers rather than fixed-position layouts.
- Each screen is treated as a page with a structured root layout and meaningful nested containers.
- Calculated and reusable values should prefer formulas or named formulas; mutable state should use variables only when state must be remembered.
- `App.OnStart` is reserved for genuine one-time startup side effects rather than becoming a general declaration area.
- Delegation, ALM, permissions, responsive behavior, accessibility, error handling, and realistic-volume testing are part of completion criteria, not optional follow-up work.

These guardrails must be reconciled against the dedicated standards and design documents already maintained for this project whenever a task touches those areas.

## ChatGPT Project Instruction

Use the following operating instruction in the ChatGPT Project:

> At the beginning of every project-related task, determine the current project phase, active task, dependencies, locked decisions, blockers, and exact next step from the authoritative project-management records in GitHub. Do not contradict a locked decision unless I explicitly approve a change. Recommend one best-practice implementation only unless I ask for alternatives. When work changes project state, update the project-management records before considering the task complete.

## Source-of-Truth Rule

When information conflicts, use this precedence:

1. Explicit instruction from the user in the current session.
2. Locked project decision recorded in GitHub.
3. Current `PROJECT-CONTROL.md` state.
4. Dedicated project standards and design documentation.
5. Prior ChatGPT conversation context.
6. General model knowledge.

This prevents an older chat or remembered discussion from silently overriding an approved project decision.

## Definition of Continuity

The continuity system is working correctly when a completely new ChatGPT session can determine, without relying on the previous chat transcript:

- what project is being worked on;
- what phase it is in;
- what has already been completed;
- what is currently in progress;
- which decisions are locked;
- which issues remain open;
- which dependencies must exist;
- what must happen next.

That is the required standard for AI-assisted project continuity.