# Text Readability

> Measures line length, line height, and paragraph sizing that make running text easy to read.

## What it measures

- Characters per line (cpl) in body-text blocks, including the width of the text container.
- Line height (leading) relative to font size for multi-line body text.
- Paragraph spacing: the gap between consecutive paragraphs compared with the line height.
- Whether running text uses sizes and spacing that stay readable at the screen's typical viewing distance and width.

## Research basis

- Body text should run about 50 to 75 characters per line. Baymard Institute reports this range and notes that users fatigue when navigating very long lines (100+ characters). Source: Baymard Institute, "Line Length Readability," https://baymard.com/research-articles/line-length-readability
- On-screen reading speed rises with line length, but readers prefer shorter lines. Dyson and Kipping (1998) found 100-character lines were read faster than 25-character lines with no loss of comprehension, while reader preference did not track performance. Source: Dyson and Kipping, "The Effects of Line Length and Method of Movement on Patterns of Reading from Screen," Visible Language, 1998, https://journals.uc.edu/index.php/vl/article/view/5671. The year is 1998 per the journal page; one bibliography gives 1996.
- Increased line spacing changes reading behaviour in measurable ways: readers made shorter fixations, skipped more words, and made less accurate return sweeps. Chiu and Drieghe (2023), Attention, Perception, & Psychophysics 85(8), DOI 10.3758/s13414-023-02787-1, https://link.springer.com/article/10.3758/s13414-023-02787-1. The effects were described as modest.
- WCAG 2.x Success Criterion 1.4.8 (Visual Presentation, Level AAA) sets the reference thresholds: lines no wider than 80 characters (40 for CJK), line spacing of at least 1.5 within paragraphs, paragraph spacing of at least 1.5 times the line spacing, and no full justification. Source: W3C, "Understanding SC 1.4.8: Visual Presentation," https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation

## Scoring method

1. Open the screen at a desktop width of about 1280 px and at a phone width of about 375 px.
2. Locate the longest running-text block (article body, description, or help text). Ignore labels, captions, and navigation.
3. Measure line length: in DevTools, read the computed width of the text container and the font size, or count the characters on three full lines and average them. Record the cpl range.
4. Measure line height: read the computed `line-height` of the body text. Divide by the computed font size to get a ratio. Record it.
5. Measure paragraph spacing: read the computed margin or gap between two consecutive paragraphs. Divide it by the line height. Record it.
6. Check at both widths whether the measured values still hold. Note any horizontal scrolling or text that wraps into a sliver.
7. Record each observation as: block, cpl range, line-height ratio, paragraph-gap ratio, width tested. Score using the rubric.

## Scoring rubric

- **0**: Running text runs beyond 120 cpl or is under 30 cpl at desktop width, line height is below 1.2, and paragraphs have no visible separation.
- **1**: Line length often exceeds 100 cpl or is under 35 cpl; line height is about 1.2 to 1.3; paragraph gaps are hard to see.
- **2**: Line length is frequently outside 45 to 85 cpl; line height is about 1.3 to 1.4; paragraph gaps are present but smaller than the line height.
- **3**: Line length is mostly within 50 to 80 cpl; line height is about 1.4; paragraph gaps are visible but not consistently 1.5 times the line height.
- **4**: Line length is 50 to 75 cpl at desktop and no more than 80 cpl at phone width; line height is at least 1.5; paragraph gaps are at least 1.5 times the line height.
- **5**: All of level 4, plus the text remains within those ranges at every breakpoint tested, reflows without horizontal scrolling, and the user can change text size or spacing without breaking the layout.

## Automated checks (optional)

A reliable automated check exists for part of this metric. A computed-style script can read `line-height`, font size, paragraph margins, and container width from the DOM. A script can also estimate cpl by dividing the container width by the average glyph width of the font. This is an approximation, because it does not account for word wrap or proportional glyph variation. It cannot judge whether a block is running text rather than labels. Manual sampling of real lines remains the reference.

## Common failure patterns

- Full-width body text on wide desktop screens, producing 110 to 150 cpl that is hard to track from line to line (Baymard Institute).
- Tight leading (around 1.2) inherited from display or heading styles and applied to body copy.
- Paragraph gaps smaller than the line height, so paragraphs blur together (WCAG 1.4.8 paragraph-spacing rule).
- Line length capped in pixels rather than characters, so the measure varies widely with the font size.
- Fully justified text that creates uneven word spacing, which WCAG 1.4.8 prohibits.

## Sources

1. Baymard Institute. "Line Length Readability." https://baymard.com/research-articles/line-length-readability
2. Dyson, M. C., and Kipping, G. J. (1998). "The Effects of Line Length and Method of Movement on Patterns of Reading from Screen." Visible Language. https://journals.uc.edu/index.php/vl/article/view/5671
3. Chiu, T.-Y., and Drieghe, D. (2023). "The role of visual crowding in eye movements during reading: effects of text spacing." Attention, Perception, & Psychophysics, 85(8). DOI 10.3758/s13414-023-02787-1. https://link.springer.com/article/10.3758/s13414-023-02787-1
4. W3C. "Understanding SC 1.4.8: Visual Presentation (Level AAA)," WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation
5. W3C WCAG GitHub issue #2256 on translating "space-and-a-half" into CSS. https://github.com/w3c/wcag/issues/2256

## Open questions

- The 50 to 75 cpl range rests on a practitioner summary (Baymard) and older print guidance. The on-screen studies are small and use older displays. The range is well supported but not settled.
- Dyson and Kipping's comprehension result is reported as no difference. Other reviews describe the wider literature as mixed. Treat the comprehension effect as uncertain.
- The Chiu and Drieghe effects are modest; the 1.5 line-height anchor is taken from WCAG, not from a reading-performance study.
- No source was verified for a minimum body font size. The rubric does not score font size; this is a gap to decide on separately.
- WCAG 1.4.8 is Level AAA and is used here as a reference threshold, not a pass/fail requirement. The CSS interpretation of "space-and-a-half" is under discussion (issue #2256).
- The paragraph-gap anchor (1.5 times line height) and the 0 to 3 breakpoints are judgment calls, not research-backed values.
