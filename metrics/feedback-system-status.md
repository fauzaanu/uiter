# Feedback and System Status

> Scores whether the interface confirms each user action promptly and reports the current system state (progress, saving, loading, success, failure) so the user is never left guessing.

## What it measures

- Every control that triggers an action (button, toggle, submit, drag drop) shows a visible response: state change, pressed style, spinner, or inline result.
- Responses that take longer than about 1 second show a progress indicator, and long operations show an estimate or elapsed/remaining time where feasible.
- Background state is visible: saving, syncing, offline, unread counts, selected items, and current filters or mode are displayed without requiring the user to open a menu.
- Completion is announced: success confirmations, toasts, or changed content appear and persist long enough to read.
- Status changes that do not move focus are exposed to assistive technology through live regions or equivalent status messages.

## Research basis

- Feedback should be given as quickly as possible, ideally immediately, and can be as light as a color change on a clicked button; progress indicators cover longer waits. Nielsen Norman Group, "Visibility of System Status" (Nielsen's Usability Heuristic 1). https://www.nngroup.com/articles/visibility-system-status/
- Response-time limits: 0.1 s feels instantaneous, 1 s keeps the user's flow of thought, and about 10 s is the attention limit for unindicated waits. Nielsen Norman Group, "Response Times: The 3 Important Limits." https://www.nngroup.com/alertbox/response-times.html (figures cited via secondary summaries of this page; verify exact wording at source).
- In a mobile eye-tracking study, users tapped a button and remained unsure whether anything was loading because no feedback appeared, and some tapped repeatedly. Nielsen Norman Group (same heuristic article, Section on feedback).
- Progress indicators shape perceived duration. Harrison, Yeo and Hudson, "Faster Progress Bars: Manipulating Perceived Duration with Visual Augmentations," CHI 2010. https://www.chrisharrison.net/index.php/Research/ProgressBars2
- In an online experiment (N = 425) on 10, 30 and 60 second waits, no time display made waits feel longer and more ambiguous, and remaining-time displays increased frustration relative to elapsed-time displays. Tan and Nov, "Counting the Wait," CHI 2026 (arXiv:2602.04138). https://arxiv.org/abs/2602.04138 (taken from search abstract only; full text not reviewed).
- Status messages (confirmations, errors, real-time updates) must be programmatically exposed without focus change. W3C, "Understanding SC 4.1.3: Status Messages (Level AA)." https://www.w3.org/WAI/WCAG21/Understanding/status-messages

## Scoring method

1. List the screen's actions: every control that changes data, navigates, or starts a process. Note the ones that are slow or asynchronous.
2. For each action, trigger it once and observe the first 100 ms and the first 1 s. Record whether a visible change occurs (state change, pressed style, spinner, or content update). Use a stopwatch or screen recording frame count.
3. For any action that takes longer than 1 s, check for a progress indicator. Determinate progress (bar, percentage, count) scores higher than indeterminate spinners. Note whether the indicator stays accurate.
4. Check persistent system state: saving, syncing, offline, selection, active filters, and mode. Confirm each is visible on the screen itself.
5. Trigger a success and a failure (or inspect the code path). Confirm a message appears near the source, states the outcome, and remains until dismissed or for at least 5 s.
6. Inspect markup or use an accessibility tree viewer: confirm that dynamically inserted status text sits in a live region (role="status" or aria-live="polite"; role="alert" for errors) and is not only a visual toast.
7. Record each action as: response time (ms), feedback type, persistence, and screen-reader exposure. Score using the rubric.

## Scoring rubric

- 0: Actions give no visible response, status is hidden, and failures are silent. Users cannot tell whether the system is working.
- 1: Responses exist for a few actions only. Waits over 10 s show no indicator, or feedback is delayed past 1 s with no sign of progress.
- 2: Most actions respond, but feedback is delayed beyond 1 s without indicators, or success and failure are inconsistently shown. Background status is absent for at least one important state.
- 3: Most actions respond within 100 ms. Waits over 1 s show a spinner or progress. Outcomes are shown, but some are transient or not announced to assistive technology.
- 4: All actions respond within 100 ms. Waits over 1 s show progress, and waits over 10 s show determinate progress or time information. Success, failure and background state are visible and persist long enough to read, with live-region exposure for most messages.
- 5: As 4, plus determinate progress and time estimates for long operations, consistent feedback patterns across the product, and verified screen-reader announcements for all status changes.

## Automated checks (optional)

None reliable for response time or progress quality; manual review only. axe-core can check that status containers use live regions (for example, rules tied to WCAG 4.1.3) but cannot judge whether feedback is timely or informative.

## Common failure patterns

- Silent buttons: a click changes nothing visible for more than 100 ms, so users tap again (NN/g eye-tracking observation).
- Indeterminate spinners for long jobs: waits past 10 s give no sense of progress or remaining time, which the Tan and Nov experiment associates with heightened ambiguity.
- Transient-only toasts: success or error messages vanish before reading and are never announced to screen readers (WCAG 4.1.3).
- Hidden system state: saving, offline, or sync status exists only inside a settings menu.
- Optimistic UI without rollback messaging: the interface shows success and later reverts silently when the server fails.

## Sources

1. Nielsen Norman Group, "Visibility of System Status," nngroup.com/articles/visibility-system-status/
2. Nielsen Norman Group, "Response Times: The 3 Important Limits," nngroup.com/alertbox/response-times.html
3. Harrison, C., Yeo, Z., and Hudson, S. E., "Faster Progress Bars: Manipulating Perceived Duration with Visual Augmentations," CHI 2010. chrisharrison.net/index.php/Research/ProgressBars2
4. Tan, and Nov, "Counting the Wait," CHI 2026; arXiv:2602.04138. arxiv.org/abs/2602.04138
5. W3C, "Understanding SC 4.1.3: Status Messages (Level AA)," WCAG 2.1. w3.org/WAI/WCAG21/Understanding/status-messages

## Open questions

- The 1 s and 10 s thresholds are widely cited from Miller (1968) and Nielsen (1993). The primary Miller paper was not retrieved; treat the figures as NN/g guidance.
- The Tan and Nov CHI 2026 study was taken from a search abstract. Author names, sample, and findings should be checked against the full paper before citing beyond this file.
- The "100 ms" and "5 s persistence" anchors are judgment calls for this rubric, not figures from the sources.
- The eye-tracking observation is from an NN/g article; sample size was not verified.
- Whether a toast is announced depends on implementation; the rubric scores observed behavior, not intent.
