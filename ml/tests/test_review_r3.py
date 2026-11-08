"""Adversarial reproductions from the 9 November review; synthetic data and mocked HTTP only."""
import csv
import io

import pandas as pd
import pytest

from ml import reference as R, ledger as L, source_access as A, source_audit as S
from ml.evaluation import prospective as P
from ml.tests import test_reference as TR, test_picks_ledger as TP, test_learning_governance as TG


@pytest.fixture
def root(tmp_path):
    return TP.root.__wrapped__(tmp_path)


@pytest.mark.parametrize("change,reason", [
    ({"team": "ANOTHER TEAM"}, "STANDINGS_TEAM"),
    ({"competition": "Basketball/ANOTHER"}, "STANDINGS_COMPETITION"),
    ({"known_at": "2026-12-01T00:00:00Z"}, "STANDINGS_HORIZON"),
    ({"snapshot_at": "2026-12-01T00:00:00Z"}, "STANDINGS_HORIZON"),
    ({"known_at": ""}, "STANDINGS_EVIDENCE"),
    ({"pf": "nan"}, "STANDINGS_NUMBER"),
])
def test_reference_refuses_wrong_or_unavailable_standings(root, change, reason):
    work = TR._inputs(root)
    rows = R._rows(work / "STANDINGS.csv")
    rows[0].update(change)
    TR._write(work / "STANDINGS.csv", rows)
    with pytest.raises(R.ReferenceError_, match=reason):
        R.run(work / "GAME.csv", work / "LINES.csv", work / "STANDINGS.csv", confirmed=True, root=root)


def test_reference_refuses_duplicate_standings_roles(root):
    work = TR._inputs(root)
    rows = R._rows(work / "STANDINGS.csv")
    rows.append(rows[0])
    TR._write(work / "STANDINGS.csv", rows)
    with pytest.raises(R.ReferenceError_, match="STANDINGS_ROLES"):
        R.run(work / "GAME.csv", work / "LINES.csv", work / "STANDINGS.csv", confirmed=True, root=root)


def test_impossible_total_probabilities_cannot_enter_ledger(root):
    rows = TP.good_rows()
    rows.append(dict(rows[1], label="OVER_190.5", line="190.5", reference_p="0.6000", final_p="0.6000",
                     w="0.6000", l="0.4000", z=str(20.5 / 17)))
    with pytest.raises(L.LedgerError, match="monotonicity"):
        L.add(TP.mini(root, TP.render(rows=rows)), TP.KEY, root=root)


def test_team_total_nesting_is_checked_within_the_named_team(root):
    from ml import picks
    rows = TP.good_rows()
    first = dict(rows[1], label="HOME_OVER", family="TEAM_TOTAL", quantity="TEAM_TOTAL", line="100.5")
    second = dict(first, label="AWAY_OVER", line="110.5", reference_p="0.60", final_p="0.60", w="0.60", l="0.40")
    rows += [first, second]
    meta = dict(TP.META, contract_scopes="HOME_OVER=HOME_FULL_MATCH|AWAY_OVER=AWAY_FULL_MATCH")
    assert picks.lint(meta, rows, root) == []
    meta["contract_scopes"] = "HOME_OVER=HOME_FULL_MATCH|AWAY_OVER=HOME_FULL_MATCH"
    assert any("monotonicity" in p for p in picks.lint(meta, rows, root))
    meta.pop("contract_scopes")
    assert any("explicit team/period" in p for p in picks.lint(meta, rows, root))


@pytest.mark.parametrize("change,reason", [
    ({"competition": "Soccer/OTHER"}, "effect competition"),
    ({"target": "game total"}, "effect target"),
    ({"unit": "goals"}, "effect unit"),
])
def test_effect_scope_and_units_are_enforced_at_ledger_admission(root, change, reason):
    effects = R._rows(root / L.EFFECTS)
    effects[0].update(change)
    TR._write(root / L.EFFECTS, effects)
    with pytest.raises(L.LedgerError, match=reason):
        L.add(TP.mini(root, TP.render()), TP.KEY, root=root)


def test_eight_weeks_and_32_games_cannot_promote():
    ledger, outcomes = [], []
    for week in range(8):
        start = TG.T0 + pd.Timedelta(days=week * 7 + 1)
        for i in range(4):
            event = f"EX-{week}-{i}"
            q, y = (.25 if i < 2 else .75), i >= 2
            if (week % 2 == 0 and i == 0) or (week % 2 == 1 and i == 2):
                y = not y
            ledger += [TG._rows("CHAMP", "v3", "CHAMPION", event, start, .5, 1),
                       TG._rows("CAND", "c1", "CANDIDATE", event, start, q, 1)]
            outcomes.append(dict(event_id=event, contract_key="WIN-H", result="WIN" if y else "LOSS",
                                 final_at=(start + pd.Timedelta(hours=3)).isoformat(),
                                 available_at=(start + pd.Timedelta(hours=4)).isoformat(), evidence_sha256="e" * 64))
    result = P.evaluate(ledger, pd.DataFrame(outcomes), "CHAMP:v3", "CAND:c1", delta=.01)
    assert result["disposition"] == "INSUFFICIENT_EVIDENCE" and "minimum 50" in result["reason"]


@pytest.mark.parametrize("status", ["BLOCKED_FOR_AI", "RULES_UNKNOWN", "BLOCKED_FOR_ALL"])
def test_fetch_refuses_before_network_for_every_nonpermitted_source(monkeypatch, status):
    monkeypatch.setattr(S, "audit", lambda urls: [{"status": status}])
    monkeypatch.setattr(A.urllib.request, "build_opener", lambda *args: pytest.fail("network must not be opened"))
    with pytest.raises(A.SourceAccessError, match="SOURCE_ACCESS_REFUSED"):
        A.fetch_bytes("https://example.org/result")


def test_redirect_checks_destination_before_following(monkeypatch):
    monkeypatch.setattr(S, "audit", lambda urls: [{"status": "BLOCKED_FOR_AI"}])
    with pytest.raises(A.SourceAccessError):
        A._CheckedRedirect().redirect_request(None, None, 302, "", {}, "https://blocked.example/result")


def test_both_agent_families_are_checked():
    assert {"GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User"} <= set(S.AGENTS)


def test_permitted_standings_refuses_partial_and_duplicate_leagues():
    from ml import permitted_standings as F
    def row(team):
        return f'<tr><td data-index="1">{team}</td><td data-index="2">2-1</td><td data-index="5">100.1</td><td data-index="6">99.9</td></tr>'
    raw = ''.join(row(t) for t in F.TEAMS).encode()
    teams = F.parse(raw)
    assert len(teams) == 30 and teams[0]["n"] == 3 and teams[0]["pf"] == pytest.approx(300.3)
    with pytest.raises(ValueError, match="30 unique"):
        F.parse(row("76ers").encode())
    with pytest.raises(ValueError, match="30 unique"):
        F.parse((row("76ers") * 30).encode())


def test_blocked_primary_standings_uses_a_labelled_permitted_alternate(monkeypatch):
    from ml import permitted_standings as F
    def refused(*args, **kwargs):
        raise A.SourceAccessError("SOURCE_ACCESS_REFUSED")
    monkeypatch.setattr(R, "espn_standings", refused)
    monkeypatch.setattr(F, "fetch", lambda: (b"source capture", [dict(team="H", n=2, pf=200.2, pa=199.8), dict(team="A", n=2, pf=199.8, pa=200.2)]))
    data, receipt = R.standings_csv("Basketball/NBA", "H", "A")
    rows = list(csv.DictReader(io.StringIO(data.decode())))
    assert receipt["source_url"] == F.URL and "PROXY" in rows[0]["precision_basis"]
    assert rows[0]["publication_basis"] == "OBSERVED_SNAPSHOT_UPPER_BOUND"


def test_reviewed_fixture_path_checks_scope_capture_and_time(tmp_path, monkeypatch):
    from ml import league_day as D, primary as p
    from ml.tests.test_reference import _write
    capture = tmp_path / "source.txt"; capture.write_text("fixture sporting facts")
    row = dict(competition="Basketball/EXAMPLE", native_event_id="OWNER:1", scheduled_start="2027-01-02T00:00:00Z",
               known_at="2027-01-01T00:00:00Z", state="pre", season_type="2", season="2026", home="H", away="A", venue="V",
               source_url="https://example.org/fixture", capture_path=str(capture), capture_sha256=p.digest(capture.read_bytes()))
    path = tmp_path / "fixtures.csv"; _write(path, [row])
    monkeypatch.setattr(A, "ensure_allowed", lambda url: {"status": "ALLOWED"})
    assert D.reviewed_fixtures(path, "Basketball/EXAMPLE", now="2027-01-01T01:00:00Z")[0]["open"]
    with pytest.raises(D.LeagueDayError, match="FIXTURE_SCOPE"):
        D.reviewed_fixtures(path, "Basketball/OTHER", now="2027-01-01T01:00:00Z")
    with pytest.raises(D.LeagueDayError, match="FIXTURE_TIME"):
        D.reviewed_fixtures(path, "Basketball/EXAMPLE", now="2026-12-31T00:00:00Z")
