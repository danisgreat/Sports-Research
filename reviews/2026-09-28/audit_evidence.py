"""Read-only source audit; writes derived evidence in this review directory only."""
from pathlib import Path
import csv, hashlib, json, re, statistics, sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent

def clean(s):
    return s.replace('**','').replace('`','').strip()

def tables(lines):
    for i, line in enumerate(lines):
        if not line.startswith('|') or i+1 >= len(lines):
            continue
        if not re.match(r'^\|\s*:?-', lines[i+1]):
            continue
        h = [clean(x) for x in line.strip('|').split('|')]
        rows = []
        j = i+2
        while j < len(lines) and lines[j].startswith('|'):
            cells = [clean(x) for x in lines[j].strip('|').split('|')]
            rows.append((j+1,dict(zip(h,cells))))
            j += 1
        yield i+1,h,rows

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    inventory = []
    paths = sorted(ROOT.glob('*.md')) + sorted((ROOT/'research').glob('*/README.md'))
    paths += sorted((ROOT/'Mini logs (to be sent to actual log later)').glob('*/*.md'))
    for p in paths:
        b=p.read_bytes(); s=b.decode('utf-8-sig')
        inventory.append(dict(path=p.relative_to(ROOT).as_posix(), bytes=len(b), lines=len(s.splitlines()), words=len(s.split()), sha256=hashlib.sha256(b).hexdigest(), headings=re.findall(r'^#{1,3} .+',s,re.M)))
    rows=list(csv.DictReader((ROOT/'research/settled_rows_2026-09-25/settled_rows.csv').open(encoding='utf-8-sig',newline='')))
    valid=[r for r in rows if r['result'] in ('W','L') and r['p'] and 0<float(r['p'])<1]
    preferred=[r for r in valid if float(r['p'])>=.5]
    brier=lambda rs: statistics.mean((float(r['p'])-(r['result']=='W'))**2 for r in rs)
    by=defaultdict(list)
    for r in preferred: by[r['card']].append(r)
    ties=defaultdict(list)
    for r in valid:
        if float(r['p'])==.5: ties[r['card']].append({k:r[k] for k in ('rank','contract','p','result','source')})
    ybar=statistics.mean(r['result']=='W' for r in valid)
    dataset=dict(rows=len(rows),cards=len({r['card'] for r in rows}), probability_rows=sum(bool(r['p']) for r in rows), decisive_probability_rows=len(valid), probability_cards=len({r['card'] for r in valid}), proxy_decisions=len(preferred), proxy_cards=len(by), all_row_brier=brier(valid), proxy_decision_brier=brier(preferred), proxy_card_equal_brier=statistics.mean(brier(v) for v in by.values()), in_sample_climatology=ybar, apparent_climatology_skill=1-brier(valid)/(ybar*(1-ybar)), exact_50_rows=dict(ties), max_card=max(int(r['num']) for r in rows))
    mini=next((ROOT/'Mini logs (to be sent to actual log later)').glob('*P-518*/*.md'))
    text=mini.read_text(encoding='utf-8-sig'); lines=text.splitlines()
    blocks=list(re.finditer(r'^### (P-\d+) —',text,re.M))
    active=[]
    for k,m in enumerate(blocks):
        body=text[m.start():blocks[k+1].start() if k+1<len(blocks) else len(text)]
        offset=text[:m.start()].count('\n')
        issued={}; settled={}; mismatches=[]; brier_checks=[]
        for n,h,rs in tables(body.splitlines()):
            if any(x in h for x in ('Contract','Exact supplied contract')) and any('q' in x for x in h) and 'Result' not in h:
                for line,r in rs:
                    rank=r.get('Rank (q)',r.get('Rank',''))
                    if rank.isdigit(): issued[rank]=dict(r,line=offset+line)
            if 'Contract (issued)' in h and 'Result' in h:
                for line,r in rs:
                    if r.get('Rank','').isdigit(): settled[r['Rank']]=dict(r,line=offset+line)
        for rank,r in settled.items():
            original=issued.get(rank,{})
            for field in ('BASELINE_P','TEAM_BASELINE_P'):
                if original.get(field)!=r.get(field): mismatches.append(dict(rank=rank,field=field,issued=original.get(field),settled=r.get(field),line=r['line']))
            for pcol,scol in [('p','Brier(p)'),('q','Brier(q)')]:
                try:
                    p=float(r[pcol]); expected=(p-(r['Result']=='WIN'))**2
                    shown=float(r[scol]); brier_checks.append(dict(rank=rank,field=scol,expected=expected,shown=shown,ok=abs(expected-shown)<=.00015,line=r['line']))
                except (ValueError,KeyError): pass
        status = next((s for s in body.splitlines() if 'Status' in s or 'LIVE_ISSUED' in s), 'NO STATUS MATCH')
        active.append(dict(card=m[1],line=offset+1,status=status,issued=issued,settled=settled,baseline_mismatches=mismatches,brier_checks=brier_checks))
    missing=[]
    for p in sorted(ROOT.glob('*.md')):
        if p.name.startswith(('PREDICTION_LOG','CONTROL_MANIFEST','GAME_LOG_STATUS_INDEX')): continue
        for n,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
            for link in re.findall(r'\]\(([^)]+)\)',line):
                target=link.split('#')[0].strip('<>')
                if not target or '://' in target or target.startswith(('mailto:','app:')) or re.match(r'^[A-Za-z]:',target): continue
                if not (p.parent/target).exists(): missing.append(dict(file=p.name,line=n,target=target))
    result=dict(as_of_utc=datetime.now(timezone.utc).isoformat(),inventory=inventory,dataset=dataset,active_mini_path=mini.relative_to(ROOT).as_posix(),active_mini_sha256=hashlib.sha256(mini.read_bytes()).hexdigest(),active_cards=active,missing_relative_links=missing)
    (OUT/'audit_evidence.json').write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(dict(inventory_files=len(inventory),root_markdown_files=len(list(ROOT.glob('*.md'))),dataset={k:v for k,v in dataset.items() if k!='exact_50_rows'},ties=ties,active_summary=[dict(card=x['card'],issued_rows=len(x['issued']),settled_rows=len(x['settled']),baseline_field_mismatches=len(x['baseline_mismatches']),incorrect_brier_cells=[z for z in x['brier_checks'] if not z['ok']]) for x in active],missing_links=missing),indent=2,ensure_ascii=False))

if __name__=='__main__': main()
