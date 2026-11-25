# Scorer prompt (haiku, one metric group per run, 5 runs total)

You score one UI screen on exactly one metric group (from `metrics/groups.json`). You do not know, and must not try to infer, any weighting.

## Inputs
- Group definition and scoring method: `metrics/<metric-id>.md`, where `<metric-id>` is a group id. Follow its scoring method and rubric. It lists the sub-metrics it covers; you may open those `metrics/<sub-id>.md` files for detail, but you produce one score for the whole group.
- The UI: `workspace/<iteration-id>/original/screenshot.png`. This is the only input about the UI.
- Metric id: `<metric-id>` (a group id)

## Task
1. Read `metrics/<metric-id>.md`.
2. Inspect the screenshot only through this metric's lens. Ignore other metrics.
3. Choose an integer score from 0 to 100, where 100 is excellent. Anchor it to the rubric in the methodology file.
4. Write 3 to 10 todo items that would raise this score. Each must be a concrete, actionable change to the UI (what to change and roughly how). Refer to visible elements on the screenshot. No vague advice like "improve the design".
5. Write `workspace/<iteration-id>/scores/<metric-id>.json` and nothing else:

```json
{
  "metric": "<metric-id>",
  "score": 72,
  "rationale": "One to three sentences citing the specific evidence behind the score.",
  "todos": [
    "Increase the body text color contrast against the card background to at least 4.5:1.",
    "Add 16px of spacing between the title and the description.",
    "Make the primary button label sentence case."
  ]
}
```

## Rules
- `todos` must contain between 3 and 10 non-empty strings. Fewer or more fails validation and the whole iteration is rejected.
- `score` must be a JSON integer from 0 to 100, not a string, not a float.
- `metric` must equal `<metric-id>` exactly.
- Do not write any other file. Do not edit `metrics/` or any other iteration folder. Do not open the target repo; scoring uses the screenshot only.
- Do not mention weights, priority, or other metrics in the rationale or todos.
