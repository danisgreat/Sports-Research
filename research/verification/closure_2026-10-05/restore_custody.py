"""Restore only historical bytes matching already frozen receipts."""
import hashlib
import json
from pathlib import Path
import subprocess
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent
def sha(raw): return hashlib.sha256(raw).hexdigest()
def dump(name, value):
    (OUT/name).write_text(json.dumps(value, indent=2)+'\n', encoding='utf-8')

if __name__ == '__main__':
    opening = {}
    for name in ['METHOD.md', 'CURRENT_RULES.md', '.github/workflows/research.yml',
                 'research/src/control_manifest.py', 'research/operations/log_card.py',
                 'research/operations/control_freeze.py',
                 'Previous Sports Results/_canonical/manifest.json',
                 'prediction logs/PREDICTION_LOG_COMBINED_6.md',
                 'research/canonical_ledger.jsonl', 'GAME_LOG_STATUS_CURRENT.md']:
        raw = (ROOT/name).read_bytes()
        target = OUT/'opening'/name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(raw)
        opening[name] = dict(bytes=len(raw), sha256=sha(raw))
    dump('opening.json', dict(utc=datetime.now(timezone.utc).isoformat(),
         head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
         files=opening))
    repairs = []
    name = 'research/src/control_manifest.py'
    commit = 'e38ff1072b831bfb3ad38cb8f413b02c29690727'
    raw = subprocess.check_output(['git','show',commit+':'+name],cwd=ROOT)
    expected = '2bd5072a533571c549fa07c5c172d819cc23ecbece5936ed55abf27f20723cc6'
    assert sha(raw) == expected
    (ROOT/name).write_bytes(raw)
    repairs.append(dict(path=name, commit=commit, transformation='EXACT_GIT_BLOB',sha256=sha(raw)))
    base = ROOT/'research/custody/implementation_2026-10-01'
    manifest = json.loads((base/'manifest.json').read_text(encoding='utf-8'))
    for entry in manifest['files']:
        path = base/entry['path']
        if path.exists(): continue
        original = subprocess.check_output(['git','show',manifest['head']+':'+entry['path']],cwd=ROOT)
        normalized = original.decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n').replace('\n','\r\n').encode('utf-8')
        candidates = [('EXACT_GIT_BLOB',original),('CRLF',normalized),('CRLF_UTF8_BOM',b'\xef\xbb\xbf'+normalized)]
        hits = [(mode,raw) for mode,raw in candidates if sha(raw)==entry['sha256'] and len(raw)==entry['bytes']]
        assert hits, entry['path']
        mode, raw = hits[0]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        assert sha(path.read_bytes())==entry['sha256']
        repairs.append(dict(path=path.relative_to(ROOT).as_posix(),commit=manifest['head'],
                            transformation=mode,sha256=sha(raw)))
    dump('custody_restoration.json', repairs)
    print(json.dumps(dict(restored=len(repairs),model_dependency_sha256=expected)))
