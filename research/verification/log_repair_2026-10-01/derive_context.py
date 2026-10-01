import json,re,html
from pathlib import Path
A=Path(__file__).resolve().parent
U=Path((A/'latest_updates_dir.txt').read_text(encoding='utf-8'))
data=json.loads((U/'results.json').read_text(encoding='utf-8'))
def table(v):
    if isinstance(v,str):
        try:v=json.loads(v)
        except Exception:return v
    if isinstance(v,list):return [table(x) for x in v]
    if isinstance(v,dict) and 'rows' in v:
        clean=lambda c:html.unescape(re.sub('<[^>]+>',' ',c.get('Text') or '')).strip()
        return {'headers':[[clean(c) for c in row['row']] for row in v.get('headers',[])],
                'rows':[[clean(c) for c in row['row']] for row in v['rows']]}
    if isinstance(v,dict):return {k:table(x) for k,x in v.items()}
    return v
out={'observation':data['20261001']['receipt']}
out['current_game']=next(g for g in data['20261001']['data']['game'] if g['G_ID']=='20261001HHSS0')
out['sep29_game']=next((g for g in data['20260929']['data']['game'] if g['G_ID']=='20260929HHSS0'),None)
box=data['box_sep29']['data']
out['sep29_pitchers']=table(box.get('arrPitcher')) if isinstance(box,dict) else None
recent={}
for team in ['HH','SS']:
    games=[]; rejected=[]
    for date,e in data.items():
        if not date.isdigit() or date>='20261001':continue
        for g in (e.get('data') or {}).get('game',[]):
            if team not in [g.get('AWAY_ID'),g.get('HOME_ID')]:continue
            if not g.get('G_ID','').startswith(date):rejected.append(g.get('G_ID'));continue
            if g.get('GAME_RESULT_CK') != 1:continue
            try:a,h=int(g['T_SCORE_CN']),int(g['B_SCORE_CN'])
            except (ValueError,TypeError):continue
            rf,ra=(a,h) if g['AWAY_ID']==team else (h,a)
            games.append({'date':date,'id':g['G_ID'],'rf':rf,'ra':ra,'total':a+h,'result':'W' if rf>ra else 'L' if rf<ra else 'T'})
    games.sort(key=lambda g:(g['date'],g['id']),reverse=True)
    windows={}
    for n in [5,10,15,20]:
        selected=games[:n]
        windows[str(n)]={'found':len(selected),'wins':sum(g['result']=='W' for g in selected),'losses':sum(g['result']=='L' for g in selected),'ties':sum(g['result']=='T' for g in selected),'rf_per_game':sum(g['rf'] for g in selected)/len(selected) if selected else None,'ra_per_game':sum(g['ra'] for g in selected)/len(selected) if selected else None,'under_11_5':sum(g['total']<=11 for g in selected),'over_11_5':sum(g['total']>=12 for g in selected)}
    recent[team]={'games':games,'windows':windows,'rejected_wrong_date':rejected}
out['recent']=recent
(A/'derived_context.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({**{'recent_'+k:v['windows'] for k,v in recent.items()},'sep29':out['sep29_game'],'sep29_pitchers':out['sep29_pitchers']},ensure_ascii=False))
