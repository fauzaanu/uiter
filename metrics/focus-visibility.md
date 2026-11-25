# Focus Visibility

> Measures whether the currently focused element is clearly and consistently indicated.

## What it measures

- Every interactive element (links, buttons, form fields, custom controls) shows a visible change when it receives keyboard focus.
- The focus indicator is distinguishable from the unfocused state, meaning its pixels change in color, outline, or shadow, not only in a subtle tint.
- The same indicator style is used across similar components on the screen, so one pattern is learned once.
- The indicator is not removed with `outline: none` or equivalent without a replacement.
- The focused element is not hidden behind sticky headers, cookie banners, or overlays.

## Research basis

- WCAG 2.2 SC 2.4.7 (Focus Visible, Level AA) requires that any keyboard-operable interface shows a visible indicator of keyboard focus. It does not prescribe the form of the indicator. Source: W3C WAI, "Understanding SC 2.4.7: Focus Visible," https://www.w3.org/WAI/WCAG22/Understanding/focus-visible
- WCAG 2.2 SC 2.4.13 (Focus Appearance, Level AAA) sets measurable thresholds: the indicator must cover at least the area of a 2 CSS pixel thick perimeter around the unfocused component, and must reach at least a 3:1 contrast ratio between the focused and unfocused states. Source: W3C WAI, "Understanding SC 2.4.13: Focus Appearance," https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance
- In the final WCAG 2.2 numbering, Focus Not Obscured is split into Minimum (2.4.11, AA) and Enhanced (2.4.12, AAA), and Focus Appearance is 2.4.13. Source: Center for Digital Accessibility (CMU), "What's New in 2.2," https://cmu.edu/computing/dao/news/2023/nov/wcag-2.2.html
- The W3C "What's New in WCAG 2.2" summary lists the focus-related criteria as a group, confirming the same numbering scheme. Source: W3C WAI, "What's New in WCAG 2.2," https://w3.org/WAI/standards-guidelines/wcag/new-in-22/
- Removing focus styles without a replacement makes keyboard navigation effectively unusable, because users cannot see where they are on the page. Source: Mozilla Hacks, "Indicating focus to improve accessibility" (2019), https://hacks.mozilla.org/2019/06/indicating-focus-to-improve-accessibility/ (seen as a search snippet; full text not fetched)
- Practical guidance on designing indicators that meet the WCAG thresholds, including contrast against adjacent colors. Source: Sara Soueidan, "A guide to designing accessible, WCAG-conformant focus indicators," https://sarasoueidan.com/blog/focus-indicators/ (practitioner guidance, not peer-reviewed)

## Scoring method

1. Open the screen at a standard desktop width (1280 px or wider) with no mouse input. Reload so focus starts at the top of the page.
2. Press Tab to move focus through every interactive element in order. Use Shift+Tab to check the reverse order for at least the first three elements.
3. For each element, take a screenshot of the focused state and a screenshot of the same element unfocused.
4. For each focused element, record: (a) visible change yes/no; (b) indicator type (outline, box-shadow, background, border); (c) measured thickness in CSS px, using devtools computed styles for `outline-width` or `box-shadow` spread; (d) contrast between focused and unfocused pixels, using a contrast checker on sampled colors.
5. Check consistency: compare the indicator style across all elements of the same type. Count distinct styles.
6. Check obstruction: scroll the focused element to the viewport edge and confirm it is not covered by fixed or sticky elements.
7. Record results in a table with one row per element: element, focus visible (Y/N), indicator, thickness, contrast, obstructed (Y/N).
8. Score using the rubric. Note the percentage of focusable elements with a visible indicator, the number of distinct indicator styles, and any obstructed elements.

## Scoring rubric

- **0 - Severe failure:** No focus indicator on most interactive elements, or focus styles are removed with no replacement. Focus cannot be followed by eye.
- **1 - Poor:** Indicator present on fewer than half of elements, or changes are hard to see (for example, a color shift with no outline and under 3:1 contrast against the unfocused state).
- **2 - Weak:** Indicator on most elements, but inconsistent: two or more unrelated styles for the same component type, or some elements are obscured by sticky or fixed UI.
- **3 - Acceptable:** Visible indicator on all elements, meets WCAG 2.4.7 (Level AA). Style is roughly consistent. Contrast or thickness is below the 2.4.13 thresholds (2 CSS px perimeter, 3:1) but still clearly visible on inspection.
- **4 - Good:** Meets the 2.4.13 thresholds (2 CSS px perimeter, 3:1 focused against unfocused) on most elements. One indicator style used across all components. No obstruction found in the test.
- **5 - Exemplary:** Meets the 2.4.13 thresholds on every element, uses one documented indicator pattern across the screen, and keeps focused elements in view through scroll and overlays.

## Automated checks (optional)

None reliable; manual review only. Computed-style reads can report outline and box-shadow values, but they cannot judge perceived visibility or whether the focus change is visible against adjacent colors.

## Common failure patterns

- Global `outline: none` or `:focus { outline: 0 }` in a reset stylesheet, with no replacement style. This is the most common cause of invisible focus (Mozilla Hacks, 2019).
- Relying on a color change alone, which can fall below the 3:1 contrast threshold in 2.4.13 and may not be perceived by users with color vision deficiency.
- Inconsistent styles: buttons use a ring, links use an underline, and custom widgets use a background tint, so users cannot predict the indicator.
- Focus obscured by sticky headers, cookie banners, or chat widgets, which WCAG 2.2 addresses with Focus Not Obscured (2.4.11, AA).
- Focus indicator visible only on `:focus` but not `:focus-visible`, or the reverse, which hides the indicator for some input methods.

## Sources

1. W3C WAI. "Understanding SC 2.4.7: Focus Visible." WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/focus-visible
2. W3C WAI. "Understanding SC 2.4.13: Focus Appearance." WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance
3. W3C WAI. "What's New in WCAG 2.2." https://w3.org/WAI/standards-guidelines/wcag/new-in-22/
4. Center for Digital Accessibility, Carnegie Mellon University. "What's New in 2.2." November 2023. https://cmu.edu/computing/dao/news/2023/nov/wcag-2.2.html
5. Mozilla Hacks. "Indicating focus to improve accessibility." 2019. https://hacks.mozilla.org/2019/06/indicating-focus-to-improve-accessibility/
6. Soueidan, Sara. "A guide to designing accessible, WCAG-conformant focus indicators." https://sarasoueidan.com/blog/focus-indicators/

## Open questions

- No peer-reviewed user study on focus indicator visibility was found in the search. The rubric anchors rely on WCAG thresholds, not on measured user performance. Score levels 1 to 4 are judgment calls.
- The 2.4.13 Focus Appearance criterion is AAA. The 3:1 adjacent-color requirement is described differently in secondary sources (DAISY summary and older drafts). The official Understanding text should be checked before citing the adjacent-color test.
- Non-text contrast (WCAG 1.4.11, 3:1 for UI component states) is likely the relevant AA test for indicator contrast, but no source for it was retrieved in this search. Confirm before relying on it.
- The Mozilla and Soueidan claims were checked only through search snippets, not full-text fetches.
- Whether the 2 CSS px perimeter is measured against the component or its bounding box is not resolved in the sources seen. The method assumes the component's bounding box.
- The 1280 px test width and the "three elements" Shift+Tab sample are conventions, not research-backed values.
