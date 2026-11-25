# Error Prevention

> Measures how well the design stops users from making mistakes through constraints, defaults, and confirmations.

## What it measures

- Inputs that make invalid values hard or impossible to enter, such as disabled impossible dates, bounded numeric fields, or pickers in place of free text.
- Sensible preset values (defaults) on fields and options where a reasonable choice exists.
- Validation that catches problems at entry time, before the user submits.
- Confirmation or reversibility on actions that are destructive, irreversible, or costly.
- Distinct, well-separated controls for consequential actions, so a slip on a nearby control does not trigger them.

## Research basis

- Slips (unintended actions performed on autopilot) are distinct from mistakes (wrong plans), and slips are the category that constraints, validation, and defaults address. Source: Nielsen Norman Group, "Slips" article (see Sources, 1).
- Constraints that rule out invalid input (for example, a return date that cannot precede departure) prevent errors rather than reporting them. Source: Nielsen Norman Group, "Slips" (1).
- Sensible defaults reduce typing and input mistakes, and forgiving or auto-formatted input reduces entry errors. Source: Nielsen Norman Group, "Slips" (1). NN/g cites no empirical study for these claims.
- Confirmation dialogs belong before consequential or non-reversible actions only. Overuse weakens them, and a confirmation must restate the request and state its effect. Source: Nielsen Norman Group, "Confirmation Dialog" (2).
- Vague prompts such as "Are you sure?" invite reflexive agreement. Buttons that name the outcome (for example "Delete file" and "Keep file") are more specific. Source: Nielsen Norman Group, "Confirmation Dialog" (2).
- WCAG 2.1 Success Criterion 3.3.4 (Level AA) requires at least one of reversible, checked, or confirmed for pages that create legal or financial commitments, modify or delete user-controllable data, or collect test responses. It explicitly does not require confirmation for every routine save. Source: W3C, "Understanding SC 3.3.4" (3).

## Scoring method

1. Identify every input, control, and destructive or consequential action on the screen. List any that are free text where a constraint or picker is possible.
2. For each input with a bounded or structured value (dates, quantities, codes, phone numbers, enumerations), note whether the UI restricts entry, offers a picker or stepper, or only checks after submit. Record the count of each.
3. For each field with a reasonable common value, note whether a default or suggestion is preset. Record the count of fields where a default would help but none is set.
4. Trigger or inspect each destructive or irreversible action. For each, record whether it is reversible (undo offered), confirmed (dialog or review step), or unprotected.
5. For each confirmation dialog present, check that it restates the action and its effect, that buttons name the outcome, and that no button is pre-selected for the dangerous path.
6. Check that consequential controls are spaced and visually separated from frequent ones.
7. Count confirmations on routine actions. Record any that interrupt low-risk work.
8. Record all observations as a tally per step, then score using the rubric.

## Scoring rubric

Scale: 0 = severe failure, 5 = exemplary.

- **0:** Free-text entry for constrained values with no validation. Destructive actions execute immediately with no undo or confirmation. Dangerous buttons sit adjacent to routine ones with identical styling.
- **1:** Most constraints are absent. Validation occurs only after submit. At most one destructive action is protected, and that protection is a generic "Are you sure?" with a default "Yes".
- **2:** Some constraints and defaults exist, but common invalid entries remain possible. Some destructive actions are protected, but others are not, or confirmations are generic.
- **3:** Constraints and pickers cover the main structured inputs. Validation runs inline. Most destructive actions offer undo or an outcome-specific confirmation. A few routine actions are still over-confirmed or a few destructive ones are unprotected.
- **4:** Structured inputs are constrained throughout. Sensible defaults are set where a common value exists. Destructive actions offer undo where feasible, otherwise outcome-named confirmations. Confirmations are reserved for consequential actions. Minor gaps remain.
- **5:** Every structured input is constrained or defaulted where reasonable. Validation is inline and specific. Irreversible actions are confirmed with an outcome-named, restating dialog or a review step. Reversible actions use undo instead of confirmation. Consequential controls are separated from routine ones. No routine action is interrupted.

## Automated checks (optional)

None reliable; manual review only. Automated tools can flag missing form validation attributes or missing labels, but they cannot judge whether a constraint is appropriate, whether a default is sensible, or whether a confirmation is proportionate.

## Common failure patterns

- Free-text date, phone, or quantity fields that accept impossible values and report the error only after submit, against the constraint principle in NN/g (1).
- Generic "Are you sure?" dialogs with a pre-selected "Yes", which users click through without reading, per NN/g (2).
- Confirmation on every save or routine change, which trains users to dismiss prompts. NN/g (2) warns against this, and WCAG 3.3.4 (3) explicitly does not require it.
- Destructive and routine controls with matching styling and placement, so slips land on the destructive one.
- Irreversible actions with neither undo nor confirmation, on pages where WCAG 3.3.4 (3) would require one of reversible, checked, or confirmed.

## Sources

1. Nielsen Norman Group. "Slips." https://www.nngroup.com/articles/slips/
2. Nielsen Norman Group. "Confirmation Dialog (Confirmation Dialogs)." https://www.nngroup.com/articles/confirmation-dialog/
3. W3C WAI. "Understanding Success Criterion 3.3.4: Error Prevention (Legal, Financial, Data) (Level AA)," WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html
4. Norman, D. A. (2013). *The Design of Everyday Things*, revised and expanded edition. Basic Books. https://jnd.org/the-design-of-everyday-things-revised-and-expanded/ (cited for the slip/mistake distinction and constraint taxonomy; seen only through secondary search summaries, not read directly.)

## Open questions

- The NN/g "Slips" and "Confirmation Dialog" articles are practitioner guidance. Neither cites controlled studies, so the thresholds in the rubric (for example, when a confirmation is warranted) are judgment calls, not research-backed numbers.
- A CHI 2023 paper on undo (Rossmy and Terzimehić, doi 10.1145/3544548.3581433) was surfaced in search, but its findings on confirmation or habituation were not verified, so it is not cited for claims. It should be read before any stronger claim about confirmation effectiveness is added.
- Evidence that confirmations cause habituation is anecdotal in the sources reviewed. A thesis-level claim reported via a secondary source was not verified in primary form.
- WCAG 3.3.4 is cited from the 2.1 Understanding document. Whether 2.2 wording differs was not checked.
- The rubric gives no numeric threshold for what counts as "too many" confirmations or how many constrained inputs are enough. Those counts are a reviewer judgment.
