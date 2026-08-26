# Tool 01 - AI Prompt Capture, Submission and Verification

## Status

Initial business requirements captured. Detailed workflow states and verification rules remain to be confirmed before implementation.

## 1. Purpose

Tool 01 replaces the existing **AI Prompt Submission Template** Word document with a structured digital application running inside Microsoft Teams.

The purpose of the existing template is to capture prompts that have delivered practical value, measurable productivity improvement, or identified a future automation opportunity, while keeping submissions concise, evidence-based, and reusable by other teams.

This tool is the first module in a larger Power Apps application. The application shell and navigation must therefore be designed so additional tools can be introduced later without rebuilding the solution architecture.

## 2. Selected Platform Direction

- User experience: Power Apps Canvas App embedded in Microsoft Teams.
- Primary data platform for Tool 01: Microsoft Lists / SharePoint Lists.
- Application structure: one reusable app shell containing modular tools.
- Tool 01 interaction pattern: multi-step guided form, not one long scrolling page.
- Security: enforced at the SharePoint/List permission layer as well as reflected in the Canvas App user experience.

## 3. User Roles

### 3.1 Submitter

A standard user must be able to:

- create a new prompt submission;
- save and continue through multiple form sections;
- see a visual completion indicator showing progress through the submission;
- submit the completed prompt for verification;
- see their own submitted prompts;
- reopen their own prompt when the workflow permits editing or when changes are requested;
- see verifier feedback on their own submission;
- not browse, open, edit, or view other users' submissions.

### 3.2 Verifier

Members of the designated verifier group must be able to:

- see all prompt submissions requiring verification;
- access all prompt submissions from within the app;
- inspect the complete submitted prompt;
- independently score the prompt;
- provide verifier feedback;
- participate in the defined verification workflow;
- see the current process/status phase of each prompt.

The original Word template requires each reviewer to independently score the prompt from 1 to 5 and uses the average score to determine readiness for reuse, improvement, or showcase consideration. This means verifier responses must be stored as separate review records rather than as a fixed set of reviewer columns on the prompt submission record.

### 3.3 Administrator

Members of the designated administrator group must be able to:

- see all prompt submissions;
- see all review records;
- edit any prompt submission;
- delete prompt submissions when authorized by the business process;
- correct or administer supporting reference/configuration data;
- access administrative functions that normal users and verifiers cannot access.

Administrator capability is the third access layer. Administrative permissions must not be implemented merely by hiding controls; permissions must also be enforced at the data layer.

## 4. Core User Experience

### 4.1 App Shell

Tool 01 will live inside a reusable application shell designed to host additional tools later.

The shell will eventually provide:

- NTT DATA branded header;
- responsive navigation/sidebar;
- main content region;
- role-aware navigation;
- Tool 01 entry point;
- future tool entry points without requiring a second application shell;
- standard dialogs, toasts, loading states, and error handling.

### 4.2 Guided Form Pattern

The Prompt Submission form must use a guided multi-step pattern.

The user must not be presented with all fields on one long scrolling page.

The form will provide:

- a clear section/step title;
- Back and Next navigation;
- section validation before progression where appropriate;
- Save Draft behaviour;
- visual completion/progress indicator;
- final review and submission action;
- preservation of entered values while navigating between sections.

Progress must communicate both current position and overall completion. It must not rely on colour alone; text/state indicators must remain understandable for accessibility.

## 5. Source Word Template - Business Sections

The current Word document contains the following business sections and these remain the initial source requirements for Tool 01.

1. Individual Details
2. Prompt Information
3. Prompt Used
4. AI Tool Used
5. Outcome Achieved
6. Productivity Impact
7. Reusability Assessment
8. Lessons Learned
9. Future Automation Opportunity
10. Peer Rating
11. Knowledge Sharing Recommendation
12. Executive Summary
13. Prompt Quality Checklist before final submission

The digital application may group these business sections into fewer user-facing steps for usability, but no source requirement may be removed without an approved design decision.

## 6. Proposed Submission Wizard Grouping

The current design grouping is:

### Step 1 - Submitter and Prompt Context

Source sections:
- Individual Details
- Prompt Information

Captures:
- individual name;
- technology stream;
- submission date;
- prompt name;
- business problem;
- type of work.

### Step 2 - Prompt and AI Tool

Source sections:
- Prompt Used
- AI Tool Used

Captures:
- exact prompt text;
- AI tool used.

### Step 3 - Outcome and Productivity Impact

Source sections:
- Outcome Achieved
- Productivity Impact

Captures:
- output type;
- result description;
- time before AI;
- time after AI;
- estimated time saved;
- quality-improvement categories.

### Step 4 - Reusability and Lessons Learned

Source sections:
- Reusability Assessment
- Lessons Learned

Captures:
- whether others can reuse the prompt;
- beneficiary groups;
- what worked well;
- what could be improved.

### Step 5 - Automation Opportunity and Executive Summary

Source sections:
- Future Automation Opportunity
- Executive Summary

Captures:
- whether an automation opportunity exists;
- automation-opportunity description when applicable;
- mandatory impact statement.

The executive-summary wording must respond to the automation answer rather than showing two competing manual template statements.

### Step 6 - Quality Check and Submit

Source section:
- Prompt Quality Checklist

The submitter confirms that the prompt:

- has a clear role or context;
- states the required output format;
- includes source information or assumptions;
- can be reused by others;
- has measurable value or learning attached;
- does not include sensitive client or confidential data.

This step will also present a final review summary before submission.

### Verifier Workspace - Peer Rating and Recommendation

Source sections:
- Peer Rating
- Knowledge Sharing Recommendation

These sections belong to the verifier workflow and are not editable by the submitter after submission.

Verifier rating categories from the source document are:

- Business Value;
- Time Saving;
- Ease of Use;
- Reusability;
- Innovation.

Knowledge-sharing recommendations from the source document are:

- Add to Prompt Library;
- Demonstrate at Next AI Champion Session;
- Candidate for Automation / Agent Development;
- Requires Further Testing.

Verifier feedback will be added as a digital requirement even though the Word template does not contain a dedicated general-feedback field, because verifier feedback is an explicit application requirement.

## 7. Initial Screen/Workspace Architecture

Exact names will be finalized using the project naming standard.

The required functional workspaces are:

1. **Home / Tool Launcher** - entry point to Tool 01 and future tools.
2. **My Prompts** - submitter view of their own drafts and submissions.
3. **Prompt Submission Wizard** - multi-step capture/edit experience.
4. **Prompt Review / Summary** - final submitter review before submission and read-only submitted view.
5. **Verifier Queue** - verifier view across all applicable submissions.
6. **Verification Workspace** - full prompt details, independent ratings, feedback, and verifier actions.
7. **Administration Workspace** - administrative access to all prompt and review records plus controlled edit/delete functions.

Role-aware navigation determines which workspaces are exposed, but data-layer permissions remain authoritative.

## 8. Data Model Direction

### 8.1 Microsoft List - Prompt Submissions

One item represents one prompt submission.

The list will contain the submitter-owned business record, including:

- ownership/submitted-by identity;
- source Word-template fields from sections 1-9 and 12;
- quality-check confirmations;
- draft/completion metadata;
- current workflow status;
- created/modified audit metadata;
- submission timestamp;
- verification outcome metadata where a summary value is needed on the parent record.

### 8.2 Microsoft List - Prompt Reviews

One item represents one verifier's review of one prompt submission.

Required relationship:

`Prompt Submission 1 -> many Prompt Reviews`

A review record will contain:

- Prompt Submission reference;
- verifier identity;
- Business Value score;
- Time Saving score;
- Ease of Use score;
- Reusability score;
- Innovation score;
- verifier feedback;
- knowledge-sharing recommendation;
- review status;
- review timestamp.

Average scores are calculated from review records rather than stored as R1/R2/R3/R4/R5 columns on Prompt Submissions.

### 8.3 Reference / Configuration Data

Reference values that are expected to change without modifying app formulas should be maintained as governed reference/configuration data. Candidate values include:

- Technology Streams;
- Types of Work;
- AI Tools;
- Output Types;
- Quality Improvement choices;
- Beneficiary groups;
- Knowledge Sharing Recommendations.

The final number and shape of supporting Lists will be defined during the data-model learning phase rather than prematurely creating many small Lists.

## 9. Security Model

Security must exist independently of Canvas App visibility logic.

### Submitter data access

- submitter may access only items they own / are authorized to access;
- submitter cannot enumerate or open other users' prompt submissions;
- submitter cannot access another user's review data.

### Verifier data access

- designated verifier group receives access required to view all prompt submissions under verification;
- verifier group receives access required to create/read applicable review records;
- verifier permissions must be governed through SharePoint/Microsoft 365 group membership and List permissions.

### Administrator data access

- designated administrator group receives the required elevated List permissions;
- edit/delete authority is controlled by group membership and data-layer permissions;
- destructive operations in the app must require explicit confirmation and appropriate audit behaviour.

The exact SharePoint permission implementation must be designed and validated before production because Canvas App filtering is not a security boundary.

## 10. Workflow and Process States

The application requires explicit process and completion phases.

The exact business-approved state model is not yet locked. It must support at minimum the concepts of:

- an incomplete/draft submission;
- a completed submission handed to verification;
- active verifier review;
- verifier feedback requiring submitter action where applicable;
- successful verification/completion;
- administrative handling where required.

State names, permitted transitions, edit rules, and who can perform each transition will be documented as a formal state-transition model before implementation.

No additional workflow states are to be treated as approved until this design step is completed.

## 11. Completion Indicator

The completion indicator is a first-class requirement, not decorative UI.

It must show:

- current wizard step;
- total wizard steps;
- completed steps;
- incomplete steps;
- validation/problem state where a step still requires attention;
- overall completion percentage or equivalent textual completion measure.

Completion will be based on required business fields/checks rather than merely the number of screens visited.

## 12. Teams Requirement

The primary operating context is Microsoft Teams.

The Canvas App must therefore be validated for:

- use as a Teams-hosted application/tab;
- Teams desktop/web dimensions;
- responsive behaviour at narrower widths;
- authenticated Microsoft 365 user context;
- keyboard accessibility;
- no dependency on a large fixed desktop canvas.

Phone/mobile behaviour will be clarified separately. The current business requirement establishes Teams as the primary host but does not yet define whether Teams mobile is a required supported target.

## 13. First Tool of a Multi-Tool Application

Tool 01 must not hard-wire the application shell around prompt submission alone.

The architecture must distinguish between:

- **application shell concerns** - authentication context, role detection, navigation, branding, theme, shared components, error/loading UX;
- **Tool 01 concerns** - prompt submission, prompt review, verifier workflow, prompt administration;
- **future tool concerns** - additional modules introduced later under the same shell.

This separation is required from the first implementation phase so future tools can be added without rebuilding the shell.

## 14. Requirements Still to Confirm

Before Phase 01 can be completed, the following business rules must still be confirmed:

1. Exact workflow/status names and allowed transitions.
2. How many independent verifier reviews are required before a prompt can be considered verified.
3. Whether every verifier may review every prompt or whether submissions are assigned to named verifiers.
4. Whether a submitter may edit a prompt after initial submission without a verifier explicitly returning it for changes.
5. What a successful verification means operationally: verified only, approved for prompt library, published elsewhere, or another outcome.
6. Whether verifier feedback should maintain a full history/thread or only the latest feedback per review.
7. Whether deleted prompts must be soft-deleted/archived rather than permanently deleted.
8. Whether Teams mobile must be supported.
9. Whether notification messages are required when a prompt is submitted, returned for changes, or verified.
10. Whether attachments/evidence files are required in addition to the captured prompt text.

## 15. Current Architecture Decision Boundary

The following direction is sufficiently defined to guide the learning architecture:

- one Canvas App hosted in Microsoft Teams;
- one reusable shell designed for multiple tools;
- Tool 01 is AI Prompt Capture, Submission and Verification;
- Microsoft Lists is the Tool 01 data platform;
- submitters see only their own submissions;
- verifiers access all prompts required for verification and create independent review records;
- administrators have elevated all-record management capability;
- prompt capture is a guided multi-step process with a meaningful completion indicator;
- submission data and reviewer data are separate related records;
- exact workflow transitions remain pending business confirmation.

This is the baseline for mapping the Power Apps hierarchy learning phases.