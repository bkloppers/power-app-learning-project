# Tool 01 - Workflow and State Model

## Status

Business workflow baseline captured. Rating threshold and formal successful-testing criteria remain intentionally unresolved and must be designed before implementation.

## 1. Roles in the Workflow

### Submitter
Owns the prompt submission, develops it through the guided form, may request informal peer ratings before formal submission, responds to verifier change requests, and resubmits when required.

### Peer Rater
A user-selected colleague/friend who can be asked to rate the prompt before formal submission. This is a pre-verification quality-improvement stage and is not equivalent to formal verification.

### Verifier
A member of the designated verifier group. At least two independent verifiers are required for a prompt to complete formal verification. Verifiers may request changes but cannot reject the submission.

### Administrator
Has elevated governance authority. Only the administrator role may reject a prompt. Administrators also retain the previously defined all-record edit/delete capability subject to audit and confirmation controls.

## 2. Selected Workflow

```text
Draft
  |
  | optional peer feedback request
  v
Peer Rating Requested
  |
  | one or more invited peer ratings / comments
  v
Peer Feedback Received
  |
  | submitter improves prompt and chooses formal submission
  v
Submitted for Verification
  |
  v
Under Verification
  |
  | minimum 2 independent verifier reviews required
  |
  +----------------------------+
  |                            |
  | changes required           | verification conditions satisfied
  v                            v
Changes Requested          Verification Agreement Reached
  |                            |
  | submitter edits            | successful testing + score threshold
  v                            | + both verifier agreement
Resubmitted                  v
  |                         Verified / Complete
  +-------------> Under Verification

Administrative exception:
Any governed stage -> Admin Rejected
```

## 3. Pre-Verification Peer Rating Layer

A new business layer exists between the submitter's draft and the formal verifier process.

The submitter may choose **Please rate my prompt** before formal submission.

This layer exists to:

- obtain informal quality feedback from a trusted colleague/friend;
- improve the prompt before it enters the governed verifier queue;
- reduce avoidable verifier rework;
- give users a safe learning loop before formal assessment.

Peer rating is not formal verification.

A peer rater:

- is selected/invited by the submitter;
- rates only the prompt explicitly shared with them;
- may provide feedback;
- does not gain access to all submissions;
- does not count toward the minimum two formal verifier approvals unless that user separately belongs to the verifier group and performs a formal verifier review in the verifier workflow.

## 4. Formal Verification Rule

A prompt requires **at least two independent verifier reviews**.

Completion requires all of the following:

1. Successful testing criteria have been satisfied.
2. The required score threshold has been reached.
3. At least two formal verifier reviews exist.
4. Both required verifiers agree that the prompt is ready.

The exact numeric score threshold is not yet approved.

The exact definition and evidence required for "successful testing" is not yet approved.

These two items must be designed and locked before the workflow can be implemented.

## 5. Verifier Authority

A verifier may:

- review the complete submitted prompt;
- independently score the prompt;
- provide feedback;
- request changes;
- confirm agreement when the prompt satisfies the verification criteria.

A verifier may not:

- permanently reject the submission;
- delete the submission;
- override another verifier's independent score;
- mark the prompt complete unless the full completion rule has been met.

## 6. Changes Requested Loop

When a verifier requests changes:

1. The prompt leaves active completion consideration and enters **Changes Requested**.
2. The submitter receives the verifier feedback.
3. The submitter edits the prompt.
4. The submitter resubmits it.
5. The prompt returns to **Under Verification**.
6. Formal verifier evaluation is performed again against the revised submission.

Previous review history must not be silently overwritten; the data model must preserve enough review history to show what was reviewed, what changes were requested, and what later review led to completion.

## 7. Administrator Rejection

Only an administrator may reject a prompt.

Administrative rejection is a governed exception rather than a normal verifier outcome.

The design must require:

- an explicit rejection reason;
- confirmation before the action is committed;
- timestamp and administrator identity;
- preservation of sufficient audit history;
- a defined rule for whether an Admin Rejected item can later be restored or resubmitted.

The restore/resubmit rule remains to be confirmed.

## 8. Data-Model Impact

The previously defined Prompt Submissions and Prompt Reviews relationship remains valid, but the workflow introduces an additional logical record type for peer feedback.

```text
Prompt Submission
   |
   +----< Peer Ratings
   |
   +----< Formal Prompt Reviews
```

### Peer Rating record
A peer rating should be stored independently from formal verifier reviews so informal feedback cannot be confused with governed verification.

Candidate fields include:

- Prompt Submission reference;
- invited peer identity;
- requested by identity;
- request timestamp;
- peer score/rating;
- peer feedback;
- response timestamp;
- invitation/response status.

### Formal Prompt Review record
Remains the governed verifier record and contains the formal rating categories, verifier feedback, recommendation, agreement state, and review timestamp.

## 9. Progress Indicator Impact

The submitter's form-completion indicator and the business-process status indicator are different concepts and must be displayed separately.

### Form completion
Shows how much of the six-step submission wizard has been completed.

### Process status
Shows where the prompt is in its lifecycle, for example:

- Draft;
- Peer Rating Requested;
- Peer Feedback Received;
- Submitted for Verification;
- Under Verification;
- Changes Requested;
- Resubmitted;
- Verified / Complete;
- Admin Rejected.

The exact user-facing wording may be refined during UX design, but the business meanings must remain distinct.

## 10. Pending Design Decisions

The workflow cannot be marked implementation-ready until these are resolved:

1. Exact score threshold for completion.
2. Formal definition of successful testing.
3. Whether exactly two verifier agreements are sufficient or whether more verifier reviews may be required in some cases.
4. Whether the two required verifiers are assigned or self-selected from the verifier group.
5. Whether peer rating uses the same five scoring categories as formal verification or a lighter rating model.
6. Whether peer feedback is anonymous or identified to the submitter.
7. Whether an Admin Rejected prompt can be restored/resubmitted.
8. Notification rules for peer requests, formal submission, changes requested, resubmission, verification completion, and admin rejection.

## 11. Locked Business Rules from Current Discussion

The following are now treated as requirements:

- minimum two formal verifiers;
- verifiers may request changes;
- submitter must resubmit after making requested changes;
- completion requires successful testing, an approved score threshold, and agreement by both required verifiers;
- verifiers cannot reject;
- administrators can reject;
- a peer-rating layer exists before formal verification;
- submitters can ask a selected colleague/friend to rate a prompt before formal submission;
- peer rating is distinct from formal verifier review.
