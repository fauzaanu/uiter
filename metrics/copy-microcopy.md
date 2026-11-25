# Copy and Microcopy

> Measures whether labels, hints, buttons, and messages are clear, concise, and action-oriented.

## What it measures

- Field labels state what to enter in plain words, and stay visible when the field has a value.
- Hint and format text sits beside the field (not as the only label) and gives a concrete example when a format is required.
- Button labels name the action with a verb and the object it affects (for example "Delete workspace," not "OK" or "Yes/No").
- Error and status messages say what happened, what to do next, and avoid blaming the user or showing raw codes.
- Empty states and helper text point to the next step instead of only describing the absence of data.

## Research basis

- Error messages should be human-readable, concise and precise, offer a remedy, and not blame the user; merely stating the problem is not enough. Neusesser and Sunwall, "Error-Message Guidelines," Nielsen Norman Group. https://www.nngroup.com/articles/error-message-guidelines/
- Permanent visible labels are preferred over inline placeholder text, which disappears on input and caused deletion and re-entry problems in a Baymard mobile study. Placeholder text is best reserved for brief format examples. Baymard Institute, "Mobile Forms: Avoid Inline Labels." https://baymard.com/blog/mobile-forms-avoid-inline-labels
- Labels and instructions should tell users what information to enter, with expected formats and examples where needed. W3C, "Understanding SC 3.3.2: Labels or Instructions" (WCAG 2.1, Level A). https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions
- Where an error is detected and a known correction exists, the user should be given a suggestion for fixing it (with a security or purpose exception). W3C, "Understanding SC 3.3.3: Error Suggestion" (WCAG 2.1, Level AA). https://w3.org/WAI/WCAG21/Understanding/error-suggestion
- Accessibility: errors must not rely on color alone. Nielsen Norman Group, same article as above.

## Scoring method

1. Take a screenshot or open the screen's live state, including at least one error state and one empty state where present.
2. List every label, hint, button, error, and status string on the screen. Record exact text.
3. For each button, check the first word: is it a verb that names the object (pass), a generic word such as "OK", "Submit", "Yes/No" (fail)?
4. For each field, check that a visible label persists after entry and that any example format is shown outside the placeholder (pass) or only in the placeholder (fail).
5. For each error or warning, check three things: it names the problem, it gives a next step, and it avoids blame or raw codes. Mark each as yes or no.
6. Count the words in each string. Flag strings over roughly 12 words for a judgment-based review of concision.
7. Check that the same action uses the same word across the screen (for example, "Delete" in one place, "Remove" in another is a fail).
8. Record the count of passes and fails per check, with the exact string as evidence, then map to the rubric.

## Scoring rubric

- **0**: Severe failure. Labels or buttons are absent, generic, or misleading. Errors are unexplained, blame the user, or show only codes. Users cannot tell what will happen.
- **1**: Most strings are unclear or generic. Errors name a problem but offer no next step. Placeholder is the only label.
- **2**: Mixed. Some buttons are verb-led, but several are generic or inconsistent. Errors are sometimes actionable. Formats are missing where needed.
- **3**: Mostly clear. Visible labels, verb-led buttons, and actionable errors on most strings. A few vague or long strings remain.
- **4**: Clear and consistent. Every button names its action and object, labels persist, errors state problem and fix, and terminology is consistent across the screen.
- **5**: Exemplary. Strings are concise, specific, and direct. Empty states and help text lead to the next step, and the copy shows no jargon, blame, or ambiguity under any state checked.

## Automated checks (optional)

None reliable; manual review only. Spell-check and word-count scripts can flag length and obvious terms, but cannot judge whether a label is action-oriented or whether an error gives a usable fix.

## Common failure patterns

- Generic buttons ("OK", "Submit", "Yes/No") that leave the user unsure of the outcome. Action-verb labels are recommended in practitioner guidance; no controlled study was found.
- Placeholder used as the only label, so the label vanishes on input and users delete entries to see it (Baymard).
- Errors that state the failure without a remedy, the guideline NN/g names as insufficient.
- Errors that blame the user ("You entered an invalid value") or show raw codes (NN/g).
- Required format given only as text outside the field, which users often ignore (Baymard observation at a single retailer).
- Inconsistent terms for one action across a screen, which weakens users' mental model.

## Sources

1. Neusesser, T. and Sunwall, E., "Error-Message Guidelines," Nielsen Norman Group. https://www.nngroup.com/articles/error-message-guidelines/
2. Baymard Institute, "Mobile Forms: Avoid Inline Labels." https://baymard.com/blog/mobile-forms-avoid-inline-labels
3. W3C WAI, "Understanding SC 3.3.2: Labels or Instructions," WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions
4. W3C WAI, "Understanding SC 3.3.3: Error Suggestion," WCAG 2.1. https://w3.org/WAI/WCAG21/Understanding/error-suggestion

## Open questions

- No peer-reviewed controlled study on button-label comprehension or call-to-action wording was found in search. The verb-led button rule rests on practitioner guidance (Userpilot, uxpsychology) and should be treated as a judgment call.
- The Baymard source is a 2013 mobile study; the newer Baymard label-placement guideline page did not return content, so its current findings are unverified.
- Year and venue for the NN/g article were not shown in search results; the author names come from the page as surfaced.
- The 12-word concision threshold and the 0 to 5 anchors are judgment calls, not research-backed thresholds.
- WCAG 2.2 text was not retrieved directly; the cited criteria are from the WCAG 2.1 Understanding documents. Search results pointed to a WCAG 2.2 Understanding page for the latest wording, which was not checked and should be verified.
