"""MARKET-BLIND illustrative basketball score simulation; NOT an official forecast.
KBL 13 Nov 2026: Wonju DB Promy (home) vs Suwon KT Sonicboom.
Season rates as of 13 Nov pre-tip: DB 90.1 PF/89.3 PA, KT 85.0 PF/86.5 PA (13 games each).
Three subjective scenario cases disclose unresolved lineup and return uncertainty.
No odds, tips, market projections or prediction-source probabilities enter inputs.
"""
import hashlib, json, pathlib
import numpy as np
seed=20261113
rng=np.random.default_rng(seed)
N=600_000
cases=[{'name':'LOW','weight':.25,'reg_total_mean':172.5,'reg_margin_mean':3.0,'total_sd':19.5,'margin_sd':15.5},
       {'name':'BASE','weight':.50,'reg_total_mean':176.0,'reg_margin_mean':5.1,'total_sd':18.0,'margin_sd':14.5},
       {'name':'HIGH','weight':.25,'reg_total_mean':181.0,'reg_margin_mean':7.5,'total_sd':19.0,'margin_sd':15.5}]
# Score-level correlation of total and home-side margin: assumed +0.08; not fitted.
rho=.08
u=rng.random(N)
assign=np.searchsorted(np.cumsum([x['weight'] for x in cases]),u,side='right').clip(0,2)
z1=rng.standard_normal(N)
z2=rho*z1+np.sqrt(1-rho*rho)*rng.standard_normal(N)
T=np.array([cases[i]['reg_total_mean'] for i in assign])+np.array([cases[i]['total_sd'] for i in assign])*z1
M=np.array([cases[i]['reg_margin_mean'] for i in assign])+np.array([cases[i]['margin_sd'] for i in assign])*z2
h=np.rint(np.maximum(0,(T+M)/2)).astype(np.int32)
a=np.rint(np.maximum(0,(T-M)/2)).astype(np.int32)
regtie=h==a
# Five-minute OT branch: ~10 points/team with extra period if OT remains tied; assumption only.
for _ in range(6):
    tie=np.flatnonzero(h==a)
    if not len(tie): break
    h[tie]+=rng.poisson(10,len(tie)).astype(np.int32)
    a[tie]+=rng.poisson(10,len(tie)).astype(np.int32)
margin=h-a
total=h+a
calc={ 'WONJU_MINUS_5_5': margin>=6, 'SUWON_PLUS_5_5': margin<=5, 'OVER_179_5': total>=180, 'UNDER_179_5': total<=179 }
out={
'event':'Wonju DB Promy vs Suwon KT Sonicboom, KBL 2026-11-13 19:00 KST / 21:00 AEDT',
'status':'ASSUMPTION_DRIVEN_UNCALIBRATED_SCENARIO_NOT_PRIMARY',
'seed':seed, 'n':N, 'rho_total_margin_assumed':rho,
'season_rates':{'wonju_PF':90.1,'wonju_PA':89.3,'suwon_PF':85.0,'suwon_PA':86.5,'n_per_team':13},
'stated_half_sum_raw_team_blend_total':round((90.1+86.5+85.0+89.3)/2,2),
'scenarios':cases,
'endpoints':'FULL_GAME_INCLUDING_5MIN_OVERTIME; 4x10min regulation; margin integer; user lines half-point no push',
'ot_parameters':'scenarios use assumed regulation T/M normal, rounded team scores; ties trigger Poisson(10) points/team each 5m extra period until resolved',
'probabilities':{k:{'fraction':float(v.mean()),'mc_se':float(np.sqrt(v.mean()*(1-v.mean())/N)),'W':float(v.mean()),'P':0.0,'L':float(1-v.mean()),'V':0.0} for k,v in calc.items()},
'expected':{'wonju':float(h.mean()),'suwon':float(a.mean()),'total':float(total.mean()),'wonju_minus_suwon_margin':float(margin.mean()),'total_sd':float(total.std()),'margin_sd':float(margin.std()),'ot_rate':float(regtie.mean()),'winner_wonju':float((margin>0).mean()),'winner_suwon':float((margin<0).mean())},
'joint_failure_top_two_if_under_and_suwon_cushion':float(np.mean((total>=180)&(margin>=6))),
'limitations':['Team ORtg/DRtg/pace and lineup stints not verified','No official reference freeze, promotion, adjustment ledger or model lint','Scenario centers, rho and widths are explicit assumptions not trained, validated or market-derived','Official first tip and starting fives not verified','Includes assumed overtime mechanism and not fitted KBL overtime statistics']}
# Case-conditioned estimates from same drawn score states
out['case_probabilities']={c['name']:{k:float(v[assign==i].mean()) for k,v in calc.items()} for i,c in enumerate(cases)}
out['method']='6e5 seeded Monte Carlo draws; sample T and M correlated Gaussian per assumed regime; round home and away points; append sampled 5 minute OT points for tied regulation scores, then price supplied sides and totals.'
out['code_sha256']=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
path=pathlib.Path('/mnt/data/kbl_wonju_suwon_scenario_20261113.json')
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:round(v['fraction'],4) for k,v in out['probabilities'].items()}))
print(json.dumps({k:round(v,2) for k,v in out['expected'].items()}))
print('script_sha256',out['code_sha256'])
