# Interaction and Feedback

> When a user acts on this screen, can they tell what is operable, see what the system is doing, avoid mistakes, and recover or back out when something goes wrong?

## Covered metrics

- `error-prevention`: Error Prevention
- `error-recovery`: Error Recovery
- `affordances`: Affordances
- `feedback-system-status`: Feedback and System Status
- `form-design`: Form Design
- `user-control-freedom`: User Control and Freedom
- `perceived-performance`: Perceived Performance
- `loading-empty-states`: Loading and Empty States
- `motion`: Motion

## What it measures

- Controls look operable and static content does not; cues match the action; disabled, pressed, and selected states differ from the resting state.
- Every action gets a visible response, waits show progress, and background state (saving, syncing, offline, selection, filters, mode) is visible on the screen itself.
- Forms: one column in logical order, a persistent visible label per input, a stated required or optional convention, grouped related fields, and input types that fit the data.
- Prevention: constrained inputs and pickers, sensible defaults, inline validation, and destructive controls separated from routine ones and protected by undo or an outcome-named confirmation.
- Recovery: errors placed at the field at fault, in plain text that names the problem and the fix, with input preserved.
- Exits: a visible Cancel, Close, or Back in every flow and overlay, undo for reversible actions, and Back that keeps entered data.
- Waiting: loading states with structure, no blank or frozen regions, and an interface that stays usable.
- Empty and no-results states that explain the cause and offer a next step, and are never shown while loading.
- Motion that has a purpose, is brief, can be paused, and is not the only carrier of information.

## Scoring method

Work from the screenshot. Timing, hover, Escape, undo, error triggering, live regions, and reduced-motion behavior cannot be observed in one image. Judge the state the screenshot shows and the visible provisions for other states, and say in the rationale which checks were not observable.

1. List every control. For each, note its visual class and whether it carries a cue (shape, border, underline, chevron, handle). Count interactive-looking static content (false affordances), cue-less controls, and cue-to-action mismatches.
2. Note which states are visible: selected, disabled, active filters or mode, saving or sync status, progress.
3. If a form is present, count columns per row, check each input for a persistent label that is not placeholder-only, find the required or optional convention, check grouping, and check that each control type suits its data.
4. List inputs with bounded or structured values. Note whether each is constrained, has a picker, or is free text, and whether a default is set where a common value exists.
5. List destructive or committing actions. Check their separation and styling against routine actions, and look for undo, a review step, or a confirmation. For any dialog shown, check that it restates the action and that buttons name the outcome.
6. For any error shown, record its position relative to the field, whether it names the problem and a fix, any blame or raw codes, and whether entered values are still present.
7. For each flow, modal, or drawer shown, look for a visible labeled exit and a way back.
8. For any loading, empty, or no-results region, record the indicator type, whether the message explains the cause, and whether a working next step is offered. A blank region or a "No records" message during loading is a defect.
9. Note any evidence of motion (carousels, autoplay, large decorative effects) and whether a pause control is visible.
10. Place each member on the rubric, combine them into one score, letting the failures most visible to a user pull the score down the most, and write todos for the lowest members first.

## Scoring rubric

Thresholds come from the member files (NN/g response-time limits; WCAG 3.3.1, 3.3.2, 3.3.3, 3.3.4, 4.1.3, 2.2.2, 2.3.3; member judgment anchors).

- **0**: Most controls are indistinguishable from static content. Actions give no visible response, and nothing appears for more than 1 s or the screen freezes or blanks. Most inputs have no visible label. Constrained values are free text with no validation. Destructive actions run immediately with no undo or confirmation and sit beside routine ones in identical styling. Errors are silent or misleading and input is lost. Users are trapped in a flow or modal. Regions are blank while loading, or show "no data" while loading. Large looping motion has no purpose.
- **25**: Controls are identifiable only after trial. Feedback arrives after 1 s, and waits over 10 s show no indicator. Labels are placeholder-only; validation runs only after submit. The only protection is a generic "Are you sure?" with a default "Yes". Errors are generic ("Invalid input") or far from the field. Most flows lack a visible exit or undo. Empty states say "Empty" with no cause or action. Several animations exceed 1 s.
- **50**: Primary actions and navigation are cued, but secondary controls rely on guessing. Most actions respond, but feedback over 1 s lacks an indicator or outcomes are shown inconsistently. Labels are visible for most fields, with a multi-column row of unrelated fields or generic input types. Some constraints, defaults, and protections exist, but common invalid entries remain possible. Errors sit near the field and are understandable, but most lack a correction path. Some exits exist; Back loses data in one flow. Indicators are the wrong type for the wait, or the empty state gives a cause but no next step. Several animations run over 500 ms.
- **75**: Every control has a consistent cue and at most one minor false affordance. Actions respond within 100 ms, waits over 1 s show progress, and waits over 10 s show determinate progress or time. Results arrive in under 3 s with a structured loading state. Single-column form with persistent labels, an explicit required convention, correct `type` and `autocomplete`, and grouped controls. Structured inputs are constrained and defaulted; confirmations are outcome-named and reserved for consequential actions. Every error is tied to its field, names problem and fix, and preserves input. Every flow has a visible exit; overlays close by control and Escape. Empty states explain the cause and offer a working next step. Feedback animation runs about 100 to 200 ms and transitions 200 to 500 ms.
- **100**: All of the above with no exceptions. No static content invites a click. Long operations show time estimates, and messages persist at least 5 s. Reversible actions use undo instead of confirmation, and no routine action is interrupted. Results are usable within 1 s or partial content appears early. Empty states say what the content will be and how to populate it. Every animation has a purpose within 100 to 500 ms, auto-starting motion over 5 seconds has a pause control, and reduced-motion gives an equivalent end state.

## Member sub-criteria

- `error-prevention`: Detail: metrics/error-prevention.md
- `error-recovery`: Detail: metrics/error-recovery.md
- `affordances`: Detail: metrics/affordances.md
- `feedback-system-status`: Detail: metrics/feedback-system-status.md
- `form-design`: Detail: metrics/form-design.md
- `user-control-freedom`: Detail: metrics/user-control-freedom.md
- `perceived-performance`: Detail: metrics/perceived-performance.md
- `loading-empty-states`: Detail: metrics/loading-empty-states.md
- `motion`: Detail: metrics/motion.md

## Common failure patterns

- Flat text-only buttons that look like labels; cards and stat tiles styled like buttons; icon-only controls with no cue.
- Silent buttons, so users click again; hidden saving, offline, or sync state; toasts that vanish before they can be read.
- Indeterminate spinners on long jobs; full-screen blocking overlays; layout shift as content loads.
- Placeholder as the only label; unrelated fields side by side; required fields unmarked; generic text inputs for dates, phone numbers, or card data.
- Free-text fields that accept impossible values and report the error only after submit.
- Generic "Are you sure?" with a pre-selected "Yes"; confirmation on every routine save.
- Destructive and routine controls with matching style and placement; deletes with neither undo nor confirmation.
- Generic or summary-only errors far from the field; fields cleared after a failed submit.
- Modals with no visible close control; wizards where Back clears data.
- Blank containers during fetch; "No results" shown before the request completes; empty states with no action.
- Decorative motion on every element; transitions well beyond 500 ms; auto-playing motion with no pause control.

## Sources

- Norman (1999), Affordance, Conventions, and Design. https://cs.uwaterloo.ca/~jianzhao/cs449-649/files/affordance-norman99.pdf
- Norman (2013), The Design of Everyday Things, revised edition. https://jnd.org/the-design-of-everyday-things-revised-and-expanded/
- Nielsen Norman Group, Clickable Elements. https://www.nngroup.com/articles/clickable-elements/
- Tiab and Hornbæk (2016), CHI. https://www.kasperhornbaek.dk/papers/CHI2016-Affordances.pdf
- Dissertation (2023), University of Lille. https://pepite-depot.univ-lille.fr/LIBRE/EDMADIS/2023/2023ULILB045.pdf
- J-STAGE (2014), vol. 61 no. 3. https://www.jstage.jst.go.jp/article/jssdj/61/3/61_3_1/_article/-char/ja
- Nielsen Norman Group, Visibility of System Status. https://www.nngroup.com/articles/visibility-system-status/
- Nielsen Norman Group, Response Times: The 3 Important Limits. https://www.nngroup.com/alertbox/response-times.html
- Harrison, Yeo, and Hudson (2010), Faster Progress Bars, CHI. https://www.chrisharrison.net/index.php/Research/ProgressBars2
- Tan and Nov, Counting the Wait, CHI 2026. https://arxiv.org/abs/2602.04138
- W3C, Understanding SC 4.1.3 Status Messages. https://www.w3.org/WAI/WCAG21/Understanding/status-messages
- Speero (2016), single or multi-column forms. https://speero.com/post/form-field-usability-should-you-use-single-or-multi-column-forms-original-research
- Baymard Institute, Avoid Multi-Column Forms. https://baymard.com/research-articles/avoid-multi-column-forms
- Penzo (2006), Label placement in forms, UXMatters. https://www.uxmatters.com/mt/archives/2006/07/label-placement-in-forms.php
- Das and McEwan, label alignment eye-tracking study. https://napier-repository.worktribe.com/OutputFile/232503
- Nielsen Norman Group, Marking Required Fields in Online Forms. https://www.nngroup.com/articles/required-fields
- Nielsen Norman Group, Placeholders in Form Fields. https://www.nngroup.com/articles/form-design-placeholders/
- W3C, Understanding SC 3.3.2 Labels or Instructions. https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions
- W3C, Understanding SC 1.3.5 Identify Input Purpose. https://www.w3.org/WAI/WCAG21/Understanding/identify-input-purpose
- Nielsen Norman Group, Slips. https://www.nngroup.com/articles/slips/
- Nielsen Norman Group, Confirmation Dialog. https://www.nngroup.com/articles/confirmation-dialog/
- W3C, Understanding SC 3.3.4 Error Prevention (Legal, Financial, Data). https://www.w3.org/WAI/WCAG21/Understanding/error-prevention-legal-financial-data.html
- W3C, Understanding SC 3.3.1 Error Identification. https://www.w3.org/WAI/WCAG22/Understanding/error-identification
- W3C, Understanding SC 3.3.3 Error Suggestion. https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion
- Seckler, Tuch, Opwis, and Bargas-Avila (2012), Interacting with Computers. DOI 10.1016/j.intcom.2012.03.002
- Seckler et al. (2014), Designing Usable Web Forms, CHI. https://research.google.com/pubs/archive/42513.pdf
- Nielsen Norman Group, Error-Message Guidelines. https://www.nngroup.com/articles/error-message-guidelines/
- Nielsen Norman Group, User Control and Freedom. https://www.nngroup.com/articles/user-control-and-freedom/
- Nielsen Norman Group, Ten Usability Heuristics. https://www.nngroup.com/articles/ten-usability-heuristics/
- Akers, Simpson, Jeffries, and Winograd (2009), CHI. https://hci.stanford.edu/publications/paper.php?id=67
- Just Undo It, arXiv:2403.11756. https://arxiv.org/pdf/2403.11756
- W3C, Understanding SC 2.5.2 Pointer Cancellation. https://www.w3.org/WAI/WCAG22/Understanding/pointer-cancellation
- Nielsen, Time Scales of UX. https://www.uxtigers.com/post/time-scales-ux
- Forch, Franke, Rauh, and Krems (2017), latency perception thresholds (venue and URL not verified).
- Franke, Attig, Rauh, and Krems (2017), System Latency Guidelines Then and Now. https://doi.org/10.1007/978-3-319-58475-1_1
- Shneiderman (1984), Response time and display rate. https://www.cs.umd.edu/users/ben/papers/Shneiderman1984Response.pdf
- Doherty and Thadani (1982), secondary source. https://lawsofux.com/doherty-threshold/
- Martin and Corl (1986). https://www.bohrium.com/paper-details/system-response-time-effects-on-user-productivity/811988601763004420-10074
- Kaplan (2021), Designing Empty States in Complex Applications, NN/g. https://nngroup.com/articles/empty-state-interface-design
- Nielsen (2009), Powers of 10: Time Scales in UX. http://www.nngroup.com/articles/powers-of-10-time-scales-in-ux/
- Nielsen, Progress Indicators, UX Tigers. https://www.uxtigers.com/post/progress-indicators
- Viget (2017), A Bone to Pick with Skeleton Screens. https://viget.com/articles/a-bone-to-pick-with-skeleton-screens
- Nielsen Norman Group, Animation Purpose in UX. https://www.nngroup.com/articles/animation-purpose-ux/
- Nielsen Norman Group, Animation Duration. https://nngroup.com/articles/animation-duration
- W3C, Understanding SC 2.3.3 Animation from Interactions. https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions
- W3C, Technique C39. https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html
- web.dev, Animation and motion. https://web.dev/learn/accessibility/motion
- Merz, Tuch, and Opwis (2016), CHI EA '16, pp. 3152-3158 (citation only).

## Open questions

- The 100 ms, 1 s, and 10 s limits are NN/g guidance with a disputed empirical basis (Forch et al. report a perception mean near 65 ms). The 3 s result boundary and 5 s message persistence are judgment calls.
- Skeleton against spinner evidence is mixed, so the rubric prefers neither.
- NN/g guidance on slips, confirmations, and exits cites no controlled studies. When a confirmation is warranted, and which actions must be undoable, is a reviewer judgment. Light dismiss is not scored.
- Label alignment outside single-column forms is unresolved (Penzo against Das and McEwan), and whether right-side error placement beats adjacent placement in general is not settled.
- Motion duration bands rest on NN/g summaries. WCAG 2.3.3 is Level AAA, so reduced-motion support is an expectation, not a conformance requirement.
- Only one controlled study tests perceived affordances directly. All rubric bands are judgment calls.
