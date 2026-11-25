# Affordances

> Affordances measures whether interactive elements look like what they do and non-interactive ones do not invite clicks.

## What it measures

- Every control a user can act on (button, link, toggle, tab, input, draggable item) carries a visual cue that it is operable: a button-like shape, a text link style, a cursor or hover state, a visible handle, or a control-specific glyph.
- Static content (headings, body text, labels, stat tiles, decorative cards) does not look like a control: no button-like fill or border, no underline that mimics a link, no hover affordance.
- Visual cues match the action: a chevron implies expansion, a pencil implies editing, a trash icon implies deletion, and a link-styled element implies navigation.
- Interactive elements are distinguishable from their neighbours when they compete for attention, rather than relying on an identical look for links, buttons and plain text.
- Disabled controls look disabled, and states (pressed, selected, focused) are visibly different from the resting state.

## Research basis

- Affordances are perceived through cues, and designers control perceived rather than real affordances in screen interfaces. Norman's own clarification is that the term should have been "perceived affordance," because design depends on what the user perceives. Norman, D. A. (1999), "Affordance, Conventions, and Design," *Interactions* 6(3). https://cs.uwaterloo.ca/~jianzhao/cs449-649/files/affordance-norman99.pdf
- Norman later distinguishes signifiers as perceivable indicators of how an object should be used, and notes that a signifier must be perceivable to work. Norman, D. A. (2013), *The Design of Everyday Things*, revised edition. Cited via secondary course material only; not independently verified against the book text.
- Users need to tell static content from clickable areas, and flat design often removes the strongest clickability cues (3-D effects, shadows, rounded rectangular shapes). Nielsen Norman Group, "Clickable Elements." https://www.nngroup.com/articles/clickable-elements/ (author and date not confirmed from the search result.)
- Shape-changing buttons were tested with 15 participants across 13 designs, examining how affordance and feedback shape perceived operability. Tiab, J. & Hornbæk, K., CHI 2016. https://www.kasperhornbaek.dk/papers/CHI2016-Affordances.pdf (author attribution taken from the search summary; the full paper was not read.)
- Added visual signifiers increased users' sense of possible inputs beyond a simple tap and reduced perceived mental effort; users preferred interfaces with added signifiers to a baseline. Dissertation, University of Lille, 2023. https://pepite-depot.univ-lille.fr/LIBRE/EDMADIS/2023/2023ULILB045.pdf (abstract read via search summary only.)
- Button size shaped which operations users judged appropriate, with users perceiving operability cued by the virtual buttons. Study published in *Journal of the Society of Mechanical Engineers* / J-STAGE, 2014, vol. 61 no. 3. https://www.jstage.jst.go.jp/article/jssdj/61/3/61_3_1/_article/-char/ja (small study; full text not read.)

## Scoring method

1. Take a full-page screenshot or live view at desktop width, then review at phone width.
2. List every interactive element by inspecting the DOM or by tabbing through the page, so that hidden or icon-only controls are included.
3. For each interactive element, record its visual class: button-like (filled or bordered), text link, icon, input field, or other. Note whether it has a visible affordance cue (shape, border, underline, icon, or chevron).
4. Hover each element on desktop and note whether the cursor changes and whether a hover state appears. Mark "not testable" for touch-only views.
5. List every non-interactive element that is styled like a control (button-like fill, underlined text, card with a shadow). Count these as false affordances.
6. Count the elements that are interactive but have no visible cue, and the elements that are non-interactive but carry a control cue.
7. Record the observation as: interactive without cue (count), false affordance (count), and cue-to-action mismatches (count), each with a screenshot reference.
8. Map the counts to the rubric below.

## Scoring rubric

- **0**: Most controls are indistinguishable from static content, or most static content looks clickable. Users cannot tell what can be operated.
- **1**: Controls are identifiable only after trial, or multiple false affordances mislead the user on the main screen.
- **2**: The primary action and navigation are cued, but secondary controls (icons, toggles, tabs) rely on guessing, or several false affordances exist.
- **3**: Most controls carry an adequate cue and static content mostly does not look interactive. Occasional icon-only controls or mismatched cues remain.
- **4**: Every interactive element has a consistent cue, states are visible on hover or focus, and at most one minor false affordance appears.
- **5**: Every control is clearly operable on first view, cues match actions, disabled and active states are explicit, and no static content invites a click.

## Automated checks (optional)

None reliable; manual review only. Partial aid: a script can enumerate elements with pointer cursors or click handlers and flag them against computed border, background and underline styles. It cannot judge whether a cue is recognisable or whether an element is visually confusable with a control, so results need manual confirmation.

## Common failure patterns

- Flat design removes the shadow, border and fill that signal clickability, leaving text-only buttons that look like labels. (Nielsen Norman Group, "Clickable Elements.")
- Cards and stat tiles are styled like buttons, creating false affordances that erode trust. (Interaction pattern noted in practitioner sources; not independently tested.)
- Icon-only controls with no label or cue force users to guess; signifiers that are not perceivable fail to work. (Norman 1999; Norman 2013.)
- Many similar-looking boxes compete, so users cannot pick out the clickable one. (Nielsen Norman Group, "Clickable Elements.")
- Controls lack hover, focus or pressed states, so the user gets no sign they are operable. (Lille dissertation 2023 suggests added visual signifiers reduce perceived effort; direct effect on hover states unverified.)

## Sources

1. Norman, D. A. (1999). Affordance, Conventions, and Design. *Interactions*, 6(3). https://cs.uwaterloo.ca/~jianzhao/cs449-649/files/affordance-norman99.pdf
2. Norman, D. A. (2013). *The Design of Everyday Things*, revised and expanded edition. Book; no direct URL verified.
3. Nielsen Norman Group. Clickable Elements. https://www.nngroup.com/articles/clickable-elements/
4. Tiab, J. & Hornbæk, K. (2016). Shape-changing buttons study. CHI 2016. https://www.kasperhornbaek.dk/papers/CHI2016-Affordances.pdf
5. Dissertation (2023). University of Lille. https://pepite-depot.univ-lille.fr/LIBRE/EDMADIS/2023/2023ULILB045.pdf
6. Journal of the Society of Mechanical Engineers, vol. 61 no. 3 (2014). J-STAGE. https://www.jstage.jst.go.jp/article/jssdj/61/3/61_3_1/_article/-char/ja

## Open questions

- Only one controlled study (Tiab & Hornbæk 2016) was found in the search results that tests perceived affordances of interface controls directly. The 2014 J-STAGE study and the 2023 Lille dissertation are small or unread in full.
- An online checkout study (Istan, thesis, 70 students) reported fewer clicks with a high-affordance interface. No URL or institution was verified, so it is excluded from the research basis.
- The 0 to 5 anchors, and the threshold between "some" and "most" elements, are judgment calls rather than research-backed values.
- No numeric threshold for minimum cue strength was found. The rubric therefore does not cite one.
- Authors and date for the NN/g "Clickable Elements" article were not confirmed from the search result.
