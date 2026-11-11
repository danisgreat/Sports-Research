"""Adversarial operational paths: retain uncertainty without inventing evidence or issuance."""
import csv
from pathlib import Path
import subprocess

import pytest

from ml import research_intake as I, research_operations as O, external as X, reference as R, team_strength as T
from ml.tests.test_external_integrity_v2 import event, make_return, put_return, complete, AT, START, URL1, URL2, write


def render(ret, receipt=""):
    text = receipt + "\n<!-- BEGIN LANE_RETURN -->\n" + "\n".join(k + ": " + v for k, v in ret["header"].items()) + "\n\n"
    for name, fields in dict(X.SECTIONS, **X.OPTIONAL_SECTIONS).items():
        text += "[" + name + "]\n" + I.csv_bytes(fields, ret.get(name, [])).decode()
    return text + "<!-- END LANE_RETURN -->\n"


def send(event, text, at=AT):
    p = event["root"] / (I.sha(text.encode()) + ".md"); p.write_text(text, encoding="utf-8")
    return I.intake(event["folder"], p, root=event["root"], at=at)


def upstream(event, lanes=("L1", "L2", "L3", "L4")):
    for lane in lanes: assert put_return(event, lane)["status"] == "ACCEPTED"
    p = event["root"] / "REVIEW.txt"; p.write_text("Reviewed original collectors in EXAMPLE evidence")
    for url, collector in ((URL1, "CLUB"), (URL2, "LEAGUE")):
        I.review_source(event["folder"], url, collector, p, status="VERIFIED", at="2026-11-11T00:41:00+00:00")


def new_mode(event, mode, lanes):
    reqs = I.read(event["folder"] / "REQUIREMENTS.csv", I.REQ_FIELDS)
    reqs = [r for r in reqs if r["lane"] in lanes]
    if "L4" not in lanes:
        for r in reqs: r["corroboration_required"] = "NO"
    if "L6" in lanes:
        reqs.append(dict(lane="L6", requirement_id="L6R", side="HOME", field="window:L5", required="YES", corroboration_required="NO"))
    arts = {r["role"]: r["path"] for r in I.read(event["folder"] / "ARTIFACTS.csv", I.ART_FIELDS)}
    dest = event["root"] / mode
    e = I.initialize(event["e"], event["contracts"], reqs, dest, artifacts=arts, root=event["root"], at="2026-11-10T23:50:00+00:00",
                     mode=mode, lanes=lanes, reason="Late request, explicitly scoped coverage")
    return dict(event, folder=dest, e=e)


def test_unknown_publication_accepts_actual_prestart_retrieval(event):
    ret = X.parse(make_return(event, "L1")); ret["EVIDENCE"][0]["published_at"] = "UNKNOWN"
    assert send(event, render(ret))["status"] == "ACCEPTED"


@pytest.mark.parametrize("field,value", [("retrieved_at", START), ("published_at", "2026-11-11T00:02:00+00:00"), ("retrieved_at", "UNKNOWN")])
def test_unknown_publication_does_not_relax_retrieval_or_publication_chronology(event, field, value):
    ret = X.parse(make_return(event, "L1")); ret["EVIDENCE"][0][field] = value
    assert send(event, render(ret))["status"] == "REFUSED"


def test_reduced_three_lane_mode_is_explicit_and_can_admit(event):
    ev = new_mode(event, "REDUCED", ["L2", "L3", "L5"])
    upstream(ev, ("L2", "L3")); assert put_return(ev, "L5")["status"] == "ACCEPTED"
    result = I.admit(ev["folder"], root=ev["root"], at=AT)
    assert result["research_mode"] == "REDUCED" and result["n_returns"] == 3
    assert result["comparator_status"] == "UNPAIRED_NO_SINGLE"


def test_sixth_lane_is_assigned_dependency_not_a_second_pricer(event):
    ev = new_mode(event, "FULL_SIX", ["L1", "L2", "L3", "L4", "L5", "L6"])
    upstream(ev)
    with pytest.raises(X.ExternalError, match="awaits L6"): I.packet_hash(ev["folder"], "L5")
    ret = X.parse(make_return(ev, "L2")); ret["header"].update(lane="L6", chat_label="CHAT-6", input_package_sha256=I.packet_hash(ev["folder"], "L6"))
    ret["REQUIREMENTS"][0]["requirement_id"] = "L6R"
    assert send(ev, render(ret), at="2026-11-11T00:42:00+00:00")["status"] == "ACCEPTED"
    assert put_return(ev, "L5")["status"] == "ACCEPTED"
    assert I.admit(ev["folder"], root=ev["root"], at=AT)["research_mode"] == "FULL_SIX"


def test_partial_pricing_keeps_unpriceable_line_and_numeric_line(event):
    upstream(event); ret = X.parse(make_return(event, "L5")); removed = ret["PROBABILITIES"].pop()
    ret["UNPRICED"] = [dict(label=removed["label"], status="UNSUPPORTED", reason="EXAMPLE exact period not covered")]
    assert send(event, render(ret, event["receipt"]))["status"] == "ACCEPTED"
    result = I.admit(event["folder"], root=event["root"], at=AT)
    assert result["admission"] == "READY_FOR_CARD" and len(result["unpriced"]) == 1


@pytest.mark.parametrize("change", ["missing", "overlap", "empty_reason", "bad_status"])
def test_partial_pricing_cannot_silently_drop_or_double_count_contracts(event, change):
    upstream(event); ret = X.parse(make_return(event, "L5")); removed = ret["PROBABILITIES"].pop()
    r = dict(label=removed["label"], status="UNSUPPORTED", reason="No exact-scope engine")
    ret["UNPRICED"] = [] if change == "missing" else [r]
    if change == "overlap": r["label"] = ret["PROBABILITIES"][0]["label"]
    if change == "empty_reason": r["reason"] = ""
    if change == "bad_status": r["status"] = "SKIPPED"
    assert send(event, render(ret, event["receipt"]))["status"] == "REFUSED"


def test_all_unpriced_is_research_only(event):
    upstream(event); ret = X.parse(make_return(event, "L5"))
    ret["UNPRICED"] = [dict(label=r["label"], status="NOT_VALIDATED", reason="Exact-scope simulator failed its checks") for r in ret["PROBABILITIES"]]
    ret["PROBABILITIES"] = []
    assert send(event, render(ret))["status"] == "ACCEPTED"
    assert I.admit(event["folder"], root=event["root"], at=AT)["admission"] == "READY_RESEARCH_ONLY"


def test_delay_preserves_returns_and_extends_only_with_fresh_official_no_play_evidence(event):
    complete(event); before = (event["folder"] / "INTAKE.csv").read_bytes(); identity = I.manifest_hash(event["folder"])
    p = event["root"] / "DELAY.txt"; p.write_text("EXAMPLE official venue: game not started; new start 03:00 UTC")
    O.delay(event["folder"], "2026-11-11T03:00:00+00:00", URL1, "EXAMPLE league", "2026-11-11T02:05:00+00:00", p,
            root=event["root"], at="2026-11-11T02:06:00+00:00")
    result = I.admit(event["folder"], root=event["root"], at="2026-11-11T02:10:00+00:00")
    assert result["effective_start"] == "2026-11-11T03:00:00+00:00"
    assert I.manifest_hash(event["folder"]) == identity and before == (event["folder"] / "INTAKE.csv").read_bytes()
    note = next((event["folder"] / "delay_evidence").iterdir()); note.write_text("TAMPERED")
    with pytest.raises(X.ExternalError, match="evidence changed"): O.effective_start(event["folder"])


@pytest.mark.parametrize("change", ["started", "stale", "past", "bound"])
def test_delay_refuses_started_stale_past_or_issued_changes(event, change):
    p = event["root"] / "DELAY.txt"; p.write_text("EXAMPLE official no-play note")
    if change == "bound": (event["folder"] / "CARD_BINDING.csv").write_text("BOUND")
    with pytest.raises(X.ExternalError):
        O.delay(event["folder"], "2026-11-11T01:00:00+00:00" if change == "past" else "2026-11-11T03:00:00+00:00", URL1, "EXAMPLE league",
                "2026-11-11T00:00:00+00:00" if change == "stale" else AT, p, status="STARTED" if change == "started" else "NOT_STARTED", root=event["root"], at=AT)


def test_access_expiry_is_judged_at_actual_retrieval_not_later_revalidation(event):
    ret = X.parse(make_return(event, "L1"))
    # At a later admission time, the source observation still attests the original pre-expiry access.
    assert send(event, render(ret))["status"] == "ACCEPTED"
    assert O.access_rows(event["folder"], event["root"], "2026-11-11T00:01:00+00:00")[0]["valid_until"]


def test_source_refresh_preserves_method_and_earlier_observation(event):
    p = event["root"] / "ACCESS_WEEK2.csv"
    write(p, ("host", "chatgpt_browsing", "chatgpt_blocked_paths", "checked_at", "valid_until"),
          [dict(host="club.example.org", chatgpt_browsing="BLOCKED", chatgpt_blocked_paths="/", checked_at="2026-11-11T00:20:00+00:00", valid_until="2026-11-25T00:00:00+00:00")])
    subprocess.run(["git", "add", "--", p.name], cwd=event["root"], check=True)
    subprocess.run(["git", "-c", "user.name=EXAMPLE", "-c", "user.email=example@example.org", "commit", "-qm", "EXAMPLE access observation"], cwd=event["root"], check=True)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=event["root"], text=True).strip()
    digest = I.manifest_hash(event["folder"])
    O.refresh_access(event["folder"], p.name, commit, root=event["root"], at="2026-11-11T00:25:00+00:00")
    assert O.access_rows(event["folder"], event["root"], "2026-11-11T00:01:00+00:00")[0]["chatgpt_browsing"] == "ALLOWED"
    assert O.access_rows(event["folder"], event["root"], "2026-11-11T00:30:00+00:00")[0]["chatgpt_browsing"] == "BLOCKED"
    assert I.manifest_hash(event["folder"]) == digest
    p.write_bytes(p.read_bytes() + b"\n")
    with pytest.raises(X.ExternalError, match="artifact changed"): O.access_rows(event["folder"], event["root"], AT)


def test_single_must_precede_packet_and_return_exposure(event):
    path = event["root"] / "SINGLE.md"; path.write_text(event["receipt"], encoding="utf-8")
    result = O.freeze_comparison(event["folder"], path, root=event["root"], at="2026-11-10T23:55:00+00:00")
    assert result["rows"] == 2
    O.packet(event["folder"], "L1", root=event["root"], at="2026-11-10T23:56:00+00:00")
    with pytest.raises(X.ExternalError, match="immutable"): O.freeze_comparison(event["folder"], path, root=event["root"], at=AT)
    ev = new_mode(event, "REDUCED", ["L2", "L3", "L5"])
    O.packet(ev["folder"], "L2", root=ev["root"], at="2026-11-10T23:56:00+00:00")
    with pytest.raises(X.ExternalError, match="before external"): O.freeze_comparison(ev["folder"], path, root=ev["root"], at=AT)


def test_fact_scorecard_uses_exact_claims_and_preserves_missingness(event):
    complete(event); claims = O.facts(event["folder"]); obs = event["root"] / "OBS.csv"
    r = dict(fact_id=claims[0]["fact_id"], actual_value=claims[0]["value"], disposition="CORRECT", source_url=URL1,
             observed_at="2026-11-11T05:00:00+00:00", reason="EXAMPLE official final roster")
    write(obs, O.FACT_FIELDS, [r])
    summaries = O.score_facts(event["folder"], obs, event["root"] / "SCORES", "2026-11-11T04:00:00+00:00", root=event["root"], at="2026-11-11T06:00:00+00:00")
    assert sum(r["UNRESOLVED"] for r in summaries if r["group_type"] == "lane") == len(claims) - 1
    assert sum(r["CORRECT"] for r in summaries if r["group_type"] == "lane") == 1


def test_soccer_baseline_and_uploaded_kit_use_measured_exact_league():
    from ml.kit import sr_kit as K
    _, meta = R.baseline_grid("Soccer/Algeria Ligue 1")
    assert meta["source"] == "Soccer/Algeria Ligue 1"
    row = K.row(K.load_params(I.ROOT / "research/external/kit/v24.15/KIT_PARAMETERS_v24.15.csv"), "Soccer/Algeria Ligue 1")
    assert float(row["mean_total"]) == pytest.approx(1.8687)
    assert row["competition"] == "Soccer/Algeria Ligue 1"


def test_team_centre_excludes_future_same_day_other_leagues_and_endpoints():
    games = [dict(competition="Soccer/EXAMPLE", date=f"2026-10-{n:02d}", home="H", away="A", hs=2., as_=1., endpoint="REGULATION", kind="MATCH", event_id=str(n)) for n in range(1, 10)]
    first = T.centre(games, "Soccer/EXAMPLE", "H", "A", "2026-10-10T00:00:00+00:00")
    for comp, date in (("Soccer/OTHER", "2026-10-01"), ("Soccer/EXAMPLE", "2026-10-10"), ("Soccer/EXAMPLE", "2026-10-20")):
        games.append(dict(games[0], competition=comp, date=date, hs=1000., event_id=comp+date))
    assert T.centre(games, "Soccer/EXAMPLE", "H", "A", "2026-10-10T00:00:00+00:00") == first
    games.append(dict(games[0], endpoint="EXTRA_TIME", event_id="MIXED"))
    with pytest.raises(ValueError, match="mixed"): T.centre(games, "Soccer/EXAMPLE", "H", "A", "2026-10-10T00:00:00+00:00")


def test_cricket_centre_is_conditional_batting_and_bowling_not_match_total():
    rows = [dict(competition="Cricket/EXAMPLE", date="2026-10-01", home="A", away="B", hs=150., as_=0., endpoint="FIRST_INNINGS", kind="INNINGS", event_id="1")]
    c = T.centre(rows, "Cricket/EXAMPLE", "A", "B", "2026-10-10T00:00:00+00:00")
    assert c["mean_home"] == 150 and c["total"] == "" and "CONDITIONAL" in c["status"]
    with pytest.raises(ValueError, match="BATTING"): T.centre(rows, "Cricket/EXAMPLE", "B", "A", "2026-10-10T00:00:00+00:00")


@pytest.mark.parametrize("mode", ["PARTIAL", "REDUCED", "DELAYED"])
def test_new_modes_reach_real_mini_learning_ledger_and_binding(event, mode):
    """A real public-function lifecycle in a temporary Git repo, not just permissive intake."""
    import shutil
    from ml import learning_log as LL, ledger
    from ml.kit import sr_kit as K
    from ml.tests import test_picks_ledger as TP, test_learning_log as TL
    if mode == "REDUCED": event = new_mode(event, "REDUCED", ["L2", "L3", "L5"])
    if mode == "DELAYED":
        p = event["root"] / "OFFICIAL_DELAY.txt"; p.write_text("EXAMPLE official no play; start 03:00 UTC")
        O.delay(event["folder"], "2026-11-11T03:00:00+00:00", URL1, "EXAMPLE league", AT, p, root=event["root"], at=AT)
    upstream(event, ("L2", "L3") if mode == "REDUCED" else ("L1", "L2", "L3", "L4"))
    unpriced = []
    if mode == "PARTIAL":
        c = event["contracts"][0]
        result, receipt = K.run("points_from_centre", dict(competition=event["e"]["competition"], total=224., margin=4.5,
                              lines=[dict(label=c["label"], family=c["family"], side=c["side"], line=float(c["line"]))]), params_path=event["params"])
        event = dict(event, result=result, receipt=receipt)
        unpriced = [dict(label=event["contracts"][1]["label"], status="UNAVAILABLE", reason="EXAMPLE requested scope lacks approved inputs")]
    ret = X.parse(make_return(event, "L5")); ret["UNPRICED"] = unpriced
    assert send(event, render(ret, event["receipt"]))["status"] == "ACCEPTED"
    res = I.admit(event["folder"], root=event["root"], at=AT)
    root, folder, e = event["root"], event["folder"], event["e"]
    TP.root.__wrapped__(root)
    dictionary = root / LL.DICTIONARY; dictionary.parent.mkdir(parents=True, exist_ok=True); shutil.copy(LL.ROOT / LL.DICTIONARY, dictionary)
    definitions = "|".join(c["label"] + "=" + "~".join(c[k] for k in ("period", "endpoint", "action", "unit")) for c in event["contracts"])
    start = O.effective_start(folder, e)
    meta = dict(competition=e["competition"], tier="B", reference_id="BASELINE_LEAGUE_V1:COMPETITION_ROW:Basketball/NBA", abstain="YES",
                scheduled_start=start, issued_at=AT, reference_frozen_at="2026-11-10T23:00:00+00:00", rank_scope="SUPPLIED_ONLY",
                event_key=e["event_key"], external_manifest_sha256=res["manifest_sha256"], external_packet_sha256=res["input_package_sha256"],
                contract_definitions=definitions, research_mode=res["research_mode"])
    rows = []
    for r in event["result"]["rows"]:
        centre, sd = (4.5, 15.1) if r["family"] == "handicap" else (224., 19.4)
        threshold = -float(r["line"]) if r["family"] == "handicap" else float(r["line"])
        rows.append(dict(label=r["label"], family=r["family"].upper(), quantity="MARGIN" if r["family"] == "handicap" else "TOTAL", side=r["side"], line=str(r["line"]),
                         line_source="SUPPLIED", reference_p=str(r["final_p"]), baseline_p=str(r["final_p"]), model_p="NONE", final_p=str(r["final_p"]),
                         w=str(r["w"]), p=str(r["p"]), l=str(r["l"]), line_implied_p="0.5", centre=str(centre), sd=str(sd), z=str(abs(threshold-centre)/sd),
                         most_likely_rank="", information_row="N"))
    text = f"<!-- BEGIN CARD {e['local_key']} -->\n" + TP.render(meta, rows, key=e["local_key"])
    text += "\n" + "\n".join(f"A{i} EXAMPLE retained evidence and gaps" for i in range(1, 10))
    if unpriced: text += f"\n<!-- BEGIN UNPRICED {e['local_key']} -->\n" + I.csv_bytes(O.UNPRICED_FIELDS, unpriced).decode() + f"<!-- END UNPRICED {e['local_key']} -->\n"
    text += f"\n<!-- END CARD {e['local_key']} -->"
    card = root / "CARD.md"; card.write_text(text, encoding="utf-8")
    receipt = root / "CENTRAL.md"; receipt.write_text(event["receipt"], encoding="utf-8")
    mini = root / "MINI.md"; mini.write_text("# EXAMPLE\n| Writer/lease | EXAMPLE; expires 2026-11-12T00:00:00+00:00 |\n<!-- BEGIN FOOTER -->\n"
        "| Last local event key / next local event key | `NONE` / `LOCAL-EXAMPLE-G0001` |\n| New cards / numeric / qualitative / NO_FORECAST | 0 / 0 / 0 / 0 |\n"
        "| Mini status | ACTIVE / EMPTY |\n<!-- END FOOTER -->\n", encoding="utf-8")
    I.append_card(folder, card, receipt, I.sha(mini.read_bytes()), "EXAMPLE", root=root, at=AT)
    game = root / "GAME.csv"
    write(game, ("local_key", "competition", "home", "away", "scheduled_start", "native_event_id", "season", "venue"),
          [dict(local_key=e["local_key"], competition=e["competition"], home=e["home"], away=e["away"], scheduled_start=start,
                native_event_id=e["native_event_id"], season="2026", venue="EXAMPLE")])
    learning = LL.init(mini, e["local_key"], game, sport="Basketball", root=root); TL._fill(learning)
    ledger.add(mini, e["local_key"], root=root, now=AT)
    assert I.bind_card(folder, receipt, root=root, at=AT)["status"] == "CARD_BOUND_NOT_PUBLICATION_PROOF"
    assert len(ledger.read(root / ledger.LEDGER)) == len(rows)


def test_cricket_importer_skips_combined_members_and_replays_hash_checked_downloads(tmp_path, monkeypatch):
    import io, zipfile
    from ml import bulk_history as B
    buf = io.BytesIO()
    header = "match_id,innings,start_date,ball,batting_team,bowling_team,runs_off_bat,extras,wides,noballs,wicket_type\n"
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("123.csv", header + "123,1,2026-01-01,0.1,A,B,1,0,,,\n")
        z.writestr("all_matches.csv", header + "123,1,2026-01-01,0.1,A,B,1,0,,,\n456,1,2026-01-02,0.1,C,D,4,0,,,\n")
    raw = buf.getvalue(); digest = I.sha(raw); cache = tmp_path / "CACHE"; cache.mkdir(); (cache / digest).write_bytes(raw)
    source = tmp_path / "RECEIPTS.csv"
    write(source, B.RECEIPT_FIELDS, [dict(dataset="cricket", url="https://cricsheet.org/downloads/example_csv2.zip", retrieved_at=AT, bytes=len(raw), sha256=digest, cache_file=digest)])
    monkeypatch.setattr(B, "CRICKET_ARCHIVES", (("example", "Cricket T20/EXAMPLE", 20),))
    result = B.cricket(cache, out=tmp_path / "CLEAN", receipts_file=source)
    assert result["innings"] == 1 and I.read(tmp_path / "CLEAN/INNINGS.csv")[0]["runs"] == "1"
    assert I.read(tmp_path / "CLEAN/EXCLUDED_MEMBERS.csv")[0]["member"] == "all_matches.csv"


def test_effort_missing_is_not_zero_and_negative_or_nan_is_refused(event):
    report = O.operating_report(event["folder"], event["root"] / "EFFORT_REPORT", root=event["root"], at=AT)
    assert report["owner_effort_status"] == "MISSING_NOT_ZERO"
    for value in (-1, float("nan"), float("inf")):
        with pytest.raises(X.ExternalError): O.record_effort(event["folder"], "OWNER_TRANSFER", value, "EXAMPLE")


def test_comparison_pair_exports_original_clocks_with_verifiable_source_hashes(event):
    from ml.evaluation import prospective as P
    receipt = event["root"] / "PRICE.md"; receipt.write_text(event["receipt"], encoding="utf-8")
    O.freeze_comparison(event["folder"], receipt, root=event["root"], at="2026-11-10T23:55:00+00:00")
    for which in ("REFERENCE", "BASELINE"):
        O.freeze_comparison(event["folder"], receipt, which=which, root=event["root"], at="2026-11-10T23:55:00+00:00")
    O.packet(event["folder"], "L1", root=event["root"], at="2026-11-10T23:56:00+00:00")
    complete(event)
    O.freeze_comparison(event["folder"], receipt, which="FIVE", root=event["root"], at=AT)
    out = event["root"] / "COLLECTION"
    assert O.collect_comparisons([event["folder"]], out, root=event["root"])[0]["status"] == "PAIRED"
    rows = P.verify_ledger(out / "FORECASTS.csv")
    assert len(rows) == 8
    assert {r["issued_at"] for r in rows} == {AT, "2026-11-10T23:55:00+00:00"}
    assert len(I.read(out / "SOURCES.csv")) == 4
    for r in rows: assert len(r["code_sha256"]) == 64


def test_expired_permission_can_attest_earlier_retrieval_but_not_a_new_open(event):
    p = event["root"] / "SHORT_ACCESS.csv"
    write(p, ("host", "chatgpt_browsing", "chatgpt_blocked_paths", "valid_until"),
          [dict(host="club.example.org", chatgpt_browsing="ALLOWED", chatgpt_blocked_paths="", valid_until="2026-11-11T00:02:00+00:00")])
    subprocess.run(["git", "add", "--", p.name], cwd=event["root"], check=True)
    subprocess.run(["git", "-c", "user.name=EXAMPLE", "-c", "user.email=example@example.org", "commit", "-qm", "EXAMPLE short access"], cwd=event["root"], check=True)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=event["root"], text=True).strip()
    arts = {r["role"]: r["path"] for r in I.read(event["folder"] / "ARTIFACTS.csv", I.ART_FIELDS)}; arts["access"] = p.name
    dest = event["root"] / "SHORT"
    e = I.initialize(dict(event["e"], commit=commit), event["contracts"], I.read(event["folder"] / "REQUIREMENTS.csv"), dest,
                     artifacts=arts, root=event["root"], at="2026-11-10T23:50:00+00:00")
    ev = dict(event, folder=dest, e=e)
    ret = X.parse(make_return(ev, "L1"))
    assert send(ev, render(ret), at=AT)["status"] == "ACCEPTED"
    ret["EVIDENCE"][0]["retrieved_at"] = "2026-11-11T00:03:00+00:00"
    ret["ACCESS_LOG"][0]["checked_at"] = "2026-11-11T00:03:00+00:00"
    result = send(ev, render(ret), at=AT)
    assert result["status"] == "REFUSED" and any("expired at retrieval" in p for p in result["problems"])


def test_soccer_installer_is_idempotent_and_requires_reviewed_table_identity(tmp_path):
    from ml.kit import params as P
    target = tmp_path / "TABLE.csv"; target.write_bytes(P.PARAMS.read_bytes())
    original = target.read_bytes(); archive = tmp_path / "ORIGINAL.csv"
    result = P.install_soccer(I.ROOT / "research/verification/framework_change_2026-11-11-1/soccer_study", target,
                              expected_sha256=I.sha(original), archive=archive)
    assert result["status"] == "ALREADY_CURRENT" and target.read_bytes() == original and not archive.exists()
    with pytest.raises(ValueError, match="changed since review"):
        P.install_soccer(I.ROOT / "research/verification/framework_change_2026-11-11-1/soccer_study", target,
                         expected_sha256="0" * 64, archive=archive)


def test_append_and_bind_cannot_race_another_event_writer(event):
    with I.locked(event["folder"]):
        with pytest.raises(X.ExternalError, match="another writer"):
            I.append_card(event["folder"], "UNREAD.md", "UNREAD.md", "0" * 64, "EXAMPLE", root=event["root"], at=AT)
        with pytest.raises(X.ExternalError, match="another writer"):
            I.bind_card(event["folder"], "UNREAD.md", root=event["root"], at=AT)
