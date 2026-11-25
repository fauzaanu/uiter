# Grid Layout

> Measures whether content is organized on a stable column and row structure that governs placement.

## What it measures

- A repeating column structure (column count, gutter width, outer margins) that content and components visibly snap to.
- Consistent placement of major blocks (cards, panels, sidebars, headers) on the same column boundaries from one section or screen to the next.
- Row rhythm: related items share a common top line and a common height or baseline step across the row.
- Whether the column structure is retained when the layout changes width, or collapses in an orderly way rather than arbitrarily.
- Whether elements that are meant to be peers share the same width or span, and whether spans are whole multiples of the column unit.

## Research basis

- A grid is a structure of columns, gutters and margins; common web types are column, modular and hierarchical. Predictable grid-based interfaces are easier for users to scan. Nielsen Norman Group, "Using Grids in Interface Designs," https://nngroup.com/articles/using-grids-in-interface-designs (retrieved as search-result excerpt; full text not read).
- Grid optimality is measurable and affects perceived layout quality. The GRIDS study had 13 participants rate UI sketches on a 0 to 100 scale across optimal, sub-optimal and far-from-optimal grid conditions. Authors not captured in the search result. arXiv:2001.02921, https://arxiv.org/pdf/2001.02921.
- Balance and symmetry are established aesthetic measures of screen layout. Ngo, Teo and Byrne model balance as the weight difference between the two sides of a layout along its axes, and report that these measures relate to viewer perception. Ngo, Teo and Byrne, "Modelling Interface Aesthetics," Information Sciences 152 (2003), pp. 25-46 (abstract and excerpts only).
- A grid-aligned layout is a stated precondition for reflow. WCAG 2.1 SC 1.4.10 (Level AA) requires content to reflow to a single column at 320 CSS pixels without two-dimensional scrolling, except where two-dimensional layout is essential. W3C, "Understanding Reflow," https://www.w3.org/WAI/WCAG21/Understanding/reflow.
- Wireframes rated for visual quality differ by layout condition, with grid-aligned layouts among the conditions compared. arXiv:2609.03918, https://arxiv.org/pdf/2609.03918 (abstract only).

## Scoring method

1. Open the screen at a desktop width and note the number of columns in use. Identify the gutter and outer margin values from the design file or computed styles.
2. Draw or overlay the column grid on the screenshot. Mark every major block edge (left, right, top) that sits on a column boundary and every one that does not.
3. Check placement across sections: compare the left and right edges of the main blocks in each section. Count how many distinct column starts appear for peer items.
4. Check rows: list items that sit side by side and confirm they share a top line and comparable height.
5. Resize to a tablet and a phone width (or inspect the responsive breakpoints). Confirm the column structure is kept or collapses in a stated order.
6. Record the observations: columns used, percentage of major edges on grid, number of off-grid placements, and the breakpoints checked.

## Scoring rubric

- **0**: No discernible column structure. Blocks start at arbitrary x-positions and peer items do not share edges.
- **1**: A grid exists in intent but is broken on most screens. Fewer than half of major edges sit on a column boundary.
- **2**: Partial structure. Main content aligns, but sections or peer rows use different column counts or gutters.
- **3**: Mostly consistent. Most major edges and peer rows sit on the same columns, with a few exceptions that do not break the reading order.
- **4**: Consistent across sections and breakpoints. Spans are whole column multiples and rows share top lines and heights.
- **5**: Exemplary. A single documented grid governs every section and breakpoint, and placement is predictable without exceptions.

Where a reflow requirement applies, a layout that cannot reach a single column at 320 CSS pixels caps the score at 2.

## Automated checks (optional)

None reliable; manual review only. Browser computed-style inspection can report element edges and gutters, but it cannot decide whether a given placement is intentional or which columns the design system defines.

## Common failure patterns

- Mixed column counts across sections (for example, a three-column grid in one band and a four-column grid in the next), which makes peer edges fail to align.
- Peer cards with different widths or different top lines within one row, weakening the scan path.
- Gutters that change per component rather than per system, so the same spacing reads differently in each block.
- Grids that hold on desktop but drop to an unstructured stack on tablet, leaving elements at arbitrary positions.
- Grids applied only in the design file and not in the implementation, so measured edges drift from the specified columns.

## Sources

1. Nielsen Norman Group. "Using Grids in Interface Designs." https://nngroup.com/articles/using-grids-in-interface-designs
2. Ngo, D. C. L., Teo, L. S., and Byrne, J. G. "Modelling Interface Aesthetics." Information Sciences 152 (2003), pp. 25-46.
3. GRIDS: Interactive Layout Design with Integer Programming. arXiv:2001.02921. https://arxiv.org/pdf/2001.02921
4. W3C. "Understanding Success Criterion 1.4.10: Reflow." WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/reflow
5. Wireframe visual-quality study (grid-aligned conditions). arXiv:2609.03918. https://arxiv.org/pdf/2609.03918

## Open questions

- The GRIDS and arXiv:2609.03918 papers were seen only as search-result excerpts. Their authors, participant counts and effect sizes are not verified beyond the snippets, and the 0 to 100 and 1 to 10 rating scales are not normalized here.
- The Ngo et al. 2003 full text was not accessible. The balance measure is cited for the concept only, not its formula.
- No source gives a numeric threshold for how many edges must sit on grid, or for a column count. The 0 to 5 anchors and the "cap at 2" reflow rule are judgment calls, not research-backed thresholds.
- A search turned up an eye-tracking comparison of grid and column layouts (Springer, DOI 10.1007/978-3-319-91803-7_20), but only its abstract was seen, so it is not cited here.
- Whether a grid must be present in the implementation (not only in the design file) is a reviewer convention; no source was found to settle it.
