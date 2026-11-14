import json, math, hashlib
from pathlib import Path
import numpy as np
from scipy.stats import poisson
P=Path('/mnt/data'); rng=np.random.default_rng(2026111202)
scenarios={
 'lower_scoring_weak_opponents_removed':{'lam_torpedo':3.17,'lam_arlan':1.77,'weight':0.25,'basis':'multiplicative team attack-vs-opponent-defence rates after omitting Ertis fixtures; rounding'},
 'mid_condition':{'lam_torpedo':3.55,'lam_arlan':2.05,'weight':0.5,'basis':'intermediate scoring assumptions between league-shrunk and additive seasonal estimates, not fitted'},
 'high_scoring_unadjusted_raw':{'lam_torpedo':3.77,'lam_arlan':2.66,'weight':0.25,'basis':'mean of each side seasonal GF and opponent seasonal GA, most aggressive combination'},
}
# Scope: purely unvalidated scenario-sensitivity diagnostics, NOT a frozen released forecast.
# 60-min goals independent Poisson, with a tie broken by exactly one extra full-match goal.
# Winner of OT/SO in simulation is weighted by team's scenario scoring parameter.
N=400000
results={}; allc={k:0 for k in ['t_minus1_5','a_plus1_5','under6_5','over6_5','torpedo_full_win','arlan_full_win','regulation_tie','regulation_under6_5','both_under_and_a_plus']}
for name,ss in scenarios.items():
    t=rng.poisson(ss['lam_torpedo'],N);a=rng.poisson(ss['lam_arlan'],N)
    tie=t==a
    ot_t=(rng.random(N)<ss['lam_torpedo']/(ss['lam_torpedo']+ss['lam_arlan']))&tie
    ot_a=tie&(~ot_t)
    ft=t+ot_t;fa=a+ot_a
    r={
     't_minus1_5':float((ft-fa>=2).mean()),
     'a_plus1_5':float((ft-fa<=1).mean()),
     'under6_5':float(((ft+fa)<=6).mean()),
     'over6_5':float(((ft+fa)>=7).mean()),
     'torpedo_full_win':float((ft>fa).mean()),
     'arlan_full_win':float((fa>ft).mean()),
     'regulation_tie':float(tie.mean()),
     'regulation_under6_5':float(((t+a)<=6).mean()),
     'both_under_and_a_plus':float(((ft+fa<=6)&(ft-fa<=1)).mean()),
    }
    r.update(ss);r['n']=N;r['mean_full_torpedo']=float(ft.mean());r['mean_full_arlan']=float(fa.mean());r['mean_full_total']=float((ft+fa).mean())
    results[name]=r
mix={k:sum(v['weight']*v[k] for v in results.values()) for k in allc}
mix.update({'mean_full_total':sum(v['weight']*v['mean_full_total'] for v in results.values()),'mean_full_torpedo':sum(v['weight']*v['mean_full_torpedo'] for v in results.values()),'mean_full_arlan':sum(v['weight']*v['mean_full_arlan'] for v in results.values())})
Ntotal=3*N
print(json.dumps({'scenarios':results,'mixture':mix,'draws':Ntotal},indent=2))
obj={'status':'EXPLORATORY_SHADOW_NOT_PRIMARY','model':'independent 60min poisson with separate 1-goal tied regulation OT/SO branch, no explicit late empty-net process','endpoint':'ASSUMED_FULL_MATCH_INCLUDING_OT_SO (operator definition unknown)','seed':2026111202,'simulations_total':Ntotal,'scenarios':results,'mixture':mix,'limitations':['NOT a validated league forecast or source-frozen pregame issued model','unconfirmed goalies/rosters','sources as-of and match live state not fully verified','season scores include OT/SO final scores in attack estimates so a small amount of extra-time goal double counting occurs','home advantage not league-fit','1-goal OT/SO branch stylized; shootout scores convention may differ','no explicit empty-net scoring state; could shift puck lines and totals','scenario weights 0.25/0.5/0.25 are assumptions not estimated']}
path=P/'HOCKEY_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0002.json'; path.write_text(json.dumps(obj,indent=2)+'\n')
for p in [path,Path(__file__)]:print(str(p),hashlib.sha256(p.read_bytes()).hexdigest())
