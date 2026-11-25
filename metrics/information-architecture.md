# Information Architecture

> Measures whether content is grouped, labeled, and structured in a logical way that matches user mental models.

## What it measures

- Whether items in a navigation menu, sidebar, or tab set are grouped into categories that a user would expect to contain them.
- Whether category and section labels use words users recognize, not internal jargon, and whether they are distinct from each other.
- Whether each item has one obvious home, or, where it legitimately belongs in several places, whether it appears in each.
- Whether parent categories are themselves destinations, and whether the hierarchy depth is consistent across branches.
- Whether headings on a page partition its content into sections that match the section titles a user would scan for.

## Research basis

- **Card sorting reveals grouping expectations, and participant groupings are reasonably consistent for the same content.** Katsanos et al. ran six open card sorts with 140 participants across a travel site and an e-shop and reported highly similar groupings for the same content (arXiv:1903.08644, 2019, https://arxiv.org/pdf/1903.08644).
- **The analysis method changes the resulting structure.** Nawaz (2012) argues that the analysis chosen can change both the resulting structure and the agreement level among users, even for similar data (https://research-api.cbs.dk/ws/files/58892620/Ather_Nawaz_2012.pdf). Paea, Katsanos and Bulivou (2022, International Journal of Human-Computer Interaction, DOI 10.1080/10447318.2022.2112077) propose category validity and related methods for open card sort analysis.
- **Card sorting generates candidate groupings; tree testing evaluates a structure.** NN/g treats card sorting as discovery and tree testing as evaluation of an existing or proposed navigation structure (https://nngroup.com/articles/card-sorting-tree-testing-differences).
- **Tree-test findability is measured by success and directness.** Success is the share of users who reach the correct destination; directness is the share who do so without backtracking (NN/g, https://nngroup.com/articles/interpreting-tree-test-results/). Scores should be reported per task, since an average can hide one failed destination.
- **Category labels that are only text break user expectations.** Baymard's e-commerce research, as reported by Smashing Magazine (2013), found that hierarchies made only of labels or headers force users into narrower sections than they want, and recommends clickable parent categories (https://www.smashingmagazine.com/2013/11/guidelines-navigation-categories-ecommerce-study).
- **Multiple routes to content are an accessibility expectation.** WCAG 2.1 SC 2.4.5 (Level AA) requires at least two ways to reach each page that is not part of a process, because people differ in which navigation method works for them (https://www.w3.org/WAI/WCAG21/Understanding/multiple-ways).

## Scoring method

1. Identify the primary navigation container on the screen (top nav, sidebar, tab bar, or section list). Record its item count and the number of levels.
2. List every top-level label verbatim. Mark each as clear, ambiguous, or generic (for example "Other", "More", "Misc", "Resources").
3. Check for overlap: flag any two labels whose intended contents a reviewer cannot tell apart from the label alone.
4. For each group, sort its items into the category they most naturally belong to. Record any item that fits two groups, and any item with no obvious group.
5. Check whether each parent category is a clickable destination. Record each parent that is a plain text label with no link.
6. Check placement consistency: if a route or item appears in two places, confirm both point to the same destination.
7. On the page body, list the section headings in order. Check that each heading names the content beneath it and that no two headings overlap in scope.
8. Record counts (ambiguous labels, misfiled items, non-clickable parents, unclear headings) and a 0 to 5 score using the rubric. Where a reviewer has access to a prototype, a tree test is the stronger check; a screen review cannot establish findability alone.

## Scoring rubric

- **0 (severe failure):** Groups are arbitrary or unlabeled; most labels are generic or overlapping; items have no discernible home.
- **1 (poor):** Several labels are ambiguous or internal jargon; multiple misfiled items; parent categories are dead text.
- **2 (weak):** Grouping is broadly logical, but at least one group is mixed and several labels need a second read to interpret.
- **3 (adequate):** Groups are coherent and labels are understandable; a small number of items sit awkwardly or some parents are not clickable.
- **4 (good):** Groups and labels match expected categories; each item has one clear home or a justified second listing; parents are destinations; headings track content.
- **5 (exemplary):** All of the above, with labels in customer vocabulary, consistent depth across branches, and evidence (for example tree-test results) that users reach the right destination directly.

## Automated checks (optional)

None reliable; manual review only. Link and heading extraction can be scripted (for example counting nav items, heading levels, and non-link parent elements), but whether a label matches user expectation cannot be detected automatically.

## Common failure patterns

- Catch-all groups ("Other", "More", "Misc") that absorb items the author could not place, which reflects an unresolved structure (Paea et al., 2022, on category validity).
- Internal organizational terms used in place of the words users say; Baymard-reported guidance favors customer vocabulary (via Smashing Magazine, 2013).
- Parent categories that open a menu but cannot be clicked, which removes a route users expect to work (Smashing Magazine, 2013; WCAG 2.4.5).
- The same item placed under different names in different sections, so users cannot tell whether they are the same thing.
- Headings that are decorative or generic ("Overview", "Details") instead of naming the content beneath them.

## Sources

1. Katsanos, C., et al. "Cross-study Reliability of the Open Card Sorting Method." arXiv:1903.08644, 2019. https://arxiv.org/pdf/1903.08644
2. Paea, S., Katsanos, C., and Bulivou, J. (2022). Information architecture analysis of open card sort data. International Journal of Human-Computer Interaction. DOI 10.1080/10447318.2022.2112077. (Metadata from search result; full text not reviewed.)
3. Nawaz, A. (2012). Analysis of open card sorting data. https://research-api.cbs.dk/ws/files/58892620/Ather_Nawaz_2012.pdf (Title and venue not confirmed from the document.)
4. Nielsen Norman Group. "Card Sorting vs. Tree Testing: What's the Difference?" https://nngroup.com/articles/card-sorting-tree-testing-differences
5. Nielsen Norman Group. "Interpreting Tree Test Results." https://nngroup.com/articles/interpreting-tree-test-results/
6. W3C WAI. "Understanding SC 2.4.5: Multiple Ways (Level AA)," WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/multiple-ways
7. Smashing Magazine (2013). "An E-Commerce Study: Guidelines For Better Navigation And Categories." https://www.smashingmagazine.com/2013/11/guidelines-navigation-categories-ecommerce-study

## Open questions

- Smashing Magazine's 2013 article reports Baymard findings secondhand; Baymard's current guidelines are paywalled and were not reviewed directly.
- The tree-test benchmark (a median task success of about 62% across 98 studies) was reported in a search summary without a verifiable primary source, so it is not used as a threshold here.
- Sample-size guidance is inconsistent: vendor sources cite 15 to 30 participants, and one cites 50 per tree test attributed to NN/g, which was not verified against NN/g.
- Nawaz (2012) and Paea et al. (2022) were identified from search metadata only; their specific findings are cited at the level the abstracts support.
- The 0 to 5 anchors, the "one clear home" standard, and the use of tree testing as the stronger check are judgment calls drawn from the sources above, not thresholds any source states.
- Whether a screen review can assess findability at all is a limitation: without a prototype or tree test, the score reflects grouping and labeling plausibility only.
