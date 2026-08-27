# GitHub Action Gateway Standard

Status: MANDATORY WHEN THE GATEWAY IS USED  
Version: 1.1  
Effective: 2026-08-27

## Purpose

Provide a constrained GitHub-native execution channel for operational transactions that the connected AI cannot perform directly, without exposing arbitrary shell, HTTP, repository-administration, or secret-management capability.

The gateway extends the GitHub Operational Control Model. Issues remain live work state, Pull Requests remain the repository change boundary, evidence proves completion, and Markdown remains durable design/summarized state.

## Selected architecture

```text
AI / connected agent
        |
        | one immutable JSON command
        v
agent-command-gateway
agent-commands/inbox/<command-id>.json
        |
        v
Agent Command Intake
(contents: read)
        |
        v
workflow_run
        |
        v
Agent Command Executor
(trusted code from main)
        |
        +--> verify authorized originating actor
        +--> verify single-file append-only command commit
        +--> validate schema/repository/operation
        +--> validate semantic workflow state
        +--> execute one allow-listed GitHub transaction
        +--> recover by commandId if mutation already occurred
        +--> append result with full provenance
```

## Trust boundary

`main` is the trusted source for executor code and governance. The command branch is transport only and cannot replace executor code.

A command commit must be single-parent, add exactly one new `agent-commands/inbox/*.json` file, and change nothing else. Command files are immutable.

The privileged executor may run only when:

- Agent Command Intake completed successfully;
- the originating branch is exactly `agent-command-gateway`;
- the originating actor is the repository owner/approved command-submission identity;
- the Python executor independently validates the same actor value.

## Transport-branch protection

`agent-command-gateway` must have a dedicated ruleset that:

- restricts updates to the approved command-submission identity and GitHub Actions integration required for result commits;
- blocks deletion;
- blocks force pushes/non-fast-forward updates;
- does not require Pull Requests, because command and result records are direct append-only transport commits;
- grants no broad administrator bypass.

The executor's actor check is mandatory defense in depth and must remain even when the branch ruleset is active.

## Permissions

The intake workflow uses only `contents: read`.

Gateway v1 executor uses only:

- `contents: write` for append-only result records on the transport branch and read access to evidence on `main`;
- `issues: write` for the allow-listed Issue operations.

No PAT is stored in ChatGPT or the repository. The executor uses the repository-scoped GitHub Actions `GITHUB_TOKEN`.

## Dependency integrity

Third-party/first-party Actions used by the gateway and Repository Integrity workflows must be pinned to reviewed full commit SHAs rather than mutable major-version tags.

## Queue integrity

The executor uses one concurrency group with `cancel-in-progress: false` and `queue: max`. Commands must not be silently replaced while pending. State-transition validation remains authoritative because queued execution order is not itself a project-state guarantee.

## Version 1 allow-list

Version 1 supports exactly:

- `create_gate`
- `create_ticket`
- `start_ticket`
- `complete_ticket`
- `add_issue_comment`

It does not support arbitrary shell/HTTP/API execution, direct `main` writes, PR merge, branch/ruleset administration, branch deletion, secrets, credentials, or `pass_gate`.

## Canonical identity

Every generated ticket must persist its immutable identifier in both the title and an exact body field:

```text
### Ticket ID
`PHxx-Gxx-Txx`
```

`ticketId` is mandatory for `start_ticket` and `complete_ticket`. Lifecycle operations parse and compare the canonical Ticket ID field; a substring elsewhere in the Issue is not identity proof.

## Creation authorization

`create_gate` must reject a duplicate Gate ID and must not create a second gate while another gate is open.

`create_ticket` must reject a duplicate Ticket ID and must independently verify:

- exactly one parent gate exists;
- the parent gate is open;
- phase/gate labels agree with the ticket;
- a READY ticket's referenced ticket/gate dependencies are satisfied.

Syntactically valid input is not sufficient authorization.

## Lifecycle controls

`start_ticket` permits only `READY -> IN PROGRESS` and rejects the transition if another open ticket in the same gate is already IN PROGRESS.

`complete_ticket` permits only `IN PROGRESS` or `VALIDATION -> COMPLETE`. It requires:

1. an open target Issue;
2. exact canonical Ticket ID match;
3. at least one checked acceptance criterion and no unchecked acceptance criteria;
4. every supplied evidence path to be under the ticket's own `project-management/phases/PHxx/evidence/` directory;
5. every supplied evidence path to be declared in that ticket's `### Evidence` section;
6. every supplied evidence file to exist on `main`.

Only then may the executor set COMPLETE and close the Issue.

## Intrinsic idempotency

Result-file existence is not the only replay control. Every mutating operation uses `commandId` as an idempotency marker on the affected GitHub object.

Before mutation the executor checks whether that marker already exists. If the GitHub mutation succeeded previously but result recording failed, the executor reconstructs a successful result instead of duplicating the transaction.

This applies to created gates, created tickets, lifecycle body transitions, and Issue comments.

A pre-existing FAILED result is terminal for that command ID. Correct the cause and submit a new immutable command with a new command ID.

## Audit provenance

Every result record contains:

- schema version;
- command ID and operation;
- status and operation detail;
- submitted command commit SHA;
- intake workflow run ID;
- executor workflow run ID;
- originating workflow actor;
- executor `main` SHA;
- UTC execution timestamp;
- target object/status information where applicable.

Commands and results remain append-only under `agent-commands/inbox/` and `agent-commands/results/`.

## Repository-change boundary

The gateway is not a shortcut around Pull Request governance. Repository source, workflows, governance, phase evidence, application files, and project documentation still change through governed branches and Pull Requests.

`complete_ticket` verifies evidence already merged to `main`; it does not manufacture evidence.

## Validation requirement

Repository Integrity must execute the Gateway unit/security tests. The suite must cover validation, canonical identity, duplicate/parent checks, lifecycle transitions, wrong-phase/undeclared/missing evidence, multi-file/modified/merge command rejection, wrong branch, and idempotent recovery.

The gateway must not be used routinely for lifecycle operations until the hardening PR is merged, the transport-branch ruleset is active, Repository Integrity passes, and a post-hardening lifecycle smoke test succeeds.
