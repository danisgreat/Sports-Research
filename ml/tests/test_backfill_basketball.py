"""Basketball two-lineage reconciliation (REV-07). Synthetic payloads only; no network."""
from datetime import date

import pytest

from ml import backfill_basketball as B, primary as p


def event(eid, home, away, hs, as_, hp, ap, start="2025-01-10T00:30Z", typ=2, completed=True, neutral=False):
    return {"id": eid, "date": start, "season": {"year": 2025, "type": typ}, "status": {"type": {"completed": completed}},
            "competitions": [{"neutralSite": neutral, "venue": {"fullName": "Arena"}, "competitors": [
                {"homeAway": "home", "score": str(hs), "team": {"displayName": home}, "linescores": [{"value": v} for v in hp]},
                {"homeAway": "away", "score": str(as_), "team": {"displayName": away}, "linescores": [{"value": v} for v in ap]}]}]}


def test_espn_rows_regulation_overtime_and_filters():
    data = {"events": [
        event("1", "Boston Celtics", "LA Clippers", 100, 90, [25, 25, 25, 25], [20, 20, 25, 25]),
        event("2", "Miami Heat", "Orlando Magic", 110, 108, [25, 25, 25, 25, 10], [25, 25, 25, 25, 8]),
        event("3", "Boston Celtics", "Miami Heat", 100, 90, [25, 25, 25, 25], [20, 20, 25, 25], typ=1),          # preseason
        event("4", "Boston Celtics", "Miami Heat", 100, 90, [25, 25, 25, 25], [20, 20, 25, 25], completed=False),
        event("5", "Boston Celtics", "Miami Heat", 100, 90, [25, 25, 25], [20, 20, 25]),                          # missing a period
        event("6", "Boston Celtics", "Miami Heat", 101, 90, [25, 25, 25, 25], [20, 20, 25, 25])]}                   # periods do not sum
    rows = B.espn_rows(data, "2025-01-09")
    assert [r["provider_id"] for r in rows] == ["1", "2"]
    first, second = rows
    assert first["away"] == "Los Angeles Clippers" and first["decision"] == "Regulation" and first["season"] == "2024"
    assert (second["reg_hs"], second["reg_as"], second["hs"], second["as_"], second["decision"]) == (100, 100, 110, 108, "Overtime")


BR_PAGE = """<table><tr><th data-stat="date_game">Date</th></tr>
<tr><th scope="row" class="left " data-stat="date_game" csk="202501090BOS" ><a>Thu, Jan 9, 2025</a></th><td data-stat="game_start_time">7:30p</td>
<td data-stat="visitor_team_name"><a>Los Angeles Clippers</a></td><td data-stat="visitor_pts">90</td><td data-stat="home_team_name"><a>Boston Celtics</a></td>
<td data-stat="home_pts">100</td><td data-stat="overtimes"></td></tr>
<tr><th scope="row" class="left " data-stat="date_game" csk="202501090MIA" ><a>Thu, Jan 9, 2025</a></th><td data-stat="visitor_team_name"><a>Orlando Magic</a></td>
<td data-stat="visitor_pts">108</td><td data-stat="home_team_name"><a>Miami Heat</a></td><td data-stat="home_pts">110</td><td data-stat="overtimes">OT</td></tr>
<tr><th scope="row" class="left " data-stat="date_game" csk="202501100ATL" ><a>Fri, Jan 10, 2025</a></th><td data-stat="visitor_team_name"><a>X</a></td>
<td data-stat="visitor_pts"></td><td data-stat="home_team_name"><a>Atlanta Hawks</a></td><td data-stat="home_pts"></td><td data-stat="overtimes"></td></tr></table>"""


def test_basketball_reference_rows_skip_headers_and_unplayed_games():
    rows = B.br_rows(BR_PAGE, 2025)
    assert [(r["home"], r["hs"], r["overtime"], r["csk"]) for r in rows] == [("Boston Celtics", 100, False, "202501090BOS"), ("Miami Heat", 110, True, "202501090MIA")]


def espn():
    return B.espn_rows({"events": [event("1", "Boston Celtics", "LA Clippers", 100, 90, [25, 25, 25, 25], [20, 20, 25, 25]),
                                   event("2", "Miami Heat", "Orlando Magic", 110, 108, [25, 25, 25, 25, 10], [25, 25, 25, 25, 8])]}, "2025-01-09")


def test_reconcile_admits_only_unique_agreement():
    pairs, decisions = B.reconcile(espn(), B.br_rows(BR_PAGE, 2025))
    assert len(pairs) == 2 and {d["status"] for d in decisions} == {"VERIFIED_FOR_FUTURE_TRAINING"}


def test_reconcile_records_every_disagreement():
    other = B.br_rows(BR_PAGE, 2025)
    other[0]["hs"] = 101                                                      # score conflict
    other[1]["overtime"] = False                                              # overtime conflict
    pairs, decisions = B.reconcile(espn(), other)
    assert not pairs
    assert [d["reason"] for d in decisions] == ["SCORE_CONFLICT_OR_AMBIGUOUS", "OVERTIME_FLAG_CONFLICT"]
    missing_pairs, missing = B.reconcile(espn(), [])
    assert not missing_pairs and {d["reason"] for d in missing} == {"NO_INDEPENDENT_MATCH"}


def test_reconcile_matches_across_the_utc_date_line():
    other = B.br_rows(BR_PAGE, 2025)           # the schedule files the 00:30Z game under the previous US evening
    pairs, _ = B.reconcile(espn(), other)
    assert pairs[0][0]["event_at"].startswith("2025-01-10") and pairs[0][1]["date"] == "2025-01-09"


def test_one_independent_game_cannot_serve_two_provider_games():
    first = espn()[0]
    twin = dict(first, event_id="ESPN:dup", provider_id="dup")
    with pytest.raises(p.AdmissionError, match="more than one"):
        B.reconcile([first, twin], B.br_rows(BR_PAGE, 2025))


def test_page_naming_and_display_aliases():
    assert B.br_page(date(2024, 10, 22)) == (2025, "october") and B.br_page(date(2025, 4, 3)) == (2025, "april")
    assert B.display("LA Clippers") == "Los Angeles Clippers" and B.display(" Boston Celtics ") == "Boston Celtics"
    assert B.canonical("LA  Clippers") == "los angeles clippers"
