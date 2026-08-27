# Agent Command Gateway Transport

This directory defines the transport contract for the GitHub Action Gateway.

The transport branch is `agent-command-gateway`. It is not a development branch and must not contain project implementation changes.

## Command submission

Each command is one new JSON file committed under:

`agent-commands/inbox/<command-id>.json`

A command commit must add exactly one file and change nothing else. The command is immutable after submission.

The low-privilege `Agent Command Intake` workflow receives the push. The privileged `Agent Command Executor` workflow is loaded from trusted `main`, re-fetches the command commit, independently validates the changed path and JSON payload, and only then performs an allow-listed GitHub transaction.

## Results

Execution results are append-only JSON records written to:

`agent-commands/results/<command-id>.json`

A pre-existing result makes a repeated workflow run idempotent; the command is not executed twice.

## Version 1 operations

- `create_gate`
- `create_ticket`
- `start_ticket`
- `complete_ticket`
- `add_issue_comment`

There is intentionally no arbitrary shell, HTTP, GitHub API, file-write, merge, or `pass_gate` operation.

## Security boundary

The command branch is an input transport only. The privileged executor always checks out its code from `main`. A command-branch commit therefore cannot replace the trusted executor. The executor also validates the repository, command schema version, command ID, operation allow-list, target Issue state, evidence requirements where applicable, and the exact files changed by the command commit.
