"""Verify exact fifteen-proposal coverage and the issued measurement catalog."""
from pathlib import Path
import json
from research.src.eligibility import digest,file_sha
from .catalog import ROOT,VERSION,catalog
from .runner import readiness

def run(root=ROOT):
    root=Path(root)
    manifest=json.loads((root/'research/experiment_measures.json').read_text(encoding='utf-8'))
    path=root/manifest['protocols_path']
    if not path.resolve().is_relative_to(root/'research/experiments'):raise ValueError('Protocol path escapes experiment definitions')
    if file_sha(path)!=manifest['protocols_sha256']:raise ValueError('Measurement protocol catalog changed')
    actual=json.loads(path.read_text(encoding='utf-8'))
    expected=catalog(root)
    if actual['protocols']!=expected:raise ValueError('Protocol definitions differ from current source-bound code')
    if len(manifest['records'])!=15 or len({r['experiment_id'] for r in manifest['records']})!=15:raise ValueError('Incomplete or duplicate measurement registry')
    records={r['experiment_id']:r for r in manifest['records']}
    for protocol in expected:
        row=records[protocol['experiment_id']]
        if row['protocol_sha256']!=digest(protocol) or row['source_card_id']!=protocol['source_card_id']:raise ValueError('Proposal/measurement mapping changed')
        if row['measures_status']!='IMPLEMENTED' or row['experiment_status']!='NOT_RUN_AT_REGISTRATION' or row['performance_eligible'] is not False:raise ValueError('Measurement implementation cannot promote an experiment')
    return dict(passed=True,schema=VERSION,proposals=15,measures_implemented=15,
                ready_to_freeze=sum(not readiness(p,root)['missing'] for p in expected),
                hypothesis_text_preserved=True,performance_eligible=False,
                limitation='Measurement/catalog mechanics only; missing candidate/baseline/cohort/power/audit inputs remain explicit.')
