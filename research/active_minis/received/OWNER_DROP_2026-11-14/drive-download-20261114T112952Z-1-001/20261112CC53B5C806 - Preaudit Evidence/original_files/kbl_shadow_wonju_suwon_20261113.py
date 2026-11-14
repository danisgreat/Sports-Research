"""Chat-local, uncalibrated Monte Carlo study, not repo model or forecast. Market blind.
Inputs from KBL schedule; StatGG pregame 2026-27 stats; AiScore dated recent results;
pre-event news Ellenson return and KT injuries. Subjective scenarios not calibrated.
"""
import json, hashlib, datetime
import numpy as np
N=1200000
seed=13112026
rng=np.random.default_rng(seed)
scenarios=[
    dict(name='low_scoring_KT_short_rotation',weight=.25,reg_wonju=89.0,reg_suwon=80.5),
    dict(name='central_regime',weight=.5,reg_wonju=90.1,reg_suwon=85.3),
    dict(name='fast_Bass_perimeter_responds',weight=.25,reg_wonju=95.0,reg_suwon=89.0)
]
sigma_t=17.93*1.10
sigma_m=13.97*1.10
rho=0.0
all_rows=[]
raw=[]
for s in scenarios:
  n=int(N*s['weight'])
  z=rng.standard_normal((2,n))
  t=s['reg_wonju']+s['reg_suwon']+sigma_t*z[0]
  m=s['reg_wonju']-s['reg_suwon']+sigma_m*(rho*z[0]+np.sqrt(1-rho**2)*z[1])
  h=np.maximum(0,np.rint((t+m)/2).astype(int))
  a=np.maximum(0,np.rint((t-m)/2).astype(int))
  draws=(h==a)
  if draws.any():
    draws_indices=np.flatnonzero(draws)
    # KBL FIBA 5min OT; approximate points pooled around 21.5, SD 7.0;
    # one overtime scorer edge picked by additional equal-centre margin perturbation.
    added=np.maximum(4,np.rint(rng.normal(21.5,7.0,len(draws_indices))).astype(int))
    h_add=rng.binomial(added,0.5)
    a_add=added-h_add
    equal=h_add==a_add
    if np.any(equal): h_add[equal]+=rng.binomial(1,0.5,equal.sum());a_add[equal]+=(h_add[equal]==added[equal]//2)
    # If still tied, add single decisive point (proxy for additional overtime continuation).
    again=h_add==a_add
    h_add[again]+=1
    h[draws_indices]+=h_add
    a[draws_indices]+=a_add
  tot=h+a; margin=h-a
  values=dict(wonju_minus5_5=float(np.mean(margin>=6)),suwon_plus5_5=float(np.mean(margin<=5)),over179_5=float(np.mean(tot>=180)),under179_5=float(np.mean(tot<=179)),wonju_win=float(np.mean(margin>0)),suwon_win=float(np.mean(margin<0)),mean_wonju=float(h.mean()),mean_suwon=float(a.mean()),mean_total=float(tot.mean()),mean_margin=float(margin.mean()),ot_rate=float(draws.mean()),joint_loss_under_and_suwon=float(np.mean((tot>=180)&(margin>=6))))
  all_rows.append(dict(scenario=s['name'],weight=s['weight'],n=n,regulation_means=[s['reg_wonju'],s['reg_suwon']],**values))
  raw.append((h,a))
h=np.concatenate([x[0] for x in raw]);a=np.concatenate([x[1] for x in raw]);tot=h+a;margin=h-a
summary=dict(wonju_minus5_5=float(np.mean(margin>=6)),suwon_plus5_5=float(np.mean(margin<=5)),over179_5=float(np.mean(tot>=180)),under179_5=float(np.mean(tot<=179)),wonju_win=float(np.mean(margin>0)),suwon_win=float(np.mean(margin<0)),mean_wonju=float(h.mean()),mean_suwon=float(a.mean()),mean_total=float(tot.mean()),sd_total=float(tot.std()),mean_margin=float(margin.mean()),sd_margin=float(margin.std()),ot_rate=float(sum(r['ot_rate']*r['weight'] for r in all_rows)),both_under_and_suwon=float(np.mean((tot<=179)&(margin<=5))),joint_loss_under_and_suwon=float(np.mean((tot>=180)&(margin>=6))),both_decisive=float(np.mean((margin>=6)|(margin<=5))))
obj=dict(status='EXECUTED_UNCALIBRATED_EXPLORATORY_SHADOW_NOT_PRIMARY',N=N,seed=seed,scenarios=all_rows,summary=summary,model='bivariate Gaussian regulation scoreboard rounded to integers + conditional equal-score 5min overtime score increments; not calibrated; no referee/foul state; scenario weights subjective.',widths=dict(total=sigma_t,margin=sigma_m,rho=rho),source_urls=['https://www.kbl.or.kr/match/schedule','https://statgg.com/en/kbl/matches/S49G01N66','https://www.aiscore.com/en/head-to-head/basketball/busan-ktf-sonicboom-vs-wonju-dongbu-promy','https://www.jumpball.co.kr/news/newsview.php?ncode=1065577530368244','https://www.dailyil.com/ko/briefing/2026-11-13_KBL/','https://en.24score.com/basketball/match/369525-wonju_db-suwon_kt'],disclaimers=['Distinct scenario weights unvalidated and not independently qualified for KBL.','No actual KBL ml reference, official pregame run or frozen card.','Overtime model is approximate: only tied regulation score receives one extra-period point proxy.','Season scoring includes historical roster and injuries; proposed adjustments illustrative and not independently measured.','Do not use retrospective match results or market lines as model features.'])
p='/mnt/data/KBL_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0005.json';open(p,'w').write(json.dumps(obj,ensure_ascii=False,indent=2));print(json.dumps(obj,ensure_ascii=False,indent=2))
