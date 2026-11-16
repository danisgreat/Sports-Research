"""ONE-CHAT-v1: the chat's own card is parsed, checked, flagged and scored without interpretation."""
import os

import pytest

from ml import one_chat as O

FACTS = O.required_facts("Basketball")
START = "2026-11-20T08:00:00+00:00"
R = "https://example.org/result/1"
DEFAULT = [f"L1,HANDICAP,HOME,-3.5,0.47,,2.1,NONE,{R}", f"L1,HANDICAP,AWAY,3.5,0.53,,-2.1,NONE,{R}",
           f"L2,TOTAL,OVER,158.5,0.62,,160.2,NONE,{R}", f"L2,TOTAL,UNDER,158.5,0.38,,160.2,NONE,{R}"]


def card(key="CHAT1-G0001", home="Alpha", away="Beta", picks=None, facts=None, **header):
    meta = dict(format="ONECHAT_V1", card_key=key, sport="Basketball", competition="Example League", home=home, away=away,
                scheduled_start=START, request_at="2026-11-20T05:00:00+00:00", research_start_at="2026-11-20T05:05:00+00:00",
                research_end_at="2026-11-20T06:30:00+00:00", not_started_source="https://example.org/fixture/1",
                not_started_observed_at="2026-11-20T06:25:00+00:00", outcome_exposure="NONE")
    meta.update(header)
    picks = DEFAULT if picks is None else picks
    facts = facts if facts is not None else [f"{s},{f},10,https://example.org/team/{s},2026-11-20T05:30:00+00:00" for s in ("HOME", "AWAY") for f in FACTS]
    body = "\n".join([f"{k}: {v}" for k, v in meta.items()] + ["", "PICKS", ",".join(O.PICK_COLUMNS), *picks, "", "FACTS", ",".join(O.FACT_COLUMNS), *facts])
    return f"# Card\n\nResearch text.\n\n<!-- BEGIN ONECHAT_V1 {key} -->\n{body}\n<!-- END ONECHAT_V1 {key} -->\n"


def drop(tmp_path, cards, name="drop"):
    d = tmp_path / name
    d.mkdir()
    for i, text in enumerate(cards):
        f = d / f"card{i:03d}.md"
        f.write_text(text, encoding="utf-8")
        os.utime(f, (1795075200 + i, 1795075200 + i))      # 2026-11-20T04:00Z onward: saved before the start
    return d


def test_a_complete_card_is_admitted_ranked_and_flagged_without_changing_a_number(tmp_path):
    d = drop(tmp_path, [card(), "# notes only\n"])
    s = O.intake(d, tmp_path / "in")
    assert (s["ADMITTED"], s["NO_BLOCK"], s["supplied_lines"], s["priced_lines"]) == (1, 1, 2, 2)
    rows = {(r["label"], r["side"]): r for r in O.read_csv(tmp_path / "in/PICKS.csv")}
    assert rows[("L2", "OVER")]["rank"] == "1" and rows[("L1", "AWAY")]["rank"] == "2" and rows[("L1", "HOME")]["rank"] == ""
    assert rows[("L1", "AWAY")]["flags"] == "NO_DIRECTION;PLUS_HANDICAP" and rows[("L2", "OVER")]["flags"] == ""
    assert [r["p"] for r in rows.values()] == ["0.47", "0.53", "0.62", "0.38"]
    facts = O.read_csv(tmp_path / "in/FACTS.csv")
    assert len(facts) == 2 * len(FACTS) and {r["status"] for r in facts} == {"OBSERVED"}
    with pytest.raises(O.OneChatError, match="already exists"):
        O.intake(d, tmp_path / "in")


@pytest.mark.parametrize("change,needle", [
    (dict(picks=[f"L1,TOTAL,OVER,158.5,0.62,,160.2,NONE,{R}"]), "both sides"),
    (dict(picks=[f"L1,TOTAL,OVER,158.5,0.62,,,NONE,{R}", f"L1,TOTAL,UNDER,158.5,0.48,,,NONE,{R}"]), "sum to"),
    (dict(picks=[f"L1,TOTAL,OVER,158.5,0.62,,,NONE,{R}", f"L1,TOTAL,UNDER,157.5,0.38,,,NONE,{R}"]), "same line"),
    (dict(picks=[f"L1,HANDICAP,HOME,-3.5,0.5,,,NONE,{R}", f"L1,HANDICAP,AWAY,4.5,0.5,,,NONE,{R}"]), "equal and opposite"),
    (dict(picks=[f"L1,TOTAL,OVER,158.5,0.62,,,GUESS,{R}", f"L1,TOTAL,UNDER,158.5,0.38,,,NONE,{R}"]), "availability_basis"),
    (dict(picks=["L1,TOTAL,OVER,158.5,0.62,,,NONE,", "L1,TOTAL,UNDER,158.5,0.38,,,NONE,NONE_FOUND"]), "result_source"),
    (dict(picks=[f"L1,TOTAL,OVER,158.5,0.62,LEAN,,NONE,{R}", f"L1,TOTAL,UNDER,158.5,0.38,,,NONE,{R}"]), "lean applies only"),
    (dict(picks=[f"L1,TOTAL,OVER,158.5,0.62,,NONE,{R}", f"L1,TOTAL,UNDER,158.5,0.38,,NONE,{R}"]), "wrong number of columns"),
    (dict(facts=[]), "required for Basketball"),
    (dict(facts=[f"{s},{f},10,," for s in ("HOME", "AWAY") for f in FACTS]), "needs its source page"),
    (dict(research_start_at="2026-11-20T04:00:00+00:00"), "time order"),
    (dict(scheduled_start="2026-11-20 08:00"), "offset-aware"),
    (dict(outcome_exposure="NONE; the odds moved"), "sporting fields only"),
])
def test_incomplete_or_incoherent_cards_are_refused_with_the_reason(tmp_path, change, needle):
    O.intake(drop(tmp_path, [card(**change)]), tmp_path / "in")
    c = O.read_csv(tmp_path / "in/CARDS.csv")[0]
    assert c["status"] == "REFUSED" and needle in c["problems"]
    assert O.read_csv(tmp_path / "in/PICKS.csv") == []


def test_unpriced_leans_missing_facts_whole_lines_and_audit_flags_are_legitimate(tmp_path):
    picks = ["L1,TOTAL,OVER,158.5,UNPRICED,LEAN,,UNMEASURED,NONE_FOUND", "L1,TOTAL,UNDER,158.5,UNPRICED,,,UNMEASURED,NONE_FOUND",
             f"L2,TOTAL,OVER,160,0.48,,155.0,UNMEASURED,{R}", f"L2,TOTAL,UNDER,160,0.44,,155.0,UNMEASURED,{R}",
             f"L3,TEAM_TOTAL,OVER,80.5,0.70,,78.0,NONE,{R}", f"L3,TEAM_TOTAL,UNDER,80.5,0.30,,78.0,NONE,{R}",
             f"L4,WINNER,HOME,,0.55,,,NONE,{R}", f"L4,WINNER,AWAY,,0.45,,,NONE,{R}"]
    facts = [f"{s},{f},MISSING,no page lists it," for s in ("HOME", "AWAY") for f in FACTS]
    s = O.intake(drop(tmp_path, [card(picks=picks, facts=facts, not_started_source="https://example.org/odds-free/fixture")]), tmp_path / "in")
    assert (s["ADMITTED"], s["supplied_lines"], s["priced_lines"]) == (1, 4, 3)
    rows = {(r["label"], r["side"]): r for r in O.read_csv(tmp_path / "in/PICKS.csv")}
    assert rows[("L1", "OVER")]["flags"] == "UNPRICED;NO_RESULT_SOURCE" and rows[("L1", "OVER")]["rank"] == ""
    assert set(rows[("L2", "OVER")]["flags"].split(";")) == {"NO_DIRECTION", "UNMEASURED_AVAILABILITY_PRICED", "CONTRADICTS_OWN_CENTRE"}
    assert rows[("L3", "OVER")]["flags"] == "CONTRADICTS_OWN_CENTRE" and rows[("L3", "OVER")]["rank"] == "1"
    assert O.read_csv(tmp_path / "in/CARDS.csv")[0]["facts_observed"] == "0"


def test_one_game_one_card_and_a_repeated_snapshot_is_taken_once(tmp_path):
    d = drop(tmp_path, [card(), card(), card(key="CHAT2-G0001")])
    s = O.intake(d, tmp_path / "in")
    assert (s["ADMITTED"], s["DUPLICATE_GAME"]) == (1, 1)
    cards = O.read_csv(tmp_path / "in/CARDS.csv")
    assert [c["card_key"] for c in cards if c["status"] == "ADMITTED"] == ["CHAT1-G0001"]


def outcomes(tmp_path, keys, start=START, capture="a" * 64, name="OUTCOMES.csv", grade=None, over=lambda n: True):
    rows = []
    for n, key in enumerate(keys):
        for label, side, won in (("L1", "HOME", False), ("L1", "AWAY", True), ("L2", "OVER", over(n)), ("L2", "UNDER", not over(n))):
            rows.append(dict(card_key=key, label=label, side=side, grade=grade or ("WIN" if won else "LOSS"), actual_start=start,
                             settled_at=f"2026-11-20T{11 + n // 60:02d}:{n % 60:02d}:00+00:00", final_source=R, final_capture_sha256=capture))
    path = tmp_path / name
    path.write_bytes(O.csv_bytes(O.OUTCOME_FIELDS, rows))
    return path


def many(tmp_path, n):
    return drop(tmp_path, [card(key=f"CHAT1-G{i:04d}", home=f"Home {i}", away=f"Away {i}") for i in range(1, n + 1)])


def test_progress_on_request_and_the_frozen_first_hundred(tmp_path):
    O.intake(many(tmp_path, 102), tmp_path / "in")
    keys = [f"CHAT1-G{i:04d}" for i in range(1, 103)]
    few = O.score([tmp_path / "in"], outcomes(tmp_path, keys[:5], name="few.csv"), tmp_path / "s1")
    assert (few["assessment_status"], few["finding"], few["eligible_games"]) == ("PROGRESS", "NOT_ASSESSED", 5)
    # per game: (0.53-1)^2, (0.47-0)^2, (0.62-1)^2, (0.38-0)^2 -> mean 0.18265, minus 0.25
    assert few["brier_minus_quarter_mean"] == pytest.approx(-0.06735)
    asked = O.score([tmp_path / "in"], outcomes(tmp_path, keys[:5], name="few.csv"), tmp_path / "s2", on_request=True)
    assert (asked["assessment_status"], asked["finding"]) == ("AUDITED_ON_REQUEST", "NOT_ASSESSED")
    assert not (tmp_path / "s2/COHORT.csv").exists()
    full = outcomes(tmp_path, keys, name="full.csv", over=lambda n: n % 4 != 0)
    ready = O.score([tmp_path / "in"], full, tmp_path / "s3")
    assert (ready["assessment_status"], ready["games_scored"], ready["eligible_games"]) == ("READY", 100, 102)
    assert ready["finding"] == "MEETS_REGISTERED_CRITERION" and ready["brier_minus_quarter_hi"] < 0
    cohort = O.read_csv(tmp_path / "s3/COHORT.csv")
    assert len(cohort) == 100 and [c["card_key"] for c in cohort] == keys[:100]
    again = O.score([tmp_path / "in"], full, tmp_path / "s4", cohort=tmp_path / "s3/COHORT.csv")
    assert again["games_scored"] == 100 and not (tmp_path / "s4/COHORT.csv").exists()
    with pytest.raises(O.OneChatError, match="cannot be combined"):
        O.score([tmp_path / "in"], full, tmp_path / "s5", on_request=True, cohort=tmp_path / "s3/COHORT.csv")
    tables = {(t["table"], t["stratum"]): t for t in O.read_csv(tmp_path / "s3/TABLES.csv")}
    assert tables[("rank", "1")]["win_rate"] == "0.75" and tables[("hypothesis_flag_favoured", "NO_DIRECTION")]["rows"] == "100"
    worse = O.score([tmp_path / "in"], outcomes(tmp_path, keys, name="coin.csv", over=lambda n: n % 2 == 0), tmp_path / "s6")
    assert worse["finding"] == "DOES_NOT_MEET_REGISTERED_CRITERION"


def test_unsettled_unpriced_late_and_uncaptured_games_do_not_count(tmp_path):
    late = card(key="CHAT1-G0002", home="Gamma", away="Delta", research_start_at="2026-11-20T08:30:00+00:00", request_at="2026-11-20T08:20:00+00:00",
                research_end_at="2026-11-20T09:00:00+00:00", not_started_observed_at="2026-11-20T08:40:00+00:00")
    exposed = card(key="CHAT1-G0003", home="Eps", away="Zeta", outcome_exposure="saw the first-quarter score")
    unpriced = card(key="CHAT1-G0004", home="Eta", away="Theta", picks=DEFAULT[:2] + [f"L2,TOTAL,OVER,158.5,UNPRICED,LEAN,,NONE,{R}", f"L2,TOTAL,UNDER,158.5,UNPRICED,,,NONE,{R}"])
    pending = card(key="CHAT1-G0005", home="Iota", away="Kappa")
    O.intake(drop(tmp_path, [card(), late, exposed, unpriced, pending]), tmp_path / "in")
    path = outcomes(tmp_path, ["CHAT1-G0001", "CHAT1-G0002", "CHAT1-G0003", "CHAT1-G0004"])
    s = O.score([tmp_path / "in"], path, tmp_path / "s", on_request=True)
    cover = {c["card_key"]: c for c in O.read_csv(tmp_path / "s/COVERAGE.csv")}
    assert s["eligible_games"] == 1 and cover["CHAT1-G0001"]["timing"] == "PRE_START_SAVED"
    assert [cover[f"CHAT1-G000{i}"]["exclusion"] for i in (2, 3, 4, 5)] == ["POST_START", "OUTCOME_EXPOSED", "UNPRICED_SUPPLIED_LINE", "NOT_FULLY_SETTLED"]
    assert s["priced_share"] == pytest.approx(9 / 10)
    with pytest.raises(O.OneChatError, match="saved capture"):
        O.score([tmp_path / "in"], outcomes(tmp_path, ["CHAT1-G0001"], capture="", name="bad.csv"), tmp_path / "s2")
    with pytest.raises(O.OneChatError, match="not WIN"):
        O.score([tmp_path / "in"], outcomes(tmp_path, ["CHAT1-G0001"], grade="MAYBE", name="bad2.csv"), tmp_path / "s3")


def test_template_lists_the_sports_required_facts():
    text = O.template("Basketball")
    assert all(f"HOME,{f},,," in text for f in FACTS) and O.BLOCK.search(text.replace("<MINI_KEY>", "X"))
