"""v29.2 fixes from the two external reviews of 22 November 2026: contract semantics, coherence across lines, kit row
naming, replay clocks and the separately registered shadow selection policy (SELECT-SHADOW-v1)."""

import pytest

from ml import forecast_integrity as F
from ml import one_chat as O
from ml import one_chat_ops as OPS
from ml import selection_shadow as S
from ml.tests import test_one_chat as M

repo = M.repo
R = M.R


# --- contract semantics: a tennis games spread is not the match winner -------------------------------------------------

def test_a_tennis_games_spread_is_not_read_as_the_match_winner():
    text = ("Upcoming Tennis Match: PlayerX vs PlayerY, ATP Challenger,\n"
            "Estimated Game Time Start: 22 November 2026, 7:00 PM AEDT\n\nPlayerX Games -0.5\nPlayerY ML\n")
    rows = OPS.contracts_for(OPS.parse_message(text))
    assert [(r["label"], r["family"], r["line"]) for r in rows] == [
        ("L1", "HANDICAP", "-0.5"), ("L1", "HANDICAP", "0.5"), ("L2", "WINNER", ""), ("L2", "WINNER", "")]
    tennis = [dict(label="L1", family="HANDICAP", side=s, line=v, period="FULL_MATCH", endpoint="COMPLETED_MATCH",
                   action="STANDARD", unit="GAMES") for s, v in (("HOME", "-0.5"), ("AWAY", "0.5"))]
    assert not F.winner_by_margin("Tennis", tennis)
    assert F.winner_by_margin("Basketball", [dict(r, unit="POINTS") for r in tennis])
    assert not F.winner_by_margin("Basketball", [dict(r, unit="REBOUNDS") for r in tennis])


# --- coherence across lines: a flag and a check-drop warning, never a refusal -------------------------------------------

def coherent_card(over_low, over_high):
    picks = [f"L1,TOTAL,OVER,149.5,{over_low},,152,NONE,{R}", f"L1,TOTAL,UNDER,149.5,{1 - over_low:.2f},,152,NONE,{R}",
             f"L2,TOTAL,OVER,154.5,{over_high},,152,NONE,{R}", f"L2,TOTAL,UNDER,154.5,{1 - over_high:.2f},,152,NONE,{R}"]
    return M.card(picks=picks)


def test_a_harder_over_priced_above_an_easier_one_is_flagged_not_refused(tmp_path):
    O.intake(M.drop(tmp_path, [coherent_card(0.70, 0.80)]), tmp_path / "in")
    assert O.read_csv(tmp_path / "in/CARDS.csv")[0]["status"] == "ADMITTED"
    rows = O.read_csv(tmp_path / "in/PICKS.csv")
    assert all("INCOHERENT_ACROSS_LINES" in r["flags"] for r in rows)
    meta, picks, facts = O.parse(O.BLOCK.search(coherent_card(0.70, 0.80))["body"])
    problems, derived = O.check(meta, picks, facts, "CHAT1-G0001")
    assert problems == [] and set(O.incoherent_labels(derived)) == {"L1", "L2"}
    meta, picks, facts = O.parse(O.BLOCK.search(coherent_card(0.80, 0.70))["body"])
    assert O.incoherent_labels(O.check(meta, picks, facts, "CHAT1-G0001")[1]) == {}


def test_a_harder_home_handicap_priced_above_an_easier_one_is_flagged():
    picks = [f"L1,HANDICAP,HOME,-7.5,0.60,,,NONE,{R}", f"L1,HANDICAP,AWAY,7.5,0.40,,,NONE,{R}",
             f"L2,HANDICAP,HOME,-3.5,0.55,,,NONE,{R}", f"L2,HANDICAP,AWAY,3.5,0.45,,,NONE,{R}"]
    meta, pk, facts = O.parse(O.BLOCK.search(M.card(picks=picks))["body"])
    assert set(O.incoherent_labels(O.check(meta, pk, facts, "CHAT1-G0001")[1])) == {"L1", "L2"}


# --- kit row naming: the packet names the row, the kit is unchanged ------------------------------------------------------

@pytest.mark.parametrize("sport,competition,needle", [
    ("Basketball", "NBL", "`Basketball/NBL` (its own row"),
    ("Basketball", "Australia NBL", "Rows named inside this competition's name: `Basketball/NBL`"),
    ("Basketball", "NBA Cup group stage", "`Basketball/NBA`. Pass the one"),
    ("Basketball", "NBA Cup group stage", "`FAMILY_PRIOR:BASKETBALL_FIBA40`"),
    ("Tennis", "ATP Challenger", "no row and no family prior"),
])
def test_the_chat_packet_names_the_kit_row_and_any_fallback(sport, competition, needle):
    assert needle in OPS.kit_row_note(sport, competition)


# --- replay clocks ------------------------------------------------------------------------------------------------------

def timing_card(**over):
    base = dict(research_start_at="2026-11-20T05:05:00+00:00", not_started_observed_at="2026-11-20T06:25:00+00:00",
                research_end_at="2026-11-20T06:30:00+00:00", facts_last_observed_at="", outcome_exposure="NONE")
    return dict(base, **over)


def test_a_seal_at_the_exact_first_play_is_not_pre_start():
    seal = dict(seal="SEALED", seal_time="2026-11-20T08:00:00+00:00", seal_basis="SERVER_PUSH_TIME")
    assert O.timing_label(timing_card(), "2026-11-20T08:00:00+00:00", seal) == "SEALED_AFTER_START"
    assert O.timing_label(timing_card(), "2026-11-20T08:00:01+00:00", seal) == O.ELIGIBLE
    assert O.timing_label(timing_card(research_end_at="2026-11-20T08:00:00+00:00"), "2026-11-20T08:00:00+00:00",
                          seal) == "POST_START"


def test_a_replay_never_uses_a_settlement_or_seal_made_after_as_of(repo, tmp_path):
    folder = M.build(repo, tmp_path, [M.card()])                     # sealed 07:00Z; first play 08:00Z; settled 11:00Z
    path = M.outcomes(repo, tmp_path / "cap", ["CHAT1-G0001"])
    M.commit_all(repo)
    now = M.run(repo, tmp_path, [folder], [path], "now")
    assert now["sealed_pre_start_server"] == 1 and now["games_in_sequence"] == 1
    before_settled = M.run(repo, tmp_path, [folder], [path], "early", as_of="2026-11-20T09:00:00+00:00")
    assert before_settled["games_in_sequence"] == 0
    cover = O.read_csv(repo / "research/one_chat/scores/early/COVERAGE.csv")[0]
    assert cover["exclusion"] == "NOT_FULLY_SETTLED"
    before_sealed = M.run(repo, tmp_path, [folder], [path], "earlier", as_of="2026-11-20T06:00:00+00:00")
    assert O.read_csv(repo / "research/one_chat/scores/earlier/COVERAGE.csv")[0]["seal"] == "SEALED_AFTER_AS_OF"
    assert before_sealed["games_in_sequence"] == 0


# --- SELECT-SHADOW-v1 ---------------------------------------------------------------------------------------------------

def pick(label, family, side, line, p, flags="", fav="Y", rank=""):
    return dict(card_key="K", game_id="G", label=label, family=family, side=side, line=line, p=str(p), favoured=fav,
                rank=rank, flags=flags)


def hockey_contracts(action):
    scope = dict(period="FULL_GAME", endpoint="FINAL_SCORE", action=action)
    return [dict(label="L1", family="HANDICAP", side="AWAY", line="-0.5", unit="GOALS", **scope),
            dict(label="L1", family="HANDICAP", side="HOME", line="0.5", unit="GOALS", **scope),
            dict(label="L2", family="WINNER", side="AWAY", line="", unit="GAMES", **scope),
            dict(label="L2", family="WINNER", side="HOME", line="", unit="GAMES", **scope)]


def shadow_picks():
    return [pick("L1", "HANDICAP", "AWAY", "-0.5", 0.66, rank="1"), pick("L1", "HANDICAP", "HOME", "0.5", 0.34, fav=""),
            pick("L2", "WINNER", "AWAY", "", 0.65, rank="2"), pick("L2", "WINNER", "HOME", "", 0.35, fav=""),
            pick("L3", "TOTAL", "OVER", "5.5", 0.52, flags="NO_DIRECTION", rank="3"),
            pick("L3", "TOTAL", "UNDER", "5.5", 0.48, fav="")]


def test_the_shadow_list_drops_coin_flips_duplicates_and_may_be_empty():
    cards = {"K": dict(sport="Ice Hockey")}
    out = S.select(shadow_picks(), cards, {"K": hockey_contracts("INCLUDE_OT_SO")})
    signal = [(r["slot"], r["label"]) for r in out if r["policy"] == "SHADOW_SIGNAL"]
    assert signal == [(1, "L1")]                                          # L2 is the same winner; L3 has no direction
    dropped = {r["label"]: r["reason"] for r in out if r["policy"] == "SHADOW_SIGNAL_DROPPED"}
    assert dropped == {"L2": "SAME_CONTRACT_AS_A_HIGHER_PICK", "L3": "NO_DIRECTION"}
    assert [(r["slot"], r["label"]) for r in out if r["policy"] == "REGISTERED_RANK"] == [(1, "L1"), (2, "L2")]
    flat = [dict(p, flags="UNMEASURED_AVAILABILITY_PRICED") for p in shadow_picks()]
    strict = [r for r in S.select(flat, cards) if r["policy"] == "SHADOW_STRICT"]
    assert [r["reason"] for r in strict] == ["NO_STRONG_PICK"]


@pytest.mark.parametrize("contracts", [None, {"K": hockey_contracts("REGULATION_ONLY")}])
def test_the_shadow_list_keeps_contracts_the_definitions_do_not_make_equal(contracts):
    # Codex review of #12: regulation-time hockey can draw, and without definitions nothing is merged.
    out = S.select(shadow_picks(), {"K": dict(sport="Ice Hockey")}, contracts)
    assert [(r["slot"], r["label"]) for r in out if r["policy"] == "SHADOW_SIGNAL"] == [(1, "L1"), (2, "L2")]


def test_the_checkpoint_follows_the_registered_order_and_needs_both_inputs():
    picks = [dict(pick("L1", "TOTAL", "OVER", "150.5", 0.62, rank="1"), card_key=k, game_id=k)
             for k in ("A-LATE", "Z-EARLY")]
    cards = {"A-LATE": dict(scheduled_start="2026-12-02T08:00:00+00:00", game_id="A-LATE"),
             "Z-EARLY": dict(scheduled_start="2026-12-01T08:00:00+00:00", game_id="Z-EARLY")}
    selected = S.select(picks, cards)
    grades = {("A-LATE", "L1", "OVER"): "WIN", ("Z-EARLY", "L1", "OVER"): "LOSS"}
    old, S.CHECKPOINT = S.CHECKPOINT, 1
    try:
        first = S.compare(selected, grades, cards=cards, confirmatory=True)[0]
        assert first["games"] == 1 and first["variant_hit_rate"] == 0.0     # Z-EARLY (a loss) is the first game
        assert first["verdict"] == "NOT_DEMONSTRATED"
        assert S.compare(selected, grades, cards=cards)[0]["verdict"] == "DESCRIPTIVE_INCOMPLETE_INPUTS"
    finally:
        S.CHECKPOINT = old


def test_the_shadow_score_keeps_the_denominator_and_the_decision_waits_for_100_games():
    picks = [pick("L1", "HANDICAP", "HOME", "-3.5", 0.60, rank="1"), pick("L1", "HANDICAP", "AWAY", "3.5", 0.40, fav=""),
             pick("L2", "TOTAL", "OVER", "150.5", 0.58, rank="2"), pick("L2", "TOTAL", "UNDER", "150.5", 0.42, fav="")]
    selected = S.select(picks, {"K": dict(sport="Basketball")})
    grades = {("K", "L1", "HOME"): "WIN", ("K", "L2", "OVER"): "LOSS"}
    rows = {r["policy"]: r for r in S.score(selected, grades)}
    assert (rows["REGISTERED_RANK"]["picks"], rows["REGISTERED_RANK"]["one_won"]) == (2, 1)
    assert rows["SHADOW_SIGNAL"]["pairs"] == 1 and rows["SHADOW_SIGNAL"]["dependent_pairs"] == 0
    verdicts = {r["variant"]: r["verdict"] for r in S.compare(selected, grades, confirmatory=True)}
    assert verdicts == {"SHADOW_SIGNAL": "DESCRIPTIVE_BELOW_100_GAMES", "SHADOW_STRICT": "DESCRIPTIVE_BELOW_100_GAMES"}


# --- late starts (owner, 22 Nov 2026): a request after the scheduled start is a full, counted game ----------------------

def test_a_request_sent_after_the_scheduled_start_is_a_full_counted_game_when_play_starts_late(repo, tmp_path):
    late = "2026-11-20T04:00:00+00:00"           # scheduled start; the request is published 04:30, research 05:05-06:30
    folder = M.build(repo, tmp_path, [M.card(start=late)])               # sealed 07:00
    path = M.outcomes(repo, tmp_path / "cap", ["CHAT1-G0001"], start="2026-11-20T08:00:00+00:00")   # first play 08:00
    M.commit_all(repo)
    s = M.run(repo, tmp_path, [folder], [path], "late")
    cover = O.read_csv(repo / "research/one_chat/scores/late/COVERAGE.csv")[0]
    assert cover["timing"] == O.ELIGIBLE and cover["eligible"] == "Y" and s["games_in_sequence"] == 1
    # The same card, but play had begun before the seal: kept, not counted.
    gone = M.outcomes(repo, tmp_path / "cap", ["CHAT1-G0001"], start="2026-11-20T06:50:00+00:00", name="OUT2.csv")
    M.commit_all(repo)
    M.run(repo, tmp_path, [folder], [gone], "begun")
    begun = O.read_csv(repo / "research/one_chat/scores/begun/COVERAGE.csv")[0]
    assert begun["timing"] == "SEALED_AFTER_START" and begun["eligible"] == ""
