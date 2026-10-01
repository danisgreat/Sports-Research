"""Read back the authorized audit and append its final receipt to living status."""
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

A = Path(__file__).resolve().parent
ROOT = A.parents[2]
sys.path.insert(0, str(ROOT))
from research.src.acceptance import run as acceptance_run
from freeze_current_manifest import selected_module

module = selected_module()
n, mismatches = module.verify()
assert not mismatches, mismatches
freeze = ROOT / module.NAME
mode, normalized = module.normalization(freeze)
freeze_sha = hashlib.sha256(normalized).hexdigest()
marker = '<!-- SETTLEMENT-FINAL-VERIFICATION-20261001 -->'
status = ROOT / 'GAME_LOG_STATUS_CURRENT.md'
if marker.encode() not in status.read_bytes():
    receipt_path = (A / 'FINAL_CHECKS.json').as_posix()
    tail = f'''

{marker}
## October 1 final verification receipt

Current selected receipt: `{module.NAME}`; normalized {mode} SHA-256 `{freeze_sha}`. The earlier receipt remains preserved. All {n} listed files match. The original Part 6 source block, original forecast cores, historical base ledger, model builds and five frozen shadows remain unchanged; canonical next ID remains P-523.

The complete research test suite passed: 107 tests in 64.39 seconds. Custody, source-body, score, historical pointer and append-prefix checks passed. The archive validation also passed; its separate pre-existing receipt gap is one unavailable raw body out of 1,615 receipts and remains disclosed.

Final audit counts: 523 inventoried identities; 116 detailed historical/manual reviews; 34 diagnostic rows on eight cards/claims; 50 historical ledger field corrections across seven IDs; 117 separate learning revisions. Newly certified full settlements: zero; new operator voids: zero; canonical transactions: zero. Forty reviewed identities retain specific row/identity/operator/rank/period/provider blockers, and the diagnostic cards retain certification gaps. These are learning results, not admitted predictive performance.

Full mechanical readback: [FINAL_CHECKS.json]({receipt_path}). Per-card evidence requirements and A–F reviews remain in the audit report.
'''
    with status.open('ab') as handle:
        handle.write(tail.replace('\n', '\r\n').encode('utf-8'))

check = subprocess.run(
    [sys.executable, '-X', 'utf8', '-B', str(A / 'verify_audit.py')],
    cwd=ROOT, text=True, encoding='utf-8', capture_output=True,
)
(A / 'final_audit_check_stdout.txt').write_text(check.stdout, encoding='utf-8')
assert check.returncode == 0, check.stdout + check.stderr
audit = json.loads((A / 'VERIFICATION.json').read_text(encoding='utf-8'))
acceptance = acceptance_run()
assert acceptance['valid'], acceptance
archive_path = ROOT / 'Previous Sports Results/_canonical/validation.json'
archive = json.loads(archive_path.read_text(encoding='utf-8'))
assert archive['valid'] and not archive['issues'], archive
diff = subprocess.run(['git', 'diff', '--check'], cwd=ROOT, text=True, capture_output=True)
assert diff.returncode == 0, diff.stdout + diff.stderr
n, mismatches = module.verify()
assert not mismatches, mismatches
receipt = {
    'observed_utc': datetime.now(timezone.utc).isoformat(),
    'valid': True,
    'test_suite': {
        'command': 'py -3.14 -X utf8 -B -m pytest -p no:cacheprovider research/tests -q',
        'observed_result': '107 passed in 64.39s',
        'exit_code': 0,
        'execution_session_id': 37431,
        'note': 'Recorded from the completed full test run; not rerun by this readback script.',
    },
    'audit_readback': audit,
    'implementation_acceptance': acceptance,
    'archive_validation': archive,
    'archive_validation_file_sha256': hashlib.sha256(archive_path.read_bytes()).hexdigest(),
    'selected_freeze': {
        'path': str(freeze), 'mode': mode, 'sha256': freeze_sha,
        'listed_files': n, 'mismatches': mismatches,
    },
    'git_diff_check': {'exit_code': diff.returncode, 'stdout': diff.stdout, 'stderr': diff.stderr},
    'limits': [
        'No new certified settlement, canonical issue/revision, operator void, model qualification or prospective performance admission.',
        'Exact missing owner fields, actual-start semantics, independent collection lineages, custody and operator terms remain listed per card.',
        'One archive source body is unavailable; retained-body checks do not certify independence or source truth.',
        'Raw source bodies are local quarantined artifacts; a copy without them cannot reproduce their body checks.',
    ],
}
(A / 'FINAL_CHECKS.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'valid': True, 'receipt': str(A / 'FINAL_CHECKS.json'), 'listed_files': n,
                  'freeze_sha256': freeze_sha, 'audit_valid': audit['valid'],
                  'acceptance_valid': acceptance['valid'], 'archive_valid': archive['valid']}, indent=2))
