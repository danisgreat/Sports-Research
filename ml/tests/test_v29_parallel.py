"""v29.0: several chats with up to ten games each, from the owner's messages to a score that cannot be stalled."""
import re
from pathlib import Path

import pytest

from ml import one_chat as O
from ml import one_chat_ops as OPS
from ml.tests import test_one_chat as M

repo = M.repo
ROOT = Path(__file__).resolve().parents[2]

MESSAGES = """Upcoming Basketball Game: Melbourne United vs Sydney Kings, NBL,
Estimated Game Time Start: 20 November 2026, 7:30 PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Melbourne United
Schedule: https://example.org/nbl/schedule

Melbourne United Spread −4.5
Sydney Kings Spread +4.5
Combined Total: Over/Under 178.5 Points

Rank: supplied lines only

Upcoming Basketball Game: Perth Wildcats vs Cairns Taipans, NBL,
Estimated Game Time Start: 20 November 2026, 8:00 PM AEDT (can be delayed so continue the process as normal)
Home side / venue: Cairns Taipans
Schedule: https://example.org/nbl/schedule

Perth Wildcats Spread +2.5
Combined Total: Over/Under 181.5 Points
"""


def prepared(tmp_path, text=MESSAGES, **kw):
    msg = tmp_path / "messages.txt"
    msg.write_text(text, encoding="utf-8")
    out = tmp_path / "prep"
    summary = OPS.prepare(msg, "MINI7", out, **kw)
    return summary, out


def fill(skeleton, *, fact_value="10"):
    """What a chat does: fill every FILL and ? field without touching the fixed values."""
    times = dict(request_at="2026-11-20T05:00:00+00:00", research_start_at="2026-11-20T05:05:00+00:00",
                 research_end_at="2026-11-20T06:30:00+00:00", not_started_source="https://example.org/fixture",
                 not_started_observed_at="2026-11-20T06:25:00+00:00")
    out, seen = [], {}
    for line in skeleton.splitlines():
        key = line.split(":", 1)[0]
        if key in times and line.endswith("FILL"):
            line = f"{key}: {times[key]}"
        elif line.endswith(",P?,,CENTRE?,BASIS?,RESULT_URL?"):
            label = line.split(",")[0]
            p = "0.6" if label not in seen else "0.4"
            seen[label] = True
            line = line.replace("P?,,CENTRE?,BASIS?,RESULT_URL?", f"{p},,,NONE,https://example.org/result")
        elif line.endswith(",VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?"):
            line = line.replace("VALUE_OR_MISSING?,SOURCE_URL_OR_REASON?,OBSERVED_AT?",
                                f"{fact_value},https://example.org/stats,2026-11-20T05:30:00+00:00")
        out.append(line)
    return "\n".join(out) + "\n"


def skeletons(out):
    return {p.parent.name: p.read_text(encoding="utf-8") for p in sorted(out.glob("MINI7-G*/SKELETON.md"))}


# ------------------------------------------------------------------------------------------------------- drafting

def test_prepare_reads_the_owners_messages_into_requests_contracts_and_skeletons(tmp_path):
    summary, out = prepared(tmp_path)
    assert summary == dict(prepared=2, refused=0, out=str(out))
    first = O.read_csv(out / "MINI7-G0001/CONTRACTS.csv")
    assert [(r["label"], r["family"], r["side"], r["line"]) for r in first] == [
        ("L1", "HANDICAP", "HOME", "-4.5"), ("L1", "HANDICAP", "AWAY", "4.5"), ("L2", "TOTAL", "OVER", "178.5"), ("L2", "TOTAL", "UNDER", "178.5")]
    second = O.read_csv(out / "MINI7-G0002/CONTRACTS.csv")      # Perth +2.5 away at Cairns: home line -2.5
    assert [(r["side"], r["line"]) for r in second if r["family"] == "HANDICAP"] == [("HOME", "-2.5"), ("AWAY", "2.5")]
    event = O.read_csv(out / "MINI7-G0002/EVENT.csv")[0]
    assert (event["home"], event["away"], event["scheduled_start"]) == ("Cairns Taipans", "Perth Wildcats", "2026-11-20T20:00:00+11:00")
    assert event["event_id"].startswith("REQ:basketball:nbl:cairns-taipans:perth-wildcats:")
    assert (out / "MINI7-G0001/REQUEST.txt").read_text(encoding="utf-8").startswith("Upcoming Basketball Game: Melbourne United")
    packet = (out / "CHAT_PACKET.md").read_text(encoding="utf-8")
    assert packet.index("MINI7-G0001") < packet.index("MINI7-G0002") and "ONE_CHAT_BRIEF_v29.0.md" in packet
    key, _, meta, picks, facts, problems, _ = O.card_blocks(fill(skeletons(out)["MINI7-G0001"]))[0]
    assert key == "MINI7-G0001" and problems == [] and len(facts) == 2 * len(O.required_facts("Basketball"))


@pytest.mark.parametrize("text,needle", [
    (MESSAGES.replace("Schedule: https://example.org/nbl/schedule\n", "", 1), "no official schedule page"),
    (MESSAGES.replace("Sydney Kings Spread +4.5", "Sydney Kings ML"), "same way"),
    (MESSAGES.replace("Sydney Kings Spread +4.5", "Sydney Kings Spread +5.5"), "equal and opposite"),
    (MESSAGES.replace("Melbourne United Spread", "Melbourne Utd Spread"), "neither"),
    (MESSAGES.replace("Upcoming Basketball Game: Melbourne", "Upcoming Darts Game: Melbourne"), "no request format"),
    (MESSAGES.replace("20 November 2026, 7:30 PM AEDT", "next Friday evening"), "Estimated Game Time Start"),
])
def test_a_message_that_cannot_be_read_exactly_is_refused_with_the_reason(tmp_path, text, needle):
    summary, out = prepared(tmp_path, text)
    report = O.read_csv(out / "PREPARE_REPORT.csv")
    assert summary["refused"] >= 1 and any(r["status"] == "REFUSED" and needle in r["detail"] for r in report)


def test_soccer_cricket_and_tennis_formats(tmp_path):
    text = """Upcoming Soccer/Football Game: Kashiwa Reysol vs Kawasaki Frontale, J1 League,
Estimated Game Time Start: Sat 21 November 2026, 3:00 PM AEDT
Home side / venue: Kashiwa Reysol
Schedule: https://example.org/j1

Combined First Half Goals: Over/Under 0.5 Goals;
Combined Total Goals: Over/Under 2.5 Goals;
Combined Total Corners: Over/Under 10.5 Corners;

Upcoming Cricket Game: Perth Scorchers Women vs Adelaide Strikers Women, WBBL, Format: T20,
Estimated Game Time Start: 22 November 2026, 7:10 PM AEDT
Home side / venue: Perth Scorchers Women
Team A bats: not known
Schedule: https://example.org/wbbl

Adelaide Strikers Women 1st Innings Runs at end of 20 overs (T20) Total: Over/Under 150.5 Runs
Adelaide Strikers Women 1st Innings Runs at the end of over 6 (T20): Over/Under 41.5 Runs

Upcoming Tennis Match: Marvin Moeller vs Jonas Forejtek, ATP Challenger Monastir 2026, R16, Hard, Best of 3,
Estimated Game Time Start: 20 November 2026, 9:00 PM AEDT
Schedule: https://example.org/atp

Marvin Moeller Handicap Games -2.5
Jonas Forejtek Handicap Games +2.5
Combined Total: Over/Under 22.5 Games
"""
    summary, out = prepared(tmp_path, text)
    assert summary["prepared"] == 3
    fam = lambda key: [(r["label"], r["family"], r["line"]) for r in O.read_csv(out / key / "CONTRACTS.csv")][::2]
    assert fam("MINI7-G0001") == [("L1", "PERIOD", "0.5"), ("L2", "TOTAL", "2.5"), ("L3", "CORNERS", "10.5")]
    assert fam("MINI7-G0002") == [("L1", "TEAM_TOTAL", "150.5"), ("L2", "PERIOD", "41.5")]
    assert fam("MINI7-G0003") == [("L1", "HANDICAP", "-2.5"), ("L2", "TOTAL", "22.5")]


# --------------------------------------------------------------------------- registering, sealing a growing mini

def register(repo, out):
    result = OPS.register_folder(out, repo)
    M.Server("2026-11-20T04:30:00Z")(repo)
    return result


def test_a_growing_mini_is_sealed_card_by_card_and_scored_from_the_sealed_copies(repo, tmp_path):
    _, out = prepared(tmp_path)
    assert register(repo, out)["registered"] == 2
    sk = skeletons(out)
    minis = tmp_path / "minis"
    minis.mkdir()
    mini = minis / "MINI7.md"
    # After game 1: the chat has finished card 1; card 2 is still an unfilled skeleton.
    mini.write_text(fill(sk["MINI7-G0001"]) + "\n" + sk["MINI7-G0002"], encoding="utf-8")
    first = O.seal([mini], repo, lookup=M.Server("2026-11-20T07:00:00Z"), wait=(0,))
    assert first["sealed"] == 1 and first["cards"] == "MINI7-G0001"
    assert [r["card_key"] for r in first["refused"]] == ["MINI7-G0002"] and "incomplete" in first["refused"][0]["reason"]
    # Later the chat re-emits the whole mini, reformatting card 1, and adds card 2.
    mini.write_text(fill(sk["MINI7-G0001"], fact_value="10.0") + "\n" + fill(sk["MINI7-G0002"]), encoding="utf-8")
    second = OPS.watch(minis, once=True, root=repo, lookup=M.Server("2026-11-20T07:10:00Z"), log=lambda *a: None)[0]
    assert second["sealed"] == 1 and second["cards"] == "MINI7-G0002"
    assert [r["card_key"] for r in second["refused"]] == ["MINI7-G0001"] and "already sealed" in second["refused"][0]["reason"]
    intake = repo / "research/one_chat/intake/from-seals"
    OPS.intake_from_seals(intake, repo)
    facts = [r["value"] for r in O.read_csv(intake / "FACTS.csv") if r["card_key"] == "MINI7-G0001"]
    assert set(facts) == {"10"}                                       # the first sealed version, not the later copy
    outcomes = M.outcomes(repo, tmp_path / "cap", ["MINI7-G0001", "MINI7-G0002"], start="2026-11-20T08:20:00+00:00")
    M.commit_all(repo)
    s = M.run(repo, tmp_path, [intake], [outcomes], "s1", as_of="2026-11-21T00:00:00+00:00")
    assert (s["custody_problems"], s["games_in_sequence"], s["sealed_pre_start_server"]) == (0, 2, 2)


def test_a_seal_retries_when_another_chat_published_first(repo, tmp_path, monkeypatch):
    _, out = prepared(tmp_path)
    register(repo, out)
    card = tmp_path / "card.md"
    card.write_text(fill(skeletons(out)["MINI7-G0001"]), encoding="utf-8")
    real, calls = O.publish_seal_tree, []

    def racing(root, payload, push=True):
        calls.append(1)
        if len(calls) == 1:
            raise O.OneChatError("seal push refused; no force or main push attempted: non-fast-forward")
        return real(root, payload, push)

    monkeypatch.setattr(O, "publish_seal_tree", racing)
    result = O.seal([card], repo, lookup=M.Server("2026-11-20T07:00:00Z"), wait=(0,), pause=0)
    assert result["sealed"] == 1 and len(calls) == 2


# ------------------------------------------------------------------------------------------- settlement deadline

def sealed_pair(repo, tmp_path):
    _, out = prepared(tmp_path)
    register(repo, out)
    sk = skeletons(out)
    files = []
    for key in ("MINI7-G0001", "MINI7-G0002"):
        f = tmp_path / f"{key}.md"
        f.write_text(fill(sk[key]), encoding="utf-8")
        files.append(f)
    assert O.seal(files, repo, lookup=M.Server("2026-11-20T07:00:00Z"), wait=(0,))["sealed"] == 2
    intake = repo / "research/one_chat/intake/pair"
    OPS.intake_from_seals(intake, repo)
    return intake


def test_an_unsettled_game_holds_back_until_its_deadline_then_is_dropped_by_rule(repo, tmp_path):
    intake = sealed_pair(repo, tmp_path)
    settled = M.outcomes(repo, tmp_path / "cap", ["MINI7-G0002"], start="2026-11-20T08:50:00+00:00")
    open_ = M.outcomes(repo, tmp_path / "cap", ["MINI7-G0001"], grade="UNRESOLVED", name="OPEN.csv")
    M.commit_all(repo)
    before = M.run(repo, tmp_path, [intake], [settled, open_], "before", as_of="2026-11-25T00:00:00+00:00")
    assert before["games_in_sequence"] == 0 and before["games_held_back_by_unsettled_earlier_game"] == 1
    after = M.run(repo, tmp_path, [intake], [settled, open_], "after", as_of="2026-12-05T00:00:00+00:00")
    assert after["games_in_sequence"] == 1 and after["games_held_back_by_unsettled_earlier_game"] == 0
    assert after["games_settlement_unattainable"] == 1 and after["custody_problems"] == 0
    assert after["worst_case_verdict"] == "NOT_YET_DEMONSTRATED" and after["worst_case_e_value"] <= after["e_value"]


def test_after_the_deadline_a_partly_settled_game_is_scored_on_its_settled_lines(repo, tmp_path):
    intake = sealed_pair(repo, tmp_path)
    path = M.outcomes(repo, tmp_path / "cap", ["MINI7-G0001", "MINI7-G0002"], start="2026-11-20T08:20:00+00:00")
    rows = O.read_csv(path)
    for r in rows:
        if r["card_key"] == "MINI7-G0001" and r["label"] == "L2":
            r["grade"] = "UNRESOLVED"
    path.write_bytes(O.csv_bytes(O.OUTCOME_FIELDS, rows))
    M.commit_all(repo)
    s = M.run(repo, tmp_path, [intake], [path], "partial", as_of="2026-12-05T00:00:00+00:00")
    cover = {c["card_key"]: c for c in O.read_csv(repo / O.SCORES / "partial/COVERAGE.csv")}
    assert s["games_in_sequence"] == 2 and s["games_scored_after_dropping_rows"] == 1
    assert cover["MINI7-G0001"]["dropped_rows"] == "2" and cover["MINI7-G0001"]["eligible"] == "Y"


# ------------------------------------------------------------------------------------------------- templates

def test_committed_templates_are_the_generated_templates(tmp_path):
    OPS.write_templates(tmp_path)
    committed = ROOT / "research/external/templates"
    for f in sorted(tmp_path.glob("*.md")):
        assert (committed / f.name).read_text(encoding="utf-8") == f.read_text(encoding="utf-8"), f.name
    assert len(list(tmp_path.glob("*.md"))) == len(O.SUPPORTED_SPORTS)
    text = (committed / "ONECHAT_V1_BASKETBALL_v29.0.md").read_text(encoding="utf-8")
    assert all(re.search(rf"^HOME,{f},", text, re.M) for f in O.required_facts("Basketball"))
