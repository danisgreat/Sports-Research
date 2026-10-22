"""PICKS_V2 card block: parse and lint (PICKS-v2 / WIDTH-v1 / REFMODEL-v1).

Every new card carries one machine-readable block between ``<!-- BEGIN PICKS_V2 <key> -->`` and
``<!-- END PICKS_V2 <key> -->`` inside its card markers: ``key: value`` header lines, a blank line, then CSV rows.

    python -m ml card lint --mini research/active_minis/<MINI_KEY>.md --key LOCAL-<MINI_KEY>-G0001

The linter replaces hand-ticked arithmetic checks: masses sum to one, the printed p equals W/(W+L), complementary rows
agree, line distances match the printed centre and SD, widths are not below the competition's floor, the most-likely list
is ordered and below the selection ceiling, information rows are exactly the rows that moved at least 0.03 from the
reference, and the abstain flag follows from the numbers. It reads no model output, price or outcome.
"""
from __future__ import annotations

import argparse
import csv
import io
import math
import re
from pathlib import Path

from ml import reference as R

ROOT = Path(__file__).resolve().parents[1]
BEGIN, END = "<!-- BEGIN PICKS_V2 {key} -->", "<!-- END PICKS_V2 {key} -->"
META_REQUIRED = ("tier", "competition", "reference_id", "reference_status", "model_stage", "abstain", "fast_card", "timing", "scheduled_start",
                 "issued_at")
META_OPTIONAL = ("reference_frozen_at", "width_floor_exception", "tier_basis", "notes")
COLUMNS = ("label", "family", "quantity", "side", "line", "line_source", "reference_p", "baseline_p", "model_p", "final_p", "w", "p", "l",
           "line_implied_p", "centre", "sd", "z", "most_likely_rank", "information_row")
FAMILIES = ("WINNER", "HANDICAP", "TOTAL", "TEAM_TOTAL", "PERIOD", "PLAYER", "CORNERS", "OTHER")
QUANTITIES = ("MARGIN", "TOTAL", "TEAM_TOTAL", "PERIOD", "PLAYER", "COUNT", "N/A")
TIMINGS = ("PREGAME", "POST_START_ISSUE", "TIMING_UNVERIFIED")
REFERENCE_STATUSES = ("EXECUTED", "BASELINE_ONLY", "NOT_AVAILABLE", "NOT_RUN_NO_RELEASE", "NOT_RUN_STALE_RELEASE",
                      "NOT_RUN_INPUT_REFUSED", "NOT_RUN_NO_TB1_CONSTANTS", "FAILED")
HAS_REFERENCE = ("EXECUTED", "BASELINE_ONLY")
MODEL_STAGES = ("EXECUTED", "NOT_RUN_NO_RELEASE", "NOT_RUN_STALE_RELEASE", "NOT_RUN_INPUT_REFUSED", "FAILED", "NOT_APPLICABLE")
SELECTION_CEILING = 0.90
STRONG = 0.65           # a calibrated p below this has behaved like a coin flip (REVIEW 2026-10-22 section 2)
INFORMATION_DELTA = 0.03
TOLERANCE = 0.002
TWO_WAY_FAMILIES = ("HANDICAP", "TOTAL", "TEAM_TOTAL", "PERIOD")
MISSING_BASELINE = re.compile(r"MISSING:(NO_LEAGUE_PROFILE|PROFILE_LACKS_ENDPOINT|DISCRETE_FAMILY_UNSUPPORTED|NEW_FORMAT_NO_PRIOR|"
                              r"SOURCE_UNREACHABLE|BASELINE_UNAVAILABLE|OTHER:.+).*")


class PicksError(ValueError):
    pass


def block(card_text: str, key: str) -> str:
    begin, end = BEGIN.format(key=key), END.format(key=key)
    if card_text.count(begin) != 1 or card_text.count(end) != 1 or card_text.index(begin) > card_text.index(end):
        raise PicksError(f"card must hold exactly one complete PICKS_V2 block for {key}")
    return card_text[card_text.index(begin) + len(begin): card_text.index(end)]


def parse(text: str) -> tuple[dict, list[dict]]:
    lines = [ln.rstrip() for ln in text.strip().splitlines() if not ln.strip().startswith("```")]
    split = next((i for i, ln in enumerate(lines) if not ln.strip()), None)
    if split is None:
        raise PicksError("PICKS_V2 needs a blank line between the header and the CSV rows")
    meta = {}
    for ln in lines[:split]:
        if ":" not in ln:
            raise PicksError(f"header line without a colon: {ln!r}")
        name, value = ln.split(":", 1)
        meta[name.strip()] = value.strip()
    body = "\n".join(ln for ln in lines[split + 1:] if ln.strip())
    reader = csv.DictReader(io.StringIO(body))
    if tuple(reader.fieldnames or ()) != COLUMNS:
        raise PicksError("PICKS_V2 CSV columns must be exactly: " + ",".join(COLUMNS))
    return meta, [dict(r) for r in reader]


def _num(value: str, name: str, row: str, allow_blank: bool = False):
    value = (value or "").strip()
    if value == "" and allow_blank:
        return None
    try:
        v = float(value)
    except ValueError:
        raise PicksError(f"{row}: {name} must be a number, got {value!r}") from None
    if not math.isfinite(v):
        raise PicksError(f"{row}: {name} must be finite")
    return v


def threshold(row: dict) -> float | None:
    """The margin or total value at which the row flips, for the line-distance check (sign-insensitive)."""
    quantity, family, side, line = row["quantity"], row["family"], row["side"].upper(), row["line"].strip()
    if quantity == "MARGIN":
        if family == "WINNER":
            return 0.0
        if line == "":
            return None
        return -float(line) if side == "HOME" else float(line)
    if quantity == "TOTAL" and line != "":
        return float(line)
    return None


def lint(meta: dict, rows: list[dict], root=ROOT) -> list[str]:
    """Every problem found; an empty list means the block is internally consistent."""
    problems: list[str] = []
    for k in META_REQUIRED:
        if not meta.get(k):
            problems.append(f"header: missing {k}")
    unknown = set(meta) - set(META_REQUIRED) - set(META_OPTIONAL)
    if unknown:
        problems.append("header: unknown field(s) " + ", ".join(sorted(unknown)))
    if problems:
        return problems
    if meta["tier"] not in ("A", "B", "C"):
        problems.append("header: tier must be A, B or C")
    if meta["abstain"] not in ("YES", "NO") or meta["fast_card"] not in ("YES", "NO"):
        problems.append("header: abstain and fast_card must be YES or NO")
    if meta["timing"] not in TIMINGS:
        problems.append("header: timing must be one of " + ", ".join(TIMINGS))
    if meta["reference_status"] not in REFERENCE_STATUSES:
        problems.append("header: reference_status must be one of " + ", ".join(REFERENCE_STATUSES))
    if meta["model_stage"] not in MODEL_STAGES:
        problems.append("header: model_stage must be one of " + ", ".join(MODEL_STAGES))
    if meta["reference_status"] in HAS_REFERENCE and not meta.get("reference_frozen_at"):
        problems.append("header: reference_frozen_at is required when a reference exists")
    if not rows:
        return problems + ["no rows: a card with nothing priced must be NO_FORECAST, not PICKS_V2"]
    try:
        expected_tier = R.tier(meta["competition"], root)["tier"]
        if expected_tier != meta["tier"]:
            problems.append(f"header: tier {meta['tier']} but the competition is tier {expected_tier} by rule")
    except Exception as exc:  # the tier rule needs the repository files; a missing one is a finding, not a crash
        problems.append(f"header: tier could not be checked ({type(exc).__name__})")
    seen, strong, informational, ranked = set(), 0, 0, []
    by_quantity: dict[str, set] = {}
    for row in rows:
        name = row["label"] or "<unlabelled>"
        try:
            if row["label"] in seen:
                problems.append(f"{name}: duplicate label")
            seen.add(row["label"])
            if row["family"] not in FAMILIES or row["quantity"] not in QUANTITIES:
                problems.append(f"{name}: family/quantity not in the allowed vocabulary")
            if row["line_source"] not in ("SUPPLIED", "ANALYST_DERIVED"):
                problems.append(f"{name}: line_source must be SUPPLIED or ANALYST_DERIVED")
            w, p, l = (_num(row[k], k, name) for k in ("w", "p", "l"))
            if min(w, p, l) < -1e-9 or abs(w + p + l - 1) > TOLERANCE:
                problems.append(f"{name}: W/P/L must be non-negative and sum to 1 (got {w + p + l:.4f})")
            final = _num(row["final_p"], "final_p", name)
            if not 0 <= final <= 1:
                problems.append(f"{name}: final_p outside [0, 1]")
            if w + l > 0 and abs(final - w / (w + l)) > TOLERANCE:
                problems.append(f"{name}: final_p {final} differs from W/(W+L) = {w / (w + l):.4f}")
            reference = row["reference_p"].strip()
            if meta["reference_status"] in HAS_REFERENCE:
                ref = _num(reference, "reference_p", name)
            elif reference != "NONE":
                problems.append(f"{name}: reference_p must be NONE when reference_status is {meta['reference_status']}")
                ref = None
            else:
                ref = None
            baseline = row["baseline_p"].strip()
            if not MISSING_BASELINE.fullmatch(baseline):
                _num(baseline, "baseline_p", name)
            model = row["model_p"].strip()
            if model != "NONE":
                if meta["model_stage"] != "EXECUTED":
                    problems.append(f"{name}: model_p must be NONE when model_stage is {meta['model_stage']}")
                else:
                    _num(model, "model_p", name)
            implied = row["line_implied_p"].strip()
            if row["line_source"] == "SUPPLIED" and row["family"] in TWO_WAY_FAMILIES:
                if implied != "0.5":
                    problems.append(f"{name}: a supplied two-way line carries line_implied_p 0.5")
            elif implied != "":
                problems.append(f"{name}: line_implied_p applies only to supplied two-way lines")
            expected_info = "Y" if ref is not None and abs(final - ref) >= INFORMATION_DELTA - 1e-9 else "N"
            if row["information_row"] != expected_info:
                problems.append(f"{name}: information_row should be {expected_info} (|final - reference| >= {INFORMATION_DELTA})")
            informational += expected_info == "Y"
            rank = row["most_likely_rank"].strip()
            if rank:
                if not rank.isdigit() or not 1 <= int(rank) <= 4:
                    problems.append(f"{name}: most_likely_rank must be 1-4 or blank")
                else:
                    ranked.append((int(rank), final, row["label"]))
                    if final > SELECTION_CEILING:
                        problems.append(f"{name}: a ranked row may not exceed the {SELECTION_CEILING} selection ceiling")
                    strong += final >= STRONG
            centre, sd, z = (_num(row[k], k, name, allow_blank=True) for k in ("centre", "sd", "z"))
            if row["quantity"] in ("MARGIN", "TOTAL"):
                if centre is None or sd is None or sd <= 0:
                    problems.append(f"{name}: a margin or total row prints a centre and a positive sd")
                else:
                    by_quantity.setdefault(row["quantity"], set()).add((round(centre, 3), round(sd, 3)))
                    t = threshold(row)
                    if t is not None and z is not None and abs(abs(z) - abs(t - centre) / sd) > 0.05:
                        problems.append(f"{name}: |z| {abs(z):.2f} does not match |line - centre| / sd = {abs(t - centre) / sd:.2f}")
                    if t is not None and z is None:
                        problems.append(f"{name}: z is required (line distance in SD)")
        except PicksError as exc:
            problems.append(str(exc))
    for quantity, values in by_quantity.items():
        if len(values) > 1:
            problems.append(f"{quantity}: rows print different centre/sd pairs {sorted(values)}; one distribution per quantity")
        for centre, sd in values:
            floor = R.width_floor(meta["competition"], quantity, root)
            if floor["floor"] is not None and sd < floor["floor"] - 1e-9 and meta.get("width_floor_exception", "NONE") in ("", "NONE"):
                problems.append(f"{quantity}: sd {sd} is below the {floor['basis']} floor {floor['floor']} and no width_floor_exception is written")
    _complements(rows, problems)
    ranked.sort()
    if [r for r, _, _ in ranked] != list(range(1, len(ranked) + 1)):
        problems.append("most_likely_rank values must be consecutive from 1")
    in_order = sorted(ranked, key=lambda x: (-x[1], x[2]))
    if [lab for _, _, lab in ranked] != [lab for _, _, lab in in_order]:
        problems.append("most_likely list must be ordered by decreasing final_p (ties by label)")
    should_abstain = "YES" if strong == 0 and informational == 0 else "NO"
    if meta["abstain"] != should_abstain:
        problems.append(f"header: abstain should be {should_abstain} ({strong} ranked row(s) at >= {STRONG}, {informational} information row(s))")
    return problems


def _complements(rows: list[dict], problems: list[str]) -> None:
    index = {}
    for r in rows:
        if r["family"] in ("TOTAL", "TEAM_TOTAL") and r["side"].upper() in ("OVER", "UNDER"):
            index[(r["family"], r["quantity"], r["line"], r["side"].upper())] = r
        if r["family"] == "HANDICAP" and r["side"].upper() in ("HOME", "AWAY") and r["line"].strip():
            index[(r["family"], r["quantity"], str(float(r["line"]) * (1 if r["side"].upper() == "HOME" else -1)), r["side"].upper())] = r
    for (family, quantity, line, side), r in list(index.items()):
        other = index.get((family, quantity, line, {"OVER": "UNDER", "UNDER": "OVER", "HOME": "AWAY", "AWAY": "HOME"}[side]))
        if other is None or side not in ("OVER", "HOME"):
            continue
        for a, b, name in (("w", "l", "win/loss"), ("l", "w", "loss/win"), ("p", "p", "push")):
            if abs(float(r[a]) - float(other[b])) > TOLERANCE:
                problems.append(f"{r['label']} / {other['label']}: complementary rows disagree on {name} ({r[a]} v {other[b]})")


def lint_card(mini, key: str, root=ROOT) -> tuple[dict, list[dict], list[str]]:
    text = Path(mini).read_text(encoding="utf-8")
    begin, end = f"<!-- BEGIN CARD {key} -->", f"<!-- END CARD {key} -->"
    if text.count(begin) != 1 or text.count(end) != 1:
        raise PicksError(f"{mini} must hold exactly one complete card {key}")
    card = text[text.index(begin): text.index(end) + len(end)]
    meta, rows = parse(block(card, key))
    return meta, rows, lint(meta, rows, root)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    ln = sub.add_parser("lint", help="check a card's PICKS_V2 block")
    ln.add_argument("--mini", type=Path, required=True)
    ln.add_argument("--key", required=True)
    args = parser.parse_args(argv)
    try:
        meta, rows, problems = lint_card(args.mini, args.key)
    except PicksError as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)
    if problems:
        print(f"PICKS_V2 LINT FAILED ({len(problems)}):")
        for p in problems:
            print(" -", p)
        raise SystemExit(1)
    print(f"PICKS_V2 LINT PASSED: {args.key}, tier {meta['tier']}, {len(rows)} rows, abstain {meta['abstain']}")


if __name__ == "__main__":
    main()
