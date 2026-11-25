# Perceived Performance

> Measures how fast the interface feels to respond to a user's action, independent of measured load times.

## What it measures

- Time from a user action (click, tap, keypress, submit) to the first visible acknowledgement on screen, such as a pressed state, a spinner, or a changed control.
- Whether the interface stays responsive while work is in progress: controls remain usable, and the screen does not freeze or go blank.
- Whether loading or waiting states show structure and progress, not just an indeterminate placeholder or an empty area.
- Whether content appears in a stable order, so the user can begin reading or acting before everything has finished loading.
- Whether the duration of an interaction feels proportionate to its effect, with no unexplained pauses before a response.

## Research basis

- Response-time thresholds in the Nielsen tradition: about 0.1 s feels instantaneous, 1 s keeps the user's flow uninterrupted, and about 10 s is the limit for holding attention. Nielsen, J. "Time Scales of UX: From 0.1 Seconds to 100 Years." https://www.uxtigers.com/post/time-scales-ux (The source is a practitioner article. The thresholds are widely repeated but have a weak empirical basis; see Open questions.)
- Measured perception of mouse-based interaction latency: perception thresholds of roughly 34 to 137 ms, mean about 65 ms. Forch, V., Franke, T., Rauh, N., & Krems, J. F. (2017). Cited as reported in secondary summaries; the original venue and URL were not verified.
- Latencies below 100 ms are seldom addressed in design guidelines, although smaller latencies are perceivable and can affect performance. Franke, T., Attig, C., Rauh, N., & Krems, J. F. (2017). "System Latency Guidelines Then and Now: Is Zero Latency Really Considered Necessary?" EPCC/HCII, Springer. https://doi.org/10.1007/978-3-319-58475-1_1
- Shneiderman's 1984 survey found that interactions under about 1 s are generally preferred and can increase productivity. Shneiderman, B. (1984). "Response time and display rate in human performance with computers." ACM Computing Surveys. https://www.cs.umd.edu/users/ben/papers/Shneiderman1984Response.pdf
- The 400 ms heuristic traces to Doherty, W. J., & Thadani, A. J. (1982). "The Economic Value of Rapid Response Time," IBM. Cited via secondary summary at https://lawsofux.com/doherty-threshold/. The original report was not retrieved.
- Martin, G. L., & Corl, K. G. (1986). "System response time effects on user productivity," Behaviour & Information Technology. Found via https://www.bohrium.com/paper-details/system-response-time-effects-on-user-productivity/811988601763004420-10074. Productivity gains from faster responses held for simple, habitual tasks, but were small or absent for complex tasks.

## Scoring method

1. Pick one screen and one primary user action (for example, submitting a form or opening a list).
2. Perform the action three times on a representative connection. Record the time to first visible feedback (T1) and the time to a usable result (T2). Use a screen recording at 60 fps or a stopwatch as a fallback.
3. Compute the median of T1 and of T2 across the three runs.
4. Check whether the interface stays interactive during T2: can the user scroll, navigate, or cancel? Record yes or no.
5. Check the loading state at T1 to T2: does it show structure (skeleton, progress, or partial content) or only a generic spinner? Record the type.
6. Compare the median T1 and T2 with the rubric thresholds. Record the score, the three raw timings, and the interactivity and loading-state observations.

## Scoring rubric

0 = severe failure, 5 = exemplary (same scale across all metrics).

- **0:** No visible feedback for more than 1 s after the action, or the screen freezes or blanks until completion.
- **1:** Feedback arrives after 1 s, and the interface is non-interactive throughout the wait.
- **2:** Feedback arrives within 1 s, but the wait is an unexplained spinner, and T2 exceeds 3 s with no partial content.
- **3:** Feedback is immediate (under 100 ms), but the result takes more than 3 s, or the interface is blocked for part of the wait.
- **4:** Feedback under 100 ms. T2 under 3 s with a structured loading state, and the interface stays interactive for most of the wait.
- **5:** Feedback under 100 ms. The result is usable within 1 s, or partial content appears early. The interface stays interactive, and loading states show progress or structure.

The 100 ms and 1 s thresholds follow the Nielsen tradition and the Franke et al. review. The 3 s boundary is a judgment call (see Open questions).

## Automated checks (optional)

None reliable; manual review only. Lighthouse and Web Vitals (INP, LCP) measure load and input timing but not whether feedback is perceived as immediate, and they do not judge loading-state design.

## Common failure patterns

- Disabled submit with no feedback after a click, so users click repeatedly (no acknowledgement within 100 ms).
- Generic spinner over a blank area with no indication of progress, which makes waits feel longer.
- Full-screen blocking overlays during background work, which stop interaction even when the user has nothing to wait for.
- Layout shift as content loads, which forces users to re-find their place (Franke et al. latency guidance does not cover this directly; treat as a judgment).
- Skeleton screens that do not match final layout, or that are used where a spinner would be clearer.

## Sources

1. Nielsen, J. "Time Scales of UX: From 0.1 Seconds to 100 Years." https://www.uxtigers.com/post/time-scales-ux
2. Forch, V., Franke, T., Rauh, N., & Krems, J. F. (2017). Mouse-based interaction perception thresholds. Venue and URL not verified.
3. Franke, T., Attig, C., Rauh, N., & Krems, J. F. (2017). "System Latency Guidelines Then and Now." Springer. https://doi.org/10.1007/978-3-319-58475-1_1
4. Shneiderman, B. (1984). "Response time and display rate in human performance with computers." ACM Computing Surveys. https://www.cs.umd.edu/users/ben/papers/Shneiderman1984Response.pdf
5. Doherty, W. J., & Thadani, A. J. (1982). "The Economic Value of Rapid Response Time." IBM. Secondary source: https://lawsofux.com/doherty-threshold/
6. Martin, G. L., & Corl, K. G. (1986). "System response time effects on user productivity." Behaviour & Information Technology. https://www.bohrium.com/paper-details/system-response-time-effects-on-user-productivity/811988601763004420-10074

## Open questions

- The 100 ms and 1 s thresholds are widely repeated, but the empirical basis for Nielsen's numbers is disputed. Forch et al. report a mean near 65 ms, below the 100 ms figure.
- The 3 s and 5-level boundaries are judgment calls, not research-backed values.
- The Doherty & Thadani 400 ms figure was not checked against the original report. Martin & Corl found weak or no effect on complex tasks, which weakens its use as a universal target.
- Forch et al. and Myers (1985, progress indicators) could not be confirmed at a stable URL. Skeleton-screen evidence is mixed: a 2017 Viget practitioner test (136 participants, not peer-reviewed) favored spinners, while a 2024 Drexel thesis favored skeletons with looped animation. No strong peer-reviewed consensus was found.
- The layout-shift failure pattern is drawn from general practice, not from a source retrieved here.
