"""v29.2 (CR-2026.11.22-R1): a request that registers can always be carded, and one contract is registered once.

The fixtures are the owner's real drops that failed or misbehaved on `card-drops` between 18 and 22 November 2026:
the AHL request written with `ML` as a line (crashed with "could not convert string to float"), the NHL request
registered with one side per label (registered, but no card could ever pass), and the re-registered AHL request
whose two labels were one two-way contract (P-689 counted one result twice).
"""

from pathlib import Path

import pytest

from ml import forecast_integrity as F
from ml import one_chat as O
from ml import one_chat_ops as OPS
from ml.tests import test_one_chat as M

repo = M.repo

HEAD = "label,family,side,line,period,endpoint,action,unit,request_excerpt,baseline_p,baseline_id\n"
BASE = ",,UNAVAILABLE:NO_FROZEN_SPORTING_BASELINE"
AHL_EVENT = ("event_id,sport,competition,home,away,scheduled_start,schedule_source\n"
             "AHL:1029340,Ice Hockey,AHL,Syracuse Crunch,Rochester Americans,2026-11-19T11:00:00+11:00,"
             "https://theahl.com/stats/schedule/323/94\n")
AHL_ML_TEXT = ("Upcoming Ice Hockey Game: ROC Americans @ SYR Crunch, AHL,\n"
               "Estimated Game Time Start: 19 November 2026, 11:00 AM AEDT (can be delayed so continue the process as normal)\n\n"
               "Americans ML\nCrunch ML\nCombined Total Goals: Over/Under 5.5 goals\n")
AHL_TEXT = AHL_ML_TEXT.replace("Americans ML\nCrunch ML", "Americans -0.5\nCrunch -0.5")
NHL_EVENT = ("event_id,sport,competition,home,away,scheduled_start,schedule_source\n"
             "NHL:2026020364,Ice Hockey,NHL Regular Season,Toronto Maple Leafs,Columbus Blue Jackets,"
             "2026-11-22T11:00:00+11:00,https://www.nhl.com/schedule\n")
NHL_TEXT = ("Upcoming Ice Hockey Game: Blue Jackets @ Maple Leafs, NHL Regular Season,\n"
            "Estimated Game Time Start: 22 November 2026, 11:00 AM AEDT\n\n"
            "Blue Jackets +0.5\nMaple Leafs +0.5\nCombined Total: Over/Under 6.5 Goals\n")
OT_SO = "FULL_GAME,FINAL_SCORE,INCLUDE_OT_SO"


def row(label, family, side, line, excerpt, unit="goals", scope=OT_SO):
    return f"{label},{family},{side},{line},{scope},{unit},{excerpt}{BASE}\n"


def payload(text, event, *rows):
    return {"REQUEST.txt": text.encode(), "EVENT.csv": event.encode(), "CONTRACTS.csv": (HEAD + "".join(rows)).encode()}


AHL_TOTAL = (row("L3", "TOTAL", "OVER", "5.5", "Combined Total Goals: Over/Under 5.5 goals"),
             row("L3", "TOTAL", "UNDER", "5.5", "Combined Total Goals: Over/Under 5.5 goals"))
# The request as re-registered (20261118DA6D9F6251746B979F5895FA-G0005, sealed; P-689).
AHL_TWICE = payload(AHL_TEXT, AHL_EVENT,
                    row("L1", "HANDICAP", "AWAY", "-0.5", "Americans -0.5"),
                    row("L1", "HANDICAP", "HOME", "0.5", "Americans -0.5"),
                    row("L2", "HANDICAP", "HOME", "-0.5", "Crunch -0.5"),
                    row("L2", "HANDICAP", "AWAY", "0.5", "Crunch -0.5"), *AHL_TOTAL)


def register(tmp_path, data, key="MINI-G0001"):
    src = tmp_path / "src"
    src.mkdir(exist_ok=True)
    for name, raw in data.items():
        (src / name).write_bytes(raw)
    return F.register_request(src / "REQUEST.txt", src / "EVENT.csv", src / "CONTRACTS.csv", key, tmp_path / "staging")


def test_moneyline_written_as_a_line_gets_a_reason_not_a_crash(tmp_path):
    # 20261118DA6D9F6251746B979F5895FA-G0004 as dropped on 18 Nov 2026.
    ml = payload(AHL_ML_TEXT, AHL_EVENT, row("L1", "WINNER", "AWAY", "ML", "Americans ML", unit="games"),
                 row("L1", "WINNER", "HOME", "ML", "Crunch ML", unit="games"),
                 row("L2", "TOTAL", "OVER", "5.5", "Combined Total Goals: Over/Under 5.5 goals"),
                 row("L2", "TOTAL", "UNDER", "5.5", "Combined Total Goals: Over/Under 5.5 goals"))
    problems = F.request_problems(ml)
    assert problems and not any("could not convert" in p for p in problems)
    assert any("not 'ML'" in p and "WINNER line with the line left empty" in p for p in problems)
    with pytest.raises(ValueError, match="WINNER line with the line left empty"):
        register(tmp_path, ml)


def test_a_line_with_one_side_is_refused_when_registered(tmp_path):
    # 20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0004 registered on 22 Nov 2026; its card was refused for this.
    one_sided = payload(NHL_TEXT, NHL_EVENT, row("L1", "HANDICAP", "AWAY", "+0.5", "Blue Jackets +0.5"),
                        row("L2", "HANDICAP", "HOME", "+0.5", "Maple Leafs +0.5"),
                        row("L3", "TOTAL", "OVER", "6.5", "Combined Total: Over/Under 6.5 Goals"),
                        row("L3", "TOTAL", "UNDER", "6.5", "Combined Total: Over/Under 6.5 Goals"))
    assert F.request_problems(one_sided) == []          # seal-time check unchanged: it was accepted then
    with pytest.raises(ValueError) as exc:
        register(tmp_path, one_sided)
    assert "request L1: both sides of the line are required" in str(exc.value) and "only AWAY" in str(exc.value)
    assert "request L2: both sides" in str(exc.value)
    assert not (tmp_path / "staging" / F.request_path("MINI-G0001")).exists()


def test_two_different_spreads_under_one_label_are_refused_when_registered(tmp_path):
    # 20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0006 registered on 22 Nov 2026; its card was refused as
    # "the two handicap lines must be equal and opposite". They are two contracts: two labels, both sides each.
    text = ("Upcoming Ice Hockey Game: Torpedo @ Aktobe, Jastar Hokei Ligasy 2026-27,\n"
            "Estimated Game Time Start: 22 November 2026, 7:00 PM AEDT\n\nAktobe +4.5\nTorpedo -3.5\n")
    event = NHL_EVENT.replace("NHL:2026020364,Ice Hockey,NHL Regular Season,Toronto Maple Leafs,Columbus Blue Jackets",
                              "SHAIBA:39216,Ice Hockey,Jastar Hokei Ligasy 2026-27,MHK Aktobe U20,MHK Torpedo U20")
    one_label = payload(text, event, row("L1", "HANDICAP", "HOME", "+4.5", "Aktobe +4.5"),
                        row("L1", "HANDICAP", "AWAY", "-3.5", "Torpedo -3.5"))
    with pytest.raises(ValueError, match="request L1: the two handicap lines must be equal and opposite"):
        register(tmp_path, one_label)
    two_labels = payload(text, event, row("L1", "HANDICAP", "HOME", "+4.5", "Aktobe +4.5"),
                         row("L1", "HANDICAP", "AWAY", "-4.5", "Aktobe +4.5"),
                         row("L2", "HANDICAP", "AWAY", "-3.5", "Torpedo -3.5"),
                         row("L2", "HANDICAP", "HOME", "+3.5", "Torpedo -3.5"))
    assert register(tmp_path, two_labels)["status"] == "REGISTERED"


def test_one_two_way_contract_registered_twice_is_refused_and_the_single_winner_registers(tmp_path):
    with pytest.raises(ValueError, match="the same two-way contract twice"):
        register(tmp_path, AHL_TWICE)
    once = payload(AHL_TEXT, AHL_EVENT, row("L1", "WINNER", "AWAY", "", "Americans -0.5", unit="games"),
                   row("L1", "WINNER", "HOME", "", "Crunch -0.5", unit="games"), *AHL_TOTAL)
    assert register(tmp_path, once)["status"] == "REGISTERED"
    # A moneyline and a half-point spread for the same game are also one contract where no draw is possible.
    both = payload(AHL_ML_TEXT + "Americans -0.5\n", AHL_EVENT,
                   row("L1", "WINNER", "AWAY", "", "Americans ML", unit="games"),
                   row("L1", "WINNER", "HOME", "", "Crunch ML", unit="games"),
                   row("L2", "HANDICAP", "AWAY", "-0.5", "Americans -0.5"),
                   row("L2", "HANDICAP", "HOME", "0.5", "Americans -0.5"))
    assert any("same two-way contract" in p for p in F.contract_problems(both))


def test_half_point_handicaps_stay_two_contracts_where_a_draw_is_possible():
    text = "Upcoming Soccer Game: A vs B, League,\nA -0.5\nB -0.5\n"
    event = AHL_EVENT.replace("AHL:1029340,Ice Hockey,AHL", "LG:1,Soccer,League")
    regulation = "FULL_MATCH,REGULATION_90,STANDARD"
    soccer = payload(text, event, row("L1", "HANDICAP", "HOME", "-0.5", "A -0.5", scope=regulation),
                     row("L1", "HANDICAP", "AWAY", "0.5", "A -0.5", scope=regulation),
                     row("L2", "HANDICAP", "AWAY", "-0.5", "B -0.5", scope=regulation),
                     row("L2", "HANDICAP", "HOME", "0.5", "B -0.5", scope=regulation))
    assert F.contract_problems(soccer) == []
    # Ice hockey settled on regulation time can draw too.
    reg = payload(AHL_TEXT, AHL_EVENT, *(r.replace("INCLUDE_OT_SO", "REGULATION_ONLY") for r in (
        row("L1", "HANDICAP", "AWAY", "-0.5", "Americans -0.5"), row("L1", "HANDICAP", "HOME", "0.5", "Americans -0.5"),
        row("L2", "HANDICAP", "HOME", "-0.5", "Crunch -0.5"), row("L2", "HANDICAP", "AWAY", "0.5", "Crunch -0.5"))))
    assert F.contract_problems(reg) == []
    # The exact same contract twice is refused in any sport.
    dup = payload(text, event, row("L1", "HANDICAP", "HOME", "-0.5", "A -0.5", scope=regulation),
                  row("L1", "HANDICAP", "AWAY", "0.5", "A -0.5", scope=regulation),
                  row("L2", "HANDICAP", "HOME", "-0.5", "A -0.5", scope=regulation),
                  row("L2", "HANDICAP", "AWAY", "0.5", "A -0.5", scope=regulation))
    assert any("the same contract twice" in p for p in F.contract_problems(dup))


def test_an_identical_earlier_registration_is_still_recognised(tmp_path):
    """Sealed history keeps its rules: the P-689 request re-pushed byte for byte is ALREADY_REGISTERED, not refused."""
    folder = tmp_path / "staging" / F.request_path("MINI-G0005")
    folder.mkdir(parents=True)
    for name, raw in AHL_TWICE.items():
        (folder / name).write_bytes(raw)
    (folder / "MANIFEST.csv").write_bytes(F.csv_bytes(("file", "sha256"), [
        dict(file=n, sha256=F.digest(AHL_TWICE[n])) for n in F.REQUEST_FILES]))
    assert F.request_problems(AHL_TWICE) == []
    assert register(tmp_path, AHL_TWICE, key="MINI-G0005")["status"] == "ALREADY_REGISTERED"


@pytest.mark.parametrize("text,winner_excerpts", [
    (AHL_TEXT, ("Americans -0.5",)),
    (NHL_TEXT, ("Blue Jackets +0.5",)),
    (AHL_TEXT.replace("Crunch -0.5", "Crunch ML"), ("Americans -0.5", "Crunch ML")),
])
def test_prepare_reads_half_point_spreads_as_the_winner_where_no_draw_is_possible(text, winner_excerpts):
    rows = OPS.contracts_for(OPS.parse_message(text))
    winner = [r for r in rows if r["family"] == "WINNER"]
    assert [(r["label"], r["side"], r["line"]) for r in winner] == [("L1", "HOME", ""), ("L1", "AWAY", "")]
    assert winner[0]["request_excerpt"] in winner_excerpts
    assert not [r for r in rows if r["family"] == "HANDICAP"]
    assert {r["label"] for r in rows} == {"L1", "L2"}


def test_prepare_reads_two_different_spreads_as_two_contracts():
    # Owner, 22 Nov 2026: "Aktobe +4.5" and "Torpedo -3.5" were asked for on purpose.
    text = ("Upcoming Ice Hockey Game: Torpedo @ Aktobe, Jastar Hokei Ligasy 2026-27,\n"
            "Estimated Game Time Start: 22 November 2026, 7:00 PM AEDT\n\nAktobe +4.5\nTorpedo -3.5\n"
            "Combined Total: Over/Under 7.5 Goals\n")
    rows = OPS.contracts_for(OPS.parse_message(text))
    assert [(r["label"], r["family"], r["side"], r["line"], r["request_excerpt"]) for r in rows if r["family"] == "HANDICAP"] == [
        ("L1", "HANDICAP", "HOME", "4.5", "Aktobe +4.5"), ("L1", "HANDICAP", "AWAY", "-4.5", "Aktobe +4.5"),
        ("L2", "HANDICAP", "HOME", "3.5", "Torpedo -3.5"), ("L2", "HANDICAP", "AWAY", "-3.5", "Torpedo -3.5")]
    assert [r["label"] for r in rows if r["family"] == "TOTAL"] == ["L3", "L3"]
    # Both sides of one line written out ("A -3.5", "B +3.5") stay one contract.
    one = OPS.contracts_for(OPS.parse_message(text.replace("Aktobe +4.5\nTorpedo -3.5", "Aktobe +3.5\nTorpedo -3.5")))
    assert [r["label"] for r in one if r["family"] == "HANDICAP"] == ["L1", "L1"]


def test_prepare_keeps_a_real_puck_line_as_a_handicap():
    rows = OPS.contracts_for(OPS.parse_message(AHL_TEXT.replace("Americans -0.5\nCrunch -0.5", "Americans -1.5")))
    assert [(r["family"], r["side"], r["line"]) for r in rows if r["label"] == "L1"] == [
        ("HANDICAP", "HOME", "1.5"), ("HANDICAP", "AWAY", "-1.5")]


def test_card_reasons_say_how_to_fix_the_source_columns(tmp_path):
    # 20261118DA6D9F6251746B979F5895FA-G0001: prose before the address in source.
    facts = [f"{s},{f},0,Same venue as the last game / https://example.org/t,2026-11-20T05:30:00+00:00"
             for s in ("HOME", "AWAY") for f in M.FACTS]
    O.intake(M.drop(tmp_path, [M.card(facts=facts, not_started_source="NONE_FOUND")]), tmp_path / "in")
    problems = O.read_csv(tmp_path / "in/CARDS.csv")[0]["problems"]
    assert "needs its source page: put only the page's https:// address in source, with no other words" in problems
    assert "write MISSING as the value and the reason in source" in problems
    assert "without such a page the card has no pre-start proof" in problems


def test_card_and_registration_share_one_line_rule():
    rows = [dict(label="L1", family="HANDICAP", side="AWAY", line="+0.5")]
    assert F.line_shape_problems(rows, "PICKS L1: ")[0].startswith("PICKS L1: both sides of the line are required")
    winner = [dict(label="L1", family="WINNER", side=s, line="ML") for s in ("HOME", "AWAY")]
    assert "leave line empty" in F.line_shape_problems(winner, "x: ")[0]
    assert Path(O.__file__).read_text(encoding="utf-8").count("F.line_shape_problems(") == 1
