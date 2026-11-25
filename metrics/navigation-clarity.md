# Navigation Clarity

> Measures whether users can tell where they are, where they can go, and how to get back.

## What it measures

- **Current-location signal:** the active top-level section, page, or step is visibly marked in primary navigation with a style that differs from its siblings, and the page heading agrees with that marking.
- **Destination visibility:** the main sections of the product are visible from the current screen as labelled items, not hidden behind unlabelled icons or ambiguous menus.
- **Return path:** every non-home screen offers a visible, predictable way back (logo or home link, breadcrumb, back link, or close control) that does not depend on the browser back button.
- **Hierarchy cues:** deep pages show their position in the structure, either as a breadcrumb trail or an equivalent cue that reaches the top-level section.
- **Programmatic current state:** the current item is exposed to assistive technology (for example `aria-current`) and is not presented as an actionable link to itself.

## Research basis

- Location indicators are often too subtle for new users, because designers who know the structure stop noticing them. Source: Nielsen Norman Group, "Navigation: You Are Here" (1).
- Marking the current top-level section with a distinct style is a simple fix. Baymard reports that 66% of desktop sites in its benchmark failed to do so (2).
- Current location should be indicated in navigation bars using an icon, text, or a changed state, and the link to the current page should be disabled so screen-reader users can detect it. Source: W3C Technique G128 (3).
- WCAG 2.4.5 Multiple Ways (Level AA) requires more than one way to locate a page within a set. WCAG 2.4.8 Location (Level AAA) requires information about the user's location, with a breadcrumb trail (G65) and current-location indication in navigation bars listed as sufficient techniques. Sources: W3C Understanding SC 2.4.5 (4) and W3C Understanding SC 2.4.8 (5).
- Breadcrumbs are most useful for visitors who land deep in a site, but they should stay secondary to primary navigation. Source: NN/g guidance as reported by secondary sources; the NN/g page itself was not verified (6).
- The empirical base is thin. A UNC thesis notes sparse empirical evidence on breadcrumbs (7).
- The "where am I" test is the closest available method: show screens from different levels without navigation and ask where the participant is and how they would get back (1).

## Scoring method

1. Choose three screens: one top-level screen, one second-level screen, and one deep screen or detail view. Open the deep screen directly from its URL, not by navigating through the product.
2. On each screen, record whether the active top-level item is marked, and how. Note whether the marking relies on colour alone.
3. Record whether the page heading or title names the section and page the user is in.
4. Count the top-level destinations visible without opening a menu. Note any destination that is hidden, unlabelled, or behind a generic "More" control.
5. Locate the return path on each non-home screen. Activate it once and confirm it lands on the expected parent.
6. In browser devtools, inspect the accessibility tree for the current item. Record whether it carries `aria-current` (or equivalent) and whether it is a non-actionable or disabled link.
7. Optional: show five screenshots to colleagues or test users, with no navigation, and ask "Where are you? How would you get back?" Record the percentage of correct answers.
8. Score three sub-dimensions (location, destinations, return path) on the rubric. The metric score is the lowest of the three, averaged across the three screens.

## Scoring rubric

- **0 (severe failure):** No current-location marking, no visible return path, and main destinations hidden or unlabelled.
- **1 (major gaps):** Location or return path is missing on most screens. Users must guess where they are or how to leave.
- **2 (partial):** Marking exists but is subtle or colour-only, or the only way back is the browser back button on most screens.
- **3 (adequate):** The current item uses a distinct style plus text or an indicator on most screens. A consistent home or back control exists. Main sections are visible. Minor gaps remain on deep pages.
- **4 (strong):** All checks pass on every tested screen, including the directly opened deep screen. A breadcrumb or equivalent shows the path. Current state is exposed to assistive technology. The where-am-I test reaches at least 80% correct (a judgement threshold, see Open questions).
- **5 (exemplary):** As 4, and the where-am-I test reaches 100% for location and return path across all depths. Current state is identifiable without colour and in the accessibility tree.

## Automated checks (optional)

None reliable; manual review only.

## Common failure patterns

- The active state is shown by colour alone or a subtle change that new users miss (1).
- Once several items share a highlight style, the active one becomes hard to spot, especially for visitors arriving from outside the site (2).
- Deep pages offer no path back to the parent section, or breadcrumbs skip levels of the hierarchy (2, as reported by secondary sources).
- Breadcrumbs are used as the only orientation aid and replace primary navigation (6).
- The current item is a live link, so screen-reader users cannot tell it is selected (3).
- The page heading and the navigation label disagree, leaving location ambiguous.

## Sources

1. Nielsen Norman Group, "Navigation: You Are Here." https://www.nngroup.com/articles/navigation-you-are-here/ (authors and year not verified)
2. Baymard Institute, highlight users' navigation scope. https://baymard.com/research-articles/highlight-users-navigation-scope (year not verified)
3. W3C, Techniques for WCAG, G128: Indicating current location within a set of Web pages. https://www.w3.org/TR/WCAG-TECHS/G128.html
4. W3C WAI, Understanding SC 2.4.5: Multiple Ways (Level AA), WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/multiple-ways
5. W3C WAI, Understanding SC 2.4.8: Location (Level AAA). https://www.w3.org/WAI/WCAG20/Understanding/location
6. Nielsen Norman Group breadcrumb guidance as summarized in secondary sources (Visa Design System, breadcrumbs usage: https://design.visa.com/components/breadcrumbs/usage/). The primary NN/g breadcrumb article was not verified.
7. UNC School of Information and Library Science, master's paper on breadcrumbs. https://ils.unc.edu/MSpapers/3305.pdf (author and year not verified)

## Open questions

- The Baymard 66% figure and the NN/g claims were taken from search summaries, not from fetched full text. Verify before relying on exact numbers.
- No controlled experiment was found that compares location-indicator designs directly. The 80% and 100% where-am-I thresholds are judgement calls, not research-backed values.
- Taking the lowest of three sub-dimensions as the metric score is a design choice, not a finding.
- WCAG 2.4.8 is Level AAA and 2.4.5 is Level AA. Confirm exact wording against the current W3C WCAG 2.2 pages, since some cited pages are older versions.
- Evidence on breadcrumb effectiveness is thin and largely expert guidance.
