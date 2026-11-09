"""Do not merge tied tiers or live views into a new prediction, or admit no-trial wins."""
import csv
import hashlib

import pandas as pd
import pytest

from ml import historical_views as hv
from ml.evaluation import card_history as ch


def write(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def example(tmp_path):
    old = pd.DataFrame([dict(card='P-999', rank=2, contract='Under 3.5 / Over 3.5',
                             event='EXAMPLE', grade='CONFLICT', p=float('nan'), q=float('nan'))])
    text = '| 2= | Under 3.5 | PASS | 2 | WIN |\n| 2= | Over 3.5 | PASS | 2 | LOSS |\n'
    source = tmp_path / 'original.md'
    source.write_bytes(text.encode())
    rows = []
    for number, line in enumerate(text.splitlines(), 1):
        cells = [c.strip() for c in line.strip('|').split('|')]
        rows.append(dict(canonical_id='P-999', view_id='P-999/ORIGINAL', contract_id='C'+str(number),
                         rank_label='2=', contract=cells[1], grade=cells[4], issued_verdict='PASS',
                         historical_eligibility='ABSTENTION_NO_FORMAL_SELECTION', cohort='LEGACY_ABSTENTION_NOT_PRIMARY',
                         source_path='original.md', source_prefix_bytes=len(text.encode()),
                         source_prefix_sha256=hashlib.sha256(text.encode()).hexdigest(), line_number=number,
                         line_sha256=hashlib.sha256(line.encode()).hexdigest(), row_literal=line,
                         rank_column=0, contract_column=1, grade_column=4))
    guards, registry = hv.input_paths(tmp_path)
    write(guards, [dict(canonical_id='P-999', aggregate_sha256=hv.aggregate_digest(old))])
    write(registry, rows)
    return old, source, guards, registry, rows


def test_tied_contracts_are_distinct_and_diagnostic(tmp_path):
    old, source, guards, registry, rows = example(tmp_path)
    result = hv.apply(old, tmp_path)
    assert list(result.grade) == ['WIN', 'LOSS']
    assert list(result['rank']) == [2, 2] and result.rank_tied.all()
    assert result.contract_id.nunique() == 2 and result.p.isna().all()
    assert ch.analysis_rows(result).empty


@pytest.mark.parametrize('failure', ['source', 'aggregate', 'grade', 'duplicate', 'primary', 'line'])
def test_changed_or_misbound_sources_cannot_close_a_reporting_conflict(tmp_path, failure):
    old, source, guards, registry, rows = example(tmp_path)
    if failure == 'source':
        source.write_bytes(source.read_bytes().replace(b'WIN', b'LOSS'))
    elif failure == 'aggregate':
        old.loc[0, 'contract'] = 'Different selection'
    elif failure == 'grade':
        rows[0]['grade'] = 'LOSS'
    elif failure == 'duplicate':
        rows[1]['contract_id'] = rows[0]['contract_id']
    elif failure == 'primary':
        rows[0]['cohort'] = 'ANALYST_PRIMARY_V1'
    elif failure == 'line':
        rows[0]['line_number'] = 0
    write(registry, rows)
    with pytest.raises(hv.HistoricalViewError):
        hv.apply(old, tmp_path)


def test_numeric_forecast_is_never_erased_by_view_recovery(tmp_path):
    old, source, guards, registry, rows = example(tmp_path)
    old.loc[0, 'p'] = .8
    write(guards, [dict(canonical_id='P-999', aggregate_sha256=hv.aggregate_digest(old))])
    with pytest.raises(hv.HistoricalViewError, match='HAS_PROBABILITY'):
        hv.apply(old, tmp_path)


def test_no_trial_and_missing_contract_wins_cannot_enter_hit_rates():
    rows = pd.DataFrame([
        dict(card='P-997', rank=1, y=1., p=.9, cohort='RANK_LOG_LITERAL', record_disposition='NOT_SCORABLE_OR_MISSING_PROPOSITION'),
        dict(card='P-998', rank=1, y=1., p=.9, cohort='RANK_LOG_LITERAL', record_disposition='NOT_SCORABLE_NO_ACTION'),
        dict(card='P-999', rank=1, y=0., p=.6, cohort='ANALYST_PRIMARY_V1', record_disposition='RETAINED_CONTRACT')])
    rows['informational_r2'] = False
    eligible = ch.analysis_rows(rows)
    assert list(eligible.card) == ['P-999']
    assert ch.calibration_table(rows)[1]['rows'] == 1
    assert ch.slot_table(rows).iloc[0]['cards'] == 1
