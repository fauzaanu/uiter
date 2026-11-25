# uiter

A Claude Code skill that runs an automated loop to rethink UI, not just tidy it up.

Most AI UI reviews end with "raise the contrast, add 8px of padding". That is because the reviewer looks for flaws, and fixes for flaws keep you close to the screen you already have. uiter uses a team of cheap, fast **haiku** subagents to score what exists, then hands their findings to **fable**, which treats them as symptoms and invents new designs. By default it goes as far as it can and builds the boldest design that still works, straight into your repo. If it goes too far, you revert. You never have to keep asking it to be more ambitious.

## How it works

```
screenshot ──► 5 haiku scorers (parallel) ──► score.py ──► fable: 1 concept  ──► fable: build ──► you review
               one per metric group          weighted      one bold direction   on a branch,
               score + todos each            judgement     no alternatives      uncommitted
```

1. **Score (haiku × 5, in parallel).** Each scorer grades the screenshot on one metric group: visual clarity, interaction and feedback, accessibility, content and cognitive effort, consistency and context fit. Together the groups cover 37 sub-metrics, each with its own method and rubric in `metrics/`. Scorers never see the weights, which keeps them from gaming the total.
2. **Judge (`scripts/score.py`).** Combines the five scores using the weights in `metrics/groups.json` and writes `judgement.md`, with an overall score and every todo.
3. **Invent (fable).** Works out what the person using the screen is trying to get done, lists what the current design takes for granted without needing to, and commits to **one** bold concept: the most ambitious idea that keeps every feature reachable and fits the stack. No alternatives and no picking between options: splitting effort across several ideas makes each one weaker. "The same screen, cleaner" is not allowed.
4. **Build (fable).** Implements that concept in your real project on a `uiter/<iteration-id>` branch, runs your type check, lint and tests, and leaves everything uncommitted with a diff and notes.
5. **Review (you).** Keep it, throw it away, or steer with a follow-up.

## Modes

| Mode | When | What you get |
| --- | --- | --- |
| **reinvent** (default) | Always, unless you ask for less | A new way of using the screen or component, from one bold concept |
| **restructure** | "less drastic", "keep the same parts" | A clearly different layout built from the same kinds of parts |
| **polish** | "just refine", "only fix contrast" | The same screen, finished |

You steer after you see the result, not before:

- "Try a different direction" (optionally "more like X"): a new run that avoids the rejected concept.
- "Too much, go back a bit": a new run in restructure or polish mode, with your words as limits.
- "Keep this, but rethink the history table": a new full redesign of just that component.

## Install

```sh
git clone https://github.com/fauzaanu/uiter.git ~/.claude/skills/uiter
```

Requirements: Claude Code with the haiku and fable models available, Python 3 (standard library only), and the target project in a git repository.

## Use

In Claude Code, inside or alongside the project:

> /uiter improve this screen — screenshot at ~/Desktop/settings.png, repo at ~/code/my-app

or name a component to focus on:

> use uiter on the recipient picker in this screenshot

The skill handles the rest: it creates the iteration, runs the scorers, judges, invents, builds and reports. See [`SKILL.md`](SKILL.md) for the full workflow and the rules each step follows.

## Layout

```
SKILL.md                  workflow and rules (what Claude follows)
metrics/groups.json       the 5 scored groups, their weights and members
metrics/*.md              scoring methods: 5 groups, 37 sub-metrics
prompts/scorer.md         haiku scorer prompt
prompts/inventor.md       fable inventor prompt (reinvent mode)
prompts/improver.md       fable build prompt (all modes)
scripts/new_iteration.py  creates workspace/<iteration-id>/ and its brief
scripts/score.py          checks the score files and writes judgement.md
workspace/                your iterations (git-ignored: screenshots and notes stay local)
```

## Safety

- Nothing is committed or pushed to your project. Every change lands uncommitted on its own branch.
- Every URL, form, endpoint, permission check and data field the screen has today must still be reachable afterwards.
- Your project's own rules (design tokens, security, data rules) and any limits you state always apply.
- `workspace/` is git-ignored, so screenshots of your apps never end up in this repo.
