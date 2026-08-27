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

## UI-024 — Incorrect media filename reference rejected

Observed in `imgHeaderLogo.Image` after entering an `If()` formula that referenced the uploaded SVG filenames including the `.svg` extension.

Snapshot directly proves:

- `imgHeaderLogo` is inside `conHeaderBrandRow` -> `conHeaderRootRow` -> `cmpAppHeader`.
- The formula parser reports: `The function 'If' has some invalid arguments.`
- The media arguments with `.svg` extensions are underlined as invalid.

Correction:

Microsoft's current multimedia guidance states that the Image property should reference the uploaded image file name **without its extension**. Therefore the Power Apps media resource identifiers for the two selected SVG files are:

- `GlobalLogo_NTTDATA_White_SVG`
- `GlobalLogo_NTTDATA_FutureBlue_SVG`

Correct formula:

```powerfx
If(
    cmpAppHeader.DarkMode,
    GlobalLogo_NTTDATA_White_SVG,
    GlobalLogo_NTTDATA_FutureBlue_SVG
)
```

This supersedes the earlier formula that included `.svg` in the references.

Next step: enter the corrected formula and verify the parser error clears and the expected logo renders.
