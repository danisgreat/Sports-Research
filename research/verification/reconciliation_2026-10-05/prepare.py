from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, collections, subprocess

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
def sha(raw): return hashlib.sha256(raw).hexdigest()
def save(name, value):
    (OUT/name).write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

if __name__ == '__main__':
    originals=OUT/'originals'; originals.mkdir(exist_ok=True)
    docs=['METHOD.md','CURRENT_RULES.md','CARD_AND_LOG_TEMPLATES.md','SCORING_AND_VALIDATION.md','SOURCES.md','RECORD_ELIGIBILITY_SCHEMA.md','VERIFICATION_PROTOCOL.md','GAME_LOG_STATUS_CURRENT.md','research/README.md','IMPLEMENTATION_2026-10-01.md','RULES_BASEBALL.md','RULES_BASKETBALL.md','RULES_ICE_HOCKEY.md','RULES_NRL_RUGBY.md','RULES_SOCCER.md','LEAGUE_RULES_SOCCER.md','Previous Sports Results/Baseball/KBO/RULES_AND_FRAMEWORK.md','Previous Sports Results/Baseball/MLB/RULES_AND_FRAMEWORK.md','prediction logs/PREDICTION_LOG_COMBINED_6.md','research/canonical_ledger.jsonl','Mini logs (to be sent to actual log later)/Mini Prediction Log - P-523 onward - 2026-10-01/PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md']
    inventory=[]
    for name in docs:
        p=ROOT/name; raw=p.read_bytes(); inventory.append(dict(path=name,bytes=len(raw),sha256=sha(raw)))
        if name in docs[-3:] or name=='GAME_LOG_STATUS_CURRENT.md':
            dest=originals/name; dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(raw)
    attachments=[('consolidated_source.txt',Path('C:/Users/danie/.codex/attachments/f0cdbc33-a769-455e-88d2-e17646248f0c/Pasted text.txt')),('instructions_a.txt',Path('C:/Users/danie/.codex/attachments/443a463b-7876-45ae-a93c-928dac137d54/Pasted text.txt')),('instructions_b.txt',Path('C:/Users/danie/.codex/attachments/72d7a73a-4006-4e30-8ac7-94f09340540a/Pasted text.txt')),('fallback_mini_source.txt',ROOT/'research/verification/mini_settlement_2026-10-02/original_mini_evidence.txt')]
    for name,p in attachments:
        raw=p.read_bytes(); (originals/name).write_bytes(raw); inventory.append(dict(path=str(p),retained=str((originals/name).relative_to(ROOT)),bytes=len(raw),sha256=sha(raw)))
    download=Path('C:/Users/danie/Downloads/PREDICTION_MINI_RUNNING_LOG_P527_ONWARD_UPDATED_4.md')
    if download.exists():
        raw=download.read_bytes(); (originals/'downloads_mini_current.md').write_bytes(raw); inventory.append(dict(path=str(download),retained=str((originals/'downloads_mini_current.md').relative_to(ROOT)),bytes=len(raw),sha256=sha(raw)))
    save('opening_custody.json',dict(captured_utc=datetime.now(timezone.utc).isoformat(),head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),dirty=subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),files=inventory))
    archive=ROOT/'Previous Sports Results'
    destinations={'Austria_Bundesliga_Basketball_CSVs':'Basketball/Austria Basketball Bundesliga','County_Cricket_CSVs':'Cricket Tests/County Championship','Greek_Basket_League_CSVs':'Basketball/Greek Basket League','IPL_CSVs':'Cricket T20/IPL','NRL_CSVs':'Rugby League/NRL'}
    mappings=[]
    for folder in sorted(ROOT.glob('*_CSVs')):
        for p in sorted(folder.rglob('*.csv')):
            raw=p.read_bytes(); h=sha(raw); year=p.stem.rsplit('_',1)[1]
            dest=archive/destinations[folder.name]/year/(year+'_games.csv')
            if not dest.exists() or sha(dest.read_bytes())!=h: raise ValueError(f'Archive destination differs: {p}: {dest}')
            with p.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.reader(f))
            mappings.append(dict(source=str(p.relative_to(ROOT)),destination=str(dest.relative_to(ROOT)),sha256=h,bytes=len(raw),data_rows=max(0,len(rows)-1)))
    save('csv_cleanup_plan.json',dict(schema='verified-exact-duplicate-cleanup-1',files=mappings,count=len(mappings),data_rows=sum(x['data_rows'] for x in mappings),action='Recycle only mapped CSV files after rechecking all hashes; preserve operational/research CSVs and non-CSV files.'))
    print(json.dumps(dict(documents=len(inventory),duplicate_csvs=len(mappings),data_rows=sum(x['data_rows'] for x in mappings),folders=sorted(set(Path(x['source']).parts[0] for x in mappings))),indent=2))
