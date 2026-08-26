# Decisions

## DEC-001
Decision: GitHub is the durable source of truth for project state, approved design, phase status, and locked decisions.
Status: LOCKED
Reason: Project continuity must survive changes of ChatGPT session and agent context.
Date: 2026-08-26

## DEC-002
Decision: The learning programme will build one real Canvas app cumulatively through the Power Apps hierarchy rather than use disconnected disposable exercises.
Status: LOCKED
Reason: Every learning activity must contribute directly toward understanding and constructing the intended end application.
Date: 2026-08-26

## DEC-003
Decision: Every hierarchy level will be delivered as Learning Phase -> Lab -> Demonstration -> Understanding.
Status: LOCKED
Reason: Each level must combine conceptual learning, implementation, observable proof, and validated understanding before progression.
Date: 2026-08-26

## DEC-004
Decision: Production-oriented Power Apps best practices apply from the start of the project.
Status: LOCKED
Reason: The learning app must not accumulate temporary architecture that later needs replacement simply because early phases were treated as throwaway training.
Date: 2026-08-26

## DEC-005
Decision: Existing project naming, variable, responsive-layout, App-object, AI implementation guardrail, and NTT DATA design-system standards govern the solution.
Status: LOCKED
Reason: The project already contains researched standards and approved brand information. New implementation must use those sources instead of ad-hoc conventions.
Date: 2026-08-26

## DEC-006
Decision: Maintain one living solution design specification at `docs/solution-design/POWER-APPS-LEARNING-SOLUTION-DESIGN.md` and update it as requirements, architecture, phases, labs, demonstrations, evidence, and deployment design mature.
Status: LOCKED
Reason: The project requires a physical start-to-finish design record rather than relying on chat history.
Date: 2026-08-26

## DEC-007
Decision: The application is a Microsoft Teams-hosted, multi-tool Power Apps Canvas App with one reusable application shell. Tool 01 is AI Prompt Capture, Submission and Verification; Tool 02 is AI Prompt Chatbot; future tools are added under the same shell.
Status: LOCKED
Reason: Approved foundation baseline establishes the application boundary and cumulative multi-tool architecture.
Date: 2026-08-27
Source: `project-management/approvals/APPROVAL-2026-08-27-FOUNDATION-BASELINE.md`

## DEC-008
Decision: Microsoft Lists / SharePoint Lists is the initial Tool 01 data platform. Prompt Submission, Peer Rating, and Formal Review records remain separate where appropriate.
Status: LOCKED
Reason: Approved foundation baseline fixes the initial data-platform direction and preserves scalable related-record design.
Date: 2026-08-27
Source: `project-management/approvals/APPROVAL-2026-08-27-FOUNDATION-BASELINE.md`

## DEC-009
Decision: Tool 01 uses submitter, peer-rater, verifier, and administrator role layers. Peer rating is optional and separate from formal verification. Formal completion requires at least two independent verifiers; verifiers may request changes but cannot reject; administrator retains rejection authority.
Status: LOCKED
Reason: Approved foundation baseline establishes the role and approval boundaries that later security and workflow phases must preserve.
Date: 2026-08-27
Source: `project-management/approvals/APPROVAL-2026-08-27-FOUNDATION-BASELINE.md`

## DEC-010
Decision: GitHub Issues are the operational gate and ticket system. Delivery follows the Process & Progress Framework and the Chat Session Ticket Capacity Model, including a maximum of 5 points and 5 tickets per session batch, same phase/gate/workstream, and one active ticket at a time.
Status: LOCKED
Reason: The approved governance baseline requires durable operational work tracking and controlled specialist handoffs.
Date: 2026-08-27
Source: `project-management/approvals/APPROVAL-2026-08-27-FOUNDATION-BASELINE.md`

## DEC-011
Decision: All Power Apps technical work follows the Future-First Power Apps Standard and must use the newest supported production-suitable capability at ticket execution time, with version-sensitive Microsoft guidance checked before implementation.
Status: LOCKED
Reason: The approved foundation baseline prohibits intentionally teaching or implementing retired, superseded, or unsupported patterns when a current production-suitable capability exists.
Date: 2026-08-27
Source: `project-management/POWER-APPS-FUTURE-FIRST-STANDARD.md`
