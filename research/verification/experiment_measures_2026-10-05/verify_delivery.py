"""Read back original custody, catalog coverage, no real runs and added links."""
from pathlib import Path
import hashlib,json,re,sys
from urllib.parse import unquote,urlsplit
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT))
from research.experiments.verify import run
from research.operations.log_card import next_id

opening=json.loads((OUT/'opening.json').read_text())
for row in opening['protected_files']:
    raw=(ROOT/row['path']).read_bytes()
    if len(raw)!=row['bytes'] or hashlib.sha256(raw).hexdigest()!=row['sha256']:raise ValueError('Original changed: '+row['path'])
result=run();links=0;local_targets=[];scopes=[];legacy_broken=[]
markers={'METHOD.md':'## Fifteen experiment measures','CURRENT_RULES.md':'## Fifteen experiments',
 'SCORING_AND_VALIDATION.md':'## Versioned fifteen-experiment','VERIFICATION_PROTOCOL.md':'## Experiment-measure verification',
 'CARD_AND_LOG_TEMPLATES.md':'## Experiment forecasts','README.md':'## Fifteen proposed experiments',
 'research/README.md':'## Fifteen experiment measures','LEARNING_REGISTER.md':'## Experiment implementation follow-through',
 'LEARNINGS_INDEX.md':'- [All fifteen experiment measures','CHANGELOG.md':'## Fifteen experiment measures'}
for row in json.loads((OUT/'document_changes_v2.json').read_text())['files']:
    path=ROOT/row['path'];raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=row['after_sha256']:raise ValueError('Changed documented delivery: '+row['path'])
    text=raw.decode('utf-8-sig');marker=markers[row['path']]
    if text.count(marker)!=1:raise ValueError('Missing/duplicate implementation section: '+row['path'])
    prior,added=text.split(marker)
    scopes.append((path,marker+added))
    for match in re.finditer(r'\]\((<[^>]+>|[^)]+)\)',prior):
        target=match[1].strip('<>')
        if urlsplit(target).scheme or target.startswith('#'):continue
        if not (path.parent/unquote(target.split('#')[0])).exists():legacy_broken.append(dict(path=row['path'],target=target))
for path in [ROOT/'research/experiments/NEXT_STEPS.md',OUT/'REPORT.md']:
    scopes.append((path,path.read_text(encoding='utf-8-sig')))
for path,text in scopes:
    for match in re.finditer(r'\]\((<[^>]+>|[^)]+)\)',text):
        target=match[1].strip('<>')
        if urlsplit(target).scheme or target.startswith('#'):continue
        target=unquote(target.split('#')[0])
        resolved=(path.parent/target).resolve();local_targets.append(resolved)
        if resolved!=(OUT/'readback.json').resolve() and not resolved.exists():raise ValueError('Broken local link: '+path.name+':'+target)
        links+=1
runs=ROOT/'research/experiments/runs'
if runs.exists() and any(p.is_file() for p in runs.rglob('*')):raise ValueError('Unexpected real experiment artifacts at initial registration')
result.update(original_artifacts_unchanged=len(opening['protected_files']),new_local_links_verified=links,
              existing_broken_local_links=legacy_broken,
              link_scope='Added sections in ten current documents plus the full new guide/report; legacy breaks retained explicitly.',
              actual_experiments_run=0,next_canonical_id=next_id())
with (OUT/'readback.json').open('w',encoding='utf-8') as stream:json.dump(result,stream,indent=2);stream.write('\n')
if any(not path.exists() for path in local_targets):raise ValueError('Missing generated local link after readback')
print(json.dumps(result,indent=2))
