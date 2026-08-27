# cmpAppHeader — Media Baseline

Status: ACTIVE / SNAPSHOT-VERIFIED
Library: `Burts Power App Components`
Environment: `AI King Env`

## UI-023 — Approved NTT DATA media assets present

Observed in the Power Apps Studio Media pane for the component library.

Snapshot directly proves the following image resources are present:

- `GlobalLogo_NTTDATA_White_PNG.png`
- `GlobalLogo_NTTDATA_White_SVG.svg`
- `GlobalLogo_NTTDATA_FutureBlue_PNG.png`
- `GlobalLogo_NTTDATA_FutureBlue_SVG.svg`
- `NTTDATA_ICON-192x192.png`

Project decision for `cmpAppHeader`:

- Use the horizontal NTT DATA logo assets, not the standalone icon, for the branded header.
- Prefer the SVG pair for the header image source because the header logo must remain crisp when the component is resized.
- Light presentation uses `GlobalLogo_NTTDATA_FutureBlue_SVG.svg`.
- Dark presentation uses `GlobalLogo_NTTDATA_White_SVG.svg`.
- The consuming app does not supply the logo as a custom property; the logo is an internal library media dependency and only the `DarkMode` input determines which approved variant is shown.

Microsoft-verified behavior:

- Component-library media is defined at library level and is available to components in the library.
- An Image control can reference a local media resource by its media name.

Next step: bind `imgHeaderLogo.Image` to the two approved SVG resources using `cmpAppHeader.DarkMode`.
