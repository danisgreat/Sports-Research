"""The legacy calibration command must share grades, exclusions and complete receipts."""
import pandas as pd
import pytest

from ml.evaluation import card_calibration as calibration, card_history, writers
from ml import run


def test_calibration_refuses_a_revision_without_an_imported_target(monkeypatch):
    from ml.evaluation import effective_settlement
    monkeypatch.setattr(effective_settlement, 'unmatched_revisions', lambda root: ['missing-target'])
    with pytest.raises(ValueError, match='match no imported row'):
        calibration.load_rows()


def test_calibration_uses_effective_grades_and_never_admits_diagnostics_or_no_trials(monkeypatch):
    rows = pd.DataFrame([
        dict(card='P-991', rank=1, p=.8, grade='WIN', cohort='RANK_LOG_LITERAL', record_disposition='RETAINED_CONTRACT'),
        dict(card='P-992', rank=1, p=.6, grade='LOSS', cohort='ANALYST_PRIMARY_V1', record_disposition='RETAINED_CONTRACT'),
        dict(card='P-993', rank=1, p=.9, grade='WIN', cohort='RESEARCH_ONLY_NOT_PRIMARY', record_disposition='RETAINED_CONTRACT'),
        dict(card='P-994', rank=1, p=.9, grade='WIN', cohort='RANK_LOG_LITERAL', record_disposition='NOT_SCORABLE_OR_MISSING_PROPOSITION'),
        dict(card='P-995', rank=1, p=.9, grade='UNATTAINABLE', cohort='RANK_LOG_LITERAL', record_disposition='CLOSED_UNATTAINABLE_DO_NOT_RETRY')])
    monkeypatch.setattr(card_history, 'build_rows', lambda path: (rows.copy(), pd.DataFrame()))
    result, info = calibration.load_rows()
    assert list(result.card_id) == ['P-991', 'P-992'] and list(result.y) == [1., 0.]
    assert info['source'] == 'EFFECTIVE_HISTORY_VIEW' and info['excluded_numeric_rows'] == 3


@pytest.mark.parametrize('change', ['evidence', 'discovery', 'none'])
def test_calibration_receipt_covers_corrections_and_input_discovery(tmp_path, monkeypatch, change):
    rank, correction = tmp_path / 'rank.csv', tmp_path / 'correction.csv'
    rank.write_text('rank'); correction.write_text('correction')
    added = []
    monkeypatch.setattr(calibration, 'RANK_LOG', rank)
    monkeypatch.setattr(card_history, 'reporting_inputs', lambda path: [rank, correction] + added)
    monkeypatch.setattr(run, 'receipt_base', lambda: {'code_sha256': 'fixed'})
    monkeypatch.setattr(run, 'code_digest', lambda: 'fixed')
    written = []
    monkeypatch.setattr(writers, 'write_cards', lambda result, receipt: written.append(receipt))
    def audit():
        if change == 'evidence': correction.write_text('changed during read')
        if change == 'discovery': added.append(tmp_path / 'new_import.csv')
        return {}
    monkeypatch.setattr(calibration, 'audit', audit)
    if change == 'none':
        run.run_cards()
        assert len(written) == 1 and 'completed_utc' in written[0]
        assert 'input:EXTERNAL:correction.csv' in written[0]
    else:
        with pytest.raises(RuntimeError, match='changed during'):
            run.run_cards()
        assert not written
