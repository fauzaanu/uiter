# Data Density

> Scores whether the amount of information shown per area suits the task: dense enough to support comparison and scanning, without clutter or sparseness that forces extra searching.

## What it measures
- Count of distinct data-bearing items (values, labels, rows, chart marks, status indicators) per visible region, such as one card, panel, or screenful.
- Share of the viewport that is empty versus occupied by content, and whether that empty space is deliberate grouping or unused space.
- Whether related items the user must compare sit within one viewport, or are split across scrolls, tabs, or accordions.
- Presence of non-data decoration (ornament, redundant icons, repeated labels, heavy gradients or borders) that competes with the data.
- Whether the task implied by the screen (monitoring, comparing, exploring, reading) is served by the density shown.

## Research basis
- Visual complexity hurts search efficiency and recall. An online CHI 2020 study (165 participants) reported a significant negative effect of website visual complexity on search efficiency and information recall, with participants who preferred simple sites most affected. Source: [6].
- Splitting related content across viewports raises cognitive load and slows findability. NN/g's 13 qualitative usability tests found participants struggled more to find information on a dispersed product page than on a condensed one, and had to scroll repeatedly to compare details. Source: [1].
- Sparse layouts can create an "illusion of completeness," where users stop scrolling before content ends. Source: [1].
- Clutter can be quantified from the image itself. Feature Congestion measures how hard it is to add a new salient item to a display, using color and luminance contrast as initial features. Source: [2].
- Feature Congestion predicts perceived clutter on computer interfaces (paired-comparison ratings, 29 participants, website screenshots), but its link to task performance is weaker than originally reported. Source: [3], [4].
- Structural clarity offsets density. A 2x2 study of social app UIs found structural clarity significantly affected preference while element density had no significant effect. Source: [5].

## Scoring method
1. Pick the primary task the screen supports (for example, monitor status, compare values, read a record). Write it down.
2. Choose one representative viewport at a common desktop width and one at a phone width.
3. For each major region (card, panel, table, chart), count distinct data-bearing items. Record the count per region.
4. Estimate the empty-area ratio: sketch or overlay a grid, and count cells with no content inside the region's bounds. Record the percentage.
5. Identify every set of items the task requires comparing. Note whether each set is fully visible in one viewport. Record any that are split.
6. Count non-data decorative elements (ornament, redundant icons, repeated labels) per region. Record the count.
7. Judge whether density fits the task. Dense enough for the task without clutter scores high; too much for a quick read or too sparse for comparison scores low.
8. Assign the 0 to 5 score from the rubric, citing the counts from steps 3 to 6.

## Scoring rubric
- 0: Severe failure. Regions are either so overloaded that items cannot be told apart, or so sparse that required comparisons are split across screens. Decorative elements dominate the data.
- 1: Major problem. Most regions are cluttered or empty, and the primary task needs repeated scrolling or switching to complete.
- 2: Noticeable problem. Several regions are cluttered or sparse, or required comparisons are often split. The task can be done but with visible friction.
- 3: Acceptable. Density is mostly appropriate. A few regions are over- or under-filled, and decoration is present but does not compete with the data.
- 4: Good. Density fits the task across regions. Related items are grouped in one viewport, and empty space is used for grouping. Decoration is minimal.
- 5: Exemplary. Density is matched to the task at both desktop and phone widths. Every region carries useful data, related items are co-located, and no non-data element competes with the data.

Numeric thresholds: none are established in the sources reviewed. The rubric is qualitative and must be applied by a reviewer.

## Automated checks (optional)
None reliable; manual review only. Feature Congestion-style saliency models estimate perceived clutter from a screenshot, but they do not measure task fit, item counts, or whether related items are split across scroll positions. Use them, if at all, only as a secondary signal.

## Common failure patterns
- Dashboard tiles with one number each, leaving most of the screen empty while the comparison the user needs requires scrolling. Source: [1].
- Splitting specs or related values behind accordions or tabs on desktop, forcing users to remember values across views. Source: [1].
- Tables or cards packed with equal-weight labels, borders, and icons, so no item stands out. Source: [6], [2].
- Density chosen for the designer's sense of completeness rather than the user's task, with no check at phone width. Source: [1].
- Relying on whitespace alone to fix clutter when structure (grouping, hierarchy) is missing. Source: [5].

## Sources
1. Nielsen Norman Group, "Content Dispersion" (qualitative study of condensed vs dispersed layouts). https://www.nngroup.com/articles/content-dispersion/
2. Rosenholtz, R., Li, Y., Mansfield, J., and Jin, Z. (2005). "Feature Congestion: A Measure of Display Clutter." ACM SIGCHI (CHI 2005). DOI 10.1145/1054972.1055078. https://unpaywall.org/10.1145%2F1054972.1055078
3. Rosenholtz, R., Li, Y., and Nakano, L. (2007). "Measuring Visual Clutter." Journal of Vision. PubMed 18217832. https://pubmed.ncbi.nlm.nih.gov/18217832
4. Pankok, E. and Kaber, D. (2018). Ergonomics (integrated clutter measure and critique of Feature Congestion's task-performance link). https://stacks.cdc.gov/view/cdc/210879/cdc_210879_DS1.pdf
5. Two-by-two between-subjects study on social app UI structure and density (preference outcome). Venue and authors not confirmed; see Open questions.
6. CHI 2020 online study on website visual complexity, search efficiency, and recall (165 participants). Venue and URL not confirmed; see Open questions.

Additional reading (not scored as core evidence): McGurgan et al. (2021), SCITEPRESS, https://www.scitepress.org/Papers/2021/102638/102638.pdf, which reviews the data-ink ratio concept and notes its limited experimental validation.

## Open questions
- Source 5 and source 6 were seen only as search summaries; I did not open the full papers, so their authors, venues, and exact figures are unverified.
- The Rosenholtz 2005 author list is from the search record and the DOI; I did not open the paper to confirm the full author order.
- The Pankok and Kaber 2018 author list and title are from a search excerpt; the stacks copy was not opened.
- The academia.edu record "Quantification of Interface Visual Complexity" could not be fetched (HTTP 403). Its findings are not used.
- No study found gives a numeric density target (items per region or percent empty). Steps 3 to 4 and the rubric anchors are judgment calls, not research thresholds.
- Sources disagree on how much data-ink minimalism helps. Tufte-style maximization of data ink is not empirically supported in the sources found, so the rubric does not reward it directly.
- Preference and task are confounded: some users prefer sparse layouts, so the rubric scores fit to task rather than to a single preferred density.
