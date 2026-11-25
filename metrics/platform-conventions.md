# Platform Conventions

> Measures whether the interface follows the standard behaviors and idioms users expect on its platform.

## What it measures

- Placement and behavior of standard controls: primary actions, close, back, cancel, and undo sit where users on that platform expect them (for example, a dialog's confirm action on the trailing side, a close button in the top corner).
- Standard navigation idioms: links are underlined or otherwise recognizable as links, the back gesture or back control returns to the previous state, and tabs, menus and breadcrumbs behave as their platform implementation does.
- Input and interaction idioms: keyboard shortcuts for common actions (copy, paste, save, find) work as users expect, Enter and Escape behave conventionally in forms and dialogs, and drag, scroll and selection behave as on the host platform.
- Use of platform components versus custom replacements: native-looking pickers, date inputs, scrollbars and context menus are used where the platform supplies them, and custom widgets reproduce the standard behavior when they replace them.
- Iconography and labeling: icons with established meanings (search, settings, share, trash) are used for those meanings, and common labels (Save, Cancel, Delete) are used instead of invented synonyms.

## Research basis

- Consistency is a core usability principle, split into internal consistency (patterns within one product family) and external consistency (conventions of the platform, web, or domain). Users should not have to wonder whether different words, situations or actions mean the same thing. Source: Nielsen Norman Group, "Consistency and Standards" (https://www.nngroup.com/articles/consistency-and-standards/).
- Users bring expectations formed on other products, because people spend most of their time on sites and apps other than yours. Interactions should therefore match what users already anticipate. Source: Nielsen Norman Group, "Consistency and Standards," citing Jakob's Law (same URL). The original Jakob's Law essay was not fetched and is not cited directly here.
- Following conventions improves learnability and reduces confusion; breaking conventions adds cognitive load and should be done only when clearly necessary or when it measurably improves efficiency. Source: Nielsen Norman Group, "Consistency and Standards" (same URL).
- Consistency is not unconditionally beneficial. A 2022 study in the *International Journal of Human-Computer Interaction* compared brand-consistent interfaces with interfaces that conform to platform conventions and reported that the brand-consistent design did not reduce user acceptance. Source: "Cross-Platform Interface Design: To Conform or Not to Conform?" *International Journal of Human-Computer Interaction*, 2022, DOI 10.1080/10447318.2022.2105480 (https://informahealthcare.com/doi/abs/10.1080/10447318.2022.2105480; also indexed at https://www.bohrium.com/paper-details/cross-platform-interface-design-to-conform-or-not-to-conform/817366391802822656-2624). Authors were not verified from the search snippet.
- Consistency only has meaning relative to a reference, typically users' prior experience. A reviewer must therefore name the platform being compared against (iOS, Android, Windows, web) before scoring. Source: Dix's position as summarized in an arXiv review of HCI principles (https://arxiv.org/pdf/0707.3638). Attribution is from a secondary summary and is not verified against the original.

## Scoring method

1. Identify the target platform and its reference conventions (platform HIG or the web standard for web products). Record the platform name at the top of the review.
2. Enumerate the screen's standard controls: primary and secondary actions, navigation, form fields, dialogs, menus, icons, and links.
3. For each control, check placement, label, icon meaning and behavior against the reference. Use the platform's own component set (for example, Apple Human Interface Guidelines or Material Design component documentation) as the reference, not personal preference.
4. Test common keyboard idioms by hand: Tab order, Enter and Escape in forms and dialogs, and standard shortcuts for copy, paste, save and find where the platform defines them.
5. Test back and cancel behavior: confirm that the back control and the browser or system back gesture return to the prior state without data loss.
6. Count each deviation and classify it as (a) breaks an expectation with user-visible cost, (b) deviates but is justified by a stated task need, or (c) cosmetic. Only (a) lowers the score substantially.
7. Record the observations as a list: element, expected convention, observed behavior, classification. Score the screen against the rubric below.

## Scoring rubric

- 0: Core controls or navigation work contrary to platform convention in ways that block task completion (for example, Enter submits a destructive action with no confirmation, back exits the app unexpectedly from every screen).
- 1: Several convention breaks on the primary path; users must relearn basic actions.
- 2: At least one primary-path break with a clear cost, or several secondary breaks; custom widgets replace native ones without matching their keyboard or focus behavior.
- 3: Standard controls and navigation follow convention; a few secondary idioms (shortcuts, icon meanings, placement of minor actions) deviate without blocking tasks.
- 4: Primary and secondary idioms follow convention; any deviations are justified by a documented task need.
- 5: Fully conventional on the target platform, including keyboard and back behavior; deviations, if any, measurably improve efficiency.

## Automated checks (optional)

None reliable; manual review only. Automated accessibility tools such as axe-core can flag some role and focus issues but cannot judge whether a placement or icon meaning matches the platform's convention.

## Common failure patterns

- Custom widgets that replace native controls (selects, date pickers, scrollbars) and lose native keyboard and focus behavior.
- Icons used with meanings that differ from common usage, such as a trash icon that archives.
- Primary action placed on the wrong side or in an unexpected position relative to the platform's dialog pattern.
- Links styled as plain text, or buttons styled as links, so the element type is unclear.
- Cross-platform products that copy one platform's idioms onto another, following neither the target platform nor the web.
- Back or cancel that loses entered data or exits the flow unexpectedly.

## Sources

- Nielsen Norman Group, "Consistency and Standards." https://www.nngroup.com/articles/consistency-and-standards/
- "Cross-Platform Interface Design: To Conform or Not to Conform?" *International Journal of Human-Computer Interaction*, 2022. DOI 10.1080/10447318.2022.2105480. https://informahealthcare.com/doi/abs/10.1080/10447318.2022.2105480
- "The Review and Analysis of Human Computer Interaction (HCI) Principles," arXiv:0707.3638. https://arxiv.org/pdf/0707.3638 (authors and year not verified from the search snippet)

## Open questions

- The original Jakob's Law essay and the Dye and Caulton (1997) study on consistency in Microsoft Project were seen only as summaries in search results. Their URLs and full bibliographic details were not retrieved, so they are not cited as sources here.
- The 2022 IJHCI study concerns brand consistency versus platform conventions, not a general test of platform conventions. Its authors and sample details are unverified, and its finding does not establish that conventions always improve outcomes.
- Sources conflict in weight: NN/g treats conventions as a default, while a 1997 study reported a less consistent interface was more usable for expert users with different goals. The 0 to 5 anchors treat justified deviation as acceptable at level 4, which is a judgment call rather than a research-backed threshold.
- No canonical list of "standard behaviors users expect" was found. The enumerated signals above are drawn from practitioner guidance and platform HIGs, not from a validated instrument.
- The rubric's distinction between "blocks task completion" and "user-visible cost" is a judgment call; no study gives a numeric cutoff.
