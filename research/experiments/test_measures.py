"""Synthetic arithmetic checks; these fixtures are not empirical experiments."""
import math
import numpy as np
import pytest
from .measures import (contract_probabilities,distribution_scores,outcome_index,paired_blocks,
                       paired_reliability,pmf,probability_scores,reliability,sample_plan)

def test_brier_scale_matches_binary_and_1x2():
    assert probability_scores([.25,.75],1)['brier']==pytest.approx(.0625)
    assert probability_scores([.25,0,.75],2)['brier']==pytest.approx(.0625)
    assert probability_scores([.2,.3,.5],2)['brier']==pytest.approx(.19)
    assert probability_scores([.25,.75],1)['logloss']==pytest.approx(-math.log(.75))

def test_zero_probability_is_explicit_infinite_loss_not_clipped():
    result=probability_scores([1.,0.],1)
    assert result['logloss'] is None and result['zero_probability_observed'] is True

@pytest.mark.parametrize('distribution',[
    {'support':[0,1],'probabilities':[.2,.2]},
    {'support':[1,0],'probabilities':[.5,.5]},
    {'support':[0,0],'probabilities':[.5,.5]},
    {'support':[0,1],'probabilities':[-.1,1.1]},
    {'support':[0,1],'probabilities':[float('nan'),.5]},
    {'support':[0,1],'probabilities':[True,False]},
    {'support':[0,1],'probabilities':['.5','.5']},
])
def test_invalid_pmf_is_rejected(distribution):
    with pytest.raises(ValueError):pmf(distribution)

def test_integer_push_and_direction_are_not_silently_dropped():
    distribution=dict(support=[0,1,2],probabilities=[.2,.3,.5])
    over=dict(threshold=1,rule='OVER');under=dict(threshold=1,rule='UNDER')
    assert contract_probabilities(distribution,over)==pytest.approx([.2,.3,.5])
    assert contract_probabilities(distribution,under)==pytest.approx([.5,.3,.2])
    assert outcome_index(1,over)==1 and outcome_index(2,under)==0
    assert contract_probabilities(distribution,dict(threshold=1.5,rule='OVER'))==pytest.approx([.5,0,.5])

def test_crps_matches_independent_double_sum_with_unequal_support_spacing():
    x=[-3,1,5];p=[.2,.5,.3];y=2
    expected=sum(prob*abs(value-y) for value,prob in zip(x,p))-.5*sum(pa*pb*abs(a-b) for a,pa in zip(x,p) for b,pb in zip(x,p))
    assert distribution_scores(dict(support=x,probabilities=p),y)['crps']==pytest.approx(expected)

def test_degenerate_distribution_and_outside_support_interval_penalty():
    scores=distribution_scores(dict(support=[2],probabilities=[1]),5)
    assert scores['crps']==3
    assert scores['intervals']['0.8']['interval_score']==pytest.approx(30)
    assert scores['intervals']['0.95']['covered'] is False

def test_reliability_includes_empty_bins_and_probability_one():
    result=reliability([[0,1],[0,1]],[1,1])
    assert result['mean_category_ece']==0
    assert result['classes'][1]['bins'][-1]['count']==2
    assert result['classes'][1]['bins'][0]['outcome_rate'] is None

def test_week_bootstrap_weights_events_not_week_means_and_is_paired():
    result=paired_blocks([-.1,-.1,.2],['A','A','B'],minimum_blocks=2)
    assert result['mean']==pytest.approx(0)
    assert result['events']==3 and result['blocks']==2
    assert result['confidence_level']==pytest.approx(1-.05/15)
    assert result==paired_blocks([-.1,-.1,.2],['A','A','B'],minimum_blocks=2)

def test_more_rows_in_one_week_cannot_supply_independent_blocks():
    with pytest.raises(ValueError,match='week blocks'):paired_blocks([0]*100,['A']*100)

def test_identical_models_have_zero_paired_reliability_difference():
    p=[[.2,.8]]*20;y=[1]*20;weeks=[str(i) for i in range(20)]
    result=paired_reliability(p,p,y,weeks)
    assert result['mean']==0 and result['ci']==[0,0]

def test_power_plan_targets_improvement_beyond_acceptance_margin():
    d=[-.03+(.01 if i%2 else -.01) for i in range(8)];weeks=[str(i) for i in range(8)]
    wide=sample_plan(d,weeks,.005,.03)
    close=sample_plan(d,weeks,.005,.006)
    assert close['minimum_blocks']>wide['minimum_blocks']
    assert close['family_size']==15 and close['minimum_blocks']>=20
    with pytest.raises(ValueError,match='exceed'):sample_plan(d,weeks,.005,.005)

def test_zero_variation_does_not_manufacture_power():
    with pytest.raises(ValueError,match='Degenerate'):sample_plan([0]*8,[str(i) for i in range(8)],.005,.02)
