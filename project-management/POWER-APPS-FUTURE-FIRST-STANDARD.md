# Power Apps Future-First Standard

## Status

GOVERNING PROJECT STANDARD

## Rule

This project must use the latest supported Power Apps and Power Platform capabilities, patterns, functions, controls, release guidance, tooling, and application architecture available at the time each design or implementation ticket is executed.

The project must not preserve an older pattern merely because it was historically common, easier to explain, or appears in older examples.

## Source Priority

For every Power Apps technical ticket, verify the current product direction before implementation using this precedence:

1. Current Microsoft Learn product documentation.
2. Current Microsoft Power Platform release plans and change history.
3. Current generally available Power Apps capabilities and Studio behavior.
4. Current project-specific standards, provided they do not conflict with newer Microsoft product direction.
5. Older examples or legacy guidance only for historical context, never as the implementation default.

## Production Capability Rule

Use the newest production-suitable capability as the default.

When a newer capability is:

- **Generally Available (GA):** prefer it when it is the current recommended production direction.
- **Public Preview:** evaluate it deliberately, label it as preview, verify tenant/environment availability, governance, support, limitations, and production suitability before adopting it.
- **Planned / not released:** account for it in architecture where useful, but do not implement against an unavailable capability.
- **Deprecated / superseded / legacy:** do not introduce it into new work unless Microsoft explicitly requires it for a capability that has no current replacement and the decision is recorded.

"Future-first" therefore means newest supported and strategically forward-compatible, not blindly using unreleased or unsupported functionality.

## Required Pre-Ticket Freshness Check

Before starting any Power Apps technical ticket, the responsible human or agent must check whether relevant product guidance or capabilities have changed since the project document was written.

The check must cover, where applicable:

- Power Apps release wave and change history;
- Canvas App capabilities;
- modern controls and their current versions/properties;
- responsive layout capabilities and templates;
- Power Fx functions and formula guidance;
- App object capabilities;
- named formulas and state-management guidance;
- data-source and delegation behavior;
- Microsoft Lists / SharePoint integration capabilities;
- Dataverse capabilities where relevant;
- Power Automate connectors/actions;
- Teams integration;
- Copilot Studio / AI / agent capabilities;
- security and governance guidance;
- ALM, solutions, pipelines, Git/source control, and maker/developer tooling;
- monitoring, testing, checker, and diagnostics capabilities.

If current Microsoft guidance conflicts with an older project document, the conflict must be surfaced and the affected project standard updated before implementation proceeds.

## Current 2026 Direction Recorded for This Project

As of August 2026, Microsoft is explicitly continuing to modernize Power Apps around modern controls, responsive app experiences, improved enterprise-scale tooling, and expanded AI capabilities. Modern controls received version/property updates beginning in February 2026, so control versions and property names must be checked rather than assumed from older examples.

The 2026 release wave 1 runs from April through September 2026. Features in release plans can move, so release status must be checked at the time of implementation rather than copied once into the project and treated as permanently current.

## Examples of Legacy Defaults We Must Not Reintroduce

Do not default to:

- giant `App.OnStart` initialization blocks;
- navigation from `App.OnStart` when `App.StartScreen` is appropriate;
- collections as substitutes for proper data-source querying;
- fixed `X`/`Y` desktop layouts for responsive Teams applications;
- classic controls when the current modern control is production-suitable;
- UI visibility as security;
- hard-coded environment-specific values;
- unmanaged production deployment practices;
- obsolete Power Apps features simply because older tutorials use them;
- old property names or formulas when current control versions have superseded them.

## Learning Rule

Because this is also a learning project, every phase must teach the current Power Apps model rather than teach a legacy technique first and replace it later.

Where understanding historical behavior is useful, it may be explained as background, but the Lab and Demonstration must implement the current selected best-practice approach.

## Agent Rule

Future agents must not rely solely on their training knowledge for version-sensitive Power Apps questions.

Before making a version-sensitive technical decision, they must verify current Microsoft documentation/release information where available and record material changes that affect the project.

## Definition of Compliance

A ticket complies with this standard when:

- current Microsoft direction was checked where version sensitivity matters;
- the newest production-suitable capability was selected;
- preview/planned features are explicitly identified and not silently treated as GA;
- deprecated or superseded techniques were avoided;
- project documentation was updated when product evolution changed an earlier design assumption;
- the learner is taught the current implementation model.
