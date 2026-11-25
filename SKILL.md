---
name: uiter
description: Score a UI screen from its screenshot against 5 grouped UI review metrics (covering 37 sub-metrics), produce a weighted judgement with actionable todos, then improve it in the target repo in one of three modes the user picks - polish (refine in place), restructure (rework layout from root causes), or reinvent (design a screen or one component from scratch via three divergent concepts the user chooses between) - and hand it to a human for review. Use when the user asks to review, critique, score, iteratively improve, redesign, or reimagine a UI screen or component that lives in a real project.
---

# uiter

A UI iteration loop: brief, score, judge, (concepts), implement, review.

- The **user** chooses a mode and a scope before anything runs (step 0).
- **haiku** scorers grade the screenshot on one metric group each: 5 scorers, one per group in `metrics/groups.json`. Each group file covers several of the 37 sub-metrics. They never see weights.
- **score.py** aggregates the 5 group scores with the weights from `metrics/groups.json` and writes `judgement.md`, including the brief.
- **fable** improves the UI in the target repo, as far as the mode allows. In reinvent mode it first writes three divergent concepts and the user picks one.
- A **human** reviews the screenshot, the judgement, and the repo diff, then decides what happens next.

There is no isolated HTML reproduction. The screenshot is the only original. Improvements are made in the real project.

## Modes

Scorers measure deficits (low contrast, cramped spacing, missing states), so their todos always pull toward refining what exists. The mode decides how much weight those todos get.

| Mode | Use when | Todos are | Result |
| --- | --- | --- | --- |
| **polish** | The structure works; it looks or reads rough. | The work list. | The same screen, finished: contrast, spacing, type, states, labels. |
| **restructure** | The layout or hierarchy is the problem. | Symptoms; fable finds the root causes. | A clearly different layout built from the same kinds of parts. |
| **reinvent** | The approach itself is wrong or tired, and you want a new idea, not a better version. | An acceptance checklist checked at the end, never the brief. | A new interaction model for the screen or one component, from three divergent concepts you choose between. |

**Scope** is the whole screen or one named component or region (`--focus`). Reinvent works best on one component ("the recipient picker", "the history table"): it keeps the change reviewable while letting that part be rethought completely.

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
    improved/choice.md        reinvent only: the concept the user picked and their changes
    improved/concept.md       the design or build plan, written before code
    improved/changes.diff     diff of the repo changes, written by the implementer
    improved/notes.md         what was applied, skipped, and why
    judgement.md              generated, never hand-edited
```

## Workflow

0. **Ask for the brief.** Unless the user's request already says it plainly ("just fix the contrast" = polish; "rethink this from scratch" = reinvent), ask with AskUserQuestion, in one call:
   - **Mode**: "How far should this iteration go?" Options: *Polish* (keep the structure, fix contrast, spacing, states and labels), *Restructure* (rework the layout and hierarchy from the root causes), *Reinvent* (design it from scratch: three different concepts, you pick one). Do not mark a recommendation unless the request or a previous iteration points to one; if the last iteration on this screen was already a polish or restructure and the user is unhappy with how incremental it was, recommend Reinvent.
   - **Scope**: "Which part?" Options: *Whole screen*, plus up to two specific components you can see in the screenshot (name them as they appear, e.g. "History table"). The user can type another one under Other.
   - Constraints are not a question: take them from the user's words if given (for example "no new copy", "keep the sidebar"), otherwise leave them empty.

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

4. **Reinvent mode only: concepts, then the user chooses.**
   - Run one fable agent with `prompts/concepts.md`. It writes `improved/concepts.md` with three concepts that differ in interaction model (ambitious-but-shippable, a different model, bold) and a recommendation. It edits nothing in the repo.
   - Show the user the three concepts (name, one-line idea, wireframe, effort, risk) with `send_to_user` or in full in the reply, then ask with AskUserQuestion which to build: A, B, C (mark the agent's recommendation), with Other for "mix A's flow with C's layout" style answers. Put each concept's wide wireframe in the option `preview`.
   - Write the answer, word for word plus any changes the user asked for, to `improved/choice.md`. If the user rejects all three, run the concepts agent again with their feedback appended, and overwrite `concepts.md`.

5. **Implement with fable, once.** Run one fable agent with `prompts/improver.md` for this iteration. It reads the brief, works at the depth the mode asks for (and only on the focus component when one is set), writes `improved/concept.md`, implements in the target repo on a new branch (or the current branch when the project forbids branches), leaves the changes uncommitted, and writes `improved/changes.diff` and `improved/notes.md`.

6. **Human review.** A person reviews the screenshot, `judgement.md`, `improved/notes.md`, and the branch diff in the repo. They decide: accept the branch, reject it, or start a new iteration from the current state, possibly in a different mode.

## Rules that must hold

- The brief (mode and scope) is set by the user, never assumed silently. When it is inferred from the request, say which mode was used in the first status line.
- Scorers never receive weights or the brief, and their todos never reference weights.
- Each todo list has 3 to 10 items. `score.py` enforces this.
- `judgement.md` is generated only. Never edit it by hand.
- In reinvent mode nothing is implemented until the user has picked a concept and `improved/choice.md` exists.
- Improvements go into the target repo only, on a branch named `uiter/<iteration-id>` (or the current branch when the target project forbids branches). Nothing is committed or pushed by the skill.
- The original screenshot in `original/` is never modified.
- Each iteration is isolated in its own folder under `workspace/`.
