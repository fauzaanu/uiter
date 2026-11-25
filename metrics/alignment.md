# Alignment

> Alignment measures how consistently element edges and centers line up along shared axes.

## What it measures

- Left, right, top, and bottom edges of sibling elements (cards, form fields, list items, buttons) share an axis where the layout implies one.
- Centers of elements that sit in the same row or column, and of text blocks placed under centered headings, line up on a common vertical or horizontal axis.
- Text baselines and the left edge of body text, headings, icons, and labels agree within a column.
- Elements placed in the same grid column or track snap to that track's start, end, or center, rather than floating between tracks.
- Misalignments are either systematic (a consistent offset) or isolated (one element off-axis among many aligned ones).

## Research basis

- Alignment in interface layout is a structural property that users respond to. Tüchler, Zarina and Skilters (2021) reported that vertical and horizontal alignment properties, including symmetry and complexity, shaped ratings of expressive and creative aesthetics and perceived usability in a quasi-experiment with 65 participants. Source: Tüchler, Zarina, Skilters, "The impact of interface alignment structure on aesthetic appreciation and usability rating," CogSci 2021. https://escholarship.org/uc/item/34b1n9zv
- Interface aesthetics, including balance and the position of rectangular regions, correlate with perceived usability. Ngo, Teo and Byrne (2003) reported high correlations between perceived aesthetics and usability in screen interfaces. Source: Ngo, Teo, Byrne, "Modelling interface aesthetics," Information Sciences, 2003. Related: Ngo, Teo, Byrne, "Evaluating Interface Esthetics," Knowledge and Information Systems 4, 2002, DOI 10.1007/s10115-002-8193-6. https://www.doi.org/10.1007/S10115-002-8193-6
- Users find alignment tools in design software hard to use. A study of 12 regular users reported problems with persistence, unpredictable results, and difficulty adjusting layouts, which supports checking alignment on the rendered output rather than assuming the design tool did it. Source: StickyLines study, University of Paris-Saclay / LRI. https://www.lri.fr/~mbl/Teach/SituatedComputing/2017/papers/Alignment/StickyLines.pdf
- Layout tools that visualize inferred alignment relationships were significantly faster than snap-dragging for 2D and 3D layout tasks. This indicates that alignment is a relationship users must perceive, not only a property of coordinates. Source: Fu group, "Layout beautification," IEEE TVCG. https://hongbofu.people.ust.hk/doc/Layout_tvcg.pdf
- Out-of-line elements attract attention in a layout where most items share an axis, which is why a single misaligned element reads as an error. Secondary summaries of NN/g eyetracking work state this; the original NN/g article was not verified (see Open questions).

## Scoring method

1. Open the screen at a desktop width (1280 px or wider) and at one phone width (375 px). Score each width and record the lower one.
2. List the containers that hold repeated or paired elements (card grids, form columns, nav items, list rows, icon-plus-label pairs).
3. For each container, note the axis it should share: left edge, right edge, top edge, center x, center y, or baseline.
4. Measure the edge or center positions. In a browser, use `getBoundingClientRect()` on the elements, or a DOM overlay, and record the largest deviation from the shared axis in CSS pixels. Manually, use a screenshot with a grid overlay at 1 px precision.
5. Mark each deviation as intentional (the design explains it, such as an icon offset for optical balance) or unintentional.
6. Count how many aligned relationships you checked and how many are unintentionally off-axis. Compute the proportion off-axis.
7. Record: screen, width, container, axis, deviation in px, intentional or not. Then score with the rubric.

## Scoring rubric

Scale: 0 = severe failure, 5 = exemplary. Scores are based on the proportion of checked relationships that are unintentionally off-axis, and on whether any off-axis element is conspicuous.

- **5 (exemplary):** All checked relationships share their axis within 1 px. Every deviation is intentional and explained by the design.
- **4 (strong):** Up to 5% of relationships are off-axis by 1 to 2 px, and none is visually obvious at normal viewing distance.
- **3 (adequate):** 5 to 15% of relationships are off-axis by up to 4 px, or one container is visibly misaligned while the rest of the screen is consistent.
- **2 (weak):** 15 to 30% of relationships are off-axis, or a misalignment is visible at a glance and breaks a repeated pattern.
- **1 (poor):** Over 30% of relationships are off-axis, or the page has no shared axes at all.
- **0 (severe failure):** Elements overlap or are clipped by misalignment, or the axis breaks at a breakpoint so content looks arbitrarily placed.

Open question: the 1 px and 2 px tolerances are engineering conventions, not thresholds found in the research. The percentage bands are judgment calls.

## Automated checks (optional)

A browser script can measure edges and centers from the DOM. It uses `getBoundingClientRect()` on tagged containers and reports the spread of `left`, `right`, `centerX`, and `centerY` values per group. This detects measurable offsets reliably. It cannot tell whether an offset is intentional, cannot judge optical alignment (for example, round icons or italic type), and cannot identify which elements belong on a shared axis without a reviewer's input.

## Common failure patterns

- **Off-by-a-few-pixels drift:** Padding, borders, or icons shift one element a few pixels from its neighbors. The eye reads the screen as careless once a repeated pattern breaks.
- **Breakpoint drift:** Elements align on desktop and fall off-axis on phone widths when a container changes padding or width.
- **Mixed alignment within one group:** Some cards align to the top and others to the center, with no visible reason.
- **Centered text over left-aligned blocks:** Headings are centered while the body is left-aligned, so the two axes compete.
- **Floating elements outside the grid:** Elements are placed by margin instead of by grid track, so they land between columns.
- **Misaligned baselines in label rows:** Icon, label, and value sit on different baselines, which reads as a layout error even when the box edges agree.

## Sources

1. Tüchler, A. F., Zarina, L., and Skilters, J. (2021). The impact of interface alignment structure on aesthetic appreciation and usability rating. Proceedings of the 43rd Annual Meeting of the Cognitive Science Society. https://escholarship.org/uc/item/34b1n9zv
2. Ngo, D. C. L., Teo, L. S., and Byrne, J. G. (2003). Modelling interface aesthetics. Information Sciences. (Venue and claim as reported in a search summary; full text not checked.)
3. Ngo, D. C. L., Teo, L. S., and Byrne, J. G. (2002). Evaluating Interface Esthetics. Knowledge and Information Systems, 4, 46-79. DOI 10.1007/s10115-002-8193-6. https://www.doi.org/10.1007/S10115-002-8193-6
4. StickyLines: alignment tool study. LRI, Université Paris-Saclay. https://www.lri.fr/~mbl/Teach/SituatedComputing/2017/papers/Alignment/StickyLines.pdf
5. Fu et al., layout beautification with alignment visualization. IEEE Transactions on Visualization and Computer Graphics. https://hongbofu.people.ust.hk/doc/Layout_tvcg.pdf

## Open questions

- Full text of Tüchler et al. (2021) was not read; only the abstract and proceedings metadata were verified. Effect sizes and rating scales are unconfirmed.
- The Ngo et al. (2003) claim comes from a search summary; the paper itself was not opened.
- The Fu et al. TVCG paper's year and full author list were not confirmed from the source.
- The StickyLines study is a tool-usability study, not a measure of how users perceive misalignment. It supports the framing but not a numeric threshold.
- No study found gives a pixel tolerance for perceived misalignment. The rubric's px bands and percentage bands are judgment calls.
- NN/g's eyetracking claim about out-of-line elements was seen only in secondary summaries (UX Planet, IxDF, Toptal). The original NN/g article was not located or verified.
- A search for a study by "Ngo, Samad, Whitenton" did not return a match; the closest author set is Ngo, Teo and Byrne.
