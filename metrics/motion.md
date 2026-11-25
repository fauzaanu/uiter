# Motion

> Measures whether animation is purposeful, brief, and respectful of reduced-motion preferences.

## What it measures

- Every animated element has a visible reason to move: confirming an action, showing a state change, or explaining a spatial relationship. Decorative motion that carries no information is a finding.
- Feedback animations (toggles, button presses, checkbox ticks) finish quickly. Screen and panel transitions stay in the sub-second range.
- Motion that the page starts on its own (carousels, autoplay, looping background effects) can be paused or stopped by the user.
- Parallax, zooms, large-area sliding, and full-screen motion are either absent or disabled when the OS reduced-motion setting is on.
- Information is not conveyed only through motion. The end state is readable and usable with motion switched off.

## Research basis

- Animation should be used sparingly and for a clear purpose, such as smooth feedback; attention-grabbing motion is both its benefit and its cost. Source: Nielsen Norman Group, "Animation Purpose in UX" (https://www.nngroup.com/articles/animation-purpose-ux/). Seen as search-result summary only; not fetched.
- Most UI animations should fall in roughly 100 to 500 ms, and the shortest duration that does not feel jarring is preferred. Animations more often run too long than too short. Source: Nielsen Norman Group, "Animation Duration" (https://nngroup.com/articles/animation-duration). Seen as search-result summary only; the figures are consistent across secondary sources but were not checked against the full article.
- Responses under about 100 ms feel instantaneous to users; this is a response-time threshold attributed to Nielsen in secondary sources. Source: same NN/g duration article, to be verified; see Open questions.
- WCAG 2.3.3 Animation from Interactions (Level AAA) requires that motion triggered by interaction can be disabled unless the motion is essential. Sufficient techniques include C39 (CSS `prefers-reduced-motion`) and SCR40 (the same query in JavaScript). Motion the page starts on its own falls under WCAG 2.2.2 Pause, Stop, Hide. Source: W3C, "Understanding SC 2.3.3" (https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions) and W3C technique C39 (https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html).
- Parallax scrolling and fast or continuous animation can trigger discomfort in people with vestibular disorders; the practical mitigation is honoring the reduced-motion setting. Source: web.dev, "Animation and motion" (https://web.dev/learn/accessibility/motion). Practitioner guidance; no controlled user study was located.
- Perceived responsiveness is affected by whether the first visible frame and the end of the transition are timed well. Source: arXiv 2508.01337, "Screencast-Based Analysis of User-Perceived GUI Responsiveness" (https://arxiv.org/pdf/2508.01337). Seen as search-result summary only.

## Scoring method

1. Open the screen in a clean session with the OS reduced-motion setting OFF. Note every element that moves on load, on hover, on click, and on scroll.
2. Trigger each interaction once and record the observed duration. Use screen recording at 60 fps or higher and count frames from first movement to rest. Duration = frames / fps. A frame-counting tool or the browser's Animations panel can substitute.
3. For each animation, record its purpose in one phrase (feedback, state change, spatial cue, decoration). Mark decorative animations as a finding.
4. Check for auto-starting motion longer than 5 seconds. Confirm a pause or stop control exists.
5. Turn the OS reduced-motion setting ON (macOS: Accessibility > Display > Reduce motion; Windows: Animation effects off). Reload and repeat steps 1 to 4. Confirm that parallax, large movement, and non-essential animation are removed or reduced to fades, and that the end state is unchanged.
6. Check that no information is available only during an animation (for example, a status message that appears only mid-transition and disappears).
7. Record: animation count, count with a clear purpose, longest duration, count of motion that ignores reduced-motion, and count of auto-starting motion without a control. Score using the rubric.

## Scoring rubric

- **0**: Severe failure. Large, looping, or parallax motion with no purpose; reduced-motion setting ignored; or information conveyed only through motion.
- **1**: Frequent decorative motion; several elements exceed 1 s without reason; reduced-motion ignored on most large animations; auto-starting motion has no control.
- **2**: Mixed. Some purposeful motion, but several animations run over 500 ms or repeat excessively; reduced-motion honored on fewer than half of large animations.
- **3**: Mostly purposeful. Most feedback animations are 100 to 300 ms and most transitions are within 500 ms; reduced-motion honored for the main transitions; one or two decorative effects remain.
- **4**: Purposeful and brief. Feedback at about 100 to 200 ms, transitions at 200 to 500 ms, every auto-starting motion has a pause control, and reduced-motion removes parallax and large movement.
- **5**: Exemplary. Every animation has a stated purpose; durations sit within 100 to 500 ms; reduced-motion produces an equivalent end state with fades or none; no information depends on motion; no animation blocks input.

## Automated checks (optional)

None reliable; manual review only. Static analysis can find `prefers-reduced-motion` in CSS or JavaScript, but cannot judge purpose, duration in context, or whether the reduced-motion branch is complete. A computed-style script can read `animation-duration` and `transition-duration`, which is useful for a first pass but misses JavaScript-driven motion.

## Common failure patterns

- Motion added as decoration on every element, drawing attention away from the content (NN/g, "Animation Purpose in UX").
- Transitions set well beyond 500 ms, so every interaction feels slower than the task requires (NN/g, "Animation Duration").
- Parallax and large-area movement left active when reduced-motion is enabled, the specific pattern web.dev identifies as a vestibular trigger.
- Reduced-motion query present in CSS but not applied to JavaScript-driven animation, so WCAG SCR40 is not met.
- Auto-playing or looping motion with no pause control (WCAG 2.2.2).
- Status or feedback shown only during a transition and gone by the time the user reads it.

## Sources

1. Nielsen Norman Group. "Animation Purpose in UX." https://www.nngroup.com/articles/animation-purpose-ux/
2. Nielsen Norman Group. "Animation Duration." https://nngroup.com/articles/animation-duration
3. W3C. "Understanding SC 2.3.3: Animation from Interactions (Level AAA)," WCAG 2.1. https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions
4. W3C. "Technique C39: Using the CSS prefers-reduced-motion query," WCAG 2.2. https://www.w3.org/WAI/WCAG22/Techniques/css/C39.html
5. web.dev. "Animation and motion" (accessibility learning module). https://web.dev/learn/accessibility/motion
6. Merz, B., Tuch, A. N., and Opwis, K. (2016). "Perceived User Experience of Animated Transitions in Mobile User Interfaces." CHI EA '16, pp. 3152-3158. ACM. Citation only; findings not verified (see Open questions).

## Open questions

- The NN/g duration figures (100 to 500 ms, roughly 100 ms for simple feedback, 200 to 300 ms for modal changes) were seen only in search summaries and secondary sites. Verify against the full NN/g article before publishing thresholds as research-backed.
- The 100 ms and 1 s response thresholds are attributed to Nielsen in secondary sources; the primary wording was not located.
- The Merz et al. CHI EA 2016 paper is the only controlled study found on mobile transition duration, but its findings were not retrieved. The 100 to 500 ms bands in the rubric are therefore a judgment call anchored on NN/g guidance, not on that paper.
- The 5-second threshold for auto-starting motion is taken from WCAG 2.2.2 (Pause, Stop, Hide) and is not stated in the 2.3.3 source.
- No user study on parallax and reduced-motion effects was located; the vestibular rationale rests on practitioner guidance.
- WCAG 2.3.3 is AAA; the rubric treats reduced-motion support as a strong expectation rather than a conformance requirement.
