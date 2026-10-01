import json,re,html
from pathlib import Path
A=Path(__file__).resolve().parent
def rows(v):
    if isinstance(v,str):
        try:v=json.loads(v)
        except Exception:return v
    if isinstance(v,dict) and 'rows' in v:
        return {'headers':v.get('headers'), 'rows':[[html.unescape(re.sub('<[^>]+>',' ',c['Text'] or '')).strip() for c in r['row']] for r in v['rows']]}
    if isinstance(v,list):return [rows(x) for x in v]
    if isinstance(v,dict):return {k:rows(x) for k,x in v.items()}
    return v
results=json.loads((A/'api_results.json').read_text(encoding='utf-8'))
out={}
for label,e in results.items():
    if e['status']!='JSON':continue
    data=e['data']
    if label=='api_games':out[label]=next(g for g in data['game'] if g['G_ID']=='20261001HHSS0')
    elif label=='api_lineup':out[label]={'metadata':data[:3],'home_order':rows(data[3][0]),'away_order':rows(data[4][0])}
    elif label in ['api_team','api_pitch']:out[label]=rows(data)
    elif label=='api_previous_box':
        out[label]={k:rows(v) for k,v in data.items() if ('Pitcher' in k or 'Etc' in k)}
(A/'native_readback.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(out.get('api_previous_box'),ensure_ascii=False))
