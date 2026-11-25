---
name: uiter
description: Score a UI screen from its screenshot against 5 grouped UI review metrics (covering 37 sub-metrics), produce a weighted judgement with actionable todos, then redesign it in the target repo as far as it can go by default (reinvent: three divergent concepts, the boldest viable one built automatically, no questions), with polish and restructure only as dial-back modes when the user asks for less, and hand the uncommitted branch to a human for review. Use when the user asks to review, critique, score, iteratively improve, redesign, or reimagine a UI screen or component that lives in a real project.
---

# uiter

A UI iteration loop: score, judge, invent, implement, review. It runs end to end without stopping to ask.

- **haiku** scorers grade the screenshot on one metric group each: 5 scorers, one per group in `metrics/groups.json`. Each group file covers several of the 37 sub-metrics. They never see weights.
- **score.py** aggregates the 5 group scores with the weights from `metrics/groups.json` and writes `judgement.md`, including the brief.
- **fable** writes three divergent concepts and picks the most ambitious viable one (reinvent, the default), then a second fable run builds it in the target repo.
- A **human** reviews the screenshot, the judgement, and the repo diff, then decides what happens next.

There is no isolated HTML reproduction. The screenshot is the only original. Improvements are made in the real project.

## Modes

Scorers measure deficits (low contrast, cramped spacing, missing states), so their todos always pull toward refining what exists. The mode decides how much weight those todos get.

**Go as far as possible by default.** Reinvent is the default and is used unless the user explicitly asks for less. Nothing is committed, so a too-bold result is undone with one `git checkout`/revert or dialled back with a follow-up, while a too-timid result costs the user a round of prompting for more ambition. Never ask which mode to use, and never pause between concepts and implementation.

| Mode | Use when | Todos are | Result |
| --- | --- | --- | --- |
| **reinvent** (default) | Always, unless the user asks for less. | An acceptance checklist checked at the end, never the brief. | A new interaction model for the screen or focus component, built from the boldest viable of three divergent concepts. |
| **restructure** | Only when asked ("less drastic", "keep the same parts"). | Symptoms; fable finds the root causes. | A clearly different layout built from the same kinds of parts. |
| **polish** | Only when asked ("just refine", "only fix contrast"). | The work list. | The same screen, finished: contrast, spacing, type, states, labels. |

**Scope** is the whole screen unless the user names a component or region (`--focus`, e.g. "the recipient picker"). Do not ask for it.

## Layout

```
uiter/
  SKILL.md                  this file
  metrics/groups.json       5 metric groups: id, name, file, weight (sums to 100), members
  metrics/index.json        the 37 sub-metrics (reference; each belongs to one group)
  metrics/<group-id>.md     methodology per group (what scorers follow)
  metrics/<id>.md           methodology per sub-metric (reference for the groups)
  prompts/scorer.md         prompt for each haiku scorer
  prompts/concepts.md       prompt for the fable concept writer (reinvent mode only)
  prompts/improver.md       prompt for the fable implementer (all modes)
  scripts/new_iteration.py  creates a workspace iteration and its brief
  scripts/score.py          validates scores and writes judgement.md
  workspace/<iteration-id>/
    original/screenshot.png   the original screenshot
    original/target.txt       path of the target repo (from --repo)
    original/brief.json       mode, focus, constraints (from step 0)
    scores/<group-id>.json    one per group, 5 total
    improved/concepts.md      reinvent only: three divergent concepts
    improved/choice.md        reinvent only: the concept to build and why (auto, or the user's follow-up)
    improved/concept.md       the design or build plan, written before code
    improved/changes.diff     diff of the repo changes, written by the implementer
    improved/notes.md         what was applied, skipped, and why
    judgement.md              generated, never hand-edited
```

## Workflow

0. **Read the brief from the request, without asking.** Mode is `reinvent` unless the user's words ask for less ("just polish", "small refinements", "only fix contrast" = polish; "less drastic", "keep the same components" = restructure). Focus is the component the user names, otherwise the whole screen. Constraints are any limits in their words ("keep the sidebar", "no new copy"), otherwise empty. State the mode and focus in the first status line.

1. **Create the iteration.**
   ```
   python3 scripts/new_iteration.py <iteration-id> --screenshot <path.png> --repo <absolute path to the project> \
     --mode <polish|restructure|reinvent> [--focus "<component>"] [--constraints "<user's limits>"]
   ```
   Iteration ids are never reused. `--mode` defaults to restructure for old invocations.

2. **Score with haiku, 5 runs.** Launch exactly one haiku scorer per group id in `metrics/groups.json` (visual-clarity, interaction-feedback, accessibility, content-cognition, consistency-context). Never launch one per sub-metric. Each follows `prompts/scorer.md` with its `<metric-id>` set to the group id and writes `scores/<group-id>.json`. Scorers are independent, so run them in parallel. Scorers score the whole screenshot in every mode; the mode does not change scoring.

3. **Judge.**
   ```
   python3 scripts/score.py workspace/<iteration-id>
   ```
   This validates all 5 files and writes `judgement.md` (with the brief at the top). If it fails, the error lists every problem. Fix the offending score files (re-run only the affected scorers) and run again. No partial judgement is ever written.

4. **Reinvent mode only: concepts, chosen automatically.**
   - Run one fable agent with `prompts/concepts.md`. It writes `improved/concepts.md` with three concepts that differ in interaction model (ambitious-but-shippable, a different model, bold) and ends with `Recommendation: <A|B|C>`, which defaults to the most ambitious concept that is viable. It edits nothing in the repo.
   - Do not ask the user. Write `improved/choice.md` with the recommended concept and the agent's reason (`Chosen automatically: C, because ...`), then go straight to step 5.

5. **Implement with fable, once.** Run one fable agent with `prompts/improver.md` for this iteration. It reads the brief, works at the depth the mode asks for (and only on the focus component when one is set), writes `improved/concept.md`, implements in the target repo on a new branch (or the current branch when the project forbids branches), leaves the changes uncommitted, and writes `improved/changes.diff` and `improved/notes.md`.

6. **Human review.** Report the branch, the concept that was built, the other two concept names in one line each, and the score. A person reviews the screenshot, `judgement.md`, `improved/notes.md`, and the branch diff. Then they keep it, discard it (`git checkout <previous branch>` and delete the branch), or send a follow-up.

## Follow-ups: dialling back or switching

The user steers after seeing the result, not before. Each follow-up is a new iteration (new id, fresh screenshot of the current state if the old one no longer applies) on the same `--repo`:

- **"Build concept B instead"** (or A): create the iteration in reinvent mode from the same original screenshot, copy the previous iteration's `improved/concepts.md`, write `choice.md` naming that concept and any changes the user asked for, skip step 4's agent, and run step 5. Start from the base the user wants (usually the original base branch, not the rejected branch).
- **"Too much, go back a bit" / "keep the layout, just ..."**: a new iteration in `restructure` (or `polish` if they ask for only small fixes), with their words as `--constraints`.
- **"Keep this, but change X"**: a new iteration with `--focus X` in reinvent mode, starting from the current branch.

## Rules that must hold

- Default to reinvent. Never ask for the mode, scope, or concept choice; drop to restructure or polish only when the user's words ask for less. Always say which mode ran.
- Scorers never receive weights or the brief, and their todos never reference weights.
- Each todo list has 3 to 10 items. `score.py` enforces this.
- `judgement.md` is generated only. Never edit it by hand.
- In reinvent mode, `improved/choice.md` is written before step 5 runs, and the improver builds that concept in full rather than trading it down.
- Improvements go into the target repo only, on a branch named `uiter/<iteration-id>` (or the current branch when the target project forbids branches). Nothing is committed or pushed by the skill.
- The original screenshot in `original/` is never modified.
- Each iteration is isolated in its own folder under `workspace/`.
