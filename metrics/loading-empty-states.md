# Loading and Empty States

> Scores whether loading, empty, and no-results states tell the user what is happening and what to do next, rather than leaving them waiting or stranded.

## What it measures

- Whether every asynchronous area shows a loading indicator, skeleton, or placeholder from the moment a wait begins, and whether that indicator matches the expected wait length.
- Whether a region with no data explains why it is empty (never loaded, filtered out, nothing created yet, or failed) instead of rendering blank.
- Whether empty states offer a next step: a call to action, a link to the creation or import path, or a clear way to clear filters.
- Whether no-results states name the query or filters in effect and offer a way to broaden or reset them.
- Whether loading and empty messages can be distinguished from one another; a "No records" message shown during loading is a defect.

## Research basis

- Empty states that are fully blank create uncertainty and reduce user confidence, because users cannot tell whether the system is loading, has failed, or has nothing to show. Kaplan, "Designing Empty States in Complex Applications: 3 Guidelines," Nielsen Norman Group, 2021. https://nngroup.com/articles/empty-state-interface-design
- Misleading placeholder text, such as "No records" while content is still loading, is described as particularly harmful. Same source.
- Empty states can raise learnability when they explain what a feature does and how to populate it, and in-context cues are presented as more effective than forced tutorials. Same source.
- Response time limits: 0.1 s feels like direct manipulation, 1 s keeps users navigating freely, and after about 10 s attention is maxed out. Nielsen, "Response Time Limits" (Powers of 10 article), Nielsen Norman Group, 2009. http://www.nngroup.com/articles/powers-of-10-time-scales-in-ux/
- Show no indicator for waits under about 1 s; use a spinner for waits of roughly 2 to 10 s; use percent-done feedback for any wait over 10 s. Nielsen, "Progress Indicators," UX Tigers (author-dated August 8, year not shown). https://www.uxtigers.com/post/progress-indicators
- Skeleton screens versus spinners: in a reported 136-person test with identical wait times, skeleton screens rated lowest on the measured perceived-speed items. Viget, "A Bone to Pick with Skeleton Screens," 2017. https://viget.com/articles/a-bone-to-pick-with-skeleton-screens. The evidence on this point is mixed, so the rubric does not prefer one indicator style.

## Scoring method

1. Identify every region on the screen that loads data or can be empty: lists, tables, cards, search results, detail panels.
2. Trigger each state in turn: throttle the network to force a slow load, return an empty dataset, apply a filter or search with zero matches, and simulate a failed request.
3. For each loading state, time how long it appears before any content or indicator shows. Record whether the indicator is a spinner, skeleton, or bar, and whether it fits the wait length (none under about 1 s, spinner for 2 to 10 s, percent-done beyond 10 s).
4. For each empty and no-results state, record: (a) the message text, (b) whether it explains the cause, (c) whether a next-step control is present, and (d) whether the control works.
5. Check that loading and empty messages never conflict: force a slow load and confirm no "No results" text appears before data returns.
6. Score each region against the rubric, then take the lowest region score as the screen score, and note the region that set it.
7. Record each observation with a screenshot, the region name, the state triggered, and the score.

## Scoring rubric

- **0 (severe failure):** Blank region during loading or after an empty result, or a misleading "no data" message shown while content is loading.
- **1:** Loading indicator present but absent or delayed beyond 1 s without any indicator, or empty state shows generic text such as "Empty" with no cause and no action.
- **2:** Indicator present, but the wrong type for the wait length (for example, a spinner with no change on a 15 s wait), or empty state gives a cause but no next step.
- **3:** Indicator appears within about 1 s and fits the wait length; empty state explains the cause; no-results state names the query, but no direct recovery control exists.
- **4:** All of 3, plus a next-step control (create, import, reset filters) that works, and percent-done feedback on waits over 10 s.
- **5 (exemplary):** All of 4 across every state checked, with the empty state explaining what the content will be and how to populate it, and no conflict between loading and empty messages on any screen.

## Automated checks (optional)

None reliable; manual review only. Automated tools can detect that a placeholder element exists, but not whether a wait is the right length or whether text is misleading.

## Common failure patterns

- Blank containers during fetch, which leave users unsure whether the page has frozen (see Kaplan, NN/g 2021).
- "No records" or "No results" text rendered before the request completes, a case the NN/g article describes as particularly harmful.
- A spinner on a wait of 15 s or more with no percent-done feedback (see Nielsen, UX Tigers).
- No-results screens that do not name the active filters, so users cannot tell why nothing matches.
- Empty states that state the absence but offer no action, so users must discover the next step on their own.

## Sources

1. Kate Kaplan, "Designing Empty States in Complex Applications: 3 Guidelines," Nielsen Norman Group, 2021. https://nngroup.com/articles/empty-state-interface-design
2. Jakob Nielsen, "Response Time Limits" (Powers of 10: Time Scales in UX), Nielsen Norman Group, 2009. http://www.nngroup.com/articles/powers-of-10-time-scales-in-ux/
3. Jakob Nielsen, "Progress Indicators," UX Tigers. https://www.uxtigers.com/post/progress-indicators
4. Viget, "A Bone to Pick with Skeleton Screens," 2017. https://viget.com/articles/a-bone-to-pick-with-skeleton-screens

## Open questions

- The Viget sample size and results come from a search summary and were not checked on the page. The sample size (136) and the direction of the finding should be verified before a reviewer relies on them.
- The Mejtoft et al. ECCE 2018 study on skeleton and spinner perceived speed was reported in secondary results only; no URL or DOI was verified, so it is not cited.
- A recent "false front" paper comparing early-rendered pages against spinners and skeletons was reported, but its venue and authors could not be confirmed, so it is not cited.
- The Nielsen UX Tigers article gives no year, so its date is unverified.
- The thresholds for the spinner band (2 to 10 s) and the percent-done band (over 10 s) come from a single practitioner source. The 1 s no-indicator threshold matches the NN/g response time limit, but the progress-indicator rubric is a judgment call rather than a research-backed value.
- Anchors for scores 2 and 3 are judgment calls; no study was found that scores empty-state quality on a numeric scale.
