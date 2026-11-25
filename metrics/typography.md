# Typography

> Judges whether the typefaces, weights, and type scale on a screen are chosen deliberately and applied consistently, and whether text is sized and spaced for comfortable reading.

## What it measures
- Number of typefaces in use (ideally one family, or a deliberate pairing of two) and whether each role (headings, body, labels, code, captions) maps to a consistent face.
- Weight usage: a small, named set of weights (for example regular, medium, bold) applied to the same roles across the screen.
- Size steps: body text size, and whether heading and label sizes follow a recognisable scale rather than arbitrary values.
- Body text size and vertical rhythm: line height and paragraph spacing relative to font size.
- Measure of body text per line (characters per line) in running-text regions.

## Research basis
- Body text at 18 pt or larger gave the best objective readability and comprehension in the tested range; 10 and 12 pt hurt comprehension. Rello, Pielot and Marcos (CHI 2016) reported readability gains continuing up to 18 pt. Source: Rello et al., 2016, CHI, doi 10.1145/2858036.2858204. Note: figures taken from presenter slides and secondary summaries; the full paper was not retrieved.
- Line spacing of about 1.0 to 1.4 was recommended, and the two extreme settings tested (0.8 and 1.8) impaired readability. Source: Rello et al., 2016 (as above).
- Optimal font choice is individual. Across 352 participants and 16 typefaces, the fastest font per reader was on average 14% faster than that reader's preferred font, and preference did not reliably predict reading speed. Source: Wallace, Bylinskii, Dobres, Kerr, Berlow, Treitman, Kumawat, Arpin, Miller, Huang and Sawyer, 2022, ACM TOCHI 29(4), https://jeffhuang.com/papers/Readability_TOCHI22.pdf. This supports rubric judgments on font choice as a convention, not a measured winner.
- Line height of at least 1.5x font size, paragraph spacing of at least 2x, and letter spacing of at least 0.12x must be supported without loss of content (WCAG 2.2 SC 1.4.12, Level AA). Source: W3C, Understanding SC 1.4.12 Text Spacing, https://www.w3.org/WAI/WCAG22/Understanding/text-spacing
- Body text line length of 50 to 75 characters is the commonly cited optimum. Source: Baymard Institute, Line Length Readability, https://baymard.com/research-articles/line-length-readability. Treat as practitioner research; the experimental literature is mixed (see Open questions).

## Scoring method
1. Take a full-resolution screenshot at a desktop width and a phone width. Note the page's main content region.
2. Inventory typefaces. Use the browser inspector or a computed-style script to list `font-family` for every text element. Count distinct families. Record the count and which roles use each.
3. Inventory weights. List distinct `font-weight` values in use. Record the count.
4. Inventory sizes. List distinct computed `font-size` values for body, headings, labels and captions. Check whether they form a consistent set of steps. Record the count of distinct sizes.
5. Measure body text. Read computed body `font-size`, `line-height` (divide by font size), and paragraph margin (divide by font size). Record the ratios.
6. Measure line length. For the main running-text block, count characters per line at the desktop width (a sample of three lines is enough). Record the average.
7. Check role consistency. Sample five same-role elements (for example, all section headings) and confirm they share family, weight and size.
8. Check that text remains readable at the WCAG 1.4.12 settings (see Automated checks). Record any clipping or overlap.
9. Assign the score using the rubric. Write the observation as: families, weights, size steps, body size, line-height ratio, paragraph ratio, characters per line, and the 1.4.12 result.

## Scoring rubric
0 = severe failure. 5 = exemplary. Applies to all typography scores.

- **0**: More than four typefaces, or body text below 12 px or unreadable, or text overlaps or clips when spacing is increased, or no discernible type hierarchy.
- **1**: Three or four typefaces with no clear role mapping. Six or more weights or many ad hoc sizes. Body text 12 to 13 px. Line height below 1.2 or line length above 100 characters in running text.
- **2**: Two or three typefaces, with some roles inconsistent (for example, the same heading role at two sizes). Body text 14 to 15 px. Line height 1.2 to 1.4. Line length 90 to 100 characters.
- **3**: One or two families and three to four weights. A roughly consistent size scale with some irregular steps. Body text 16 px. Line height 1.4 to 1.5. Line length 75 to 90 characters.
- **4**: One family (or a deliberate two-family pair) with a named, limited weight set. Clear size scale with consistent role mapping. Body text 16 to 18 px. Line height at least 1.5. Paragraph spacing at least 1x. Line length 50 to 75 characters. Passes WCAG 1.4.12 without clipping.
- **5**: Everything in level 4, plus a documented or evident modular scale, body text at 16 to 18 px or larger, paragraph spacing at least 2x, and a passing 1.4.12 result on all tested settings at both widths. Hierarchy holds without colour.

## Automated checks (optional)
- Computed-style script (browser devtools or Playwright): reads `font-family`, `font-weight`, `font-size`, `line-height` for each text node. It can count families, weights and sizes and compute ratios. It cannot judge whether a face is appropriate or whether roles are intentional.
- WCAG 1.4.12 check: apply a user stylesheet with line height 1.5, paragraph spacing 2, letter spacing 0.12 and word spacing 0.16 (the word spacing value is from secondary sources), then check for overflow and clipping with a DOM overlap test. It detects clipping and overlap, not aesthetic quality.
- None reliable for scale coherence or font appropriateness; manual review.

## Common failure patterns
- Too many typefaces and weights accumulated across components, with no role mapping (no research source; practitioner observation).
- Small body text on dense screens, reducing comprehension (Rello et al., 2016).
- Fixed-height containers that clip text when line spacing or letter spacing is increased (WCAG 1.4.12 Understanding, which names overlap as a failure).
- Long running-text lines beyond the 50 to 75 character range (Baymard Institute).
- Arbitrary sizes that do not form a scale, so hierarchy depends on colour or position alone.

## Sources
1. Rello, L., Pielot, M., & Marcos, M.-C. (2016). Make It Big! The Effect of Font Size and Line Spacing on Online Readability. CHI 2016. doi 10.1145/2858036.2858204.
2. Wallace, S., Bylinskii, Z., Dobres, J., Kerr, B., Berlow, S., Treitman, R., Kumawat, N., Arpin, K., Miller, D. B., Huang, J., & Sawyer, B. D. (2022). Towards Individuated Reading Experiences: Different Fonts Increase Reading Speed for Different Individuals. ACM TOCHI, 29(4). https://jeffhuang.com/papers/Readability_TOCHI22.pdf
3. W3C. Understanding SC 1.4.12: Text Spacing (WCAG 2.2). https://www.w3.org/WAI/WCAG22/Understanding/text-spacing
4. Baymard Institute. Line Length Readability. https://baymard.com/research-articles/line-length-readability

## Open questions
- The Rello et al. figures come from presenter slides and secondary summaries; the full paper was not read. Verify the 18 pt and 1.0 to 1.4 line spacing numbers against the paper.
- Line-length evidence conflicts. Dyson and Haselgrove (2001), as cited secondhand, suggested about 55 characters; a 2000s-era study found 80 characters not slower than 40 in one condition. The 50 to 75 band is practitioner consensus, not a settled experimental result. Rubric anchors for line length are a judgment call.
- The word spacing value of 0.16x is from secondary sources (BrowserStack) and was not verified against the W3C text.
- Nielsen Norman Group was searched for a line-length study and none was found; no NN/g claim is used here.
- Limit of 3 typefaces, and the weight and size thresholds at each rubric level, are judgment calls, not research-backed numbers.
- No research found that directly compares sans-serif and serif faces for screen reading; font appropriateness is scored by convention and consistency, not measured superiority.
