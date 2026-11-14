"""Illustrative deterministic game/set/match model for the Piros-Altmaier Orleans ATP Challenger 125 contracts.
No market inputs; not a calibrated model or repository release.
"""
from functools import lru_cache
from collections import defaultdict


def hold_from_point(p):
    q=1-p
    return p**4*(1+4*q+10*q*q)+20*p**3*q**3 * (p*p/(p*p+q*q))

@lru_cache(None)
def tiebreak_chance(i,j,first,pA,pB):
    if (i>=7 or j>=7) and abs(i-j)>=2:
        return float(i>j)
    n=i+j
    if i==j and i>=6:
        # At n>=12, next two serves are from opposing players; first-order invariant.
        w=pA*(1-pB); l=(1-pA)*pB
        return w/(w+l)
    srv=first if n==0 or ((n-1)//2)%2==1 else 1-first
    # Verify first,receiver,receiver,first,first,...
    pa=pA if srv==0 else 1-pB
    return pa*tiebreak_chance(i+1,j,first,pA,pB)+(1-pa)*tiebreak_chance(i,j+1,first,pA,pB)


def set_distribution(initial_server,pA,pB):
    hA=hold_from_point(pA);hB=hold_from_point(pB)
    @lru_cache(None)
    def go(a,b):
        res=defaultdict(float)
        total=a+b
        current=initial_server if total%2==0 else 1-initial_server
        if (a>=6 or b>=6) and abs(a-b)>=2:
            res[(int(a>b),a,b,current)]=1.
        elif a==b==6:
            ptb=tiebreak_chance(0,0,current,pA,pB)
            ns=1-current
            res[(1,7,6,ns)] = ptb
            res[(0,6,7,ns)] = 1-ptb
        else:
            gameA=hA if current==0 else 1-hB
            for (w,ga,gb,ns),prob in go(a+1,b).items():res[(w,ga,gb,ns)]+=gameA*prob
            for (w,ga,gb,ns),prob in go(a,b+1).items():res[(w,ga,gb,ns)]+=(1-gameA)*prob
        return dict(res)
    return go(0,0)


def match_distribution(pA,pB):
    sets={i:set_distribution(i,pA,pB) for i in (0,1)}
    result=defaultdict(float)
    def explore(sa,sb,ga,gb,first,weight,setsPlayed):
        if sa>=2 or sb>=2:
            result[(int(sa>sb),ga,gb,setsPlayed)] +=weight
            return
        for (wa,oa,ob,nextServer),p in sets[first].items():
            explore(sa+wa,sb+1-wa,ga+oa,gb+ob,nextServer,weight*p,setsPlayed+1)
    explore(0,0,0,0,0,.5,0)
    explore(0,0,0,0,1,.5,0)
    Z=sum(result.values())
    assert abs(Z-1.)<1e-8,Z
    return result


def summarize(dist):
    return dict(
        pAwin=sum(p for (w,a,b,ss),p in dist.items() if w),
        pAplus25=sum(p for (w,a,b,ss),p in dist.items() if a-b>=-2),
        pBminus25=sum(p for (w,a,b,ss),p in dist.items() if b-a>=3),
        pUnder225=sum(p for (w,a,b,ss),p in dist.items() if a+b<=22),
        pOver225=sum(p for (w,a,b,ss),p in dist.items() if a+b>=23),
        p3sets=sum(p for (w,a,b,ss),p in dist.items() if ss==3),
        expectedA=sum(a*p for (w,a,b,ss),p in dist.items()),
        expectedB=sum(b*p for (w,a,b,ss),p in dist.items()),
        expectedSets=sum(ss*p for (w,a,b,ss),p in dist.items()),
        pBothLossOverAndPirosPlus=sum(p for (w,a,b,ss),p in dist.items() if a-b<=-3 and a+b<=22),
    )


if __name__=='__main__':
    # Frozen hypothetical assumptions, not estimates fitted to verified raw point-count data.
    # A = Piros, B = Altmaier; best-of-three; standard set TB 7 points at 6-6.
    # Low/base/high weights = .25/.50/.25, declared before evaluating model.
    cases=[('Altmaier_serve_edge',0.638,0.668,0.25),
           ('close_elo_baseline',0.647,0.658,0.50),
           ('Piros_indoor_strength',0.666,0.646,0.25)]
    ensemble=defaultdict(float)
    for tag,pA,pB,w in cases:
        d=match_distribution(pA,pB)
        for k,v in d.items(): ensemble[k]+=w*v
        print(tag, 'serve_point',pA,pB,'weight',w,'hold',round(hold_from_point(pA),5),round(hold_from_point(pB),5), 'metrics', {k:round(v,5) for k,v in summarize(d).items()})
    print('mixture', {k:round(v,6) for k,v in summarize(ensemble).items()})
    print('checksum',round(sum(ensemble.values()),12), 'states',len(ensemble))
    # This model is strictly a sensitivity diagnostic; no market data used,
    # no validated tennis Elo snapshot / no calibrated conditional serve inputs,
    # no certified p_card, no Monte Carlo, no GitHub issuance or freeze.
