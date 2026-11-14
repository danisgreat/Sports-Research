"""Research-only, uncalibrated, independent FIBA-40-style score diagnostic.
No GitHub code, bookmaker prices, odds, historical outcomes, or frozen issue used.
Full-game score includes overtime. Uses transparent 3-scenario Gaussian score object.
"""
import numpy as np, json, hashlib
from pathlib import Path
ROOT=Path('/mnt/data')
SEED=202611131849
N=1200000
rng=np.random.default_rng(SEED)
# Repo FIBA-40 family prior: total SD17.93 and margin SD13.97,
# widen by 10% because exact WNBL competition row unavailable.
sd_t=17.93*1.1
sd_m=13.97*1.1
# three market-blind, data/pace sensitivity scenarios (not fitted):
# low=Geelong's home-restriction; base=matched attack/defence; high=Perth's scoring environment.
cases=[('low_geelong_control',155.0,0.0,300000,.25),('base_attack_defence',165.5,1.81,600000,.50),('high_perth_tempo',176.0,5.5,300000,.25)]
def stats(t,m):
    geelong=(t-m)/2
    perth=(t+m)/2
    # zero or higher, integer scores for regulation
    return np.rint(geelong).astype(int),np.rint(perth).astype(int)
out=[]
for name,mu_t,mu_m,n,w in cases:
    # approximate expected OT uplift .6 points (2.6% tie mass x 21 points)
    tr=rng.normal(mu_t-.55,sd_t,n)
    mr=rng.normal(mu_m,sd_m,n)
    g,p=stats(tr,mr)
    # FIBA 5 min overtime if regulation tied, until non-tie
    ot_counts=np.zeros(n,dtype=np.int8)
    pending=np.flatnonzero(g==p)
    while pending.size:
        # ~20.6 points per OT, 10.3 each team, no fitted WNBL OT rate
        d_g=rng.poisson(10.3,pending.size)
        d_p=rng.poisson(10.3,pending.size)
        g[pending]+=d_g;p[pending]+=d_p
        ot_counts[pending]+=1
        pending=pending[g[pending]==p[pending]]
    tot=g+p
    diff=p-g
    winners={'geelong':float(np.mean(diff<0)),'perth':float(np.mean(diff>0))}
    geelong_cover=(diff<=6)
    perth_cover=(diff>=7)
    over=(tot>=164)
    under=(tot<=163)
    d={'name':name,'scenario_weight':w,'n':n,'inputs':{'mu_regulation_total_before_ot_offset':mu_t-.55,'mu_final_target_total':mu_t,'mu_perth_minus_geelong':mu_m,'sd_total':sd_t,'sd_margin':sd_m,'assumed_corr_total_margin':0.0},
    'simulated':{'geelong_plus_6_5':float(np.mean(geelong_cover)),'perth_minus_6_5':float(np.mean(perth_cover)),'over_163_5':float(np.mean(over)),'under_163_5':float(np.mean(under)),
    'geelong_wins':winners['geelong'],'perth_wins':winners['perth'],'average_geelong_pts':float(g.mean()),'average_perth_pts':float(p.mean()),'average_total':float(tot.mean()),'average_perth_margin':float(diff.mean()),'ot_frequency':float(np.mean(ot_counts>0)),
    'joint_failure_geelong_cushion_and_over':float(np.mean(~geelong_cover & ~over)), 'joint_failure_geelong_cushion_and_under':float(np.mean(~geelong_cover & ~under))}}
    assert np.all((geelong_cover ^ perth_cover))
    assert np.all((over ^ under))
    assert np.all(diff!=0)
    out.append(d)
keys=list(out[0]['simulated'].keys())
mixture={k:sum(x['scenario_weight']*x['simulated'][k] for x in out) for k in keys}
for a,b in [('geelong_plus_6_5','perth_minus_6_5'),('over_163_5','under_163_5'),('geelong_wins','perth_wins')]:assert abs(mixture[a]+mixture[b]-1)<1e-6
report={'type':'LOCAL_RESEARCH_UNCALIBRATED_SHADOW','event':'2026-11-13 19:00 AEDT, WNBL Geelong Venom v Perth Lynx','seed':SEED,'n':N,'scenario_weights':[x[4] for x in cases], 'sources':{'official_fixtures':'https://www.wnbl.com.au/news/how-to-watch-geelong-v-perth','season_scores':['https://schedule.nbl.com.au/wnbl','https://www.wnbl.com.au/news/lynx-hold-strong-to-overcome-spirit','https://www.sofascore.com/basketball/match/perth-lynx-adelaide-lightning/RQYsiRY']},'historic_inputs':{'geelong_for':[90,74,68,77,67],'geelong_against':[103,69,77,70,80],'perth_for':[86,90,86,94],'perth_against':[83,82,99,84], 'geelong_home_totals':[143,145,147],'perth_away_totals':[172,185]},'reference':{'family_prior':'BASKETBALL_FIBA40','prior_mean_total':166.65,'prior_total_sd':17.93,'prior_margin_sd':13.97,'no_WNBL_row':True},'assumptions':['Results are unvalidated conditional probabilities and NOT official p_card.','Independent regulation total and margin normal draws with integer score rounding; covariance not fitted.','Small-sample league scores control centre, no teammate-minute-usage model.','Overtime branch: regulation tie after rounding triggers 5-min Poisson additions to each team, repeated until no tie.','No released reference receipt, prospective evaluation, calibration or freeze was executed.','Model does not use current/future score, live scores or any betting prices.'], 'scenarios':out,'mixture':mixture}
path=ROOT/'WNBL_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0004.json'
path.write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'file':str(path),'n':N,'scenario':[(x['name'],x['simulated']['geelong_plus_6_5'],x['simulated']['over_163_5']) for x in out],'mix':mixture},indent=2))
