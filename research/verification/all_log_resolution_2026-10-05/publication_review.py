"""Check staged scope, new local links and authored-text whitespace before push."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import json, re, subprocess, sys

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent

def git(*args):
    return subprocess.run(['git', *args], cwd=ROOT, stdout=subprocess.PIPE,
                          stderr=subprocess.STDOUT)

paths = git('diff', '--cached', '--name-only', '-z').stdout.decode().split('\0')
paths = [p for p in paths if p]
link_errors = []
checked_links = 0
for name in paths:
    if not name.endswith('.md') or not (ROOT / name).exists():
        continue
    diff = git('diff', '--cached', '--unified=0', '--', name).stdout.decode('utf-8')
    for line in diff.splitlines():
        if not line.startswith('+') or line.startswith('+++'):
            continue
        for match in re.finditer(r'\]\((<[^>]+>|[^)]+)\)', line):
            target = match.group(1).strip('<>')
            if urlsplit(target).scheme or target.startswith('#'):
                continue
            target = unquote(target.split('#')[0])
            checked_links += 1
            if not ((ROOT / name).parent / target).exists():
                link_errors.append({'file': name, 'target': target})

whitespace = git('-c', 'core.whitespace=blank-at-eol,blank-at-eof,space-before-tab,cr-at-eol',
                 'diff', '--cached', '--check', '--', '.',
                 ':!research/data/raw/source_snapshots/**',
                 ':!research/verification/**/*.txt',
                 ':!research/verification/**/*.body',
                 ':!research/verification/**/*.bin')
followup = '--followup' in sys.argv
(OUT / ('whitespace_followup.txt' if followup else 'whitespace_scoped.txt')).write_bytes(whitespace.stdout)
inventory = json.loads((OUT / 'source_inventory.json').read_text())
excluded = {r['body_path'].replace('\\', '/') for r in inventory['records']
            if r['excluded_from_git']}
staged_excluded = sorted(excluded.intersection(paths))
result = dict(staged_files=len(paths), paths=paths, added_local_links_checked=checked_links,
              broken_added_local_links=link_errors, staged_excluded_bodies=staged_excluded,
              authored_whitespace_exit=whitespace.returncode,
              whitespace_scope='CRLF accepted; raw source captures, immutable byte artifacts and retained transcripts excluded')
(OUT / ('followup_staged_paths.json' if followup else 'staged_paths.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='paths'}, indent=2))
raise SystemExit(bool(link_errors or staged_excluded or whitespace.returncode))
