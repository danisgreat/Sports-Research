"""ML-SEP-v1: an unpromoted fitted model never reaches a card (owner instruction 2026-11-09).

Synthetic EXAMPLE competitions only."""
import pytest

from ml import ml_separation as S, picks as P, pregame, reference as R
from ml.tests.test_chat_execution import runtime  # noqa: F401  (pytest fixture)
from ml.tests.test_picks_ledger import META, edit, good_rows, root  # noqa: F401  (pytest fixture)
from ml.tests.test_reference import _write

PROMO = dict(competition="Basketball/EXAMPLE-A", release="EX-1", promoted_at="2027-01-01", lane_evidence="research/x.csv",
             paired_interval="[-0.020, -0.004]", owner_decision="owner decision 2027-01-01")


def test_an_unpromoted_release_is_never_the_reference(root):
    t = R.tier("Basketball/EXAMPLE-A", root)
    assert t["tier"] == "A" and t["release"] == "EX-1" and t["reference"] == "BASELINE_ONLY" and S.RULE in t["basis"]
    _write(root / R.CHOICE, [dict(competition="Basketball/EXAMPLE-A", reference_model="RELEASE:EX-1", basis="b", evidence="e",
                                  declared_for="s", declared_at="d")])
    assert R.tier("Basketball/EXAMPLE-A", root)["reference"] == "BASELINE_ONLY"


def test_a_promotion_row_restores_the_release_reference(root):
    _write(root / S.PROMOTIONS, [PROMO])
    assert R.tier("Basketball/EXAMPLE-A", root)["reference"] == "RELEASE:EX-1"


def test_a_promotion_row_must_carry_its_evidence(root):
    _write(root / S.PROMOTIONS, [dict(PROMO, owner_decision="")])
    with pytest.raises(ValueError, match="owner_decision"):
        S.promoted("Basketball/EXAMPLE-A", root)


def test_the_latest_reference_declaration_is_in_force(root):
    rows = [dict(competition="Basketball/EXAMPLE-B", reference_model=m, basis="b", evidence="e", declared_for="s", declared_at=d)
            for m, d in (("TB1-MD", "2026-10-01"), ("TB2-MD", "2026-11-09"))]
    _write(root / R.CHOICE, rows)
    assert R.reference_choice("Basketball/EXAMPLE-B", root)["reference_model"] == "TB2-MD"


def test_a_card_may_not_print_a_model_probability_or_cite_a_model_reference(root):
    rows = edit(good_rows(), "HOME_ML", model_p="0.5800")
    problems = P.lint(dict(META, model_stage="EXECUTED"), rows, root)
    assert any("model_p must be NONE" in p and S.RULE in p for p in problems), problems
    problems = P.lint(dict(META, reference_id="RELEASE:EX-1"), good_rows(), root)
    assert any("names a fitted model" in p for p in problems), problems
    _write(root / S.PROMOTIONS, [dict(PROMO, competition=META["competition"])])
    assert P.lint(dict(META, model_stage="EXECUTED"), rows, root) == []


def test_the_model_cannot_run_before_the_card_without_a_promotion(runtime):
    with pytest.raises(pregame.PregameError, match=S.RULE):
        pregame.reference(runtime["work"] / "GAME.csv", runtime["work"] / "LINES.csv", runtime["work"] / "fixture.txt",
                          confirmed=True, root=runtime["root"])


def test_the_shadow_block_hides_the_model_numbers(runtime):
    result = dict(stage="SHADOW", status="EXECUTED", release="EX-1", timing_at_generation="PRE_START", reason="",
                  receipt=str(runtime["work"] / "r.csv"), competition="Basketball/EXAMPLE-NEVER-PROMOTED",
                  results=[dict(label="HOME_ML", p_card="0.6123", baseline_p="0.55", model_rank="1")])
    text = pregame.markdown(result)
    assert "0.6123" not in text and S.RULE in text and "unchanged by this block" in text


def test_model_reference_names_are_recognised():
    assert S.is_model_reference("RELEASE:NHL-CYCLE-6") and S.is_model_reference("NBA-CYCLE-4")
    assert not S.is_model_reference("TB2-MD:NBA") and not S.is_model_reference("BASELINE_LEAGUE_V1:COMPETITION_ROW:X")


def test_the_repository_promotes_no_model_today():
    from ml.reference import ROOT
    assert S.promotions(ROOT) == []
    for competition in ("Basketball/NBA", "Ice Hockey/NHL", "Baseball/MLB"):
        assert not S.is_model_reference(R.tier(competition, ROOT)["reference"]), competition
