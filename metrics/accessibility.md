# Accessibility

> Can a person who uses a keyboard, a screen reader, or an imprecise pointer reach, identify, and operate every control on this screen?

## Covered metrics

- `accessibility-keyboard`: Keyboard Accessibility
- `screen-reader-semantics`: Screen Reader Semantics
- `focus-visibility`: Focus Visibility
- `touch-target-size`: Touch Target Size

## What it measures

- Reach: every interactive control can take keyboard focus, and every pointer function can be completed with Tab, Shift+Tab, Enter, Space, arrow keys, and Escape.
- Order: focus stops follow the visual and reading order, with no jumps and no positive `tabindex`.
- Layers: dialogs, menus, and popovers can be entered and left without a pointer, and focus returns to the trigger.
- Name: each control has a non-empty accessible name that states its purpose ("Close dialog", not "X"), and the visible label is contained in that name.
- Role: native elements are used where one fits; ARIA roles appear only where HTML cannot express the widget; static content has no interactive role.
- State: `aria-expanded`, `aria-pressed`, `aria-checked`, `aria-selected`, `aria-current`, `aria-invalid`, `disabled`, and `required` are exposed and change with the visual state.
- Focus indicator: every focusable element shows a visible change that is thick enough, contrasts with the unfocused state, uses one style across similar components, and is not hidden behind sticky or fixed UI.
- Target size: the hit area of each button, link, icon button, checkbox, toggle, and tab, including invisible padding, and the gap to its neighbours. Primary actions are the largest.
- Decorative icons and images are hidden from assistive technology.

## Scoring method

Work from the screenshot. Focus order, key handling, focus return, and the accessibility tree cannot be observed in one image. Measure what is visible, use the visible proxies named below for the rest, and say in the rationale which checks were not observable. Do not assume an unobserved check passes or fails.

1. List every interactive element: buttons, links, icon buttons, form controls, tabs, toggles, close buttons, and list-row actions.
2. Estimate each element's hit area in CSS px from the screenshot and record its smallest dimension. Mark it Pass (at least 44 x 44), Acceptable (at least 24 x 24), or Fail (below 24 x 24).
3. For every Fail, apply the spacing test: a 24 px circle centred on the target must not intersect another target. Record the gaps between adjacent targets in toolbars, icon rows, and row actions. Inline text links are exempt.
4. Record the size of the primary action and whether it is larger than secondary controls.
5. Naming proxy: flag every control with no visible text (icon-only buttons, unlabeled inputs, placeholder-only fields). Each needs a specific accessible name and is the likeliest place for a missing one.
6. Role proxy: flag elements that look custom-built (styled toggles, custom selects, clickable cards or rows, drag handles). These are the likeliest to lack focus, role, and key handling.
7. State proxy: for each stateful control visible (expanded section, selected tab, checked box, invalid field, disabled button), note whether the state is shown by more than color.
8. Order proxy: trace the visual reading order and note layouts where focus order is likely to diverge (multi-column blocks, visually reordered items, sticky bars, an open dialog or menu).
9. Focus indicator: if a focused element is visible, estimate indicator thickness and contrast against the unfocused state and check it is not obscured. If none is visible, note the check as unobserved and check that sticky headers or banners would not cover focused content.
10. Place each member on the rubric, combine them into one score, letting the failures most visible to a user pull the score down the most, and write todos for the lowest members first. Phrase unobserved checks as verification todos (for example, "confirm the icon button exposes the name 'Close dialog'").

## Scoring rubric

Thresholds come from the member files (WCAG 2.1.1, 2.1.2, 2.4.3, 2.4.7, 2.4.11, 2.4.13, 2.5.5, 2.5.8, 4.1.2).

- **0**: The main task cannot be completed with a keyboard, or focus is trapped with no way out. Most controls have no accessible name or the wrong role, and custom controls are bare `div` or `span` elements with no state. Focus styles are removed with no replacement. Core controls are under about 16 px or overlap so that primary tasks are blocked.
- **25**: Several controls are skipped or inoperable by keyboard, or a keyboard trap has no documented exit. Many controls lack names or states, and state attributes do not update. A focus indicator appears on fewer than half of elements, or is a color shift under 3:1 with no outline. Many targets are below 24 px and touching.
- **50**: All functions are operable, but there are two to three order breaks, or focus returns to the page top after a layer closes; or one function is inoperable. Some controls are unnamed or mis-roled, with states sometimes stale. Indicators appear on most elements but in two or more unrelated styles, or some are obscured by sticky UI. All targets meet 24 x 24 px or pass the spacing exception, with some secondary targets at 24 to 43 px and reduced spacing.
- **75**: All functions are operable, with at most one minor order break. All controls have specific names, correct roles, and states that update in sync with visuals; no ARIA is used where a native element works. Indicators meet the 2.4.13 thresholds (2 CSS px perimeter, 3:1 focused against unfocused) on most elements, in one style, with no obstruction. All targets meet 24 x 24 px, primary actions are at least 44 x 44 px, and any target under 44 px has at least 8 px of clear space.
- **100**: All controls are reachable in visual and reading order with no positive `tabindex`; every layer enters and exits cleanly. Names and states are verified with at least one screen reader on the critical flows, with no automated findings. Indicators meet the 2.4.13 thresholds on every element and focused elements stay in view. All targets are at least 44 x 44 CSS px with at least 8 px between hit areas, and primary actions are clearly the largest.

## Member sub-criteria

- `accessibility-keyboard`: Detail: metrics/accessibility-keyboard.md
- `screen-reader-semantics`: Detail: metrics/screen-reader-semantics.md
- `focus-visibility`: Detail: metrics/focus-visibility.md
- `touch-target-size`: Detail: metrics/touch-target-size.md

## Common failure patterns

- Custom controls built on `div` or `span` with no `tabindex`, role, or key handlers; `role="button"` on a non-focusable element.
- Positive `tabindex` values that produce focus jumps; hidden controls left in the tab sequence.
- Modal dialogs that trap focus with no Escape or close control; closing a layer drops focus to the top of the page.
- Icon-only buttons with no name, or a name such as "icon" or an SVG file name.
- Toggles and disclosure widgets whose `aria-expanded` or `aria-pressed` never updates.
- Visible label text that differs from the accessible name.
- Global `outline: none` with no replacement; focus shown by a color change alone; a different indicator style per component type.
- Focus obscured by sticky headers, cookie banners, or chat widgets.
- Icon-only buttons at 16 to 20 px with no padding; toolbars and row actions with less than 4 px between hit areas.
- Close, dismiss, and checkbox controls sized as decoration; primary actions no larger than secondary ones.

## Sources

- W3C, Understanding SC 2.4.3 Focus Order. https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html
- W3C, Understanding SC 2.1.2 No Keyboard Trap. https://www.w3.org/WAI/WCAG21/Understanding/no-keyboard-trap
- GOV.UK, Guide to WCAG 2.4.3 Focus Order. https://alphagov.github.io/guide-to-wcag/sc/2.4.3.html
- WebAIM, Keyboard Accessibility. https://webaim.org/techniques/keyboard/
- Power, Freire, Petrie, and Swallow (2012), Guidelines are only half of the story, CHI. DOI 10.1145/2207676.2207736
- Lazar, Allen, Kleinman, and Malarkey (2007), What Frustrates Screen Reader Users on the Web. DOI 10.1080/10447310709336964
- W3C, Understanding SC 4.1.2 Name, Role, Value. https://www.w3.org/WAI/WCAG21/Understanding/name-role-value
- W3C, Names and Descriptions, ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions
- Bezemer, Mesbah, and van Deursen (2015), Look Ma, No ARIA, W4A. https://researchconnect.stonybrook.edu/en/publications/look-ma-no-aria-generic-accessible-interfaces-for-web-widgets/
- web.dev, ARIA and HTML. https://web.dev/learn/accessibility/aria-html
- Deque, Top 5 Rules of ARIA. https://www.deque.com/?p=23982
- USA.gov (2024), Designing for people with disabilities. https://www.usa.gov/blog/2024/07/designing-for-people-with-disabilities
- W3C, Understanding SC 2.4.7 Focus Visible. https://www.w3.org/WAI/WCAG22/Understanding/focus-visible
- W3C, Understanding SC 2.4.13 Focus Appearance. https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance
- W3C, What's New in WCAG 2.2. https://w3.org/WAI/standards-guidelines/wcag/new-in-22/
- Carnegie Mellon University, What's New in 2.2 (November 2023). https://cmu.edu/computing/dao/news/2023/nov/wcag-2.2.html
- Mozilla Hacks (2019), Indicating focus to improve accessibility. https://hacks.mozilla.org/2019/06/indicating-focus-to-improve-accessibility/
- Soueidan, A guide to designing accessible, WCAG-conformant focus indicators. https://sarasoueidan.com/blog/focus-indicators/
- W3C, Understanding SC 2.5.8 Target Size (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html
- Parhi, Karlson, and Bederson (2006), Target Size Study for One-Handed Thumb Use, MobileHCI. https://dx.doi.org/10.1145/1152215.1152260
- Nielsen Norman Group, Touch Target Size. https://www.nngroup.com/articles/touch-target-size/
- Google, Touch target size, Android Accessibility Help. https://support.google.com/accessibility/android/answer/7101858
- Deque, axe rule target-size. https://dequeuniversity.com/rules/axe/4.7/target-size

## Open questions

- No controlled study was found that measures keyboard task completion, screen reader success with ARIA widgets, or focus indicator visibility. The bands rest on WCAG and practitioner guidance and are judgment calls.
- Sources conflict on whether a keyboard exit in only one direction is sufficient; a documented exit is treated as acceptable.
- 2.4.13 is Level AAA and its adjacent-color test is described differently across sources. WCAG 1.4.11 is probably the AA test for indicator contrast, but no source was retrieved. WCAG 2.5.3 was not verified.
- The 8 px spacing and 16 px floor are judgment calls, and the Apple 44 pt figure was not verified. The Parhi et al. millimetre figures are not rubric thresholds because CSS px do not map to physical size.
- Keyboard and screen reader behavior cannot be confirmed from a screenshot, so this group's score is less certain than the others when no live screen or markup is available.
