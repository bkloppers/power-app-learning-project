# Chat Session and Ticket Capacity Model

## Purpose

This document defines how GitHub tickets are grouped into ChatGPT work sessions so that project work remains traceable, focused, resumable, and suitable for future agent orchestration.

A GitHub ticket is the unit of accountable work. A chat session is a temporary execution workspace that may complete one or more closely related tickets.

The model deliberately avoids one-chat-per-ticket because that would create excessive session fragmentation. It also avoids placing an entire phase into one uncontrolled chat because that would make scope, validation, handoff, and context difficult to manage.

## Selected Operating Model

Use persistent specialist chat workstreams, but create a **Session Batch** for each coherent unit of execution.

A Session Batch may contain multiple tickets only when they:

- belong to the same project phase;
- belong to the same gate;
- belong to the same specialist workstream;
- share a coherent implementation context;
- can be validated without requiring a different specialist discipline first;
- fit within the session capacity defined below.

Only one ticket is considered the **Active Ticket** at a time inside the session. Additional tickets in the batch are queued and may start only after the active ticket reaches its required handoff state.

## Chat Workstreams

Use these persistent chat categories for the project:

```text
00 - Project Manager
01 - Architecture and Solution Design
02 - Power Apps Build
03 - Data and Microsoft Lists
04 - Security and Permissions
05 - Power Automate and Integration
06 - AI and Chatbot
07 - Testing and Validation
08 - Deployment and ALM
09 - Issues, Decisions and Cross-Cutting Review
```

A workstream chat may span many sessions over the life of the project. Chat identity does not determine project state; GitHub remains authoritative.

## Session Batch Identifier

Every execution session should be identifiable using this format:

`SES-PHxx-Gxx-<WORKSTREAM>-nn`

Example:

`SES-PH11-G01-POWERAPPS-01`

The session identifier should be referenced in ticket outcomes or Project Control when useful for auditability.

## Ticket Size Model

Each ticket receives a session-effort size before it is placed into a Session Batch.

### Small - 1 point

A small ticket has narrow scope, few dependencies, and one clear validation path.

Typical examples:

- rename or create a defined control/component;
- add one already-designed formula;
- add one field/column to an approved data design;
- document one approved decision;
- execute one narrow validation check.

### Medium - 2 points

A medium ticket changes one coherent capability and requires several related implementation or validation steps.

Typical examples:

- build one wizard step;
- create one responsive screen structure;
- configure one Microsoft List from an approved schema;
- implement one role-aware navigation rule;
- create and test one Power Automate notification flow.

### Large - 3 points

A large ticket implements a substantial capability with several dependencies and multiple acceptance criteria.

Typical examples:

- build the complete reusable application header/sidebar component set;
- implement the draft save/load pattern for the prompt wizard;
- implement the verifier queue with filtering, detail access and review actions;
- implement a role/security capability spanning app and data-layer configuration.

### Session-sized - 5 points

A ticket that reasonably consumes the whole session is assigned 5 points and must be the only implementation ticket in that Session Batch.

Typical examples:

- design the full Lists data model and permission model;
- implement a major cross-screen workflow capability;
- perform an integrated security validation across all roles;
- perform a full gate validation where many evidence items must be reviewed together.

If a ticket is larger than one 5-point session, it is too large and must be decomposed into smaller linked tickets before execution.

## Session Capacity Rule

**Maximum execution capacity: 5 ticket points per chat session.**

This is the authoritative batching limit.

Examples of valid Session Batches:

```text
5 Small tickets       = 1+1+1+1+1 = 5 points
2 Medium + 1 Small    = 2+2+1     = 5 points
1 Large + 2 Small     = 3+1+1     = 5 points
1 Large + 1 Medium    = 3+2       = 5 points
1 Session-sized       = 5         = 5 points
```

The point total is a capacity ceiling, not a target. A session may contain fewer points when the work reaches a natural handoff boundary earlier.

## Practical Ticket Quantity Per Session

Because ticket size varies, quantity is governed by points rather than a fixed count. In practice, one session will normally contain:

- 1 substantial ticket; or
- 2 to 3 normal implementation tickets; or
- up to 5 very small tightly related tickets.

A Session Batch must never contain more than **5 tickets**, even if the arithmetic point total would otherwise allow it.

## Same-Gate Rule

All execution tickets in one Session Batch must belong to the same gate.

Do not begin tickets from the next gate because the current session has spare capacity. Gate progression requires explicit validation and Project Control updates first.

## Same-Workstream Rule

A Session Batch must remain within one specialist workstream.

For example, a Power Apps Build session may implement UI/formula tickets but should not also perform the independent security validation ticket. The security ticket belongs to the Security workstream or Testing/Validation workstream as defined by the gate.

This separation becomes essential when specialist chats are later replaced or supplemented by specialist agents.

## Dependency Rule

A ticket may be placed in the same Session Batch as its prerequisite ticket only when:

1. the prerequisite is expected to be completed first within that same session;
2. both tickets belong to the same gate and workstream;
3. completion of the prerequisite can be objectively established before the dependent ticket starts.

If the dependency requires a different specialist workstream or human approval, the dependent ticket must remain outside the current batch.

## Session Start Process

At the start of every execution session:

1. Read `README.md` and `AGENTS.md` when needed for a new chat/workstream.
2. Read `project-management/PROJECT-CONTROL.md`.
3. Identify the current phase and gate.
4. Identify all `READY` tickets for the current workstream and gate.
5. Check dependencies and blockers.
6. Read applicable locked decisions.
7. Read the active phase and relevant design/standards documents.
8. Size candidate tickets using the point model.
9. Create the Session Batch with a maximum of 5 points and 5 tickets.
10. Select exactly one ticket as the Active Ticket.
11. Confirm the exact first action before implementation begins.

## Session Execution Process

For each ticket in the batch:

```text
READY
  ↓
IN PROGRESS
  ↓
Implementation / Design Work
  ↓
Self-check against acceptance criteria
  ↓
VALIDATION or COMPLETE according to ticket design
  ↓
Record outcome and evidence
  ↓
Activate next queued ticket
```

Only one ticket is actively modified at a time unless the tickets are explicitly defined as one inseparable atomic change.

A ticket that requires independent validation must end the implementation session in `VALIDATION`, not `COMPLETE`.

## When to Stop a Session Early

Stop the Session Batch before reaching 5 points when any of these occurs:

- a blocker is discovered;
- a new business decision is required;
- a locked decision would need to change;
- the next ticket requires another specialist workstream;
- the next ticket requires independent validation first;
- a ticket expands materially beyond its approved scope;
- acceptance criteria are ambiguous;
- required access, connector, data source, control, screen, or environment dependency is missing and cannot be created within the approved ticket sequence;
- the current gate may now be ready for validation;
- the session context has become too broad to maintain reliable traceability.

Unused capacity is not carried into another gate.

## When to Start a New Chat vs Continue an Existing Chat

Continue the existing specialist chat when:

- the work remains in the same specialist domain;
- GitHub state is clear;
- the chat is still manageable;
- the new Session Batch can be reconstructed from GitHub without relying on old conversational assumptions.

Start a new chat when:

- the specialist domain changes;
- a major phase transition occurs and a clean context boundary improves reliability;
- the current chat has become long enough that old implementation discussion creates ambiguity;
- a different specialist/agent is taking ownership;
- the user explicitly wants a clean session.

A new chat does not create new project state. The new chat must reconstruct state from GitHub.

## Project Manager Chat Role

The Project Manager chat is not an implementation bucket.

Its responsibilities are:

- read and maintain project state;
- determine the current phase and gate;
- identify eligible tickets;
- enforce dependencies;
- size and batch work;
- route tickets to the correct workstream;
- review progress and blockers;
- coordinate gate validation;
- record the exact next action.

The Project Manager chat may process several project-management tickets in one session, but the same 5-point capacity rule applies.

## Validation Sessions

Validation work is deliberately separated from implementation where practical.

A validation Session Batch may include validation tickets from the same gate up to the same 5-point capacity. However, gate passage must be treated as a dedicated decision step after all mandatory evidence is available.

A Gate Validation ticket is normally sized as Large (3 points) or Session-sized (5 points), depending on the amount of evidence and cross-cutting review required.

## Example - Multi-Step Prompt Form Gate

Assume Gate `PH11-G01` contains these tickets:

```text
T101 DESIGN  Define wizard step architecture         2 points
T102 BUILD   Build wizard shell and step navigation  3 points
T103 BUILD   Implement draft save/load               3 points
T104 BUILD   Implement completion calculation        2 points
T105 TEST    Validate wizard and draft behaviour      3 points
T106 VALIDATE Gate review                             3 points
```

The sessions would be grouped as:

```text
SES-PH11-G01-POWERAPPS-01
- T101 (2)
- T102 (3)
Total: 5

SES-PH11-G01-POWERAPPS-02
- T103 (3)
- T104 (2)
Total: 5

SES-PH11-G01-TEST-01
- T105 (3)
Total: 3

SES-PH11-G01-VALIDATE-01
- T106 (3)
Total: 3
```

The fact that the test and validation sessions have unused capacity does not permit unrelated work to be added.

## Example - Small Configuration Work

Assume one gate has five closely related small configuration tickets:

```text
T201 Create approved status-choice values     1 point
T202 Add technology-stream reference values   1 point
T203 Add AI-tool reference values              1 point
T204 Add output-type reference values          1 point
T205 Validate reference data                   1 point
```

If they belong to the same workstream and their dependency order permits it, they may form one 5-point Session Batch.

## Session End Process

Every session ends with a structured handoff even when more work remains in the same specialist chat.

Record:

- Session Batch ID;
- phase;
- gate;
- tickets planned;
- tickets completed;
- tickets moved to validation;
- tickets blocked or deferred;
- files/artifacts changed;
- validation performed;
- evidence produced;
- decisions created or affected;
- issues/blockers created or affected;
- dependencies discovered;
- remaining gate work;
- exact next ticket/action.

Update `PROJECT-CONTROL.md` when the active project state has changed.

## Future Agent-Orchestration Mapping

The same model becomes the dispatch rule for future agents.

```text
Project Manager Agent
        ↓
Reads current Gate and READY tickets
        ↓
Checks dependencies
        ↓
Sizes tickets
        ↓
Creates <=5-point Session Batch
        ↓
Routes batch to one Specialist Agent
        ↓
Specialist processes one active ticket at a time
        ↓
Validation Agent evaluates required evidence
        ↓
Project Manager updates gate/project state
```

The 5-point capacity prevents an orchestrator from assigning an agent an uncontrolled collection of unrelated work.

## Authoritative Rules

1. GitHub tickets are the work units; chats are execution sessions.
2. One chat may process multiple tickets.
3. A Session Batch may contain at most 5 points and at most 5 tickets.
4. All tickets in a batch must belong to the same phase, gate, and specialist workstream.
5. Only one ticket is Active at a time.
6. A ticket larger than 5 points must be decomposed before work begins.
7. A blocker, decision boundary, specialist boundary, validation boundary, or gate boundary ends the current batch when necessary.
8. Independent validation is not bypassed merely because implementation occurred in the same chat.
9. Project state is reconstructed from GitHub at the start of every session.
10. Every session ends with an explicit handoff and exact next action.
