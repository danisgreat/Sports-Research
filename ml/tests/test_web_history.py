"""Web-recovered history is usable without promoting broken/missing local archive data."""
from dataclasses import replace
import copy

import pytest

from ml.config import SPORT_RULES
from ml.primary import (AdmissionError, csv_bytes, digest, forecast, main, read_rows,
                        reviewed_source_league, verify_bundle)
from ml.tests.test_primary import inputs


def source_row(inputs, sport='Basketball'):
    rules=SPORT_RULES[sport]
    return dict(sport=sport, competition='EXAMPLE', endpoint=rules.get('endpoint','FULL_GAME'),
                tie_rule=rules.get('tie_rule','draw'), extra_fraction=str(.125 if sport=='Basketball' else rules.get('extra_fraction',0)),
                winner_bonus=str(rules.get('winner_bonus',1)), overs_cap=str(rules.get('overs_cap','')),
                source_url='https://example.org/synthetic-rules', available_at='2022-12-01T00:00:00Z',
                review_status='RESEARCH_INPUT_REVIEWED', evidence_path=str(inputs[5]),
                evidence_sha256=digest(inputs[5].read_bytes()), archive_disposition='MISSING', reason='EXAMPLE missing archive; synthetic fixture only')


@pytest.mark.parametrize('sport', list(SPORT_RULES))
def test_exact_source_route_across_registered_sports(inputs,sport):
    row=source_row(inputs,sport)
    request=dict(inputs[0],competition=sport+'/EXAMPLE',endpoint=row['endpoint'])
    if SPORT_RULES[sport]['engine'] not in ('gaussian','count','dixon_coles','cricket'):
        with pytest.raises(AdmissionError,match='unsupported sport engine'):
            reviewed_source_league(request,row)
    else:
        lg=reviewed_source_league(request,row)
        assert lg.path==request['competition'] and lg.engine==SPORT_RULES[sport]['engine']
        assert not lg.data_warnings and lg.tb1 is None  # no inherited archive hold or major-league baseline


@pytest.mark.parametrize('defect',['future','hash','unknown_endpoint','scope','unreviewed','market','no_reason','invalid_fraction','invalid_bonus'])
def test_bad_source_configuration_never_issues(inputs,defect):
    req,_,history,contracts,tmp,_=inputs
    row=source_row(inputs)
    if defect=='future':row['available_at']='2030-01-01T00:00:00Z'
    if defect=='hash':row['evidence_sha256']='0'*64
    if defect=='unknown_endpoint':row['endpoint']='HALFTIME';req=dict(req,endpoint='HALFTIME')
    if defect=='scope':row['competition']='OTHER'
    if defect=='unreviewed':row['review_status']='PROBABLE'
    if defect=='market':row['odds']='1.9'
    if defect=='no_reason':row['reason']=''
    if defect=='invalid_fraction':row['extra_fraction']='nan'
    if defect=='invalid_bonus':row['winner_bonus']='9'
    with pytest.raises(AdmissionError):
        forecast(req,None,history,contracts,tmp/defect,competition_source=[row])
    assert not (tmp/defect).exists()


def test_fresh_web_history_can_replace_defective_archive_scope(inputs):
    req,lg,history,contracts,tmp,_=inputs
    row=source_row(inputs);row.update(archive_disposition='INCORRECT',reason='EXAMPLE archive date/endpoint defects quarantined')
    for r in history:r['source_kind']='WEB_CORRECTED'
    held=replace(lg,data_warnings=('BAD_ARCHIVE_ONLY',))
    with pytest.raises(AdmissionError,match='DATA_HOLD'):
        forecast(req,held,history,contracts,tmp/'held')
    rec=forecast(req,held,history,contracts,tmp/'web',competition_source=[row])
    assert rec['config_origin']=='REVIEWED_SPORTING_SOURCE' and rec['history_web_rows']==len(history)
    assert verify_bundle(tmp/'web')['competition']==lg.path
    original_receipt=(tmp/'web'/'RECEIPT.csv').read_bytes()
    receipt=read_rows(tmp/'web'/'RECEIPT.csv');receipt[0]['history_web_rows']='0'
    (tmp/'web'/'RECEIPT.csv').write_bytes(csv_bytes(receipt))
    with pytest.raises(AdmissionError,match='source coverage'):verify_bundle(tmp/'web')
    (tmp/'web'/'RECEIPT.csv').write_bytes(original_receipt)
    # Even self-consistent file hashes cannot hide a source/model configuration mismatch.
    sources=read_rows(tmp/'web'/'COMPETITION_SOURCE.csv');sources[0]['extra_fraction']='0.1'
    (tmp/'web'/'COMPETITION_SOURCE.csv').write_bytes(csv_bytes(sources))
    receipt=read_rows(tmp/'web'/'RECEIPT.csv');receipt[0]['competition_source_sha256']=digest((tmp/'web'/'COMPETITION_SOURCE.csv').read_bytes())
    (tmp/'web'/'RECEIPT.csv').write_bytes(csv_bytes(receipt))
    with pytest.raises(AdmissionError,match='frozen model config'):verify_bundle(tmp/'web')


def test_cli_does_not_require_archive_discovery_for_reviewed_web_history(inputs,monkeypatch):
    from ml import primary
    req,_,history,contracts,tmp,_=inputs
    for r in history:r['source_kind']='WEB_RECOVERED'
    for name,rows in [('request',[req]),('history',history),('contracts',contracts),('source',[source_row(inputs)])]:
        (tmp/(name+'.csv')).write_bytes(csv_bytes(rows))
    def forbidden(*args):raise AssertionError('empty archive must not be consulted to route reviewed web inputs')
    monkeypatch.setattr(primary,'get_league',forbidden)
    main(['predict','--request',str(tmp/'request.csv'),'--history',str(tmp/'history.csv'),
          '--contracts',str(tmp/'contracts.csv'),'--competition-source',str(tmp/'source.csv'),'--out',str(tmp/'cli')])
    assert verify_bundle(tmp/'cli')['history_web_rows']==str(len(history))


def test_web_origin_does_not_relax_training_cutoff(inputs):
    req,_,history,contracts,tmp,_=copy.deepcopy(inputs)
    history[0].update(source_kind='WEB_RECOVERED',available_at='2030-01-01T00:00:00Z')
    with pytest.raises(AdmissionError,match='not known'):
        forecast(req,None,history,contracts,tmp/'future',competition_source=[source_row(inputs)])


def test_reviewed_routing_requires_row_source_dispositions(inputs):
    req,_,history,contracts,tmp,_=inputs
    with pytest.raises(AdmissionError,match='each history row labelled'):
        forecast(req,None,history,contracts,tmp/'unlabelled',competition_source=[source_row(inputs)])
