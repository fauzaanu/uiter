# Color Palette

> Measures whether color is restrained, purposeful, and used to convey meaning rather than decoration.

## What it measures

- The number of distinct hues on one screen, and whether each has a stated role (neutral surface, text, brand accent, status, data category).
- Whether color marks something that matters (an action, a state, a selection, a category) or only decorates a surface, header, icon, or background.
- Whether the same meaning uses the same color everywhere on the screen, and whether status colors follow conventional mappings (red for error, amber for caution, green for success).
- Whether every colored signal is duplicated by a non-color cue (text, icon shape, position, pattern, or underline).
- The approximate share of the visible area taken by saturated color compared with neutrals.

## Research basis

- Color may not be the only visual means of conveying information, indicating an action, prompting a response, or distinguishing an element. The W3C explicitly notes this does not discourage color use when it is redundant with another cue. Source: W3C, "Understanding SC 1.4.1: Use of Color" (WCAG 2.1 and 2.2 editions), https://www.w3.org/WAI/WCAG21/Understanding/use-of-color and https://w3.org/WAI/WCAG22/Understanding/use-of-color.html
- Where color distinguishes link text from body text, the WCAG 2.1 Understanding document notes that palette limits can make it impossible to reach 3:1 contrast between link and non-link text, and 4.5:1 for all text, using color alone. Source: same W3C Understanding document, WCAG 2.1 edition.
- Categorical palettes trade discriminability against aesthetic preference: hue similarity raises preference but lowers discriminability. Colorgorical generates palettes from perceptual distance and preference weights and reports 3-, 5-, and 8-color palettes as balanced. Source: Gramazio, Laidlaw, and Schloss, "Colorgorical: Creating Discriminable and Preferable Color Palettes for Information Visualization," IEEE TVCG (2017), PDF at https://connorgr.github.io/pdf/gramazio-2016-ccd.pdf. The venue is taken from search-result summaries; the full paper was not retrieved.
- Affective responses to color depend on palette composition, not only on single hues. Palettes in visualization typically use fewer colors than design palettes. Source: "Affective Color in Visualization," CHI 2017, https://tableau.com/sites/default/files/2023-01/Affective%20Color%20CHI%202017.pdf. Author list was not captured from search results.
- Practitioner guidance from Blender's interface guidelines advises against accent colors where nothing needs attention, because they add visual noise, and against color as the sole status signal. Source: Blender Developer Documentation, "Human Interface Guidelines: Color," https://developer.blender.org/docs/features/interface/human_interface_guidelines/color/ (practitioner guidance, not controlled research).
- Windows UX guidance assigns red to problems or errors, yellow to caution, and green to good, and asks for consistent use so color does not confuse. Source: Microsoft, "Visual color" (Windows Win32 UX guide), https://learn.microsoft.com/en-us/Windows/Win32/uxguide/vis-color.

## Scoring method

1. Take one full screen at normal zoom in the default theme. Note the background, surface, and text colors.
2. List every distinct hue that is not a neutral (gray, black, white). Count distinct hues, not tints. Count each brand or status hue once.
3. For each non-neutral hue, write down what it is used for (action, status, selection, category, decoration). Mark any hue with no meaningful role as decorative.
4. Locate every colored element that carries meaning (buttons, badges, links, status text, selected items, chart series). For each, check whether the same meaning uses the same color on other screens shown.
5. Check status colors against the conventional mapping in the rubric. Record any red used for a non-error, or any color reused for two unrelated meanings.
6. For each meaningful colored element, check for a redundant non-color cue (label, icon shape, underline, position). Record the count of meaningful elements with no such cue.
7. Estimate the share of visible area covered by saturated color (eyeball by thirds: under 10 percent, 10 to 30 percent, over 30 percent). Record the estimate.
8. Score against the rubric using the most severe failure found. Record hue count, decorative-hue count, color-only signal count, and the area estimate beside the score.

## Scoring rubric

- **5 (exemplary):** Neutrals dominate. At most one brand accent plus status hues. Every non-neutral hue has a stated role. Status colors follow convention and are consistent across screens. Every meaningful color signal has a redundant non-color cue. Saturated color covers roughly 10 percent of the screen or less.
- **4 (strong):** One minor excess, such as one decorative hue or a single extra accent, with no effect on meaning. All meaningful color signals are redundant with a non-color cue.
- **3 (adequate):** Two or three hues compete for attention, or one meaningful signal relies on color alone. Status meaning is mostly consistent. Saturated color covers about 10 to 30 percent of the screen.
- **2 (weak):** Several decorative hues, or the same color means two different things, or two or more meaningful signals rely on color alone. Status colors are partly unconventional.
- **1 (poor):** Many hues with no clear roles, decorative gradients or multicolor surfaces, and status conveyed mainly by color. Saturated color covers over 30 percent of the screen.
- **0 (severe failure):** Color is the only carrier of critical information across the screen (for example, errors shown only as red), or status colors contradict convention and each other.

## Automated checks (optional)

None reliable; manual review only. Tools such as a contrast calculator can verify text and non-text contrast of colored elements, but they cannot judge purpose, count roles, or detect decorative use. Contrast is scored under its own metric.

## Common failure patterns

- Errors, required fields, or selected states marked only by red or a colored border, which fails the W3C guidance that color cannot be the only visual cue.
- Accent colors applied to headers, icons, and backgrounds that have no action or state meaning, which dilutes the signal where it matters (Blender guidance).
- The same hue assigned to a brand accent and to a status or category, so users cannot tell the meanings apart.
- Unconventional status mappings, such as green for a warning, which conflict with the Windows guidance and force users to learn the palette.
- Many categorical hues in one view; the CHI 2023 scatterplot work reportedly found category judgments harder as category count grows, though the full paper was not verified.

## Sources

1. W3C, "Understanding Success Criterion 1.4.1: Use of Color," WCAG 2.1 and 2.2 editions. https://www.w3.org/WAI/WCAG21/Understanding/use-of-color ; https://w3.org/WAI/WCAG22/Understanding/use-of-color.html
2. Gramazio, C. C., Laidlaw, D. H., and Schloss, K. B. (2017). Colorgorical: Creating Discriminable and Preferable Color Palettes for Information Visualization. IEEE Transactions on Visualization and Computer Graphics. https://connorgr.github.io/pdf/gramazio-2016-ccd.pdf
3. "Affective Color in Visualization." CHI 2017. https://tableau.com/sites/default/files/2023-01/Affective%20Color%20CHI%202017.pdf
4. Blender Developer Documentation, "Human Interface Guidelines: Color." https://developer.blender.org/docs/features/interface/human_interface_guidelines/color/
5. Microsoft, "Visual color," Windows Win32 UX Guide. https://learn.microsoft.com/en-us/Windows/Win32/uxguide/vis-color

## Open questions

- The Colorgorical venue and year are from search summaries, and the full per-size (3, 5, 8 color) results were not verified.
- The Affective Color CHI 2017 authors were not captured; the paper's findings are cited only at the level of its abstract summary.
- A CHI 2023 scatterplot study on category count was reported in search summaries but no verified URL was captured, so it is not cited above.
- No peer-reviewed study was found that directly measures whether restrained palettes improve task performance in general UI screens. The 5-point anchors (roughly 10 percent saturated area, at most one accent) are judgment calls drawn from practitioner guidance, not research thresholds.
- Microsoft Research's icon color study (grayscale versus accent-color variants) was reported only in a blog summary and was not verified, so it is not cited.
- Conflicting guidance: some sources recommend a 60-30-10 proportion; this is practitioner convention and is not backed by the sources above.
