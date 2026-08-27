# GitHub Action Gateway Standard

Status: MANDATORY WHEN THE GATEWAY IS USED  
Version: 1.0  
Effective: 2026-08-27

## Purpose

Provide a controlled GitHub-native execution channel for operational transactions that an AI connector cannot perform directly, without giving the AI arbitrary repository or shell execution capability.

The gateway extends the existing GitHub Operational Control Model. It does not replace Issues, Pull Requests, phase evidence, protected `main`, Repository Integrity, or formal gate approval.

## Selected architecture

```text
AI / connected agent
        |
        | one structured JSON command
        v
agent-command-gateway branch
agent-commands/inbox/<command-id>.json
        |
        v
Agent Command Intake
(low privilege, contents: read)
        |
        v
workflow_run
        |
        v
Agent Command Executor
(trusted code checked out from main)
        |
        +--> independently verify command commit
        +--> validate schema and repository
        +--> validate allow-listed operation
        +--> validate workflow state transition
        +--> execute GitHub REST transaction
        +--> write append-only result record
```

## Trust boundary

`main` remains the trusted source for executor code and governance.

The `agent-command-gateway` branch is transport only. A command submission must add exactly one new JSON file under `agent-commands/inbox/` and must not modify workflows, scripts, governance documents, project files, or implementation artifacts.

The intake workflow is deliberately unprivileged. The executor is triggered by `workflow_run` and checks out `main`, so command-branch content cannot replace the privileged executor implementation.

## Permissions

The intake workflow uses:

- `contents: read`

The executor uses only:

- `actions: read`
- `contents: write` — restricted by executor code to append-only result records on the gateway branch and evidence existence checks on `main`
- `issues: write`
- `pull-requests: read`

No personal access token is stored in ChatGPT or the repository. The executor uses the repository-scoped `GITHUB_TOKEN` supplied by GitHub Actions.

## Command envelope

Every command must contain:

```json
{
  "schemaVersion": 1,
  "commandId": "unique-id",
  "operation": "allow-listed-operation",
  "repository": "bkloppers/power-app-learning-project"
}
```

The command ID is immutable and becomes the result-record key.

## Version 1 allow-list

Version 1 supports exactly:

- `create_gate`
- `create_ticket`
- `start_ticket`
- `complete_ticket`
- `add_issue_comment`

Version 1 intentionally does not support:

- arbitrary shell commands;
- arbitrary HTTP or GitHub API calls;
- direct writes to `main`;
- merging Pull Requests;
- changing branch/ruleset protection;
- deleting branches;
- secrets or credential operations;
- `pass_gate`.

Formal gate passage remains an explicitly authorized project decision until a later gateway version defines and proves stronger independent gate controls.

## State-transition controls

`start_ticket` may transition only `READY -> IN PROGRESS`. The executor rejects the transition if another open ticket in the same gate is already labelled `status:in-progress`.

`complete_ticket` may transition only `IN PROGRESS` or `VALIDATION -> COMPLETE`. It requires:

1. an open target Issue;
2. matching ticket identity when supplied;
3. no unchecked acceptance criteria in the Issue acceptance section;
4. at least one checked acceptance criterion;
5. every command-supplied evidence path to exist on `main`;
6. every evidence path to be phase-owned under `project-management/phases/PHxx/.../evidence/`.

Only after those checks pass may the executor set `status:complete` and close the Issue as completed.

## Create controls

`create_gate` and `create_ticket` build canonical Issue bodies and canonical labels. Missing canonical labels may be created by the executor. New tickets may begin only as `NOT STARTED` or `READY`.

The gateway does not invent project scope. The calling agent must derive gate/ticket definitions from already-approved planning and governance sources.

## Audit and replay protection

Commands are append-only under `agent-commands/inbox/`.

Results are append-only under `agent-commands/results/` and contain:

- schema version;
- command ID;
- operation;
- `SUCCEEDED` or `FAILED`;
- execution detail or error.

If a result already exists for a command ID, a workflow rerun is treated as an idempotent success and the GitHub transaction is not repeated.

## Relationship to protected main

The gateway must never be used as a shortcut around Pull Request governance for repository changes. Repository source, governance, phase evidence, application files, and project documentation still change through governed branches and Pull Requests.

The gateway's `contents: write` permission is solely for its append-only result record on the transport branch. Evidence is verified on `main`; it is not manufactured by `complete_ticket`.

## Bootstrap sequence

1. Merge the governed PR that introduces this standard, workflows, executor and tests.
2. Confirm Repository Integrity passes on the merged `main` state.
3. Create `agent-command-gateway` from that exact `main` commit.
4. Do not add implementation content to the transport branch.
5. Submit a non-destructive `add_issue_comment` smoke-test command.
6. Verify both Action workflows and the append-only result record.
7. Only then use lifecycle commands such as `start_ticket` or `complete_ticket`.

## Failure handling

A rejected command changes no intended target state. The executor attempts to write a `FAILED` result record with the rejection/error detail. Correct the cause and submit a new command with a new command ID; do not edit the rejected command file.
