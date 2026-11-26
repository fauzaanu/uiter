# uiter

A Claude Code skill that redesigns a UI screen from a screenshot, directly in your repo.

Haiku subagents score the screen, fable invents one bold redesign, and fable builds it on a branch. It goes as far as it can by default. If it goes too far, revert.

## Loop

```
screenshot → 5 scorers → judgement → 1 concept → build → you review
```

1. **Score:** 5 parallel scorers, one per metric group (37 sub-metrics in `metrics/`).
2. **Judge:** `scripts/score.py` weights the scores and writes `judgement.md`.
3. **Invent:** one concept, one direction. The todos are a checklist, not the brief.
4. **Build:** implemented on `uiter/<iteration-id>`, checks run, nothing committed.
5. **Review:** keep it, discard it, or follow up.

## Modes

| Mode | Result |
| --- | --- |
| `reinvent` (default) | New design for the screen or one component |
| `restructure` | New layout, same kinds of parts |
| `polish` | Same screen, refined |

Follow-ups: "try a different direction", "go back a bit", "keep this, rethink X".

## Models

Each role takes its own model. Presets are in `models.json`:

| Preset | scorer | inventor | improver |
| --- | --- | --- | --- |
| `default` | haiku | fable | fable |
| `all-fable` | fable | fable | fable |
| `opus-build` | haiku | fable | opus |

Override a single role with `--inventor opus` or similar.

## Install

```sh
git clone https://github.com/fauzaanu/uiter.git ~/.claude/skills/uiter
```

Needs Python 3 and a target project in git.

## Use

```
/uiter                      with a screenshot attached
/uiter use opus to build    swap a role's model
/uiter the topic field      one component only
```

`workspace/` holds your runs and is git-ignored.
