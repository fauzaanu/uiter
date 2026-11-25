# Visual Hierarchy

> Measures how clearly size, weight, and emphasis signal what matters most and in what order.

## What it measures

- Whether the most important element on the screen is the largest or most prominent one, and whether a reviewer can name it within a few seconds.
- Whether heading, subheading, body, and caption levels use distinct, stepped sizes rather than near-identical ones.
- Whether weight (bold, semibold, regular, light) differs between levels and is reserved for a small number of emphasized items.
- Whether color, contrast, and position reinforce the same ordering, rather than competing with it.
- Whether the reading order implied by the layout (top to bottom, left to right, primary to secondary actions) matches the intended priority.

## Research basis

- Size is the most consistently reported driver of first fixation. Faraday (2000), as summarized in a secondary student source, lists size, scanning, images, text style, and position as the main factors, and reports that normal-sized text rarely served as an entry point even when bold or linked. Source: Faraday, 2000, original not retrieved; see Sources.
- Position predicts entry points better than size in a later test of the same model. Still (2018) found that position predicted entry points well, color and text style did a fair job, and size and images largely failed; the authors describe a strong bias toward size in the model. Source: Still, 2018, Computers in Human Behavior.
- Visual complexity changes scanning. Djamasbi, Siegel, and Tullis (2011) found viewing patterns on pages with a more complex visual hierarchy were more scattered than in earlier studies using simpler hierarchies. Source: Djamasbi et al., 2011, HCII 2011, LNCS 6761.
- Gaze is distributed unevenly across page elements and varies by task, so visual weight must be checked against actual attention patterns. Buscher, Cutrell, and Morris (2009) mapped gaze to page elements across 361 web pages from 20 participants. Source: Buscher et al., 2009, CHI.
- Combining size and weight produces stronger level contrast than either alone. This is practitioner consensus, not controlled evidence; see Open questions.

## Scoring method

1. Load the screen at a standard desktop width and at a common phone width. Record both.
2. Without reading, squint or blur the screen (or view a reduced-size screenshot). Note the one to three elements that dominate. Record them.
3. Ask the reviewer to name the most important action or content on the screen in one sentence. If the answer is not clear within about five seconds, record a miss.
4. List the distinct text levels on the screen. For each, record font size in px and font weight from computed styles or the design file. Count the distinct size steps and weight steps.
5. Check that the primary element differs from the next level by a clearly visible step in size or weight. Record the ratio and whether it is combined with a weight change.
6. Count the elements using bold or the highest emphasis style. Record the count; more than about three per viewport reduces the signal.
7. Check that color, contrast, and position point to the same element identified in step 2. Record any element that is emphasized by one cue only, or that is emphasized by a cue that contradicts the others.
8. Trace the intended reading order (top-to-bottom, left-to-right in the locale). Record any high-emphasis element that sits below or away from the expected entry point.
9. Score using the rubric. Record the observations, the chosen score, and the single element that most weakens the hierarchy.

## Scoring rubric

- **0 (severe failure):** No discernible order. All text is one size and weight, or the most prominent element is a low-priority item. The reviewer cannot name the main content.
- **1 (poor):** Some levels exist, but two or more are indistinguishable, or several elements compete for top emphasis. The main content is named only after effort.
- **2 (weak):** A primary element is identifiable, but the step to the next level is small (roughly under 1.25x in size and no weight change), or emphasis is applied to many items.
- **3 (adequate):** A clear primary element and at least three distinct levels. Steps are visible but not strong, or one cue (size, weight, or color) contradicts another in one place.
- **4 (good):** Primary element is named within about five seconds. Levels step clearly (roughly 1.25x or more between adjacent levels), weight is reserved for a few items, and color and position agree.
- **5 (exemplary):** Primary and secondary levels are named at a glance at both desktop and phone widths. Each level has a distinct, consistent size and weight, emphasis is sparing, and every cue reinforces the same order.

## Automated checks (optional)

Partial only. A script can read computed font sizes and weights, count distinct values, and flag elements using the highest weight. It cannot judge which element a viewer perceives as primary, cannot model gaze, and cannot assess color competition. Use it to fill steps 4 and 6; steps 2, 3, 7, and 8 remain manual.

## Common failure patterns

- Near-identical sizes across levels (for example 16px and 18px headings), so the hierarchy collapses into one tier. Relevant to Faraday's finding that size is the leading cue.
- Bold applied to many items, which dilutes the signal. Research on visual complexity (Djamasbi et al., 2011) links cluttered hierarchies to more scattered scanning.
- A high-contrast or colored element placed low on the page, competing with a top-placed primary element. Still (2018) shows position carries strong weight.
- A large image or banner that dominates the page while the actual task element is small. The size bias noted by Still (2018) means reviewers and users alike may fixate on the wrong item.
- Emphasis that is inconsistent across themes or breakpoints, so the order holds on desktop and fails on mobile.

## Sources

1. Faraday, P. (2000). Visually critiquing web pages. Original not retrieved; claims are taken from a secondary summary at https://tigerweb.towson.edu/rchelch1/ex5/page3.html
2. Still, J. D. (2018). Web page visual hierarchy: Examining Faraday's guidelines for entry points. Computers in Human Behavior. https://www.bohrium.com/paper-details/web-page-visual-hierarchy-examining-faraday-s-guidelines-for-entry-points/813051593975922689-7721
3. Djamasbi, S., Siegel, M., & Tullis, T. (2011). Visual hierarchy and viewing behavior: An eye tracking study. HCI International 2011, LNCS vol. 6761, pp. 331-340. https://rd.springer.com/chapter/10.1007/978-3-642-21602-2_36
4. Buscher, G., Cutrell, E., & Morris, M. R. (2009). What do you see when you're surfing? Using eye tracking to predict salient regions of web pages. CHI 2009. https://www.microsoft.com/en-us/research/publication/what-do-you-see-when-youre-surfing-using-eye-tracking-to-predict-salient-regions-of-web-pages/

## Open questions

- Faraday (2000) and Still (2018) were reached through secondary snippets. Full author lists for Still (2018) and the original Faraday text were not verified, and the Faraday claims are unverified at source.
- The 1.25x size step and the "about three" emphasis limit in the rubric are judgment calls, not research thresholds. No source found gives a numeric size ratio for hierarchy.
- The claim that combining size and weight beats either alone comes from practitioner blogs and is not verified in a controlled study.
- Sources conflict on the strength of size: Faraday (2000) ranks it highest, while Still (2018) finds size largely failed to predict entry points. The rubric weights size and position equally on purpose, pending better evidence.
- No NN/g primary article on typographic hierarchy was retrieved; NN/g attributions found in secondary sources were not used.
