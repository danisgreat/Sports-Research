const DEFAULT_TOLERANCE = 1e-9;
export const SCORING_SPEC_VERSION = 'SPORTS_SCORE_V3_20260716';

export function validateProbabilityVector(probabilities, tolerance = DEFAULT_TOLERANCE, { allowStructuralBoundary = false, structuralMask = [] } = {}) {
  const errors = [];
  if (!Array.isArray(probabilities) || probabilities.length < 2) {
    return ['probability vector must contain at least two branches'];
  }
  probabilities.forEach((probability, index) => {
    if (typeof probability !== 'number' || !Number.isFinite(probability)) {
      errors.push(`branch ${index}: probability must be finite`);
    } else if (probability < 0 || probability > 1) {
      errors.push(`branch ${index}: probability must be in [0,1]`);
    } else if (!allowStructuralBoundary && !structuralMask[index] && (probability === 0 || probability === 1)) {
      errors.push(`branch ${index}: non-structural probability must be strictly inside (0,1)`);
    }
  });
  const sum = probabilities.reduce((total, probability) => total + probability, 0);
  if (Math.abs(sum - 1) > tolerance) errors.push(`probabilities sum to ${sum}; tolerance is ${tolerance}`);
  return errors;
}

export function brierLoss(probabilities, observedIndex) {
  if (!Number.isInteger(observedIndex) || observedIndex < 0 || observedIndex >= probabilities.length) {
    throw new RangeError('observedIndex is outside the probability vector');
  }
  return probabilities.reduce((sum, probability, index) => {
    const observed = index === observedIndex ? 1 : 0;
    return sum + (probability - observed) ** 2;
  }, 0) / 2;
}

export function logLoss(probabilities, observedIndex) {
  if (!Number.isInteger(observedIndex) || observedIndex < 0 || observedIndex >= probabilities.length) {
    throw new RangeError('observedIndex is outside the probability vector');
  }
  return probabilities[observedIndex] === 0 ? Number.POSITIVE_INFINITY : -Math.log(probabilities[observedIndex]);
}

export function proportionalNoVig(decimalPrices) {
  if (!Array.isArray(decimalPrices) || decimalPrices.length < 2) throw new TypeError('at least two decimal prices are required');
  const implied = decimalPrices.map((price, index) => {
    if (typeof price !== 'number' || !Number.isFinite(price) || price <= 1) {
      throw new RangeError(`decimal price ${index} must be finite and greater than 1`);
    }
    return 1 / price;
  });
  const bookSum = implied.reduce((sum, value) => sum + value, 0);
  return {
    raw_implied_probabilities: implied,
    overround: bookSum - 1,
    no_vig_probabilities: implied.map((value) => value / bookSum),
  };
}

export function conditionalProbability(numerator, denominatorParts) {
  const denominator = denominatorParts.reduce((sum, value) => sum + value, 0);
  if (!(denominator > 0)) throw new RangeError('conditioning event has zero probability');
  return numerator / denominator;
}

export function expectedReturn(branchProbabilities, branchNetPayoffs) {
  if (!Array.isArray(branchProbabilities) || branchProbabilities.length !== branchNetPayoffs.length) {
    throw new TypeError('probability and payoff vectors must have equal length');
  }
  const errors = validateProbabilityVector(branchProbabilities, DEFAULT_TOLERANCE, { allowStructuralBoundary: true });
  if (errors.length) throw new RangeError(errors.join('; '));
  return branchProbabilities.reduce((sum, probability, index) => {
    const payoff = branchNetPayoffs[index];
    if (typeof payoff !== 'number' || !Number.isFinite(payoff)) throw new TypeError(`payoff ${index} must be finite`);
    return sum + probability * payoff;
  }, 0);
}

export function scoreDistribution(states, observedStateId) {
  if (!Array.isArray(states) || states.length < 2) throw new TypeError('states must contain at least two branches');
  const observedIndex = states.findIndex((state) => state.settlement_state_id === observedStateId);
  if (observedIndex < 0) throw new Error(`observed state ${observedStateId} is not in the forecast distribution`);
  const probabilities = states.map((state) => state.decision_probability);
  const validationErrors = validateProbabilityVector(probabilities, DEFAULT_TOLERANCE, {
    structuralMask: states.map((state) => state.is_structural === true),
  });
  if (validationErrors.length) throw new Error(validationErrors.join('; '));
  return {
    brier_loss: brierLoss(probabilities, observedIndex),
    log_loss: logLoss(probabilities, observedIndex),
  };
}

// Exact linked-market checks need a declared relation; line direction is never guessed.
export function validateLinkedMarketCoherence(relations, distributions, tolerance = 1e-9) {
  const errors = [];
  if (!Array.isArray(relations) || !Array.isArray(distributions)) return ['relations and distributions must be arrays'];
  const distributionIds = distributions.map((distribution) => distribution.forecast_distribution_id);
  if (distributionIds.some((id) => !id) || new Set(distributionIds).size !== distributionIds.length) {
    errors.push('forecast_distribution_id values must be unique and nonempty');
  }
  const byId = new Map(distributions.map((distribution) => [distribution.forecast_distribution_id, distribution]));
  const relationIds = new Set();
  for (const relation of relations ?? []) {
    if (!relation?.relation_id || relationIds.has(relation.relation_id)) errors.push(`${relation?.relation_id ?? '<missing>'}: relation_id must be unique and nonempty`);
    relationIds.add(relation?.relation_id);
    if (!['LEFT_GTE_RIGHT', 'EQUAL'].includes(relation?.constraint)) {
      errors.push(`${relation?.relation_id ?? '<missing>'}: unknown constraint ${relation?.constraint ?? '<missing>'}`);
      continue;
    }
    const left = byId.get(relation.left_distribution_id);
    const right = byId.get(relation.right_distribution_id);
    if (!left || !right) {
      errors.push(`${relation.relation_id}: linked distribution missing`);
      continue;
    }
    if (!Array.isArray(relation.left_winning_state_ids) || relation.left_winning_state_ids.length === 0
      || !Array.isArray(relation.right_winning_state_ids) || relation.right_winning_state_ids.length === 0) {
      errors.push(`${relation.relation_id}: both winning-state sets must be nonempty arrays`);
      continue;
    }
    const leftStates = new Set(left.states?.map((state) => state.settlement_state_id));
    const rightStates = new Set(right.states?.map((state) => state.settlement_state_id));
    const missingLeft = relation.left_winning_state_ids.filter((id) => !leftStates.has(id));
    const missingRight = relation.right_winning_state_ids.filter((id) => !rightStates.has(id));
    if (missingLeft.length || missingRight.length) {
      errors.push(`${relation.relation_id}: unknown state ids left=${missingLeft.join('|') || 'none'} right=${missingRight.join('|') || 'none'}`);
      continue;
    }
    const leftProbability = left.states
      .filter((state) => relation.left_winning_state_ids.includes(state.settlement_state_id))
      .reduce((sum, state) => sum + state.decision_probability, 0);
    const rightProbability = right.states
      .filter((state) => relation.right_winning_state_ids.includes(state.settlement_state_id))
      .reduce((sum, state) => sum + state.decision_probability, 0);
    if (relation.constraint === 'LEFT_GTE_RIGHT' && leftProbability + tolerance < rightProbability) {
      errors.push(`${relation.relation_id}: ${leftProbability} is below nested probability ${rightProbability}`);
    } else if (relation.constraint === 'EQUAL' && Math.abs(leftProbability - rightProbability) > tolerance) {
      errors.push(`${relation.relation_id}: linked probabilities differ (${leftProbability} vs ${rightProbability})`);
    }
  }
  return errors;
}
