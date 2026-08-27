# power-app-learning-project

Power Apps learning and implementation repository with durable AI project-continuity rules.

## Agent entry point

All AI agents and coding assistants must read [`AGENTS.md`](AGENTS.md) before making project changes.

## Project state

Use these canonical project-management locations:

- `project-management/control/PROJECT-CONTROL.md` — derived current project snapshot and exact next step.
- `project-management/control/AI-PROJECT-CONTINUITY-FLOW.md` — cross-session continuity process.
- `project-management/registers/DECISIONS.md` — durable and locked project decisions.
- `project-management/registers/ISSUES.md` — durable blockers and unresolved cross-cutting issues.
- `project-management/planning/PROJECT-OPERATIONAL-DELIVERY-PLAN.md` — cross-phase delivery roadmap.
- `project-management/phases/` — phase-owned specifications, gates, evidence, approvals and handoffs.

Governance standards live under `project-management/governance/`. Solution architecture, technical standards and design documentation live under `docs/`.

## Source of truth

GitHub Issues are the transactional source of truth for live gate/ticket workflow state. Pull Requests control repository changes. Phase evidence proves completion. `PROJECT-CONTROL.md` is a derived dashboard. Chat history and AI memory may provide context, but they must not override locked decisions or tracked GitHub state.
