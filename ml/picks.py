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

from ml import ml_separation, reference as R

ROOT = Path(__file__).resolve().parents[1]
BEGIN, END = "<!-- BEGIN PICKS_V2 {key} -->", "<!-- END PICKS_V2 {key} -->"
META_REQUIRED = ("tier", "competition", "reference_id", "reference_status", "model_stage", "abstain", "fast_card", "timing", "scheduled_start",
                 "issued_at")
META_OPTIONAL = ("reference_frozen_at", "width_floor_exception", "tier_basis", "notes", "issue_evidence", "contract_scopes", "rank_scope",
                 "event_key", "external_runs", "external_disagreement", "external_manifest_sha256", "external_packet_sha256", "contract_definitions", "research_mode", "original_scheduled_start",
                 "research_started_at", "not_started_observed_at", "not_started_source", "outcome_exposure",
                 "audit_policy", "audit_event_key", "audit_review", "audit_review_sha256")
# TIMING-v3 (CR-2026.11.15-R1, owner instruction 15 Nov 2026): research that began before the actual start is enough. A card
# finished after the start counts with PREGAME cards when it declares when research began, a not-started observation taken
# at or after that moment (official live page or match centre, with its time) and no outcome exposure.
PRE_START_RESEARCH_FIELDS = ("research_started_at", "not_started_observed_at", "not_started_source", "outcome_exposure")
URL = re.compile(r"https?://\S+")
# FREEZE-v1 (CR-2026.11.11-R1): from this issue time a card names its ranking scope. SUPPLIED_ONLY (the default the request
# template asks for) ranks only the lines the owner supplied, so that the top-two count is not lifted by easy derived lines.
RANK_SCOPES = ("SUPPLIED_ONLY", "ALL")
RANK_SCOPE_FROM = "2026-11-11T00:00:00+11:00"
EVENT_KEY = re.compile(r"(?:EV-\d{8}-[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+|EV2-[A-F0-9]{32})")
SIDES = {"WINNER": ("HOME", "AWAY", "DRAW"), "HANDICAP": ("HOME", "AWAY"), "TOTAL": ("OVER", "UNDER"),
         "TEAM_TOTAL": ("OVER", "UNDER"), "CORNERS": ("OVER", "UNDER", "HOME", "AWAY"),
         "PERIOD": ("HOME", "AWAY", "DRAW", "OVER", "UNDER"), "PLAYER": ("OVER", "UNDER", "YES", "NO"),
         "OTHER": ("HOME", "AWAY", "DRAW", "OVER", "UNDER", "YES", "NO")}
ISSUE_EVIDENCE = re.compile(r"(COMMIT:[0-9a-f]{7,40}|PREGAME_RECEIPT:research/pregame/\S+)")
COLUMNS = ("label", "family", "quantity", "side", "line", "line_source", "reference_p", "baseline_p", "model_p", "final_p", "w", "p", "l",
           "line_implied_p", "centre", "sd", "z", "most_likely_rank", "information_row")
FAMILIES = ("WINNER", "HANDICAP", "TOTAL", "TEAM_TOTAL", "PERIOD", "PLAYER", "CORNERS", "OTHER")
QUANTITIES = ("MARGIN", "TOTAL", "TEAM_TOTAL", "PERIOD", "PLAYER", "COUNT", "N/A")
TIMINGS = ("PREGAME", "PRE_START_RESEARCH", "POST_START_ISSUE", "TIMING_UNVERIFIED")
# Scoring pools these timing labels into one cohort (TIMING-v3): verified pre-start issue and verified pre-start research.
PRE_START_COHORT = ("PREGAME", "PRE_START_RESEARCH")
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


def _when(value: str, name: str):
    """An ISO 8601 time with an explicit UTC offset (BIND-v1): a naive or malformed time is refused, never guessed."""
    from datetime import datetime
    try:
        t = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError:
        raise PicksError(f"header: {name} {value!r} is not an ISO 8601 time") from None
    if t.tzinfo is None:
        raise PicksError(f"header: {name} {value!r} needs a UTC offset")
    return t


def _probability(value, name: str, row: str) -> float:
    v = _num(value, name, row)
    if not 0 <= v <= 1:
        raise PicksError(f"{row}: {name} {v} is outside [0, 1]")
    return v


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


def pre_start_research_problems(meta: dict) -> list[str]:
    from ml import timing
    return timing.problems(meta)


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
    times = {}
    for name in ("scheduled_start", "issued_at", "reference_frozen_at"):
        if meta.get(name):
            try:
                times[name] = _when(meta[name], name)
            except PicksError as exc:
                problems.append(str(exc))
    if "issued_at" in times and "scheduled_start" in times:
        late = times["issued_at"] >= times["scheduled_start"]
        if meta["timing"] == "PREGAME" and late:
            problems.append("header: timing PREGAME but issued_at is not before scheduled_start; use POST_START_ISSUE")
        if meta["timing"] == "POST_START_ISSUE" and not late:
            problems.append("header: timing POST_START_ISSUE but issued_at is before scheduled_start")
        if meta["timing"] == "PRE_START_RESEARCH" and not late:
            problems.append("header: timing PRE_START_RESEARCH but issued_at is before scheduled_start; use PREGAME")
    if meta["timing"] == "PRE_START_RESEARCH":
        problems += pre_start_research_problems(meta)
    if "issued_at" in times and times["issued_at"] >= _when(RANK_SCOPE_FROM, "rank_scope_from") and not meta.get("rank_scope"):
        problems.append("header: rank_scope (SUPPLIED_ONLY or ALL) is required for cards issued under FREEZE-v1")
    if meta.get("rank_scope") and meta["rank_scope"] not in RANK_SCOPES:
        problems.append("header: rank_scope must be SUPPLIED_ONLY or ALL")
    if meta.get("event_key") and not EVENT_KEY.fullmatch(meta["event_key"]):
        problems.append("header: event_key must be the shared external key EV-YYYYMMDD-SPORT-HOME-AWAY (python -m ml external event-key)")
    if meta.get("event_key", "").startswith("EV2-"):
        for field in ("external_manifest_sha256", "external_packet_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", meta.get(field, "")):
                problems.append(f"header: {field} must name the admitted EXT-v2 package")
        if not meta.get("contract_definitions"):
            problems.append("header: EXT-v2 requires contract_definitions (period, endpoint, action and unit)")
    if meta.get("external_runs") and not re.fullmatch(r"[1-9][0-9]?", meta["external_runs"]):
        problems.append("header: external_runs is the number of lane returns merged (1-99)")
    if meta.get("issue_evidence") and not ISSUE_EVIDENCE.fullmatch(meta["issue_evidence"]):
        problems.append("header: issue_evidence must be COMMIT:<sha> or PREGAME_RECEIPT:research/pregame/<key>/<file>")
    if "reference_frozen_at" in times and "issued_at" in times and times["reference_frozen_at"] > times["issued_at"]:
        problems.append("header: reference_frozen_at is after issued_at; the reference must be frozen before the card")
    if not rows:
        return problems + ["no rows: a card with nothing priced must be NO_FORECAST, not PICKS_V2"]
    try:
        expected_tier = R.tier(meta["competition"], root)["tier"]
        if expected_tier != meta["tier"]:
            problems.append(f"header: tier {meta['tier']} but the competition is tier {expected_tier} by rule")
    except Exception as exc:  # the tier rule needs the repository files; a missing one is a finding, not a crash
        problems.append(f"header: tier could not be checked ({type(exc).__name__})")
    try:
        separate_ok = ml_separation.promoted(meta["competition"], root)
    except ValueError as exc:
        problems.append(f"header: {exc}")
        separate_ok = False
    if ml_separation.is_model_reference(meta["reference_id"]) and not separate_ok:
        problems.append(f"header: reference_id {meta['reference_id']} names a fitted model; until a promotion it is a separate shadow, "
                        f"never the card's reference ({ml_separation.RULE})")
    seen, strong, informational, ranked = set(), 0, 0, []
    disagreement = {x.strip() for x in meta.get("external_disagreement", "").split("|") if x.strip()}
    if disagreement - {r["label"] for r in rows}:
        problems.append("header: external_disagreement names an unknown row")
    by_quantity: dict[str, set] = {}
    for row in rows:
        name = row["label"] or "<unlabelled>"
        try:
            if row["label"] in seen:
                problems.append(f"{name}: duplicate label")
            seen.add(row["label"])
            if row["family"] not in FAMILIES or row["quantity"] not in QUANTITIES:
                problems.append(f"{name}: family/quantity not in the allowed vocabulary")
            if row["family"] in SIDES and row["side"].strip().upper() not in SIDES[row["family"]]:
                problems.append(f"{name}: side {row['side']!r} is not valid for {row['family']} ({'/'.join(SIDES[row['family']])})")
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
                ref = _probability(reference, "reference_p", name)
            elif reference != "NONE":
                problems.append(f"{name}: reference_p must be NONE when reference_status is {meta['reference_status']}")
                ref = None
            else:
                ref = None
            baseline = row["baseline_p"].strip()
            if not MISSING_BASELINE.fullmatch(baseline):
                _probability(baseline, "baseline_p", name)
            model = row["model_p"].strip()
            if model != "NONE" and not separate_ok:
                problems.append(f"{name}: model_p must be NONE: fitted-model output is kept separate from cards ({ml_separation.RULE}); "
                                "it is frozen and scored in its own shadow ledger")
            elif model != "NONE":
                if meta["model_stage"] != "EXECUTED":
                    problems.append(f"{name}: model_p must be NONE when model_stage is {meta['model_stage']}")
                else:
                    _probability(model, "model_p", name)
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
                    if row["label"] in disagreement:
                        problems.append(f"{name}: the external runs disagree on this contract (EXT-v1); it stays unranked")
                    if meta.get("rank_scope") == "SUPPLIED_ONLY" and row["line_source"] != "SUPPLIED":
                        problems.append(f"{name}: rank_scope SUPPLIED_ONLY ranks supplied lines only; an ANALYST_DERIVED row stays unranked")
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
    scopes = {}
    for item in meta.get("contract_scopes", "").split("|"):
        if not item.strip():
            continue
        label, sep, scope = item.partition("=")
        if not sep or not scope.strip() or label.strip() in scopes:
            problems.append("header: contract_scopes needs unique LABEL=SCOPE entries")
        else:
            scopes[label.strip()] = scope.strip()
    for row in rows:
        if row["family"] == "TEAM_TOTAL" and row["label"] not in scopes:
            problems.append(f"{row['label']}: TEAM_TOTAL needs an explicit team/period contract_scopes entry")
    if set(scopes) - seen:
        problems.append("header: contract_scopes names an unknown row")
    _complements(rows, problems, scopes)
    _monotonic(rows, problems, scopes)
    ranked.sort()
    if [r for r, _, _ in ranked] != list(range(1, len(ranked) + 1)):
        problems.append("most_likely_rank values must be consecutive from 1")
    in_order = sorted(ranked, key=lambda x: (-x[1], x[2]))
    if [lab for _, _, lab in ranked] != [lab for _, _, lab in in_order]:
        problems.append("most_likely list must be ordered by decreasing final_p (ties by label)")
    should_abstain = "YES" if strong == 0 and informational == 0 else "NO"
    if meta["abstain"] != should_abstain:
        problems.append(f"header: abstain should be {should_abstain} ({strong} ranked row(s) at >= {STRONG}, {informational} information row(s))")
    from ml import audit_controls
    problems += audit_controls.problems(meta, rows, root)
    return problems


def _complements(rows: list[dict], problems: list[str], scopes=None) -> None:
    scopes = scopes or {}
    index = {}
    for r in rows:
        if r["family"] in ("TOTAL", "TEAM_TOTAL") and r["side"].upper() in ("OVER", "UNDER"):
            index[(r["family"], r["quantity"], scopes.get(r["label"], "FULL_MATCH"), r["line"], r["side"].upper())] = r
        if r["family"] == "HANDICAP" and r["side"].upper() in ("HOME", "AWAY") and r["line"].strip():
            try:
                line = str(float(r["line"]) * (1 if r["side"].upper() == "HOME" else -1))
            except ValueError:
                continue
            index[(r["family"], r["quantity"], scopes.get(r["label"], "FULL_MATCH"), line, r["side"].upper())] = r
    for (family, quantity, scope, line, side), r in list(index.items()):
        other = index.get((family, quantity, scope, line, {"OVER": "UNDER", "UNDER": "OVER", "HOME": "AWAY", "AWAY": "HOME"}[side]))
        if other is None or side not in ("OVER", "HOME"):
            continue
        for a, b, name in (("w", "l", "win/loss"), ("l", "w", "loss/win"), ("p", "p", "push")):
            if abs(float(r[a]) - float(other[b])) > TOLERANCE:
                problems.append(f"{r['label']} / {other['label']}: complementary rows disagree on {name} ({r[a]} v {other[b]})")


def _monotonic(rows: list[dict], problems: list[str], scopes=None) -> None:
    """Nested contracts must have nested unconditional win/loss events, including integer pushes."""
    groups = {}; scopes = scopes or {}
    for row in rows:
        if row["family"] not in ("TOTAL", "TEAM_TOTAL", "HANDICAP"):
            continue
        try:
            line, w, loss = (float(row[k]) for k in ("line", "w", "l"))
        except (ValueError, KeyError):
            continue                       # the row validator reports malformed numbers
        if not all(math.isfinite(v) for v in (line, w, loss)):
            continue
        groups.setdefault((row["family"], row["quantity"], scopes.get(row["label"], "FULL_MATCH"), row["side"].upper()), []).append((line, w, loss, row["label"]))
    for (family, _, _, side), group in groups.items():
        ordered = sorted(group)
        increasing = family == "HANDICAP" or side == "UNDER"
        for lo, hi in zip(ordered, ordered[1:]):
            if lo[0] == hi[0]:
                bad = abs(lo[1] - hi[1]) > TOLERANCE or abs(lo[2] - hi[2]) > TOLERANCE
            elif increasing:
                bad = hi[1] < lo[1] - TOLERANCE or hi[2] > lo[2] + TOLERANCE
            else:
                bad = hi[1] > lo[1] + TOLERANCE or hi[2] < lo[2] - TOLERANCE
            if bad:
                problems.append(f"{lo[3]} / {hi[3]}: nested contracts violate probability monotonicity")


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
