# Screen Reader Semantics

> Measures whether markup and labels expose correct roles, names, and states to assistive technology.

## What it measures

- Every interactive control (button, link, field, toggle, tab, menu item) has a non-empty accessible name that describes its purpose, not just its appearance (for example, an icon button named "Close dialog", not "X").
- Each control's role matches its behaviour: a native element where one fits (`<button>`, `<a href>`, `<input type="checkbox">`), and ARIA roles only where native HTML cannot express the widget.
- Stateful controls expose their current state in markup: `aria-expanded`, `aria-pressed`, `aria-checked`, `aria-selected`, `aria-current`, `aria-invalid`, `disabled`, and `required`, and these change when the visual state changes.
- Visible labels are programmatically associated with their inputs (`<label for>`, `aria-labelledby`), and a visible label text is contained in the accessible name.
- Non-interactive content is not given interactive roles, and decorative elements are hidden from the accessibility tree (`alt=""`, `aria-hidden` used sparingly).

## Research basis

- **Name, role, and state are required for all user interface components.** WCAG 2.1 Success Criterion 4.1.2 (Level A) requires that the name, role, state, and value of components be programmatically determinable, and gives custom toggle buttons and disclosure widgets built with ARIA as examples. Source: W3C, "Understanding SC 4.1.2: Name, Role, Value," https://www.w3.org/WAI/WCAG21/Understanding/name-role-value
- **Focusable interactive elements must have an accessible name.** The W3C ARIA Authoring Practices state that WAI-ARIA and WCAG both require all focusable, interactive elements to have an accessible name. Source: W3C, "Names and Descriptions," ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions
- **Native HTML is preferred; ARIA is a fallback.** The first rule of ARIA is to use a native element when one already provides the role and behaviour. A `<div role="button">` is announced as a button but gives none of the keyboard or activation behaviour of a `<button>`. Source: web.dev, "ARIA and HTML," https://web.dev/learn/accessibility/aria-html (secondary guidance; the W3C "Using ARIA" document states the same rule and should be checked directly).
- **Incorrect ARIA can be worse than none.** Practitioner evidence, cited by Deque, is that misused ARIA produces a more inaccessible experience than no ARIA. WebAIM's Million data reports that pages using ARIA have more detectable errors, although the sources quote different figures (see Open questions). Source: Deque, "Top 5 Rules of ARIA," https://www.deque.com/?p=23982
- **Users need precise state and control wording.** A usability report from a federal website study with assistive technology users found that generic terms such as "drop down" or "toggle" did not adequately describe an element's function or state. Source: USA.gov, "Designing for people with disabilities," https://www.usa.gov/blog/2024/07/designing-for-people-with-disabilities (practitioner report, small sample; not peer-reviewed).
- **Generic, ARIA-based widgets are a documented source of inconsistency.** Bezemer, Mesbah, and van Deursen, "Look Ma, No ARIA: Generic Accessible Interfaces for Web Widgets," W4A 2015, observe that ARIA markup is often used incorrectly and inconsistently, and evaluate their approach with 18 blind screen reader users. Source: https://researchconnect.stonybrook.edu/en/publications/look-ma-no-aria-generic-accessible-interfaces-for-web-widgets/ (abstract seen; full text not retrieved).

## Scoring method

1. Open the screen in a browser and note every interactive control and every control-like element (including `div`/`span` with click handlers).
2. Run an automated accessibility scan (see Automated checks) and record each name, role, and state finding with its element selector.
3. For each control, read its accessible name with the browser's accessibility inspector (Chrome DevTools "Accessibility" pane or Firefox "Accessibility" tab). Record the computed name and role. Mark the control as failing if the name is empty, is only a generic word ("button", "click here", "icon"), or differs from the visible label without reason.
4. Check the role. If a non-native element has a role, confirm that the required keyboard behaviour and state attributes for that role exist. If a native element is used, record it as correct.
5. Toggle each stateful control (open a menu, check a box, select a tab, submit an invalid field) and confirm the state attribute changes in the inspector at the same time as the visual state. Record mismatches.
6. Check labels: for each form field, confirm it has a programmatic label whose text matches or contains the visible label.
7. Check decorative and hidden content: confirm icons and images are hidden or have empty alternatives, and that focusable content is not hidden with `aria-hidden`.
8. Count the controls that pass steps 3 to 7 and divide by the total checked. Record the ratio, the failing element list, and the failure type (name, role, state, label, hidden content).

## Scoring rubric

- **0. Severe failure:** Most controls have no accessible name or the wrong role. Custom controls are built from `div`/`span` with no role, and state is not exposed.
- **1. Poor:** Many controls lack names or states, or several roles contradict their behaviour. Stateful controls do not update their state attributes.
- **2. Weak:** Some controls are unnamed or mis-roled. States are present but sometimes stale. Labels are partly associated.
- **3. Adequate:** All controls have names and roles that meet WCAG 4.1.2 (Level A), with a few minor issues such as a vague name or a missing description on a complex control.
- **4. Good:** All controls pass steps 3 to 7. Names are specific. States update in sync with visuals. No ARIA is used where a native element works.
- **5. Exemplary:** Everything in level 4, plus names and states verified with at least one screen reader (for example NVDA or VoiceOver) on the critical flows, and no automated findings.

## Automated checks (optional)

axe-core (Deque, open source; used in browser extensions and test runners) detects missing accessible names on buttons and links, invalid ARIA attributes and roles, and required ARIA attributes missing from a role. It cannot judge whether a name is meaningful, whether a role matches behaviour, or whether a state is updated at the right time. Those steps remain manual. Semi-automated: browser accessibility inspectors show computed names and roles for step 3.

## Common failure patterns

- Icon-only buttons with no name, or with a name such as "icon" or the file name of an SVG.
- Clickable `div` or `span` elements with no role, so they are not announced or reachable (WCAG 4.1.2, failure F59).
- `role="button"` added to a non-focusable element, announced as a button but not operable.
- Toggles and disclosure widgets whose `aria-expanded` or `aria-pressed` is never updated after the first render.
- Visible label text that differs from the accessible name, so speech-input users cannot say what they see (WCAG 2.5.3 Label in Name; not verified in this review).
- Redundant or conflicting ARIA on native elements, such as `role="link"` on an `<a>` with a different name than its text.

## Sources

1. W3C, "Understanding Success Criterion 4.1.2: Name, Role, Value," WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/name-role-value
2. W3C, "Names and Descriptions," WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions
3. Bezemer, C.-P., Mesbah, A., and van Deursen, A., "Look Ma, No ARIA: Generic Accessible Interfaces for Web Widgets," W4A 2015. https://researchconnect.stonybrook.edu/en/publications/look-ma-no-aria-generic-accessible-interfaces-for-web-widgets/
4. web.dev, "ARIA and HTML." https://web.dev/learn/accessibility/aria-html
5. Deque, "Top 5 Rules of ARIA." https://www.deque.com/?p=23982
6. USA.gov, "Designing for people with disabilities," 2024. https://www.usa.gov/blog/2024/07/designing-for-people-with-disabilities

## Open questions

- No peer-reviewed study was found that directly measures screen reader users' task success with ARIA-marked widgets. The rubric's thresholds rest on WCAG and W3C guidance, not on measured user performance.
- The "no ARIA is better than bad ARIA" finding comes from practitioner sources, and the cited WebAIM figure conflicts across sources: one reports 70% more detectable errors on pages with ARIA, while Deque quotes 41% from WebAIM's 2021 data. The direction of the effect is consistent, but the magnitude is unverified; the WebAIM Million report should be checked directly.
- The Bezemer et al. abstract was seen but not the full text, so the 18-participant detail is taken from the abstract only.
- The rubric's 4 and 5 anchors (specific names, screen reader verification) are judgment calls, not research-derived thresholds.
- This review uses WCAG 2.1 wording. WCAG 2.2 retains 4.1.2 but its Understanding page was not checked.
- The WCAG 2.5.3 Label in Name failure is cited from general knowledge and was not verified in the searches.
