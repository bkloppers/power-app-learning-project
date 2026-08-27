# GitHub Gate and Ticket Tracking Model

## Selected Tracking Model

GitHub Issues are the operational ticket system for project work and phase gates.

`project-management/PROJECT-CONTROL.md` remains the high-level authoritative project status page and must point to the currently active phase, active gate, active ticket, blockers, and exact next step.

## Tracking Hierarchy

```text
Project
└── Phase
    ├── Gate
    │   ├── Work Ticket
    │   ├── Work Ticket
    │   └── Validation Ticket
    └── Gate
        ├── Work Ticket
        └── Validation Ticket
```

## Phase

A Phase represents a learning/build stage in the cumulative Power Apps programme.

Each phase retains its durable design and acceptance criteria in `project-management/phases/PHASE-XX.md`.

A phase may contain one or more gates.

## Gate

A Gate is a formal checkpoint that must be passed before the project may advance.

Each gate is tracked by a GitHub Issue and must contain:

- Gate ID;
- phase;
- objective;
- dependencies;
- required evidence;
- acceptance criteria checklist;
- linked implementation/work tickets;
- blockers;
- validation result;
- final gate status.

A gate may not be closed merely because implementation work is finished. Its acceptance criteria and required evidence must be validated first.

## Work Ticket

Each meaningful unit of implementation, design, testing, or documentation is tracked as a GitHub Issue.

Each work ticket must contain:

- Ticket ID / issue number;
- phase and gate;
- task description;
- dependencies;
- one selected implementation approach;
- acceptance criteria;
- evidence required;
- status;
- links to relevant design documents, commits, pull requests, screenshots, or test evidence.

## Gate Closure Rule

A Gate can close only when:

1. all required work tickets are complete;
2. all gate acceptance criteria are satisfied;
3. required demonstration/evidence exists;
4. blockers affecting the gate are resolved or explicitly accepted;
5. the Learning Phase -> Lab -> Demonstration -> Understanding criteria for that gate are satisfied;
6. `PROJECT-CONTROL.md` is updated with the result and exact next step.

## Source-of-Truth Responsibilities

### GitHub Issues

Operational work tracking:

- gates;
- tasks;
- validation work;
- blockers requiring action;
- ownership and progress.

### `PROJECT-CONTROL.md`

Executive project state:

- current phase;
- current gate;
- active ticket;
- overall status;
- blockers;
- exact next step.

### `DECISIONS.md`

Durable architectural and business decisions.

### `project-management/phases/PHASE-XX.md`

Phase objectives, learning outcomes, lab, demonstration, understanding, dependencies, acceptance criteria, and exit criteria.

### Solution Design Documents

Approved architecture, process, data, security, UX, and tool requirements.

## Ticket Naming Standard

Use concise issue titles in the form:

```text
[PH01][G01] Define Tool 01 workflow states
[PH01][G01] Confirm verifier completion rules
[PH02][G01] Create solution and publisher
[PH02][G02] Validate application shell hierarchy
```

Gate issues use:

```text
[GATE][PH01-G01] Business process defined
[GATE][PH02-G01] Solution foundation approved
```

## Labels

Use labels consistently:

- `type:gate`
- `type:design`
- `type:build`
- `type:test`
- `type:documentation`
- `status:blocked`
- `priority:high`
- `tool:01-prompt-submission`
- `tool:02-ai-prompt-chatbot`
- `shared:app-shell`

Phase is encoded in the issue title and linked from Project Control so a large custom phase-label set is not required.

## Pull Request Relationship

Implementation changes are made through branches and pull requests.

A pull request must reference the GitHub Issue(s) it implements or validates. Closing a pull request does not automatically mean a gate has passed; gate closure still requires acceptance validation.

## Current Project Application

For Phase 01, the first operational gate should be:

`[GATE][PH01-G01] Solution business process and scope defined`

Its work tickets should cover:

- Tool 01 business requirements;
- Tool 01 workflow/status model;
- peer-rating stage;
- formal verifier rules;
- admin rejection rules;
- Tool 02 architectural dependency;
- unresolved score/testing completion rules;
- hierarchy learning map;
- initial architecture approval.

The gate closes only when Phase 01 exit criteria are met and the project is ready to enter Phase 02.
