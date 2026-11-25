# Progressive Disclosure

> Measures whether advanced or rarely needed content is revealed only when the user asks for it, and whether the default view keeps the primary path uncluttered without hiding what is needed to finish the task.

## What it measures
- Whether the default view shows only the controls and content needed for the most common task, with secondary options collapsed, moved to a second screen, or behind an explicit trigger.
- Whether each disclosure trigger is a visible, labeled control (for example "Advanced options", "Show more", a chevron with text) rather than hover-only or gesture-only reveal.
- Whether revealed content is consistent with the trigger: the control states its current state (expanded or collapsed) and reverts cleanly.
- Whether required fields, primary actions, or information needed to proceed are never hidden behind a disclosure.
- Whether the number of disclosure levels stays shallow (one or two) so the user does not lose track of where content lives.

## Research basis
- Progressive disclosure defers advanced or rarely used features to a secondary screen, which Nielsen describes as making applications easier to learn and less error-prone. Source: Nielsen, J., "Progressive Disclosure" (Alertbox, 2006), https://www.nngroup.com/alertbox/progressive-disclosure.html. The 2006 date is taken from secondary summaries; the article text was not fetched directly.
- Carroll and Rosson's "training wheels" experiments found that a reduced-function interface in early use led to faster early performance (Nielsen reports 26% and 21% faster time on task in two studies) and better later performance on advanced editing functions than training on the full system. Sources: Carroll, J. M., and Rosson, M. B. (1987), "Learning a word processing system with training wheels and guided exploration," CHI '87 (URL not verified); Nielsen Norman Group summary, "Training Wheels in User Interfaces," https://www.nngroup.com/alertbox/training-wheels.html. The studies used one word processor, so generalization is limited.
- Nielsen Norman Group reports that designs going beyond two disclosure levels typically have low usability because users get lost between levels. Source: https://www.nngroup.com/alertbox/training-wheels.html (summary of the same guidance; not independently verified against a primary study).
- Hidden features must remain discoverable. Nielsen's guidance and the NN Group article on the same topic both stress that disclosure should be based on observed user behavior, not assumptions. Source: https://www.nngroup.com/alertbox/progressive-disclosure.html.
- Disclosure widgets need programmatic state. The W3C APG Disclosure (Show/Hide) pattern requires a button with `aria-expanded` set to true when content is visible and false when hidden, and optional `aria-controls`, operable with Enter and Space. Source: W3C, "Disclosure (Show/Hide) Pattern," WAI-ARIA Authoring Practices Guide, https://www.w3.org/WAI/ARIA/apg/patterns/disclosure.

## Scoring method
1. Identify the screen's primary task and list the controls and content on the default view.
2. For each item, classify it as primary (needed for the main task or required to proceed), secondary (occasionally needed), or advanced (rarely needed). Use the product's own task list or documented usage where available; otherwise state the assumption.
3. Count how many secondary and advanced items are visible without any user action. Record the count and the proportion of visible items that are secondary or advanced.
4. Check each secondary or advanced item: is it hidden behind a labeled trigger, a separate screen, or an equivalent explicit step? Record yes or no for each.
5. For each trigger, check that it is visible without hover, reads as a control (label or affordance), and states its state. Inspect the DOM or accessibility tree for `aria-expanded` and `aria-controls` on disclosure buttons, or record a manual observation if the markup is not available.
6. Confirm no primary or required item (including required form fields and the main action) is hidden. Record any violation as a failure.
7. Trace the path to one advanced item from the default view. Count the disclosure levels and clicks needed. Record the depth.
8. Record the observations in a table: item, classification, visible by default (Y/N), trigger labeled (Y/N), state exposed (Y/N), depth. Assign the score from the rubric.

## Scoring rubric
- **0**: Advanced or required content is hidden with no discoverable trigger, or primary content is hidden. Users cannot complete the main task without guessing.
- **1**: Most secondary or advanced content is visible by default, or triggers are icon-only or hover-only, or disclosure goes beyond three levels with no orientation cues.
- **2**: Some secondary content is hidden, but the default view is cluttered with several advanced options, or triggers are weakly labeled, or state is not exposed.
- **3**: Advanced content is generally hidden behind labeled triggers, but one or two items are misclassified, or the disclosure depth is three levels or the user loses track of location.
- **4**: The default view shows only primary and common secondary content. Every advanced item sits behind a labeled, visible trigger that exposes its expanded state. Depth is at most two levels. Minor inconsistencies only.
- **5**: As in 4, and the disclosure is based on evident usage data or a documented task analysis. Triggers are consistent across the product, every required item stays visible, and the state is programmatically exposed to assistive technology.

## Automated checks (optional)
Partial only. axe-core can flag disclosure buttons that lack an accessible name or `aria-expanded` when the markup uses the pattern, but it cannot decide whether content is primary or advanced, whether a trigger is discoverable, or whether the classification matches user needs. Counting visible elements against a classification list is a manual step. Otherwise: manual review only for classification and discoverability.

## Common failure patterns
- Primary or required fields hidden behind an "Advanced" section, forcing users to find them (NN Group guidance that hidden features must remain discoverable).
- Disclosure chosen by designer assumption, not observed use, so the wrong items are hidden (Nielsen 2006 guidance).
- Triggers that are icon-only, hover-only, or visually indistinct from decoration, so users never learn they exist.
- Three or more disclosure levels, leaving users unable to tell where content is (NN Group's two-level guidance).
- Disclosure widgets without `aria-expanded`, so assistive technology users cannot tell whether content is open (W3C APG).

## Sources
- Nielsen, J. (2006). "Progressive Disclosure." Nielsen Norman Group Alertbox. https://www.nngroup.com/alertbox/progressive-disclosure.html
- Nielsen Norman Group. "Training Wheels in User Interfaces." https://www.nngroup.com/alertbox/training-wheels.html
- Carroll, J. M., and Rosson, M. B. (1987). "Learning a word processing system with training wheels and guided exploration." CHI '87. URL not verified.
- Carroll, J. M., and Rosson, M. B. (1987). "The Paradox of the Active User." In Carroll (ed.), Interfacing Thought, MIT Press. Summary: https://www.nngroup.com/articles/paradox-of-the-active-user/
- W3C. "Disclosure (Show/Hide) Pattern." WAI-ARIA Authoring Practices Guide. https://www.w3.org/WAI/ARIA/apg/patterns/disclosure

## Open questions
- The Carroll and Rosson training-wheels results come from a single word processor study. Generalization to other products is not established.
- The 2006 date for Nielsen's guidance and the 1985 and 1995 dates mentioned in secondary sources conflict. The 2006 date is used here, unverified against the article.
- The "more than two levels" threshold comes from a NN Group summary, not a controlled study. Treat as practitioner guidance.
- The 26% and 21% time-on-task figures are reported by Nielsen Norman Group and were not checked against the original CHI paper.
- The rubric's distinction between a 3 and 4 (misclassified items, depth) and between 4 and 5 (usage data, consistency) is a judgment call, not research-backed.
- Research on the best threshold for how much content to hide is thin; the rubric's primary-versus-advanced split depends on the reviewer's task analysis.
