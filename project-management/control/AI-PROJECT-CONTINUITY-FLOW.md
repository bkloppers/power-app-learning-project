# AI Project Continuity and Phase-Tracking Flow

## Purpose

This document defines how project work must be managed across multiple ChatGPT sessions so that project phases, decisions, dependencies, completed work, open issues and next actions are not lost between chats.

The GitHub repository is the durable source of truth. ChatGPT Project memory can provide conversational continuity, but tracked GitHub state remains authoritative.

## Selected Operating Model

Use one ChatGPT Project for the Power Apps project and maintain durable project state in this GitHub repository.

The model has two layers:

1. **ChatGPT Project** — conversational context, project files and instructions.
2. **GitHub Operational Control** — authoritative workflow state, decisions, evidence, blockers, dependencies and next actions.

## Repository Structure

```text
project-management/
├── control/
│   ├── AI-PROJECT-CONTINUITY-FLOW.md
│   └── PROJECT-CONTROL.md
├── governance/
│   ├── GITHUB-OPERATIONAL-CONTROL-STANDARD.md
│   ├── PROCESS-AND-PROGRESS-FRAMEWORK.md
│   ├── GATE-TRACKING-MODEL.md
│   ├── CHAT-SESSION-TICKET-CAPACITY-MODEL.md
│   └── PHASE-FOLDER-STANDARD.md
├── planning/
│   └── PROJECT-OPERATIONAL-DELIVERY-PLAN.md
├── registers/
│   ├── DECISIONS.md
│   ├── ISSUES.md
│   ├── APPROVALS.md
│   └── approvals/
└── phases/
    └── PHxx/
        ├── PHASE-xx.md
        ├── gates/
        ├── evidence/
        ├── approvals/
        └── handoffs/
```

Solution architecture, implementation standards and solution-design documentation live under `docs/`.

## Session Start Flow

At the beginning of every project-related session:

1. Read `README.md` and `AGENTS.md`.
2. Read `project-management/control/PROJECT-CONTROL.md`.
3. Read the current gate GitHub Issue.
4. Read the active/next ticket GitHub Issue.
5. Read applicable locked decisions in `project-management/registers/DECISIONS.md`.
6. Check `project-management/registers/ISSUES.md` for relevant unresolved cross-cutting issues.
7. Read the active phase specification.
8. Read only the governance, architecture, technical standards and evidence relevant to the current ticket.
9. Confirm the exact next action before proposing implementation work.

## Work Execution Flow

For each technical task:

1. Check all required dependencies first, including screens, controls, variables, connectors, functions, data sources, environment configuration and prior project decisions.
2. If something required is missing, identify it explicitly and include creating it within the selected implementation sequence.
3. Recommend exactly one best-practice implementation unless alternatives are explicitly requested.
4. Complete the work in the context of the current project phase and active ticket.
5. Do not silently move into a later project phase.
6. Do not mark a ticket complete merely because a formula or configuration validates.
7. Validate against the ticket acceptance criteria and applicable project standards.
8. Record durable evidence at the canonical phase-owned path.

## Session End Flow

Before project-changing work is considered complete:

1. Record validation and evidence.
2. Update the live ticket/gate GitHub Issue state as authorized.
3. Record any new or changed durable decision in `project-management/registers/DECISIONS.md`.
4. Record unresolved cross-cutting issues in `project-management/registers/ISSUES.md`.
5. Merge repository changes through the governed Pull Request process when required.
6. Synchronize `project-management/control/PROJECT-CONTROL.md` from live GitHub state.
7. Record the exact next action.

## Task Status Values

Use only these operational task states:

- `NOT STARTED`
- `READY`
- `IN PROGRESS`
- `BLOCKED`
- `VALIDATION`
- `COMPLETE`

A ticket may only become `COMPLETE` after its acceptance criteria and evidence have been validated.

## Decision Management

Every architectural or implementation decision that must survive future chats should receive a stable ID such as `DEC-001`. A locked decision remains in force until the user explicitly approves a replacement. When superseding a decision, retain the prior record, mark it `SUPERSEDED`, reference the replacement and record why it changed.

## Issue Management

Durable cross-cutting project issues receive stable IDs such as `ISS-001` and live in `project-management/registers/ISSUES.md`. Operational gate/ticket work remains in GitHub Issues and must not be duplicated as a second workflow database in Markdown.

## Phase Management

Every phase owns its specification, gate artifacts, evidence, approvals and handoffs under `project-management/phases/PHxx/`. A phase must not be marked complete until its gate criteria are satisfied and the formal gate decision is recorded.

## Source-of-Truth Rule

When information conflicts, use this precedence:

1. Explicit instruction from the user in the current session.
2. Locked decision in `project-management/registers/DECISIONS.md`.
3. Live GitHub gate/ticket Issue state.
4. `project-management/control/PROJECT-CONTROL.md` as the derived snapshot.
5. Applicable project standards and design documentation.
6. Prior conversation context.
7. General model knowledge.

## Definition of Continuity

The continuity system is working correctly when a new session can determine, without the prior transcript:

- what project is being worked on;
- what phase and gate are active;
- which ticket is active/next;
- what is complete and blocked;
- which decisions are locked;
- which issues remain open;
- which dependencies and standards apply;
- what evidence exists;
- what must happen next.
