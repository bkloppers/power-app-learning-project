# Basecoat Site Header Module Source

Status: AUTHORITATIVE SOURCE / IMPLEMENTATION REVIEW PENDING
Baseline: 2026-08-28

## Supplied source

The NTT DATA Basecoat Site Header module is the authoritative source for the application header shell:

- Documentation: `https://basecoat.nttdata.com/css-modules/site-header.html`
- CSS: `https://basecoat.nttdata.com/5/css/module.site-header.min.css`

The current web environment could not fetch either resource on 2026-08-28, so no selectors, exact dimensions, margins, breakpoints, states, or CSS values are inferred here.

## Module ownership hierarchy

For `cmpAppHeader`, use the Basecoat modules in this order of responsibility:

1. `site-header` — overall header shell structure, spacing, presentation and site-header behavior.
2. `logos` — NTT DATA logo + divider + modifier/application heading lockup inside the header.
3. `icons` — generic UI glyphs used in the header, such as back and hamburger/menu.
4. `close` — dedicated Close/X control where a drawer/sidebar close control is required.
5. NTT DATA Brand Icons library — content-facing/brand illustrative icons, not generic shell chrome.

## Current cmpAppHeader consequence

The current component tree may remain structurally useful, but the following values are not brand-final until verified against the Site Header module and its dependent module patterns:

- component/header shell height;
- outer left/right padding;
- spacing between brand and utility regions;
- background/border treatment;
- bottom accent rule treatment;
- utility-control placement;
- mobile/tablet hamburger placement and visibility behavior;
- Avatar/utility alignment and spacing.

The logo-divider-heading trio is governed by the separate Basecoat Logos module and must be validated together as a single lockup.

## Brand-first rule

Do not tune the Power Apps header by visual approximation when a Basecoat module defines the pattern. Resolve the relevant Basecoat source first, then translate the verified pattern to responsive Power Apps controls and formulas.

## Verification boundary

No Power Apps control or property changes are authorized from this source record alone because the exact Site Header CSS could not be retrieved in the current environment. The source establishes module ownership and the next verification dependency only.
