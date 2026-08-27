# GitHub Operational Control Standard

Status: MANDATORY
Effective: 2026-08-27

## Purpose

Make GitHub mechanics enforce the project process so that a new human or AI agent can establish the exact live state without relying on chat history or manually reconciling several competing status stores.

## Authoritative responsibility model

- GitHub Issues are the transactional source of truth for live gate and ticket workflow state.
- Pull Requests are the controlled repository-change and review boundary.
- Phase evidence proves completion and lives in the owning phase folder.
- `project-management/PROJECT-CONTROL.md` is a derived project dashboard/snapshot; it must reflect live GitHub operational state and must not independently advance a ticket or gate.
- Phase documents define durable phase scope, learning, dependencies, acceptance criteria and historical outcomes; they do not replace live Issue state.
- `project-management/DECISIONS.md` remains authoritative for locked durable decisions.
- `project-management/ISSUES.md` remains authoritative for durable unresolved cross-cutting project issues.

## Operational hierarchy

`Project -> Phase -> Gate Issue -> Ticket Issue -> Working Branch -> Pull Request -> Validation/Evidence -> Ticket Complete -> Gate Decision -> Project Control Snapshot`

## Gate Issues

A gate Issue must contain:

- Gate ID and phase;
- objective;
- entry criteria;
- required ticket IDs;
- required evidence;
- acceptance criteria;
- gate decision (`NOT DECIDED`, `PASSED`, or `FAILED`);
- decision date when decided.

A gate may be marked `PASSED` only after all mandatory ticket Issues are complete and the required evidence exists.

## Ticket Issues

A ticket Issue must contain:

- ticket ID;
- phase and gate;
- workstream/type;
- dependencies;
- exactly one selected solution;
- acceptance criteria;
- required evidence;
- points;
- status.

Allowed operational statuses are:

- `NOT STARTED`
- `READY`
- `IN PROGRESS`
- `BLOCKED`
- `VALIDATION`
- `COMPLETE`

Only one ticket may be active at a time unless an approved session batch explicitly permits tightly related work under the Chat Session Ticket Capacity Model.

## GitHub-native metadata

Use labels in addition to the structured Issue body. The canonical label families are:

- `phase:PHxx`
- `gate:PHxx-Gxx`
- `type:design`, `type:doc`, `type:build`, `type:data`, `type:security`, `type:automation`, `type:ai`, `type:test`, `type:alm`, `type:validate`, `type:gate`, `type:bug`, `type:decision`
- `status:not-started`, `status:ready`, `status:in-progress`, `status:blocked`, `status:validation`, `status:complete`
- `priority:high`, `priority:normal`, `priority:low`

The Issue body explains the work. GitHub metadata makes the workflow queryable and automatable.

## Branch and Pull Request rule

Repository-changing ticket work uses one branch per active ticket:

`phxx-gxx-txx-short-purpose`

Examples:

`ph02-g01-t03-validate-solution-foundation`

Commits must begin with the ticket ID for ticket-scoped work, for example:

`PH02-G01-T03: add publisher validation evidence`

Cross-phase governance work uses an explicit governance identifier or descriptive governance commit message.

Changes to `main` must normally arrive through a Pull Request. The PR must identify:

- Ticket ID or governance scope;
- Phase/gate if applicable;
- selected solution;
- dependencies;
- validation performed;
- evidence produced;
- unresolved items;
- Project Control impact.

A merged PR does not by itself complete a ticket or pass a gate.

## Phase artifact rule

All phase-owned durable artifacts follow `project-management/PHASE-FOLDER-STANDARD.md`.

Live workflow status must not be duplicated into additional phase-specific tracking files merely to mirror GitHub Issues. Evidence, specifications, approvals and handoffs remain in the phase folder; live ticket/gate status remains in Issues.

## Project Control rule

`PROJECT-CONTROL.md` is updated after operational state changes. It must name the current phase, gate, active/next ticket and blockers, but its values are derived from the corresponding GitHub Issues.

If `PROJECT-CONTROL.md` conflicts with the live operational Issues, stop execution, reconcile the conflict, and do not advance work until the discrepancy is resolved.

## Completion rule

A ticket is complete only when:

1. acceptance criteria are satisfied;
2. required evidence exists at the canonical path;
3. validation is recorded;
4. the Pull Request is merged when repository changes were required;
5. the ticket Issue is marked complete/closed;
6. Project Control is synchronized.

A gate passes only when all required tickets are complete, the gate evidence exists, and the formal gate decision is recorded.

## Automation rule

Repository automation should progressively enforce machine-checkable rules, beginning with:

- canonical phase artifact paths;
- required phase structure;
- unique decision and issue IDs;
- required PR metadata;
- no phase-owned evidence under deprecated shared evidence paths.

Automation is a guardrail, not a substitute for human gate approval or domain validation.

## Branch protection target

`main` must be configured to require Pull Requests for ordinary changes and to prevent routine direct pushes. The required repository ruleset/branch-protection setting is an administrative GitHub configuration and must be kept aligned with this standard.

## Agent start sequence

A new agent should establish state in this order:

1. `README.md`
2. `AGENTS.md`
3. `project-management/GITHUB-OPERATIONAL-CONTROL-STANDARD.md`
4. `project-management/PROJECT-CONTROL.md`
5. current gate Issue
6. active/next ticket Issue
7. `project-management/DECISIONS.md`
8. `project-management/ISSUES.md`
9. active phase specification and relevant standards/evidence

No agent may infer a different live workflow state from chat history when GitHub operational records exist.