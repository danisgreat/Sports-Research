"""PICKS-v2 lint, the adjustment ledger, benchmarks and coverage (LEDGER-v1 / BENCH-v1 / WIDTH-v1).

Synthetic EXAMPLE competitions and LOCAL-EXAMPLE keys only."""
import csv
import io
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from ml import benchmarks as B, ledger as L, picks as P, reference as R
from ml.tests.test_reference import PARAMS, _row, _write

KEY = "LOCAL-EXAMPLE-G0001"
META = dict(tier="B", competition="Basketball/EXAMPLE-B", reference_id="BASELINE_LEAGUE_V1:COMPETITION_ROW:Basketball/EXAMPLE-B",
            reference_status="BASELINE_ONLY", reference_frozen_at="2026-10-22T01:00:00+00:00", model_stage="NOT_RUN_NO_RELEASE", abstain="NO",
            fast_card="NO", timing="PREGAME", scheduled_start="2026-10-22T10:00:00+00:00", issued_at="2026-10-22T09:30:00+00:00")


def good_rows():
    def r(**kw):
        base = dict(label="", family="TOTAL", quantity="TOTAL", side="OVER", line="170.5", line_source="SUPPLIED", reference_p="0.5000",
                    baseline_p="0.5000", model_p="NONE", final_p="0.5200", w="0.5200", p="0.0000", l="0.4800", line_implied_p="0.5",
                    centre="170", sd="17", z="0.03", most_likely_rank="", information_row="N")
        base.update(kw)
        return base
    return [r(label="HOME_ML", family="WINNER", quantity="MARGIN", side="HOME", line="", reference_p="0.6200", baseline_p="0.6000", final_p="0.6600",
              w="0.6600", l="0.3400", line_implied_p="", centre="5", sd="13", z="0.38", most_likely_rank="1", information_row="Y"),
            r(label="OVER_170.5", reference_p="0.5200"),
            r(label="UNDER_170.5", side="UNDER", reference_p="0.4800", final_p="0.4800", w="0.4800", l="0.5200")]


def render(meta=None, rows=None, key=KEY):
    meta, rows = dict(META, **(meta or {})), rows if rows is not None else good_rows()
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=P.COLUMNS, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    head = "\n".join(f"{k}: {v}" for k, v in meta.items())
    return f"<!-- BEGIN PICKS_V2 {key} -->\n```text\n{head}\n\n{out.getvalue()}```\n<!-- END PICKS_V2 {key} -->"


@pytest.fixture
def root(tmp_path):
    _write(tmp_path / R.RELEASES, [dict(competition="Basketball/EXAMPLE-A", endpoint="E", active_experimental_release="EX-1", release_path="x",
                                        release_sha256="x", source_code_sha256="x", qualification="X", prospective_events="0")])
    _write(tmp_path / R.STORE_EVENTS, [dict(event_uid=f"E{i}", competition="Basketball/EXAMPLE-B", endpoint="E", native_event_id=str(i), identity_basis="N",
                                            season="2025", event_at="2025-01-01T00:00:00+00:00", home="a", away="b", venue="", ingest_seq="1")
                                       for i in range(R.MIN_STORE_EVENTS)])
    _write(tmp_path / L.EFFECTS, [dict(row_id="E-EX-REST", factor="rest", competition="Basketball/EXAMPLE-B", target="home margin", estimate="2.0",
                                       se="", ci_low="", ci_high="", unit="points", n="", period="", status="MEASURED_NOT_CONFIRMED",
                                       out_of_sample="", source="", data_needed=""),
                                  dict(row_id="E-EX-NULL", factor="null", competition="Basketball/EXAMPLE-B", target="total", estimate="0.1",
                                       se="", ci_low="", ci_high="", unit="points", n="", period="", status="MEASURED_NULL",
                                       out_of_sample="", source="", data_needed="")])
    _write(tmp_path / R.PARAMETERS, [_row(row_type="COMPETITION", competition="Basketball/EXAMPLE-B", usable="USABLE_DEVELOPMENT", family="BASKETBALL",
                                          mean_total="170", mean_home_margin="3", raw_margin_sd="13.5", raw_total_sd="17.5", resid_margin_sd="12.0",
                                          resid_total_sd="16.5", evidence_class="X", dev_last_date="2026-06-01")])
    return tmp_path


def lint(root, meta=None, rows=None):
    parsed_meta, parsed_rows = P.parse(P.block(render(meta, rows), KEY))
    return P.lint(parsed_meta, parsed_rows, root)


def test_a_clean_block_lints_clean(root):
    assert lint(root) == []


def test_parse_requires_exact_columns_and_one_block():
    with pytest.raises(P.PicksError, match="exactly one complete PICKS_V2"):
        P.block("no block", KEY)
    with pytest.raises(P.PicksError, match="columns must be exactly"):
        P.parse("tier: A\n\nlabel,family\nx,y")
    with pytest.raises(P.PicksError, match="blank line"):
        P.parse("tier: A")


@pytest.mark.parametrize("meta,needle", [
    (dict(tier="A"), "tier A but the competition is tier B"),
    (dict(timing="LATE"), "timing must be"),
    (dict(abstain="MAYBE"), "abstain and fast_card"),
    (dict(model_stage="ALMOST"), "model_stage must be"),
    (dict(reference_frozen_at=""), "reference_frozen_at is required"),
])
def test_header_problems(root, meta, needle):
    problems = lint(root, meta)
    assert any(needle in p for p in problems), problems


def test_missing_header_field_is_reported(root):
    meta = dict(META)
    del meta["competition"]
    parsed_meta, rows = P.parse(P.block(render(None, None), KEY))
    parsed_meta.pop("competition")
    assert lint_ok(P.lint(parsed_meta, rows, root), "missing competition")


def lint_ok(problems, needle):
    return any(needle in p for p in problems)


def edit(rows, label, **kw):
    return [dict(r, **kw) if r["label"] == label else r for r in rows]


@pytest.mark.parametrize("label,change,needle", [
    ("OVER_170.5", dict(w="0.60"), "sum to 1"),
    ("OVER_170.5", dict(final_p="0.60"), "differs from W/(W+L)"),
    ("OVER_170.5", dict(line_implied_p=""), "carries line_implied_p 0.5"),
    ("HOME_ML", dict(line_implied_p="0.5"), "only to supplied two-way lines"),
    ("HOME_ML", dict(information_row="N"), "information_row should be Y"),
    ("OVER_170.5", dict(information_row="Y"), "information_row should be N"),
    ("HOME_ML", dict(model_p="0.61"), "model_p must be NONE"),
    ("HOME_ML", dict(reference_p="NONE"), "must be a number"),
    ("HOME_ML", dict(baseline_p="maybe"), "baseline_p must be a number"),
    ("HOME_ML", dict(z="2.00"), "does not match"),
    ("HOME_ML", dict(sd=""), "centre and a positive sd"),
    ("HOME_ML", dict(family="CRICKET"), "allowed vocabulary"),
    ("HOME_ML", dict(line_source="GUESSED"), "SUPPLIED or ANALYST_DERIVED"),
    ("HOME_ML", dict(most_likely_rank="7"), "must be 1-4"),
])
def test_row_problems(root, label, change, needle):
    problems = lint(root, rows=edit(good_rows(), label, **change))
    assert any(needle in p for p in problems), (needle, problems)


@pytest.mark.parametrize("label,change,needle", [
    ("HOME_ML", dict(reference_p="9"), "reference_p 9.0 is outside [0, 1]"),
    ("HOME_ML", dict(baseline_p="1.2"), "baseline_p 1.2 is outside [0, 1]"),
    ("HOME_ML", dict(baseline_p="-2"), "baseline_p -2.0 is outside [0, 1]"),
    ("HOME_ML", dict(side="OVER"), "not valid for WINNER"),
    ("OVER_170.5", dict(side="HOME"), "not valid for TOTAL"),
])
def test_comparators_and_sides_are_bounded(root, label, change, needle):
    """BIND-v1 (review 2026-11-08): comparator probabilities of 9, 1.2 and -2 and invalid sides were accepted."""
    problems = lint(root, rows=edit(good_rows(), label, **change))
    assert any(needle in p for p in problems), (needle, problems)


def test_model_p_is_bounded_when_the_model_ran(root):
    problems = lint(root, dict(model_stage="EXECUTED"), rows=edit(good_rows(), "HOME_ML", model_p="1.5"))
    assert any("model_p 1.5 is outside [0, 1]" in p for p in problems), problems


@pytest.mark.parametrize("meta,needle", [
    (dict(issued_at="2026-13-40T09:30:00+00:00"), "issued_at '2026-13-40T09:30:00+00:00' is not an ISO 8601 time"),
    (dict(scheduled_start="tonight"), "is not an ISO 8601 time"),
    (dict(issued_at="2026-10-22T09:30:00"), "needs a UTC offset"),
    (dict(issued_at="2026-10-22T10:05:00+00:00"), "timing PREGAME but issued_at is not before scheduled_start"),
    (dict(timing="POST_START_ISSUE"), "timing POST_START_ISSUE but issued_at is before scheduled_start"),
    (dict(reference_frozen_at="2026-10-22T09:45:00+00:00"), "reference_frozen_at is after issued_at"),
    (dict(issue_evidence="trust me"), "issue_evidence must be"),
])
def test_dates_and_timing_follow_the_evidence(root, meta, needle):
    problems = lint(root, meta)
    assert any(needle in p for p in problems), (needle, problems)


def test_ranked_rows_may_not_exceed_the_selection_ceiling_and_must_be_ordered(root):
    rows = edit(good_rows(), "HOME_ML", final_p="0.9300", w="0.9300", l="0.0700", reference_p="0.62")
    assert any("selection ceiling" in p for p in lint(root, rows=rows))
    two = edit(edit(good_rows(), "OVER_170.5", most_likely_rank="2", final_p="0.7000", w="0.7000", l="0.3000"), "UNDER_170.5", final_p="0.3000", w="0.3000", l="0.7000")
    assert any("ordered by decreasing final_p" in p for p in lint(root, rows=two))


def test_complementary_total_rows_must_agree(root):
    rows = edit(good_rows(), "UNDER_170.5", w="0.4000", l="0.6000", final_p="0.4000")
    assert any("complementary rows disagree" in p for p in lint(root, rows=rows))


def test_one_distribution_per_quantity_and_the_width_floor(root):
    rows = edit(good_rows(), "UNDER_170.5", sd="18")
    assert any("different centre/sd pairs" in p for p in lint(root, rows=rows))
    narrow = [dict(r, sd="14.0") if r["quantity"] == "TOTAL" else r for r in good_rows()]          # floor is 16.5
    assert any("below the COMPETITION_ROW floor 16.5" in p for p in lint(root, rows=narrow))
    excused = lint(root, meta=dict(width_floor_exception="injury-reduced rotation, 6 men out; SD from the lineup mixture"), rows=narrow)
    assert not any("floor" in p for p in excused)


def test_abstain_follows_from_the_numbers(root):
    weak = [dict(r, most_likely_rank="", information_row="N", final_p=r["reference_p"], w=r["reference_p"], l=f"{1 - float(r['reference_p']):.4f}") for r in good_rows()]
    weak = edit(weak, "UNDER_170.5", reference_p="0.5000", final_p="0.5000", w="0.5000", l="0.5000")
    weak = edit(weak, "OVER_170.5", reference_p="0.5000", final_p="0.5000", w="0.5000", l="0.5000")
    assert any("abstain should be YES" in p for p in lint(root, rows=weak))
    assert lint(root, meta=dict(abstain="YES"), rows=weak) == []
    assert any("abstain should be NO" in p for p in lint(root, meta=dict(abstain="YES")))


def test_a_reference_is_required_when_the_status_says_one_exists_and_forbidden_otherwise(root):
    none = [dict(r, reference_p="NONE", information_row="N") for r in good_rows()]
    assert any("must be a number" in p for p in lint(root, rows=none))
    ok = lint(root, meta=dict(reference_status="NOT_AVAILABLE", reference_frozen_at="", abstain="YES"), rows=[dict(r, most_likely_rank="") for r in none])
    assert ok == []


def test_the_model_stage_may_carry_a_challenger_probability(root):
    rows = edit(good_rows(), "HOME_ML", model_p="0.5800")
    assert lint(root, meta=dict(model_stage="EXECUTED"), rows=rows) == []


ADJ = dict(adjustment_id="A1", effect_row_id="E-EX-REST", fact="away team on a back-to-back", target="MARGIN", unit="points",
           applied_size="1.0", entry="HALF", source_url="https://example.org/schedule", published_at="2026-10-21T00:00:00+00:00",
           retrieved_at="2026-10-22T08:00:00+00:00", corroboration="league schedule", overlap_check="NONE_FOUND", centre_before="4",
           centre_after="5", counterfactual="HOME_ML=0.6200")


def adjustments(rows=None):
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=L.ADJ_COLUMNS, lineterminator="\n")
    w.writeheader()
    w.writerows(rows if rows is not None else [ADJ])
    return f"<!-- BEGIN ADJUSTMENTS_V1 {KEY} -->\n```text\n{out.getvalue()}```\n<!-- END ADJUSTMENTS_V1 {KEY} -->"


def mini(tmp_path, block, adj=None):
    p = tmp_path / "MINI.md"
    adj = adjustments() if adj is None else adj
    p.write_text(f"# mini\n<!-- BEGIN CARD {KEY} -->\ncard text\n{block}\n{adj}\n<!-- END CARD {KEY} -->\n# footer\n", encoding="utf-8")
    return p


def test_lint_card_reads_the_block_from_the_mini(root, tmp_path):
    meta, rows, problems = P.lint_card(mini(tmp_path, render()), KEY, root)
    assert problems == [] and len(rows) == 3 and meta["tier"] == "B"
    with pytest.raises(P.PicksError):
        P.lint_card(mini(tmp_path, "no picks here"), KEY, root)


# ------------------------------------------------------------------ the ledger
def test_ledger_add_refuses_a_failing_card_and_a_second_entry(root, tmp_path):
    bad = mini(tmp_path, render(rows=edit(good_rows(), "OVER_170.5", w="0.60")))
    with pytest.raises(L.LedgerError, match="does not lint clean"):
        L.add(bad, KEY, root=root)
    assert not (root / L.LEDGER).exists()
    good = mini(tmp_path, render())
    added = L.add(good, KEY, root=root)
    # LEDGER-v2: the card claims PREGAME but no receipt or commit proves it, so the ledger records TIMING_UNVERIFIED.
    assert added["rows"] == 3 and added["timing"] == "TIMING_UNVERIFIED" and added["adjustments"] == 1
    frame = L.read(root / L.LEDGER)
    assert len(frame) == 3 and set(frame["local_key"]) == {KEY} and tuple(frame.columns) == L.FIELDS
    assert set(frame["timing"]) == {"TIMING_UNVERIFIED"} and set(frame["timing_claimed"]) == {"PREGAME"}
    adj = L.read_adjustments(root / L.ADJUSTMENTS)
    assert len(adj) == 1 and adj["effect_status"][0] == "MEASURED_NOT_CONFIRMED" and len(adj["effect_version"][0]) == 64
    with pytest.raises(L.LedgerError, match="already in the ledger"):
        L.add(good, KEY, root=root)


def test_ledger_rejects_a_changed_header_and_duplicate_rows(root, tmp_path):
    L.add(mini(tmp_path, render()), KEY, root=root)
    path = root / L.LEDGER
    path.write_text(path.read_text().replace("local_key,", "key,", 1))
    with pytest.raises(L.LedgerError, match="header changed"):
        L.read(path)


def _synthetic_ledger(tmp_path, n_cards=80, seed=3):
    """Cards whose reference is right, whose analyst moved some rows by a known fraction of the true logit shift."""
    rng = np.random.default_rng(seed)
    rows, results = [], []
    for i in range(n_cards):
        key = f"LOCAL-EXAMPLE-G{i:04d}"
        true_logit = rng.normal(0, 1.0)
        shift = rng.normal(0, 0.6)                      # information the analyst saw; half of it is real (lambda = 0.5 is the truth)
        ref = 1 / (1 + np.exp(-true_logit))
        final = 1 / (1 + np.exp(-(true_logit + shift)))
        outcome = rng.random() < 1 / (1 + np.exp(-(true_logit + 0.5 * shift)))
        week = pd.Timestamp("2026-10-05T10:00:00Z") + pd.Timedelta(days=7 * (i % 12))
        rows.append(dict(local_key=key, competition="Basketball/EXAMPLE-B", tier="B", timing="PREGAME", scheduled_start=week.isoformat(),
                         issued_at=week.isoformat(), reference_id="X", reference_status="EXECUTED", abstain="NO", fast_card="NO",
                         label="HOME_ML", family="WINNER", quantity="MARGIN", side="HOME", line="", line_source="SUPPLIED",
                         reference_p=f"{ref:.4f}", baseline_p="0.5000", model_p="NONE", final_p=f"{final:.4f}", w=f"{final:.4f}", p="0.0000",
                         l=f"{1 - final:.4f}", line_implied_p="", centre="3", sd="13", z="0.2", most_likely_rank="1",
                         information_row="Y" if abs(final - ref) >= 0.03 else "N"))
        rows.append(dict(rows[-1], label="OVER_170.5", family="TOTAL", quantity="TOTAL", side="OVER", line="170.5", line_implied_p="0.5",
                         reference_p="0.5000", final_p="0.5000", w="0.5000", l="0.5000", centre="170", sd="17", information_row="N", most_likely_rank=""))
        results += [dict(local_key=key, label="HOME_ML", grade="WIN" if outcome else "LOSS"),
                    dict(local_key=key, label="OVER_170.5", grade="WIN" if rng.random() < 0.5 else "LOSS")]
    path = tmp_path / "ADJUSTMENT_LEDGER.csv"
    path.write_bytes(L._csv(rows, L.FIELDS))
    pd.DataFrame(results).to_csv(tmp_path / "RESULTS.csv", index=False)
    return path, tmp_path / "RESULTS.csv"


def test_score_reports_paired_differences_on_identical_rows(tmp_path):
    ledger, results = _synthetic_ledger(tmp_path)
    out = L.score(ledger, results)
    strata = {r["stratum"] for r in out["scores"]}
    assert strata == {"timing=PREGAME|card=FULL|line=SUPPLIED|reference=EXECUTED"}
    by = {(r["scope"], r["comparison"]): r for r in out["scores"]}
    row = by[("ALL_IN_STRATUM", "final minus reference")]
    assert row["n_rows"] == 160 and row["n_events"] == 80 and row["k_weeks"] == 12
    assert by[("INFORMATION_ROWS", "final minus reference")]["n_rows"] <= row["n_rows"]
    assert ("ALL_IN_STRATUM", "final minus line-implied 0.5") in by and ("ALL_IN_STRATUM", "final minus league baseline") in by
    assert out["rows"] == 160 and out["events"] == 80 and out["calibration"]["n"] == 160


def test_score_never_pools_timing_card_or_line_strata(tmp_path):
    """Review 2026-11-08: timing, fast/full and supplied/derived cohorts were pooled; each stratum is now scored alone."""
    ledger, results = _synthetic_ledger(tmp_path)
    frame = L.read(ledger)
    frame.loc[frame.index % 4 == 0, "timing"] = "POST_START_ISSUE"
    frame.loc[frame.index % 4 == 1, "fast_card"] = "YES"
    frame.loc[frame.index % 4 == 2, "line_source"] = "ANALYST_DERIVED"
    ledger.write_bytes(L._csv(frame.to_dict("records"), L.FIELDS))
    out = L.score(ledger, results)
    strata = {r["stratum"] for r in out["scores"]}
    assert any("timing=POST_START_ISSUE" in s for s in strata) and any("card=FAST" in s for s in strata)
    assert any("line=ANALYST_DERIVED" in s for s in strata)
    for r in out["scores"]:
        assert r["n_rows"] < 160            # no row pools every stratum
    assert out["lam"]["status"] in ("BY_STRATUM", "NOT_ESTIMATED", "ESTIMATED") and len(out["lambda_by_stratum"]) == len(strata)


def _adj_problems(root, change=None, rows=None, adj_rows=None):
    meta, picks_rows = P.parse(P.block(render(None, rows), KEY))
    a = [dict(ADJ, **(change or {}))] if adj_rows is None else adj_rows
    return L.check_adjustments(a, meta, picks_rows, root)


@pytest.mark.parametrize("change,needle", [
    (dict(effect_row_id="E-NOPE"), "not in EFFECT_TABLES.csv"),
    (dict(effect_row_id="E-EX-NULL"), "MEASURED_NULL"),
    (dict(entry="FULL"), "enters HALF, not FULL"),
    (dict(applied_size="2.0"), "is not the table estimate 2.0 at HALF"),
    (dict(published_at="2026-10-23T00:00:00+00:00"), "published_at <= retrieved_at <= issued_at"),
    (dict(source_url="a friend"), "source_url must be"),
    (dict(overlap_check=""), "overlap_check must name"),
    (dict(counterfactual="NOPE=0.5"), "not a PICKS_V2 row"),
    (dict(counterfactual="HOME_ML=1.4"), "must be in [0, 1]"),
    (dict(counterfactual=""), "counterfactual must give"),
])
def test_adjustments_must_match_the_effect_table_and_the_evidence(root, change, needle):
    problems = _adj_problems(root, change)
    assert any(needle in p for p in problems), (needle, problems)


def test_a_moved_row_needs_an_adjustment_block_and_adjustments_are_immutable(root, tmp_path):
    assert any("no ADJUSTMENTS_V1 block" in p for p in _adj_problems(root, adj_rows=[]))
    with pytest.raises(L.LedgerError, match="no ADJUSTMENTS_V1 block"):
        L.add(mini(tmp_path, render(), adj=""), KEY, root=root)
    L.add(mini(tmp_path, render()), KEY, root=root)
    path = root / L.ADJUSTMENTS
    path.write_text(path.read_text().replace("back-to-back", "rested"))
    with pytest.raises(L.LedgerError, match="chain broken"):
        L.read_adjustments(path)


def test_a_late_card_labelled_pregame_is_refused_and_a_receipt_verifies_timing(root, tmp_path):
    late = mini(tmp_path, render(dict(issued_at="2026-10-22T10:30:00+00:00")))
    with pytest.raises(L.LedgerError, match="timing PREGAME but issued_at is not before scheduled_start"):
        L.add(late, KEY, root=root)
    good = mini(tmp_path, render())
    card = L._card_text(good, KEY)
    receipt = root / "research" / "pregame" / KEY / "20261022T093500000000Z_PREGAME.csv"
    receipt.parent.mkdir(parents=True)
    receipt.write_bytes(L._csv([dict(local_key=KEY, status="EXECUTED", card_block_sha256=L._sha(card.encode("utf-8")),
                                     run_at="2026-10-22T09:35:00+00:00")], ["local_key", "status", "card_block_sha256", "run_at"]))
    assert L.add(good, KEY, root=root)["timing"] == "PREGAME"
    assert set(L.read(root / L.LEDGER)["timing_evidence"]) == {"PREGAME_RECEIPT:" + receipt.relative_to(root).as_posix()}


def test_lambda_recovers_the_true_value_and_refuses_small_samples():
    rng = np.random.default_rng(5)
    shift = rng.normal(0, 0.8, 4000)
    base = rng.normal(0, 1.0, 4000)
    ref = 1 / (1 + np.exp(-base))
    final = 1 / (1 + np.exp(-(base + shift)))
    y = rng.random(4000) < 1 / (1 + np.exp(-(base + 0.5 * shift)))
    est = L.adjustment_lambda(ref, final, y)
    assert est["status"] == "ESTIMATED" and abs(est["lam"] - 0.5) < 3 * est["se"] + 0.02
    small = L.adjustment_lambda(ref[:30], final[:30], y[:30])
    assert small["status"] == "NOT_ESTIMATED" and "40 needed" in small["reason"]
    unchanged = L.adjustment_lambda(ref, ref, y)
    assert unchanged["status"] == "NOT_ESTIMATED"


def test_only_decisive_rows_are_scored(tmp_path):
    ledger, results = _synthetic_ledger(tmp_path, n_cards=10)
    r = pd.read_csv(results)
    r.loc[r.index[:6], "grade"] = ["PUSH", "VOID", "UNRESOLVED", "PUSH", "VOID", "UNRESOLVED"]
    r.to_csv(results, index=False)
    assert L.score(ledger, results)["rows"] == 14


def test_coverage_reports_z_rms_against_the_band(tmp_path):
    ledger, _ = _synthetic_ledger(tmp_path, n_cards=60)
    rng = np.random.default_rng(2)
    rows = []
    for i in range(60):
        key = f"LOCAL-EXAMPLE-G{i:04d}"
        rows += [dict(local_key=key, quantity="MARGIN", actual=3 + rng.normal(0, 13)), dict(local_key=key, quantity="TOTAL", actual=170 + rng.normal(0, 17))]
    pd.DataFrame(rows).to_csv(tmp_path / "ACTUALS.csv", index=False)
    cov = {r["quantity"]: r for r in L.coverage(ledger, tmp_path / "ACTUALS.csv")}
    assert cov["MARGIN"]["cards"] == 60 and cov["MARGIN"]["status"] == "WITHIN_BAND" and cov["TOTAL"]["status"] == "WITHIN_BAND"
    wide = [dict(r, actual=3 + 30 * (1 if i % 2 else -1)) if r["quantity"] == "MARGIN" else r for i, r in enumerate(rows)]
    pd.DataFrame(wide).to_csv(tmp_path / "ACTUALS2.csv", index=False)
    assert {r["quantity"]: r for r in L.coverage(ledger, tmp_path / "ACTUALS2.csv")}["MARGIN"]["status"] == "OUTSIDE_BAND"
    few = pd.DataFrame(rows[:20])
    few.to_csv(tmp_path / "ACTUALS3.csv", index=False)
    assert L.coverage(ledger, tmp_path / "ACTUALS3.csv")[0]["status"] == "INSUFFICIENT_EVIDENCE"


# ------------------------------------------------------------------ benchmarks
def bench(tmp_path, **kw):
    row = dict(local_key=KEY, label="HOME_ML", benchmark_id="NOVIG_CLOSE", p="0.61", method="POWER", source_url="https://example.org/close",
               retrieved_at="2026-10-22T13:00:00+00:00", final_at="2026-10-22T12:00:00+00:00")
    row.update(kw)
    path = tmp_path / "BENCH.csv"
    path.write_bytes(L._csv([row], list(row)))
    return path


def test_benchmarks_load_when_entered_after_the_final(tmp_path):
    frame = B.load(bench(tmp_path))
    assert frame.p.iloc[0] == 0.61 and frame.benchmark_id.iloc[0] == "NOVIG_CLOSE"


@pytest.mark.parametrize("change,needle", [
    (dict(retrieved_at="2026-10-22T11:00:00+00:00"), "after the verified final"),
    (dict(method="GUESS"), "named de-vig method"),
    (dict(p="1.2"), "strictly between"),
    (dict(benchmark_id="LINE_IMPLIED"), "benchmark_id must be one of"),
    (dict(source_url="http://example.org"), "HTTPS"),
    (dict(final_at="2026-10-22T12:00:00"), "UTC offset"),
])
def test_benchmark_refusals(tmp_path, change, needle):
    with pytest.raises(B.BenchmarkError, match=needle):
        B.load(bench(tmp_path, **change))


def test_a_price_column_cannot_enter_the_repository(tmp_path):
    path = bench(tmp_path, decimal_odds="1.65")
    with pytest.raises(B.BenchmarkError, match="no price, odds or line-movement field"):
        B.load(path)


def test_scoring_includes_a_hand_entered_benchmark(tmp_path):
    ledger, results = _synthetic_ledger(tmp_path, n_cards=20)
    rows = [dict(local_key=f"LOCAL-EXAMPLE-G{i:04d}", label="HOME_ML", benchmark_id="NOVIG_CLOSE", p="0.55", method="POWER",
                 source_url="https://example.org/close", retrieved_at="2026-11-01T00:00:00+00:00", final_at="2026-10-31T00:00:00+00:00") for i in range(20)]
    path = tmp_path / "B.csv"
    path.write_bytes(L._csv(rows, B.FIELDS))
    out = L.score(ledger, results, path)
    assert any(r["comparison"] == "final minus NOVIG_CLOSE" and r["n_rows"] == 20 for r in out["scores"])



def test_a_superseded_effect_row_cannot_be_used(root):
    """REGIME-v3: re-estimated rows are appended and the old row is retired in SUPERSEDED.csv, never overwritten."""
    _write(root / L.SUPERSEDED, [dict(row_id="E-EX-REST", superseded_by="E-EX-REST-R2", superseded_at="2026-11-08", reason="test")])
    assert any("superseded by E-EX-REST-R2" in p for p in _adj_problems(root))


def test_the_live_regime_rows_follow_the_chronological_evidence():
    effects, retired = L.effect_rows(), L.superseded()
    assert effects["E-NBA-PLAYOFF-TOTAL-R2"]["status"] == "MEASURED_CONFIRMED"
    for row in ("E-MLB-POSTSEASON-TOTAL-R2", "E-NRL-EARLY-TOTAL-R2", "E-AFL-FINALS-TOTAL-R2"):
        assert effects[row]["status"] == "MEASURED_NOT_CONFIRMED"
    assert {r: retired[r] for r in ("E-NBA-PLAYOFF-TOTAL", "E-MLB-POSTSEASON-TOTAL", "E-NRL-EARLY-TOTAL", "E-AFL-FINALS-TOTAL")} == {
        r: r + "-R2" for r in ("E-NBA-PLAYOFF-TOTAL", "E-MLB-POSTSEASON-TOTAL", "E-NRL-EARLY-TOTAL", "E-AFL-FINALS-TOTAL")}
