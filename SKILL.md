---
name: uiter
description: Score a UI screen from its screenshot against 5 grouped UI review metrics (covering 37 sub-metrics), produce a weighted judgement with actionable todos, then redesign it in the target repo as far as it can go by default (reinvent: one bold concept from an inventor agent, built automatically, no questions), with polish and restructure only as dial-back modes when the user asks for less, and hand the uncommitted branch to a human for review. Each role (scorer, inventor, improver) runs on a configurable model: presets in models.json (default haiku/fable/fable, all-haiku, all-fable, opus-build) or per-role overrides. Use when the user asks to review, critique, score, iteratively improve, redesign, or reimagine a UI screen or component that lives in a real project.
---

# uiter

A UI iteration loop: score, judge, invent, implement, review. It runs end to end without stopping to ask.

- **Scorers** (haiku by default) grade the screenshot on one metric group each: 5 scorers, one per group in `metrics/groups.json`. Each group file covers several of the 37 sub-metrics. They never see weights.
- **score.py** aggregates the 5 group scores with the weights from `metrics/groups.json` and writes `judgement.md`, including the brief.
- The **inventor** (fable by default) commits to one bold concept for the screen or component (reinvent, the default), then the **improver** (fable by default) builds it in the target repo. One direction only: no alternatives, no choosing between options.
- A **human** reviews the screenshot, the judgement, and the repo diff, then decides what happens next.

There is no isolated HTML reproduction. The screenshot is the only original. Improvements are made in the real project.

## Modes

Scorers measure deficits (low contrast, cramped spacing, missing states), so their todos always pull toward refining what exists. The mode decides how much weight those todos get.

**Go as far as possible by default.** Reinvent is the default and is used unless the user explicitly asks for less. Nothing is committed, so a too-bold result is undone with one `git checkout`/revert or dialled back with a follow-up, while a too-timid result costs the user a round of prompting for more ambition. Never ask which mode to use, and never pause between concepts and implementation.

| Mode | Use when | Todos are | Result |
| --- | --- | --- | --- |
| **reinvent** (default) | Always, unless the user asks for less. | An acceptance checklist checked at the end, never the brief. | A new interaction model for the screen or focus component, built from one bold concept. |
| **restructure** | Only when asked ("less drastic", "keep the same parts"). | Symptoms; the improver finds the root causes. | A clearly different layout built from the same kinds of parts. |
| **polish** | Only when asked ("just refine", "only fix contrast"). | The work list. | The same screen, finished: contrast, spacing, type, states, labels. |

**Scope** is the whole screen unless the user names a component or region (`--focus`, e.g. "the recipient picker"). Do not ask for it.

## Models per role

Each role runs on its own model, read from `original/brief.json` (`models`). Always pass that model to the Agent tool (`model: "haiku"`, `"sonnet"`, `"opus"` or `"fable"`), never the session default.

| Preset | scorer | inventor | improver | Use |
| --- | --- | --- | --- | --- |
| `default` | haiku | fable | fable | Normal runs. |
| `all-haiku` | haiku | haiku | haiku | Experiment: cheapest and fastest; compare its result against a default run of the same screen. |
| `all-fable` | fable | fable | fable | Strongest scoring too, at the highest cost. |
| `opus-build` | haiku | fable | opus | Fable's idea, built by opus. |

Pick the preset from the user's words ("all haiku", "use opus to build"); otherwise use `default`. Single roles can be overridden on top of any preset (`--inventor opus`). Report the preset and the model per role in the first status line and in the final report, so runs on different models can be compared.

## Layout

```
uiter/
  SKILL.md                  this file
  metrics/groups.json       5 metric groups: id, name, file, weight (sums to 100), members
  metrics/index.json        the 37 sub-metrics (reference; each belongs to one group)
  metrics/<group-id>.md     methodology per group (what scorers follow)
  metrics/<id>.md           methodology per sub-metric (reference for the groups)
  models.json               model per role: presets and allowed models
  prompts/scorer.md         prompt for each scorer
  prompts/inventor.md       prompt for the inventor (reinvent mode only)
  prompts/improver.md       prompt for the improver (all modes)
  scripts/new_iteration.py  creates a workspace iteration and its brief
  scripts/score.py          validates scores and writes judgement.md
  workspace/<iteration-id>/
    original/screenshot.png   the original screenshot
    original/target.txt       path of the target repo (from --repo)
    original/brief.json       mode, focus, constraints, preset and model per role (from step 0)
    scores/<group-id>.json    one per group, 5 total
    improved/concept.md       the design, written before code (by the inventor in reinvent mode, by the improver otherwise)
    improved/changes.diff     diff of the repo changes, written by the implementer
    improved/notes.md         what was applied, skipped, and why
    judgement.md              generated, never hand-edited
```

## Workflow

0. **Read the brief from the request, without asking.** Mode is `reinvent` unless the user's words ask for less ("just polish", "small refinements", "only fix contrast" = polish; "less drastic", "keep the same components" = restructure). Focus is the component the user names, otherwise the whole screen. Constraints are any limits in their words ("keep the sidebar", "no new copy"), otherwise empty. State the mode and focus in the first status line.

1. **Create the iteration.**
   ```
   python3 scripts/new_iteration.py <iteration-id> --screenshot <path.png> --repo <absolute path to the project> \
     --mode <polish|restructure|reinvent> [--focus "<component>"] [--constraints "<user's limits>"] \
     [--models <preset>] [--scorer <model>] [--inventor <model>] [--improver <model>]
   ```
   Iteration ids are never reused. `--mode` defaults to reinvent; `--models` defaults to the `default` preset.

2. **Score, 5 runs.** Launch exactly one scorer, on the `scorer` model from `brief.json`, per group id in `metrics/groups.json` (visual-clarity, interaction-feedback, accessibility, content-cognition, consistency-context). Never launch one per sub-metric. Each follows `prompts/scorer.md` with its `<metric-id>` set to the group id and writes `scores/<group-id>.json`. Scorers are independent, so run them in parallel. Scorers score the whole screenshot in every mode; the mode does not change scoring.

3. **Judge.**
   ```
   python3 scripts/score.py workspace/<iteration-id>
   ```
   This validates all 5 files and writes `judgement.md` (with the brief at the top). If it fails, the error lists every problem. Fix the offending score files (re-run only the affected scorers) and run again. No partial judgement is ever written.

4. **Reinvent mode only: invent, once.** Run one agent on the `inventor` model with `prompts/inventor.md`. It commits to a single concept, the most ambitious one that keeps every capability and fits the stack, and writes it as a buildable spec in `improved/concept.md`. It edits nothing in the repo. Do not ask the user about it; go straight to step 5.

5. **Implement, once.** Run one agent on the `improver` model with `prompts/improver.md` for this iteration. It reads the brief, works at the depth the mode asks for (and only on the focus component when one is set), writes `improved/concept.md` (polish and restructure; in reinvent it builds the inventor's), implements in the target repo on a new branch (or the current branch when the project forbids branches), leaves the changes uncommitted, and writes `improved/changes.diff` and `improved/notes.md`.

6. **Human review.** Report the branch, the concept that was built (name and one sentence), the score, and the model per role. A person reviews the screenshot, `judgement.md`, `improved/notes.md`, and the branch diff. Then they keep it, discard it (`git checkout <previous branch>` and delete the branch), or send a follow-up.

## Follow-ups: dialling back or switching

The user steers after seeing the result, not before. Each follow-up is a new iteration (new id, fresh screenshot of the current state if the old one no longer applies) on the same `--repo`:

- **"Try a different direction"** (optionally "...more like X" or "not Y"): a new reinvent iteration from the same original screenshot and the original base branch, with the user's words and the rejected concept's name in `--constraints`, so the inventor goes somewhere else.
- **"Too much, go back a bit" / "keep the layout, just ..."**: a new iteration in `restructure` (or `polish` if they ask for only small fixes), with their words as `--constraints`.
- **"Keep this, but change X"**: a new iteration with `--focus X` in reinvent mode, starting from the current branch.

## Rules that must hold

- Default to reinvent. Never ask for the mode, scope, or concept choice; drop to restructure or polish only when the user's words ask for less. Always say which mode ran.
- Scorers never receive weights or the brief, and their todos never reference weights.
- Each todo list has 3 to 10 items. `score.py` enforces this.
- `judgement.md` is generated only. Never edit it by hand.
- In reinvent mode there is exactly one concept. The inventor never writes alternatives, and the improver builds it in full rather than trading it down.
- Improvements go into the target repo only, on a branch named `uiter/<iteration-id>` (or the current branch when the target project forbids branches). Nothing is committed or pushed by the skill.
- The original screenshot in `original/` is never modified.
- Each iteration is isolated in its own folder under `workspace/`.
