# power-app-learning-project

Power Apps learning and implementation repository with durable AI project-continuity rules.

## Agent entry point

All AI agents and coding assistants must read [`AGENTS.md`](AGENTS.md) before making project changes.

The project-management continuity process is documented in [`project-management/AI-PROJECT-CONTINUITY-FLOW.md`](project-management/AI-PROJECT-CONTINUITY-FLOW.md).

When the operational tracking files exist, agents must also use:

- `project-management/PROJECT-CONTROL.md` for the current phase, active task, dependencies, acceptance criteria, status, and exact next step;
- `project-management/DECISIONS.md` for durable and locked project decisions;
- `project-management/ISSUES.md` for blockers and unresolved issues;
- `project-management/phases/` for phase-specific objectives, tasks, dependencies, and exit criteria.

## Source of truth

GitHub is the durable source of truth for project state. Chat history and AI memory may provide context, but they must not override locked decisions or the tracked project state in this repository.
