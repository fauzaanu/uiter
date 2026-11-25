# Responsiveness

> Scores whether a screen's layout and content adapt without breaking, losing information, or requiring horizontal scrolling across viewport widths and both orientations.

## What it measures

- Horizontal overflow: no content, image, or control extends past the viewport edge, and no horizontal scrollbar appears at the narrowest tested width.
- Reflow: at a 320 CSS px viewport (equivalent to 400% zoom on a 1280 px desktop), all text and controls remain readable and usable in one column without two-dimensional scrolling.
- Content preservation: navigation, primary actions, and information present at wide widths remain reachable at narrow widths, possibly through collapse or reordering rather than deletion.
- Orientation: the screen works in portrait and landscape and does not lock to one orientation or show a "rotate your device" block.
- Text integrity: headings, labels, and buttons wrap or stack instead of truncating, overlapping, or clipping.

## Research basis

- Content must reflow to a 320 CSS px width without loss of information or two-dimensional scrolling, except for content that requires two-dimensional layout (maps, data tables, diagrams). Source: W3C, *Understanding WCAG 2.2, SC 1.4.10 Reflow (Level AA)*, https://www.w3.org/WAI/WCAG22/Understanding/reflow
- Content must not be restricted to one display orientation unless that orientation is essential. Source: W3C, *Understanding WCAG 2.2, SC 1.3.4 Orientation (Level AA)*, https://www.w3.org/WAI/WCAG22/Understanding/orientation. The W3C notes that users may have devices mounted in a fixed orientation, which is why locking is treated as a barrier.
- Breakpoints should mark where the layout changes arrangement, not simply where device classes begin. Source: Nielsen Norman Group, "Grids, Layouts, and Responsive Design," https://www.nngroup.com/articles/breakpoints-in-responsive-design/. The search summary gave a tablet band of about 500 to 1200 px; the full article was not opened, so treat that figure as unverified.
- Responsive pages were rated more favourably than fixed-layout pages on perceived usability in a controlled comparison of desktop and mobile tourism websites. Source: Springer, ENTER 2015 proceedings, DOI 10.1007/978-3-319-14343-9_43 (authors not captured in search results).
- A study of responsive versus fixed-layout sites on laptops and smartphones found the responsive version better for user experience, while information-architecture tasks required more scrolling and clicking. Source: *Jurnal Teknologi*, "The Effect of Responsive Web Design on the User Experience with Laptop and Smartphone Devices," https://journals.utm.my/jurnalteknologi/article/view/6041 (authors not captured in search results).

## Scoring method

1. Open the screen at 1280 px wide, then at 768 px, then at 390 px, then at 320 px (in a browser at 100% zoom, or by setting the viewport in devtools).
2. At each width, check for a horizontal scrollbar on the page. Record pass or fail. In a browser console, compare `document.documentElement.scrollWidth` with `window.innerWidth`; a difference above 0 is a failure.
3. At 320 px, scroll the full screen and confirm every text block, control, and image is visible in a single column. Note any element that is clipped, overlaps another, or needs two-dimensional scrolling (exempt only if it is a map, chart, or data table).
4. Compare the navigation and primary actions at 1280 px with those at 390 px. Record any function that is missing, not just relocated.
5. Rotate or emulate landscape at 844 × 390 (a phone size) and portrait at 390 × 844. Check for a lock, a rotate prompt, or content that is cut off.
6. Record the count of failing widths, orientations, and element types. Score with the rubric below, citing the widths and elements.

## Scoring rubric

- **0**: Horizontal scrolling or clipped content at 320 px; key content or actions missing at narrow widths; the screen is locked to one orientation.
- **1**: Overflow or clipping at two or more tested widths, or one orientation fails; some functions are lost on narrow screens.
- **2**: Reflows at most widths, but one of the 320 px, portrait, or landscape checks fails in a way that hides or truncates information.
- **3**: Passes the 320 px reflow and both orientations, with minor issues such as cramped spacing, awkward wrapping, or an oversized element at one width.
- **4**: Passes all widths and orientations. Navigation and actions adapt in form (collapsed menu, stacked buttons) without loss of function.
- **5**: Passes all checks, and layout changes at breakpoints that match the content's structure. Tables and complex widgets have a stated narrow-width pattern, and no tested size needs a rotate prompt.

## Automated checks (optional)

Partially reliable. A headless browser (Playwright or Puppeteer) can load the page at the fixed widths above, read `scrollWidth` against the viewport, and capture screenshots for review. It detects horizontal overflow and some off-screen elements, but cannot judge whether a reflowed layout is readable, whether a function was silently removed, or whether a two-dimensional exception is justified. axe-core does not test reflow or orientation. Manual review is required for scores above 2.

## Common failure patterns

- Fixed-width containers, large images, or wide tables overflow the viewport at 320 px, producing a horizontal scrollbar (WCAG 1.4.10).
- Navigation is hidden behind a menu with no visible trigger, so features are effectively lost on narrow screens (Nielsen Norman Group breakpoint guidance, as the layout change should not remove content).
- A "rotate your device" overlay or portrait-only layout blocks landscape use (WCAG 1.3.4).
- Breakpoints are set by device families rather than by where the layout visibly breaks, so content is cramped just above a breakpoint.
- Text truncates with ellipses or clips inside fixed-height containers when translated or enlarged.

## Sources

1. W3C, *Understanding WCAG 2.2: SC 1.4.10 Reflow*, https://www.w3.org/WAI/WCAG22/Understanding/reflow
2. W3C, *Understanding WCAG 2.2: SC 1.3.4 Orientation*, https://www.w3.org/WAI/WCAG22/Understanding/orientation
3. Nielsen Norman Group, "Grids, Layouts, and Responsive Design," https://www.nngroup.com/articles/breakpoints-in-responsive-design/
4. Springer, ENTER 2015 proceedings, DOI 10.1007/978-3-319-14343-9_43, https://rd.springer.com/chapter/10.1007/978-3-319-14343-9_43
5. *Jurnal Teknologi*, "The Effect of Responsive Web Design on the User Experience with Laptop and Smartphone Devices," https://journals.utm.my/jurnalteknologi/article/view/6041

## Open questions

- Breakpoint values conflict across sources: NN/g's tablet band (about 500 to 1200 px) differs from government and commercial guidance (768 to 1024 px). The rubric does not prescribe breakpoints and uses observed breakage instead.
- Authors and full-text findings for sources 4 and 5 were not verified beyond search summaries.
- The 2025 Preprints.org study (manuscript 202511.2063) reported positive results, but it is a preprint and was not used as a citation.
- The 0 to 5 anchors for scores 3 to 5, and the rule that a dropped function counts as a failure, are judgment calls rather than research-backed thresholds.
- The 844 × 390 and 390 × 844 test sizes are common device dimensions chosen for convenience, not sourced thresholds.
