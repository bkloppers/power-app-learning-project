# Basecoat Logos Module Source

Status: ACTIVE / BRAND-SOURCE IDENTIFIED / IMPLEMENTATION DETAILS PENDING SOURCE EXTRACTION
Baseline: 2026-08-28

## Authoritative source supplied by user

NTT DATA Basecoat Logos module documentation:

`https://basecoat.nttdata.com/css-modules/logos.html`

NTT DATA Basecoat Logos module CSS:

`https://basecoat.nttdata.com/5/css/module.logos.min.css`

## Scope established by this source

The Basecoat Logos module is the authoritative source for the branded header logo lockup, including the relationship between:

- the NTT DATA horizontal Global Logo;
- the vertical logo divider/pipe used beside modifier/application text;
- the modifier/application heading/text positioned beside the logo.

This supersedes treating the divider and application title as independently invented visual elements.

## cmpAppHeader impact

The current `cmpAppHeader` already contains:

- `imgHeaderLogo`
- `conHeaderDivider`
- `lblHeaderAppTitle`

Those controls remain structurally appropriate, but their final dimensions, spacing, typography, divider treatment, and alignment must be derived from the Basecoat Logos module rather than from approximation.

Current values such as divider `Width = 1`, divider `Height = 32`, title `Size = 12`, and the current gap values are therefore implementation state only until verified against the Logos module.

The project remains brand-first: do not continue by treating the current approximation as final.

## Verification boundary

The supplied Basecoat URLs could not be retrieved through the current web environment on 2026-08-28. Therefore this record stores the exact authoritative source locations and scope without inventing CSS selectors, class names, pixel values, font sizes, margins, line heights, or responsive rules not yet extracted from those sources.

## Required next action

Before finalizing the logo/divider/title lockup in Power Apps, obtain and inspect the Logos module documentation/CSS content, map the exact Basecoat values to Power Apps controls, then validate the rendered result in Studio.
