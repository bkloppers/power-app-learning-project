# Lessons Learned

## LL-001 - Early training governance was too strict

Date: 2026-08-27
Applies from: PH03 onward

### Observation

The PH01-PH02 training/governance setup consumed disproportionate time compared with the Power Apps work completed. The practical Power Apps foundation established so far could have been completed in roughly 20 minutes, while several hours were spent on governance, GitHub workflow, evidence, branch, gate, and control mechanics. The project has not yet progressed to naming and creating the Canvas App.

### Impact

The training objective was diluted by administrative overhead. The learner was spending more time operating the project-management system than learning and building in Power Apps.

### Required correction

From PH03 onward, hands-on Power Apps build progress is the primary activity. Governance must support the build and stay proportionate to the risk of the change.

- Start each phase with the minimum control work required to authorize the next practical build step.
- Batch routine evidence and project-control updates instead of interrupting every small Power Apps action.
- Do not add quiz, exam, or forced knowledge-check activities unless explicitly requested.
- Explain concepts in context while building the real app.
- Keep GitHub, gate, and evidence work in the background wherever it can be automated or completed as one batch.
- Escalate governance effort only for changes that materially affect architecture, security, ALM, data integrity, or production readiness.
- Measure training progress primarily by useful Power Apps capability built and understood, not by the number of governance artifacts produced.

### Immediate consequence

Complete the remaining PH02 gate administration as efficiently as possible, then proceed directly to the next hands-on Power Apps phase. The next practical milestone must include establishing the actual Canvas App identity and beginning the app object rather than introducing further administrative work without a direct build dependency.
