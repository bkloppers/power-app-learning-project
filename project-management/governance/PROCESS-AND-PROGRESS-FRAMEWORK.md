# Process and Progress Framework

## Purpose

This document defines the complete delivery process used to design, build, validate, track, and advance the Power Apps learning project. It is intended to serve two purposes:

1. govern the project while the application is being designed and built;
2. provide the future operating specification for an agent-assisted workflow after the human process has been proven.

GitHub remains the durable source of truth. Chat history may provide context, but project state, gate status, decisions, issues, evidence, and next actions must be recoverable from the repository without depending on a previous conversation.

## Core Delivery Model

Every learning/build unit follows this sequence:

```text
Learning Phase
    ↓
Lab
    ↓
Demonstration
    ↓
Understanding
    ↓
Validation
    ↓
Gate Decision
    ↓
Next Phase
```

No phase advances solely because implementation work exists. A phase advances only after its acceptance criteria, validation evidence, learning outcome, and gate criteria are satisfied.

## Project Hierarchy

```text
Project
└── Phase
    └── Gate
        ├── Design Ticket
        ├── Build Ticket
        ├── Test Ticket
        ├── Documentation Ticket
        └── Validation Ticket
```

The hierarchy is cumulative. A later phase extends the same application architecture and must preserve all locked decisions and validated standards from earlier phases unless an explicitly approved decision supersedes them.

## Source-of-Truth Model

### PROJECT-CONTROL.md

Records the current operational state:

- current phase;
- current gate;
- active ticket;
- overall status;
- blockers;
- dependencies;
- last completed work;
- exact next step.

This is the first project-status document to read when resuming work.

### GitHub Issues

GitHub Issues are the operational work-management system.

Issues represent:

- gates;
- design tasks;
- implementation tasks;
- testing tasks;
- documentation tasks;
- validation tasks;
- actionable blockers and defects.

An issue must contain enough context that another engineer or future agent can understand the work without relying on the chat that created it.

### DECISIONS.md

Records durable architectural, business, security, data, UX, and process decisions.

A decision marked `LOCKED` remains authoritative until explicitly superseded.

### ISSUES.md

Records project-level unresolved risks, blockers, or design questions that must remain visible across phases.

GitHub Issues may be used to execute the work needed to resolve an item recorded in `ISSUES.md`.

### Phase Documents

Each `PHASE-XX.md` defines:

- objective;
- prerequisites;
- learning outcome;
- lab;
- demonstration;
- understanding criteria;
- gates;
- tasks;
- acceptance criteria;
- exit criteria.

### Solution Design Documents

These contain the approved solution architecture and detailed technical/business design.

They answer what the system is and how it is intended to work.

### Evidence

Evidence proves that implementation and learning outcomes were achieved.

Evidence may include:

- screenshots;
- test results;
- test data;
- validation notes;
- Power Apps Monitor evidence;
- Power Platform checker output;
- accessibility checks;
- delegation validation;
- demonstrations;
- release validation.

## Status Model

Use only these work states:

- `NOT STARTED`
- `READY`
- `IN PROGRESS`
- `BLOCKED`
- `VALIDATION`
- `COMPLETE`

### State Rules

`NOT STARTED` means prerequisites are not yet satisfied or the work is intentionally future work.

`READY` means all known dependencies exist and work may begin.

`IN PROGRESS` means active work is occurring.

`BLOCKED` means progress cannot continue until a recorded dependency, decision, access requirement, defect, or external action is resolved.

`VALIDATION` means implementation is finished but acceptance criteria and evidence are still being checked.

`COMPLETE` means all acceptance criteria have been validated and required evidence has been recorded.

Implementation alone is not sufficient for `COMPLETE`.

## Gate Model

A gate is a formal decision point between meaningful stages of the project.

Each gate must have a GitHub Issue with a title using this pattern:

`[GATE][PHxx-Gxx] <Gate Name>`

Example:

`[GATE][PH01-G01] Solution business process and scope defined`

Each gate issue must include:

- Gate ID;
- Phase;
- Objective;
- Entry criteria;
- Required tickets;
- Required evidence;
- Acceptance criteria;
- Blockers;
- Gate decision;
- Date passed;
- Links to relevant design documents, PRs, evidence, and decisions.

A gate may only be marked passed when every mandatory criterion is satisfied.

## Ticket Model

Tickets use GitHub Issues.

Recommended title pattern:

`[PHxx][Gxx][TYPE] <Task>`

Where `TYPE` is one of:

- `DESIGN`
- `BUILD`
- `TEST`
- `DOC`
- `VALIDATE`
- `BUG`
- `SECURITY`
- `DATA`
- `ALM`

Each ticket must contain:

### Context

Why the task exists and which solution capability it supports.

### Dependencies

Everything that must exist before work begins, including where applicable:

- screens;
- controls;
- components;
- formulas;
- variables;
- data sources;
- Lists;
- connectors;
- flows;
- security groups;
- environment configuration;
- prior decisions;
- other tickets.

### Selected Solution

Exactly one approved implementation direction unless alternatives were explicitly requested.

### Acceptance Criteria

Observable, testable criteria required for completion.

### Validation Evidence

Links or references to evidence proving the criteria were met.

### Outcome

What changed and any new dependency, decision, issue, or follow-up work discovered.

## Pull Request Model

Pull Requests are used to review controlled repository changes.

A PR should normally map to one gate or one coherent set of related tickets.

A PR must identify:

- linked tickets;
- linked gate;
- files changed;
- decisions introduced or changed;
- validation performed;
- unresolved items;
- impact on Project Control.

Merging a PR does not automatically mean a gate has passed.

## Learning Phase Model

Every learning phase must teach one coherent layer of the final application while adding a production-relevant capability.

Each phase contains four mandatory parts.

### 1. Learning Phase

Defines:

- what Power Apps concept is being learned;
- where it sits in the solution hierarchy;
- why the concept matters;
- dependencies;
- applicable standards;
- common implementation risks.

### 2. Lab

Adds a real part of the final app.

Labs are never isolated throwaway exercises.

### 3. Demonstration

Proves the behaviour visibly.

The demonstration must show the learner how the hierarchy level affects the working application.

### 4. Understanding

Requires the learner to explain:

- what was built;
- why it was built in that layer;
- why the selected structure is preferred;
- what would break or become difficult if the layer were misused;
- how the capability connects to earlier and later levels.

## Progress Calculation

Project progress must not be represented only by a raw percentage.

Progress is tracked through five dimensions:

1. Phase progress;
2. Gate progress;
3. Ticket progress;
4. Validation progress;
5. Learning/understanding progress.

A phase is complete only when all mandatory gates are passed.

A gate is complete only when all mandatory tickets and validation criteria are complete.

A ticket is complete only when acceptance criteria have been validated.

The project may display summary percentages for visibility, but the authoritative progress measure is gate completion.

## Session Start Process

At the start of every project session, human or agent:

1. Read `README.md`.
2. Read `AGENTS.md`.
3. Read `project-management/PROJECT-CONTROL.md`.
4. Identify the current phase.
5. Identify the current gate.
6. Identify the active ticket.
7. Read applicable locked decisions.
8. Read applicable project issues/blockers.
9. Read the active phase document.
10. Read the relevant solution-design and standards documents.
11. Check all task dependencies.
12. Confirm the exact next action before changing anything.

No implementation work should start before this context is established.

## Work Execution Process

For each active ticket:

1. Validate prerequisites.
2. Identify missing dependencies.
3. Add creation of missing dependencies into the selected solution sequence.
4. Execute exactly the approved ticket scope.
5. Preserve existing standards and locked decisions.
6. Record new decisions when durable choices are made.
7. Record new issues when unresolved risks or blockers are discovered.
8. Create or update implementation/design artifacts.
9. Test the work against acceptance criteria.
10. Move the ticket to `VALIDATION`.
11. Capture validation evidence.
12. Move to `COMPLETE` only when all criteria pass.
13. Update the parent gate status.
14. Update Project Control.

## Gate Review Process

When all required gate tickets are complete:

1. Review gate entry and acceptance criteria.
2. Verify all required evidence exists.
3. Confirm unresolved issues do not violate gate criteria.
4. Confirm no required dependency is missing.
5. Confirm applicable design documents are current.
6. Confirm Project Control reflects reality.
7. Record the gate decision.
8. If passed, close the gate and activate the next gate or phase.
9. If not passed, create the required corrective tickets and leave the gate open.

## Phase Exit Process

A phase exits only when:

- all mandatory gates are passed;
- all phase acceptance criteria are validated;
- the Lab is complete;
- the Demonstration has been performed;
- Understanding criteria are satisfied;
- design documentation reflects the implementation;
- decisions are recorded;
- blockers are resolved or explicitly accepted;
- Project Control identifies the next phase and exact next action.

## Application Delivery Lifecycle

The end-to-end application lifecycle follows this model:

```text
Business Need
    ↓
Requirements
    ↓
Architecture
    ↓
Learning / Build Roadmap
    ↓
Phase
    ↓
Gate
    ↓
Design Ticket(s)
    ↓
Build Ticket(s)
    ↓
Test Ticket(s)
    ↓
Demonstration
    ↓
Understanding Validation
    ↓
Gate Review
    ↓
Next Gate / Phase
    ↓
Integrated Testing
    ↓
Security Validation
    ↓
User Acceptance
    ↓
Release Readiness
    ↓
Deployment
    ↓
Operational Review
```

## Change-Control Process

When a new requirement appears:

1. Capture the requirement.
2. Determine whether it changes scope, architecture, data, security, UX, or process.
3. Record any required decision.
4. Identify affected phase/gate/tickets.
5. Update design documents before implementation where appropriate.
6. Create new or revised tickets.
7. Do not silently change completed work without traceability.

When a locked decision changes:

1. retain the previous decision;
2. mark it `SUPERSEDED`;
3. create a new decision ID;
4. reference the old decision;
5. record the reason;
6. identify affected gates/tickets;
7. revalidate affected work where required.

## Defect Process

A defect must record:

- observed behaviour;
- expected behaviour;
- affected phase/gate;
- severity;
- reproduction steps;
- dependencies;
- fix ticket;
- validation evidence.

A defect discovered during gate validation prevents gate passage when it violates acceptance criteria.

## Risk and Blocker Process

A blocker must state:

- what cannot proceed;
- why;
- owner/action required;
- affected tickets;
- affected gate;
- resolution criteria.

No agent should work around a blocked requirement by silently redesigning the solution.

## Documentation Synchronization Rule

Whenever implementation or business design changes, determine whether these artifacts also require updates:

- Solution Design;
- Tool Design;
- Phase document;
- Gate issue;
- Ticket;
- Decisions;
- Issues;
- Project Control;
- Evidence;
- AGENTS instructions.

A task is not fully complete when the repository describes a different system than the application that was built.

## Human Approval Boundaries

Future automation must preserve explicit human control over high-impact decisions.

Human approval is required for:

- changing project scope;
- changing a locked decision;
- passing a major gate where business acceptance is required;
- changing security architecture;
- changing production data permissions;
- rejecting or removing business functionality;
- production deployment approval;
- destructive administrative actions where required by the application process.

Agents may prepare recommendations, evidence, proposed changes, and tickets, but must not silently replace required human decisions.

## Future Agent Workflow Model

The future agent system should be built around the proven process rather than inventing a separate automation model.

The target logical agent workflow is:

```text
Project Manager Agent
    ↓
Reads Project Control + Gate + Tickets
    ↓
Determines next eligible work
    ↓
Routes to Specialist Agent
    ├── Architecture Agent
    ├── Power Apps Agent
    ├── Data / Lists Agent
    ├── Security Agent
    ├── Power Automate Agent
    ├── AI / Chatbot Agent
    ├── Testing Agent
    └── Documentation Agent
    ↓
Specialist performs scoped task
    ↓
Validation Agent checks acceptance criteria
    ↓
Evidence recorded
    ↓
Project Manager Agent updates progress
    ↓
Human approval when required
    ↓
Gate passes or corrective ticket created
```

## Agent Contract

Every future agent should receive the same minimum work packet:

- project;
- phase;
- gate;
- ticket ID;
- objective;
- dependencies;
- locked decisions;
- applicable standards;
- selected solution;
- allowed scope;
- acceptance criteria;
- required evidence;
- prohibited changes;
- output location;
- exact handoff condition.

This prevents agents from independently redefining the project architecture.

## Agent Handoff Format

Every agent handoff should return:

- Ticket ID;
- Status;
- Work completed;
- Files/artifacts changed;
- Validation performed;
- Evidence produced;
- Decisions created or affected;
- Issues/blockers created or affected;
- Dependencies discovered;
- Acceptance criteria result;
- Exact recommended next action.

The next agent must be able to continue without reading the previous agent's private reasoning or chat transcript.

## Agent Routing Rules

An orchestrating agent must not assign a ticket until its dependencies are satisfied.

If dependencies are missing:

- mark or keep the ticket `BLOCKED` or `NOT STARTED` as appropriate;
- identify the missing dependency;
- create or activate the dependency ticket;
- do not redesign the target ticket to avoid the dependency.

If a task crosses specialist boundaries, the Project Manager Agent should split it into linked tickets rather than allow multiple agents to make overlapping uncontrolled changes.

## Agent Validation Rule

The agent that performs implementation should not be treated as the sole authority that its work is complete.

Completion should be validated against explicit acceptance criteria by a validation step or separate validation role where practical.

This mirrors the application's own verifier model and prevents self-certification from replacing evidence.

## Agent Escalation Rules

Escalate to a human when:

- a locked decision must change;
- requirements conflict;
- security impact is uncertain;
- required access cannot be obtained;
- acceptance criteria are ambiguous;
- business process meaning is unclear;
- destructive action is proposed;
- a gate requires business approval;
- multiple technically valid solutions require a business trade-off.

## Auditability Requirement

The future workflow must make it possible to reconstruct:

- who or what performed work;
- when it occurred;
- which ticket authorized it;
- which decision governed it;
- what changed;
- what evidence was produced;
- who validated it;
- why a gate passed;
- who approved required human decisions.

GitHub issue history, commits, PRs, project documents, and evidence are the primary audit trail.

## Initial Application Context

The current confirmed solution consists of:

- one Microsoft Teams-hosted Power Apps Canvas App;
- one reusable multi-tool application shell;
- Tool 01: AI Prompt Capture, Submission and Verification;
- Tool 02: AI Prompt Chatbot;
- future tools added under the same shell;
- Microsoft Lists as the initial Tool 01 data platform;
- submitter, peer rater, verifier, and administrator process roles;
- multi-step prompt submission rather than a single long scrolling form;
- completion/progress visualization;
- optional pre-submission peer rating;
- formal verification requiring at least two independent verifiers;
- changes returned to the submitter and resubmitted for verification;
- completion requiring successful testing, a future-defined score threshold, and verifier agreement;
- rejection authority reserved for administrators.

Detailed architecture remains governed by the solution-design documents and applicable locked decisions.

## Process Definition of Done

The project process is considered sufficiently mature for agent automation when:

1. the full application learning/build roadmap has been executed or proven through enough phases to validate the process;
2. gate criteria consistently produce clear pass/fail decisions;
3. tickets contain enough context for independent execution;
4. dependencies are explicitly tracked;
5. acceptance criteria are objective enough for validation;
6. evidence requirements are repeatable;
7. human approval boundaries are known;
8. handoff records allow a new session/agent to continue reliably;
9. project documents stay synchronized with implementation;
10. recurring manual coordination steps can be safely expressed as deterministic agent-routing rules.

At that point this document becomes the source specification for designing the agent orchestration workflow.
