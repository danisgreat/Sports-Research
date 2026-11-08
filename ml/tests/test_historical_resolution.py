"""Historical corrections require exact source custody and event/contract parent chains."""
import csv
import hashlib

import pandas as pd
import pytest

from ml import historical_resolution as H
from ml.evaluation import effective_settlement as E, card_history as C


def write(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('w', encoding='utf8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=rows[0]); w.writeheader(); w.writerows(rows)


def binding(root):
    body = b'## P-900 - Event A\n'
    (root / 'source.md').write_bytes(body)
    r = dict(alias_id='P-900', canonical_id='P-901', event_key='EVENT-A', source_path='source.md',
             source_prefix_bytes=len(body), source_prefix_sha256=H._sha(body), line_number=1,
             heading_sha256=H._sha(body.rstrip(b'\n')))
    write(H.input_paths(root)[0], [r])
    return r, dict(source_path='source.md', line_number=1, alias_id='P-900', heading_sha256=r['heading_sha256'])


def test_only_fully_bound_aliases_resolve_and_appended_unknown_occurrences_reopen(tmp_path):
    r, observation = binding(tmp_path)
    assert H.resolved_aliases([observation], tmp_path) == {'P-900'}
    assert H.resolved_aliases([observation, dict(observation, line_number=3)], tmp_path) == set()
    with (tmp_path / 'source.md').open('ab') as f: f.write(b'new unrelated suffix\n')
    assert H.resolved_aliases([observation], tmp_path) == {'P-900'}  # old prefix intact


def test_tampered_identity_prefix_is_refused(tmp_path):
    _, observation = binding(tmp_path)
    (tmp_path / 'source.md').write_text('changed')
    with pytest.raises(H.HistoricalResolutionError, match='SOURCE_CHANGED'):
        H.resolved_aliases([observation], tmp_path)


def test_contract_recovery_does_not_create_a_probability_or_grade(tmp_path):
    text = '| 1 | Home Over 4.5 corners |\n'
    (tmp_path / 'source.md').write_bytes(text.encode())
    row = dict(canonical_id='P-900', rank='1', contract='Home Over 4.5 corners', source_path='source.md',
               start_line=1, end_line=1, block_sha256=H._sha(text.encode()), row_literal=text.strip())
    write(H.input_paths(tmp_path)[1], [row])
    frame = pd.DataFrame([dict(card='P-900', rank=1, contract='', grade='UNRESOLVED', p=float('nan'))])
    out = H.recover_contracts(frame, tmp_path)
    assert out.iloc[0].contract == row['contract'] and out.iloc[0].grade == 'UNRESOLVED' and pd.isna(out.iloc[0].p)
    row['contract'] = 'Away Over 4.5 corners'; write(H.input_paths(tmp_path)[1], [row])
    with pytest.raises(H.HistoricalResolutionError, match='NOT_LITERAL'):
        H.recover_contracts(frame, tmp_path)


def test_historical_revision_preserves_probability_and_refuses_wrong_prior(tmp_path):
    (tmp_path / 'revision.md').write_text('reviewed result')
    row = dict(canonical_id='P-900', rank='1', contract='Home Over 4.5 corners', prior_grade='UNRESOLVED',
               sporting_grade='LOSS', evidence_class='B', revision='revision-1', parent_revision='BASE',
               effective_at='2026-11-09T10:00:00+11:00', source_document='revision.md',
               source_document_sha256=H._sha((tmp_path / 'revision.md').read_bytes()))
    write(H.input_paths(tmp_path)[2], [row])
    frame = pd.DataFrame([dict(card='P-900', rank=1, contract=row['contract'], grade='UNRESOLVED', p=.7)])
    out = H.apply_row_revisions(frame, tmp_path)
    assert out.iloc[0].grade == 'LOSS' and out.iloc[0].p == .7
    with pytest.raises(H.HistoricalResolutionError, match='PRIOR_GRADE'):
        H.apply_row_revisions(out, tmp_path)


def test_legacy_layout_enters_the_same_validated_effective_revision_view(tmp_path):
    original = tmp_path / E.V / 'mini_import_EX' / 'EFFECTIVE_SETTLEMENT_ROWS.csv'
    write(original, [dict(event_id='P-900', key='P-900-SUPPLIED-01', revision_id='P-900-SETTLEMENT-R1-20261016',
                          original_contract='Home -8.5 ML', original_rank_type='ANALYST_ONLY', sporting_grade='UNRESOLVED',
                          source_evidence_class='X', event='H v A', original_analyst_p='')])
    (tmp_path / 'revision.md').write_text('owner chose handicap; actual margin3')
    row = dict(canonical_id='P-900', local_key='P-900-SUPPLIED-01', original_rank='ANALYST_ONLY',
               original_contract='Home -8.5 ML', revision='revision-2', parent_revision='revision-1', sporting_grade='LOSS',
               evidence_class='B', effective_at='2026-11-09T10:00:00+11:00', source_document='revision.md', note='')
    write(tmp_path / E.V / 'settlement_import_EX' / 'SETTLEMENT_REVISIONS.csv', [row])
    result = E.effective_rows(tmp_path).iloc[0]
    assert result.sporting_grade == 'LOSS' and result.local_key == 'P-900-SUPPLIED-01'
    assert result.revision_chain == 'revision-1 > revision-2' and not E.unmatched_revisions(tmp_path)


def test_legacy_normalization_refuses_unversioned_or_duplicated_source_keys():
    r = dict(event_id='P-900', key='K', revision_id='unspecified', original_contract='C', original_rank_type='ANALYST_ONLY', sporting_grade='WIN')
    with pytest.raises(E.RevisionError, match='LEGACY_REVISION_ID'):
        E.normalize_inventory(pd.DataFrame([r]))
    r['revision_id'] = 'P-900-SETTLEMENT-R1-20261016'
    with pytest.raises(E.RevisionError, match='LEGACY_REVISION_ID'):
        E.normalize_inventory(pd.DataFrame([r, r]))


def test_qualitative_historical_import_preserves_rank_without_primary_eligibility(tmp_path):
    path = tmp_path / 'EFFECTIVE_SETTLEMENT_ROWS.csv'
    write(path, [dict(canonical_id='P-900', local_key='LOCAL-HIST-G0001',
                     probability_role='ANALYST_NOT_PRIMARY (UNCALIBRATED_QUALITATIVE)', original_rank='2',
                     original_contract='Under 165.5', original_probability='', sporting_grade='LOSS',
                     effective_revision='revision-1', evidence_class='A', note='No numeric primary forecast')])
    row = C.inventory_rows(path)[0]
    assert row['rank'] == 2 and row['cohort'] == 'RESEARCH_ONLY_NOT_PRIMARY' and pd.isna(row['p'])


def test_event_date_correction_is_bound_to_reviewed_evidence(tmp_path):
    (tmp_path / 'date.md').write_bytes(b'Game 4 September; imported 9 November')
    write(H.input_paths(tmp_path)[3], [dict(canonical_id='P-900', event_date='2026-09-04',
          date_basis='OFFICIAL_MATCH_DATE_UTC', source_document='date.md',
          source_document_sha256=H._sha((tmp_path / 'date.md').read_bytes()))])
    assert H.event_dates(tmp_path)['P-900'] == ('2026-09-04', 'VERIFIED_EVENT_DATE:OFFICIAL_MATCH_DATE_UTC')
    (tmp_path / 'date.md').write_bytes(b'Changed to import date')
    with pytest.raises(H.HistoricalResolutionError, match='EVIDENCE_CHANGED'):
        H.event_dates(tmp_path)
