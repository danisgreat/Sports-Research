"""Reproduced review failures and the complete five-lane admission/correction lifecycle. Offline EXAMPLE data only."""
import csv
import io
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest

from ml import external as X, history_pack as H, research_intake as I
from ml.kit import sr_kit as K, cli as KC
from ml.tests.test_release_v24_13 import _params, lane, EV, PR

START = "2026-11-11T02:00:00+00:00"
AT = "2026-11-11T01:00:00+00:00"
URL1, URL2 = "https://club.example.org/news", "https://league.example.net/report"


def write(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(I.csv_bytes(fields, rows))


@pytest.fixture
def event(tmp_path):
    root = tmp_path / "repo"; root.mkdir()
    params = _params(root)
    (root / "PHASES.csv").write_text("kit_version,group,innings,over\n", encoding="utf-8")
    (root / "REFERENCE.md").write_text("EXAMPLE frozen centre 224 and 4.5; no outcome seen.\n", encoding="utf-8")
    (root / "sr_kit.py").write_bytes(Path(K.__file__).read_bytes())
    write(root / "ACCESS.csv", ("host", "chatgpt_browsing", "chatgpt_blocked_paths", "valid_until"),
          [dict(host=h, chatgpt_browsing="ALLOWED", chatgpt_blocked_paths="", valid_until="2026-11-18T00:00:00+00:00")
           for h in ("club.example.org", "league.example.net")])
    artifacts = dict(kit="sr_kit.py", params=params.name, phases="PHASES.csv", reference="REFERENCE.md", access="ACCESS.csv")
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "config", "core.autocrlf", "false"], cwd=root, check=True)
    subprocess.run(["git", "add", "--", *artifacts.values()], cwd=root, check=True)
    subprocess.run(["git", "-c", "user.name=EXAMPLE", "-c", "user.email=example@example.org", "commit", "-qm", "EXAMPLE inputs"], cwd=root, check=True)
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    spec = dict(commit=commit, sport="Basketball", competition="Basketball/NBA", native_event_id="EXAMPLE:GAME1", home="Home", away="Away",
                scheduled_start=START, game_number="1", mini_path="MINI.md", local_key="LOCAL-EXAMPLE-G0001", writer="EXAMPLE")
    contracts = [dict(label="H-4.5", family="handicap", side="HOME", line="-4.5", period="FULL_MATCH", endpoint="INCLUDING_OVERTIME", action="PLAYED", unit="POINTS"),
                 dict(label="U224.5", family="total", side="UNDER", line="224.5", period="FULL_MATCH", endpoint="INCLUDING_OVERTIME", action="PLAYED", unit="POINTS")]
    fields = (("L1", "status:Player A", "HOME"), ("L2", "window:L5", "HOME"), ("L3", "endpoint_rule", "EVENT"),
              ("L4", "status:Player A", "HOME"), ("L5", "pricing", "EVENT"))
    reqs = [dict(lane=l, requirement_id=l + "R", side=s, field=f, required="YES", corroboration_required="YES" if l in ("L1", "L4") else "NO")
            for l, f, s in fields]
    folder = root / "EVENT"
    e = I.initialize(spec, contracts, reqs, folder, artifacts=artifacts, root=root, at="2026-11-10T23:50:00+00:00")
    inputs = dict(competition="Basketball/NBA", total=224.0, margin=4.5, lines=[{k: c[k] for k in ("label", "family", "side", "line")} for c in contracts])
    for r in inputs["lines"]: r["line"] = float(r["line"])
    result, receipt = K.run("points_from_centre", inputs, params_path=params)
    return dict(root=root, folder=folder, e=e, params=params, receipt=receipt, result=result, contracts=contracts)


def make_return(event, lane_id, *, value=None):
    folder, e = event["folder"], event["e"]
    index = int(lane_id[-1])
    started, completed = ("00:30:00", "00:35:00") if index == 4 else ("00:50:00", "00:55:00") if index == 5 else ("00:00:00", "00:05:00")
    h = dict(event_key=e["event_key"], lane=lane_id, chat_label=f"CHAT-{index}", profile_version=X.PROFILE_VERSION,
             commit=e["commit"], started_at=f"2026-11-11T{started}+00:00", completed_at=f"2026-11-11T{completed}+00:00",
             reader="CHATGPT_BROWSING", manifest_sha256=I.manifest_hash(folder), input_package_sha256=I.packet_hash(folder, lane_id), outcome_exposure="NONE_DECLARED")
    evidence, access, probs = [], [], []
    if index != 5:
        source = URL2 if index == 4 else URL1
        field = "status:Player A" if index in (1, 4) else "window:L5" if index == 2 else "endpoint_rule"
        evidence = [dict(side="EVENT" if index == 3 else "HOME", field=field, value=value or ("OUT" if index in (1, 4) else "n=5" if index == 2 else "INCLUDING_OVERTIME"),
                         source_url=source, source_class="FIELD_OWNER", published_at="2026-11-10T23:00:00+00:00", retrieved_at="2026-11-11T00:01:00+00:00",
                         confirmation="OFFICIAL_CONFIRMED", notes="EXAMPLE")]
        access = [dict(url=source, result="OPENED", checked_at="2026-11-11T00:01:00+00:00", notes="pinned reader decision checked")]
    else:
        probs = [{k: str(r[k]) for k in ("label", "family", "side", "line", "w", "p", "l", "final_p")} for r in event["result"]["rows"]]
        for r in probs: r.update(line_source="SUPPLIED", kit_receipt_sha256=K.receipt_sha256(event["receipt"]))
    text = (event["receipt"] + "\n" if index == 5 else "") + "<!-- BEGIN LANE_RETURN -->\n"
    text += "\n".join(k + ": " + v for k, v in h.items()) + "\n\n"
    for name, rows in (("EVIDENCE", evidence), ("PROBABILITIES", probs), ("ACCESS_LOG", access),
                       ("REQUIREMENTS", [dict(requirement_id=lane_id + "R", status="DONE", reason="")])):
        text += "[" + name + "]\n" + I.csv_bytes(dict(X.SECTIONS, **X.OPTIONAL_SECTIONS)[name], rows).decode()
    return text + "<!-- END LANE_RETURN -->\n"


def put_return(event, lane_id, *, value=None, parent=""):
    path = event["root"] / f"RETURN_{lane_id}_{value or 'original'}.md"
    path.write_text(make_return(event, lane_id, value=value), encoding="utf-8")
    at = "2026-11-11T00:40:00+00:00" if lane_id == "L4" else AT if lane_id == "L5" else "2026-11-11T00:10:00+00:00"
    return I.intake(event["folder"], path, parent=parent, root=event["root"], at=at)


def complete(event):
    for lane_id in ("L1", "L2", "L3", "L4"):
        assert put_return(event, lane_id)["status"] == "ACCEPTED"
    review = event["root"] / "review.txt"; review.write_text("EXAMPLE independent original collection reviewed; sporting-only source notes.")
    for source, collector in ((URL1, "ORIGINAL_CLUB"), (URL2, "ORIGINAL_LEAGUE")):
        I.review_source(event["folder"], source, collector, review, status="VERIFIED", at="2026-11-11T00:41:00+00:00")
    assert put_return(event, "L5")["status"] == "ACCEPTED"
    return I.admit(event["folder"], root=event["root"], at=AT)


def test_five_lane_lifecycle_captures_originals_reproduces_prices_and_admits(event):
    res = complete(event)
    assert res["admission"] == "READY_FOR_CARD" and res["predictive_qualification"] == "UNPROVEN"
    assert res["n_returns"] == 5 and not res["conflicts"]
    assert next(r for r in res["evidence"] if r["field"] == "status:Player A")["corroboration"] == "CORROBORATED"
    assert len(I.ledger(event["folder"])) == 5
    again = I.intake(event["folder"], event["root"] / "RETURN_L1_original.md", root=event["root"], at=AT)
    assert again["status"] == "ALREADY_EXISTS" and len(I.ledger(event["folder"])) == 5


def test_upstream_correction_invalidates_independent_recheck_and_pricing(event):
    complete(event)
    parent = I.accepted(event["folder"])["L1"]["return_sha256"]
    assert put_return(event, "L1", value="QUESTIONABLE", parent=parent)["status"] == "ACCEPTED"
    with pytest.raises(X.ExternalError, match="stale"):
        I.admit(event["folder"], root=event["root"], at=AT)


def test_copied_feed_does_not_create_independent_quorum(event):
    for lane_id in ("L1", "L2", "L3", "L4"): assert put_return(event, lane_id)["status"] == "ACCEPTED"
    p = event["root"] / "review.txt"; p.write_text("Both domains use the same provider")
    for url in (URL1, URL2): I.review_source(event["folder"], url, "SAME_FEED", p, status="VERIFIED", at="2026-11-11T00:41:00+00:00")
    assert put_return(event, "L5")["status"] == "ACCEPTED"
    with pytest.raises(X.ExternalError, match="incomplete"):
        I.admit(event["folder"], root=event["root"], at=AT)


@pytest.mark.parametrize("change", ["future", "version", "manifest", "exposure", "access", "requirement"])
def test_bad_lane_is_retained_but_not_accepted(event, change):
    text = make_return(event, "L1")
    if change == "future": text = text.replace("2026-11-10T23:00:00+00:00", "2027-01-01T00:00:00+00:00")
    if change == "version": text = text.replace("profile_version: v24.15", "profile_version: UNRELATED")
    if change == "manifest": text = text.replace(I.manifest_hash(event["folder"]), "0" * 64)
    if change == "exposure": text = text.replace("NONE_DECLARED", "OUTCOME_SEEN")
    if change == "access": text = text.replace(",OPENED,", ",RULES_UNKNOWN,")
    if change == "requirement": text = text.replace("L1R,DONE,", "L1R,NOT_ATTEMPTED,")
    source = event["root"] / "BAD.md"; source.write_text(text, encoding="utf-8")
    result = I.intake(event["folder"], source, root=event["root"], at=AT)
    assert result["status"] == "REFUSED" and not I.accepted(event["folder"])
    assert (event["folder"] / I.ledger(event["folder"])[0]["file"]).read_bytes() == source.read_bytes()


def test_pinned_artifact_change_and_manifest_tampering_are_refused(event):
    event["params"].write_bytes(event["params"].read_bytes() + b"\n")
    with pytest.raises(X.ExternalError, match="artifact"):
        I.load(event["folder"], event["root"])


@pytest.mark.parametrize("change", ["nan", "removed", "contract", "duplicate", "hash"])
def test_receipt_counterexamples_are_rejected(event, change):
    lines = event["receipt"].splitlines(); row = lines.index("rows:") + 2
    if change == "nan":
        cells = next(csv.reader([lines[row]])); cells[4:8] = ["nan"] * 4; lines[row] = ",".join(cells)
    if change == "removed": lines = lines[:row] + [lines[-1]]
    if change == "contract":
        cells = next(csv.reader([lines[row]])); cells[1:4] = ["winner", "AWAY", "999"]; lines[row] = ",".join(cells)
    if change == "duplicate": lines.insert(row, lines[row])
    if change == "hash": lines = ["params_sha256: NOT_USED" if l.startswith("params_sha256:") else l for l in lines]
    try: problems = KC.verify("\n".join(lines), params=event["params"], phases=event["root"] / "PHASES.csv")
    except K.KitError: problems = ["REFUSED"]
    assert problems


@pytest.mark.parametrize("number", ["nan", "inf", "-0.1", "1.1"])
def test_invalid_lane_probabilities_are_refused(number):
    p = X.parse(lane("L5", "CHAT-5", probs=[PR]))
    p["PROBABILITIES"][0]["final_p"] = number
    assert X.check(p)


def test_duplicate_and_mixed_version_consensus_is_refused():
    p = X.parse(lane("L5", "CHAT-5", probs=[PR]))
    with pytest.raises(X.ExternalError, match="duplicate"): X.merge([p, p], p["header"]["event_key"])
    other = deepcopy(p); other["raw_sha256"] = "d" * 64; other["header"].update(chat_label="OTHER", commit="c" * 40)
    with pytest.raises(X.ExternalError, match="mixed commits"): X.merge([p, other], p["header"]["event_key"])


def test_native_identity_distinguishes_competitions_doubleheaders_and_survives_aliases():
    make = lambda **kw: X.event_key("Basketball", "2026-11-11", "Melbourne Tigers A", "Sydney Kings", **kw)
    a = make(competition="Basketball/League A", native_event_id="EXAMPLE:1", game_number="1")
    assert a != make(competition="Basketball/League B", native_event_id="EXAMPLE:1", game_number="1")
    assert a != make(competition="Basketball/League A", native_event_id="EXAMPLE:1", game_number="2")
    assert a == X.event_key("Basketball", "2026-11-12", "Sydney Kings", "Tigers A", competition="Basketball/League A", native_event_id="EXAMPLE:1", game_number="1")


def test_endpoint_conflict_is_reported(event):
    a = X.parse(make_return(event, "L3")); b = deepcopy(a)
    b["header"].update(lane="FULL", chat_label="SECOND"); b["raw_sha256"] = "c" * 64
    b["EVIDENCE"][0]["value"] = "REGULATION_ONLY"
    assert X.merge([a, b], event["e"]["event_key"])["conflicts"][0]["field"] == "endpoint_rule"


def test_history_never_falls_back_to_another_competition(monkeypatch):
    base = dict(date="2026-11-01", season="2026", home="A", away="B", ft_home="2", ft_away="1", ht_home="1", ht_away="0", source_url="https://example.org")
    monkeypatch.setattr(H, "_read", lambda _: [dict(base, competition="Soccer/A"), dict(base, competition="Soccer/B")])
    _, games = H.soccer_games("Soccer/A", "A", "2026-11-11")
    assert len(games) == 1 and games[0]["competition"] == "Soccer/A"
    cricket = dict(competition="Cricket T20/B", innings="1", start_date="2026-11-01", batting_team="A", bowling_team="B")
    monkeypatch.setattr(H, "_read", lambda _: [cricket])
    with pytest.raises(H.PackError): H.cricket_games("Cricket T20/A", "A", "2026-11-11")


def test_cricket_views_are_explicit_conditional_samples(monkeypatch):
    base = dict(competition="Cricket T20/A", start_date="2026-11-01", batting_team="A", bowling_team="B", format_overs="20", runs_at_over6="40",
                venue="EXAMPLE", runs="150", reduced="N", match_id="ONE", season="2026")
    monkeypatch.setattr(H, "_read", lambda _: [dict(base, innings="1"), dict(base, innings="2", batting_team="B", bowling_team="A")])
    _, first = H.cricket_games("Cricket T20/A", "A", "2026-11-11")
    _, chase = H.cricket_games("Cricket T20/A", "B", "2026-11-11", "CHASING")
    assert first[0]["sample_scope"] == "BATTING_FIRST_INNINGS_NOT_LAST_MATCHES"
    assert chase[0]["sample_scope"] == "CHASING_INNINGS_NOT_LAST_MATCHES"


def test_unvalidated_simulation_cannot_supply_primary():
    with pytest.raises(K.KitError, match="NOT_VALIDATED"):
        K.run("cricket_innings", dict(lines=[], group="EXAMPLE", innings=1))
    with pytest.raises(K.KitError, match="NOT_VALIDATED"):
        K.run("tennis_match", dict(pa=.65, pb=.62, lines=[], sigma=.1))


def test_full_card_append_learning_ledger_binding_and_settlement(event):
    """Actual public functions, real temporary Git repo and real byte-preserving mini write; no forecast/ledger mocks."""
    import shutil
    from ml import picks, ledger, learning_log as LL
    from ml.tests import test_picks_ledger as TP, test_learning_log as TL
    res = complete(event)
    root, folder, e = event["root"], event["folder"], event["e"]
    TP.root.__wrapped__(root)
    dictionary = root / LL.DICTIONARY; dictionary.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(Path(LL.ROOT) / LL.DICTIONARY, dictionary)
    definitions = "|".join(c["label"] + "=" + "~".join(c[k] for k in ("period", "endpoint", "action", "unit")) for c in event["contracts"])
    meta = dict(competition="Basketball/NBA", tier="B", reference_id="BASELINE_LEAGUE_V1:COMPETITION_ROW:Basketball/NBA", abstain="YES",
                scheduled_start=START, issued_at="2026-11-11T01:00:00+00:00", reference_frozen_at="2026-11-10T23:00:00+00:00",
                rank_scope="SUPPLIED_ONLY", event_key=e["event_key"], external_manifest_sha256=res["manifest_sha256"],
                external_packet_sha256=res["input_package_sha256"], contract_definitions=definitions)
    rows = []
    for p in event["result"]["rows"]:
        centre, sd = (4.5, 15.1) if p["family"] == "handicap" else (224.0, 19.4)
        threshold = -float(p["line"]) if p["family"] == "handicap" else float(p["line"])
        rows.append(dict(label=p["label"], family=p["family"].upper(), quantity="MARGIN" if p["family"] == "handicap" else "TOTAL", side=p["side"], line=str(p["line"]),
                         line_source="SUPPLIED", reference_p=str(p["final_p"]), baseline_p=str(p["final_p"]), model_p="NONE", final_p=str(p["final_p"]),
                         w=str(p["w"]), p=str(p["p"]), l=str(p["l"]), line_implied_p="0.5", centre=str(centre), sd=str(sd), z=str(abs(threshold-centre)/sd),
                         most_likely_rank="", information_row="N"))
    card_text = f"<!-- BEGIN CARD {e['local_key']} -->\n" + TP.render(meta, rows, key=e["local_key"])
    card_text += "\n" + "\n".join(f"### A{i} EXAMPLE synthetic research procedure and evidence" for i in range(1, 10))
    card_text += f"\n<!-- END CARD {e['local_key']} -->"
    card = root / "CANDIDATE.md"; card.write_text(card_text, encoding="utf-8")
    receipt = root / "CENTRAL_RECEIPT.md"; receipt.write_text(event["receipt"], encoding="utf-8")
    mini = root / "MINI.md"
    before = ("# EXAMPLE existing mini\r\n| Writer/lease | EXAMPLE; expires 2026-11-12T00:00:00+00:00 |\r\n"
              "<!-- BEGIN FOOTER -->\r\n| Last local event key / next local event key | `NONE` / `LOCAL-EXAMPLE-G0001` |\r\n"
              "| New cards / numeric / qualitative / NO_FORECAST | 0 / 0 / 0 / 0 |\r\n| Mini status | ACTIVE / EMPTY |\r\n<!-- END FOOTER -->").encode()
    mini.write_bytes(before)
    with pytest.raises(X.ExternalError, match="writer"):
        I.append_card(folder, card, receipt, I.sha(before), "OTHER", root=root, at=AT)
    with pytest.raises(X.ExternalError, match="changed"):
        I.append_card(folder, card, receipt, "0"*64, "EXAMPLE", root=root, at=AT)
    app = I.append_card(folder, card, receipt, I.sha(before), "EXAMPLE", root=root, at=AT)
    assert app["canonical_ids_assigned"] == "0" and mini.read_bytes().startswith(before.split(b"<!-- BEGIN FOOTER -->")[0])
    assert I.append_card(folder, card, receipt, I.sha(mini.read_bytes()), "EXAMPLE", root=root, at=AT)["status"] == "ALREADY_EXISTS"
    game = root / "GAME.csv"
    game_fields = ("local_key", "competition", "home", "away", "scheduled_start", "native_event_id", "season", "venue")
    write(game, game_fields, [dict(local_key=e["local_key"], competition=e["competition"], home=e["home"], away=e["away"], scheduled_start=START,
                                  native_event_id=e["native_event_id"], season="2026", venue="EXAMPLE")])
    learning = LL.init(mini, e["local_key"], game, sport="Basketball", root=root)
    TL._fill(learning)
    ledger.add(mini, e["local_key"], root=root, now=AT)
    bound = I.bind_card(folder, receipt, root=root, at=AT)
    assert bound["status"] == "CARD_BOUND_NOT_PUBLICATION_PROOF"
    assert I.bind_card(folder, receipt, root=root, at=AT) == bound
    write(learning / "OUTCOME.csv", LL.OUTCOME, [dict(status="FINAL", home_score="110", away_score="105", home_regulation="110", away_regulation="105",
           decision="REGULATION", final_at="2026-11-11T04:00:00+00:00", source_url=URL1, second_source_url=URL2,
           retrieved_at="2026-11-11T04:05:00+00:00", evidence_grade="A")])
    write(learning / "GRADES.csv", LL.GRADES, [dict(label=c["label"], grade="WIN", basis="EXAMPLE margin 5 / total 215") for c in event["contracts"]])
    assert LL.check(e["local_key"], "settled", root=root) == []
    assert len(ledger.read(root / ledger.LEDGER)) == 2
    # Later unrelated mini content and a later clock do not invalidate the unchanged frozen card.
    mini.write_bytes(mini.read_bytes() + b"\r\nDated unrelated continuity note\r\n")
    assert I.bind_card(folder, receipt, root=root, at="2026-11-12T00:00:00+00:00") == bound


def test_research_only_retention_never_invents_a_numeric_card(event):
    root, folder, e = event["root"], event["folder"], event["e"]
    mini = root / "MINI.md"
    mini.write_text("| Writer/lease | EXAMPLE; expires 2026-11-13T00:00:00+00:00 |\n<!-- BEGIN FOOTER -->\n"
                    "| Last local event key / next local event key | `NONE` / `LOCAL-EXAMPLE-G0001` |\n"
                    "| New cards / numeric / qualitative / NO_FORECAST | 0 / 0 / 0 / 0 |\n| Mini status | ACTIVE / EMPTY |\n<!-- END FOOTER -->\n")
    record = root / "NO_FORECAST.md"
    record.write_text(f"<!-- BEGIN CARD {e['local_key']} -->\n<!-- RESEARCH_STATUS: NO_FORECAST -->\n{e['event_key']} {e['competition']} {START}\n"
                      + "\n".join(f"A{i} EXAMPLE unavailable with actual attempted source recorded" for i in range(1, 10))
                      + f"\n<!-- END CARD {e['local_key']} -->")
    r = I.append_card(folder, record, None, I.sha(mini.read_bytes()), "EXAMPLE", root=root,
                      at="2026-11-12T00:00:00+00:00", research_only="NO_FORECAST")
    assert r["status"] == "RETAINED_NO_FORECAST_NOT_ISSUED" and "1 / 0 / 0 / 1" in mini.read_text()
    assert not (folder / "CARD_BINDING.csv").exists() and not (root / "research/adjustment_ledger/ADJUSTMENT_LEDGER.csv").exists()


def test_empty_research_evaluation_remains_insufficient(tmp_path):
    from ml import external_evaluation as E
    from ml.evaluation import prospective as P
    labels = tmp_path / "OUTCOMES.csv"; write(labels, P.OUTCOME_FIELDS, [])
    result = E.evaluate(tmp_path / "NO_FORECASTS.csv", labels, tmp_path / "REPORT")
    assert all(r["disposition"] == "INSUFFICIENT_EVIDENCE" for r in result)


def test_evaluation_uses_exact_floor_and_never_moves_the_completed_cohort(tmp_path):
    import pandas as pd
    from ml import external_evaluation as E
    from ml.evaluation import prospective as P
    from ml.tests.test_learning_governance import _rows
    path = tmp_path / "FROZEN.csv"; labels = []
    def add_range(begin, end):
        for i in range(begin, end):
            start = pd.Timestamp("2025-01-06T09:00:00Z") + pd.Timedelta(days=i)
            group = []
            for name, prob in (("SINGLE_RESEARCH", .55), ("FIVE_LANES", .65), ("REFERENCE", .5), ("BASELINE", .5)):
                issued = start - pd.Timedelta(hours=1 if name == "FIVE_LANES" else 2)
                group.append(_rows(name, "v24.15", "CHAMPION" if name != "FIVE_LANES" else "CANDIDATE", f"EXAMPLE:{i}", start, prob, 1, issued=issued))
            P.freeze(path, group, now=start-pd.Timedelta(minutes=30))
            labels.append(dict(event_id=f"EXAMPLE:{i}", contract_key="WIN-H", result="WIN" if i % 2 else "LOSS",
                               final_at=(start+pd.Timedelta(hours=3)).isoformat(), available_at=(start+pd.Timedelta(hours=4)).isoformat(), evidence_sha256="e"*64))
    outcome = tmp_path / "OUTCOMES.csv"
    add_range(0, 99); write(outcome, P.OUTCOME_FIELDS, labels)
    result = E.evaluate(path, outcome, tmp_path / "N99", as_of="2026-01-01T00:00:00Z")
    assert all(r["disposition"] == "INSUFFICIENT_EVIDENCE" for r in result)
    add_range(99, 105); write(outcome, P.OUTCOME_FIELDS, labels)
    first = E.evaluate(path, outcome, tmp_path / "N105", as_of="2026-01-01T00:00:00Z")
    assert first[0]["paired_events"] == 105 and first[0]["settled_weeks"] >= 8
    add_range(105, 115); write(outcome, P.OUTCOME_FIELDS, labels)
    E.evaluate(path, outcome, tmp_path / "N115", as_of="2026-01-01T00:00:00Z")
    assert (tmp_path / "N105/COHORT.csv").read_bytes() == (tmp_path / "N115/COHORT.csv").read_bytes()
