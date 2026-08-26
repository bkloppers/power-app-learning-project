# Tool 02 - AI Prompt Chatbot

## Status

Confirmed future tool. Detailed requirements are intentionally deferred until Tool 01 business-process definition is complete.

## Purpose

Tool 02 will provide an AI Prompt Chatbot capability inside the same Microsoft Teams-hosted Power Apps solution.

The chatbot must be treated as a first-class module in the application architecture, not as an afterthought added after Tool 01 is complete.

## Architectural Implication

The application shell must support multiple tools from the first build phase.

Current confirmed tool map:

```text
Application Shell
├── Tool 01 - AI Prompt Capture, Submission and Verification
└── Tool 02 - AI Prompt Chatbot
```

Future tools may be added under the same shell.

This requires shared concerns to remain outside individual tools, including:

- application navigation;
- role detection;
- branding and theme;
- responsive layout;
- shared header/sidebar components;
- loading, dialog, toast, and error patterns;
- application-level security context;
- shared configuration;
- future extensibility.

## Relationship to Tool 01

Tool 02 must be designed so it can later work with the prompt knowledge captured and verified through Tool 01 where business rules permit.

Potential relationships that must be considered in later design phases include:

- using verified prompts as chatbot knowledge or examples;
- helping users discover approved prompts;
- helping users construct or improve prompts before submission;
- guiding users toward the correct Tool 01 submission fields;
- linking chatbot conversations to prompt records where appropriate.

These are architectural considerations only. They are not yet approved functional requirements.

## Data and Security Boundary

The chatbot must not automatically gain access to all Tool 01 data merely because both tools live in the same app.

Any future integration between Tool 01 and Tool 02 must respect:

- submitter ownership restrictions;
- verifier access rules;
- administrator permissions;
- confidential/sensitive-data controls;
- approved prompt-publication status;
- least-privilege access.

## Learning-Programme Impact

The hierarchy learning plan must avoid designing Tool 01-specific navigation or state that blocks a second tool.

When the project reaches components, navigation, data, connectors, AI/Copilot integration, security, and application architecture phases, Tool 02 must be considered as a known future dependency.

## Requirements Still to Define

Before Tool 02 implementation begins, define:

1. chatbot platform and hosting model;
2. whether the chatbot is embedded directly in the Canvas App or launched through another Teams experience;
3. permitted knowledge sources;
4. whether only verified prompts may be surfaced;
5. whether chat history is stored;
6. whether users can submit a chatbot-created prompt directly into Tool 01;
7. whether the chatbot may read the current user's own draft prompts;
8. whether verifier/admin capabilities are exposed through chat;
9. data-loss-prevention and governance requirements;
10. audit, telemetry, and safety requirements.

## Current Decision Boundary

Tool 02 is confirmed as part of the future application scope. Its existence must influence the shared shell and modular architecture now, but its detailed implementation will not be invented before its business requirements are defined.
