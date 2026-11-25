# White Space

> Measures whether there is enough negative space around and between elements to let content breathe.

## What it measures

- Margin between the content block and the viewport edges, and between the content block and any fixed UI (headers, sidebars, footers).
- Gap between distinct groups of elements (sections, cards, form blocks) compared with the gap between items inside a group.
- Line height and paragraph spacing in running text.
- Padding inside containers, buttons, cards and inputs, so text does not touch borders.
- Whether spacing holds up when text is enlarged or spacing is increased, without overlap or clipping.

## Research basis

- Margins and spacing around on-screen text improve reading speed and comprehension. Chaparro and colleagues compared four white-space layouts for online reading; margins affected both reading speed and comprehension compared with no margin, while leading (line spacing) did not change reading performance but did change user preference. Source: Chaparro et al., 2004, *Usability News* (Wichita State University). https://portfolio.erau.edu/en/publications/reading-online-text-a-comparison-of-four-white-space-layouts/
- Clutter can be measured and correlates with visual search time. Rosenholtz, Li and Nakano (2007) tested Feature Congestion, Subband Entropy and Edge Density as clutter measures against search performance, finding good correlation in complex imagery and maps. Source: Rosenholtz, Li & Nakano, "Measuring visual clutter," *Journal of Vision* 7(2):17, 2007. https://pubmed.ncbi.nlm.nih.gov/18217832 (lab publication page: https://persci.mit.edu/research/uiinfovis/)
- Users must be able to increase text spacing without losing content. WCAG 2.2 SC 1.4.12 (Level AA) requires that content and functionality survive user overrides of line height 1.5x, paragraph spacing 2x, letter spacing 0.12x and word spacing 0.16x. Source: W3C, *Understanding SC 1.4.12: Text Spacing*. https://www.w3.org/WAI/WCAG22/Understanding/text-spacing
- Paragraph spacing should be clearly larger than line spacing. WCAG 2.2 SC 1.4.8 (Level AAA) sets line spacing within paragraphs at no less than space-and-a-half and paragraph spacing at least 1.5 times the line spacing. Source: W3C, *Understanding SC 1.4.8: Visual Presentation*. https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation
- Technique G188 gives a worked CSS example of `line-height: 1.5` with `margin-bottom: 2em` for paragraphs. Source: W3C, *Technique G188*. https://www.w3.org/WAI/WCAG21/Techniques/general/G188

## Scoring method

1. Open the screen at 1440 px wide and at 375 px wide. Record both.
2. Identify content groups: each section, card, form block or list. Note the outer margin from each group to the viewport edge and to fixed UI.
3. Measure the outer margin in px using the browser inspector (computed box model). Record the smallest value.
4. Measure the gap between two neighbouring groups and the gap between two items inside one group. Compute the proximity ratio = between-group gap / within-group gap. Record the lowest ratio on the screen.
5. For running text, read `line-height` and the paragraph margin in computed styles. Compute line-height as a multiple of font size, and paragraph spacing as a multiple of line spacing.
6. Check padding inside buttons, cards and inputs: note any text within 4 px of a border.
7. Apply a user stylesheet (or a bookmarklet) with line-height 1.5, paragraph spacing 2em, letter spacing 0.12em and word spacing 0.16em, using `!important`. Reload and look for overlap, clipping or hidden text. Record the number of affected components.
8. Score each dimension (outer margin, proximity ratio, text spacing, padding, override survival). Take the lowest dimension score as the metric score, then note the others in the observation.
9. Record: screen name, viewport, measured values, affected components, and the score with one sentence of justification.

## Scoring rubric

0 = severe failure. 1 = poor. 2 = weak. 3 = adequate. 4 = good. 5 = exemplary.

- **5:** Outer margin at least 24 px on desktop and 16 px on mobile. Proximity ratio at least 2.0. Line-height at least 1.5 and paragraph spacing at least 1.5 times line spacing. Padding at least 8 px inside containers. Text-spacing override causes no overlap or clipping.
- **4:** Outer margin at least 16 px. Proximity ratio 1.5 to 2.0. Line-height 1.4 to 1.5. One minor tight spot. Overrides cause no lost content, with at most one cosmetic issue.
- **3:** Outer margin 8 to 15 px. Proximity ratio 1.2 to 1.5, so groups are hard to tell apart. Line-height 1.3 to 1.4. Overrides cause clipping in one or two components.
- **2:** Outer margin under 8 px in places. Proximity ratio near 1.0, so groups blur into each other. Line-height about 1.2. Overrides cause overlap in several components.
- **1:** Content touches edges or fixed UI. Text blocks with no paragraph separation. Overrides break the layout across much of the screen.
- **0:** Content is clipped or overlapping at default settings. Text cannot be read without zooming or horizontal scroll.

## Automated checks (optional)

Partial. Computed-style scripts can measure margins, line-height and gaps between elements, and the text-spacing override can be applied with a user stylesheet and checked for overflow with a DOM script. These cannot decide whether a gap reads as deliberate or whether the groups are visually meaningful. Clutter measures (Feature Congestion, Subband Entropy) are research prototypes that score a whole image for clutter; they do not measure white space per group and are not validated as UI scores. Use these as evidence for steps 3 to 7, not as the score.

## Common failure patterns

- Groups separated by the same gap as items inside them, so the layout reads as one undifferentiated block. Visual search is slower in cluttered displays (Rosenholtz et al., 2007).
- Tight line-height (around 1.2) on body text, which makes long text harder to scan and read (WCAG 1.4.8 and 1.4.12 thresholds).
- Fixed-height containers that clip or overlap text when text spacing is increased (WCAG 1.4.12).
- Cards and buttons with text touching their borders, which looks crowded even when the page margin is adequate.
- Generous white space in the page margin but no space between related controls, such as form labels and inputs.
- Margins that collapse to near zero on mobile widths.

## Sources

1. Chaparro, B. et al. (2004). "Reading online text: a comparison of four white space layouts." *Usability News*. https://portfolio.erau.edu/en/publications/reading-online-text-a-comparison-of-four-white-space-layouts/
2. Rosenholtz, R., Li, Y. & Nakano, L. (2007). "Measuring visual clutter." *Journal of Vision* 7(2):17. https://pubmed.ncbi.nlm.nih.gov/18217832
3. W3C WAI. *Understanding SC 1.4.12: Text Spacing (Level AA)*. WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/text-spacing
4. W3C WAI. *Understanding SC 1.4.8: Visual Presentation (Level AAA)*. WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation
5. W3C WAI. *Technique G188*. https://www.w3.org/WAI/WCAG21/Techniques/general/G188

## Open questions

- The Chaparro (2004) result was confirmed from search-result summaries, not the full paper. The exact sample size and effect sizes are unverified.
- Rosenholtz et al. (2005), "Feature Congestion," SIGCHI, is cited in the 2007 work but I did not retrieve its full text or URL.
- A commonly quoted "about 20% comprehension gain" from white space, and a 2005 Nielsen Norman Group eye-tracking claim about white space, could not be traced to a primary source. They are not used in the rubric.
- The proximity ratio thresholds (2.0, 1.5, 1.2) are a judgment call derived from Gestalt proximity reasoning, not from a measured study. No source here gives a numeric ratio.
- The outer margin pixel thresholds (24 px, 16 px, 8 px) are judgment calls, not research thresholds.
- WCAG 1.4.8 is a Level AAA criterion. Its paragraph-spacing rule is stated relative to line spacing, while the 2em value appears only in an example technique. The rubric uses the 1.5x and 2em values as a practical target, and the ambiguity about "1.5 times line spacing" for fonts with different default line heights is unresolved.
- Sources do not give one ideal amount of white space; the rubric scores relative balance and survival under overrides, not a fixed percentage of empty area.
