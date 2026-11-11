"""LEARNLOG-v1: every game gets a structured, point-in-time learning log (owner instruction 2026-11-09).

Synthetic EXAMPLE competitions and LOCAL-EXAMPLE keys only; nothing under the live research/ folder is touched."""
import csv
import io
import shutil
from pathlib import Path

import pytest

from ml import learning_log as LL
from ml.tests.test_picks_ledger import META, render

ROOT = Path(LL.ROOT)
KEY = "LOCAL-EXAMPLE-G0001"


def _rows(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def _put(path, fields, rows):
    buf = io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=list(fields), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    path.write_bytes(buf.getvalue().encode("utf-8"))


@pytest.fixture
def repo(tmp_path):
    (tmp_path / LL.LOG).mkdir(parents=True)
    shutil.copy(ROOT / LL.DICTIONARY, tmp_path / LL.DICTIONARY)
    mini = tmp_path / "MINI.md"
    mini.write_text(f"# mini\n<!-- BEGIN CARD {KEY} -->\n{render()}\n<!-- END CARD {KEY} -->\n", encoding="utf-8")
    game = tmp_path / "GAME.csv"
    _put(game, ("local_key", "competition", "home", "away", "scheduled_start", "native_event_id", "season", "venue"),
         [dict(local_key=KEY, competition=META["competition"], home="Home FC", away="Away FC", scheduled_start=META["scheduled_start"],
               native_event_id="EXAMPLE:1", season="2026", venue="Example Arena")])
    return dict(root=tmp_path, mini=mini, game=game)


def _init(repo, sport="Basketball"):
    return LL.init(repo["mini"], KEY, repo["game"], sport=sport, root=repo["root"])


def _fill(folder, **override):
    rows = _rows(folder / "FEATURES.csv")
    for r in rows:
        r.update(value="101.5", status="OBSERVED", missing_reason="", source_url="https://example.org/stats",
                 published_at="2026-10-21T00:00:00+00:00", retrieved_at="2026-10-22T08:00:00+00:00", known_at="2026-10-21T00:00:00+00:00")
        r.update(override)
    _put(folder / "FEATURES.csv", LL.FEATURES, rows)
    _put(folder / "AVAILABILITY.csv", LL.AVAILABILITY, [
        dict(side=side, team=team, player=LL.NONE_PUBLISHED, role="UNKNOWN", status="UNKNOWN", confirmation="REPORTED",
             source_url="https://example.org/team-news", published_at="", retrieved_at="2026-10-22T08:00:00+00:00",
             known_at="2026-10-22T08:00:00+00:00") for side, team in (("HOME", "Home FC"), ("AWAY", "Away FC"))])


def test_every_card_captures_both_sides_availability_or_says_none_was_published(repo):
    """LINEUP-CAPTURE-v1: an empty availability file fails; NONE_PUBLISHED rows name the page checked."""
    folder = _init(repo)
    _fill(folder)
    assert LL.check(KEY, root=repo["root"]) == []
    rows = _rows(folder / "AVAILABILITY.csv")
    _put(folder / "AVAILABILITY.csv", LL.AVAILABILITY, rows[:1])
    assert any("no row for AWAY" in p for p in LL.check(KEY, root=repo["root"]))
    rows[1].update(role="STARTER")
    _put(folder / "AVAILABILITY.csv", LL.AVAILABILITY, rows)
    assert any("NONE_PUBLISHED row has role and status UNKNOWN" in p for p in LL.check(KEY, root=repo["root"]))


def test_init_copies_identity_and_contracts_and_lists_the_required_features(repo):
    folder = _init(repo)
    card = _rows(folder / "CARD.csv")[0]
    assert card["local_key"] == KEY and card["competition"] == META["competition"] and card["home"] == "Home FC" and card["canonical_id"] == ""
    contracts = _rows(folder / "CONTRACTS.csv")
    assert [c["label"] for c in contracts] == ["HOME_ML", "OVER_170.5", "UNDER_170.5"] and "model_p" not in contracts[0]
    features = _rows(folder / "FEATURES.csv")
    required = LL.required_features("Basketball", repo["root"])
    assert len(features) == 2 * len(required) and {f["status"] for f in features} == {"MISSING"}
    with pytest.raises(LL.LearningLogError, match="already exists"):
        _init(repo)


def test_a_fresh_log_fails_until_every_feature_is_researched_or_explained(repo):
    folder = _init(repo)
    assert any(LL.PLACEHOLDER in p for p in LL.check(KEY, root=repo["root"]))
    _fill(folder)
    assert LL.check(KEY, root=repo["root"]) == []
    rows = _rows(folder / "FEATURES.csv")
    rows[0].update(value="", status="MISSING", missing_reason="no permitted source publishes it (SRC-ALT-v2)", source_url="",
                   published_at="", retrieved_at="", known_at="")
    _put(folder / "FEATURES.csv", LL.FEATURES, rows)
    assert LL.check(KEY, root=repo["root"]) == []


def test_post_start_facts_market_terms_fills_and_absent_features_are_refused(repo):
    folder = _init(repo)
    _fill(folder, known_at="2026-10-22T11:00:00+00:00")
    assert any("not before the scheduled start" in p for p in LL.check(KEY, root=repo["root"]))
    _fill(folder, window="from odds")
    assert any("market term" in p for p in LL.check(KEY, root=repo["root"]))
    rows = _rows(folder / "FEATURES.csv")
    rows[0].update(status="MISSING", value="110.0", missing_reason="league average")
    _put(folder / "FEATURES.csv", LL.FEATURES, rows[:-1])
    problems = LL.check(KEY, root=repo["root"])
    assert any("never a league-average fill" in p for p in problems) and any("is absent" in p for p in problems)


def test_availability_and_prior_games_use_the_vocabulary_and_pregame_times(repo):
    folder = _init(repo)
    _fill(folder)
    _put(folder / "AVAILABILITY.csv", LL.AVAILABILITY, [dict(side="HOME", team="Home FC", player="A. Player", role="STARTER",
                                                             status="HEALTHY", confirmation="OFFICIAL_CONFIRMED", source_url="https://example.org/inj",
                                                             published_at="", retrieved_at="", known_at="2026-10-21T00:00:00+00:00")])
    _put(folder / "PRIOR_GAMES.csv", LL.PRIOR_GAMES, [dict(side="AWAY", event_at="2026-10-23T00:00:00+00:00", competition=META["competition"],
                                                           opponent="X", venue_role="HOME", score_for="99", score_against="90", decision="WIN",
                                                           endpoint="FULL_GAME_INCL_OT", source_url="https://example.org/box", retrieved_at="",
                                                           known_at="2026-10-21T00:00:00+00:00")])
    problems = LL.check(KEY, root=repo["root"])
    assert any("AVAILABILITY.csv line 2" in p and "vocabulary" in p for p in problems)
    assert any("PRIOR_GAMES.csv line 2: event_at" in p for p in problems)


def test_settlement_needs_an_outcome_and_a_grade_for_every_contract_then_build_joins_them(repo):
    folder = _init(repo)
    _fill(folder)
    assert any("OUTCOME.csv: missing" in p for p in LL.check(KEY, "settled", repo["root"]))
    _put(folder / "OUTCOME.csv", LL.OUTCOME, [dict(status="FINAL", home_score="101", away_score="95", home_regulation="101",
                                                   away_regulation="95", decision="HOME", final_at="2026-10-22T12:30:00+00:00",
                                                   source_url="https://example.org/box", second_source_url="https://example.net/box",
                                                   retrieved_at="2026-10-22T13:00:00+00:00", evidence_grade="B")])
    _put(folder / "GRADES.csv", LL.GRADES, [dict(label="HOME_ML", grade="WIN", basis="101-95"), dict(label="OVER_170.5", grade="WIN", basis="196")])
    assert any("UNDER_170.5 has no grade" in p for p in LL.check(KEY, "settled", repo["root"]))
    _put(folder / "GRADES.csv", LL.GRADES, [dict(label="HOME_ML", grade="WIN", basis="101-95"), dict(label="OVER_170.5", grade="WIN", basis="196"),
                                            dict(label="UNDER_170.5", grade="LOSS", basis="196")])
    assert LL.check(KEY, "settled", repo["root"]) == []
    LL.link(KEY, "P-999", repo["root"])
    with pytest.raises(LL.LearningLogError, match="already linked"):
        LL.link(KEY, "P-998", repo["root"])
    summary = LL.build(repo["root"] / "BUILD", repo["root"])
    assert summary == dict(games=1, admitted=1, settled=1, contracts=3)
    data = _rows(repo["root"] / "BUILD" / "DATASET_CONTRACTS.csv")
    home_ml = next(r for r in data if r["label"] == "HOME_ML")
    assert home_ml["grade"] == "WIN" and home_ml["canonical_id"] == "P-999" and home_ml["home__rest_days"] == "101.5"
    assert home_ml["home__rest_days__missing"] == "0" and "model_p" not in home_ml


def test_build_refuses_an_incomplete_log_and_says_why(repo):
    _init(repo)
    summary = LL.build(repo["root"] / "BUILD", repo["root"])
    assert summary["admitted"] == 0
    receipt = _rows(repo["root"] / "BUILD" / "BUILD_RECEIPT.csv")[0]
    assert receipt["admitted"] == "NO" and LL.PLACEHOLDER in receipt["problems"]


def test_every_sport_in_the_dictionary_has_required_features_and_no_market_field():
    rows = LL.dictionary(ROOT)
    sports = {r["sport"] for r in rows}
    assert {"TEAM_SPORT", "Basketball", "Ice Hockey", "Baseball", "Soccer", "Cricket", "Tennis", "Australian Rules",
            "Rugby League", "Rugby Union", "American Football"} <= sports
    for sport in sports:
        assert LL.required_features(sport, ROOT), sport
    assert not any(LL.MARKET.search(r["feature"] + " " + r["description"]) for r in rows)
    assert LL.required_features("Handball", ROOT) == LL.required_features("TEAM_SPORT", ROOT)
