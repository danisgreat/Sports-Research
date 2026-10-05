"""Retain independent final checks without short-circuiting after a failure."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def check(name, args):
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run([sys.executable, '-X', 'utf8', '-B', *args], cwd=ROOT,
                            env={**os.environ, 'PYTHONIOENCODING': 'utf-8', 'PYTHONDONTWRITEBYTECODE': '1'},
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    target = OUT/(name+'.txt')
    target.write_bytes(result.stdout)
    return dict(check=name, command=[sys.executable, '-B', *args], started_utc=started,
                completed_utc=datetime.now(timezone.utc).isoformat(), exit_code=result.returncode,
                output_path=target.relative_to(ROOT).as_posix(), output_sha256=sha(result.stdout))


def readback():
    opening = json.loads((OUT/'opening.json').read_text())
    for item in opening['immutable_files']:
        raw = (ROOT/item['path']).read_bytes()
        if len(raw) != item['bytes'] or sha(raw) != item['sha256']:
            raise ValueError('Original artifact changed: '+item['path'])
    cleanup = json.loads((OUT/'cleanup_receipt.json').read_text(encoding='utf-8-sig'))
    if (ROOT/cleanup['path']).exists() or not cleanup['removal_status'].startswith('REMOVED'):
        raise ValueError('Redundant mini pointer was not removed')
    status = (ROOT/'GAME_LOG_STATUS_CURRENT.md').read_text(encoding='utf-8-sig')
    before = subprocess.run(['git', 'show', opening['head']+':GAME_LOG_STATUS_CURRENT.md'],
                            cwd=ROOT, capture_output=True, check=True).stdout.decode('utf-8-sig')
    end = '<!-- END CURRENT RESEARCH QUEUE -->'
    original_history = before.split(end, 1)[1].replace('\r\n', '\n').strip('\n')
    current_history = status.split(end, 1)[1].split('<!-- BEGIN CURRENT IMPLEMENTATION READBACK 2026-10-05-I2 -->', 1)[0].strip('\n')
    if original_history != current_history:
        raise ValueError('Historical status-register body changed')
    changes = json.loads((OUT/'document_changes.json').read_text())
    docs = sorted({r['path'] for r in changes['files']} | {'METHOD.md', 'GAME_LOG_STATUS_CURRENT.md'})
    links = []
    # Check newly introduced links, not inaccessible historical source links.
    report = OUT/'REPORT.md'
    candidates = {report: report.read_text(encoding='utf-8')}
    for name in docs:
        path = ROOT/name
        diff = subprocess.run(['git', 'diff', '--', name], cwd=ROOT, capture_output=True, check=True).stdout.decode('utf-8')
        candidates[path] = '\n'.join(line[1:] for line in diff.splitlines() if line.startswith('+') and not line.startswith('+++'))
    for path, text in candidates.items():
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
            if target.startswith(('http:', 'https:', 'mailto:', '#')):
                continue
            destination = (path.parent/unquote(target.split('#', 1)[0])).resolve()
            if not destination.exists():
                raise ValueError(f'New link missing: {path.relative_to(ROOT)} -> {target}')
            links.append(dict(document=path.relative_to(ROOT).as_posix(), target=target))
    return dict(passed=True, immutable_files=len(opening['immutable_files']),
                all_six_prediction_logs_unchanged=True, canonical_ledger_unchanged=True,
                model_builds_and_dependencies_unchanged=True, historical_status_body_unchanged=True,
                redundant_documents_removed=1, newly_added_local_links_verified=len(links),
                modified_existing_documents=len(docs), links=links)


def main():
    commands = [
        ('regressions', ['-m', 'pytest', '-p', 'no:cacheprovider', 'research/tests', 'research/operations', '-q']),
        ('canonical', ['-m', 'research.operations.log_card', 'verify']),
        ('custody', ['-m', 'research.operations.verify_custody']),
        ('reconciliation', ['-m', 'research.operations.verify_reconciliation']),
        ('freeze', ['-m', 'research.operations.control_freeze', '--verify']),
        ('archive', ['-m', 'research.src.archive', 'validate']),
        ('workflow_status', ['-m', 'research.src.workflow', 'status']),
        ('workflow_score', ['-m', 'research.src.workflow', 'score']),
    ]
    results = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(check, name, args) for name, args in commands]
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            print(result['check']+': '+str(result['exit_code']), flush=True)
    manifest = dict(observed_utc=datetime.now(timezone.utc).isoformat(), results=sorted(results, key=lambda r: r['check']),
                    passed=all(r['exit_code'] == 0 for r in results),
                    scope='LOCAL_REQUIRED_CHECKS; tracked-only source export independently remains incomplete')
    (OUT/'checks.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    try:
        evidence = readback()
    except (OSError, ValueError, KeyError) as exc:
        evidence = dict(passed=False, error=f'{type(exc).__name__}: {exc}')
    (OUT/'readback.json').write_text(json.dumps(evidence, indent=2)+'\n', encoding='utf-8')
    print('originals/cleanup/links: '+str(evidence['passed']), flush=True)
    return not (manifest['passed'] and evidence['passed'])


if __name__ == '__main__':
    raise SystemExit(main())
