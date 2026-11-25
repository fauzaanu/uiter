# Interaction Cost

> Interaction cost is the total effort a user spends to reach a goal in an interface, counted as the number of steps, clicks, and decisions needed to complete common tasks.

## What it measures

- Number of discrete actions (taps, clicks, keypresses) needed to complete a named task from a stated starting screen.
- Number of navigation hops: screens, dialogs, or menu levels entered before the goal is reached.
- Number of decision points: moments where the user must choose among options, such as picking a menu item, a filter, or a button label.
- Avoidable steps: actions that repeat information already given, re-enter data the system already holds, or confirm something that needed no confirmation.
- Unnecessary scrolling or searching that a reviewer can observe as extra motion between the start and the goal.

## Research basis

- Interaction cost is defined as "the sum of efforts, mental and physical, that users must deploy in interacting with a digital product in order to reach their goals." Clicks are only one component; reading, comprehension, scanning, attention switches, memory load, typing, and waiting also count. Source: Raluca Budiu, "Interaction Cost: Definition," Nielsen Norman Group, 2013, last reviewed 2024. https://www.nngroup.com/articles/interaction-cost-definition/
- Click counts correlate with task time but explain only part of it. Across 19 unmoderated ecommerce tasks (1,228 users), the average correlation was r = .5, meaning clicks explain about 25% of task-time variation; for consumer software the correlation was r = .67. Source: Jeff Sauro, "Clicks don't really matter" (MeasuringU), 2011. https://measuringu.com/?p=90
- Step counts are an imperfect proxy because clicks are not equal (one scroll versus repeated scroll-arrow clicks). Keystroke-Level Modeling estimates expert task time by summing operator times. Source: Stuart K. Card, Thomas P. Moran, and Allen Newell, "The Keystroke-Level Model for User Performance Time with Interactive Systems," Communications of the ACM 23(7), 1980, pp. 396-410 (cited via secondary summary; the original was not opened). https://en.wikipedia.org/wiki/Keystroke-level_model
- Decision time grows with the number of choices, roughly logarithmically under Hick-Hyman, though randomly ordered long menus behave closer to linear scanning. Source: IxDF, "The Hick-Hyman Law: An Argument Against Complexity in User Interface Design." https://ixdf.org/literature/article/the-hick-hyman-law-an-argument-against-complexity-in-user-interface-design
- Pointing time for menu and button selection follows Fitts' law (distance and target width). Source: Penn State IST course notes, "Fitts' law and menus." https://acs.ist.psu.edu/courses/ist230-fall2000/Fitts_law_and_menus.html
- Recent work codes task attempts for clicks, full screens, popups, and interface states rather than clicks alone. Source: arXiv 2609.28672, "Available but Not Usable: Dark Patterns and Interaction Cost in Social Media Privacy and Safety Settings for Teens" (seen as search excerpt only). https://arxiv.org/pdf/2609.28672

## Scoring method

1. Pick 3 to 5 common tasks from the product's primary flows and write each as a single goal with a fixed starting screen.
2. Start a recording or a step log. Use a screen recorder or a timed walkthrough with the first-time-user path.
3. Count each discrete action: taps, clicks, keypresses, and form entries. Record each navigation hop as a screen change or a dialog open.
4. Count decision points separately: each moment where the path forks or the user must read and choose among labelled options.
5. Mark avoidable steps: repeated input, unnecessary confirmations, and scroll-to-find cases. Note each by screen.
6. Compare the counted path with the shortest path the design could reasonably offer. Record the ratio of actual to minimum steps.
7. Record the observations per task in the form: task, actions, hops, decisions, avoidable steps, minimum path, ratio.
8. Where time is available, record task time alongside step counts, because step counts alone explain only part of task time.

## Scoring rubric

Scale 0 to 5 (0 = severe failure, 5 = exemplary). Anchors use the ratio of actual steps to the minimum path across the sampled tasks.

- 5: Every task completes at or within 1.1 times the minimum path; no avoidable steps; no more than one decision per screen.
- 4: Ratio 1.1 to 1.3; at most one avoidable step in the sampled tasks.
- 3: Ratio 1.3 to 1.6; a few avoidable steps or one task with a redundant confirmation or hop.
- 2: Ratio 1.6 to 2.0; several avoidable steps or dead-end navigation that the user must back out of.
- 1: Ratio above 2.0; or a task needs a hunt across multiple unrelated screens.
- 0: A common task cannot be completed, or the path is blocked by a mandatory detour that a reviewer cannot resolve.

The 1.1, 1.3, 1.6, and 2.0 cut-offs are judgment calls, not research thresholds. No source found gives a click limit for good design. The "3-click rule" is not supported by published data, per a critique from the University of St Andrews (https://digitalcommunications.wp.st-andrews.ac.uk/2019/09/18/clicks-dont-really-matter/).

## Automated checks (optional)

None reliable; manual review only. Step counting depends on task definition and the user's path, which a tool cannot infer. A script could count DOM navigations for a scripted path, but it would miss decision cost and mental effort.

## Common failure patterns

- Counting only clicks and ignoring reading, scanning, and decision load, which NN/g identifies as part of the interaction cost.
- Hiding primary actions in deep menus, which increases both hops and Hick-Hyman decision time for expert users.
- Forcing re-entry of data the system already holds, adding avoidable steps with no benefit to the user.
- Adding confirmation dialogs to low-risk actions, adding steps without reducing error cost.
- Reporting one task's step count as representative of the product; the sampled tasks must cover the main flows.
- Treating fewer clicks as always better, when a longer path that is familiar can cost less than a short one with unclear labels.

## Sources

1. Raluca Budiu, "Interaction Cost: Definition," Nielsen Norman Group, 2013 (rev. 2024). https://www.nngroup.com/articles/interaction-cost-definition/
2. Jeff Sauro, "Clicks don't really matter," MeasuringU, 2011. https://measuringu.com/?p=90
3. Stuart K. Card, Thomas P. Moran, and Allen Newell, "The Keystroke-Level Model for User Performance Time with Interactive Systems," Communications of the ACM 23(7), 1980. (Secondary summary: https://en.wikipedia.org/wiki/Keystroke-level_model)
4. "The Hick-Hyman Law: An Argument Against Complexity in User Interface Design," Interaction Design Foundation. https://ixdf.org/literature/article/the-hick-hyman-law-an-argument-against-complexity-in-user-interface-design
5. "Fitts' law and menus," Penn State IST 230 course notes, 2000. https://acs.ist.psu.edu/courses/ist230-fall2000/Fitts_law_and_menus.html
6. "Available but Not Usable: Dark Patterns and Interaction Cost in Social Media Privacy and Safety Settings for Teens," arXiv 2609.28672 (seen as excerpt only). https://arxiv.org/pdf/2609.28672

## Open questions

- The Card, Moran, and Newell 1980 paper and its operator timings were not opened; the KLM details come from secondary summaries. Verify the operator times before using KLM estimates.
- The arXiv 2609.28672 and 2610.05047 (terminal UIs) findings are from search excerpts only, not full papers.
- The CDC-hosted Markov-chain study on clicks was seen only as a search excerpt with no verified title or venue, so it is not cited above.
- Sauro's correlation figures come from unmoderated ecommerce and consumer software tests, which may not transfer to other domains.
- The ratio cut-offs in the rubric are judgment calls. No source reviewed gives a numeric threshold for acceptable step counts.
- Hick-Hyman applies to chosen options, but the research on whether users scan non-linearly in real interfaces is contested (Seow 2005, cited in the IxDF piece, was not read directly).
