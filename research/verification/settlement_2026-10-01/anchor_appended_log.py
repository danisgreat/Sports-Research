"""Append source-anchor revisions for an unchanged prefix of a living log."""
from pathlib import Path
import json,hashlib
A=Path(__file__).resolve().parent;R=A.parents[2]
path=R/'research/data/processed/legacy_learning/source_anchor_corrections.json'
original=json.loads((A/'originals/research/data/processed/legacy_learning/source_anchor_corrections.json').read_text())
now=json.loads(path.read_text());assert now['revisions'][:len(original['revisions'])]==original['revisions']
manifest=json.loads((R/'research/data/processed/legacy_learning/manifest.json').read_text())
retained=A/'originals/prediction logs/PREDICTION_LOG_COMBINED_6.md';raw=retained.read_bytes();sha=hashlib.sha256(raw).hexdigest();lines=raw.decode('utf-8-sig').splitlines()
seen={r['pointer'] for r in now['revisions']};added=[]
for ref in manifest['source_pointers']:
    if ref['pointer'].startswith('PREDICTION_LOG_COMBINED_6.md:'):
        assert sha==ref['file_sha256']
        assert hashlib.sha256(lines[ref['line']-1].encode()).hexdigest()==ref['line_sha256']
        if ref['pointer'] in seen:continue
        row={'pointer':ref['pointer'],'original_path':ref['path'],'retained_path':retained.relative_to(R).as_posix(),'sha256':sha,'line':ref['line'],'reason':'October1 authorized append changes living whole-file hash; original source line and complete pre-append file remain byte-identical in retained custody. No normalized probability, rank, contract or grade changes.','revision_id':'ANCHOR-20261001-PART6-'+str(ref['line'])}
        now['revisions'].append(row);added.append(row)
if added:path.write_text(json.dumps(now,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
receipt={'new_anchor_revisions':len(now['revisions'])-len(original['revisions']),'prior_revisions_unchanged':True,'retained_original_sha256':sha,'current_anchor_store_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'scope':'DOCUMENTARY_CUSTODY_ONLY; NO_FORECAST_OR_NORMALIZED_ROW_CHANGE'}
assert receipt['new_anchor_revisions']==20
(A/'source_anchor_append_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
