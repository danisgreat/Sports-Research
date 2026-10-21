"""Strict log execution: actual fits without a registered baseline, failures and delayed feedback."""
import pytest

from ml import primary as p
from ml.execution import MANIFEST_FIELDS, execute_files, verify_execution, verify_log
from ml.tests.test_primary import inputs
from ml.tests.test_web_history import source_row


def files(inputs):
    req, _, history, contracts, tmp, _ = inputs
    for row in history:
        row['source_kind'] = 'WEB_RECOVERED'
    for name, rows in [('request', [req]), ('history', history), ('contracts', contracts), ('source', [source_row(inputs)])]:
        # Actual Windows-style source bytes need not equal normalized bundle bytes.
        (tmp / (name + '.csv')).write_bytes(p.csv_bytes(rows).replace(b'\n', b'\r\n'))
    return dict(request=tmp/'request.csv', history=tmp/'history.csv', contracts=tmp/'contracts.csv',
                competition_source=tmp/'source.csv', out=tmp/'attempt')


def manifest(inputs, rec, status=None, feedback=None, card_status=None):
    tmp = inputs[4]
    row = dict.fromkeys(MANIFEST_FIELDS, '')
    row.update(card_id='P-900001', event_id=rec['event_id'], competition=rec['competition'], endpoint=rec['endpoint'],
               execution_path='attempt', execution_sha256=p.digest((tmp/'attempt'/'EXECUTION.csv').read_bytes()),
               feedback_status=status or ('PENDING_EVENT' if rec['status']=='EXECUTED' else 'NOT_APPLICABLE_NO_MODEL'),
               reason='EXAMPLE synthetic fixture; pending event or actual failure, not sports evidence')
    if feedback:
        row.update(feedback_path=str(feedback), feedback_sha256=p.digest(feedback.read_bytes()))
    (tmp/'manifest.csv').write_bytes(p.csv_bytes([row]))
    body = card_status or ('MODEL_ASSISTED_PRIMARY_V3' if rec['status']=='EXECUTED' else 'NO_FORECAST')
    (tmp/'mini.md').write_text(
        '<!-- MINI-LOG-FORMAT: mini-log-8 -->\n<!-- BEGIN CARD P-900001 -->\n- **Analysis status:** ' + body + '\n' +
        f"- **ML execution identity:** {rec['event_id']} | {rec['competition']} | {rec['endpoint']}\n" +
        '<!-- END CARD P-900001 -->\n', encoding='utf-8')
    return tmp/'manifest.csv', tmp/'mini.md'


def test_real_fit_and_hedge_without_archive_or_registered_baseline(inputs, monkeypatch):
    kwargs = files(inputs)
    def no_archive(*args):
        raise AssertionError('reviewed new competition must not need archive/baseline discovery')
    monkeypatch.setattr(p, 'get_league', no_archive)
    rec = execute_files(**kwargs)
    assert rec['status']=='EXECUTED' and rec['baseline_status']=='FITTED_FROM_HISTORY'
    assert verify_execution(kwargs['out'])['status']=='EXECUTED'
    model = p.verify_bundle(kwargs['out']/'BUNDLE')
    assert model['warm_start_games']!='0'
    assert set(p._parse_vector(model['mixture_weights']))==set(p.ARMS)
    assert all(0 <= float(r['baseline_p']) <= 1 for r in p.read_rows(kwargs['out']/'BUNDLE'/'PREDICTIONS.csv'))
    paths = manifest(inputs, rec)
    assert verify_log(*paths)==dict(cards=1, executed=1, failed=0, feedback_retained=0, research_only=0)
    with pytest.raises(FileExistsError):
        execute_files(**kwargs)


@pytest.mark.parametrize('defect', ['unknown_competition', 'unsupported', 'missing_history', 'future_history'])
def test_actual_rejections_retain_failure_receipt(inputs, monkeypatch, defect):
    kwargs = files(inputs)
    if defect=='unknown_competition':
        kwargs['competition_source']=None
        def missing(*args):raise KeyError('EXAMPLE no archive route')
        monkeypatch.setattr(p, 'get_league', missing)
    if defect=='unsupported':
        rows=p.read_rows(kwargs['competition_source']);rows[0]['sport']='Tennis'
        kwargs['competition_source'].write_bytes(p.csv_bytes(rows))
        request=p.read_rows(kwargs['request']);request[0]['competition']='Tennis/EXAMPLE'
        kwargs['request'].write_bytes(p.csv_bytes(request))
    if defect=='missing_history':kwargs['history']=inputs[4]/'missing.csv'
    if defect=='future_history':
        rows=p.read_rows(kwargs['history']);rows[0]['available_at']='2030-01-01T00:00:00Z'
        kwargs['history'].write_bytes(p.csv_bytes(rows))
    rec=execute_files(**kwargs)
    assert rec['status']=='FAILED' and rec['error_type'] and rec['error']
    if defect=='unsupported':assert 'unsupported sport engine' in rec['error']
    assert not (kwargs['out']/'BUNDLE').exists()
    assert verify_execution(kwargs['out'])['status']=='FAILED'
    assert verify_log(*manifest(inputs, rec))['failed']==1
    with pytest.raises(p.AdmissionError, match='numeric primary'):
        verify_log(*manifest(inputs, rec, card_status='MODEL_ASSISTED_PRIMARY_V3'))


def test_feedback_is_recomputed_and_missing_baseline_profile_does_not_skip_learning(inputs):
    kwargs=files(inputs);rec=execute_files(**kwargs)
    tmp=inputs[4];capture=inputs[5]
    feedback=p.settle(kwargs['out']/'BUNDLE',110,95,'2023-01-01T13:00:00Z','2023-01-01T14:00:00Z',
                      capture,p.digest(capture.read_bytes()))
    path=tmp/'feedback.csv';path.write_bytes(p.csv_bytes([feedback]))
    paths=manifest(inputs,rec,status='FEEDBACK_RETAINED',feedback=path)
    assert verify_log(*paths)['feedback_retained']==1
    req=p.read_rows(kwargs['request'])[0]
    req.update(event_id='EXAMPLE-PRIMARY-2',scheduled_start='2023-01-02T11:00:00Z',
               issue_at='2023-01-02T10:00:00Z',actual_start='2023-01-02T11:00:00Z')
    kwargs['request'].write_bytes(p.csv_bytes([req]))
    next_kwargs=dict(kwargs,out=tmp/'next_attempt',feedback=path)
    assert execute_files(**next_kwargs)['status']=='EXECUTED'
    next_model=p.verify_bundle(tmp/'next_attempt'/'BUNDLE')
    assert next_model['feedback_events']=='1'
    assert verify_execution(tmp/'next_attempt')['status']=='EXECUTED'
    feedback['loss_'+p.ARMS[0]]=1.0
    path.write_bytes(p.csv_bytes([feedback]))
    paths=manifest(inputs,rec,status='FEEDBACK_RETAINED',feedback=path)
    with pytest.raises(p.AdmissionError,match='loss differs'):verify_log(*paths)


@pytest.mark.parametrize('defect',['missing','duplicate','wrong_identity','tampered','no_reason','fake_feedback','header'])
def test_manifest_cannot_skip_mismatch_or_fabricate_execution(inputs,defect):
    kwargs=files(inputs);rec=execute_files(**kwargs)
    path,mini=manifest(inputs,rec)
    rows=p.read_rows(path)
    if defect=='missing':rows=[]
    if defect=='duplicate':rows.append(rows[0])
    if defect=='wrong_identity':rows[0]['event_id']='OTHER'
    if defect=='tampered':rows[0]['execution_sha256']='0'*64
    if defect=='no_reason':rows[0]['reason']=''
    if defect=='fake_feedback':rows[0]['feedback_path']='fake.csv'
    path.write_bytes(p.csv_bytes(rows) if rows else (','.join(MANIFEST_FIELDS)+'\n').encode())
    if defect=='header':path.write_text('invented_header\n',encoding='utf-8')
    with pytest.raises(p.AdmissionError):verify_log(path,mini)


def test_comparator_fit_failure_is_attempted_and_never_replaced_with_invented_baseline(inputs,monkeypatch):
    from ml.models.common import FitError
    def failed_baseline(*args):raise FitError('EXAMPLE exact-competition comparator cannot be fitted')
    monkeypatch.setattr(p.LeagueBaseline,'fit',failed_baseline)
    kwargs=files(inputs)
    rec=execute_files(**kwargs)
    assert rec['status']=='FAILED' and rec['stage']=='PRIMARY_PIPELINE'
    assert rec['error_type']=='FitError' and 'comparator' in rec['error']
    assert verify_execution(kwargs['out'])['baseline_status']=='NO_RESULT'
    assert not (kwargs['out']/'BUNDLE').exists()


def test_failed_cli_exits_nonzero_and_keeps_attempt(inputs):
    kwargs=files(inputs);kwargs['history'].unlink()
    args=['execute']
    for key,value in kwargs.items():args.extend(['--'+key.replace('_','-'),str(value)])
    with pytest.raises(SystemExit) as exc:p.main(args)
    assert exc.value.code==1
    assert verify_execution(kwargs['out'])['status']=='FAILED'


def test_empty_new_mini_passes_but_interrupted_attempt_and_legacy_are_not_upgraded(tmp_path):
    mini=tmp_path/'mini.md';manifest_path=tmp_path/'manifest.csv'
    mini.write_text('<!-- MINI-LOG-FORMAT: mini-log-8 -->\n',encoding='utf-8')
    manifest_path.write_text(','.join(MANIFEST_FIELDS)+'\n',encoding='utf-8')
    assert verify_log(manifest_path,mini)['cards']==0
    mini.write_text('<!-- MINI-LOG-FORMAT: mini-log-7 -->\n',encoding='utf-8')
    with pytest.raises(p.AdmissionError,match='legacy'):verify_log(manifest_path,mini)
    with pytest.raises(FileNotFoundError):verify_execution(tmp_path)


@pytest.mark.parametrize('reason', ['NOT_RUN_CAPABILITY_BLOCKED: No module named ml',
                                    'NOT_IMPLEMENTED: no exact sport adapter',
                                    'NOT_RUN_DATA_UNAVAILABLE: reviewed history missing'])
def test_research_card_retained_without_model_receipt_or_probability(tmp_path, reason):
    mini=tmp_path/'mini.md';path=tmp_path/'manifest.csv'
    mini.write_text('<!-- MINI-LOG-FORMAT: mini-log-9 -->\n<!-- BEGIN CARD P-900002 -->\n'
                    '- **Analysis status:** RESEARCH_ONLY_NO_MODEL\n'
                    '- **ML execution identity:** EXAMPLE-RESEARCH | Ice Hockey/EXAMPLE | FULL_GAME\n'
                    '- **Model p_card:** NOT_ESTIMATED\n'
                    '<!-- END CARD P-900002 -->\n',encoding='utf-8')
    row=dict.fromkeys(MANIFEST_FIELDS,'')
    row.update(card_id='P-900002',event_id='EXAMPLE-RESEARCH',competition='Ice Hockey/EXAMPLE',endpoint='FULL_GAME',
               feedback_status='NOT_APPLICABLE_NO_MODEL',reason=reason)
    path.write_bytes(p.csv_bytes([row]))
    result=verify_log(path,mini)
    assert result==dict(cards=1,executed=0,failed=0,feedback_retained=0,research_only=1)
    # Identical evidence cannot claim a model prediction or fabricated expert-loss feedback.
    mini.write_text(mini.read_text(encoding='utf-8').replace('RESEARCH_ONLY_NO_MODEL','MODEL_ASSISTED_PRIMARY_V3'),encoding='utf-8')
    with pytest.raises(p.AdmissionError,match='numeric primary'):verify_log(path,mini)
    mini.write_text(mini.read_text(encoding='utf-8').replace('MODEL_ASSISTED_PRIMARY_V3','RESEARCH_ONLY_NO_MODEL'),encoding='utf-8')
    row['feedback_status']='FEEDBACK_RETAINED';path.write_bytes(p.csv_bytes([row]))
    with pytest.raises(p.AdmissionError,match='invented expert feedback'):verify_log(path,mini)


def test_no_code_analyst_mini_verifies_without_a_manifest(tmp_path):
    """MLSCOPE-v1: a prompt-1 mini priced by hand has no execution manifest and claims no model."""
    mini=tmp_path/'mini.md'
    cards=[('LOCAL-EXAMPLE-G0001','ANALYST_PRIMARY_V1'),('LOCAL-EXAMPLE-G0002','UNCALIBRATED_QUALITATIVE')]
    mini.write_text('<!-- MINI-LOG-FORMAT: mini-log-10 -->\n'+''.join(
        f'<!-- BEGIN CARD {k} -->\n- **Analysis status:** {s} / EXAMPLE\n<!-- END CARD {k} -->\n' for k,s in cards),encoding='utf-8')
    assert verify_log(None,mini)==dict(cards=2,analyst_primary=1,qualitative_or_no_forecast=1)
    assert p.main(['verify-log','--mini',str(mini)]) is None
    # The status may be written as code; a backtick-wrapped NOT_A_STATUS is still refused below.
    mini.write_text(mini.read_text(encoding='utf-8').replace('** ANALYST_PRIMARY_V1 /','** `ANALYST_PRIMARY_V1 /'),encoding='utf-8')
    assert verify_log(None,mini)['analyst_primary']==1
    bad=tmp_path/'bad.md'
    bad.write_text(mini.read_text(encoding='utf-8').replace('`ANALYST_PRIMARY_V1','`NOT_A_STATUS'),encoding='utf-8')
    with pytest.raises(p.AdmissionError,match='hand-derived'):verify_log(None,bad)
    # A model claim without its manifest, or a card without a disposition, is refused.
    mini.write_text(mini.read_text(encoding='utf-8').replace('ANALYST_PRIMARY_V1','MODEL_ASSISTED_CYCLE_V1'),encoding='utf-8')
    with pytest.raises(p.AdmissionError,match='hand-derived'):verify_log(None,mini)
    mini.write_text('<!-- MINI-LOG-FORMAT: mini-log-10 -->\n<!-- BEGIN CARD LOCAL-EXAMPLE-G0001 -->\n<!-- END CARD LOCAL-EXAMPLE-G0001 -->\n',encoding='utf-8')
    with pytest.raises(p.AdmissionError,match='hand-derived'):verify_log(None,mini)


def test_analyst_card_in_a_legacy_manifest_mini_needs_no_execution(tmp_path):
    mini=tmp_path/'mini.md';path=tmp_path/'manifest.csv'
    mini.write_text('<!-- MINI-LOG-FORMAT: mini-log-10 -->\n<!-- BEGIN CARD LOCAL-EXAMPLE-G0003 -->\n'
                    '- **Analysis status:** ANALYST_PRIMARY_V1\n'
                    '- **ML execution identity:** EXAMPLE-ANALYST | Basketball/EXAMPLE | FULL_GAME\n'
                    '<!-- END CARD LOCAL-EXAMPLE-G0003 -->\n',encoding='utf-8')
    row=dict.fromkeys(MANIFEST_FIELDS,'')
    row.update(card_id='LOCAL-EXAMPLE-G0003',event_id='EXAMPLE-ANALYST',competition='Basketball/EXAMPLE',endpoint='FULL_GAME',
               feedback_status='NOT_APPLICABLE_NO_MODEL',reason='MLSCOPE-v1: priced by hand, no model')
    path.write_bytes(p.csv_bytes([row]))
    assert verify_log(path,mini)['research_only']==1
