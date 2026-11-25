# Error Recovery

> Measures how clearly errors are explained and how easily users can correct them and continue.

## What it measures

- Each error is tied to the field or element at fault, with the message placed next to it rather than only at the top of the form or in a transient toast.
- The error text states what went wrong in plain language, without blaming the user.
- The message gives a correction path where one is known, such as an example format or the list of accepted values.
- User input is preserved after the error, so the user does not retype valid fields.
- The user can locate, fix and resubmit without losing context, and the error state clears once the input is corrected.

## Research basis

- Errors should be identified in text tied to the field at fault. This is the W3C requirement for WCAG 3.3.1 Error Identification (Level A); color or icons may supplement the text but cannot replace it. Source: W3C, "Understanding SC 3.3.1: Error Identification," https://www.w3.org/WAI/WCAG22/Understanding/error-identification
- Where the fix is known, the message should suggest it. WCAG 3.3.3 Error Suggestion (Level AA) asks for correction suggestions unless they would jeopardize security or purpose. The W3C notes that default HTML validation messages are often too generic to meet this. Source: W3C, "Understanding SC 3.3.3: Error Suggestion," https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion
- Placement affects how quickly users find and fix errors. In a controlled study, Seckler and colleagues compared error-message locations and found that placing the message to the right of the erroneous field supported faster scanning than placing it at the top or bottom of the form. Source: Seckler, Tuch, Opwis, and Bargas-Avila (2012), "User-friendly locations of error messages in web forms: Put them on the right side of the erroneous input field," *Interacting with Computers*, DOI 10.1016/j.intcom.2012.03.002.
- Optimized forms, including clearer error handling, reduced completion time, submission trials and eye fixations, and raised satisfaction. Error-message placement was among the guidelines that interview participants singled out. Source: Seckler, Heinz, Bargas-Avila, Opwis, and Tuch (2014), "Designing Usable Web Forms: Empirical Evaluation of Web Form Improvement Guidelines," CHI 2014, https://research.google.com/pubs/archive/42513.pdf
- Errors should be shown after the mistake is made, not while the user is still typing, and the message should stay visible while the user corrects it. Source: Nielsen Norman Group, "Error-Message Guidelines," https://www.nngroup.com/articles/error-message-guidelines/

## Scoring method

1. Open the screen in its error state. Trigger errors with realistic invalid input for each required or constrained field, plus one form-level failure if the screen has a submit action.
2. For each error, note the location of the message relative to the field. Record whether it sits adjacent to the field, is linked to it programmatically (for example via `aria-describedby` or `aria-errormessage`), or appears only elsewhere.
3. Read the message text aloud. Record whether it names the problem and whether it contains blame language or jargon.
4. Check whether a correction path is given: an example format, an accepted-values list, or a specific instruction. Mark it as known and absent, or as unknown if the rule is not discoverable from the screen.
5. Enter a correction and resubmit. Confirm that the error clears, that previously valid fields kept their values, and that focus or scroll moves to the first error.
6. Repeat once with a screen reader or accessibility tree inspection to confirm the error is announced and associated with its field.
7. Record one line per error: location, text quality, suggestion presence, preservation of input, recovery path. Score the screen against the rubric using the worst recurring pattern as the main driver.

## Scoring rubric

- **0 (severe failure):** Errors are silent, misleading or absent. The user cannot tell what is wrong, and input is lost on error.
- **1 (poor):** Errors exist but are generic (for example "Invalid input") or placed far from the field, with no correction path. Recovery requires guessing.
- **2 (weak):** Errors are located near or linked to the field and are understandable, but the correction path is missing for most cases, or input is lost in some cases.
- **3 (adequate):** Each error is tied to its field and states the problem clearly. A correction path is given for most cases. Valid input is preserved. Minor gaps remain, such as blame-adjacent wording or one unannounced error.
- **4 (good):** Every error is tied to its field, announced to assistive technology, and clear about the problem and fix. Input is preserved, focus moves to the first error, and the error clears on correction.
- **5 (exemplary):** Meets all criteria of 4, and the interface prevents errors where possible (for example format hints before input, or confirmation before destructive actions). The user can recover from any error without outside help.

## Automated checks (optional)

Partial only. axe-core flags missing error association and some ARIA misuse, and can confirm that an error element is linked with `aria-describedby`. It cannot judge whether a message is clear, specific or actionable, or whether input survives a failed submit. Those require manual review.

## Common failure patterns

- Generic messages such as "Invalid input" or default browser validation text, which the W3C notes do not satisfy the suggestion requirement.
- Only a summary error at the top of a long form, away from the erroneous field, which slows location as shown in the placement studies.
- Premature errors that appear before the user has finished typing, as NN/g cautions against.
- Form reset or cleared fields after a failed submit, forcing users to re-enter valid data.
- Error text that disappears when the user begins correcting it, or a modal that hides the field the user must fix.

## Sources

1. W3C, "Understanding SC 3.3.1: Error Identification (Level A)," WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/error-identification
2. W3C, "Understanding SC 3.3.3: Error Suggestion (Level AA)," WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion
3. Seckler, M., Tuch, A., Opwis, K., and Bargas-Avila, J. (2012). "User-friendly locations of error messages in web forms: Put them on the right side of the erroneous input field." *Interacting with Computers*. DOI 10.1016/j.intcom.2012.03.002
4. Seckler, M., Heinz, S., Bargas-Avila, J., Opwis, K., and Tuch, A. N. (2014). "Designing Usable Web Forms: Empirical Evaluation of Web Form Improvement Guidelines." CHI 2014. https://research.google.com/pubs/archive/42513.pdf
5. Nielsen Norman Group, "Error-Message Guidelines." https://www.nngroup.com/articles/error-message-guidelines/

## Open questions

- The Seckler 2014 CHI venue and author list come from search summaries. The full paper was not read, so the exact error-related results are unverified beyond the summary.
- The 2012 placement result is cited from an abstract-level summary, not the full text.
- The NN/g guidelines article was not read in full. Its points are taken from its summaries and related NN/g pages, so authorship and year are unverified.
- The 0 to 5 anchors and the "worst pattern drives the score" rule are judgment calls. The research supports the criteria, not the specific score bands.
- Whether right-side placement beats adjacent placement generally, or only in the tested layouts, is not settled by the sources reviewed.
