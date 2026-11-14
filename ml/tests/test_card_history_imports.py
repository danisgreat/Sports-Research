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
    # SETTLE-VIEW-v1: later settlement revisions apply on top of the preserved 2026-10-21 rows, and only to their own keys.
    from ml.evaluation import effective_settlement as es
    revised = {}
    for path in es.revision_files():
        for v in es.read_revisions(path).to_dict("records"):
            revised[(v["canonical_id"], v["original_contract"])] = v
    assert len([k for k in revised if 601 <= int(k[0][2:]) <= 622]) == 12
    for r in reference.to_dict("records"):
        row = a.loc[(r["canonical_id"], r["contract"])]
        v = revised.get((r["canonical_id"], r["contract"]))
        assert row["rank"] == (int(r["rank"]) if r["cohort"] == "ANALYST_PRIMARY_V1" and str(r["rank"]).isdigit() else 0)
        assert row.grade == (v["sporting_grade"] if v else r["grade"]) and row.cohort == r["cohort"]
        assert row.date == r["event_date"] and row.week == r["iso_week"]
        assert row.effective_revision == (v["revision"] if v else r["effective_revision"])
        assert row.evidence.startswith(v["evidence_class"] if v else r["evidence"])  # keep the source's literal "R1 package" wording
        assert row.p == pytest.approx(float(r["p"])) if r["p"] else math.isnan(row.p)
        assert row.baseline == pytest.approx(float(r["baseline_p"])) if r["baseline_p"] else math.isnan(row.baseline)


def test_revised_legacy_rows_override_existing_rank_log_without_becoming_primary(current_rows):
    from ml.evaluation import effective_settlement as es
    effective = es.effective_rows()
    for cid in ("P-596", "P-598"):
        original = effective[(effective.canonical_id == cid) & (effective.revision_source != "")].iloc[0]
        row = current_rows[(current_rows.card == cid) & (current_rows.contract == original.original_contract)].iloc[0]
        assert row.grade == original.sporting_grade == "LOSS"
        assert row.effective_revision == "revision-2" and row.literal_grade == "UNRESOLVED"
        assert row.cohort == "LEGACY_ANALYST_NOT_PRIMARY" and not row.counted_slot


def test_owner_closed_nine_corner_rows_are_terminal_and_excluded_from_scores(current_rows):
    registry = pd.read_csv(ch.ROOT / 'research/historical_resolution/PERMANENT_CLOSURES.csv', dtype=str)
    keys = set(zip(registry.canonical_id, registry['rank']))
    closed = current_rows[[ (r.card, str(r['rank'])) in keys for _, r in current_rows.iterrows() ]]
    assert len(closed) == 9 and closed.card.nunique() == 8
    assert closed.y.isna().all() and not closed.counted_slot.any()
    assert set(closed.record_disposition) == {"CLOSED_UNATTAINABLE_DO_NOT_RETRY"}
    assert (closed[closed.card == "P-630"].literal_grade == "UNRESOLVED").all()
    # The 9 Nov 2026 closure emptied the queue for every card up to P-638; later imports may carry genuinely
    # unresolved rows (P-647 corners, CR-2026.11.14-R1), which must stay UNRESOLVED and listed in their import queue.
    historical = current_rows.card.str.extract(r"P-(\d+)", expand=False).astype(float) <= 638
    assert not ((current_rows.grade == "UNRESOLVED") & (current_rows.record_disposition == "RETAINED_CONTRACT") & historical).any()
    later = current_rows[(current_rows.grade == "UNRESOLVED") & ~historical]
    assert set(later.card) <= {"P-647"} and len(later) == 3
    original = pd.read_csv(ch.V / "historical_resolution_2026-11-09-1/final_history/CARD_ROWS.csv", dtype=str, keep_default_na=False)
    old = original[original.card.isin(["P-126", "P-418"])].copy()
    old.loc[(old.card == 'P-126') & old['rank'].isin(['2', '4']), 'grade'] = 'UNATTAINABLE'
    now = current_rows[current_rows.card.isin(["P-126", "P-418"])]
    assert {(r.card, str(r['rank']), r.contract if pd.notna(r.contract) else '', r.grade) for _, r in now.iterrows()} == {
        (r.card, r['rank'], r.contract, r.grade) for _, r in old.iterrows()}


def test_new_missing_field_closures_and_recovered_contracts_remain_nonprospective(current_rows):
    new = current_rows[(current_rows.card.eq('P-126') & current_rows['rank'].isin([2, 4])) |
                       (current_rows.card.eq('P-537') & current_rows['rank'].eq(4))]
    assert len(new) == 3 and set(new.grade) == {'UNATTAINABLE'}
    assert set(new.literal_grade) == {'VOID'} and not new.counted_slot.any() and new.y.isna().all()
    recovered = pd.read_csv(ch.ROOT / 'research/verification/historical_gap_resolution_2026-11-09-1/RECOVERED_PROPOSITIONS.csv', dtype=str)
    assert len(recovered) == 54
    for r in recovered.itertuples():
        row = current_rows[(current_rows.card == r.canonical_id) & (current_rows['rank'] == int(r.rank))].iloc[0]
        assert row.contract == r.contract and row.contract_recovery_source
        if r.canonical_id in {'P-306', 'P-509', 'P-517'}:
            assert row.cohort == 'LEGACY_ANALYST_NOT_PRIMARY' and not row.counted_slot
    excluded = current_rows[current_rows.grade.isin(['WIN', 'LOSS']) &
                            current_rows.record_disposition.eq('NOT_SCORABLE_OR_MISSING_PROPOSITION')]
    assert len(excluded) == 4 and set(excluded.card) == {'P-157'}
    learning_only = current_rows[current_rows.card.eq('P-509')]
    assert len(learning_only) == 4 and set(learning_only.cohort) == {'LEGACY_ANALYST_NOT_PRIMARY'}
    assert not learning_only.counted_slot.any()


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
