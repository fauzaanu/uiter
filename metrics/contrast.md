# Contrast

> Measures the luminance difference between text, icons, and their backgrounds against accessibility thresholds.

## What it measures

- Text color against its immediate background, including placeholder text, helper text, disabled-looking labels, and text on images or gradients.
- Icon and graphic color against adjacent background, for icons that carry meaning (status, action, navigation).
- Boundaries of form fields, buttons, and focus or selected states, where the boundary is the only cue that the control exists or changed state.
- Whether text size and weight are large enough to qualify for the lower large-text threshold.
- Whether the same pairs hold in every theme (light, dark, high contrast).

## Research basis

- WCAG 2.x defines contrast as (L1 + 0.05) / (L2 + 0.05), where L1 is the relative luminance of the lighter color and L2 of the darker, giving 1:1 to 21:1. Source: W3C, "Understanding relative luminance" and "Contrast ratio" (https://www.w3.org/WAI/WCAG22/Understanding/relative-luminance.html).
- Normal text needs at least 4.5:1, and large-scale text at least 3:1 (SC 1.4.3, Level AA). Logotypes and inactive components are exempt. Source: W3C, "Understanding SC 1.4.3 Contrast (Minimum)" (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).
- Meaningful non-text visuals, control boundaries, and state indicators need at least 3:1 against adjacent colors (SC 1.4.11, Level AA). Inactive components are excluded. Source: W3C, "Understanding SC 1.4.11 Non-text Contrast" (https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast).
- Reading rate falls sharply as contrast drops. Legge, Rubin, and Luebker's "Psychophysics of reading V: the role of contrast in normal vision" reports that reading rate depends on both contrast and character size (1987; venue not confirmed in this session; https://legge.dl8.umn.edu/sites/legge.psych.umn.edu/files/2020-08/psychophysics_of_reading-v._the_role_of_contrast_in_normal_vision_legge_rubin_luebker_1987.pdf).
- Low contrast is a usability problem, not only a compliance one: it causes eye strain and hides state and navigation cues. Source: Nielsen Norman Group, "Low Contrast" (https://www.nngroup.com/articles/low-contrast/). This is an expert critique, not a controlled study.
- Light-on-dark text may need more contrast to be equally legible. Scharff and Ahumada, reported via NASA NTRS, found light-on-dark text slower and less accurate at a given contrast (https://ntrs.nasa.gov/citations/20060020677). This supports checking dark themes separately.

## Scoring method

1. Take a full-resolution screenshot or open the live screen in each theme you are scoring.
2. List every text element, icon that carries meaning, and control boundary. Skip logotypes and disabled controls, and note them as excluded.
3. For each pair, pick the foreground and the immediately surrounding background. Sample hex values with a color picker or from computed styles, not by eye.
4. Compute the ratio with a WCAG contrast calculator, or with the formula above. Record the foreground, background, ratio, and whether the element is large text (18.66px bold or 24px regular and above).
5. Classify each pair: pass for text at or above 4.5:1 (3:1 if large), pass for non-text at or above 3:1, fail otherwise.
6. Record the worst five pairs with their ratios and location. Score using the rubric on the worst pairs, weighted by how much the element matters to the task.
7. Repeat steps 3 to 6 in dark and high-contrast themes, if present. Report the lower score.

## Scoring rubric

- **0**: Primary text or task-critical icons fall well below 3:1 (for example, light grey on white at roughly 2:1), with no alternate cue.
- **1**: Body text or key controls fail 3:1; several are unreadable in bright light.
- **2**: Body text is below 4.5:1, or control boundaries and state cues are below 3:1 on the main task path.
- **3**: Body text meets 4.5:1 with a few exceptions on secondary text (helper text, placeholders); control boundaries mostly meet 3:1.
- **4**: All body text and meaningful icons meet thresholds; a small number of decorative or secondary elements fall short; themes are consistent.
- **5**: Every text and meaningful non-text pair meets AA in all themes, with body text commonly at or above 7:1 (the AAA level, SC 1.4.6), and state cues stay visible in every theme.

## Automated checks (optional)

Axe-core's color-contrast rule and WCAG contrast calculators compute ratios for rendered text on a solid background. They detect text failures reliably in the DOM. They cannot detect contrast for icons drawn as images or SVG without a text role, text over gradients or images, control boundaries that depend on adjacent colors, or state cues that only appear on interaction. Use them as a first pass, then complete steps 2 to 4 by hand.

## Common failure patterns

- Placeholder, helper, and metadata text set in light grey, often below 3:1, while body text passes.
- Dark-mode palettes that invert the hue but not the luminance, leaving text and borders too close in value (Scharff and Ahumada; WCAG 2.x dark-theme behavior).
- Borderless inputs and buttons whose only boundary is a tint near the page background, failing the 3:1 non-text rule (SC 1.4.11).
- Disabled-looking text that is actually active, so users cannot tell what they can do.
- Text placed over photos or gradients where the ratio changes across the element and is only checked at one point.

## Sources

1. W3C WAI. "Understanding SC 1.4.3: Contrast (Minimum)." WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
2. W3C WAI. "Understanding SC 1.4.11: Non-text Contrast." WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast
3. W3C WAI. "Understanding relative luminance." WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/relative-luminance.html
4. Legge, G. E., Rubin, G. S., and Luebker, A. (1987). "Psychophysics of reading V: The role of contrast in normal vision." Venue not confirmed. https://legge.dl8.umn.edu/sites/legge.psych.umn.edu/files/2020-08/psychophysics_of_reading-v._the_role_of_contrast_in_normal_vision_legge_rubin_luebker_1987.pdf
5. Scharff, L. and Ahumada, A. Light-on-dark text legibility findings, reported via NASA NTRS. https://ntrs.nasa.gov/citations/20060020677
6. Nielsen Norman Group. "Low Contrast." https://www.nngroup.com/articles/low-contrast/

## Open questions

- The WCAG 2.2 normative text was not re-read in full; the 2.2 understanding pages were checked only through search summaries. Confirm the thresholds against https://www.w3.org/TR/WCAG22/ before publishing.
- The 7:1 AAA threshold (SC 1.4.6) and the large-text definition (18.66px bold or 24px) are stated from the WCAG definitions, not verified against a fetched page in this session.
- The Legge 1987 venue and the Scharff and Ahumada study details were taken from search summaries, not full papers.
- The W3C wiki flags that the WCAG 2.x relative-luminance formula is contested against the IEC sRGB standard. The rubric uses the WCAG 2.x ratio because it is the normative test; treat any disagreement as a known limitation.
- APCA (a candidate for WCAG 3) is polarity-sensitive and better matches dark-mode perception, but it is not yet normative and its supporting evidence is largely the author's own advocacy. The rubric does not use it.
- The 0 to 5 anchors (for example, "body text commonly at or above 7:1" for a 5) are a judgment call rather than a research-derived cut-off.
