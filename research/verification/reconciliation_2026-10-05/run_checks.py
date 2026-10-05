from pathlib import Path
from datetime import datetime, timezone
import subprocess,json,hashlib,sys
ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent/(sys.argv[1] if len(sys.argv)>1 else 'checks')
OUT.mkdir(exist_ok=True)
commands={
 'research_tests':['-m','pytest','-p','no:cacheprovider','research/tests','-q'],
 'logging_tests':['-m','pytest','-p','no:cacheprovider','research/operations/test_log_card.py','-q'],
 'custody':['-m','research.operations.verify_custody'],
 'acceptance':['-m','research.src.acceptance'],
 'canonical':['-m','research.operations.log_card','verify'],
 'freeze':['-m','research.operations.control_freeze','--verify'],
 'archive':['-m','research.src.archive','validate'],
 'workflow_status':['-m','research.src.workflow','status'],
 'workflow_score':['-m','research.src.workflow','score'],
}
results=[]
for name,args in commands.items():
 validation=ROOT/'Previous Sports Results/_canonical/validation.json'
 before=validation.read_bytes() if name=='archive' and validation.exists() else None
 started=datetime.now(timezone.utc).isoformat()
 p=subprocess.run([sys.executable,'-B',*args],cwd=ROOT,capture_output=True,env={**__import__('os').environ,'PYTHONIOENCODING':'utf-8'})
 raw=p.stdout+p.stderr; (OUT/(name+'.output.txt')).write_bytes(raw)
 if name=='archive' and before is not None:
  (OUT/'archive_validation_generated.json').write_bytes(validation.read_bytes()); validation.write_bytes(before)
 results.append(dict(name=name,command=[sys.executable,'-B',*args],started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),exit_code=p.returncode,output_sha256=hashlib.sha256(raw).hexdigest()))
 print(name,p.returncode,flush=True)
 (OUT/'command_results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
