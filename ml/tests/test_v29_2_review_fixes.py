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


# --- coherence across lines (v29.4): compared only on one registered quantity; a flag, never a refusal ------------------

def coherent_card(lines, family="TOTAL", side=("OVER", "UNDER")):
    picks = []
    for n, (x, p) in enumerate(lines, start=1):
        other = -x if family == "HANDICAP" else x
        picks += [f"L{n},{family},{side[0]},{x},{p},,,NONE,{R}", f"L{n},{family},{side[1]},{other},{1 - p:.2f},,,NONE,{R}"]
    return M.card(picks=picks)


def derived_of(card):
    meta, pk, fc = O.parse(O.BLOCK.search(card)["body"])
    problems, derived = O.check(meta, pk, fc, "CHAT1-G0001")
    assert problems == []
    return derived


def scope(family, period="FULL_GAME", endpoint="FINAL_SCORE"):
    return (family, period, endpoint, "STANDARD", "POINTS")


def test_lines_on_one_registered_quantity_are_compared_however_far_apart():
    # Review of 23 Nov 2026: 130.5 at 0.40 and 180.5 at 0.60 escaped the v29.3 25% rule.
    derived = derived_of(coherent_card([(130.5, 0.40), (180.5, 0.60)]))
    assert set(O.incoherent_labels(derived, {"L1": scope("TOTAL"), "L2": scope("TOTAL")})) == {"L1", "L2"}
    assert O.incoherent_labels(derived_of(coherent_card([(130.5, 0.60), (180.5, 0.40)])),
                               {"L1": scope("TOTAL"), "L2": scope("TOTAL")}) == {}


def test_lines_on_different_registered_quantities_or_without_definitions_are_not_compared():
    # Review: 74.5 and 80.5 were compared although they could be different periods.
    derived = derived_of(coherent_card([(74.5, 0.50), (80.5, 0.60)]))
    assert O.incoherent_labels(derived, {"L1": scope("TOTAL", "FIRST_HALF"), "L2": scope("TOTAL")}) == {}
    assert O.incoherent_labels(derived) == {}
    # G0007 (WBBL): a 6-over score and a 20-over innings total on one card.
    derived = derived_of(coherent_card([(148.5, 0.465013), (41.5, 0.452242)]))
    assert O.incoherent_labels(derived, {"L1": scope("TOTAL", "STARS_INNINGS", "CAP_20"),
                                         "L2": scope("TOTAL", "STARS_INNINGS", "END_6")}) == {}


def test_a_harder_home_handicap_priced_above_an_easier_one_is_flagged_on_one_quantity():
    derived = derived_of(coherent_card([(-7.5, 0.60), (-3.5, 0.55)], family="HANDICAP", side=("HOME", "AWAY")))
    assert set(O.incoherent_labels(derived, {"L1": scope("HANDICAP"), "L2": scope("HANDICAP")})) == {"L1", "L2"}


def test_intake_and_score_flag_with_the_same_registered_definitions(repo, tmp_path):
    card = coherent_card([(149.5, 0.70), (154.5, 0.80)])
    folder = M.build(repo, tmp_path, [card])            # registers the request (one quantity), seals, then intake
    rows = O.read_csv(folder / "PICKS.csv")
    assert rows and all("INCOHERENT_ACROSS_LINES" in r["flags"] for r in rows)
    path = M.outcomes(repo, tmp_path / "cap", ["CHAT1-G0001"])
    M.commit_all(repo)
    M.run(repo, tmp_path, [folder], [path], "coherent")
    problems = O.read_csv(repo / "research/one_chat/scores/coherent/CUSTODY_PROBLEMS.csv")
    assert not [p for p in problems if "differ from the exact published block" in p["problem"]], problems


# --- kit row naming: the packet names the row, the kit is unchanged ------------------------------------------------------

@pytest.mark.parametrize("sport,competition,needle", [
    ("Basketball", "NBL", "`Basketball/NBL` (its own row"),
    ("Basketball", "Australia NBL", "`Basketball/NBL` (USABLE_DEVELOPMENT), the reviewed alias"),
    ("Basketball", "NBA Cup group stage", "`Basketball/NBA` (USABLE_DEVELOPMENT), the reviewed alias"),
    ("Basketball", "Some Cup Final", "`FAMILY_PRIOR:BASKETBALL_FIBA40`"),
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


# --- SELECT-SHADOW-v2 ---------------------------------------------------------------------------------------------------

def pick(label, family, side, line, p, flags="", fav="Y", rank="", key="K"):
    return dict(card_key=key, game_id=key, label=label, family=family, side=side, line=line, p=str(p), favoured=fav,
                rank=rank, flags=flags)


def hockey_contracts(action):
    scope_ = dict(period="FULL_GAME", endpoint="FINAL_SCORE", action=action)
    return [dict(label="L1", family="HANDICAP", side="AWAY", line="-0.5", unit="GOALS", **scope_),
            dict(label="L1", family="HANDICAP", side="HOME", line="0.5", unit="GOALS", **scope_),
            dict(label="L2", family="WINNER", side="AWAY", line="", unit="GAMES", **scope_),
            dict(label="L2", family="WINNER", side="HOME", line="", unit="GAMES", **scope_)]


def shadow_picks():
    return [pick("L1", "HANDICAP", "AWAY", "-0.5", 0.66, rank="1"), pick("L1", "HANDICAP", "HOME", "0.5", 0.34, fav=""),
            pick("L2", "WINNER", "AWAY", "", 0.65, rank="2"), pick("L2", "WINNER", "HOME", "", 0.35, fav=""),
            pick("L3", "TOTAL", "OVER", "5.5", 0.52, flags="NO_DIRECTION", rank="3"),
            pick("L3", "TOTAL", "UNDER", "5.5", 0.48, fav="")]


def test_the_shadow_list_drops_coin_flips_duplicates_and_may_be_empty():
    cards = {"K": dict(sport="Ice Hockey", competition="NHL")}
    out = S.select(shadow_picks(), cards, {"K": hockey_contracts("INCLUDE_OT_SO")})
    assert [(r["slot"], r["label"]) for r in out if r["policy"] == "SHADOW_SIGNAL"] == [(1, "L1")]
    dropped = {r["label"]: r["reason"] for r in out if r["policy"] == "SHADOW_SIGNAL_DROPPED"}
    assert dropped == {"L2": "SAME_CONTRACT_AS_A_HIGHER_PICK", "L3": "BELOW_0.55_CONDITIONAL"}
    assert [(r["slot"], r["label"]) for r in out if r["policy"] == "REGISTERED_RANK"] == [(1, "L1"), (2, "L2")]
    flat = [dict(p, flags="UNMEASURED_AVAILABILITY_PRICED") for p in shadow_picks()]
    assert [r["reason"] for r in S.select(flat, cards) if r["policy"] == "SHADOW_STRICT"] == ["NO_STRONG_PICK"]


@pytest.mark.parametrize("contracts", [None, {"K": hockey_contracts("REGULATION_ONLY")}])
def test_the_shadow_list_keeps_contracts_the_definitions_do_not_make_equal(contracts):
    out = S.select(shadow_picks(), {"K": dict(sport="Ice Hockey", competition="NHL")}, contracts)
    assert [(r["slot"], r["label"]) for r in out if r["policy"] == "SHADOW_SIGNAL"] == [(1, "L1"), (2, "L2")]


def test_a_push_does_not_change_which_picks_the_shadow_admits():
    # Review: Over 0.50, Under 0.36, push 0.14 is 58.14% given a decision; v1 dropped it on the raw-p NO_DIRECTION flag.
    picks = [pick("L1", "TOTAL", "OVER", "150", 0.50, flags="NO_DIRECTION", rank="1"),
             pick("L1", "TOTAL", "UNDER", "150", 0.36, fav="")]
    out = [r for r in S.select(picks, {"K": dict(sport="Basketball")}) if r["policy"] == "SHADOW_SIGNAL"]
    assert [(r["label"], r["p_stated"], r["p_push"], r["p_conditional"]) for r in out] == [("L1", 0.5, 0.14, 0.5814)]


def test_conflicting_grades_are_refused_not_overwritten(tmp_path):
    a, b = tmp_path / "a.csv", tmp_path / "b.csv"
    a.write_text("card_key,label,side,grade\nK,L1,OVER,WIN\n", encoding="utf-8")
    b.write_text("card_key,label,side,grade\nK,L1,OVER,LOSS\n", encoding="utf-8")
    with pytest.raises(S.ShadowError, match="conflicting grades"):
        S.read_grades([a, b])
    assert S.read_grades([a, a]) == {("K", "L1", "OVER"): "WIN"}


def two_pick_cards(n, *, grade):
    picks, grades = [], {}
    for i in range(n):
        k = f"C{i:03d}"
        picks += [pick("L1", "HANDICAP", "HOME", "-3.5", 0.62, rank="1", key=k),
                  pick("L1", "HANDICAP", "AWAY", "3.5", 0.38, fav="", key=k),
                  pick("L2", "TOTAL", "OVER", "150.5", 0.51, rank="2", key=k),
                  pick("L2", "TOTAL", "UNDER", "150.5", 0.49, fav="", key=k)]
        grades[(k, "L1", "HOME")] = "WIN"
        grades[(k, "L2", "OVER")] = grade(i)
    return picks, grades


def test_the_decision_is_both_picks_winning_so_a_one_pick_policy_cannot_pass():
    # Review: v1 judged picks one at a time; SIGNAL here issues only L1 (L2 is below 0.55) and wins every pick.
    picks, grades = two_pick_cards(100, grade=lambda i: "WIN" if i % 2 else "LOSS")
    selected = S.select(picks, {})
    keys = sorted({p["card_key"] for p in picks})
    rows = {r["policy"]: r for r in S.score(selected, grades, keys)}
    assert rows["SHADOW_SIGNAL"]["pick_hit_rate"] == 1.0 and rows["SHADOW_SIGNAL"]["requests_with_pair"] == 0
    assert rows["REGISTERED_RANK"]["both_won_per_request"] == 0.5
    verdicts = {r["variant"]: r for r in S.compare(selected, grades, keys, confirmatory=True)}
    assert verdicts["SHADOW_SIGNAL"]["variant_pair_coverage"] == 0.0
    assert verdicts["SHADOW_SIGNAL"]["verdict"] == "NOT_DEMONSTRATED"
    assert S.compare(selected, grades, keys, confirmatory=False)[0]["verdict"] == "DESCRIPTIVE_INPUTS_NOT_VERIFIED"


def test_every_pick_of_an_eligible_request_must_be_graded():
    picks, grades = two_pick_cards(2, grade=lambda i: "WIN")
    del grades[("C001", "L2", "OVER")]
    with pytest.raises(S.ShadowError, match="no grade"):
        S.compare(S.select(picks, {}), grades, ["C000", "C001"], confirmatory=True)


def test_registered_pairs_are_marked_by_quantity():
    picks = [pick("L1", "TOTAL", "OVER", "148.5", 0.60, rank="1"), pick("L1", "TOTAL", "UNDER", "148.5", 0.40, fav=""),
             pick("L2", "TOTAL", "OVER", "150.5", 0.58, rank="2"), pick("L2", "TOTAL", "UNDER", "150.5", 0.42, fav="")]
    defs = [dict(label=lab, family="TOTAL", side=s, line=x, period="FULL_GAME", endpoint="FINAL", action="STANDARD",
                 unit="POINTS") for lab, x in (("L1", "148.5"), ("L2", "150.5")) for s in ("OVER", "UNDER")]
    out = S.select(picks, {"K": dict(sport="Basketball")}, {"K": defs})
    assert {r["pair"] for r in out if r["policy"] == "REGISTERED_RANK"} == {"SAME_QUANTITY"}
    plain = S.select(picks, {"K": dict(sport="Basketball")})
    assert {r["pair"] for r in plain if r["policy"] == "REGISTERED_RANK"} == {"SAME_GAME"}



def test_the_shadow_plan_publication_time_is_read_from_main_history(repo, tmp_path):
    # Codex on PR #14: Repo indexed only the evaluation plan, so the shadow plan's publication was never found.
    plan = repo / S.PLAN
    plan.parent.mkdir(parents=True, exist_ok=True)
    plan.write_bytes((O.ROOT / S.PLAN).read_bytes())
    M.git(repo, "add", S.PLAN)
    M.git(repo, "commit", "-q", "-m", "shadow plan")
    M.git(repo, "push", "-q", "origin", "main")
    head = M.git(repo, "rev-parse", "HEAD")
    M.LIVE_PUSHES[str(repo)].append(dict(before="", after=head, pushed_at_server="2026-11-23T10:00:00Z",
                                         ref="refs/heads/main"))
    score = tmp_path / "score"
    score.mkdir()
    (score / "SUMMARY.csv").write_text("custody_problems\n0\n", encoding="utf-8")
    (score / "SEQUENCE.csv").write_text("card_key\nEARLY\nLATE\n", encoding="utf-8")
    (score / "COVERAGE.csv").write_text("card_key,seal_time\nEARLY,2026-11-23T09:00:00Z\nLATE,2026-11-23T11:00:00Z\n",
                                        encoding="utf-8")
    keep, published, problems = S.registered_sequence(score, repo)
    assert problems == [] and published.startswith("2026-11-23T10:00:00")
    assert keep == ["LATE"]


# --- contract identity (v29.4) --------------------------------------------------------------------------------------------

def test_two_different_totals_are_two_contracts():
    text = ("Upcoming Basketball Game: A vs B, NBL,\nEstimated Game Time Start: 22 November 2026, 7:00 PM AEDT\n\n"
            "Combined Total: Over/Under 140.5 Points\nCombined Total: Over/Under 145.5 Points\n")
    rows = OPS.contracts_for(OPS.parse_message(text))
    assert sorted({(r["label"], r["line"]) for r in rows}) == [("L1", "140.5"), ("L2", "145.5")]


@pytest.mark.parametrize("competition,family", [("NPB", "HANDICAP"), ("KBO", "HANDICAP"), ("MLB", "WINNER")])
def test_a_half_point_run_line_is_the_winner_only_where_a_tie_is_impossible(competition, family):
    # RULES_BASEBALL: KBO/NPB permit ties, so "+0.5" there is never a two-way winner.
    text = (f"Upcoming Baseball Game: Giants vs Tigers, {competition},\n"
            "Estimated Game Time Start: 22 November 2026, 7:00 PM AEDT\n\nGiants +0.5\nTigers -0.5\n")
    rows = OPS.contracts_for(OPS.parse_message(text))
    assert {r["family"] for r in rows} == {family}
    assert {r["request_excerpt"] for r in rows} == {"Giants +0.5", "Tigers -0.5"}


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
