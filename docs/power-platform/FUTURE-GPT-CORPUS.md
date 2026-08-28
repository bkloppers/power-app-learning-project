# Future Power Platform GPT Corpus

Status: APPROVED / LOCKED PROJECT END-STATE
Baseline: August 2026

## Objective

At the end of this project, the material under `docs/power-platform/` will be used as the primary knowledge corpus for a dedicated ChatGPT GPT focused on Microsoft Power Platform, with Power Apps as the principal implementation focus.

This is not an end-of-project cleanup task. The corpus must be built continuously while the project is executed.

## Corpus construction rules

Each area guide must be written so that a future specialist GPT can teach and support a maker without access to the original chat history.

The corpus must preserve and clearly distinguish:

1. **Verified project procedure** — a sequence executed and/or confirmed from project snapshots or validated project evidence.
2. **Microsoft-verified product guidance** — current Microsoft documentation confirms the behavior or recommendation, even if the project has not yet executed it.
3. **Project-specific decision or standard** — conventions and architectural choices adopted for this project, such as reusable-first architecture, responsive-first Canvas Apps, naming, branding and ALM rules.
4. **Superseded or incorrect guidance** — earlier instructions that were disproved or replaced, including the verified reason and corrected procedure.

## Required content quality

Area guides should progressively capture:

- exact step-by-step procedures;
- current UI navigation paths and menu contents;
- snapshot-verified properties and configuration;
- Power Fx formulas with purpose, dependencies and validation;
- reusable component patterns and contracts;
- naming and variable standards;
- responsive layout rules;
- solution, ALM and administration procedures;
- data-source and integration setup;
- Power Automate, Dataverse, SharePoint/Microsoft Lists and Teams guidance when covered;
- Copilot/AI guidance when covered;
- errors encountered and verified fixes;
- prerequisites and dependency checks;
- validation criteria and expected results;
- explicit corrections for obsolete or inaccurate instructions;
- explanations of why a step or pattern is used when that knowledge is required to teach the subject correctly.

## Snapshot requirement

Every relevant project snapshot remains evidence for the active area guide. Snapshot-derived facts must not be rewritten as generic product facts unless separately verified against current Microsoft guidance.

## End-state

The project should finish with a structured, area-based Power Platform knowledge base that can be supplied to a dedicated Power Platform / Power Apps GPT with minimal restructuring and without depending on historical conversation transcripts.
