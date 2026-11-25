# Theme Parity

> Measures whether light, dark, and other themes preserve the same legibility, hierarchy, and meaning.

## What it measures
- Text and icon contrast in each theme, measured against that theme's own background, at the same thresholds in every theme.
- Typographic hierarchy (page title, section heading, body, caption, primary action) staying in the same order and distinguishable in each theme.
- Semantic meaning (error, success, warning, selected, disabled) carried by the same non-color cue in each theme, with the hue family preserved.
- Focus indicators and component boundaries remaining visible in each theme.
- Images, logos, charts, and icons designed for one background remaining legible on the others.

## Research basis
- Under simulated daytime lighting, contrast polarity had no significant effect on performance. At night, light-on-dark was worse, most strongly for small text. Source: Nielsen Norman Group, "Dark Mode," https://www.nngroup.com/articles/dark-mode/ (summarizing the MIT AgeLab study by Dobres and colleagues). NN/g states it did not conduct its own dark-mode research, so the primary study was not checked here.
- Text needs at least 4.5:1 contrast against its background, and large text at least 3:1. Source: W3C, "Understanding SC 1.4.3: Contrast (Minimum)," WCAG 2.2, https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- Visual information required to identify UI components and meaningful graphics needs at least 3:1 against adjacent colors. Source: W3C, "Understanding SC 1.4.11: Non-text Contrast," WCAG 2.2, https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- Light and dark polarity were compared for accuracy and completion time across bar, line, and scatter chart tasks in a crowdsourced study with 134 participants. Source: While and Sarvghad, arXiv:2409.10841, https://arxiv.org/abs/2409.10841v1. The reported results were not verified; the source is cited only to support that polarity effects are tested per task.

## Scoring method
1. Capture the same screen, viewport, and interaction state (default, hover, focus, error) in every shipped theme, including light and dark.
2. Inventory text, icons, borders, focus rings, status colors, and images. Read the resolved foreground and background colors per theme from computed styles, not from design tokens.
3. Compute each text and non-text contrast ratio with the WCAG relative-luminance formula. Apply 4.5:1 to normal text, 3:1 to large text (18pt regular or 14pt bold), and 3:1 to UI components and meaningful graphics. Record the worst failing pair per theme. Exclude disabled controls and purely decorative elements, and note each exclusion.
4. Compare hierarchy. List the five levels above in each theme and mark whether each remains distinct from its neighbors and keeps its rank order.
5. Check meaning. For each semantic color, confirm the same text, icon, or shape appears in each theme and that the color still reads as the same family.
6. Check assets. Confirm that transparent or single-background images, logos, and chart marks remain visible without dark or light halos.
7. Record per theme: failing pairs (count and worst ratio), hierarchy mismatches, meaning mismatches, and assets that fail. Assign the rubric score from the worst theme, not the average.

## Scoring rubric
- **0 - Severe failure:** In at least one theme, primary text or the primary action is unreadable, or an error or selected state is indistinguishable from its normal state.
- **1 - Major failure:** In one theme, several text pairs fall below their threshold, or two or more hierarchy levels merge.
- **2 - Partial:** Failing pairs are limited to secondary elements, or one semantic color is the only cue in one theme.
- **3 - Acceptable:** Primary text and controls pass in every theme. Hierarchy and meaning differ only in secondary elements.
- **4 - Strong:** All text and required non-text pairs pass in every theme. Hierarchy and semantic cues match, with at most one cosmetic difference.
- **5 - Exemplary:** Every theme passes all thresholds. Hierarchy and meaning are structurally identical, and every theme was checked in the same state, including focus and assets.

## Automated checks (optional)
axe-core's `color-contrast` rule can run in each theme to flag text contrast failures on rendered pages. It cannot judge hierarchy or semantic meaning, reports "incomplete" for text over images or gradients, and does not check non-text contrast in general. Manual review is still required for the remaining checks.

## Common failure patterns
- Hard-coded hex values in components that do not switch with theme tokens, leaving light text on a light surface in dark mode.
- Pure black or pure white backgrounds in dark themes, where small text is hardest to read at night (per the NN/g summary of Dobres and colleagues).
- Semantic colors retuned per theme so that hue drifts, for example a red error that reads as orange in dark mode.
- Borders and shadows that disappear on dark surfaces, removing component boundaries that 1.4.11 requires.
- Hierarchy created by shadow in light and by lightness in dark, so the levels do not map one to one across themes.

## Sources
- Nielsen Norman Group, "Dark Mode." https://www.nngroup.com/articles/dark-mode/
- W3C, "Understanding SC 1.4.3: Contrast (Minimum)," WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- W3C, "Understanding SC 1.4.11: Non-text Contrast," WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- While and Sarvghad, arXiv:2409.10841, 2024. https://arxiv.org/abs/2409.10841v1

## Open questions
- The MIT AgeLab study (Dobres and colleagues) was not retrieved. Its date and venue are unconfirmed, and the claim rests on the NN/g summary.
- Palmen, Gilbert, and Crossland, "How bold can we be?" (CHI 2023), was seen only as a citation in a course slide deck. Its findings on font weight and polarity are unverified and are not used here.
- The While and Sarvghad results (direction and size of any polarity effect) were not verified.
- No source was found on structural parity of hierarchy or semantic meaning across themes. Those checks and the rubric's distinction between levels 2 and 3 are judgment calls, not research-backed.
- The large-text threshold (18pt or 14pt bold) comes from a secondary summary, not from the W3C page's text, which was seen only in search snippets.
- Thresholds for high-contrast or sepia themes were not researched. The same thresholds are applied.
- Whether 1.4.11 applies to inactive components is taken from a secondary summary of the WCAG 2.1 page and is treated as exempt here.
