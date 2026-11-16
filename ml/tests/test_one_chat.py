"""ONE-CHAT-v2: cards parsed as written, sealed before play, scored only from committed and hash-checked inputs, and
judged by an anytime-valid test. Includes a reproduction of every defect found in the v25.0 review."""
import os
import random
import shutil
import subprocess

import pytest

from ml import one_chat as O

FACTS = O.required_facts("Basketball")
START = "2026-11-20T08:00:00+00:00"
R = "https://example.org/result/1"
DEFAULT = [f"L1,HANDICAP,HOME,-3.5,0.47,,2.1,NONE,{R}", f"L1,HANDICAP,AWAY,3.5,0.53,,-2.1,NONE,{R}",
           f"L2,TOTAL,OVER,158.5,0.62,,160.2,NONE,{R}", f"L2,TOTAL,UNDER,158.5,0.38,,160.2,NONE,{R}"]


def card(key="CHAT1-G0001", home="Alpha", away="Beta", picks=None, facts=None, start=START, **header):
    meta = dict(format="ONECHAT_V1", card_key=key, sport="Basketball", competition="Example League", home=home, away=away,
                scheduled_start=start, request_at="2026-11-20T05:00:00+00:00", research_start_at="2026-11-20T05:05:00+00:00",
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
        os.utime(f, (1795075200 + i, 1795075200 + i))
    return d


# ------------------------------------------------------------------------------------------------------------- intake

def test_a_complete_card_is_admitted_ranked_flagged_and_manifested_without_changing_a_number(tmp_path):
    d = drop(tmp_path, [card(), "# notes only\n"])
    s = O.intake(d, tmp_path / "in")
    assert (s["ADMITTED"], s["NO_BLOCK"], s["supplied_lines"], s["priced_lines"]) == (1, 1, 2, 2)
    rows = {(r["label"], r["side"]): r for r in O.read_csv(tmp_path / "in/PICKS.csv")}
    assert rows[("L2", "OVER")]["rank"] == "1" and rows[("L1", "AWAY")]["rank"] == "2" and rows[("L1", "HOME")]["rank"] == ""
    assert rows[("L1", "AWAY")]["flags"] == "NO_DIRECTION;PLUS_HANDICAP" and rows[("L2", "OVER")]["flags"] == ""
    assert [r["p"] for r in rows.values()] == ["0.47", "0.53", "0.62", "0.38"]
    assert O.verify_intake(tmp_path / "in", tmp_path, require_committed=False) == []
    assert O.read_csv(tmp_path / "in/CARDS.csv")[0]["facts_last_observed_at"] == "2026-11-20T05:30:00+00:00"
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
    # review defect 4: facts read after the research ended, and a not-started check before the research began
    (dict(facts=[f"{s},{f},10,https://example.org/t,2026-11-20T07:45:00+00:00" for s in ("HOME", "AWAY") for f in FACTS]), "observed_at must fall within"),
    (dict(not_started_observed_at="2026-11-20T05:00:00+00:00"), "not-started observation must be made during"),
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


def test_one_game_one_card_within_a_drop_and_a_repeated_snapshot_is_taken_once(tmp_path):
    s = O.intake(drop(tmp_path, [card(), card(), card(key="CHAT2-G0001")]), tmp_path / "in")
    assert (s["ADMITTED"], s["DUPLICATE_GAME"]) == (1, 1)


# ------------------------------------------------------------------------------------------- repository and custody

def git(root, *args):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, check=True).stdout.strip()


@pytest.fixture()
def repo(tmp_path):
    origin = tmp_path / "origin.git"
    subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(origin)], check=True)
    root = tmp_path / "repo"
    subprocess.run(["git", "init", "-q", "-b", "main", str(root)], check=True)
    git(root, "config", "user.email", "example@example.org")
    git(root, "config", "user.name", "Example")
    git(root, "config", "core.autocrlf", "false")
    (root / "README.md").write_text("example\n", encoding="utf-8")
    git(root, "add", "README.md")
    git(root, "commit", "-q", "-m", "start")
    git(root, "remote", "add", "origin", str(origin))
    git(root, "push", "-q", "origin", "main")
    return root


class Server:
    """Stands in for GitHub's push record: every push of main is timed at a clock the test controls."""
    def __init__(self, at):
        self.at, self.seen = at, []

    def __call__(self, root):
        head = git(root, "rev-parse", "refs/remotes/origin/main")
        if not any(r["after"] == head for r in self.seen):
            self.seen.append(dict(before="", after=head, pushed_at_server=self.at, ref="refs/heads/main"))
        return list(self.seen)


def seal(repo, files, at="2026-11-20T07:00:00Z"):
    return O.seal(files, repo, lookup=Server(at), wait=(0,))


def commit_all(repo, message="records"):
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", message)


def outcomes(repo, captures, keys, *, over=lambda n: True, start=START, name="OUTCOMES.csv", event=lambda n, k: f"EVT-{k}",
             grade=None, fake_hash=False, total_line=None):
    captures.mkdir(exist_ok=True)
    rows = []
    for n, key in enumerate(keys):
        page = captures / f"{key}.html"
        page.write_text(f"final for {key}", encoding="utf-8")
        digest = "f" * 64 if fake_hash else O.sha(page.read_bytes())
        if fake_hash:
            page.unlink()
        for label, side, won in (("L1", "HOME", False), ("L1", "AWAY", True), ("L2", "OVER", over(n)), ("L2", "UNDER", not over(n))):
            rows.append(dict(card_key=key, label=label, side=side, grade=grade or ("WIN" if won else "LOSS"), event_id=event(n, key),
                             actual_start=start, settled_at=f"2026-11-20T{11 + n // 60:02d}:{n % 60:02d}:00+00:00",
                             final_source=R, final_capture_sha256=digest, final_capture_path=page.name))
    path = repo / "research" / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(O.csv_bytes(O.OUTCOME_FIELDS, rows))
    return path


def build(repo, tmp_path, cards, *, at="2026-11-20T07:00:00Z", sealed=True, name="in1"):
    d = drop(tmp_path, cards, name="drop-" + name)
    if sealed:
        seal(repo, sorted(d.glob("*.md")), at)
    O.intake(d, repo / "research/one_chat/intake" / name, repo)
    return repo / "research/one_chat/intake" / name


def many(n, start_day=20):
    return [card(key=f"CHAT1-G{i:04d}", home=f"Home {i}", away=f"Away {i}",
                 start=f"2026-11-{start_day:02d}T{8 + i // 60:02d}:{i % 60:02d}:00+00:00") for i in range(1, n + 1)]


def run(repo, tmp_path, intakes, outs, name, **kw):
    return O.score(intakes, outs, repo / "research/one_chat/scores" / name, root=repo, captures=tmp_path / "cap", **kw)


def test_a_sealed_skilled_sequence_is_demonstrated_and_the_first_hundred_freeze_once(repo, tmp_path):
    folder = build(repo, tmp_path, many(105))
    keys = [f"CHAT1-G{i:04d}" for i in range(1, 106)]
    path = outcomes(repo, tmp_path / "cap", keys, over=lambda n: n % 5 != 0)
    commit_all(repo)
    s = run(repo, tmp_path, [folder], [path], "s1")
    assert s["custody_problems"] == 0 and s["sealed_pre_start_server"] == 105 and s["games_in_sequence"] == 105
    assert s["advantage"] == "DEMONSTRATED" and 0 < s["crossed_at_game"] <= 105 and s["lower_bound_95"] > 0
    assert s["cohort_status"] == "COHORT_FROZEN_NOW" and s["cohort_finding"] == "MEETS_REGISTERED_CRITERION"
    out = repo / "research/one_chat/scores/s1"
    assert len(O.read_csv(out / "COHORT.csv")) == 100 and O.read_csv(out / "SEQUENCE.csv")[0]["card_key"] == "CHAT1-G0001"
    commit_all(repo, "scores")
    with pytest.raises(O.OneChatError, match="already frozen"):
        run(repo, tmp_path, [folder], [path], "s2")
    again = run(repo, tmp_path, [folder], [path], "s3", cohort=out / "COHORT.csv")
    assert again["cohort_status"] == "FROZEN_COHORT_REUSED" and again["advantage"] == "DEMONSTRATED"


def test_a_coin_flip_card_is_not_demonstrated(repo, tmp_path):
    folder = build(repo, tmp_path, many(60))
    keys = [f"CHAT1-G{i:04d}" for i in range(1, 61)]
    path = outcomes(repo, tmp_path / "cap", keys, over=lambda n: n % 2 == 0)
    commit_all(repo)
    s = run(repo, tmp_path, [folder], [path], "s1")
    assert s["advantage"] == "NOT_YET_DEMONSTRATED" and s["cohort_status"] == "COHORT_NOT_YET_FULL"


def test_review_defect_1_one_game_in_a_hundred_intakes_counts_once(repo, tmp_path):
    pairs, files = [], []
    for i in range(1, 101):                      # the same game, a new card key and a new intake each time
        d = drop(tmp_path, [card(key=f"CHAT{i}-G0001")], name=f"drop{i:03d}")
        files += sorted(d.glob("*.md"))
        pairs.append((d, repo / "research/one_chat/intake" / f"in{i:03d}"))
    seal(repo, files)
    for d, out in pairs:
        O.intake(d, out, repo)
    folders = [out for _, out in pairs]
    keys = [f"CHAT{i}-G0001" for i in range(1, 101)]
    path = outcomes(repo, tmp_path / "cap", keys, event=lambda n, k: "EVT-ONE-GAME")
    commit_all(repo)
    s = run(repo, tmp_path, folders, [path], "s1")
    assert s["games_in_sequence"] == 1 and s["duplicate_cards"] == 99
    assert s["advantage"] == "NOT_YET_DEMONSTRATED" and s["cohort_status"] == "COHORT_NOT_YET_FULL"


def test_review_defect_1b_respelled_teams_are_one_game_when_the_settled_event_is_one(repo, tmp_path):
    cards = [card(key=f"CHAT{i}-G0001", home="Alpha" + " FC" * i, away="Beta") for i in range(1, 6)]
    folder = build(repo, tmp_path, cards)
    path = outcomes(repo, tmp_path / "cap", [f"CHAT{i}-G0001" for i in range(1, 6)], event=lambda n, k: "EVT-SAME")
    commit_all(repo)
    s = run(repo, tmp_path, [folder], [path], "s1")
    assert s["games_in_sequence"] == 1 and s["duplicate_cards"] == 4


def test_review_defect_2_a_supplied_cohort_must_be_the_frozen_hundred(repo, tmp_path):
    folder = build(repo, tmp_path, many(3))
    path = outcomes(repo, tmp_path / "cap", ["CHAT1-G0001", "CHAT1-G0002", "CHAT1-G0003"])
    commit_all(repo)
    fake = repo / "research/one_chat/scores/fake"
    fake.mkdir(parents=True)
    rows = [dict(card_key=k, game_id=c["game_id"], scheduled_start="", settled_at="") for k, c in
            ((c["card_key"], c) for c in O.read_csv(folder / "CARDS.csv"))][:2]
    data = O.csv_bytes(("card_key", "game_id", "scheduled_start", "settled_at"), rows)
    (fake / "COHORT.csv").write_bytes(data)
    (fake / "COHORT_RECEIPT.csv").write_bytes(O.csv_bytes(("cohort_sha256", "games", "frozen_at", "rule"),
                                                          [dict(cohort_sha256=O.sha(data), games=100, frozen_at="x", rule="x")]))
    with pytest.raises(O.OneChatError, match="exactly 100 distinct games"):
        run(repo, tmp_path, [folder], [path], "s1", cohort=fake / "COHORT.csv")
    (fake / "COHORT_RECEIPT.csv").write_bytes(O.csv_bytes(("cohort_sha256", "games", "frozen_at", "rule"),
                                                          [dict(cohort_sha256="0" * 64, games=100, frozen_at="x", rule="x")]))
    with pytest.raises(O.OneChatError, match="does not match its COHORT_RECEIPT"):
        run(repo, tmp_path, [folder], [path], "s2", cohort=fake / "COHORT.csv")


def test_review_defect_3_edited_intakes_uncommitted_outcomes_and_invented_captures_are_refused(repo, tmp_path):
    folder = build(repo, tmp_path, many(3))
    path = outcomes(repo, tmp_path / "cap", ["CHAT1-G0001", "CHAT1-G0002", "CHAT1-G0003"])
    commit_all(repo)
    picks = folder / "PICKS.csv"
    picks.write_bytes(picks.read_bytes().replace(b"0.62", b"0.92"))       # change a stated probability after intake
    s = run(repo, tmp_path, [folder], [path], "s1")
    assert s["advantage"] == "NOT_ASSESSABLE" and s["custody_problems"] >= 1
    problems = {r["problem"] for r in O.read_csv(repo / "research/one_chat/scores/s1/CUSTODY_PROBLEMS.csv")}
    assert any("PICKS.csv: bytes differ from MANIFEST.csv" in p for p in problems)
    git(repo, "checkout", "--", str(picks.relative_to(repo)))
    path.write_bytes(path.read_bytes() + b"")
    with open(path, "ab") as fh:
        fh.write(b"")
    later = outcomes(repo, tmp_path / "cap2", ["CHAT1-G0001"], name="LATER.csv")    # written but never committed
    s = run(repo, tmp_path, [folder], [later], "s2")
    assert s["advantage"] == "NOT_ASSESSABLE"
    fake = outcomes(repo, tmp_path / "cap3", ["CHAT1-G0001"], name="FAKE.csv", fake_hash=True)
    with pytest.raises(O.OneChatError, match="missing or its SHA-256 differs"):
        O.score([folder], [fake], repo / "research/one_chat/scores/s3", root=repo, captures=tmp_path / "cap3")


def test_review_defect_5_whole_number_lines_are_scored_on_the_probability_given_no_push(repo, tmp_path):
    whole = [f"L1,HANDICAP,HOME,-3.5,0.47,,,NONE,{R}", f"L1,HANDICAP,AWAY,3.5,0.53,,,NONE,{R}",
             f"L2,TOTAL,OVER,160,0.45,,,NONE,{R}", f"L2,TOTAL,UNDER,160,0.45,,,NONE,{R}"]
    folder = build(repo, tmp_path, [card(picks=whole)])
    path = outcomes(repo, tmp_path / "cap", ["CHAT1-G0001"])
    commit_all(repo)
    run(repo, tmp_path, [folder], [path], "s1")
    seq = O.read_csv(repo / "research/one_chat/scores/s1/SEQUENCE.csv")
    # L1: (0.53-1)^2 twice; L2 given no push: 0.5 each side -> 0.25 twice; d = 0.25 - mean(0.2209, 0.2209, 0.25, 0.25)
    assert float(seq[0]["d"]) == pytest.approx(0.25 - (0.2209 * 2 + 0.25 * 2) / 4)


def test_unsealed_late_sealed_client_timed_post_start_and_exposed_cards_never_enter_the_sequence(repo, tmp_path, monkeypatch):
    good = build(repo, tmp_path, [card(key="K1-G0001", home="A1", away="B1")], name="good")
    unsealed = build(repo, tmp_path, [card(key="K2-G0001", home="A2", away="B2")], sealed=False, name="unsealed")
    late = build(repo, tmp_path, [card(key="K3-G0001", home="A3", away="B3")], at="2026-11-20T09:00:00Z", name="late")
    # GitHub's push times only move forward, so later seals carry later server times.
    exposed = build(repo, tmp_path, [card(key="K5-G0001", home="A5", away="B5", outcome_exposure="saw the first quarter")],
                    at="2026-11-20T09:05:00Z", name="exposed")
    post = build(repo, tmp_path, [card(key="K6-G0001", home="A6", away="B6")], at="2026-11-20T09:10:00Z", name="post")
    # The last push carries a card with no server record at all: only its own (client) commit time is known.
    d = drop(tmp_path, [card(key="K4-G0001", home="A4", away="B4")], name="drop-client")
    monkeypatch.setenv("GIT_COMMITTER_DATE", "2026-11-20T07:30:00+00:00")
    O.seal(sorted(d.glob("*.md")), repo, push=False)
    monkeypatch.delenv("GIT_COMMITTER_DATE")
    git(repo, "push", "-q", "origin", "main")
    client = repo / "research/one_chat/intake/client"
    O.intake(d, client, repo)
    keys = ["K1-G0001", "K2-G0001", "K3-G0001", "K4-G0001", "K5-G0001"]
    path = outcomes(repo, tmp_path / "cap", keys)
    early = outcomes(repo, tmp_path / "cap", ["K6-G0001"], start="2026-11-20T06:00:00+00:00", name="EARLY.csv")
    commit_all(repo)
    s = run(repo, tmp_path, [good, unsealed, late, client, exposed, post], [path, early], "s1")
    cover = {c["card_key"]: c for c in O.read_csv(repo / "research/one_chat/scores/s1/COVERAGE.csv")}
    found = {k: c["exclusion"] for k, c in cover.items()}
    assert s["games_in_sequence"] == 1 and cover["K1-G0001"]["eligible"] == "Y", found
    assert [found[k] for k in keys[1:]] == ["UNSEALED", "SEALED_AFTER_START", "SEALED_PRE_START_CLIENT", "OUTCOME_EXPOSED"], found
    assert found["K6-G0001"] == "POST_START", found        # research ended at 06:30, after the 06:00 first play


def test_an_unsettled_earlier_game_holds_back_later_games_until_it_settles(repo, tmp_path):
    folder = build(repo, tmp_path, many(4))
    path = outcomes(repo, tmp_path / "cap", ["CHAT1-G0001", "CHAT1-G0003", "CHAT1-G0004"])
    commit_all(repo)
    s = run(repo, tmp_path, [folder], [path], "s1")
    assert s["games_in_sequence"] == 1 and s["games_held_back_by_unsettled_earlier_game"] == 2


def test_seal_refuses_an_incomplete_card_and_does_not_reseal_the_same_file(repo, tmp_path):
    d = drop(tmp_path, [card(facts=[])], name="bad")
    with pytest.raises(O.OneChatError, match="not sealed"):
        seal(repo, sorted(d.glob("*.md")))
    assert not (repo / O.SEALED).exists() or not list((repo / O.SEALED).glob("*.md"))
    d2 = drop(tmp_path, [card()], name="good")
    first = seal(repo, sorted(d2.glob("*.md")))
    assert first["sealed"] == 1 and first["pushed"] and first["server_time"] == "2026-11-20T07:00:00Z"
    assert seal(repo, sorted(d2.glob("*.md")))["sealed"] == 0
    assert git(repo, "status", "--porcelain") == ""


# ------------------------------------------------------------------------------------------------- the test itself

def test_the_anytime_test_keeps_its_error_rate_on_a_mean_zero_null():
    rng = random.Random(11)
    alarms = sum(O.advantage([rng.choice((0.15, -0.15)) for _ in range(O.HORIZON)])["verdict"] == "DEMONSTRATED" for _ in range(300))
    assert alarms / 300 <= O.ALPHA


def test_the_anytime_test_has_power_against_a_calibrated_seventy_percent_card():
    rng = random.Random(5)
    def game():
        out = []
        for _ in range(2):
            p = rng.uniform(0.62, 0.78)
            out.append(0.25 - (p - (rng.random() < p)) ** 2)
        return sum(out) / 2
    wins = sum(O.advantage([game() for _ in range(O.HORIZON)])["verdict"] == "DEMONSTRATED" for _ in range(40))
    assert wins >= 36


def test_bets_never_risk_ruin_and_the_lower_bound_is_below_the_mean():
    ds = [-0.75] * 5 + [0.2] * 50
    path = O.e_process(ds)
    assert all(r["e_value"] > 0 for r in path) and all(r["bet"] <= O.BET_CAP / (0 - O.D_LOW) + 1e-12 for r in path)
    a = O.advantage([0.05] * 200)
    assert a["verdict"] == "DEMONSTRATED" and 0 < a["lower_bound_95"] < 0.05


def test_template_lists_the_sports_required_facts():
    text = O.template("Basketball")
    assert all(f"HOME,{f},,," in text for f in FACTS) and O.BLOCK.search(text.replace("<MINI_KEY>", "X"))


def test_push_receipts_are_recorded_once_even_when_the_server_repeats_a_page(repo):
    page = [dict(before="a" * 40, after="b" * 40, pushed_at_server="2026-11-20T07:00:00Z", ref="refs/heads/main")]
    assert O.record_receipts(repo, lambda root: page * 10) == 1
    assert O.record_receipts(repo, lambda root: page * 3) == 0
    assert len(O.read_csv(repo / O.RECEIPTS)) == 1
