# Project Operational Phase, Gate and Ticket Delivery Plan

Status: ACTIVE PROJECT PLAN
Source branch: `main`
Foundation baseline: APPROVED 2026-08-27
Origin: Produced by completed Phase 01 `TASK-002`; maintained from this point as a cross-phase project artifact, not as a task.

## Purpose

Convert the approved `POWER-APPS-HIERARCHY-LEARNING-ROADMAP.md` into the operational delivery structure required by the Process & Progress Framework, Gate Tracking Model, Chat Session Ticket Capacity Model, Future-First Power Apps Standard, and Phase Folder Standard.

This project-level plan spans PH01-PH20. It does not belong to a single phase and does not authorize implementation by itself. A phase may begin implementation only when its gate entry criteria and ticket dependencies are satisfied and the relevant tickets are marked `READY`.

Phase-specific execution state, evidence, gate packages, approvals and handoffs belong in the canonical `project-management/phases/PHxx/` folder. Where this cross-phase baseline and an approved phase-specific record differ because of later validated project changes, the current phase-specific record and locked decisions govern execution.

## Governing rules

- One cumulative Microsoft Teams-hosted Canvas App.
- Every phase follows Learning Phase -> Lab -> Demonstration -> Understanding -> Validation -> Gate Decision.
- One formal gate per approved roadmap phase unless later work proves a second gate is required.
- GitHub Issues are the operational gate/ticket system.
- Maximum 5 ticket points and maximum 5 tickets in a Session Batch.
- Same phase + same gate + same specialist workstream per Session Batch.
- One active ticket at a time.
- Independent validation remains separate where practical.
- Version-sensitive technical tickets require a current Microsoft-product freshness check before execution.
- Missing dependencies become explicit dependency tickets; approved architecture is not redesigned to avoid them.
- Every phase-specific artifact is stored under `project-management/phases/PHxx/` according to `project-management/PHASE-FOLDER-STANDARD.md`.

## Workstream codes

- `PM` - 00 Project Manager
- `ARCH` - 01 Architecture and Solution Design
- `PA` - 02 Power Apps Build
- `DATA` - 03 Data and Microsoft Lists
- `SEC` - 04 Security and Permissions
- `AUTO` - 05 Power Automate and Integration
- `AI` - 06 AI and Chatbot
- `TEST` - 07 Testing and Validation
- `ALM` - 08 Deployment and ALM
- `XREV` - 09 Issues, Decisions and Cross-Cutting Review

## Ticket point scale

- 1 = Small
- 2 = Medium
- 3 = Large
- 5 = Session-sized

---

# PH01 - Solution Definition and Learning Architecture

Gate: `PH01-G01 - Solution scope and process approved`

Entry: repository/governance available; initial design artifacts exist.

Tickets:
- `PH01-G01-T01 DESIGN` Reconcile approved foundation against Phase 01 acceptance/exit criteria - 2 pts - ARCH.
- `PH01-G01-T02 DOC` Synchronize living solution design, Phase 01 and Project Control with approved baseline - 2 pts - PM.
- `PH01-G01-T03 VALIDATE` Validate roadmap traceability from business process/roles/data to PH02-PH20 - 3 pts - TEST.
- `PH01-G01-T04 VALIDATE` Perform formal PH01 gate review and record decision - 3 pts - PM.

Dependencies: approved foundation baseline; roadmap; Tool 01/02 design; workflow-state model.

Acceptance/evidence: approved baseline linked; stale pre-approval statements corrected; roadmap traceability reviewed; unresolved rules assigned to future tickets; gate checklist and human approval evidence recorded.

Gate outcome required before PH02: `PASSED`.

---

# PH02 - Solution, Publisher and Environment Foundation

Gate: `PH02-G01 - Solution and ALM foundation valid`

Entry: PH01-G01 passed; target Dev environment access confirmed; maker permissions confirmed; current ALM guidance checked.

Tickets:
- `PH02-G01-T01 DESIGN` Define environment, publisher, solution, unique-name and prefix specification - 2 pts - ARCH.
- `PH02-G01-T02 ALM` Verify current solution/publisher/pipeline capabilities and production-suitable ALM pattern - 1 pt - ALM.
- `PH02-G01-T03 ALM` Validate the approved existing custom publisher and unmanaged development solution - 2 pts - ALM.
- `PH02-G01-T04 BUILD` Establish initial environment-variable and connection-reference container strategy - 2 pts - ALM.
- `PH02-G01-T05 TEST` Validate solution ownership, publisher metadata and deployable foundation - 2 pts - TEST.
- `PH02-G01-T06 VALIDATE` Gate review - 3 pts - TEST.

Evidence: screenshots/exports of publisher and solution metadata; naming checks; environment ownership; validation notes; current Microsoft guidance references.

Current approved PH02 foundation is recorded in `project-management/phases/PH02/` and supersedes the original assumption that T03 would create a new publisher/solution.

---

# PH03 - App Object and Application Configuration

Gate: `PH03-G01 - App foundation configured`

Entry: PH02 passed; Canvas App may be created inside approved solution; current modern Canvas/App-object behavior verified.

Tickets:
- `PH03-G01-T01 DESIGN` Define App object responsibility map and initial application configuration - 2 pts - ARCH.
- `PH03-G01-T02 BUILD` Create Canvas App inside solution and configure StartScreen/App.Formulas/minimal OnStart/OnError baseline - 3 pts - PA.
- `PH03-G01-T03 TEST` Validate formula/state boundaries and startup/error behavior - 2 pts - TEST.
- `PH03-G01-T04 DOC` Record App-level learning/demonstration evidence - 1 pt - PM.
- `PH03-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: App tree/config screenshots; formulas; startup behavior; error demonstration; learner explanation.

---

# PH04 - Screens and Navigation Boundaries

Gate: `PH04-G01 - Screen architecture approved`

Entry: PH03 passed; approved functional screen boundaries available.

Tickets:
- `PH04-G01-T01 DESIGN` Finalize screen inventory, responsibilities, suffixes and navigation map - 2 pts - ARCH.
- `PH04-G01-T02 BUILD` Create approved functional screens with plain-language `...Screen` names - 3 pts - PA.
- `PH04-G01-T03 BUILD` Implement declarative/navigation-context transitions without authorization logic - 2 pts - PA.
- `PH04-G01-T04 TEST` Validate navigation boundaries, back behavior and naming uniqueness - 2 pts - TEST.
- `PH04-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: screen tree; navigation map; route tests; explanation of navigation vs security.

---

# PH05 - Responsive Containers and Page Structure

Gate: `PH05-G01 - Responsive screen tree validated`

Entry: PH04 passed; responsive standard current and current Power Apps layout capabilities verified.

Tickets:
- `PH05-G01-T01 DESIGN` Define canonical screen-root/page-flow/overlay hierarchy and responsive rules - 2 pts - ARCH.
- `PH05-G01-T02 BUILD` Implement responsive root/container hierarchy on initial screens - 3 pts - PA.
- `PH05-G01-T03 TEST` Validate Teams-relevant widths, parent-relative sizing, flow, scrolling and overlay separation - 3 pts - TEST.
- `PH05-G01-T04 DOC` Capture screen-tree and learner explanation evidence - 1 pt - PM.
- `PH05-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: tree screenshots; width-resize captures; no fixed-position dependency in normal flow; overlay behavior.

---

# PH06 - Design System and Reusable Components

Gate: `PH06-G01 - Shared shell components validated`

Entry: PH05 passed; approved NTT DATA assets/tokens available; current modern control/component capability checked.

Tickets:
- `PH06-G01-T01 DESIGN` Define shared shell component inputs/outputs, token bindings and responsive responsibilities - 3 pts - ARCH.
- `PH06-G01-T02 BUILD` Build reusable Header component - 2 pts - PA.
- `PH06-G01-T03 BUILD` Build responsive Sidebar/navigation component and shell composition - 3 pts - PA.
- `PH06-G01-T04 TEST` Validate reuse, theme switching, responsive behavior, logo/icon rules and accessibility - 3 pts - TEST.
- `PH06-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: component definitions; reuse across screens; dark/light captures; accessible labels/focus; approved assets.

---

# PH07 - Controls, Properties and Formula Binding

Gate: `PH07-G01 - Control/property/formula patterns validated`

Entry: PH06 passed; control naming and current modern-control property names verified.

Tickets:
- `PH07-G01-T01 DESIGN` Define Home/Tool Launcher and My Prompts control/property binding specification - 2 pts - ARCH.
- `PH07-G01-T02 BUILD` Build Home/Tool Launcher controls - 2 pts - PA.
- `PH07-G01-T03 BUILD` Build initial My Prompts presentation controls - 2 pts - PA.
- `PH07-G01-T04 TEST` Validate naming, token/formula reuse, accessibility and property recalculation - 2 pts - TEST.
- `PH07-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: control tree; formula bindings; change-one-token demonstration; accessibility checks.

---

# PH08 - State, Variables and Navigation Context

Gate: `PH08-G01 - State architecture validated`

Entry: PH07 passed; state decision order/current Power Fx guidance checked.

Tickets:
- `PH08-G01-T01 DESIGN` Map each required state value to direct formula/named formula/With/context/global/collection - 3 pts - ARCH.
- `PH08-G01-T02 BUILD` Implement shell/theme/sidebar shared mutable state - 2 pts - PA.
- `PH08-G01-T03 BUILD` Implement selected prompt, wizard step, dialogs, filters and edit-mode local/navigation context - 3 pts - PA.
- `PH08-G01-T04 TEST` Validate scope lifetime and absence of unnecessary globals/collections - 2 pts - TEST.
- `PH08-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: state inventory; Variables view; demonstrations of local vs app-wide lifetime.

---

# PH09 - Microsoft Lists Data Architecture

Gate: `PH09-G01 - Tool 01 data model validated`

Entry: PH08 passed; approved Tool 01 requirements/workflow model; SharePoint site/List creation access; current Lists delegation/security guidance checked.

Tickets:
- `PH09-G01-T01 DATA` Finalize Prompt Submissions schema/index/metadata design - 3 pts - DATA.
- `PH09-G01-T02 DATA` Finalize Peer Ratings and Prompt Reviews relationship schemas - 3 pts - DATA.
- `PH09-G01-T03 DATA` Define reference/configuration structures and indexes - 2 pts - DATA.
- `PH09-G01-T04 BUILD` Create approved Lists and columns/lookups/indexes - 5 pts - DATA.
- `PH09-G01-T05 TEST` Validate relationships, indexing, sample records and delegation-sensitive fields - 3 pts - TEST.
- `PH09-G01-T06 VALIDATE` Gate review - 3 pts - TEST.

Evidence: schema docs; List settings; sample parent/child records; index configuration; delegation notes.

---

# PH10 - Galleries, Filtering and Record Access

Gate: `PH10-G01 - Record-list experiences validated`

Entry: PH09 passed; data sources connected; security design direction known but final enforcement remains PH13.

Tickets:
- `PH10-G01-T01 DESIGN` Define delegable My Prompts and verifier-queue query patterns - 2 pts - ARCH.
- `PH10-G01-T02 BUILD` Build My Prompts gallery/query experience - 3 pts - PA.
- `PH10-G01-T03 BUILD` Build initial verifier queue/query experience - 3 pts - PA.
- `PH10-G01-T04 TEST` Validate empty, sort/filter/search, delegation and selection behavior - 3 pts - TEST.
- `PH10-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: delegation warnings absent/understood; record-count tests; gallery captures; UX-vs-security explanation.

---

# PH11 - Multi-Step Forms and Draft Persistence

Gate: `PH11-G01 - Guided draft form validated`

Entry: PH10 passed; Prompt Submission schema available; six wizard steps approved.

Tickets:
- `PH11-G01-T01 DESIGN` Define wizard step architecture, field ownership, persistence boundaries and resume logic - 3 pts - ARCH.
- `PH11-G01-T02 BUILD` Build wizard shell and step navigation - 3 pts - PA.
- `PH11-G01-T03 BUILD` Implement draft create/save/load/resume pattern - 3 pts - PA.
- `PH11-G01-T04 BUILD` Implement six approved content steps - 5 pts - PA.
- `PH11-G01-T05 TEST` Validate new/edit/resume/back-forward/no-data-loss behavior - 3 pts - TEST.
- `PH11-G01-T06 VALIDATE` Gate review - 3 pts - TEST.

Evidence: persisted draft records; resume demonstration; state-vs-record explanation.

---

# PH12 - Validation and Completion Indicator

Gate: `PH12-G01 - Validation and completion model validated`

Entry: PH11 passed; required/conditional field rules explicitly documented.

Tickets:
- `PH12-G01-T01 DESIGN` Define validation matrix and derived completion formula model - 3 pts - ARCH.
- `PH12-G01-T02 BUILD` Implement section validation/error-summary patterns - 3 pts - PA.
- `PH12-G01-T03 BUILD` Implement accessible completion/progress indicator - 2 pts - PA.
- `PH12-G01-T04 TEST` Validate completion derives from business data rather than page visits - 3 pts - TEST.
- `PH12-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: validation matrix; failing/passing records; accessible status text; problem-step demonstration.

---

# PH13 - Roles and Data-Layer Security

Gate: `PH13-G01 - Security model validated`

Entry: PH12 passed; identities/groups/permissions available; SharePoint permission architecture approved.

Tickets:
- `PH13-G01-T01 SECURITY` Finalize role-to-data-action permission matrix and sharing model - 5 pts - SEC.
- `PH13-G01-T02 SECURITY` Configure submitter/peer/verifier/admin data-layer permissions - 5 pts - SEC.
- `PH13-G01-T03 BUILD` Bind role-aware UX to authorized capabilities without treating visibility as security - 2 pts - PA.
- `PH13-G01-T04 TEST` Execute cross-role negative and positive authorization tests - 5 pts - TEST.
- `PH13-G01-T05 VALIDATE` Security gate review - 5 pts - SEC.

Evidence: permission matrix; test identities; direct-access denial evidence; List permissions; role test results.

---

# PH14 - Peer Rating Workflow

Gate: `PH14-G01 - Peer rating workflow validated`

Entry: PH13 passed; invitation/share mechanism approved; Peer Rating List available.

Tickets:
- `PH14-G01-T01 DESIGN` Define peer invitation, status transitions, access expiry/removal and feedback contract - 3 pts - ARCH.
- `PH14-G01-T02 BUILD` Implement submitter peer-rating request experience - 2 pts - PA.
- `PH14-G01-T03 BUILD` Implement peer-rating workspace/record creation - 3 pts - PA.
- `PH14-G01-T04 SECURITY` Validate invited-record-only access and separation from verifier rights - 3 pts - SEC.
- `PH14-G01-T05 TEST` End-to-end peer-rating test - 3 pts - TEST.
- `PH14-G01-T06 VALIDATE` Gate review - 3 pts - TEST.

Evidence: invitation; restricted access; rating record; submitter feedback display; peer excluded from formal verification.

---

# PH15 - Formal Verification Workflow

Gate: `PH15-G01 - Formal verification lifecycle validated`

Entry: PH14 passed; verifier groups/Review schema; explicit decisions for score threshold and successful-testing definition completed before completion-state logic is built.

Tickets:
- `PH15-G01-T01 DESIGN` Resolve score threshold and successful-testing business rules - 3 pts - ARCH.
- `PH15-G01-T02 DESIGN` Define formal state machine, independent-verifier agreement and resubmission semantics - 5 pts - ARCH.
- `PH15-G01-T03 BUILD` Implement verifier queue/workspace and review-record actions - 5 pts - PA.
- `PH15-G01-T04 BUILD` Implement changes-requested/resubmission/two-verifier completion logic - 5 pts - PA.
- `PH15-G01-T05 SECURITY` Implement/validate administrator-only rejection - 3 pts - SEC.
- `PH15-G01-T06 TEST` Execute lifecycle/state-integrity tests - 5 pts - TEST.
- `PH15-G01-T07 VALIDATE` Gate review - 5 pts - TEST.

Evidence: state-transition matrix; two independent review records; changes/resubmit demo; admin reject test; completion-rule proof.

---

# PH16 - Power Automate and Notifications

Gate: `PH16-G01 - Workflow automation validated`

Entry: PH15 passed; notification recipients/events confirmed; connection references available; current connector/actions checked.

Tickets:
- `PH16-G01-T01 DESIGN` Define event-to-flow matrix, idempotency and retry/failure contract - 3 pts - ARCH.
- `PH16-G01-T02 BUILD` Implement approved submission/peer/changes/resubmission notifications - 5 pts - AUTO.
- `PH16-G01-T03 BUILD` Implement verification-complete/admin notifications confirmed by design - 3 pts - AUTO.
- `PH16-G01-T04 TEST` Validate retries, duplicate prevention, connector failure and misleading-state prevention - 5 pts - TEST.
- `PH16-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: flow definitions; run history; failure tests; connection-reference use; duplicate/idempotency proof.

---

# PH17 - Microsoft Teams Integration

Gate: `PH17-G01 - Teams-hosted experience validated`

Entry: PH16 passed; approved Teams target/team/tab deployment access available.

Tickets:
- `PH17-G01-T01 DESIGN` Confirm Teams host/deployment configuration and responsive test matrix - 2 pts - ARCH.
- `PH17-G01-T02 ALM` Publish/install approved app version into Teams context - 3 pts - ALM.
- `PH17-G01-T03 TEST` Validate submitter, peer, verifier and admin journeys inside Teams - 5 pts - TEST.
- `PH17-G01-T04 TEST` Validate Teams widths, keyboard, focus, navigation and host-specific behavior - 3 pts - TEST.
- `PH17-G01-T05 VALIDATE` Gate review - 3 pts - TEST.

Evidence: Teams-host screenshots/video; role journeys; responsive captures; accessibility results.

---

# PH18 - Tool 02 AI Prompt Chatbot

Gate: `PH18-G01 - AI Prompt Chatbot validated`

Entry: PH17 passed; Tool 02 detailed requirements and platform decision approved; security/knowledge boundaries approved; current AI/Copilot capabilities verified.

Tickets:
- `PH18-G01-T01 DESIGN` Complete Tool 02 requirements, use cases and conversation UX - 3 pts - AI.
- `PH18-G01-T02 DESIGN` Select production-suitable chatbot platform and integration architecture - 5 pts - ARCH.
- `PH18-G01-T03 SECURITY` Define knowledge/data authorization and Tool 01 isolation model - 5 pts - SEC.
- `PH18-G01-T04 BUILD` Implement approved chatbot capability in shared shell - 5 pts - AI.
- `PH18-G01-T05 TEST` Validate approved use cases, grounding, failures and unauthorized-data isolation - 5 pts - TEST.
- `PH18-G01-T06 VALIDATE` Gate review - 5 pts - TEST.

Evidence: platform decision; architecture; prompts/knowledge config; authorization tests; chatbot demonstrations.

---

# PH19 - Integrated Testing, Accessibility, Delegation and Resilience

Gate: `PH19-G01 - Integrated quality gate passed`

Entry: PH18 passed; production-like test data and all role identities available.

Tickets:
- `PH19-G01-T01 TEST` Execute realistic/high-volume and delegation validation suite - 5 pts - TEST.
- `PH19-G01-T02 TEST` Execute concurrency, duplicate-action, slow-network and integration-failure suite - 5 pts - TEST.
- `PH19-G01-T03 TEST` Execute accessibility/responsive/keyboard/focus suite - 5 pts - TEST.
- `PH19-G01-T04 SECURITY` Revalidate role isolation and permission changes/failures - 5 pts - SEC.
- `PH19-G01-T05 TEST` Run current App Checker/Monitor/Solution Checker diagnostics and triage findings - 5 pts - TEST.
- `PH19-G01-T06 VALIDATE` Integrated quality gate review - 5 pts - TEST.

Evidence: test logs; Monitor traces; checker exports; defect links; closed/accepted findings; role-isolation proof.

---

# PH20 - ALM, Deployment and Operational Handover

Gate: `PH20-G01 - Production release readiness approved`

Entry: PH19 passed; target downstream environments and deployment authority available; production release decision remains human-controlled.

Tickets:
- `PH20-G01-T01 ALM` Finalize versioning, managed-solution, pipeline and environment-configuration release design - 5 pts - ALM.
- `PH20-G01-T02 ALM` Validate solution dependency/connection/environment-variable readiness - 3 pts - ALM.
- `PH20-G01-T03 TEST` Perform release-candidate regression and deployment rehearsal - 5 pts - TEST.
- `PH20-G01-T04 DOC` Produce operational handover, support, rollback/repair and ownership documentation - 3 pts - PM.
- `PH20-G01-T05 VALIDATE` Human-controlled production release-readiness gate review - 5 pts - PM.

Evidence: pipeline/deployment logs; managed-solution artifact; environment configuration; regression results; handover pack; explicit human approval.

---

# Cross-phase dependency chain

`PH01 -> PH02 -> PH03 -> PH04 -> PH05 -> PH06 -> PH07 -> PH08 -> PH09 -> PH10 -> PH11 -> PH12 -> PH13 -> PH14 -> PH15 -> PH16 -> PH17 -> PH18 -> PH19 -> PH20`

No downstream phase becomes `READY` merely because its ticket plan exists.

# Known unresolved decisions intentionally preserved as tickets

1. Formal verification score threshold - resolved in `PH15-G01-T01` before completion-state implementation.
2. Definition of successful testing for formal completion - resolved in `PH15-G01-T01` before completion-state implementation.
3. Tool 02 platform selection and detailed requirements - resolved in PH18 design tickets before build.
4. Exact downstream deployment target/pipeline configuration - finalized in PH20, while PH02 establishes the solution-first foundation.

# Current execution state

This file is the cross-phase baseline, not the current-task tracker. Current execution state is authoritative in `project-management/PROJECT-CONTROL.md` and the active phase folder.

As of 2026-08-27:

- PH01 is COMPLETE and PH01-G01 PASSED.
- PH02 is active.
- PH02-G01-T01 is COMPLETE.
- PH02-G01-T02 is COMPLETE.
- PH02-G01-T03 is READY and is validation-only against the approved existing `AI King Env` / `GCC AI Champions Power Platform` / `GCC AI Champions` foundation.
- No duplicate publisher or development solution is to be created.
