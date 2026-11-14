"""Chat-local independent diagnostic for Kawasaki vs Saga, 2026-11-13.
No GitHub writes, no fitted or qualified model, no outcome or betting inputs.
Historical results are prior to scheduled 19:05 JST start. Not an issued forecast.
Run: python b_league_20261113_kawasaki_saga_diagnostic.py
"""
import numpy as np
from math import erf, sqrt

# Official B.PREMIER table (as of games ended Nov 12 2026):
# https://www.bleague.jp/en/standings/
KAWASAKI=(16,1256,1355)
SAGA=(14,1095,1333)
# Each tuple is date, points scored, points allowed in reverse chronological order.
# Official Kawasaki reports: https://kawasaki-bravethunders.com/game-report/?month=all&year=all
# Official Saga records: https://www.bleague.jp/record/?club1=1638&club2=0
K10=[('11-11',74,95),('11-09',76,85),('11-06',75,81),('11-01',66,77),('10-31',65,75),('10-26',92,89),('10-24',82,93),('10-21',101,67),('10-19',69,80),('10-16',74,82),('10-10',82,94),('10-08',87,81),('10-04',82,74),('10-03',90,99),('09-27',78,90),('09-26',63,93)]
S10=[('11-08',103,111),('11-01',78,84),('10-31',83,100),('10-26',88,112),('10-21',66,84),('10-18',70,115),('10-16',90,109),('10-12',61,72),('10-10',84,77),('10-08',74,90),('10-04',89,93),('10-03',61,97),('09-27',61,89),('09-25',87,100)]

def rates(x):return float(np.mean([v[1] for v in x])),float(np.mean([v[2] for v in x]))

def estimate():
    _, kp,ka=KAWASAKI; _,sp,sa=SAGA
    # Equal opponent attack vs defense blend. Season weight 75%, L5 25%; declarative, not optimized.
    season_home=(kp/16+sa/14)/2
    season_away=(sp/14+ka/16)/2
    k5,s5=rates(K10[:5]),rates(S10[:5])
    recent_home=(k5[0]+s5[1])/2
    recent_away=(s5[0]+k5[1])/2
    mu_h=.75*season_home+.25*recent_home
    mu_a=.75*season_away+.25*recent_away
    return mu_h,mu_a,((season_home,season_away),(recent_home,recent_away))

mu_h,mu_a,parts=estimate()
mu_t,mu_m=mu_h+mu_a,mu_h-mu_a
# Regime: 40-minute 4Q, plus hypothetical 5-minute OT if a tied regulation score.
# Old B.League raw SDs are NOT transferred as actual B.PREMIER parameters;
# sigma_total=20, sigma_margin=16.5 are uncertainty assumptions, varied in scenarios.
def simulate(n=200000,seed=20261113,mu_total=mu_t,mu_margin=mu_m,sigma_total=20.0,sigma_margin=16.5):
    rng=np.random.default_rng(seed)
    # Regulation mean total adjusted by ~0.4 for plausible rare overtime scoring.
    t_reg=rng.normal(mu_total-0.4,sigma_total,n)
    m_reg=rng.normal(mu_margin,sigma_margin,n)
    h=np.maximum(0,np.rint((t_reg+m_reg)/2)).astype('int32')
    a=np.maximum(0,np.rint((t_reg-m_reg)/2)).astype('int32')
    ot_start=(h==a)
    # Illustrative 5-minute overtime points (unvalidated Poisson(8)); continue until tie broken.
    active=ot_start.copy()
    for i in range(6):
        ix=np.where(active)[0]
        if len(ix)==0:break
        h[ix]+=rng.poisson(8,len(ix))
        a[ix]+=rng.poisson(8,len(ix))
        active=(h==a)
    if np.any(active):
        ix=np.where(active)[0]
        h[ix]+=rng.integers(0,2,len(ix))
        a[ix]+=(h[ix]==a[ix])
    total=h+a; margin=h-a
    return {'N':n,'seed':seed,'mu_home':np.mean(h),'mu_away':np.mean(a),'mu_total':np.mean(total),
        'mu_margin':np.mean(margin),'ot_rate':np.mean(ot_start),'regulation_draw_rate':np.mean(ot_start),
        'sigma_total':float(np.std(total)),'sigma_margin':float(np.std(margin)),
        'kawasaki_m9p5':np.mean(margin>=10),'saga_p9p5':np.mean(margin<=9),
        'over169p5':np.mean(total>=170),'under169p5':np.mean(total<=169),
        'kawasaki_win':np.mean(margin>0),'saga_win':np.mean(margin<0),
        'ties_final':np.mean(margin==0),
        'count_covered_saga':int(np.sum(margin<=9))}
if __name__=='__main__':
    print('Season result PF,PA',KAWASAKI,SAGA)
    for team,rows in [('Kawasaki',K10),('Saga',S10)]:
        for period,n in [('L5',5),('L10',10),('L15',min(15,len(rows))),('L20',min(20,len(rows)))]:
            print(team,period,'true_n',n,'rates',rates(rows[:n]),'record',sum(x[1]>x[2] for x in rows[:n]),'wins')
        print(team,'season_points_check',sum(x[1] for x in rows),sum(x[2] for x in rows))
    print('season pairing, recent L5 pairing:',parts)
    print('base pre-OT forecast: H,A,total,margin=',mu_h,mu_a,mu_t,mu_m)
    for label,t,m in [('LOW_TOTAL_CLOSE',mu_t-8,mu_m-4),('CENTRAL',mu_t,mu_m),('HIGH_TOTAL_FAV',mu_t+8,mu_m+4)]:
        print(label,simulate(mu_total=t,mu_margin=m))
