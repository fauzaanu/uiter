# Consistency and Context Fit

> Does the screen behave like one coherent, trustworthy product that matches its platform and still holds up at other widths, in other themes, and in other languages?

## Covered metrics

- `consistency`: Consistency
- `responsiveness`: Responsiveness
- `platform-conventions`: Platform Conventions
- `trust-credibility`: Trust and Credibility
- `theme-parity`: Theme Parity
- `localization-readiness`: Localization Readiness

## What it measures

- Internal consistency: repeated components share one visual treatment; the same action uses the same control, label, and placement; feedback patterns and navigation stay the same.
- External consistency: standard controls, navigation idioms, keyboard and back behavior, icons, and labels follow the named platform; custom widgets reproduce the behavior of the native ones they replace.
- Craft and legitimacy: no typos, placeholder content, broken images, clipped or overlapping text, or unhandled error text; trust cues fit the task; visual formality fits the product's purpose.
- Width and orientation: no horizontal overflow, single-column reflow at 320 CSS px, no lost functions at narrow widths, no orientation lock, and text that wraps instead of truncating.
- Themes: contrast, hierarchy order, semantic meaning, focus indicators, component boundaries, and assets hold in every theme.
- Languages: containers tolerate strings 30 to 40 percent longer, layout mirrors correctly for right-to-left scripts, mixed-direction content keeps its order, and dates and numbers are locale-driven.

## Scoring method

Work from the screenshot. Other screens, widths, orientations, themes, locales, and keyboard behavior cannot be observed in one image. Judge the screen shown plus the visible signs of how it would hold up, and say in the rationale which checks were not observable.

1. Name the target platform (iOS, Android, Windows, web) and the theme and approximate width the screenshot shows.
2. Inventory repeated components (buttons, inputs, cards, badges, icons, navigation). Record every variant that is not a deliberate size or emphasis variant.
3. For each recurring action (save, delete, cancel, add, back), record its control type, label, and placement. List terms where two words mean one thing or one word means two things. Check that same-type messages share color, icon, and position.
4. Compare standard controls with the platform reference: placement of primary, close, back, and cancel; link styling; icon meanings; common labels; native components against custom replacements. Classify each deviation as (a) breaking an expectation with user-visible cost, (b) justified by a task need, or (c) cosmetic. Only (a) lowers the score substantially.
5. Craft: count typos, placeholder text, broken or missing images, clipped or overlapping text, and misaligned controls. Count type families (more than three is a warning).
6. Trust: if the screen collects personal or payment data, look for a clear security or privacy cue and a visible path to help or contact. Write one sentence on whether the formality suits the product category.
7. Width: look for horizontal overflow, clipped or truncated text, overlapping elements, and fixed-width containers already near their limit. Note navigation or actions that appear to be missing rather than relocated.
8. Theme: in the theme shown, check text against 4.5:1 (3:1 for large text) and component boundaries and meaningful graphics against 3:1. Flag hard-coded-looking colors, images or logos with halos, borders or shadows that vanish, and semantic colors with no non-color cue.
9. Localization: flag text containers with no room for 30 to 40 percent longer strings, text that cannot wrap, directional icons and layout that would need mirroring, and dates or numbers that look hard-coded.
10. Place each member on the rubric, combine them into one score, letting the failures most visible to a user pull the score down the most, and write todos for the lowest members first.

## Scoring rubric

Thresholds come from the member files (WCAG 1.4.10, 1.3.4, 1.4.3, 1.4.11, 3.2.4; practitioner 30 and 40 percent expansion figures; member judgment anchors).

- **0**: No recognizable shared system. Core controls or navigation work against platform convention in ways that block the task. Broken layout or images on the main path, visible placeholder or error text, or a payment or login screen with no credible cue. Horizontal scrolling or clipped content at 320 px, key actions missing at narrow widths, or an orientation lock. In at least one theme, primary text or the primary action is unreadable. Primary actions are clipped under long strings, or right-to-left is not supported at all.
- **25**: Frequent conflicts in core components or terms (three button styles for one primary action; "Delete" and "Remove" for the same operation). Several convention breaks on the primary path. Three or more typos or broken elements; the product looks unfinished. Overflow or clipping at two or more widths. In one theme, several text pairs fall below threshold, or two hierarchy levels merge. Several fixed-width components clip.
- **50**: A shared style exists but is applied unevenly; at least one primary-path convention break carries a clear cost, or secondary idioms deviate. Recurring defects a user would notice within a minute, or one or two minor defects in a mostly coherent system. Reflow works at most widths with one failing check or cramped spacing. Theme failures are limited to secondary elements. Primary components tolerate about 30 percent expansion, while secondary ones clip.
- **75**: Nearly all repeated components, actions, and terms match, and deviations are deliberate. Primary and secondary idioms follow the platform. No visible defects on the main path, with appropriate cues on sensitive screens. The screen passes all widths and both orientations, with navigation adapting in form without loss of function. All text and required non-text pairs pass in every theme, with matching hierarchy and semantic cues. Components tolerate about 40 percent expansion, dates and numbers are locale-driven, and non-directional icons stay unflipped.
- **100**: Every repeated component, action, term, and feedback pattern is identical across reviewed screens, and departures from convention are justified by the product's purpose. No defects across screens, with cues calibrated to the task. Layout changes at breakpoints that match the content's structure, with no horizontal scroll at 320 CSS px. Every theme passes 4.5:1 for text and 3:1 for large text and non-text, with structurally identical hierarchy. The screen passes long-string, right-to-left, and locale-format conditions with no clipping, overlap, or ordering errors.

## Member sub-criteria

- `consistency`: Detail: metrics/consistency.md
- `responsiveness`: Detail: metrics/responsiveness.md
- `platform-conventions`: Detail: metrics/platform-conventions.md
- `trust-credibility`: Detail: metrics/trust-credibility.md
- `theme-parity`: Detail: metrics/theme-parity.md
- `localization-readiness`: Detail: metrics/localization-readiness.md

## Common failure patterns

- Parallel variants of one component; synonym drift ("Delete", "Remove", "Trash", "Discard").
- The primary action moves between flows; errors appear as a toast on one screen and inline on another.
- Custom widgets that replace native selects, date pickers, or scrollbars and lose keyboard and focus behavior.
- Icons used against their common meaning (a trash icon that archives); links styled as plain text.
- Polished hero areas above broken or placeholder content; sensitive flows with no security or contact signal; raw technical text in error states.
- Fixed-width containers, large images, or wide tables that overflow at 320 px; navigation hidden with no visible trigger; a "rotate your device" overlay.
- Text truncated with ellipses or clipped in fixed-height containers.
- Hard-coded hex values that do not switch with the theme; borders and shadows that disappear on dark surfaces; semantic hues that drift between themes.
- Fixed-width buttons and tabs that clip after translation; mirroring applied to clocks, play icons, and refresh symbols; hard-coded date and number strings.

## Sources

- Nielsen Norman Group, Consistency and Standards. https://www.nngroup.com/articles/consistency-and-standards/
- W3C, Understanding SC 3.2.4 Consistent Identification. https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification
- Satzinger and Olfman (1998), JMIS 14(4). https://jmis-web.org/articles/856
- Lin and Levin, Consistency vs. Multiplicity in Interface Design. https://pages.ucsd.edu/~jalevin/TTA/Papers/Lin-Levin/index.html
- Grudin (1989), The Case Against User Interface Consistency. https://www.microsoft.com/en-us/research/publication/case-user-interface-consistency/
- SciTePress (2021), paper on the consistency heuristic (title not verified). https://www.scitepress.org/Papers/2021/103130/103130.pdf
- Cross-Platform Interface Design: To Conform or Not to Conform? (2022). https://informahealthcare.com/doi/abs/10.1080/10447318.2022.2105480
- The Review and Analysis of HCI Principles, arXiv:0707.3638. https://arxiv.org/pdf/0707.3638
- Lindgaard, Fernandes, Dudek, and Brown (2006). https://doi.org/10.1080/01449290500330448
- Robins and Holmes (2008), Aesthetics and credibility in web site design. https://makinggood.ac.nz/media/1276/robinsholmes_2008_aestheticsandcredibilityinwebdesign.pdf
- Fogg (2002), Stanford Guidelines for Web Credibility. https://credibility.stanford.edu/guidelines
- Nielsen Norman Group, Dark Mode. https://www.nngroup.com/articles/dark-mode/
- W3C, Understanding SC 1.4.3 Contrast (Minimum). https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
- W3C, Understanding SC 1.4.11 Non-text Contrast. https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html
- While and Sarvghad (2024), arXiv:2409.10841. https://arxiv.org/abs/2409.10841v1
- Goldenberg and Tractinsky (2025), Exploring amBiDiguity. https://cris.iucc.ac.il/en/publications/exploring-ambidiguity-ui-item-direction-interpretation-by-arabic-/
- Anvari and Woods (2024), AHFE. https://openaccess.cms-conferences.org/publications/book/978-1-964867-19-9/article/978-1-964867-19-9_24
- W3C (2015), HTML bidi Note. https://www.w3.org/TR/2015/NOTE-html-bidi-20150721/
- Unicode TR35, Dates and Numbers. https://www.unicode.org/reports/tr35/tr35-78/tr35-dates.html and https://www.unicode.org/reports/tr35/tr35-78/tr35-numbers.html
- Nielsen Norman Group, International Usability: Details Differ. https://www.nngroup.com/articles/international-usability-details-differ/
- Microsoft Globalization, Pseudolocalization. https://learn.microsoft.com/globalization/methodology/pseudolocalization
- W3C, Understanding SC 1.4.10 Reflow. https://www.w3.org/WAI/WCAG22/Understanding/reflow
- W3C, Understanding SC 1.3.4 Orientation. https://www.w3.org/WAI/WCAG22/Understanding/orientation
- Nielsen Norman Group, Grids, Layouts, and Responsive Design. https://www.nngroup.com/articles/breakpoints-in-responsive-design/
- Springer, ENTER 2015 proceedings. https://rd.springer.com/chapter/10.1007/978-3-319-14343-9_43
- Jurnal Teknologi, responsive web design and user experience. https://journals.utm.my/jurnalteknologi/article/view/6041

## Open questions

- Consistency is not unconditionally good (Grudin; Satzinger and Olfman; the 2022 cross-platform study). The rubric treats justified deviation as acceptable, which is a judgment call.
- No canonical list of platform conventions was found; the reviewer must name the reference platform before scoring.
- No source tests typos or broken links directly against credibility. The defect counts and the "more than three type families" limit are judgment calls.
- No source covers structural parity of hierarchy or meaning across themes.
- The 30 and 40 percent expansion figures are practitioner numbers, and breakpoint values conflict across sources, so the rubric scores observed breakage.
- One screenshot shows one width, one theme, and one locale. Without more captures, the responsiveness, theme, and localization parts are estimates from visible risk signs.
