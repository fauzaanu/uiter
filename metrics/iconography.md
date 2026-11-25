# Iconography

> Measures whether icons are recognizable, consistent in style, and paired with labels where meaning is ambiguous.

## What it measures

- **Recognizability:** each icon's meaning is clear to a first-time user in its on-screen context, without hovering or guessing.
- **Label pairing:** icons whose meaning is not standard (most app-specific actions) have visible text beside them, not only on hover or in a tooltip.
- **Accessible naming:** every icon-only control exposes a text name that states its function, and purely decorative icons are hidden from assistive technology.
- **Style consistency:** icons on one screen and across the product share one stroke weight, corner treatment, fill style, size grid, and perspective.
- **Semantic consistency:** the same icon is never reused for different actions, and one action does not appear under different icons.

## Research basis

- Icons without labels are often misread. In a remote test of 190 Android app icons with 35 users, predicted tap outcomes were correct 88% of the time for labeled icons, 60% for unlabeled common icons, and 34% for unlabeled app-specific icons. Source: UserTesting, "Making Your Icons User-Friendly: A Guide to Usability in UI Design" (vendor report, not peer-reviewed; figures not independently verified).
- Recognition depends on context, not the icon alone. NN/g reports that simple shapes shown without labels were recognized unevenly, and that icon testing should be done in place within the interface. Source: Nielsen Norman Group, "Icon Usability," https://www.nngroup.com/articles/icon-usability/ ; "How to Test Digital Icons," https://www.nngroup.com/articles/how-to-test-digital-icons/
- Labels improve learning and retention of icon-based commands. Wiedenbeck (1999), "The use of icons and labels in an end user application program: An empirical study of learning and retention," *Behaviour & Information Technology*. Known only from secondary summaries: labeled icons performed about as well as text labels alone and better than icons alone (60 novice undergraduates, email program). Original text not reviewed.
- Functional icons need a text alternative describing their function, not their appearance. W3C, "Understanding SC 1.1.1: Non-text Content (Level A)," https://www.w3.org/WAI/WCAG21/Understanding/non-text-content . Decorative icons are hidden from assistive technology.
- Icon style familiarity affects perceived quality more than icon consistency is shown to affect usability. Peer-reviewed IJHCS study (2026; authors and volume not verified from the search snippet) reports that familiarity with icon style is the strongest predictor of aesthetic appeal, and that the aesthetic-usability effect for icons is weak once other factors are controlled.
- Flat versus skeuomorphic style did not change recognizability, task time, or error counts, though users rated flat icons as more usable. Source: *Multimodal Technologies and Interaction*, 2018 (authors and page range not verified from the snippet; https://doaj.org/article/73ebc2c455b6449daee89731bd5a9da7).

## Scoring method

1. Take a full-screen screenshot at 100% in the default theme, then repeat in the dark theme if one exists.
2. List every icon on screen. Mark each as icon-only (no visible text), icon-with-label, or decorative.
3. For each icon-only control, cover the icon and ask a reviewer unfamiliar with the product to name its action in five seconds. Record "clear", "guessed", or "wrong".
4. For each icon whose meaning is not a common standard (for example search, close, menu, or home), check for visible text beside it. Record "labeled" or "unlabeled".
5. Inspect the icon set: count distinct stroke weights, corner radii, fill styles, and grid sizes. Record the number of distinct styles.
6. Compare icons that share a function across the screen and across two other screens. Record any icon reused for different actions and any action shown with different icons.
7. Check the accessible name of each icon-only control (inspect the accessibility tree or use the automated check below). Record "named", "generic" (for example "button" or an icon file name), or "missing".
8. Score using the rubric. Note the screen name and the list of failing icons.

## Scoring rubric

- **0:** Most icon-only controls are unclear or wrong, no ambiguous icon has a label, and icons mix three or more styles on one screen.
- **1:** Several icons are guessed or wrong, ambiguous icons are mostly unlabeled, and some controls have no accessible name.
- **2:** Half or more of the icons are clear, but two or more ambiguous icons are unlabeled, or two or more icons conflict in meaning.
- **3:** Most icons are clear. Ambiguous icons are labeled. One style is mostly used, with at most one outlier. Icon-only controls are named, though some names are generic.
- **4:** All icons are clear or labeled. One style set is used throughout the screen. Every icon-only control has a specific accessible name. Decorative icons are hidden from assistive technology.
- **5:** Icons are clear in context without labels for common actions. Ambiguous icons are labeled. Style and meaning match across the product. Icon-only controls expose specific names and have a visible focus state.

Anchors for labeling: "ambiguous" means the icon is not a widely standard symbol for its action. The 88%/60%/34% figures are the only numeric evidence used here; they are a vendor result and should be treated as an indicator, not a threshold.

## Automated checks (optional)

axe-core (Deque) flags icon-only buttons and links with no accessible name (rules such as `button-name`, `link-name`, `image-alt`). It can confirm a name is present, but not whether the name is specific or whether the icon is recognizable. Recognition, label pairing, and style consistency require manual review.

## Common failure patterns

- Icon-only toolbars with app-specific glyphs, where the Wiedenbeck (1999) and UserTesting results predict the most misreads.
- Labels shown only on hover or in tooltips, which NN/g states adds interaction cost and fails on touch devices.
- Icon sets mixing filled, outlined, and multi-color glyphs, which the consistency literature does not show to hurt usability but practitioners and familiarity findings flag as a source of confusion.
- Icon-only controls whose accessible name is the file name or a generic word such as "icon" or "button", which fails WCAG 1.1.1 in practice.
- The same glyph reused for different commands, such as a gear for both settings and export.
- Decorative icons exposed to assistive technology, creating noise for screen-reader users.

## Sources

1. UserTesting. "Making Your Icons User-Friendly: A Guide to Usability in UI Design." https://www.usertesting.com/blog/user-friendly-ui-icons/
2. Nielsen Norman Group. "Icon Usability." https://www.nngroup.com/articles/icon-usability/
3. Nielsen Norman Group. "How to Test Digital Icons." https://www.nngroup.com/articles/how-to-test-digital-icons/
4. Wiedenbeck, S. (1999). "The use of icons and labels in an end user application program: An empirical study of learning and retention." *Behaviour & Information Technology*. (Secondary summaries only.)
5. W3C. "Understanding SC 1.1.1: Non-text Content (Level A)." WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/non-text-content
6. *International Journal of Human-Computer Studies* (2026). Icon aesthetics and familiarity study. (Authors and URL not captured from search.)
7. *Multimodal Technologies and Interaction* (2018). Flat versus skeuomorphic icon study. https://doaj.org/article/73ebc2c455b6449daee89731bd5a9da7

## Open questions

- The 88%/60%/34% figures come from a vendor blog and have not been checked against the original report.
- Wiedenbeck (1999) was seen only through secondary summaries. The exact retention results and sample need checking against the Taylor & Francis original.
- The 2026 IJHCS and 2018 MTI sources were identified from search snippets; authors, volume, and page details are unverified.
- No source found tests style consistency against task performance. The "one style" anchors in the rubric are a judgment call.
- Whether an icon is "widely standard" has no numeric definition; the labeling threshold is a reviewer judgment.
- The axe-core rule names are from general knowledge, not from the searches.
