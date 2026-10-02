"""Read-only checks for the October 2 local-mini addendum. No issuer writes."""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
MINI = Path(r'C:\Users\danie\Downloads\PREDICTION_MINI_RUNNING_LOG_P527_ONWARD_UPDATED_4.md')
def now(): return datetime.now(timezone.utc).isoformat()
def sha(raw): return hashlib.sha256(raw).hexdigest()
def put(name, obj):
    (OUT/name).write_text(json.dumps(obj, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

if sys.argv[1] == 'snapshot':
    raw = MINI.read_bytes()
    assert len(raw) == 7831, 'Unexpected opening mini; stop and inspect'
    with (OUT/'original_mini_evidence.txt').open('xb') as f: f.write(raw)
    names = ['METHOD.md','CURRENT_RULES.md','CARD_AND_LOG_TEMPLATES.md',
             'SCORING_AND_VALIDATION.md','SOURCES.md','RECORD_ELIGIBILITY_SCHEMA.md',
             'VERIFICATION_PROTOCOL.md','GAME_LOG_STATUS_CURRENT.md','research/README.md',
             'prediction logs/PREDICTION_LOG_COMBINED_6.md','research/canonical_ledger.jsonl',
             'research/sources_registry.json','research/admission_registry.json',
             'CONTROL_MANIFEST_2026-10-01-5.md','RULES_BASKETBALL.md','RULES_BASEBALL.md',
             'RULES_ICE_HOCKEY.md','IMPLEMENTATION_2026-10-01.md']
    put('opening_custody.json', dict(observed_utc=now(), mini_path=str(MINI),
        original_mini_bytes=len(raw), original_mini_sha256=sha(raw),
        authority_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        origin_main=subprocess.check_output(['git','rev-parse','origin/main'],cwd=ROOT,text=True).strip(),
        files=[dict(path=n,bytes=len((ROOT/n).read_bytes()),sha256=sha((ROOT/n).read_bytes())) for n in names]))
    print('Opening original and authority hashes retained')
elif sys.argv[1] == 'commands':
    if len(sys.argv)>2:
        assert sys.argv[2] in {'post_append','publication'}
        OUT=OUT/sys.argv[2]
        OUT.mkdir(exist_ok=False)
    commands = [('tests', ['-X','utf8','-B','-m','pytest','-p','no:cacheprovider','research/tests','research/operations/test_log_card.py','-q']),
        ('archive', ['-B','-m','research.src.archive','validate']),
        ('custody', ['-B','-m','research.operations.verify_custody']),
        ('acceptance', ['-B','-m','research.src.acceptance']),
        ('canonical_log', ['-B','-m','research.operations.log_card','verify']),
        ('freeze', ['-B','-m','research.operations.control_freeze','--verify']),
        ('workflow_status', ['-B','-m','research.src.workflow','status']),
        ('workflow_score', ['-B','-m','research.src.workflow','score'])]
    results=[]
    for label,args in commands:
        started=now()
        run=subprocess.run([sys.executable,*args],cwd=ROOT,capture_output=True,encoding='utf-8',errors='replace')
        output=run.stdout+run.stderr
        (OUT/(label+'.output.txt')).write_bytes(output.encode('utf-8'))
        results.append(dict(check=label,command=[sys.executable,*args],started_utc=started,
            finished_utc=now(),exit_code=run.returncode,output_path=label+'.output.txt',output_sha256=sha(output.encode())))
        put('command_results.json',results)
        print(label,run.returncode,output[-1200:],flush=True)
else:
    raise ValueError('snapshot or commands required')
