# Spacing Consistency

> Measures whether gaps between elements follow a coherent, repeated spacing scale.

## What it measures

- Distinct gap values between sibling elements, cards, list rows, form fields, and section blocks, compared against a small repeated set of values.
- Whether gaps that play the same structural role (for example, between label and input, or between cards in a grid) use the same value on every screen.
- Whether larger gaps are consistently larger than smaller ones, so that spacing signals hierarchy (within-group gap < between-group gap).
- Whether gaps stay consistent across breakpoints, or whether grouping collapses when the layout scales down.

## Research basis

- Proximity is a strong grouping cue: items close together are perceived as one group, and proximity can override similarity cues such as color or shape. Harley, A. (2020). "Gestalt Proximity." Nielsen Norman Group. https://www.nngroup.com/articles/gestalt-proximity/
- Scaling down to smaller devices can shrink or enlarge gaps and break the groupings the layout relied on. Harley (2020), same source.
- Grouping gaps must be meaningful to help. Splitting 12 form fields into three groups made the form feel less daunting, but only when the groups were meaningful. Harley (2020), same source.
- Spacing is a user-adjustable property that content must survive. WCAG 2.2 SC 1.4.12 (Text Spacing, Level AA) requires no loss of content or functionality when users set line height to at least 1.5x, paragraph spacing to at least 2x, letter spacing to at least 0.12x, and word spacing to at least 0.16x of font size. W3C. "Understanding SC 1.4.12: Text Spacing." https://www.w3.org/WAI/WCAG22/Understanding/text-spacing
- Visual search for icons is affected by the spacing between them; a CHI 2004 paper manipulated icon spacing and measured search times. Venue confirmed as CHI 2004, Vienna; title and authors not verified (see Open questions). https://hci.rwth-aachen.de/materials/conferences/CHI2004/1p695.pdf
- Design-system practice (for example, Atlassian's 8px base unit and Microsoft Azure DevOps' 4px grid with a small set of common values) treats a limited, repeated scale as the mechanism for consistency. These are practitioner sources, not studies.

## Scoring method

1. Take a full-page screenshot at desktop width and note the viewport width.
2. Identify the repeating component types on the screen: cards, list rows, form groups, section blocks, toolbars, and navigation items.
3. For each component type, measure the padding, margin, and gap values between its elements. Use browser DevTools computed styles, or read the design tokens if available.
4. Record each distinct value (in px or rem) and the number of times it occurs.
5. Check whether the values fall on a single base scale (for example, a 4px or 8px multiple, or a short token list). Count values that fall off the scale.
6. Check that structurally equivalent gaps match across component instances and that within-group gaps are smaller than between-group gaps.
7. Repeat steps 3 to 6 at a narrow phone width and note any gaps that collapse or grow out of proportion.
8. Record: number of distinct gap values, percentage on-scale, count of inconsistent equivalent pairs, and any grouping failures per breakpoint. Score with the rubric.

## Scoring rubric

- **0**: No discernible scale. Gaps are arbitrary, and equivalent elements use different values on the same screen. Grouping is unclear.
- **1**: Scale exists in intent but is broken often. Many off-scale values, and grouping is frequently ambiguous.
- **2**: Visible inconsistency. Several equivalent gaps differ, or within-group and between-group gaps are often similar.
- **3**: Mostly coherent. A small set of values covers most gaps, with a few off-scale exceptions that do not change grouping.
- **4**: Coherent scale. Nearly all gaps are on a single base scale, equivalent gaps match, and grouping is clear at desktop and phone widths.
- **5**: Exemplary. A documented, limited scale governs every gap, grouping holds across breakpoints, and spacing still works when users apply WCAG 1.4.12 overrides without content loss.

## Automated checks (optional)

Semi-automated only: a script that reads computed `margin`, `padding`, and `gap` values for visible elements, counts distinct values, and flags those not divisible by the base unit. It can detect scale drift and off-scale values. It cannot judge whether gaps group the right elements, so grouping must be checked manually. WCAG 1.4.12 overrides can be tested with a bookmarklet or stylesheet that applies the four minimum values, then checking for clipping or overlap; this tests resilience, not scale consistency.

## Common failure patterns

- Arbitrary one-off values (for example, 13px, 7px, 22px) scattered across components, so no scale is recognizable. Design-system sources describe this as breaking rhythm, but no study measures its effect.
- Gaps that do not differ between groups and within groups, so proximity fails to separate sections (Harley, 2020).
- Scaling down that shrinks inter-group gaps until groups merge, or pushes items apart until they read as separate (Harley, 2020).
- Equivalent components using different padding in different views, usually from copy-pasted styles.
- Spacing that breaks when users increase text spacing, causing clipping or overlap (WCAG 2.2 SC 1.4.12).

## Sources

1. Harley, A. (2020). Gestalt Proximity. Nielsen Norman Group. https://www.nngroup.com/articles/gestalt-proximity/
2. W3C. Understanding SC 1.4.12: Text Spacing (WCAG 2.2). https://www.w3.org/WAI/WCAG22/Understanding/text-spacing
3. CHI 2004, Vienna. Paper on icon spacing and visual search (title and authors not verified). https://hci.rwth-aachen.de/materials/conferences/CHI2004/1p695.pdf

## Open questions

- The CHI 2004 paper: only the venue was confirmed. Its title, authors, and findings could not be read from the PDF, so it is not cited for a specific result.
- No controlled study was found that measures user outcomes from spacing-scale consistency specifically. The scale requirement, the 4px/8px base-unit guidance, and the "limited set of values" rule are design-practice judgment calls, not research-backed thresholds.
- The 0 to 5 anchors, including the on-scale percentage and any cutoff for "mostly coherent," are judgment calls.
- WCAG 1.4.12 concerns user overrides, not authored spacing, so it is used here only as a resilience check.
