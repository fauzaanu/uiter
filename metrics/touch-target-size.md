# Touch Target Size

> Scores whether tappable and clickable targets are large enough, and spaced far enough apart, for users to hit them accurately with a finger or thumb.

## What it measures

- The rendered hit area of each button, link, icon button, checkbox, radio, toggle, and tab, measured in CSS pixels (or points/dp on native).
- Whether the hit area is larger than the visible glyph when padding is used (a 16px icon with 12px of invisible padding is a 40px target).
- Gaps between adjacent targets, especially in toolbars, lists, icon rows, and pagination.
- Whether the primary action of a screen is larger than secondary and tertiary controls.
- Whether targets remain usable on a phone-width viewport, not only on desktop.

## Research basis

- Targets smaller than 24 x 24 CSS px fail WCAG 2.2 SC 2.5.8 (AA) unless a spacing or equivalent exception applies. The spacing test: a 24 px diameter circle centred on each undersized target must not intersect another target. Inline links are exempt. WCAG 2.2 is a W3C Recommendation (5 October 2023). Source: W3C, "Understanding Success Criterion 2.5.8: Target Size (Minimum)", https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- The AAA criterion 2.5.5 sets 44 x 44 CSS px with no spacing exception. Source: same W3C page.
- Parhi, Karlson and Bederson (2006) studied one-handed thumb use on small touchscreens and reported target sizes of 9.2 mm for discrete tasks and 9.6 mm for serial tasks as large enough without degrading performance or preference. Those figures come from search-result summaries, not a full read of the paper. Source: Parhi, P., Karlson, A. K., and Bederson, B. B., "Target Size Study for One-Handed Thumb Use on Small Touchscreen Devices," MobileHCI 2006, pp. 203-210, DOI 10.1145/1152215.1152260, https://dx.doi.org/10.1145/1152215.1152260
- Nielsen Norman Group recommends a minimum of about 1 cm x 1 cm for touch targets, citing fingertip size and the small-target error literature. Source: Nielsen Norman Group, "Touch Target Size," https://www.nngroup.com/articles/touch-target-size/
- Android guidance recommends touch targets of at least 48 x 48 dp. Source: Google, "Touch target size," Android Accessibility Help, https://support.google.com/accessibility/android/answer/7101858

## Scoring method

1. Select the screen at phone width (390 px) and at desktop width. Score both; report the lower score.
2. List every interactive element: buttons, links, icon buttons, form controls, tabs, toggles, close buttons, and list-row actions.
3. For each element, measure the hit area with browser devtools (computed `width`/`height` of the element, plus any padding or pseudo-element that extends the clickable region). Record the smallest dimension.
4. Mark each element as Pass (hit area at least 44 x 44), Acceptable (at least 24 x 24), or Fail (below 24 x 24).
5. For every Fail, check spacing: draw a 24 px circle centred on the target's bounding box and confirm it does not hit a neighbour. Record the failures that also fail spacing.
6. Identify the primary action(s) on the screen and record their size separately.
7. Record the counts (total, Pass, Acceptable, Fail, Fail-with-crowding), the smallest target found with its selector, and the primary-action size. Assign the score using the rubric.

## Scoring rubric

- **5 (exemplary):** All interactive targets are at least 44 x 44 CSS px. Adjacent targets have at least 8 px between hit areas. Primary actions are clearly the largest.
- **4 (strong):** All targets meet 24 x 24 px. Primary actions are at least 44 x 44 px. Any target below 44 px has at least 8 px of clear space.
- **3 (adequate):** All targets meet 24 x 24 px or pass the spacing exception. Some secondary targets are 24-43 px with reduced spacing, and primary actions are at least 24 px.
- **2 (weak):** Several targets are below 24 px and crowd each other. Some primary actions are hard to hit.
- **1 (poor):** Many targets are below 24 px and touching, with frequent overlap on phone width.
- **0 (severe failure):** Core controls are under about 16 px or cannot be tapped reliably; overlapping targets block primary tasks.

## Automated checks (optional)

- axe-core rule `target-size` (WCAG 2.2) flags targets under 24 x 24 px that fail the spacing exception. It cannot judge primary-action prominence, padding intent, or native-app dp/pt sizes, and it sees only rendered web content at the tested viewport. Source: Deque, axe rule "target-size", https://dequeuniversity.com/rules/axe/4.7/target-size
- Use it as a floor check only; it does not confirm the 44 px or 8 px targets in the 4 and 5 anchors.

## Common failure patterns

- Icon-only buttons at 16-20 px with no padding, which pass visually but fail the 24 px floor (WCAG 2.2 SC 2.5.8).
- Dense toolbars and table row actions packed with less than 4 px between hit areas, producing mis-taps on neighbours (Parhi et al., 2006; NN/g).
- Visible text links sized to the glyph rather than the line box, leaving a hit area far smaller than the layout suggests.
- Close, dismiss, and checkbox controls that are sized as decoration rather than as targets.
- Primary and destructive actions the same size as secondary ones, so the most important tap is no easier to hit.

## Sources

- W3C, "Understanding Success Criterion 2.5.8: Target Size (Minimum)," WCAG 2.2, 2023. https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Parhi, P., Karlson, A. K., Bederson, B. B., "Target Size Study for One-Handed Thumb Use on Small Touchscreen Devices," MobileHCI 2006. DOI 10.1145/1152215.1152260. https://dx.doi.org/10.1145/1152215.1152260
- Nielsen Norman Group, "Touch Target Size." https://www.nngroup.com/articles/touch-target-size/
- Google, "Touch target size," Android Accessibility Help. https://support.google.com/accessibility/android/answer/7101858
- Deque, axe rule "target-size." https://dequeuniversity.com/rules/axe/4.7/target-size

## Open questions

- The Parhi et al. figures were read from summaries. The full paper's accuracy-by-size data was not checked.
- The Apple 44 pt figure appeared only in secondary sources in search results; Apple's Human Interface Guidelines were not fetched and should be verified before citing.
- The 8 px spacing in the 4 and 5 anchors is a judgment call, not a research-backed threshold.
- The 16 px floor in the 0 anchor is a judgment call.
- Sizes measured in CSS px do not map directly to physical millimetres across devices, so the mm figures from Parhi et al. are not used as rubric thresholds.
