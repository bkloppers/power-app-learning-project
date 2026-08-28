# NTT DATA Icon Sizing Evidence

Status: ACTIVE / USER-SUPPLIED BRAND-SOURCE EVIDENCE
Baseline: 2026-08-28

This record captures three user-supplied NTT DATA Brand Portal screenshots that define icon sizing and clearspace rules. These screenshots are authoritative project evidence for icon sizing unless superseded by a newer NTT DATA source.

## UI-028 — Main navigation icons

Screenshot text establishes:

- Main navigation icons fit into a `30 x 30 px` container.
- Neither icon height nor width should exceed that `30 x 30 px` container.
- An additional `15 px` clearspace is created around the icon.
- Main-navigation icons are accompanied by a one-word label describing the section or information node.
- For mobile breakpoints, these main-navigation icons are discarded.

Power Apps translation:

- main-navigation glyph bounding box: maximum `30 x 30`;
- clearspace: `15 px` on each side around that icon area;
- full nominal footprint when the clearspace is represented by the control/container: `60 x 60 px`;
- desktop/tablet navigation items using this main-navigation pattern include a one-word label;
- the main-navigation icon itself is not retained in the mobile form of that pattern.

Do not apply this main-navigation rule automatically to header utility controls such as Back or hamburger/menu; those are governed by the toolbar/general icon sizing evidence below unless a more specific Site Header rule overrides it.

## UI-029 — Toolbar icons

Screenshot text establishes:

- tool/utility bars may use additional icons to aid user guidance across an application;
- toolbar icons should be vertically aligned with their accompanying label;
- toolbar icons must not exceed `24 x 24 px`;
- there is a `10 px` space before the accompanying text.

Power Apps translation:

- toolbar/utility glyph bounding box: maximum `24 x 24`;
- when a text label accompanies the glyph, use `10 px` icon-to-text spacing;
- vertical centering must align icon and label as one utility control.

## UI-030 — General icon size and clearspace

Screenshot text establishes:

- adequate space is required around an icon for legibility and touch;
- general clearspace is `50%` of the icon height;
- explicit example: a `24 px` high icon creates `12 px` clearspace;
- in general, an icon should not exceed the font size of its related content;
- exceptions are main navigation and special contextual uses such as a large dominant search field.

Power Apps translation for a 24 px toolbar/utility glyph:

- glyph: `24 x 24 px` maximum;
- clearspace: `12 px` around the glyph;
- full nominal touch/control footprint: `48 x 48 px` when that clearspace is represented around all four sides.

This supersedes the previously planned `40 x 40` shell-icon control sizing. For branded header utility icons such as Back and hamburger/menu, the selected baseline is now a maximum 24 px glyph inside a 48 x 48 px interactive/control footprint, subject to any more-specific value later proven by the Basecoat Site Header module.

## Current cmpAppHeader impact

No Power Apps change has yet been made from these screenshots.

Required correction before the header is complete:

- `btnHeaderBack` must not remain a 40 x 40 Fluent-icon implementation;
- use the verified Basecoat Icons-module glyph;
- target a maximum `24 x 24 px` glyph;
- target a `48 x 48 px` control/touch footprint from the documented 50% clearspace rule;
- retain `OnSelect = cmpAppHeader.OnBack()` and the existing component behavior contract.

For the planned hamburger/menu control:

- use the Basecoat Icons-module glyph from the first implementation;
- maximum glyph size `24 x 24 px`;
- nominal control/touch footprint `48 x 48 px`;
- final placement remains governed by the Site Header module.

## Evidence classification

These values are USER-SUPPLIED BRAND-SOURCE / SNAPSHOT-VERIFIED evidence. They are not Microsoft Power Apps product rules. Power Apps control mechanics still require current Microsoft guidance and Studio verification during implementation.
