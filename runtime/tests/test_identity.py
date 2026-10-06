"""Unit tests for identity schemas."""

from runtime.src.common.identity import MatchIdentity, Contract, ContractType, SportIdentity


def test_match_identity_determinism():
    m1 = MatchIdentity(
        sport="soccer",
        competition="epl",
        season="2025-2026",
        date="2026-10-10",
        home_team="Arsenal",
        away_team="Chelsea"
    )
    m2 = MatchIdentity(
        sport="soccer",
        competition="epl",
        season="2025-2026",
        date="2026-10-10",
        home_team="Arsenal",
        away_team="Chelsea"
    )
    assert m1.match_id == m2.match_id
    assert "arsenal" in m1.match_id
    assert "chelsea" in m1.match_id


def test_sport_identity_coverage():
    expected_sports = {
        "cricket", "basketball", "american_football", "baseball",
        "afl", "nrl", "soccer", "nhl"
    }
    actual_sports = {s.value for s in SportIdentity}
    assert expected_sports == actual_sports


def test_contract_dataclass():
    c = Contract(
        contract_id="test_contract_1",
        contract_type=ContractType.SPREAD,
        target_side="home",
        line=-3.5,
        stated_prob=0.58,
        market_prob=0.52
    )
    assert c.line == -3.5
    assert c.stated_prob == 0.58
    assert c.contract_type == ContractType.SPREAD

