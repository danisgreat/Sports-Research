"""REFMODEL-v1 / WIDTH-v1: tiers, TB-1-MD and TB-2-MD, width floors and the tier B/C reference stage.

Synthetic EXAMPLE competitions only for the filesystem tests; the TB-1-MD arithmetic is checked against the toolkit's worked example."""
import csv
import io
from pathlib import Path

import pytest
from scipy import stats

from ml import config, reference as R


def _write(path: Path, rows: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=list(rows[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    path.write_bytes(out.getvalue().encode())


def test_constants_equal_the_validated_toolkit_constants():
    for key, spec in R.TB1_MD.items():
        if key in config.TB1_VALIDATED and spec["kind"] == "normal":
            c = config.TB1_VALIDATED[key]
            assert (spec["k"], spec["sd_margin"], spec["sd_total"], spec["he"]) == (c.k, c.sd_margin, c.sd_total, c.home_edge), key
    assert R.TB1_MD["Premier League"]["he"] == config.TB1_VALIDATED["Premier League"].home_edge


# The toolkit section 4.2 worked example (NBL, k = 5, LM = 91.25, HE = +1.57).
NBL = dict(lm=91.25, home=dict(team="H", pf=1195, pa=1102, n=13), away=dict(team="A", pf=1150, pa=1231, n=13))


def test_tb1_average_form_reproduces_the_toolkit_worked_example():
    c = R.tb1_centre(R.TB1_MD["NBL"], NBL, form="average")
    assert c["total"] == pytest.approx(180.64, abs=0.01) and c["margin"] == pytest.approx(6.40, abs=0.01)
    assert float(stats.norm.cdf(c["margin"] / 15.2)) == pytest.approx(0.663, abs=0.002)


def test_tb2_additive_form_doubles_the_net_rating_signal_and_keeps_the_home_edge():
    avg, add = R.tb1_centre(R.TB1_MD["NBL"], NBL, form="average"), R.tb1_centre(R.TB1_MD["NBL"], NBL, form="additive")
    he = R.TB1_MD["NBL"]["he"]
    assert (add["margin"] - he) == pytest.approx(2 * (avg["margin"] - he))         # net rating difference, not half of it
    assert add["total"] == pytest.approx(91.74 + 93.74 + 89.24 + 86.57 - 2 * 91.25, abs=0.05)       # the toolkit rounds each rating to 2 dp
    neutral = R.tb1_centre(R.TB1_MD["NBL"], NBL, neutral=True, form="additive")
    assert neutral["margin"] == pytest.approx(add["margin"] - he)
    with pytest.raises(R.ReferenceError_):
        R.tb1_centre(R.TB1_MD["NBL"], NBL, form="bogus")


def test_early_season_is_flagged_and_equal_teams_get_only_the_home_edge():
    even = dict(lm=100.0, home=dict(team="H", pf=0, pa=0, n=0), away=dict(team="A", pf=0, pa=0, n=0))
    c = R.tb1_centre(R.TB1_MD["NBA"], even, form="additive")
    assert "TB1_EARLY_SEASON" in c["flags"] and c["margin"] == pytest.approx(1.71) and c["total"] == pytest.approx(200.0)


def test_default_form_by_kind():
    assert R.default_form("NBA") == "additive" and R.default_form("Premier League") == "average"


def test_grid_prices_are_coherent_and_complements_agree():
    grid, info = R.tb1_grid("Basketball/NBL", NBL)
    rows = R.price_rows(grid, [dict(label="HOME_ML", family="winner", side="HOME", line=""),
                               dict(label="HOME_M5", family="handicap", side="HOME", line="-5.5"),
                               dict(label="AWAY_P5", family="handicap", side="AWAY", line="5.5"),
                               dict(label="O180", family="total", side="OVER", line="180.5"),
                               dict(label="U180", family="total", side="UNDER", line="180.5"),
                               dict(label="O180i", family="total", side="OVER", line="180")])
    by = {r["label"]: r for r in rows}
    assert all(abs(r["w"] + r["p"] + r["l"] - 1) < 1e-4 for r in rows)
    assert by["HOME_M5"]["w"] == pytest.approx(by["AWAY_P5"]["l"], abs=1e-5)
    assert by["O180"]["w"] == pytest.approx(by["U180"]["l"], abs=1e-5) and by["O180i"]["p"] > 0       # an integer line can push
    assert by["HOME_ML"]["p_decisive"] > 0.5 and info["form"] == "additive" and info["key"] == "NBL"


def test_a_winner_row_with_an_unknown_side_or_family_is_refused():
    grid, _ = R.tb1_grid("Basketball/NBL", NBL)
    with pytest.raises(R.ReferenceError_):
        R.price_rows(grid, [dict(label="X", family="winner", side="OVER", line="")])
    with pytest.raises(R.ReferenceError_):
        R.price_rows(grid, [dict(label="X", family="corners", side="OVER", line="9.5")])


def test_soccer_uses_the_average_form_and_a_poisson_grid():
    data = dict(lm=1.4, home=dict(team="H", pf=30, pa=15, n=15), away=dict(team="A", pf=20, pa=25, n=15))
    grid, info = R.tb1_grid("Soccer/Premier League", data)
    assert info["form"] == "average"
    w, d, l = grid.winner()
    assert w > l and d > 0.15 and w + d + l == pytest.approx(1.0)


def test_unsupported_leagues_have_no_tb1_grid():
    with pytest.raises(R.ReferenceError_, match="tier C"):
        R.tb1_grid("Soccer/Prva Liga RS", NBL)


def test_league_mean_prior_blend_touches_only_the_total():
    rows = [dict(role="HOME", team="H", pf=315, pa=300, n=3), dict(role="AWAY", team="A", pf=285, pa=307, n=3),
            dict(role="LEAGUE", team="ALL", pf=800, pa=800, n=8)]
    plain = R.tb1_inputs(rows, "NBA")
    blended = R.tb1_inputs(rows, "NBA", lm_prior=114.5)
    assert plain["lm"] == pytest.approx(100.0) and blended["lm"] == pytest.approx((8 * 100 + 200 * 114.5) / 208) and blended["lm_blended"]
    a, b = R.tb1_centre(R.TB1_MD["NBA"], plain, form="additive"), R.tb1_centre(R.TB1_MD["NBA"], blended, form="additive")
    assert a["margin"] == pytest.approx(b["margin"]) and abs(b["total"] - a["total"]) > 1.0        # the league mean cancels from every margin


# ------------------------------------------------------------------ filesystem: tiers, floors, the reference stage
PARAMS = ["row_type", "competition", "model_dir", "engine", "family", "usable", "dev_rows", "dev_seasons", "dev_first_date", "dev_last_date",
          "mean_total", "mean_home_margin", "home_win_rate", "raw_margin_sd", "raw_total_sd", "resid_margin_sd", "resid_total_sd", "z_margin_sd",
          "z_total_sd", "store_final_events", "store_extra_time_rate", "store_mean_total", "store_mean_home_margin", "store_margin_sd",
          "store_total_sd", "members", "flags", "evidence_class"]


def _row(**kw):
    base = {k: "" for k in PARAMS}
    base.update(kw)
    return base


@pytest.fixture
def root(tmp_path):
    _write(tmp_path / R.RELEASES, [dict(competition="Basketball/EXAMPLE-A", endpoint="FULL_GAME_INCL_OT", active_experimental_release="EX-1",
                                        release_path="x", release_sha256="x", source_code_sha256="x", qualification="X", prospective_events="0")])
    _write(tmp_path / R.STORE_EVENTS, [dict(event_uid=f"E{i}", competition="Basketball/EXAMPLE-B", endpoint="E", native_event_id=str(i),
                                            identity_basis="N", season="2025", event_at="2025-01-01T00:00:00+00:00", home="a", away="b",
                                            venue="", ingest_seq="1") for i in range(R.MIN_STORE_EVENTS)])
    _write(tmp_path / R.PARAMETERS, [
        _row(row_type="COMPETITION", competition="Basketball/EXAMPLE-B", usable="USABLE_DEVELOPMENT", family="BASKETBALL", mean_total="170",
             mean_home_margin="3", raw_margin_sd="13.5", raw_total_sd="17.5", resid_margin_sd="12.0", resid_total_sd="16.5",
             evidence_class="HISTORICAL_DEVELOPMENT_UNADMITTED", dev_last_date="2025-06-01"),
        _row(row_type="COMPETITION", competition="Basketball/EXAMPLE-BAD", usable="NOT_USABLE", family="BASKETBALL", resid_margin_sd="123", resid_total_sd="126"),
        _row(row_type="FAMILY_PRIOR", competition="FAMILY_PRIOR:BASKETBALL_FIBA40", usable="USABLE_DEVELOPMENT", family="BASKETBALL",
             mean_total="168", mean_home_margin="2.5", raw_margin_sd="14", raw_total_sd="18", resid_margin_sd="12.8", resid_total_sd="16.8",
             evidence_class="MEDIAN_OF_USABLE_MEMBERS")])
    return tmp_path


def test_tier_ladder(root):
    assert R.tier("Basketball/EXAMPLE-A", root)["tier"] == "A" and R.tier("Basketball/EXAMPLE-A", root)["reference"] == "RELEASE:EX-1"
    b = R.tier("Basketball/EXAMPLE-B", root)
    assert b["tier"] == "B" and "100 verified" in b["basis"] and b["reference"] == "BASELINE_ONLY"
    assert R.tier("Basketball/NBL", root)["tier"] == "B" and R.tier("Basketball/NBL", root)["reference"] == "TB2-MD"
    assert R.tier("Soccer/La Liga", root)["reference"] == "TB1-MD"
    c = R.tier("Soccer/Prva Liga RS", root)
    assert c["tier"] == "C" and c["reference"] == "BASELINE_ONLY"


def test_a_declared_choice_overrides_the_default(root):
    _write(root / R.CHOICE, [dict(competition="Basketball/EXAMPLE-A", reference_model="TB2-MD", basis="b", evidence="e", declared_for="s", declared_at="d")])
    assert R.tier("Basketball/EXAMPLE-A", root)["reference"] == "TB2-MD"


def test_width_floor_ladder(root):
    own = R.width_floor("Basketball/EXAMPLE-B", "MARGIN", root)
    assert own == dict(floor=12.0, basis="COMPETITION_ROW", competition="Basketball/EXAMPLE-B", row_evidence="HISTORICAL_DEVELOPMENT_UNADMITTED")
    fallback = R.width_floor("Basketball/EXAMPLE-BAD", "TOTAL", root)                   # an unusable row never sets a floor
    assert fallback["basis"] == "FAMILY_PRIOR_PLUS_10_PERCENT" and fallback["floor"] == pytest.approx(16.8 * 1.1, abs=0.01)
    assert R.width_floor("Cricket T20/IPL", "TOTAL", root)["floor"] is None
    with pytest.raises(KeyError):
        R.width_floor("Basketball/EXAMPLE-B", "PERIOD", root)


def test_baseline_grid_uses_the_row_or_the_prior_and_flags_a_stale_profile(root):
    grid, info = R.baseline_grid("Basketball/EXAMPLE-B", root)
    assert info["status"] == "COMPETITION_ROW" and "STALE_PROFILE" in info["flags"]
    assert grid.winner()[0] > 0.5                                                          # a positive home edge
    prior, pinfo = R.baseline_grid("Basketball/EXAMPLE-BAD", root)
    assert pinfo["status"] == "FAMILY_PRIOR" and prior.winner()[0] > 0.5
    with pytest.raises(R.ReferenceError_):
        R.baseline_grid("Baseball/EXAMPLE", root)


def _inputs(root):
    work = root / "work"
    _write(work / "GAME.csv", [dict(local_key="LOCAL-EXAMPLE-G0001", competition="Basketball/NBL", home="H", away="A",
                                    scheduled_start="2026-11-01T09:00:00+00:00")])
    _write(work / "LINES.csv", [dict(label="HOME_ML", family="winner", side="HOME", line=""), dict(label="OVER_180.5", family="total", side="OVER", line="180.5")])
    _write(work / "STANDINGS.csv", [dict(role="HOME", team="H", pf=1195, pa=1102, n=13), dict(role="AWAY", team="A", pf=1150, pa=1231, n=13),
                                    dict(role="LEAGUE", team="ALL", pf=18250, pa=18250, n=200)])
    return work


def test_reference_stage_requires_the_outcome_confirmation(root):
    work = _inputs(root)
    with pytest.raises(R.ReferenceError_, match="confirm-no-outcome-seen"):
        R.run(work / "GAME.csv", work / "LINES.csv", work / "STANDINGS.csv", root=root)


def test_reference_stage_runs_tb2_for_a_points_league_and_writes_a_receipt(root):
    work = _inputs(root)
    result = R.run(work / "GAME.csv", work / "LINES.csv", work / "STANDINGS.csv", confirmed=True, root=root)
    assert result["status"] == "EXECUTED" and result["reference_id"] == "TB2-MD:NBL" and len(result["rows"]) == 2
    assert result["baseline_id"].startswith("BASELINE_LEAGUE_V1:FAMILY_PRIOR")          # no NBL row in this synthetic parameter table
    text = R.markdown(result)
    assert "Reference (REFMODEL-v1, frozen before this card)" in text and "TB2-MD:NBL" in text and "departure goes in the adjustment ledger" in text
    receipt = R.write_receipt(result, root)
    assert receipt.exists() and (receipt.parent / receipt.name.replace("_REFERENCE.csv", "_REFERENCE_ROWS.csv")).exists()
    rows = list(csv.DictReader(io.StringIO((receipt.parent / receipt.name.replace("_REFERENCE.csv", "_REFERENCE_ROWS.csv")).read_text())))
    assert rows[0]["reference_id"] == "TB2-MD:NBL" and rows[0]["baseline_p"]


def test_reference_stage_flags_the_nfl_key_numbers(root):
    work = _inputs(root)
    _write(work / "GAME.csv", [dict(local_key="LOCAL-EXAMPLE-G0001", competition="American Football/NFL", home="H", away="A",
                                    scheduled_start="2026-11-01T09:00:00+00:00")])
    result = R.run(work / "GAME.csv", work / "LINES.csv", work / "STANDINGS.csv", confirmed=True, root=root)
    assert result["status"] == "EXECUTED" and "KEY_NUMBERS_NOT_MODELLED" in result["flags"]
    nbl = R.run(_inputs(root) / "GAME.csv", work / "LINES.csv", work / "STANDINGS.csv", confirmed=True, root=root)
    assert "KEY_NUMBERS_NOT_MODELLED" not in nbl["flags"]


def test_reference_stage_without_standings_falls_back_to_the_baseline(root):
    work = _inputs(root)
    _write(work / "GAME.csv", [dict(local_key="LOCAL-EXAMPLE-G0001", competition="Basketball/EXAMPLE-B", home="H", away="A",
                                    scheduled_start="2026-11-01T09:00:00+00:00")])
    result = R.run(work / "GAME.csv", work / "LINES.csv", None, confirmed=True, root=root)
    assert result["status"] == "BASELINE_ONLY" and result["reference_id"].startswith("BASELINE_LEAGUE_V1")


def test_reference_stage_for_a_release_reference_points_to_the_pregame_command(root):
    work = _inputs(root)
    _write(work / "GAME.csv", [dict(local_key="LOCAL-EXAMPLE-G0001", competition="Basketball/EXAMPLE-A", home="H", away="A",
                                    scheduled_start="2026-11-01T09:00:00+00:00")])
    with pytest.raises(R.ReferenceError_, match="pregame reference"):
        R.run(work / "GAME.csv", work / "LINES.csv", work / "STANDINGS.csv", confirmed=True, root=root)


def test_standings_csv_parses_the_feed_and_suggests_names(monkeypatch):
    feed = {"children": [{"standings": {"entries": [
        {"team": {"displayName": "Alpha"}, "stats": [{"name": "pointsFor", "value": 200}, {"name": "pointsAgainst", "value": 190},
                                                      {"name": "wins", "value": 2}, {"name": "losses", "value": 0}]},
        {"team": {"displayName": "Beta"}, "stats": [{"name": "pointsFor", "value": 180}, {"name": "pointsAgainst", "value": 195},
                                                     {"name": "gamesPlayed", "value": 2}]}]}}]}
    import json

    class Body:
        def read(self):
            return json.dumps(feed).encode()

    monkeypatch.setattr("urllib.request.urlopen", lambda *a, **k: Body())
    data, receipt = R.standings_csv("Basketball/NBA", "Alpha", "Beta")
    rows = list(csv.DictReader(io.StringIO(data.decode())))
    assert [r["role"] for r in rows] == ["HOME", "AWAY", "LEAGUE"] and rows[0]["n"] == "2.0" and rows[2]["pf"] == "380.0" and rows[2]["n"] == "4.0"
    assert receipt["source_url"].endswith("basketball/nba/standings") and len(receipt["raw_sha256"]) == 64
    with pytest.raises(R.ReferenceError_, match="closest: Alpha"):
        R.standings_csv("Basketball/NBA", "Alfa", "Beta")
    with pytest.raises(R.ReferenceError_, match="no standings feed"):
        R.espn_standings("Cricket T20/IPL")
