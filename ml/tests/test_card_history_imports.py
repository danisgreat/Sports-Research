"""Regression checks for current imports and future log/inventory discovery."""
import math

import pandas as pd
import pytest

from ml.evaluation import card_history as ch


def local_inventory(path, **changes):
    row = dict(canonical_id="P-999", local_key="LOCAL-EXAMPLE-G0001",
               probability_role="ANALYST_PRIMARY_V1 p_card (uncalibrated)", original_rank="1",
               original_contract="Under 200.5", original_probability="0.7", sporting_grade="WIN",
               effective_revision="revision-1", evidence_class="B", note="BASELINE_P 0.6")
    row.update(changes)
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([row]).to_csv(path, index=False)
    return path


def test_discovery_refreshes_each_call_and_orders_numbered_parts(tmp_path, monkeypatch):
    monkeypatch.setattr(ch, "ROOT", tmp_path)
    monkeypatch.setattr(ch, "V", tmp_path / "verification")
    logs = tmp_path / "prediction logs"
    logs.mkdir()
    for name in ("PREDICTION_LOG_COMBINED_10.md", "PREDICTION_LOG_COMBINED.md",
                 "PREDICTION_LOG_COMBINED_2.md", "PREDICTION_LOG_COMBINED_10_backup.md"):
        (logs / name).touch()
    assert [p.name for p in ch.combined_logs()] == ["PREDICTION_LOG_COMBINED.md",
            "PREDICTION_LOG_COMBINED_2.md", "PREDICTION_LOG_COMBINED_10.md"]
    assert ch.import_inventories() == []
    source = local_inventory(ch.V / "mini_import_EXAMPLE" / "EFFECTIVE_SETTLEMENT_ROWS.csv")
    (source.parent / "IMPORTED_ROW_INVENTORY.csv").touch()  # effective rows take precedence
    assert ch.import_inventories() == [source]


def test_research_only_and_unranked_directions_never_create_primary_slots(tmp_path):
    source = local_inventory(tmp_path / "research.csv", original_rank="A1",
                             probability_role="ANALYST_NOT_PRIMARY (research-only; primary p_card NOT_ESTIMATED)")
    row = ch.inventory_rows(source)[0]
    assert row["cohort"] == "RESEARCH_ONLY_NOT_PRIMARY" and row["rank"] == 0 and row["p"] == .7
    source = local_inventory(tmp_path / "unranked.csv", original_rank="-", note="baseline unavailable")
    row = ch.inventory_rows(source)[0]
    assert row["cohort"] == "ANALYST_PRIMARY_V1" and row["rank"] == 0 and math.isnan(row["baseline"])


@pytest.mark.parametrize("changes", [{"probability_role": "UNRECOGNISED_PRIMARY"}, {"original_rank": "A1"}])
def test_unknown_roles_and_invalid_primary_ranks_are_rejected(tmp_path, changes):
    with pytest.raises(ValueError):
        ch.inventory_rows(local_inventory(tmp_path / "bad.csv", **changes))


def test_unknown_schema_and_duplicate_effective_rows_are_rejected(tmp_path):
    unknown = tmp_path / "unknown.csv"
    unknown.write_text("card,grade\nP-999,WIN\n", encoding="utf-8")
    with pytest.raises(ValueError, match="Unsupported import inventory schema"):
        ch.inventory_rows(unknown)
    source = local_inventory(tmp_path / "duplicate.csv")
    frame = pd.read_csv(source)
    pd.concat([frame, frame]).to_csv(source, index=False)
    with pytest.raises(ValueError, match="Duplicate effective"):
        ch.inventory_rows(source)


def test_full_and_abbreviated_grades_preserve_the_same_meaning():
    for short, full in zip(("W", "L", "P", "V", "U"), ("WIN", "LOSS", "PUSH", "VOID", "UNRESOLVED")):
        assert ch._grade(short) == ch._grade(full) == full


def test_missing_new_canonical_card_is_visible_in_coverage(tmp_path):
    log = tmp_path / "PREDICTION_LOG_COMBINED_10.md"
    log.write_text("<!-- BEGIN CANONICAL RESEARCH P-998 -->\n<!-- BEGIN CANONICAL RESEARCH P-999 -->\n", encoding="utf-8")
    coverage = ch.canonical_coverage(pd.DataFrame([dict(card="P-998")]), [log]).set_index("card")
    assert coverage.loc["P-998", "status"] == "ROWS_PRESENT"
    assert coverage.loc["P-999", "status"] == "NO_CONTRACT_ROWS_REVIEW_REQUIRED"
    assert coverage.loc["P-999", "rows"] == 0


def test_dates_and_source_lines_support_later_years_and_parts(tmp_path):
    log = tmp_path / "PREDICTION_LOG_COMBINED_10.md"
    log.write_text("## P-1000 — Example event · 2027-01-10\n", encoding="utf-8")
    assert ch.card_dates([log], tmp_path / "no_status")["P-1000"][0] == "2027-01-10"
    row = pd.DataFrame([dict(card="P-1000", source=log.name + ":1")])
    assert ch.fallback_dates(row, {}, [log])["P-1000"][0] == "2027-01-10"
    assert ch._event_date("born 2001-09-16; game 2027-01-10") == "2027-01-10"
    assert ch._event_date("born 2001-09-16") is None


@pytest.mark.parametrize("changed", [False, True])
def test_cli_receipt_covers_discovered_inputs_and_rejects_changes(tmp_path, monkeypatch, changed):
    source = local_inventory(tmp_path / "mini_import_EXAMPLE" / "EFFECTIVE_SETTLEMENT_ROWS.csv")
    mapping = source.parent / "LOCAL_ID_MAPPING.csv"  # initially absent; creating it mid-run is also a change
    log = tmp_path / "PREDICTION_LOG_COMBINED_10.md"
    log.write_text("example", encoding="utf-8")
    monkeypatch.setattr(ch, "import_inventories", lambda: [source])
    monkeypatch.setattr(ch, "combined_logs", lambda: [log])
    monkeypatch.setattr(ch, "build_rows", lambda *a, **k: (pd.DataFrame([dict(card="P-999")]), pd.DataFrame()))
    def report(*a, **k):
        if changed:
            mapping.write_text("canonical_id,event\nP-999,Example\n", encoding="utf-8")
        return {}
    monkeypatch.setattr(ch, "build_report", report)
    receipts = []
    monkeypatch.setattr(ch, "write", lambda out, folder, receipt: receipts.append(receipt))
    if changed:
        with pytest.raises(ValueError, match="changed during reporting"):
            ch.main(["--out", str(tmp_path / "report")])
        assert not receipts
    else:
        ch.main(["--out", str(tmp_path / "report")])
        assert receipts[0]["input:" + ch._label(source)]
        assert receipts[0]["input:" + ch._label(log)]
        assert receipts[0]["input:" + ch._label(mapping)] == "MISSING"


def test_overlapping_imports_require_reconciliation(tmp_path):
    first = local_inventory(tmp_path / "first" / "EFFECTIVE_SETTLEMENT_ROWS.csv")
    second = local_inventory(tmp_path / "second" / "EFFECTIVE_SETTLEMENT_ROWS.csv")
    with pytest.raises(ValueError, match="Overlapping import inventories"):
        ch.build_rows(inventories=[first, second])


@pytest.fixture(scope="module")
def current_rows():
    return ch.build_rows()[0]


def test_current_import_matches_preserved_cohort_rows(current_rows):
    reference = pd.read_csv(ch.V / "retrospective_2026-10-21" / "COHORT_ROWS.csv", keep_default_na=False)
    actual = current_rows[current_rows.n.between(601, 622)]
    assert len(actual) == 102 and actual.card.nunique() == 22
    a = actual.set_index(["card", "contract"])
    for r in reference.to_dict("records"):
        row = a.loc[(r["canonical_id"], r["contract"])]
        assert row["rank"] == (int(r["rank"]) if r["cohort"] == "ANALYST_PRIMARY_V1" and str(r["rank"]).isdigit() else 0)
        assert row.grade == r["grade"] and row.cohort == r["cohort"]
        assert row.date == r["event_date"] and row.week == r["iso_week"]
        assert row.effective_revision == r["effective_revision"]
        assert row.evidence.startswith(r["evidence"])  # keep the source's literal "R1 package" wording
        assert row.p == pytest.approx(float(r["p"])) if r["p"] else math.isnan(row.p)
        assert row.baseline == pytest.approx(float(r["baseline_p"])) if r["baseline_p"] else math.isnan(row.baseline)


def test_current_primary_counts_and_research_exclusion(current_rows):
    current_rows = current_rows[current_rows.n.between(601, 622)]  # future cohorts must not change this fixture
    summary = ch.cohort_summary(current_rows).set_index("cohort")
    primary = summary.loc["ANALYST_PRIMARY_V1"]
    assert (primary.cards, primary.rows, primary.primary_slots) == (11, 50, 22)
    assert (primary.wins, primary.losses, primary.pushes, primary.decisive_scored) == (11, 10, 1, 21)
    assert primary.primary_brier == pytest.approx(0.204092523809524)
    assert primary.baseline_rows == 8
    research = current_rows[current_rows.cohort == "RESEARCH_ONLY_NOT_PRIMARY"]
    assert len(research) == 52 and not research.counted_slot.any()
    without = current_rows[current_rows.cohort != "RESEARCH_ONLY_NOT_PRIMARY"]
    assert ch.calibration_table(current_rows)[1]["rows"] == ch.calibration_table(without)[1]["rows"]


def test_refreshed_rank_log_does_not_duplicate_cards(tmp_path):
    rank_log = pd.read_csv(ch.RANK_LOG, dtype=str).fillna("")
    row = rank_log.iloc[0].to_dict()
    row.update(card_id="P-999", rank="1", selection_or_contract="Under 200.5", logged_result="WIN", stated_p="0.7")
    refreshed = tmp_path / "rank.csv"
    pd.concat([rank_log, pd.DataFrame([row])]).to_csv(refreshed, index=False)
    source = local_inventory(tmp_path / "EFFECTIVE_SETTLEMENT_ROWS.csv")
    result, _ = ch.build_rows(refreshed, inventories=[source])
    assert len(result[result.card == "P-999"]) == 1
    assert result[result.card == "P-999"].cohort.iloc[0] == "ANALYST_PRIMARY_V1"
