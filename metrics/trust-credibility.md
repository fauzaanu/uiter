# Trust and Credibility

> Scores whether the visual quality, details, and signals on a screen make the product feel reliable and legitimate.

## What it measures

- Visual polish and consistency: a coherent type scale, spacing, colour use, and imagery across the screens a reviewer sees.
- Craft details: no visible typos, broken images, clipped or overlapping text, misaligned elements, or placeholder content such as lorem ipsum.
- Trust signals that fit the context: security or payment cues on checkout, identifiable contact or company information where the task calls for it, and believable real-looking content rather than obvious filler.
- Stability cues: no layout shifts while loading, no error states left unhandled, and no dead-end links or buttons.
- Fit to purpose: the level of visual formality matches what the product is for (a bank and a game should not look alike).

## Research basis

- Visual appeal shapes first impressions quickly. Ratings of web page visual appeal made from 50 ms exposures correlated strongly with ratings from 500 ms exposures, which the authors read as a 50 ms window for a first impression. Lindgaard, Fernandes, Dudek and Brown (2006), *Behaviour & Information Technology*, 25, 115-126. https://doi.org/10.1080/01449290500330448
- Higher aesthetic treatment of identical content raised perceived credibility, and the effect appeared within the first few seconds of viewing. Robins and Holmes (2008), "Aesthetics and credibility in web site design." https://makinggood.ac.nz/media/1276/robinsholmes_2008_aestheticsandcredibilityinwebdesign.pdf
- Users evaluate credibility largely from surface cues such as visual design, and do not apply rigorous criteria when judging a site. The Stanford Persuasive Technology Lab guidelines report that visual design should fit the site's purpose and that ease of use and usefulness both contribute to credibility. Fogg (2002), "Stanford Guidelines for Web Credibility." https://credibility.stanford.edu/guidelines
- Aesthetics and credibility are linked but the effect varies by context. Robins and Holmes report the link; the strength of the effect across site types, cultures, and aesthetic dimensions is not settled by the results I could check. See Open questions.

## Scoring method

1. Open the screen at a common desktop and a common phone width. Note the first impression within a few seconds.
2. Zoom into the main content and check typography: font count (more than three families is a warning), size steps, line spacing, and alignment to a consistent grid.
3. Check craft details: scan for typos, placeholder text, broken or missing images, overlapping or clipped text, and misaligned controls. Count each instance.
4. Check trust signals against the screen's task. For any screen that collects personal or payment data, confirm a clear security or privacy cue and a visible path to help or contact.
5. Check stability: note any visible loading flicker or layout jump, and trigger one error or empty state if the screen allows it. Record whether it is handled.
6. Check fit to purpose: write one sentence on whether the visual formality suits the product's category.
7. Record counts and one-line observations per check. Assign the score from the rubric using the most severe finding that is not offset by an equal strength.

## Scoring rubric

- 0: Severe failure. Broken layout or images on the main path, visible placeholder or error text on key screens, or a payment or login screen with no credible cue.
- 1: Several visible defects (three or more typos or broken elements) or the product looks clearly unfinished. Trust cues are absent where needed.
- 2: Recurring defects that a user would notice within a minute. Visual system inconsistent (more than three type families, mixed spacing scales). Sensitive screens have weak cues.
- 3: Mostly coherent. One or two minor defects. Sensitive screens have adequate cues. Some stability or formality mismatch.
- 4: Coherent system with no visible defects on the main path. Appropriate cues on sensitive screens. Stable loading and handled errors.
- 5: Exemplary. Coherent system, no defects across the screens reviewed, cues calibrated to the task, and stable behaviour including error and empty states.

Anchors reference counts from the Scoring method. Where a count is a judgment threshold rather than a published one, see Open questions.

## Automated checks (optional)

None reliable; manual review only. Broken-image and console-error scans exist, but they cannot judge typographic consistency, tone, or whether a trust cue fits the task.

## Common failure patterns

- Polished hero areas paired with broken or placeholder content further down, which undercuts the first impression (Lindgaard et al., 2006, measure only the first impression, not later screens).
- Visual inconsistency across screens that makes the product look like several products stitched together (Robins and Holmes, 2008, on aesthetic treatment and credibility judgments).
- Trust cues copied from unrelated categories, such as a corporate look on a casual tool, which Fogg (2002) notes does not automatically add credibility.
- Sensitive flows (checkout, sign-in) without any visible security or contact signal.
- Unhandled error or empty states that show raw technical text.

## Sources

1. Lindgaard, G., Fernandes, G., Dudek, C., and Brown, J. (2006). Attention web designers: You have 50 milliseconds to make a good first impression! *Behaviour & Information Technology*, 25, 115-126. https://doi.org/10.1080/01449290500330448
2. Robins, D., and Holmes, J. (2008). Aesthetics and credibility in web site design. https://makinggood.ac.nz/media/1276/robinsholmes_2008_aestheticsandcredibilityinwebdesign.pdf
3. Fogg, B.J. (2002). Stanford Guidelines for Web Credibility. A Research Summary from the Stanford Persuasive Technology Lab. https://credibility.stanford.edu/guidelines

## Open questions

- Robins and Holmes (2008): the search result showed a file name and a "sciencedirect" banner, but I did not confirm the venue or page numbers from the full text.
- Lindgaard et al. (2006) is a journal article, not a CHI paper. The 50 ms claim is taken from the abstract and secondary coverage (Nature news). The full text was not read.
- The Stanford guidelines are from 2002 and the lab's site was last updated in 2007. Findings are dated and were not re-tested on modern products.
- Other studies surfaced in search (a 526-participant cross-cultural mobile study on classical vs. expressive aesthetics, and a Taiwanese payment-page study on visual complexity) suggest effects vary by site type and culture. I did not verify their venues or URLs, so they are not cited.
- No source I checked tests typos or broken links directly against credibility. The rubric's count thresholds (one, three, and more-than-three defects) and the "more than three type families" limit are judgment calls, not research-backed values.
- Fogg's Prominence-Interpretation Theory (2003) is referenced in search results, but I did not read its text, so it is not cited.
