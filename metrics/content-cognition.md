# Content and Cognitive Effort

> Can a user find what they need, understand what every label, icon, and message means, and finish the task without extra steps or having to remember things?

## Covered metrics

- `navigation-clarity`: Navigation Clarity
- `information-architecture`: Information Architecture
- `copy-microcopy`: Copy and Microcopy
- `cognitive-load`: Cognitive Load
- `interaction-cost`: Interaction Cost
- `recognition-over-recall`: Recognition over Recall
- `progressive-disclosure`: Progressive Disclosure
- `iconography`: Iconography

## What it measures

- Orientation: the current section, page, or step is visibly marked, the heading agrees with it, main destinations are visible as labeled items, and a return path exists that does not depend on the browser back button.
- Structure: items are grouped into categories users expect, labels are distinct and in user vocabulary, each item has one obvious home, and headings name the content beneath them.
- Wording: labels say what to enter, hints give concrete formats, buttons name the action and its object, and messages say what happened and what to do next.
- Load: the number of items and simultaneous decisions in view, and whether they are grouped into a few scannable chunks.
- Effort: actions, navigation hops, and decision points needed for a common task, and steps that are avoidable.
- Memory: options, state (filters, mode, selections, step), earlier values, and help are shown where needed, not left to recall.
- Disclosure: advanced or rare content sits behind a visible labeled trigger, while required fields and primary actions are never hidden.
- Icons: recognizable in context, labeled where meaning is not standard, one style, and one meaning per glyph.

## Scoring method

Work from the screenshot. Multi-screen paths, tree tests, "where am I" tests, disclosure behavior, and accessible names cannot be observed in one image. Judge the screen shown and say in the rationale which checks were not observable.

1. State the primary task the screen supports and the starting point.
2. Navigation: check that the active top-level item is marked and how (color alone is a weak mark), that the heading names the section and page, and that a return path is visible. Count top-level destinations visible without opening a menu, and note any hidden, unlabeled, or behind a generic "More".
3. Structure: list top-level labels verbatim and mark each clear, ambiguous, or generic ("Other", "More", "Misc", "Resources"). Flag labels that overlap, items that fit two groups or none, and headings that do not name their content.
4. Copy: list every label, hint, button, error, and status string. Check each button for a verb plus object, each field for a label outside the placeholder, and each message for problem, next step, and no blame or raw codes. Flag strings over roughly 12 words and any action named with two different words.
5. Load: count visible controls and blocks, simultaneous decisions before the primary action, the number of chunks, the items in the largest chunk, and the extraneous items.
6. Effort: walk the primary task on the screen. Count actions and decision points, and mark avoidable steps (re-entered data, needless confirmations, scroll-to-find). Estimate the ratio of actual to minimum steps where the path is visible.
7. Memory: list what the user must know that is not on screen, such as a command, a path, an earlier value, an ID, a format, or an icon's meaning. Check that state and in-context hints are visible.
8. Disclosure: classify visible items as primary, secondary, or advanced. Count secondary and advanced items shown by default, and check that triggers are visible and labeled and that nothing required is hidden.
9. Icons: mark each icon as icon-only, labeled, or decorative. For each icon-only control, judge whether a first-time user could name its action in five seconds. Count distinct icon styles and any glyph reused for two meanings.
10. Place each member on the rubric, combine them into one score, letting the failures most visible to a user pull the score down the most, and write todos for the lowest members first.

## Scoring rubric

Thresholds come from the member files (Cowan's 3 to 5 chunks; NN/g two-level disclosure guidance; WCAG 2.4.5, 2.4.8, 3.3.2, 3.3.3, 1.1.1; member judgment anchors).

- **0**: No current-location marking, no return path, and destinations hidden or unlabeled. Groups are arbitrary, with most labels generic or overlapping. Buttons are absent, generic, or misleading, and errors show only codes. Dozens of ungrouped controls with an unclear primary action. A common task cannot be completed, or needs memorized commands, paths, or codes. Primary or required content is hidden. Most icon-only controls are unclear.
- **25**: Location or return path is missing on most screens. Several labels are ambiguous or internal jargon, and items are misfiled. Most strings are generic; placeholder is the only label. More than about 9 items sit in one group, with advanced options shown by default. Steps exceed 2.0 times the minimum path. Most tasks need recall of a hidden command or code. Triggers are icon-only or hover-only, or disclosure goes beyond three levels. Several icons are guessed or wrong.
- **50**: Location marking exists but is subtle or color-only. Grouping is broadly logical, with one mixed group or a few items sitting awkwardly. Some buttons are verb-led, others generic or inconsistent. The largest group is about 7 items, or more than 5 simultaneous decisions are asked. Step ratio is 1.3 to 2.0. Primary actions are visible, but several secondary tasks rely on unlabeled icons or carried values. Some advanced options clutter the default view. Two or more ambiguous icons are unlabeled.
- **75**: Location, destinations, and return path are all clear, with a breadcrumb or equivalent on deep pages. Groups and labels match expected categories, each item has one clear home, and headings track content. Every button names its action and object, labels persist, errors state problem and fix, and terms are consistent. Essential decisions are about 3 to 5 at a time in 3 to 5 chunks. Step ratio is 1.1 to 1.3 with at most one avoidable step. All common tasks are completable from what is on screen. Advanced items sit behind labeled triggers at most two levels deep. All icons are clear or labeled, in one style.
- **100**: All of the above with no exceptions. Current state is identifiable without color. Labels use customer vocabulary with consistent depth across branches. Copy is concise and specific, and empty states lead to the next step. Only the decisions the task needs are visible, in no more than about 4 chunks, with no extraneous items and no memory dependence. Every task is within 1.1 times the minimum path with no more than one decision per screen. Every required item stays visible. Icon style and meaning match across the product.

## Member sub-criteria

- `navigation-clarity`: Detail: metrics/navigation-clarity.md
- `information-architecture`: Detail: metrics/information-architecture.md
- `copy-microcopy`: Detail: metrics/copy-microcopy.md
- `cognitive-load`: Detail: metrics/cognitive-load.md
- `interaction-cost`: Detail: metrics/interaction-cost.md
- `recognition-over-recall`: Detail: metrics/recognition-over-recall.md
- `progressive-disclosure`: Detail: metrics/progressive-disclosure.md
- `iconography`: Detail: metrics/iconography.md

## Common failure patterns

- Active state shown by color alone or too subtly; heading and navigation label disagree; deep pages with no path back.
- Catch-all groups ("Other", "More", "Misc"); internal terms in place of user words; the same item under different names.
- Generic headings ("Overview", "Details"); parent categories that cannot be clicked.
- Generic buttons ("OK", "Submit", "Yes/No"); errors with no remedy, with blame, or with raw codes; two words for one action ("Delete" and "Remove").
- Settings pages that show every option at once; long ungrouped option lists; a primary metric competing with many equal-weight values.
- Primary actions hidden in deep menus; re-entry of data the system already holds; confirmations on low-risk actions.
- Commands available only through shortcuts; wizards that do not show earlier entries; active filters or modes not displayed.
- Required fields hidden behind "Advanced"; hover-only or icon-only triggers; three or more disclosure levels.
- Icon-only toolbars with app-specific glyphs; labels shown only on hover; mixed icon styles; one glyph for two commands.

## Sources

- Nielsen Norman Group, Navigation: You Are Here. https://www.nngroup.com/articles/navigation-you-are-here/
- Baymard Institute, highlight users' navigation scope. https://baymard.com/research-articles/highlight-users-navigation-scope
- W3C, Technique G128. https://www.w3.org/TR/WCAG-TECHS/G128.html
- W3C, Understanding SC 2.4.5 Multiple Ways. https://www.w3.org/WAI/WCAG21/Understanding/multiple-ways
- W3C, Understanding SC 2.4.8 Location. https://www.w3.org/WAI/WCAG20/Understanding/location
- Visa Design System, breadcrumbs usage (secondary for NN/g breadcrumb guidance). https://design.visa.com/components/breadcrumbs/usage/
- UNC master's paper on breadcrumbs. https://ils.unc.edu/MSpapers/3305.pdf
- Katsanos et al. (2019), arXiv:1903.08644. https://arxiv.org/pdf/1903.08644
- Paea, Katsanos, and Bulivou (2022). DOI 10.1080/10447318.2022.2112077
- Nawaz (2012). https://research-api.cbs.dk/ws/files/58892620/Ather_Nawaz_2012.pdf
- Nielsen Norman Group, Card Sorting vs. Tree Testing. https://nngroup.com/articles/card-sorting-tree-testing-differences
- Nielsen Norman Group, Interpreting Tree Test Results. https://nngroup.com/articles/interpreting-tree-test-results/
- Smashing Magazine (2013), e-commerce navigation study. https://www.smashingmagazine.com/2013/11/guidelines-navigation-categories-ecommerce-study
- Neusesser and Sunwall, Error-Message Guidelines, NN/g. https://www.nngroup.com/articles/error-message-guidelines/
- Baymard Institute, Mobile Forms: Avoid Inline Labels. https://baymard.com/blog/mobile-forms-avoid-inline-labels
- W3C, Understanding SC 3.3.2 Labels or Instructions. https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions
- W3C, Understanding SC 3.3.3 Error Suggestion. https://w3.org/WAI/WCAG21/Understanding/error-suggestion
- Cowan (2001), The magical number 4 in short-term memory. https://pubmed.ncbi.nlm.nih.gov/11515286/
- Sweller (1988), Cognitive Science 12(2), 257-285 (DOI unconfirmed).
- Nielsen Norman Group, Minimize Cognitive Load. https://www.nngroup.com/articles/minimize-cognitive-load/
- Hick-Hyman law (secondary summary). https://en.wikipedia.org/wiki/Hick%27s_law
- Cognitive load measurement review (2024). https://arxiv.org/abs/2402.11820
- Extraneous cognitive load instrument (2024), Heliyon. https://doaj.org/article/e84ec60dc0564af488c0c05ded27d741
- Budiu, Interaction Cost: Definition, NN/g. https://www.nngroup.com/articles/interaction-cost-definition/
- Sauro (2011), Clicks don't really matter. https://measuringu.com/?p=90
- Card, Moran, and Newell (1980), Keystroke-Level Model (secondary summary). https://en.wikipedia.org/wiki/Keystroke-level_model
- IxDF, The Hick-Hyman Law. https://ixdf.org/literature/article/the-hick-hyman-law-an-argument-against-complexity-in-user-interface-design
- Penn State, Fitts' law and menus. https://acs.ist.psu.edu/courses/ist230-fall2000/Fitts_law_and_menus.html
- Available but Not Usable, arXiv 2609.28672. https://arxiv.org/pdf/2609.28672
- Nielsen Norman Group, Recognition and Recall. https://www.nngroup.com/articles/recognition-and-recall/
- Nielsen Norman Group, 10 Usability Heuristics. https://www.nngroup.com/articles/ten-usability-heuristics/
- Nielsen Norman Group, Recognition vs. Recall (video). https://www.nngroup.com/videos/recognition-vs-recall/
- Norman, Schwartz, and Shneiderman (1984), Memory for Menus. https://lccd.umiacs.umd.edu/node/17294
- Badre and Morris, transition from menus to commands. https://repository.gatech.edu/entities/publication/5029ea30-bf1e-4f6c-8d44-93d24eca4d44
- Franzke, CHI '95. https://chi1995.chistatic.hosting.acm.org/proceedings/papers/mf_bdy.htm
- Nielsen (2006), Progressive Disclosure. https://www.nngroup.com/alertbox/progressive-disclosure.html
- Nielsen Norman Group, Training Wheels in User Interfaces. https://www.nngroup.com/alertbox/training-wheels.html
- Carroll and Rosson (1987), training wheels, CHI '87 (URL not verified).
- Carroll and Rosson (1987), The Paradox of the Active User (summary). https://www.nngroup.com/articles/paradox-of-the-active-user/
- W3C, Disclosure (Show/Hide) Pattern. https://www.w3.org/WAI/ARIA/apg/patterns/disclosure
- UserTesting, Making Your Icons User-Friendly. https://www.usertesting.com/blog/user-friendly-ui-icons/
- Nielsen Norman Group, Icon Usability. https://www.nngroup.com/articles/icon-usability/
- Nielsen Norman Group, How to Test Digital Icons. https://www.nngroup.com/articles/how-to-test-digital-icons/
- Wiedenbeck (1999), Behaviour & Information Technology (secondary summaries only).
- W3C, Understanding SC 1.1.1 Non-text Content. https://www.w3.org/WAI/WCAG21/Understanding/non-text-content
- International Journal of Human-Computer Studies (2026), icon aesthetics and familiarity study (authors and URL not captured).
- Multimodal Technologies and Interaction (2018), flat versus skeuomorphic icons. https://doaj.org/article/73ebc2c455b6449daee89731bd5a9da7

## Open questions

- A screen review cannot establish findability. Without a prototype or tree test, the navigation and structure parts reflect plausibility only. Evidence on breadcrumbs is thin.
- Chunk limits come from Cowan's estimate for unrelated items, not from studies of screens. The "about 9 items" and "more than 5 decisions" breakpoints are judgment calls.
- The step-ratio cut-offs (1.1, 1.3, 1.6, 2.0) and the 12-word flag are judgment calls. Click counts explain only part of task time, and the "3-click rule" is unsupported.
- The verb-led button rule and the two-level disclosure limit rest on practitioner guidance, not controlled studies.
- The icon figures (88%, 60%, 34%) come from a vendor report, and no source tests icon style consistency against task performance.
- Whether recognition-based designs always beat recall for expert users is not settled.
