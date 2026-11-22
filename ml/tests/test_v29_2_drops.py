"""v29.2 drops: a draft can be checked exactly as a seal would check it, a refused card can be fixed before first
play, and each seal reports how far before the scheduled start the server published it."""

from ml import drop_seal as D
from ml import forecast_integrity as F
from ml import one_chat as O
from ml.tests import test_drop_seal as DS
from ml.tests import test_one_chat as M

repo = M.repo
PROSE = [f"{s},{f},10,Same venue as the last game / https://example.org/t,2026-11-20T05:30:00+00:00"
         for s in ("HOME", "AWAY") for f in M.FACTS]


def registered(repo):
    text = M.card()
    key, files = DS.request_files(text)
    D.process(repo, *DS.push_drop(repo, DS.request_drop(key, files)))
    M.Server("2026-11-20T04:30:00Z")(repo)
    return key, text


def sealed_keys(repo):
    return [r["card_key"] for r in F.rows(DS.seal_branch(repo, O.SEALS))]


def test_a_check_drop_reports_the_seal_verdict_and_never_publishes(repo):
    key, text = registered(repo)
    bad = M.card(facts=PROSE).encode()
    out = D.process(repo, *DS.push_drop(repo, {"drops/check/draft.md": bad}), lookup=M.Server("2026-11-20T06:40:00Z"), wait=(0,))
    assert [(r["kind"], r["card_key"], r["status"]) for r in out] == [("check", key, "CHECK_FAILED")]
    assert "would NOT be sealed" in out[0]["detail"] and "with no other words" in out[0]["detail"]
    out = D.process(repo, *DS.push_drop(repo, {"drops/check/draft.md": text.encode()}),
                    lookup=M.Server("2026-11-20T06:45:00Z"), wait=(0,))
    assert [r["status"] for r in out] == ["CHECK_PASSED"] and "push it to drops/cards/" in out[0]["detail"]
    assert sealed_keys(repo) == []                       # a check never seals


def test_a_refused_card_can_be_fixed_before_first_play_and_the_seal_reports_its_margin(repo):
    key, text = registered(repo)
    out = D.process(repo, *DS.push_drop(repo, {"drops/cards/first.md": M.card(facts=PROSE).encode()}),
                    lookup=M.Server("2026-11-20T06:40:00Z"), wait=(0,))
    assert [r["status"] for r in out] == ["FAILED"] and sealed_keys(repo) == []
    out = D.process(repo, *DS.push_drop(repo, {"drops/cards/fixed.md": text.encode()}),
                    lookup=M.Server("2026-11-20T07:00:00Z"), wait=(0,))
    assert [r["status"] for r in out] == ["SEALED"] and sealed_keys(repo) == [key]
    assert "60 min before the scheduled start" in out[0]["detail"]


def test_the_margin_says_when_a_seal_came_after_the_scheduled_start():
    assert D._margin("2026-11-20T11:15:24Z", "2026-11-20T22:10:00+11:00").startswith("5 min after the scheduled start; normal for a late start")
    assert D._margin("2026-11-21T00:28:31Z", "2026-11-21T11:30:00+11:00") == "1 min before the scheduled start"
    assert D._margin("", "2026-11-21T11:30:00+11:00") == ""


def test_a_long_refusal_reason_is_kept_in_full(repo):
    # 20261120-…-G0006's reason was cut off at 300 characters ("…may lea").
    key, text = registered(repo)
    out = D.process(repo, *DS.push_drop(repo, {"drops/cards/first.md": M.card(facts=PROSE).encode()}),
                    lookup=M.Server("2026-11-20T06:40:00Z"), wait=(0,))
    assert out[0]["detail"].count("with no other words") == 2 * len(M.FACTS)
