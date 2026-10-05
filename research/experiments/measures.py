"""Proper probability scores, discrete PMF diagnostics and paired block inference."""
from collections import defaultdict
import math
import numpy as np
from scipy.stats import norm

def pmf(value):
    if any(isinstance(v,bool) or not isinstance(v,(int,float)) for k in ('support','probabilities') for v in value[k]):
        raise ValueError('PMF entries must be actual numeric values, not booleans or strings')
    x=np.asarray(value['support'],dtype=float); p=np.asarray(value['probabilities'],dtype=float)
    if x.ndim!=1 or p.shape!=x.shape or not len(x) or len(x)>2000:
        raise ValueError('PMF needs 1..2000 support points and matching probabilities')
    if not np.isfinite(x).all() or not np.isfinite(p).all() or (p<0).any() or (np.diff(x)<=0).any() or abs(p.sum()-1)>1e-9:
        raise ValueError('Unordered, nonfinite or unnormalized PMF')
    return x,p

def contract_probabilities(distribution,contract):
    x,p=pmf(distribution);threshold=contract['threshold'];rule=contract['rule']
    if isinstance(threshold,bool) or not isinstance(threshold,(int,float)) or not math.isfinite(threshold):
        raise ValueError('Finite exact contract threshold required')
    if rule not in {'OVER','UNDER','HOME_1X2'}:raise ValueError('Unsupported exact sporting contract rule')
    probs=[float(p[x<threshold].sum()),float(p[x==threshold].sum()),float(p[x>threshold].sum())]
    if rule=='UNDER':probs=[probs[2],probs[1],probs[0]]
    # OVER/UNDER: LOSS,PUSH,WIN. HOME_1X2: AWAY,DRAW,HOME.
    if rule=='HOME_1X2' and threshold!=0:raise ValueError('1X2 requires margin threshold zero')
    return probs

def outcome_index(value,contract):
    if isinstance(value,bool) or not isinstance(value,(float,int)) or not math.isfinite(value):
        raise ValueError('Finite numeric sporting outcome required')
    threshold=contract['threshold'];index=0 if value<threshold else 2 if value>threshold else 1
    return 2-index if contract['rule']=='UNDER' else index

def probability_scores(probs,outcome):
    p=np.asarray(probs,dtype=float)
    if p.ndim!=1 or len(p)<2 or not np.isfinite(p).all() or (p<0).any() or abs(p.sum()-1)>1e-9:
        raise ValueError('Coherent outcome probabilities required')
    if isinstance(outcome,bool) or not isinstance(outcome,int) or not 0<=outcome<len(p):
        raise ValueError('Outcome category invalid')
    one=np.zeros(len(p));one[outcome]=1
    return dict(brier=float(np.square(p-one).sum()/2),
                logloss=float(-math.log(p[outcome])) if p[outcome]>0 else None,
                zero_probability_observed=bool(p[outcome]==0))

def distribution_scores(distribution,observed):
    x,p=pmf(distribution)
    if not math.isfinite(observed):raise ValueError('Numeric outcome required')
    # E|X-y| - .5 E|X-X'|; sorted-support O(K) form for the second term.
    before=np.cumsum(p)-p; previous_x=np.cumsum(p*x)-p*x
    crps=float(np.dot(p,np.abs(x-observed))-np.sum(p*(x*before-previous_x)))
    intervals={}
    cumulative=np.cumsum(p)
    for coverage in (.5,.8,.95):
        alpha=1-coverage
        lower=float(x[min(int(np.searchsorted(cumulative,alpha/2)),len(x)-1)])
        upper=float(x[min(int(np.searchsorted(cumulative,1-alpha/2)),len(x)-1)])
        score=upper-lower+2/alpha*(max(lower-observed,0)+max(observed-upper,0))
        intervals[str(coverage)]=dict(lower=lower,upper=upper,covered=lower<=observed<=upper,
                                      width=upper-lower,interval_score=float(score))
    return dict(crps=crps,intervals=intervals)

def reliability(probs,outcomes):
    p=np.asarray(probs,dtype=float);y=np.asarray(outcomes,dtype=int)
    if p.ndim!=2 or y.shape!=(len(p),):raise ValueError('Reliability dimensions invalid')
    output=[]; weighted_error=0
    for category in range(p.shape[1]):
        bins=[]
        for b in range(10):
            selected=(p[:,category]>=b/10)&((p[:,category]<(b+1)/10) if b<9 else (p[:,category]<=1))
            count=int(selected.sum())
            mean=float(p[selected,category].mean()) if count else None
            rate=float((y[selected]==category).mean()) if count else None
            if count:weighted_error+=count*abs(mean-rate)/(len(p)*p.shape[1])
            bins.append(dict(lower=b/10,upper=(b+1)/10,count=count,mean_probability=mean,outcome_rate=rate))
        output.append(dict(category=category,bins=bins))
    return dict(mean_category_ece=float(weighted_error),classes=output,
                limitation='Fixed-bin descriptive reliability; finite-sample ECE is not proof of calibration.')

def paired_blocks(differences,weeks,*,alpha=.05/15,reps=10000,seed=20261005,minimum_blocks=20):
    values=np.asarray(differences,dtype=float)
    if not len(values) or len(values)!=len(weeks) or not np.isfinite(values).all():
        raise ValueError('Finite paired scores and matching block IDs required')
    if not 0<alpha<1 or not isinstance(reps,int) or reps<10000:
        raise ValueError('Fixed inference settings invalid')
    groups=defaultdict(list)
    for week,value in zip(weeks,values):groups[week].append(value)
    if len(groups)<minimum_blocks:raise ValueError('Insufficient week blocks')
    sums=np.array([sum(groups[k]) for k in sorted(groups)]); counts=np.array([len(groups[k]) for k in sorted(groups)])
    rng=np.random.default_rng(seed); boot=[]
    # Bound memory for long cohorts instead of allocating reps x all blocks.
    for start in range(0,reps,250):
        pick=rng.integers(0,len(groups),size=(min(250,reps-start),len(groups)))
        boot.extend((sums[pick].sum(axis=1)/counts[pick].sum(axis=1)).tolist())
    return dict(mean=float(values.mean()),ci=np.quantile(boot,[alpha/2,1-alpha/2]).tolist(),
                confidence_level=1-alpha,events=len(values),blocks=len(groups),reps=reps,seed=seed,
                sign='candidate_minus_baseline; negative is improvement',
                limitation='Approximate paired week-block percentile inference; depends on the frozen dependence audit, not a guarantee of independent blocks.')

def paired_reliability(candidate,baseline,outcomes,weeks,*,alpha=.05/15,reps=10000,seed=20261005,minimum_blocks=20):
    """Paired week resampling of fixed-bin ECE, retaining category/bin totals."""
    c=np.asarray(candidate,dtype=float);b=np.asarray(baseline,dtype=float);y=np.asarray(outcomes,dtype=int)
    if c.shape!=b.shape or c.ndim!=2 or len(c)!=len(weeks) or y.shape!=(len(c),):
        raise ValueError('Paired reliability shapes invalid')
    for p in (c,b):
        if not np.isfinite(p).all() or (p<0).any() or (p>1).any() or not np.allclose(p.sum(axis=1),1,rtol=0,atol=1e-9):
            raise ValueError('Paired reliability probabilities invalid')
    if (y<0).any() or (y>=c.shape[1]).any():raise ValueError('Reliability outcome invalid')
    blocks=sorted(set(weeks));index={week:i for i,week in enumerate(blocks)}
    if len(blocks)<minimum_blocks or not 0<alpha<1 or reps<10000:raise ValueError('Reliability inference settings/blocks invalid')
    arrays=[];counts=np.zeros(len(blocks))
    for week in weeks:counts[index[week]]+=1
    for p in (c,b):
        residual=np.zeros((len(blocks),p.shape[1],10))
        for row,week in enumerate(weeks):
            for category in range(p.shape[1]):
                bin_id=min(int(p[row,category]*10),9)
                residual[index[week],category,bin_id]+=p[row,category]-float(y[row]==category)
        arrays.append(residual.reshape(len(blocks),-1))
    mean=(np.abs(arrays[0].sum(axis=0)).sum()-np.abs(arrays[1].sum(axis=0)).sum())/(len(c)*c.shape[1])
    rng=np.random.default_rng(seed);boot=[]
    for start in range(0,reps,250):
        n=min(250,reps-start);pick=rng.integers(0,len(blocks),size=(n,len(blocks)))
        freq=np.zeros((n,len(blocks)));np.add.at(freq,(np.arange(n)[:,None],pick),1)
        difference=(np.abs(freq@arrays[0]).sum(axis=1)-np.abs(freq@arrays[1]).sum(axis=1))/(freq@counts*c.shape[1])
        boot.extend(difference.tolist())
    return dict(mean=float(mean),ci=np.quantile(boot,[alpha/2,1-alpha/2]).tolist(),confidence_level=1-alpha,
                events=len(c),blocks=len(blocks),reps=reps,seed=seed,
                limitation='Uncertainty for a fixed-bin descriptive reliability difference; not proof of full-distribution calibration.')

def sample_plan(differences,weeks,minimum_improvement,anticipated_improvement,*,family_size=15,power=.8):
    values=np.asarray(differences,dtype=float)
    if not len(values) or len(values)!=len(weeks) or not np.isfinite(values).all():raise ValueError('Pilot differences invalid')
    if (np.abs(values)>1).any():raise ValueError('Paired Brier differences must be within [-1,1]')
    if not isinstance(minimum_improvement,(int,float)) or isinstance(minimum_improvement,bool) or not 0<minimum_improvement<1:
        raise ValueError('Justified minimum worthwhile Brier improvement required')
    if family_size!=15 or not .5<power<1:raise ValueError('Fixed comparison family or power invalid')
    if isinstance(anticipated_improvement,bool) or not isinstance(anticipated_improvement,(int,float)) or not minimum_improvement<anticipated_improvement<1:
        raise ValueError('Anticipated improvement must exceed the minimum worthwhile threshold')
    groups=defaultdict(list)
    for week,value in zip(weeks,values):groups[week].append(value)
    if len(groups)<8:raise ValueError('At least eight separate pilot week blocks required')
    mean=float(values.mean()); counts=np.array([len(v) for v in groups.values()]); sums=np.array([sum(v) for v in groups.values()])
    influence=(sums-mean*counts)/counts.mean();sd=float(influence.std(ddof=1))
    if sd<=0:raise ValueError('Degenerate pilot variation cannot establish power')
    separation=anticipated_improvement-minimum_improvement
    blocks=max(20,math.ceil(((norm.ppf(1-.05/(2*family_size))+norm.ppf(power))*sd/separation)**2))
    return dict(method='NORMAL_APPROXIMATION_BLOCK_RATIO_INFLUENCE',pilot_events=len(values),pilot_blocks=len(groups),
                alpha_family=.05,family_size=family_size,power=power,minimum_brier_improvement=minimum_improvement,
                anticipated_improvement=anticipated_improvement,
                block_influence_sd=sd,minimum_blocks=blocks,approximate_events=math.ceil(blocks*float(counts.mean())),
                limitation='Planning approximation, not achieved power; separate pilot data and a dependence audit are required before protocol freeze.')
