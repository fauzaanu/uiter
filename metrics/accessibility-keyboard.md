# Keyboard Accessibility

> Measures whether every function can be reached and operated using only a keyboard in a logical order.

## What it measures

- Every interactive control (links, buttons, form fields, menus, tabs, toggles, custom widgets) can receive keyboard focus.
- Every function that works with a pointer can also be completed with keyboard input alone (Tab, Shift+Tab, Enter, Space, arrow keys, Escape).
- The sequence of focus stops follows the visual and reading order, so a keyboard user moves through the screen in the order the content is meant to be read.
- Components that capture focus (dialogs, menus, embedded players) can be entered and exited without a pointer.
- Opened content (dialogs, menus, popovers) is reached next to its trigger in the focus sequence.

## Research basis

- Keyboard operation is a Level A requirement: all functionality must be operable through a keyboard interface, regardless of whether focus order is logical. Operability (2.1.1) and sequence (2.4.3) are separate tests. Source: GOV.UK, "Guide to WCAG," https://alphagov.github.io/guide-to-wcag/sc/2.4.3.html
- Focus order must preserve the meaning and operation of the page. It need not match the visual layout exactly, but it should reinforce the reading order implied by the layout. Source: W3C, "Understanding SC 2.4.3: Focus Order" (WCAG 2.1), https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html
- A component is a keyboard trap only if focus cannot be moved out using the keyboard. Intentional focus confinement (for example, a modal dialog) is acceptable when the user is told how to leave. Source: W3C, "Understanding SC 2.1.2: No Keyboard Trap" (WCAG 2.1), https://www.w3.org/WAI/WCAG21/Understanding/no-keyboard-trap
- Positive tabindex values disrupt focus order and are hard to maintain; tab order should follow the DOM and visual order. Source: WebAIM, "Keyboard Accessibility," https://webaim.org/techniques/keyboard/ (practitioner guidance, not a study).
- Problems encountered by blind users are not fully captured by WCAG success criteria: in a task study of 32 blind users on 16 sites, only 50.4% of problems were covered by WCAG 2.0. This supports pairing the rubric with manual task-based checks. Source: Power, Freire, Petrie and Swallow, "Guidelines are only half of the story: accessibility problems encountered by blind users on the web," CHI 2012, pp. 433-442, DOI 10.1145/2207676.2207736.
- Screen reader users frequently report that page structure and unlabeled controls cost them time; in a diary study of 100 blind users, participants reported losing about 30.4% of their time to web frustrations. Source: Lazar, Allen, Kleinman and Malarkey, "What Frustrates Screen Reader Users on the Web: A Study of 100 Blind Users," International Journal of Human-Computer Interaction, 2007, DOI 10.1080/10447310709336964. The study is cited here for context, not for a keyboard-specific threshold.

## Scoring method

1. Load the screen and clear focus by clicking an empty area. Press Tab repeatedly from the top of the page until focus reaches the last control. Record each focus stop in order.
2. Press Shift+Tab from the last control back to the first. Confirm the reverse order mirrors the forward order.
3. Count the interactive controls visible on screen and compare with the number of focus stops. Note any control that is skipped (not reachable).
4. For each control, activate it with Enter or Space (buttons, links) or arrow keys (menus, tabs, radio groups, sliders). Record whether the function completes.
5. For each opened layer (dialog, menu, popover, drawer), confirm focus moves into it, Tab cycles inside it, and Escape or a visible close control returns focus to the trigger. Record any case where focus is lost or stuck.
6. Check for focus jumps: any focus stop that is far from the previous one in visual order, or a control that receives focus twice in one forward pass. Record each occurrence.
7. Use a browser DevTools check or Accessibility Insights for Web (tab-stop visualization) to confirm the presence of positive tabindex values. Record the count.
8. Calculate: skipped or unreachable controls (S), focus-order breaks (B), keyboard traps or lost-focus events (T), and inoperable functions (F). Assign the score using the rubric.

## Scoring rubric

- **5 (exemplary):** All controls reachable; order matches visual and reading order; no positive tabindex; every function completes by keyboard; all layers enter and exit cleanly.
- **4 (good):** All functions operable; at most one minor order break that does not change meaning; one layer exits with a non-obvious but working path.
- **3 (adequate):** All functions operable, but two to three order breaks or one control reached only with extra presses; focus returns to the page top instead of the trigger after closing a layer.
- **2 (weak):** One function inoperable by keyboard, or four or more order breaks, or a layer that cannot be reached from its trigger.
- **1 (poor):** Several controls skipped or inoperable; focus is lost on common actions; a keyboard trap with no documented exit.
- **0 (severe failure):** The main task cannot be completed with a keyboard, or focus is trapped with no way out.

No numeric thresholds in the sources define an acceptable number of tab stops. The counts above are judgment-based.

## Automated checks (optional)

Partially reliable. axe-core can detect positive tabindex values, some missing keyboard handlers on custom widgets, and some focus traps in modals. It cannot judge whether the sequence is logical, whether a custom widget's arrow-key behavior matches the pattern, or whether a function completes. Manual tab-through remains required.

## Common failure patterns

- Custom controls built on `div` or `span` without tabindex or key handlers, so they cannot be reached or activated (WCAG 2.1.1).
- Positive tabindex values that pull a control to the front of the sequence, producing focus jumps (WCAG 2.4.3; CHI 2012 study of blind-user problems shows structural problems outside WCAG coverage).
- Modal dialogs that trap focus with no Escape or close control (WCAG 2.1.2).
- Closing a menu or dialog that drops focus to the top of the page, forcing the user to tab through the whole screen again.
- Hidden or off-screen controls that remain in the tab sequence, or visible controls removed from it with `display` or `visibility` tricks.

## Sources

1. W3C, "Understanding SC 2.4.3: Focus Order (Level A)," WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/focus-order.html
2. W3C, "Understanding SC 2.1.2: No Keyboard Trap (Level A)," WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/no-keyboard-trap
3. GOV.UK, "Guide to WCAG 2.4.3 Focus Order." https://alphagov.github.io/guide-to-wcag/sc/2.4.3.html
4. WebAIM, "Keyboard Accessibility." https://webaim.org/techniques/keyboard/
5. Power, C., Freire, A. P., Petrie, H., and Swallow, D. (2012). "Guidelines are only half of the story: accessibility problems encountered by blind users on the web." CHI 2012. DOI 10.1145/2207676.2207736.
6. Lazar, J., Allen, A., Kleinman, J., and Malarkey, C. (2007). "What Frustrates Screen Reader Users on the Web: A Study of 100 Blind Users." International Journal of Human-Computer Interaction. DOI 10.1080/10447310709336964.

## Open questions

- I did not locate a controlled study that measures keyboard task completion or focus-order errors against outcome measures. The keyboard rubric is therefore built from the WCAG Understanding text and practitioner guidance, and the 0 to 5 anchors are judgment calls.
- The WCAG 2.1.2 Understanding page was seen in search snippets; the editor's draft adds that focus is not trapped if the user can exit by a standard key. The published 2.1 wording was used here. Sources conflict on whether an escape in only one direction is sufficient, so the rubric treats a documented exit as acceptable.
- The Lazar et al. (2007) abstract was seen through indexes and secondary summaries, not the full text. Its exact ranking of frustrations differs between sources, so only the aggregate time figure is cited.
- WCAG 2.1.1 (Keyboard) was cited through the GOV.UK guide's description, not the W3C text.
- Whether a positive tabindex always breaks the user's experience, rather than only the code's maintainability, is supported by practitioner guidance but not by a measured user study.
