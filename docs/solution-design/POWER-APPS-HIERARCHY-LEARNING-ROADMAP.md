# Power Apps Hierarchy Learning and Build Roadmap

## Status

Initial authoritative roadmap for review and gate creation.

## Purpose

This roadmap converts the final application architecture into a cumulative Power Apps learning programme. Every phase adds a production-relevant capability to the same Microsoft Teams-hosted Canvas App.

The delivery pattern for every phase is:

**Learning Phase -> Lab -> Demonstration -> Understanding -> Validation -> Gate Decision**

No phase is a disposable exercise.

## Final Application Target

```text
Microsoft Teams
└── Power Apps Canvas App
    ├── Shared Application Shell
    │   ├── App object/configuration
    │   ├── NTT DATA theme/design tokens
    │   ├── Header
    │   ├── Navigation/sidebar
    │   ├── Role context
    │   ├── Main responsive workspace
    │   ├── Dialog/toast/loading host
    │   └── Shared error handling
    ├── Tool 01 - AI Prompt Capture, Submission and Verification
    │   ├── My Prompts
    │   ├── Multi-step Prompt Wizard
    │   ├── Completion Indicator
    │   ├── Peer Rating
    │   ├── Formal Verification
    │   ├── Changes and Resubmission
    │   ├── Testing and Score Gate
    │   └── Administration
    ├── Tool 02 - AI Prompt Chatbot
    └── Future Tools
```

## Roadmap Rules

1. Build the final architecture progressively rather than designing throwaway training screens.
2. Check dependencies before every phase begins.
3. Preserve project naming, responsive-layout, formula/state, App-object, design-system, accessibility, delegation, security, ALM, and testing standards.
4. Security is enforced in the data/platform layer, not by hiding controls.
5. Microsoft Lists is the initial Tool 01 data platform.
6. Tool 02 is a known architectural dependency from the beginning, even though its implementation occurs later.
7. A phase is complete only after demonstration, understanding, validation evidence, and gate approval.

---

# PHASE 01 - Solution Definition and Learning Architecture

## Hierarchy Level
Solution / business architecture.

## Learning Phase
Understand that the app hierarchy begins above screens and controls. Business process, roles, data boundaries, security, workflow, host, and future modules determine how the app must be structured.

## Lab
Document Tool 01, Tool 02, users, roles, workflow, Microsoft Lists direction, Microsoft Teams hosting, gate model, and future multi-tool architecture.

## Demonstration
Trace a prompt from submitter draft through optional peer rating, formal verification by at least two verifiers, changes/resubmission, testing/score criteria, completion, and administrator rejection authority.

## Understanding
Explain why screens and controls cannot be designed correctly before the process and access model are known.

## Gate
`PH01-G01 - Solution scope and process approved`

## Exit
Approved hierarchy roadmap and initial architecture.

---

# PHASE 02 - Solution, Publisher and Environment Foundation

## Hierarchy Level
Power Platform solution and ALM container.

## Learning Phase
Understand the relationship between environment, publisher, unmanaged development solution, connection references, environment variables, and deployable app assets.

## Lab
Create the development solution foundation using the project naming standard and custom publisher. Establish Dev-first solution ownership before creating production assets.

## Demonstration
Show where the Canvas App, flows, environment variables, and connection references will live and how they move together.

## Understanding
Explain why production apps should not begin as untracked standalone artifacts.

## Gate
`PH02-G01 - Solution and ALM foundation valid`

---

# PHASE 03 - App Object and Application Configuration

## Hierarchy Level
App object.

## Learning Phase
Understand `App.StartScreen`, `App.Formulas`, minimal `App.OnStart`, `App.OnError`, and application-level state boundaries.

## Lab
Create the Canvas App inside the approved solution. Add initial immutable design/configuration formulas and only the mutable session state that genuinely belongs at app scope.

## Demonstration
Show declarative startup, application-wide formulas, error fallback, and the difference between formulas and mutable variables.

## Understanding
Explain why the App object is an application configuration layer rather than a dumping ground for initialization logic.

## Gate
`PH03-G01 - App foundation configured`

---

# PHASE 04 - Screens and Navigation Boundaries

## Hierarchy Level
Screens.

## Learning Phase
Understand a screen as a page/workspace boundary and learn when a capability deserves its own screen.

## Lab
Create the initial screen set needed for the multi-tool shell and Tool 01 workspaces using the approved plain-language `...Screen` naming convention.

Initial functional screen boundaries:
- Home / Tool Launcher;
- My Prompts;
- Prompt Submission Wizard;
- Prompt Review / Summary;
- Verifier Queue;
- Verification Workspace;
- Administration Workspace.

## Demonstration
Navigate between screen boundaries without embedding business security into navigation logic.

## Understanding
Explain the difference between screen navigation and authorization.

## Gate
`PH04-G01 - Screen architecture approved`

---

# PHASE 05 - Responsive Containers and Page Structure

## Hierarchy Level
Containers / layout hierarchy.

## Learning Phase
Understand responsive auto-layout, parent-relative sizing, fill portions, wrapping, gaps, alignment, and the standard screen tree.

## Lab
Implement the standard hierarchy on the initial screens:

```text
Screen
└── conScreenRoot
    ├── conPageFlowCol
    │   ├── conAppHeaderRow
    │   ├── conAppBodyRow
    │   │   ├── conSideNavCol
    │   │   └── conMainCol
    │   └── conAppFooterRow (when required)
    └── conOverlayHost
```

## Demonstration
Resize the Teams-hosted experience and show container-driven layout changes without hard-coded X/Y positioning.

## Understanding
Explain why the overlay host is separated from normal page flow and why logical containers are used instead of wrapping every individual control.

## Gate
`PH05-G01 - Responsive screen tree validated`

---

# PHASE 06 - Design System and Reusable Components

## Hierarchy Level
Components and shared visual system.

## Learning Phase
Understand reusable components, design tokens, input/output properties, and separation of structural UI from tool-specific content.

## Lab
Create the shared application shell components required at this level, including branded Header and responsive Sidebar/navigation patterns, using approved NTT DATA design values and icons.

## Demonstration
Use the same shared components across multiple screens and show application-wide theme behaviour.

## Understanding
Explain when a component is appropriate and why repeated shell UI should not be manually rebuilt on every screen.

## Gate
`PH06-G01 - Shared shell components validated`

---

# PHASE 07 - Controls, Properties and Formula Binding

## Hierarchy Level
Controls -> properties -> formulas.

## Learning Phase
Understand how controls expose properties and how Power Fx formulas bind behaviour, appearance, accessibility, and data.

## Lab
Build the Home / Tool Launcher and first My Prompts UI controls using descriptive names and formula-bound properties rather than duplicated raw values.

## Demonstration
Change a shared formula/token/state and show dependent control properties recalculate automatically.

## Understanding
Explain the dependency chain from control to property to formula and why hard-coded repeated values create maintenance problems.

## Gate
`PH07-G01 - Control/property/formula patterns validated`

---

# PHASE 08 - State, Variables and Navigation Context

## Hierarchy Level
Direct formulas -> named formulas -> `With()` -> context state -> global state -> collections.

## Learning Phase
Understand the project's state-management decision order and why variables are used only when state must be remembered.

## Lab
Implement real application state such as sidebar open/closed, theme state, selected prompt navigation context, wizard step, dialogs, filters, and edit modes using the narrowest appropriate state scope.

## Demonstration
Show local state disappearing with screen context where appropriate while true application state persists across screens.

## Understanding
Explain why selected records, wizard steps, temporary calculations, and app-wide mutable state should not all be global variables.

## Gate
`PH08-G01 - State architecture validated`

---

# PHASE 09 - Microsoft Lists Data Architecture

## Hierarchy Level
Data sources and relationships.

## Learning Phase
Understand Lists as persistent data sources, column types, lookup relationships, indexing, delegation implications, ownership, audit metadata, and configuration/reference data.

## Lab
Design and create the governed Lists required for Tool 01, beginning with:

- Prompt Submissions;
- Prompt Peer Ratings;
- Prompt Reviews;
- required reference/configuration structures.

Relationship direction:

```text
Prompt Submission 1 -> many Peer Ratings
Prompt Submission 1 -> many Prompt Reviews
```

## Demonstration
Create related records and retrieve the correct child records for one prompt.

## Understanding
Explain why peer ratings and formal verifier reviews are separate records and why reviewer columns such as R1-R5 are not scalable data design.

## Gate
`PH09-G01 - Tool 01 data model validated`

---

# PHASE 10 - Galleries, Filtering and Record Access

## Hierarchy Level
Data-bound galleries and delegable queries.

## Learning Phase
Understand galleries, `ThisItem`, delegable filtering, sorting, search constraints, selection, empty states, and role-aware record presentation.

## Lab
Build My Prompts and the initial verifier queue against real List data.

## Demonstration
Show a submitter seeing only permitted records in the UX and a verifier workspace presenting its governed dataset.

## Understanding
Explain why gallery filtering is a user-experience rule and not a security boundary.

## Gate
`PH10-G01 - Record-list experiences validated`

---

# PHASE 11 - Multi-Step Forms and Draft Persistence

## Hierarchy Level
Forms, cards/fields, record editing, Patch/Submit patterns.

## Learning Phase
Understand forms and form state, cards/fields, draft persistence, edit/new modes, submit behaviour, and when direct `Patch()` is more appropriate for targeted updates.

## Lab
Implement the six-step Prompt Submission Wizard:

1. Submitter and Prompt Context;
2. Prompt and AI Tool;
3. Outcome and Productivity Impact;
4. Reusability and Lessons Learned;
5. Automation Opportunity and Executive Summary;
6. Quality Check and Submit.

## Demonstration
Start a prompt, save a draft, leave the wizard, reopen the same prompt, continue from persisted data, and navigate backward/forward without losing values.

## Understanding
Explain the difference between UI step state and persisted record state.

## Gate
`PH11-G01 - Guided draft form validated`

---

# PHASE 12 - Validation and Completion Indicator

## Hierarchy Level
Business validation formulas and derived progress.

## Learning Phase
Understand required-field validation, conditional validation, section completion formulas, accessible error states, and derived progress.

## Lab
Implement section validation, error summaries, quality checklist requirements, and the completion indicator.

The progress indicator must show:
- current step;
- total steps;
- completed steps;
- incomplete/problem steps;
- accessible textual completion;
- overall completion derived from required business data.

## Demonstration
Show that simply visiting a section does not increase true completion if required data is missing.

## Understanding
Explain the difference between navigation progress, form completion, workflow status, and business approval status.

## Gate
`PH12-G01 - Validation and completion model validated`

---

# PHASE 13 - Roles and Data-Layer Security

## Hierarchy Level
Identity, groups, permissions and authorization.

## Learning Phase
Understand Microsoft 365 identity, submitter ownership, peer access, verifier group access, administrator privileges, SharePoint/List permission enforcement, and least privilege.

## Lab
Implement the approved security model:
- Submitter: own prompt records only;
- Peer rater: explicitly invited prompt only;
- Verifier: formal verification dataset and review creation;
- Administrator: all-record management and reject authority.

## Demonstration
Test the same app using different role identities and prove restricted users cannot access unauthorized records even if UI controls are manipulated.

## Understanding
Explain why `Visible = gblIsAdmin` is not authorization.

## Gate
`PH13-G01 - Security model validated`

---

# PHASE 14 - Peer Rating Workflow

## Hierarchy Level
Related-record workflow and controlled sharing.

## Learning Phase
Understand invitation-driven access, child records, status transitions, feedback loops, and temporary/limited participant permissions.

## Lab
Implement the optional `Please rate my prompt` process between Draft and formal submission.

## Demonstration
A submitter requests a peer rating, the invited user accesses only the specific prompt/rating experience, provides feedback/rating, and the submitter sees the response without the peer becoming a verifier.

## Understanding
Explain why peer feedback is intentionally excluded from formal verification calculations.

## Gate
`PH14-G01 - Peer rating workflow validated`

---

# PHASE 15 - Formal Verification Workflow

## Hierarchy Level
Governed business process/state machine.

## Learning Phase
Understand formal status transitions, review records, multi-reviewer agreement, changes requested, resubmission, review history, and administrator-only rejection.

## Lab
Implement the formal verification lifecycle with a minimum of two independent verifiers.

Required behaviour:
- verifier may request changes;
- submitter edits and resubmits;
- verification restarts/continues according to approved rules;
- verifier cannot reject;
- administrator can reject;
- completion requires successful testing, future-defined score threshold, and both required verifiers agreeing.

## Demonstration
Run a prompt through changes requested, resubmission, two verifier reviews, and successful completion.

## Understanding
Explain the difference between review record status and parent Prompt Submission workflow status.

## Gate
`PH15-G01 - Formal verification lifecycle validated`

---

# PHASE 16 - Power Automate and Notifications

## Hierarchy Level
Automation/integration outside synchronous Canvas formulas.

## Learning Phase
Understand when Power Automate is appropriate, connection references, service-side actions, notifications, retries, idempotency, and failure handling.

## Lab
Add the flows required by the approved business process, such as submission, peer-rating request, changes-requested, resubmission, verification-complete, and administrative notifications where confirmed.

## Demonstration
Trigger each approved flow from real state changes and prove errors do not create duplicate or misleading process outcomes.

## Understanding
Explain why every action should not be converted into a flow and why synchronous UI logic and service automation have different roles.

## Gate
`PH16-G01 - Workflow automation validated`

---

# PHASE 17 - Microsoft Teams Integration

## Hierarchy Level
Host/integration context.

## Learning Phase
Understand Teams hosting, authenticated user context, responsive dimensions, app/tab deployment, Teams-specific navigation expectations, and accessibility.

## Lab
Publish/install the application into the approved Teams context and validate the full shell and Tool 01 user journeys there.

## Demonstration
Run submitter and verifier journeys inside Teams rather than only Power Apps Studio/player.

## Understanding
Explain how host constraints affect layout, authentication context, navigation, and testing.

## Gate
`PH17-G01 - Teams-hosted experience validated`

---

# PHASE 18 - Tool 02 AI Prompt Chatbot

## Hierarchy Level
AI/agent capability integrated into the modular app architecture.

## Learning Phase
Understand the selected chatbot platform, knowledge boundaries, security/governance, prompt grounding, approved data access, conversation UX, and integration with Tool 01.

## Dependencies
Tool 02 detailed requirements and platform decision must be approved before build work begins.

## Lab
Implement the approved AI Prompt Chatbot capability without giving it implicit access to restricted Tool 01 records.

## Demonstration
Show approved chatbot use cases and prove knowledge/data access follows the user's authorization boundary.

## Understanding
Explain why sharing an app shell does not imply sharing all data permissions with an AI capability.

## Gate
`PH18-G01 - AI Prompt Chatbot validated`

---

# PHASE 19 - Integrated Testing, Accessibility, Delegation and Resilience

## Hierarchy Level
Quality/operational validation across the full solution.

## Learning Phase
Understand production validation beyond formula correctness.

## Lab
Execute integrated tests covering at minimum:
- zero records;
- realistic and high record volumes;
- delegation boundaries;
- duplicate actions;
- simultaneous edits;
- missing/changed permissions;
- connector/flow failure;
- slow network behaviour;
- responsive Teams widths;
- keyboard use;
- accessible labels and focus order;
- error handling;
- role isolation;
- workflow transition integrity.

## Demonstration
Produce evidence from the app, Power Apps Monitor/Checker and relevant Power Platform diagnostics.

## Understanding
Explain why a valid formula is not proof of a production-ready app.

## Gate
`PH19-G01 - Integrated quality gate passed`

---

# PHASE 20 - ALM, Deployment and Operational Handover

## Hierarchy Level
Release lifecycle.

## Learning Phase
Understand versioning, managed deployment downstream, pipelines, environment-specific configuration, release evidence, rollback/repair thinking, and operational ownership.

## Lab
Package and deploy the validated solution through the approved ALM process into the target environment, including connection references and environment variables.

## Demonstration
Show that the same solution moves environments without hard-coded environment-specific configuration.

## Understanding
Explain the difference between making an app work in Development and operating a governed solution through its lifecycle.

## Gate
`PH20-G01 - Production release readiness approved`

---

# Cross-Phase Gate Requirements

Every phase gate requires:

1. required design artifact current;
2. required tickets complete;
3. acceptance criteria validated;
4. demonstration performed;
5. learner understanding confirmed;
6. evidence recorded;
7. no unresolved blocker that violates the gate;
8. applicable decisions recorded;
9. Project Control updated;
10. exact next step identified.

# Dependency Chain

```text
PH01 Requirements/Architecture
  -> PH02 Solution/ALM foundation
  -> PH03 App object
  -> PH04 Screens
  -> PH05 Containers
  -> PH06 Components/design system
  -> PH07 Controls/properties/formulas
  -> PH08 State/navigation context
  -> PH09 Lists/data model
  -> PH10 Galleries/queries
  -> PH11 Multi-step forms
  -> PH12 Validation/progress
  -> PH13 Security
  -> PH14 Peer rating
  -> PH15 Formal verification
  -> PH16 Power Automate
  -> PH17 Teams integration
  -> PH18 AI Prompt Chatbot
  -> PH19 Integrated quality
  -> PH20 Deployment/operations
```

# Roadmap Definition of Done

The roadmap is ready to drive implementation when:

- the phase order is approved;
- each phase has a clear learning objective and real app contribution;
- dependencies are explicit;
- gates can be converted into GitHub Issues;
- unresolved business rules are assigned to the correct future phase rather than guessed;
- Tool 01 and Tool 02 both fit the architecture without redesigning the application shell;
- the sequence preserves production best practices from the first build phase.
