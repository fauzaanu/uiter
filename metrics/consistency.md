# Consistency

> Consistency scores whether the same components, patterns, and terms behave and look the same across the screens of a product, and whether the product follows conventions users already know from elsewhere.

## What it measures

- Repeated components (buttons, inputs, cards, badges, tables) share one visual treatment: same fill, border radius, type, icon style, and size variants across screens.
- The same action uses the same control and placement everywhere (for example, "Save" is always a primary button at the bottom right of a form, not a link on one screen and a button on another).
- The same concept uses the same label everywhere ("Delete" on one screen and "Remove" for the same operation on another is an inconsistency).
- Status and feedback patterns repeat: errors, success messages, and warnings use the same color, icon, and position.
- Navigation elements keep their order, labels, and location across pages.
- Where the product departs from platform or web conventions, the departure is deliberate and does not break familiar behavior.

## Research basis

- **Consistency is about predictability, not uniformity.** Consistency with the product's own designs (internal) and with conventions in other systems users already know (external) are both evaluated. Nielsen Norman Group, "Consistency and Standards" (Usability Heuristic 4). https://www.nngroup.com/articles/consistency-and-standards/
- **Consistent identification of repeated functional components is a conformance requirement.** WCAG 2.2 SC 3.2.4 requires that components with the same functionality across a set of pages be identified consistently. Labels need not be identical when the functions differ. W3C, "Understanding SC 3.2.4 Consistent Identification (Level AA)." https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification
- **Consistent action syntax reduces the number of actions users need.** In a 114-participant laboratory study, inconsistent action syntax across two applications increased the number of user actions needed to finish tasks. Satzinger and Olfman, "User Interface Consistency Across End-User Applications: The Effects on Mental Models," Journal of Management Information Systems 14(4), 1998. https://jmis-web.org/articles/856
- **Inconsistent visual appearance did not reduce accuracy in that study.** The same study found that inconsistent visual appearance produced greater accuracy, which the authors called surprising. Satzinger and Olfman, 1998 (as above).
- **Consistency has limits and can trade off against fit to purpose.** Lin and Levin report a fast learning curve from consistent interfaces, but a lower ceiling on expertise than multiple-interface groups achieved. Lin and Levin, "Consistency vs. Multiplicity in Interface Design." https://pages.ucsd.edu/~jalevin/TTA/Papers/Lin-Levin/index.html
- **Consistency is a weak goal taken alone.** Grudin argues that consistency is an unreliable guide and that designers often do better by attending to users' work contexts, while noting that rejecting consistency as a primary goal does not license randomness. Grudin, "The Case Against User Interface Consistency," Communications of the ACM 32(10), 1989. https://www.microsoft.com/en-us/research/publication/case-user-interface-consistency/

## Scoring method

1. Collect at least five screens that cover the main flows, including one form, one list or table, one detail view, and one error or empty state.
2. Inventory the repeated components on those screens: buttons, inputs, links, cards, tags, icons, tables, and navigation.
3. For each component type, compare its visual properties (fill, border, radius, type size, weight, icon style) across screens using a screenshot overlay or a side-by-side view. Note every variant that is not a deliberate size or emphasis variant.
4. For each recurring action (save, delete, cancel, add, back), record the control type and its placement on every screen where it appears.
5. List the terms used for each recurring concept (status words, object names, action verbs) and note every case where two terms refer to the same thing, or one term refers to two things.
6. Check feedback patterns: the same message type (success, error, warning) should use the same color, icon, and position.
7. Record each inconsistency with screen, component, and the two conflicting instances. Count the total and the number of distinct component types affected.
8. Score using the rubric below, weighting inconsistencies in high-frequency components and in destructive or high-stakes actions more heavily.

## Scoring rubric

- **0**: No recognizable shared system. The same action, component, or term looks or behaves differently on most screens, so users cannot predict behavior.
- **1**: Frequent conflicts in core components or terms (for example, three different button styles for the same primary action, or "Delete" and "Remove" used interchangeably for the same operation).
- **2**: A shared style exists but is applied unevenly. Several conflicts in common components or actions, and at least one destructive action or error pattern differs from the rest.
- **3**: Core components and actions behave consistently. Remaining conflicts are limited to secondary components, edge states, or a few labels.
- **4**: Nearly all repeated components, actions, and terms match. Any deviation is deliberate and documented by a visible variant (size, emphasis, or context).
- **5**: Every repeated component, action, term, and feedback pattern is identical in behavior and appearance across all reviewed screens, and departures from platform conventions are clearly justified by the product's purpose.

## Automated checks (optional)

None reliable; manual review only. Automated tools can flag identical-role components with different computed styles, but they cannot judge whether a difference is deliberate or whether two labels mean the same thing.

## Common failure patterns

- **Parallel variants of one component.** Several button or card styles coexist because each screen was built separately. Users cannot tell which one is "primary" (see the component-variant guidance in Satzinger and Olfman, 1998).
- **Synonym drift.** "Delete", "Remove", "Trash", and "Discard" are used for the same operation. Users must wonder whether words differ in meaning, which the NN/g heuristic identifies as the core failure (NN/g, "Consistency and Standards").
- **Action placement changes.** The primary action moves from bottom-right to top-right between flows, increasing actions needed to complete tasks (Satzinger and Olfman, 1998).
- **Inconsistent feedback semantics.** Errors appear as red toast on one screen and as inline text on another, so users cannot learn where to look.
- **Non-functional consistency overreach.** Teams make decorative elements identical while functional controls diverge. WCAG 3.2.4 scopes consistency to functional components.

## Sources

1. Nielsen Norman Group. "Consistency and Standards" (Usability Heuristic 4). https://www.nngroup.com/articles/consistency-and-standards/
2. W3C WAI. "Understanding SC 3.2.4 Consistent Identification (Level AA)," WCAG 2.2. https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification
3. Satzinger, J. W., and Olfman, L. (1998). "User Interface Consistency Across End-User Applications: The Effects on Mental Models." Journal of Management Information Systems, 14(4). https://jmis-web.org/articles/856
4. Lin, Z., and Levin, J. "Consistency vs. Multiplicity in Interface Design." Year and venue not verified. https://pages.ucsd.edu/~jalevin/TTA/Papers/Lin-Levin/index.html
5. Grudin, J. (1989). "The Case Against User Interface Consistency." Communications of the ACM, 32(10), 1164-1173. https://www.microsoft.com/en-us/research/publication/case-user-interface-consistency/
6. SciTePress (2021). Paper on ambiguity of the NN/g consistency heuristic for novice evaluators. Full title not verified. https://www.scitepress.org/Papers/2021/103130/103130.pdf

## Open questions

- The Satzinger and Olfman findings come from abstracts only. The full text was not checked, so the statistical detail and the conditions for the "surprising" accuracy result are unverified.
- Lin and Levin's year and venue were not confirmed from the search record.
- The Grudin paper was read through excerpts and secondary citations, not the full text.
- The 0 to 5 anchors are a judgment call. The research supports the direction of effects (consistency aids learning and reduces actions) but gives no validated threshold for how many conflicts equal a given score.
- Research points to consistency mattering most for repeated functional elements. How much weight decorative or brand elements should carry is not supported by the sources reviewed.
