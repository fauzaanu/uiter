# Visual Clarity

> Can a user read everything on the screen and see at a glance what matters, what belongs together, and in what order to read it?

## Covered metrics

- `contrast`: Contrast
- `visual-hierarchy`: Visual Hierarchy
- `text-readability`: Text Readability
- `typography`: Typography
- `white-space`: White Space
- `alignment`: Alignment
- `spacing-consistency`: Spacing Consistency
- `grid-layout`: Grid Layout
- `color-palette`: Color Palette
- `data-density`: Data Density

## What it measures

- Luminance contrast of text, meaningful icons, and control boundaries against their immediate background, including placeholder, helper, and metadata text and text over images.
- Whether one primary element dominates, and whether heading, body, and caption levels step clearly in size and weight, with color and position agreeing.
- Typeface count, weight set, and size scale, and whether each text role uses the same face, weight, and size.
- Running text: characters per line, line height, paragraph spacing, body size.
- Negative space: outer margins, padding inside containers, and between-group gaps that are larger than within-group gaps.
- Gaps that repeat a small scale; equal roles use equal gaps.
- Shared edges, centers, and baselines; blocks and peer items sitting on one column structure with common top lines.
- Color restraint: few hues, each with a role, conventional status colors, and a non-color cue beside every colored signal.
- Amount of information per region fitting the screen's task, without clutter, decoration, or emptiness that splits a comparison.

## Scoring method

Work from the screenshot. Estimate pixel values and ratios from it. Checks that need computed styles, other widths, other themes, or user text-spacing overrides cannot be confirmed from one image: judge the visible evidence and say so in the rationale.

1. Squint or shrink the screenshot. Note the one to three elements that dominate and name the main content or action. If it is not clear within about five seconds, record a miss.
2. List the text levels. Estimate size and weight for each, count typefaces, weights, and sizes, and count elements in the strongest emphasis style (more than about three per viewport weakens the signal).
3. Sample foreground and background colors for body text, secondary text, meaningful icons, and control boundaries. Compute the WCAG ratio, (L1 + 0.05) / (L2 + 0.05). Record the worst five pairs.
4. Find the longest running-text block. Count characters on three lines, and estimate line height and paragraph gap relative to font size.
5. Measure the outer margin, container padding, and the lowest between-group to within-group gap ratio. List the distinct gap values and check that same-role gaps match.
6. Overlay a column grid. Mark sibling edges, centers, baselines, and block edges that miss a shared axis or column, and whether each miss looks intentional.
7. Count non-neutral hues and give each a role. Flag decorative hues, colored signals with no non-color cue, unconventional status colors, and the share of area in saturated color.
8. State the screen's primary task. Per region, count data-bearing items and decorative items, and note comparisons split across regions.
9. Place each member on the rubric, combine them into one score, letting the failures most visible to a user pull the score down the most, and write todos for the lowest members first.

## Scoring rubric

Thresholds come from the member files (WCAG 1.4.3, 1.4.6, 1.4.8, 1.4.11, 1.4.12; Baymard; member judgment anchors).

- **0**: Primary text or task-critical icons sit well below 3:1 (about 2:1). All text is one size and weight, or the most prominent element is low priority. Content clips or overlaps at default settings. Body text under 12 px, or more than four typefaces. Blocks start at arbitrary positions. Color is the only carrier of critical information.
- **25**: Body text or key controls fail 3:1. Several elements compete for top emphasis. Content touches edges; groups blur together (proximity ratio near 1.0). Line height about 1.2; lines over 100 or under 35 characters. Over 30% of checked alignments are off-axis. Three or four typefaces with no role mapping. Many hues without roles, with saturated color over 30% of the area.
- **50**: Body text meets 4.5:1, but secondary text or control boundaries fall short (boundaries under 3:1). A primary element exists, but the step to the next level is under about 1.25x. Outer margin 8 to 15 px; proximity ratio 1.2 to 1.5; line height 1.3 to 1.4; lines 75 to 90 characters; body 14 to 16 px. 5 to 15% of alignments off by up to 4 px. Two or three hues compete, saturated color at 10 to 30%. A few regions are over- or under-filled.
- **75**: All body text and meaningful icons meet 4.5:1 (3:1 for large text, 18.66 px bold or 24 px regular) and non-text meets 3:1. The primary element is named within about five seconds, levels step by about 1.25x or more, and emphasis is sparing. Outer margin at least 16 px; proximity ratio 1.5 to 2.0; line height about 1.5; 50 to 75 characters per line (no more than 80); body 16 to 18 px. At most 5% of alignments off by 1 to 2 px. One family or a deliberate pair. At most one decorative hue. Density fits the task.
- **100**: Every pair meets AA, with body text commonly at or above 7:1. Hierarchy reads at a glance. Outer margin at least 24 px on desktop and 16 px on mobile; proximity ratio at least 2.0; padding at least 8 px; paragraph spacing at least 1.5 times line spacing. All alignments within 1 px. A single limited scale governs type and spacing; one grid governs every section. Saturated color covers about 10% or less and every colored signal has a non-color cue. Every region carries useful data, and text survives WCAG 1.4.12 overrides (line height 1.5, paragraph spacing 2x, letter spacing 0.12x, word spacing 0.16x).

## Member sub-criteria

- `contrast`: Detail: metrics/contrast.md
- `visual-hierarchy`: Detail: metrics/visual-hierarchy.md
- `text-readability`: Detail: metrics/text-readability.md
- `typography`: Detail: metrics/typography.md
- `white-space`: Detail: metrics/white-space.md
- `alignment`: Detail: metrics/alignment.md
- `spacing-consistency`: Detail: metrics/spacing-consistency.md
- `grid-layout`: Detail: metrics/grid-layout.md
- `color-palette`: Detail: metrics/color-palette.md
- `data-density`: Detail: metrics/data-density.md

## Common failure patterns

- Placeholder, helper, and metadata text in light grey, often below 3:1; text over photos or gradients.
- Borderless inputs and buttons whose only boundary is a tint near the page background.
- Near-identical sizes across levels (16 px and 18 px headings), or bold on many items.
- A large image or a low-placed colored element outcompeting the real task element.
- Full-width body text at 110 to 150 characters per line; tight leading (about 1.2); paragraph gaps smaller than the line height.
- Too many typefaces, weights, and arbitrary sizes with no role mapping.
- Groups separated by the same gap as the items inside them; text touching borders.
- One-off gap values (13 px, 7 px, 22 px); off-by-a-few-pixels drift; mixed column counts between sections.
- Accent color with no action or state meaning; one hue for two meanings; status shown by color alone.
- One-number tiles that leave the screen empty, or tables packed with equal-weight labels, borders, and icons.

## Sources

- W3C, Understanding SC 1.4.3 Contrast (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- W3C, Understanding SC 1.4.11 Non-text Contrast. https://www.w3.org/WAI/WCAG21/Understanding/non-text-contrast
- W3C, Understanding relative luminance. https://www.w3.org/WAI/WCAG22/Understanding/relative-luminance.html
- Legge, Rubin, and Luebker (1987), Psychophysics of reading V. https://legge.dl8.umn.edu/sites/legge.psych.umn.edu/files/2020-08/psychophysics_of_reading-v._the_role_of_contrast_in_normal_vision_legge_rubin_luebker_1987.pdf
- Scharff and Ahumada, light-on-dark legibility, NASA NTRS. https://ntrs.nasa.gov/citations/20060020677
- Nielsen Norman Group, Low Contrast. https://www.nngroup.com/articles/low-contrast/
- Faraday (2000), Visually critiquing web pages (secondary summary). https://tigerweb.towson.edu/rchelch1/ex5/page3.html
- Still (2018), Web page visual hierarchy. https://www.bohrium.com/paper-details/web-page-visual-hierarchy-examining-faraday-s-guidelines-for-entry-points/813051593975922689-7721
- Djamasbi, Siegel, and Tullis (2011), Visual hierarchy and viewing behavior. https://rd.springer.com/chapter/10.1007/978-3-642-21602-2_36
- Buscher, Cutrell, and Morris (2009), CHI. https://www.microsoft.com/en-us/research/publication/what-do-you-see-when-youre-surfing-using-eye-tracking-to-predict-salient-regions-of-web-pages/
- Chaparro et al. (2004), four white space layouts. https://portfolio.erau.edu/en/publications/reading-online-text-a-comparison-of-four-white-space-layouts/
- Rosenholtz, Li, and Nakano (2007), Measuring visual clutter. https://pubmed.ncbi.nlm.nih.gov/18217832
- W3C, Understanding SC 1.4.12 Text Spacing. https://www.w3.org/WAI/WCAG22/Understanding/text-spacing
- W3C, Understanding SC 1.4.8 Visual Presentation. https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation
- W3C, Technique G188. https://www.w3.org/WAI/WCAG21/Techniques/general/G188
- Tüchler, Zarina, and Skilters (2021), CogSci. https://escholarship.org/uc/item/34b1n9zv
- Ngo, Teo, and Byrne (2003), Modelling interface aesthetics, Information Sciences 152, pp. 25-46.
- Ngo, Teo, and Byrne (2002), Evaluating Interface Esthetics. https://www.doi.org/10.1007/S10115-002-8193-6
- StickyLines alignment tool study. https://www.lri.fr/~mbl/Teach/SituatedComputing/2017/papers/Alignment/StickyLines.pdf
- Fu et al., layout beautification, IEEE TVCG. https://hongbofu.people.ust.hk/doc/Layout_tvcg.pdf
- Harley (2020), Gestalt Proximity, NN/g. https://www.nngroup.com/articles/gestalt-proximity/
- CHI 2004 paper on icon spacing (title and authors not verified). https://hci.rwth-aachen.de/materials/conferences/CHI2004/1p695.pdf
- Nielsen Norman Group, Using Grids in Interface Designs. https://nngroup.com/articles/using-grids-in-interface-designs
- GRIDS, arXiv:2001.02921. https://arxiv.org/pdf/2001.02921
- W3C, Understanding SC 1.4.10 Reflow. https://www.w3.org/WAI/WCAG21/Understanding/reflow
- Wireframe visual-quality study, arXiv:2609.03918. https://arxiv.org/pdf/2609.03918
- Rello, Pielot, and Marcos (2016), Make It Big!, CHI. doi 10.1145/2858036.2858204
- Wallace et al. (2022), ACM TOCHI 29(4). https://jeffhuang.com/papers/Readability_TOCHI22.pdf
- Baymard Institute, Line Length Readability. https://baymard.com/research-articles/line-length-readability
- Dyson and Kipping (1998), Visible Language. https://journals.uc.edu/index.php/vl/article/view/5671
- Chiu and Drieghe (2023). https://link.springer.com/article/10.3758/s13414-023-02787-1
- W3C WCAG GitHub issue #2256. https://github.com/w3c/wcag/issues/2256
- W3C, Understanding SC 1.4.1 Use of Color. https://www.w3.org/WAI/WCAG21/Understanding/use-of-color ; https://w3.org/WAI/WCAG22/Understanding/use-of-color.html
- Gramazio, Laidlaw, and Schloss (2017), Colorgorical. https://connorgr.github.io/pdf/gramazio-2016-ccd.pdf
- Affective Color in Visualization, CHI 2017. https://tableau.com/sites/default/files/2023-01/Affective%20Color%20CHI%202017.pdf
- Blender Human Interface Guidelines: Color. https://developer.blender.org/docs/features/interface/human_interface_guidelines/color/
- Microsoft, Visual color (Win32 UX Guide). https://learn.microsoft.com/en-us/Windows/Win32/uxguide/vis-color
- Nielsen Norman Group, Content Dispersion. https://www.nngroup.com/articles/content-dispersion/
- Rosenholtz, Li, Mansfield, and Jin (2005), Feature Congestion. https://unpaywall.org/10.1145%2F1054972.1055078
- Pankok and Kaber (2018), Ergonomics. https://stacks.cdc.gov/view/cdc/210879/cdc_210879_DS1.pdf
- Two-by-two study on social app UI structure and density (venue and authors not confirmed).
- CHI 2020 online study on website visual complexity, 165 participants (venue and URL not confirmed).
- McGurgan et al. (2021), additional reading. https://www.scitepress.org/Papers/2021/102638/102638.pdf

## Open questions

- WCAG thresholds (4.5:1, 3:1, 7:1, the large-text definition, 0.16x word spacing) were taken from Understanding pages and summaries, not the normative text. APCA is not used because it is not normative.
- The 1.25x size step, the emphasis limit, proximity ratios, margin and padding values, alignment tolerances, typeface limits, hue counts, and saturated-area shares are judgment calls, not research thresholds.
- Line-length evidence is mixed; 50 to 75 characters is practitioner consensus. `text-readability` has no verified minimum body size; the pixel anchors come from `typography`.
- Sources disagree on how strongly size drives attention (Faraday against Still), and no study gives a numeric density target.
- Many cited papers were seen only as abstracts or search summaries; the member files list which.
