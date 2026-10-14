"""Archive parsing: score-text patterns, nested team names, stage vocabulary."""
from ml.data import archive as A


def test_afl_score_text_parses_and_orders():
    m = A.AFL_RE.match("Sydney Swans 8.8 (56) def. by Brisbane Lions 12.9 (81)")
    assert m and int(m["p1"]) == 56 and int(m["p2"]) == 81 and m["verb"] == "def. by"


def test_nested_names_resolve_by_exact_then_jaccard():
    assert A._which("Sydney", "Sydney", "Greater Western Sydney") == "home"
    assert A._which("Greater Western Sydney", "Sydney", "Greater Western Sydney") == "away"
    assert A._which("GWS GIANTS", "Greater Western Sydney", "Sydney") == "home"
    assert A._which("Port Adelaide", "Adelaide", "Port Adelaide") == "away"
    assert A._which("North Melbourne", "Melbourne", "North Melbourne") == "away"


def test_nfl_score_text_with_digits_in_name():
    m = A.NFL_RE.match("San Francisco 49ers 24 def. Los Angeles Rams 17")
    assert m and m["t1"] == "San Francisco 49ers" and int(m["p1"]) == 24 and int(m["p2"]) == 17


def test_stage_vocabulary():
    assert A.stage_of("Regular Season") == "REG"
    assert A.stage_of("League") == "REG"
    assert A.stage_of("pre-Season") == "PRE"
    assert A.stage_of("Pre-Season / NBL Blitz") == "PRE"
    assert A.stage_of("Grand Final") == "POST"
    assert A.stage_of("Not applicable") == "OTHER"


def test_integrity_gate_flags_always_no_overtime_but_not_blank_fields():
    from ml.config import integrity_warnings
    flagged = integrity_warnings("Basketball", (900, 900, 0), {})
    assert flagged and flagged[0].startswith("OVERTIME_FIELD_IMPLAUSIBLE")
    assert integrity_warnings("Basketball", (1300, 0, 0), {}) == ()          # blank field = missing, not suspect
    assert integrity_warnings("Basketball", (817, 817, 42), {}) == ()        # EuroCup-like 5% share passes


def test_integrity_gate_flags_collapsed_season_dispersion():
    from ml.config import integrity_warnings
    import random
    rnd = random.Random(1)
    m = {y: [rnd.gauss(0, 12) for _ in range(100)] for y in range(2000, 2010)}
    m[2004] = [rnd.gauss(0, 3) for _ in range(100)]
    w = integrity_warnings("Basketball", (0, 0, 0), {y: [round(x) for x in v] for y, v in m.items()})
    assert w == ("IMPLAUSIBLE_SCORE_DISPERSION:2004",)


def test_status_for_data_hold():
    from ml.evaluation.writers import status_for
    assert status_for("PASS_DEVELOPMENT", ()) == "SHADOW_CANDIDATE"
    assert status_for("PASS_DEVELOPMENT", ("OVERTIME_FIELD_IMPLAUSIBLE:0/900",)) == "DATA_HOLD"
    assert status_for("FAIL_DEVELOPMENT", ("x",)) == "DEVELOPMENT_ONLY"


def test_zero_zero_placeholders_by_sport():
    from ml.config import is_placeholder_zero
    assert is_placeholder_zero("State Level AFL", 0, 0, False)        # VFL 2021 cancelled-season rows
    assert is_placeholder_zero("Basketball", 0, 0, False)
    assert is_placeholder_zero("Baseball", 0, 0, False)              # MLB 2001 / KBO 2008-14 placeholder rows
    assert not is_placeholder_zero("Baseball", 0, 0, True)           # genuine scoreless extra-inning tie (NPB/KBO)
    assert not is_placeholder_zero("Soccer", 0, 0, False)            # 0-0 is a real soccer result
    assert not is_placeholder_zero("Ice Hockey", 0, 0, False)
    assert not is_placeholder_zero("AFL", 50, 0, False)
