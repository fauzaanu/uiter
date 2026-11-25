# Localization Readiness

> Measures whether the layout and components tolerate longer text, right-to-left scripts, and varied date and number formats.

## What it measures

- Whether text containers (buttons, labels, tabs, table headers, badges) keep their content readable when strings run roughly 30 to 40 percent longer than the source language.
- Whether containers use flexible sizing (min-width, wrapping, growing rows) rather than fixed widths that clip or overflow.
- Whether the layout mirrors correctly when the base direction is right-to-left, including order of navigation, progress indicators, and leading icons, while non-directional items (clocks, play symbols, logos, refresh icons) are left unflipped.
- Whether mixed-direction content (Latin numerals, brand names, or code inside RTL text) stays in the correct order and does not break alignment.
- Whether dates, times, and numbers are rendered from locale-aware patterns rather than hard-coded formats, so day/month order, separators, and digit grouping can vary without breaking the layout.

## Research basis

- Text expansion is a recurring cause of layout breakage in localized UIs, and the expansion must be tested rather than assumed. Roughly 30 percent expansion for German relative to English, and about 40 percent as a stress test, are common practitioner figures. They rest on vendor and industry guidance rather than peer-reviewed measurement and are used here only as test targets.
- Pseudo-localization can be applied before translation exists, by padding strings and substituting characters, to expose clipping and font problems early. Source: Microsoft Globalization, pseudolocalization methodology.
- Switching a UI to right-to-left is more than mirroring. Anvari and Woods (2024) report that the LTR-to-RTL change involves more than mirroring elements, and that Arabic typography (direction, word wrapping) affects the experience. Source: AHFE 2024 proceedings.
- Users do not agree on the direction of every UI item. Goldenberg and Tractinsky (2025), surveying 1,705 Arabic and Hebrew users on items with ambiguous direction, found that direction preferences vary by item and by language. Source: International Journal of Human-Computer Studies.
- The W3C HTML bidi guidance states that the `dir` attribute sets base direction for directionally neutral text, that `lang` must not be used to determine directionality, and that HTML5 isolates `dir` content by default, with `dir="auto"` and `<bdi>` available for user-supplied text. Source: W3C HTML bidi Note (2015).
- Date, time, and number formats differ by locale in ordering, separators, and digit grouping. CLDR (Unicode TR35) defines locale patterns for these, and implementations should resolve them from locale data rather than fixed strings. Source: Unicode TR35 Dates and Numbers.
- Core usability principles hold across cultures, but the details differ, so localization should change details without weakening the underlying structure. Source: Nielsen Norman Group, "International usability details differ."

## Scoring method

1. Identify the base screen and one or more stress conditions: (a) a long-string locale or pseudo-localized copy padded about 40 percent; (b) an RTL rendering (set `dir="rtl"` on the root or switch the OS/app locale); (c) a non-default date, time, and number locale (for example, a day-first format and a comma decimal separator).
2. Under condition (a), inspect every text-bearing component: primary and secondary buttons, navigation items, tabs, form labels, table headers, badges, and tooltips. Record any clipped, truncated without an affordance, overlapping, or wrapped-into-another-element case.
3. Measure the fixed-width risk with a computed-style check: list elements whose `width` is set in px and whose text is not allowed to wrap. Each is a finding even if it currently fits English.
4. Under condition (b), verify that directional layout reverses: primary navigation order, back/forward arrows, progress direction, and leading icons on list items. Confirm that non-directional items (clocks, media controls, logos, refresh) are not flipped.
5. Check mixed content in RTL: a Latin brand name, a number, and a URL in an RTL sentence should keep their internal order and sit at the correct edge without shifting neighboring elements.
6. Under condition (c), confirm dates, times, and numbers come from locale formatting calls and not from literal strings. Look for fixed-width date fields or columns that clip the longer pattern.
7. Record each observation with the component, the stress condition, the screenshot, and severity (blocks use, cosmetic, or none). Score the screen against the rubric.

## Scoring rubric

Scale: 0 = severe failure, 5 = exemplary.

- **0**: Under at least one stress condition, primary actions or navigation are unreadable, clipped, or unreachable; RTL is not supported at all; dates or numbers are hard-coded and break the layout.
- **1**: Core flows fail under long strings or RTL; several components use fixed widths that clip; mirroring is partial and breaks reading order.
- **2**: Primary flows survive, but multiple secondary components clip or overlap at about 30 percent expansion; RTL mirrors most elements but leaves visible errors in navigation or mixed content.
- **3**: Primary components tolerate about 30 percent expansion with at most minor wrapping; RTL reverses directional layout correctly on the screen; one or two non-critical items show awkward mixed-direction ordering.
- **4**: Components tolerate about 40 percent expansion without clipping; non-directional icons are correctly left unflipped; mixed content is correctly isolated; date and number formats are locale-driven and fit their containers.
- **5**: Passes all three stress conditions with no clipping, overlap, or ordering errors; text containers use flexible sizing throughout; direction and locale behavior are verified against both pseudo-localized and real translated strings.

## Automated checks (optional)

Pseudo-localization tools (for example, the Unity Localization Expander method or Microsoft-style padding generators) can produce expanded strings for a screenshot run, and a DOM script can list fixed-width text containers via computed styles. Neither reliably detects mirroring errors, icon direction, or whether a date format is correct for its locale. Treat automated output as a candidate list for manual review.

## Common failure patterns

- Fixed-width buttons and tabs that clip after translation, which is the most frequent failure reported in localization testing.
- Mirroring applied to everything, including clocks, play icons, and refresh symbols that research and platform guidance say should stay unflipped.
- Mixed Latin numerals or brand names inside RTL text that reorder punctuation and break alignment.
- Hard-coded date and number strings that ignore locale ordering and separators.
- Testing only with English, so long-string and RTL defects surface only after release.

## Sources

1. Goldenberg, N. and Tractinsky, N. (2025). "Exploring amBiDiguity: UI item direction interpretation by Arabic and Hebrew users." International Journal of Human-Computer Studies. https://cris.iucc.ac.il/en/publications/exploring-ambidiguity-ui-item-direction-interpretation-by-arabic-/
2. Anvari, A. and Woods, (co-author not verified) (2024). "Localizing Graphical User Interfaces for Right-to-Left Languages: A Practical Study." AHFE International Conference Proceedings. https://openaccess.cms-conferences.org/publications/book/978-1-964867-19-9/article/978-1-964867-19-9_24
3. W3C (2015). "HTML bidi" Working Group Note. https://www.w3.org/TR/2015/NOTE-html-bidi-20150721/
4. Unicode Consortium. "Unicode Technical Standard #35: Locale Data Markup Language, Part 4: Dates" and "Part 3: Numbers." https://www.unicode.org/reports/tr35/tr35-78/tr35-dates.html and https://www.unicode.org/reports/tr35/tr35-78/tr35-numbers.html
5. Nielsen Norman Group. "International Usability: Details Differ." https://www.nngroup.com/articles/international-usability-details-differ/
6. Microsoft Globalization. "Pseudolocalization." https://learn.microsoft.com/globalization/methodology/pseudolocalization

## Open questions

- The 30 percent German and 40 percent stress-test figures are practitioner numbers, not peer-reviewed measurements. The rubric thresholds are a judgment call anchored to them.
- Goldenberg and Tractinsky's abstract and listing were reviewed, not the full paper. The claim about variation by item and language is taken from the summary and should be checked against the full text.
- Anvari and Woods' co-author name was not verified from the search results; only the first author and title were confirmed.
- No W3C document on date and number formatting was found; the date and number claims rely on Unicode TR35 instead.
- No peer-reviewed study on text expansion and layout breakage was found. The evidence base for that criterion is industry practice.
- Icon mirroring rules are platform-specific (Material and Microsoft guidance differ in detail) and are not cited here; the rubric treats them as a judgment call.
