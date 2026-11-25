# Form Design

> Scores how well a form's structure, labels, grouping, and input types let a user complete it quickly and with few errors.

## What it measures

- **Column structure:** whether fields run in one vertical column in logical order, or split across multiple columns that force side-to-side and up-down scanning.
- **Label presence and placement:** whether every input has a visible, persistent text label placed above (or otherwise consistently adjacent to) the field, not only a placeholder.
- **Required and optional marking:** whether the form states which fields are required, and whether that marking is consistent and understandable.
- **Grouping:** whether related fields (for example, name parts, address blocks, a radio set) are visually grouped and programmatically grouped.
- **Input type fit:** whether the control matches the data (date picker or segmented input for dates, numeric keyboard for numbers, select for fixed choices) and whether autocomplete is offered for personal data.

## Research basis

- Single-column layouts are faster and produce fewer errors than multi-column layouts for short, linear forms. A 2016 CXL/Speero split test (702 desktop participants) reported roughly 102 s for single-column versus 118 s for multi-column completion. Baymard's usability testing reports fewer skipped, misread, and erroneous fields in single-column layouts. Source: Speero (2016); Baymard Institute, "Avoid Multi-Column Forms."
- Top-aligned labels produced the fastest completion in an eye-tracking study that tested label placements; a later replication by Das and McEwan favored right-aligned labels in multi-column contexts. The evidence therefore supports top-aligned labels for single-column forms, with the placement question still open for other layouts. Source: Penzo, UXMatters (2006); Das and McEwan (Napier repository, see Open questions).
- Optional fields need marking only when most fields are required, and the marking must not rely on the asterisk alone for a mostly-optional form. NN/g recommends marking required fields, since omitting marks on a registration form is the riskier error; marking optional fields is a helpful extra. Source: Nielsen Norman Group, "Marking Required Fields."
- WCAG 3.3.2 (Level A) requires that labels or instructions be provided for inputs. WCAG 1.3.1 requires that those labels be programmatically associated with their controls, and related radio or checkbox groups be grouped. Source: W3C, Understanding SC 3.3.2.
- WCAG 1.3.5 (Level AA) requires that the purpose of inputs collecting user data be programmatically determinable, normally via the HTML `autocomplete` attribute. Source: W3C, Understanding SC 1.3.5.
- Placeholder text that replaces a label disappears on typing and is not reliably read by screen readers, which harms recall and accessibility. Source: Nielsen Norman Group, "Placeholders in Form Fields."

## Scoring method

1. Open the form on a desktop viewport and on a phone-width viewport. Record the number of fields and the number of steps.
2. Count columns per row. Note any row with more than one input that does not belong to a single entity (such as a date or a first/last name pair). Record each as a column-structure issue.
3. For every input, confirm a visible text label is present after the user clicks in the field, not only before. Check the DOM: the label must be a `<label>` or an equivalent accessible name. Record any input whose only label is a placeholder.
4. Identify the required/optional convention. Count required and optional fields. Record whether the form states the convention in a legend or on each field.
5. Check grouping. Confirm that related radios, checkboxes, and multi-part fields sit inside a `fieldset` with a `legend`, or are visually grouped with a shared heading.
6. For each input collecting personal data, check the `type` and `autocomplete` attributes against the field's purpose. Check the control type against the data (date, number, email, choice list).
7. Record each finding with a screen reference, field name, and the step number. Compute the score from the rubric using the most severe unresolved issue as the anchor, then adjust by the count of issues.

## Scoring rubric

- **0:** Form has no visible labels for most inputs, mixes unrelated fields in multi-column rows, and gives no indication of required fields.
- **1:** Labels are present but several are placeholder-only or hidden; multi-column layout is used for a long form; required status is unclear.
- **2:** Labels are visible for most fields, but there is at least one multi-column row with unrelated fields, grouping is missing for a radio or checkbox set, or input types are generic throughout (text for dates or phone numbers).
- **3:** Single column with visible labels above fields and a clear required convention. Minor gaps: one or two fields lack `autocomplete` or an appropriate `type`, or a related group is not wrapped in `fieldset`.
- **4:** Single column, visible persistent labels, explicit required/optional convention, correct `type` and `autocomplete` on personal fields, and grouped related controls. At most one minor inconsistency.
- **5:** All of level 4, plus fields are in a logical order that matches the data flow, inputs suit the data type (date pickers or segmented inputs, numeric keyboards), and the form is split into steps only where the length warrants it.

Numeric thresholds are not used in this rubric because the reviewed research gives no reliable number for field count or step count. Those are judgment calls.

## Automated checks (optional)

Partially reliable. axe-core flags inputs with no accessible name, missing `fieldset` for radio groups in some cases, and invalid `autocomplete` values. It cannot judge whether a label is visible after input, whether a column split is logically wrong, whether an input type suits its data, or whether the required convention is understandable. Manual review is required for scores above 2.

## Common failure patterns

- Placeholder used as the only label, so the field's purpose disappears once the user starts typing (NN/g, placeholder article).
- Multi-column rows that place unrelated fields side by side, causing skipped or misread fields (Baymard, multi-column article).
- Required fields unmarked or marked only by an asterisk with no legend, especially on registration forms (NN/g, required fields).
- Generic text inputs for dates, phone numbers, or card data, with no `autocomplete`, forcing manual entry of personal data (WCAG 1.3.5).
- Radio and checkbox sets presented without a group label, so the question context is lost for assistive technology (WCAG 1.3.1 and H71 grouping guidance).

## Sources

1. Speero (formerly CXL), "Form field usability: should you use single or multi-column forms?" (2016). https://speero.com/post/form-field-usability-should-you-use-single-or-multi-column-forms-original-research
2. Baymard Institute, "Avoid Multi-Column Forms." https://baymard.com/research-articles/avoid-multi-column-forms
3. M. Penzo, "Label placement in forms," UXMatters (2006). https://www.uxmatters.com/mt/archives/2006/07/label-placement-in-forms.php
4. Das and McEwan, eye-tracking study on label alignment in online forms, Napier University repository. https://napier-repository.worktribe.com/OutputFile/232503
5. Nielsen Norman Group, "Marking Required Fields in Online Forms." https://www.nngroup.com/articles/required-fields
6. Nielsen Norman Group, "Placeholders in Form Fields." https://www.nngroup.com/articles/form-design-placeholders/
7. W3C WAI, "Understanding SC 3.3.2: Labels or Instructions." https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions
8. W3C WAI, "Understanding SC 1.3.5: Identify Input Purpose." https://www.w3.org/WAI/WCAG21/Understanding/identify-input-purpose

## Open questions

- The Speero figures (702 participants, 102 s versus 118 s) come from search summaries, not the full article. Verify against the original before quoting numbers.
- The Das and McEwan author names and findings come from a secondary summary. The paper itself was not opened.
- Penzo's 2006 eye-tracking result conflicts with the later Das and McEwan replication on right-aligned labels. Treat label alignment outside single-column forms as unresolved.
- HubSpot reported a 22% conversion lift for a two-column 13-field form. This conflicts with the single-column findings on conversion, though it measures conversion, not completion time or error rate. The rubric scores structure, not conversion, so this is not weighed.
- The NN/g required-fields guidance was read through search summaries; the full article was not fetched. The "mostly required" advice (marking optional fields) is from a secondary summary of a 2025 Nielsen piece.
- The 2 to 5 rubric anchors on step count and field count are judgment calls rather than research-backed thresholds.
