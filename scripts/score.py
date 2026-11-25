#!/usr/bin/env python3
"""Aggregate per-metric UI scores into a weighted judgement.md.

Usage:
    python3 scripts/score.py <iteration-dir> [--check] [--index PATH]

    --check   validate the score files only; write nothing.
    --index   metric index to use (default: ../metrics/groups.json next to
              this script: the 5 grouped metrics. Pass metrics/index.json to
              score the 37 individual metrics instead).

Iteration layout (<iteration-dir> = workspace/<iteration-id>/):
    original/screenshot.png     original screenshot (optional for this script)
    scores/<metric-id>.json     one file per metric in the index, all required
    judgement.md                GENERATED here, never hand-edited

Score file schema (scores/<metric-id>.json):
    {
      "metric":    "<id; equals the filename stem and is in the index>",
      "score":     <integer 0-100, 100 = excellent; booleans are rejected>,
      "rationale": "<non-empty string, 1-3 sentences>",
      "todos":     ["<actionable item>", ...]   # 3 to 10 non-empty strings
    }

Formula (weights come from the index; scorers never see them):
    weighted_i = score_i * weight_i
    share_i    = weighted_i / sum(weights)
    overall    = sum(weighted_i) / sum(weights)     # 0-100, shown to 1 decimal

Validation collects every error, prints them all, and exits non-zero without
touching judgement.md. Exit codes: 0 ok, 1 invalid scores, 2 usage/setup error.
"""

import argparse
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

MIN_TODOS = 3
MAX_TODOS = 10
SCREENSHOT_REL = "original/screenshot.png"
BRIEF_REL = "original/brief.json"
MODE_MEANING = {
    "polish": "refine in place: keep the structure, apply the todos as targeted fixes",
    "restructure": "rework the layout and hierarchy from the root causes behind the todos",
    "reinvent": "design from scratch: the todos are an acceptance checklist, not the brief",
}
DEFAULT_INDEX = Path(__file__).resolve().parent.parent / "metrics" / "groups.json"


class SetupError(Exception):
    """The index or iteration directory is unusable (not a scoring error)."""


def load_index(index_path):
    """Return the ordered metric list [{id, name, weight, ...}] from the index."""
    try:
        data = json.loads(Path(index_path).read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise SetupError(f"cannot read metric index {index_path}: {exc}")
    metrics = data.get("metrics") if isinstance(data, dict) else None
    if not isinstance(metrics, list) or not metrics:
        raise SetupError(f"{index_path}: expected a non-empty 'metrics' list")
    seen = set()
    for entry in metrics:
        if not isinstance(entry, dict) or not isinstance(entry.get("id"), str):
            raise SetupError(f"{index_path}: every metric needs a string 'id'")
        weight = entry.get("weight")
        if isinstance(weight, bool) or not isinstance(weight, (int, float)) or weight < 0:
            raise SetupError(f"{index_path}: metric '{entry['id']}' has an invalid weight")
        if entry["id"] in seen:
            raise SetupError(f"{index_path}: duplicate metric id '{entry['id']}'")
        seen.add(entry["id"])
        entry.setdefault("name", entry["id"])
    if sum(m["weight"] for m in metrics) <= 0:
        raise SetupError(f"{index_path}: the weights must sum to more than zero")
    return metrics


def validate_score(data, expected_id, known_ids):
    """Return a list of error strings for one parsed score file (empty = valid)."""
    if not isinstance(data, dict):
        return ["top level must be a JSON object"]
    errors = []

    metric = data.get("metric")
    if not isinstance(metric, str):
        errors.append("'metric' must be a string")
    elif metric not in known_ids:
        errors.append(f"unknown metric id '{metric}'")
    elif metric != expected_id:
        errors.append(f"'metric' is '{metric}' but the filename says '{expected_id}'")

    score = data.get("score")
    if isinstance(score, bool) or not isinstance(score, int):
        errors.append(f"'score' must be an integer 0-100, got {type(score).__name__} {score!r}")
    elif not 0 <= score <= 100:
        errors.append(f"'score' must be between 0 and 100, got {score}")

    rationale = data.get("rationale")
    if not isinstance(rationale, str) or not rationale.strip():
        errors.append("'rationale' must be a non-empty string")

    todos = data.get("todos")
    if not isinstance(todos, list):
        errors.append("'todos' must be a list of strings")
    else:
        if not MIN_TODOS <= len(todos) <= MAX_TODOS:
            errors.append(f"'todos' must have {MIN_TODOS}-{MAX_TODOS} items, got {len(todos)}")
        for i, todo in enumerate(todos, start=1):
            if not isinstance(todo, str):
                errors.append(f"todo #{i} must be a string, got {type(todo).__name__}")
            elif not todo.strip():
                errors.append(f"todo #{i} is empty")
    return errors


def collect_scores(iteration_dir, metrics):
    """Read and validate scores/*.json. Return (scores_by_id, all_errors)."""
    scores_dir = Path(iteration_dir) / "scores"
    known_ids = {m["id"] for m in metrics}
    scores, errors = {}, []
    if not scores_dir.is_dir():
        return scores, [f"scores directory not found: {scores_dir}"]

    for metric in metrics:
        path = scores_dir / f"{metric['id']}.json"
        label = f"scores/{path.name}"
        if not path.is_file():
            errors.append(f"{label}: missing score file for metric '{metric['id']}'")
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            errors.append(f"{label}: cannot read as JSON ({exc})")
            continue
        file_errors = validate_score(data, metric["id"], known_ids)
        errors.extend(f"{label}: {e}" for e in file_errors)
        if not file_errors:
            scores[metric["id"]] = data

    for path in sorted(scores_dir.glob("*.json")):
        if path.stem not in known_ids:
            errors.append(f"scores/{path.name}: unknown metric id '{path.stem}' (not in the index)")
    return scores, errors


def aggregate(metrics, scores):
    """Apply the weights. Return (rows, total_weight, total_weighted, overall)."""
    total_weight = sum(m["weight"] for m in metrics)
    rows = []
    for metric in metrics:
        score = scores[metric["id"]]["score"]
        weighted = score * metric["weight"]
        rows.append({
            "id": metric["id"],
            "name": metric["name"],
            "weight": metric["weight"],
            "score": score,
            "weighted": weighted,
            "share": weighted / total_weight,
            "todos": scores[metric["id"]]["todos"],
        })
    total_weighted = sum(r["weighted"] for r in rows)
    return rows, total_weight, total_weighted, total_weighted / total_weight


def _num(value):
    """Format a weight or product: integers without a trailing '.0'."""
    return str(int(value)) if float(value).is_integer() else f"{value:.2f}"


def _one_line(text):
    """Collapse whitespace so a value stays on a single Markdown line."""
    return " ".join(str(text).split())


def render_judgement(iteration_dir, rows, total_weight, total_weighted, overall):
    """Build the judgement.md text."""
    iteration_dir = Path(iteration_dir)
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines = [f"# UI Judgement: {iteration_dir.name}", "", f"Generated at: {generated} (UTC)", ""]

    if (iteration_dir / SCREENSHOT_REL).is_file():
        lines.append(f"![Original screenshot]({SCREENSHOT_REL})")
    else:
        lines.append(f"_Original screenshot is missing (expected at `{SCREENSHOT_REL}`)._")

    brief_path = iteration_dir / BRIEF_REL
    if brief_path.is_file():
        try:
            brief = json.loads(brief_path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            brief = None
        if isinstance(brief, dict):
            mode = _one_line(brief.get("mode") or "restructure")
            lines += ["", "## Brief", "",
                      f"- Mode: **{mode}** ({MODE_MEANING.get(mode, 'unknown mode')})",
                      f"- Focus: {_one_line(brief.get('focus') or 'whole screen')}",
                      f"- Constraints: {_one_line(brief.get('constraints') or 'none given')}"]
            models = brief.get("models")
            if isinstance(models, dict) and models:
                roles = ", ".join(f"{_one_line(r)} = {_one_line(m)}" for r, m in models.items())
                lines.append(f"- Models ({_one_line(brief.get('preset') or 'custom')}): {roles}")

    lines += ["", "## Overall score", "", f"**{overall:.1f} / 100**", ""]

    lines += [
        "## Metric scores",
        "",
        "| Metric | Weight | Score (0-100) | Weighted (score x weight) "
        "| Weighted share (weighted / sum of weights) |",
        "| --- | ---: | ---: | ---: | ---: |",
    ]
    for r in rows:
        name = _one_line(r["name"]).replace("|", "\\|")
        lines.append(
            f"| {name} | {_num(r['weight'])} | {r['score']} "
            f"| {_num(r['weighted'])} | {r['share']:.2f} |"
        )
    lines.append(
        f"| **Total** | **{_num(total_weight)}** | | **{_num(total_weighted)}** "
        f"| **{overall:.1f}** |"
    )

    lines += ["", "## Todo list", ""]
    for r in rows:
        lines += [f"### {_one_line(r['name'])}", ""]
        lines += [f"- [ ] {_one_line(todo)}" for todo in r["todos"]]
        lines.append("")

    lines += ["---", "", "_Generated by `scripts/score.py`. Do not hand-edit; re-run the script instead._", ""]
    return "\n".join(lines)


def write_atomic(path, text):
    """Write text to path via a temp file in the same directory + os.replace."""
    path = Path(path)
    fd, tmp_name = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.chmod(tmp_name, 0o644)
        os.replace(tmp_name, path)
    except BaseException:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)
        raise


def main(argv=None):
    parser = argparse.ArgumentParser(description="Aggregate UI metric scores into judgement.md.")
    parser.add_argument("iteration_dir", help="path to workspace/<iteration-id>/")
    parser.add_argument("--check", action="store_true", help="validate only, write nothing")
    parser.add_argument("--index", default=str(DEFAULT_INDEX), help="path to the metric index (default metrics/groups.json)")
    args = parser.parse_args(argv)

    iteration_dir = Path(args.iteration_dir).resolve()
    try:
        if not iteration_dir.is_dir():
            raise SetupError(f"iteration directory not found: {iteration_dir}")
        metrics = load_index(args.index)
    except SetupError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    scores, errors = collect_scores(iteration_dir, metrics)
    if errors:
        print(f"INVALID: {len(errors)} error(s) in {iteration_dir}", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        print("judgement.md was not written.", file=sys.stderr)
        return 1

    rows, total_weight, total_weighted, overall = aggregate(metrics, scores)
    if args.check:
        print(f"OK: {len(rows)} score files valid. Overall score: {overall:.1f} / 100 (not written)")
        return 0

    out_path = iteration_dir / "judgement.md"
    write_atomic(out_path, render_judgement(iteration_dir, rows, total_weight, total_weighted, overall))
    print(f"Overall score: {overall:.1f} / 100")
    print(f"Wrote {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
