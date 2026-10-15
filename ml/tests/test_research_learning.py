"""Research-only retention supports future labels without inventing old forecasts."""
from pathlib import Path

import pytest

from ml import primary as p
from ml.research_learning import LABEL_FIELDS, retain_candidate, verify_candidate


@pytest.fixture
def research(tmp_path):
    record=tmp_path/'card.md';settlement=tmp_path/'settlement.md';evidence=tmp_path/'source.txt'
    record.write_text('# P-900003 EXAMPLE research-only; model absent; not sporting evidence\n',encoding='utf-8')
    settlement.write_text('# P-900003 revision-1 EXAMPLE reviewed final\n',encoding='utf-8')
    evidence.write_text('SYNTHETIC count target 4; no actual event',encoding='utf-8')
    row=dict(zip(LABEL_FIELDS,['EXAMPLE-RESEARCH','Ice Hockey/EXAMPLE','FULL_GAME','HOME_GOALS','4','GOALS',
        '2026-01-01T10:00:00Z','2026-01-01T13:00:00Z','2026-01-01T14:00:00Z',
        'https://example.org/synthetic',str(evidence),p.digest(evidence.read_bytes()),
        'FROZEN_FRAMEWORK_CONVENTION','TERMINAL_LABEL_REVIEWED','revision-1','FEATURES_NOT_VERIFIED']))
    labels=tmp_path/'labels.csv';labels.write_bytes(p.csv_bytes([row]))
    return record,settlement,labels,tmp_path/'candidate',row


def test_missing_model_still_retains_real_settlement_labels_for_future_admission(research):
    record,settlement,labels,out,row=research
    rec=retain_candidate('P-900003',record,settlement,labels,out)
    assert rec['status']=='LABELS_RETAINED_NOT_MODEL_FEEDBACK' and rec['labels']==1
    assert verify_candidate(out)['card_id']=='P-900003'
    assert (out/'ORIGINAL_CARD.md').read_bytes()==record.read_bytes()
    assert (out/'SETTLEMENT.md').read_bytes()==settlement.read_bytes()
    with pytest.raises(FileExistsError):retain_candidate('P-900003',record,settlement,labels,out)
    feedback=dict(row,record_kind='RESEARCH_TRAINING_CANDIDATE')
    with pytest.raises(p.AdmissionError,match='not frozen expert feedback'):
        p.feedback_losses([feedback],'ANY','2026-01-02T00:00:00Z')
    with pytest.raises(p.AdmissionError,match='not frozen expert feedback'):
        p.feedback_losses([rec],'ANY','2026-01-02T00:00:00Z')


@pytest.mark.parametrize('defect',['unresolved','estimate','definition','future_final','future_label','duplicate','negative','hash','market','wrong_id','wrong_settlement'])
def test_reject_unverified_conflicting_or_fabricated_training_labels(research,defect):
    record,settlement,labels,out,row=research
    if defect=='unresolved':row.update(label_unit='OUTCOME',label_value='UNRESOLVED')
    if defect=='estimate':row['review_status']='ANALYST_ESTIMATE'
    if defect=='definition':row['definition_status']='UNKNOWN_DEFINITION'
    if defect=='future_final':row['final_at']='2027-01-01T13:00:00Z'
    if defect=='future_label':row.update(event_at='2099-01-01T10:00:00Z',final_at='2099-01-01T13:00:00Z',available_at='2099-01-01T14:00:00Z')
    if defect=='negative':row['label_value']='-1'
    if defect=='hash':row['evidence_sha256']='0'*64
    if defect=='market':row['odds']='2.0'
    if defect=='wrong_id':record.write_text('# P-900004 different original',encoding='utf-8')
    if defect=='wrong_settlement':settlement.write_text('# P-900004 different final',encoding='utf-8')
    labels.write_bytes(p.csv_bytes([row,row] if defect=='duplicate' else [row]))
    with pytest.raises((p.AdmissionError,ValueError)):retain_candidate('P-900003',record,settlement,labels,out)
    assert not out.exists()


def test_mutated_retained_candidate_fails_hash_check(research):
    record,settlement,labels,out,row=research
    retain_candidate('P-900003',record,settlement,labels,out)
    (out/'LABELS.csv').write_text('tampered',encoding='utf-8')
    with pytest.raises(p.AdmissionError,match='hash mismatch'):verify_candidate(out)
