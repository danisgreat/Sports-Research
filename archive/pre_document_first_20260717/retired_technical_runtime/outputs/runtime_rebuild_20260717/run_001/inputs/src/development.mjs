import { compareCanonicalStrings, hashObject, isSha256, parseUtc } from './canonical.mjs';

const PARTITION_ORDER = ['TRAIN', 'TUNE', 'CALIBRATION', 'UNTOUCHED_TEST', 'PROSPECTIVE_SHADOW'];
const GUARDRAIL_METRICS = new Set([
  'CALIBRATION_INTERCEPT_ABS', 'CALIBRATION_SLOPE_DEVIATION_ABS', 'ECE', 'MAX_BIN_GAP',
  'TAIL_LOG_LOSS', 'SEGMENT_SCORE_DELTA', 'INTERVAL_COVERAGE', 'AURC',
]);

export function validateDevelopmentPlan(plan) {
  const errors = [];
  if (!plan || typeof plan !== 'object' || Array.isArray(plan)) return ['development plan must be an object'];
  for (const field of ['plan_version', 'hypothesis_family_id', 'model_id', 'model_version', 'primary_metric']) {
    if (!plan?.[field]) errors.push(`missing ${field}`);
  }
  if (!['BRIER', 'LOG_LOSS', 'CRPS', 'RPS', 'JOINT_LOG_SCORE'].includes(plan.primary_metric)) errors.push('primary_metric is not controlled');
  const scopeFields = ['sport_family', 'competition_id', 'market_family', 'forecast_state', 'horizon_bucket_id', 'settlement_convention_id'];
  for (const field of scopeFields) {
    if (!plan.scope?.[field] || String(plan.scope[field]).includes('ALL')) errors.push(`scope.${field} must be exact and cannot contain ALL`);
  }
  const partitions = plan?.partitions ?? [];
  if (!Array.isArray(partitions)) return [...errors, 'partitions must be an array'];
  for (const partition of partitions) {
    if (!PARTITION_ORDER.includes(partition?.role)) errors.push(`unknown partition role ${partition?.role ?? '<missing>'}`);
  }
  for (const role of PARTITION_ORDER) {
    if (partitions.filter((partition) => partition.role === role).length !== 1) errors.push(`exactly one ${role} partition is required`);
  }
  const byRole = new Map(partitions.map((partition) => [partition.role, partition]));
  let previousEnd = Number.NEGATIVE_INFINITY;
  const seenEvents = new Map();
  for (const role of PARTITION_ORDER) {
    const partition = byRole.get(role);
    if (!partition) continue;
    try {
      const start = parseUtc(partition.start_utc, `${role}.start_utc`);
      const end = parseUtc(partition.end_utc, `${role}.end_utc`);
      if (start >= end) errors.push(`${role}: start must precede end`);
      if (start < previousEnd) errors.push(`${role}: half-open [start,end) partitions overlap`);
      previousEnd = end;
    } catch (error) { errors.push(error.message); }
    try { parseUtc(partition.labels_available_by_utc, `${role}.labels_available_by_utc`); } catch (error) { errors.push(error.message); }
    if (!isSha256(partition.event_manifest_hash)) errors.push(`${role}: invalid event_manifest_hash`);
    if (!Array.isArray(partition.event_ids) || partition.event_ids.length === 0) errors.push(`${role}: event_ids are required`);
    else {
      const sortedIds = [...partition.event_ids].sort(compareCanonicalStrings);
      const expectedManifestHash = hashObject({ manifest_version: 'SPORTS_EVENT_ID_MANIFEST_V1', role, event_ids: sortedIds });
      if (partition.event_manifest_hash !== expectedManifestHash) errors.push(`${role}: event_manifest_hash does not match event_ids`);
    }
    if (!partition.purge_rule_id || !partition.label_availability_rule) errors.push(`${role}: purge_rule_id and label_availability_rule are required`);
    for (const eventId of partition.event_ids ?? []) {
      if (seenEvents.has(eventId)) errors.push(`${eventId}: overlaps ${seenEvents.get(eventId)} and ${role}`);
      seenEvents.set(eventId, role);
    }
  }
  for (let index = 0; index < PARTITION_ORDER.length - 1; index += 1) {
    const current = byRole.get(PARTITION_ORDER[index]);
    const next = byRole.get(PARTITION_ORDER[index + 1]);
    if (!current || !next) continue;
    try {
      if (parseUtc(current.labels_available_by_utc, `${current.role}.labels_available_by_utc`) > parseUtc(next.start_utc, `${next.role}.start_utc`)) {
        errors.push(`${current.role}: labels were not available before ${next.role} began`);
      }
    } catch (error) { errors.push(error.message); }
  }
  if (byRole.get('UNTOUCHED_TEST')?.test_status !== 'PLANNED_UNTOUCHED') errors.push('untouched test must begin PLANNED_UNTOUCHED');
  if (byRole.get('PROSPECTIVE_SHADOW')?.test_status !== 'PLANNED_UNTOUCHED') errors.push('prospective shadow must begin PLANNED_UNTOUCHED');

  if (!plan.baseline?.baseline_id || !plan.baseline?.version) errors.push('frozen naive baseline ID/version is required');
  if (!(typeof plan.promotion_rule?.minimum_score_improvement === 'number' && plan.promotion_rule.minimum_score_improvement > 0)) {
    errors.push('positive minimum_score_improvement is required');
  }
  if (!(Number.isInteger(plan.promotion_rule?.minimum_effective_n) && plan.promotion_rule.minimum_effective_n > 0)) {
    errors.push('positive minimum_effective_n is required');
  }
  if (!(plan.promotion_rule?.confidence_level > 0 && plan.promotion_rule.confidence_level < 1)) errors.push('confidence_level must be in (0,1)');
  if (!(typeof plan.promotion_rule?.required_lower_bound === 'number'
    && plan.promotion_rule.required_lower_bound >= plan.promotion_rule.minimum_score_improvement)) {
    errors.push('required_lower_bound must be numeric and at least the minimum improvement');
  }
  if (!['ROW_EQUAL', 'CLUSTER_EQUAL'].includes(plan.promotion_rule?.point_weighting)
    || plan.promotion_rule?.resampling_unit !== 'EVENT_CLUSTER') errors.push('point weighting and EVENT_CLUSTER resampling must be preregistered');
  const validGuardrail = (guardrail) => {
    if (!guardrail || !GUARDRAIL_METRICS.has(guardrail.metric) || !['LTE', 'GTE', 'BETWEEN'].includes(guardrail.operator)
      || !Number.isInteger(guardrail.minimum_n) || guardrail.minimum_n < 1) return false;
    if (guardrail.operator === 'BETWEEN') return Number.isFinite(guardrail.lower) && Number.isFinite(guardrail.upper) && guardrail.lower <= guardrail.upper;
    return Number.isFinite(guardrail.threshold);
  };
  if (!Array.isArray(plan.calibration_guardrails) || plan.calibration_guardrails.length === 0
    || !plan.calibration_guardrails.every(validGuardrail)) errors.push('at least one executable calibration guardrail is required');
  if (!Array.isArray(plan.tail_and_segment_guardrails) || plan.tail_and_segment_guardrails.length === 0
    || !plan.tail_and_segment_guardrails.every(validGuardrail)) errors.push('at least one executable tail/segment guardrail is required');
  if (!plan.multiplicity?.hypothesis_family_definition || !['HOLM', 'PREREGISTERED_SINGLE'].includes(plan.multiplicity?.confirmatory_method)) {
    errors.push('multiplicity family and confirmatory method are required');
  }
  if (!(plan.multiplicity?.family_alpha > 0 && plan.multiplicity.family_alpha < 1)) errors.push('family_alpha must be in (0,1)');
  if (!plan.selective_policy?.coverage_denominator || !plan.selective_policy?.primary_selective_metric) {
    errors.push('risk-coverage policy and denominator are required');
  }
  if (!Number.isFinite(plan.selective_policy?.target) || !['RISK_AT_FIXED_COVERAGE', 'COVERAGE_AT_FIXED_RISK'].includes(plan.selective_policy?.primary_selective_metric)) {
    errors.push('selective-policy metric and numeric target are required');
  }
  if (plan.selective_policy?.primary_selective_metric === 'RISK_AT_FIXED_COVERAGE'
    && !(plan.selective_policy.target > 0 && plan.selective_policy.target <= 1)) errors.push('fixed coverage target must be in (0,1]');
  if (plan.selective_policy?.primary_selective_metric === 'COVERAGE_AT_FIXED_RISK'
    && !(plan.selective_policy.target >= 0)) errors.push('fixed risk target must be nonnegative');
  const monitoringMetrics = new Set([
    'BRIER_DELTA', 'LOG_LOSS_DELTA', 'CALIBRATION_ECE', 'SOURCE_MISSING_RATE', 'DRIFT_STATISTIC',
    'DATA_INTEGRITY_FAILURE_COUNT', 'REMEDIATION_EVIDENCE_COMPLETE',
  ]);
  const executableRule = (rule) => rule && typeof rule === 'object' && typeof rule.rule_id === 'string'
    && rule.rule_id.length > 0 && monitoringMetrics.has(rule.metric) && ['LTE', 'GTE', 'EQ'].includes(rule.operator)
    && Number.isFinite(rule.threshold) && Number.isInteger(rule.consecutive_windows) && rule.consecutive_windows >= 1;
  const windowValid = plan.monitoring?.performance_window && Number.isInteger(plan.monitoring.performance_window.size)
    && plan.monitoring.performance_window.size > 0 && ['SETTLED_EVENTS', 'DAYS'].includes(plan.monitoring.performance_window.unit);
  if (!Array.isArray(plan.monitoring?.integrity_failures) || plan.monitoring.integrity_failures.length === 0
    || !plan.monitoring.integrity_failures.every((item) => typeof item === 'string' && item.length > 0)
    || !windowValid || !Number.isInteger(plan.monitoring?.minimum_settled_n)
    || plan.monitoring.minimum_settled_n < 1 || !executableRule(plan.monitoring?.alert_rule)
    || !executableRule(plan.monitoring?.suspension_rule) || !executableRule(plan.monitoring?.restart_rule)) {
    errors.push('numeric monitoring and suspension policy is required');
  }
  return errors;
}

export function riskCoverageCurve(rows) {
  if (!Array.isArray(rows) || rows.length === 0) throw new Error('risk-coverage rows are required');
  const requestIds = new Set();
  for (const row of rows) {
    if (!row.request_id || requestIds.has(row.request_id)) throw new Error('request_id values must be unique and nonempty');
    requestIds.add(row.request_id);
    if (!Number.isFinite(row.loss) || row.loss < 0 || !Number.isFinite(row.selector_score)) {
      throw new Error('loss must be finite/nonnegative and selector_score must be finite');
    }
  }
  const sorted = [...rows].sort((left, right) => {
    const delta = right.selector_score - left.selector_score;
    return delta || compareCanonicalStrings(String(left.request_id), String(right.request_id));
  });
  const curve = [];
  let cumulativeLoss = 0;
  let issuedCount = 0;
  for (let index = 0; index < sorted.length;) {
    const threshold = sorted[index].selector_score;
    let blockEnd = index;
    while (blockEnd < sorted.length && sorted[blockEnd].selector_score === threshold) {
      cumulativeLoss += sorted[blockEnd].loss;
      blockEnd += 1;
    }
    issuedCount = blockEnd;
    curve.push({
      threshold,
      tie_block_size: blockEnd - index,
      issued_count: issuedCount,
      eligible_count: sorted.length,
      coverage: issuedCount / sorted.length,
      selective_risk: cumulativeLoss / issuedCount,
    });
    index = blockEnd;
  }
  let previousCoverage = 0;
  let aurc = 0;
  for (const point of curve) {
    aurc += (point.coverage - previousCoverage) * point.selective_risk;
    previousCoverage = point.coverage;
  }
  return { curve, aurc, aurc_convention: 'right-continuous step area over implementable complete tie blocks', eligible_count: sorted.length };
}

function xorshift32(seed) {
  let state = seed >>> 0 || 0x9e3779b9;
  return () => {
    state ^= state << 13;
    state ^= state >>> 17;
    state ^= state << 5;
    return (state >>> 0) / 0x1_0000_0000;
  };
}

function quantile(sorted, probability) {
  const position = (sorted.length - 1) * probability;
  const lower = Math.floor(position);
  const upper = Math.ceil(position);
  if (lower === upper) return sorted[lower];
  return sorted[lower] + (sorted[upper] - sorted[lower]) * (position - lower);
}

export function pairedClusterBootstrap(rows, { seed = 20260716, resamples = 5000, confidenceLevel = 0.95, pointWeighting = 'ROW_EQUAL' } = {}) {
  if (!Array.isArray(rows) || rows.length === 0) throw new Error('paired score rows are required');
  if (!Number.isInteger(resamples) || resamples < 100) throw new Error('resamples must be an integer >=100');
  if (!Number.isInteger(seed) || seed < 0 || seed > 0xFFFFFFFF) throw new Error('seed must be an unsigned 32-bit integer');
  if (!(confidenceLevel > 0 && confidenceLevel < 1)) throw new Error('confidenceLevel must be in (0,1)');
  const clusters = new Map();
  for (const row of rows) {
    if (!row.cluster_id || !Number.isFinite(row.model_loss) || !Number.isFinite(row.baseline_loss)) throw new Error('each row needs cluster_id and finite paired losses');
    if (!clusters.has(row.cluster_id)) clusters.set(row.cluster_id, []);
    clusters.get(row.cluster_id).push(row.baseline_loss - row.model_loss);
  }
  const clusterValues = [...clusters.entries()].sort(([left], [right]) => compareCanonicalStrings(String(left), String(right)))
    .map(([, values]) => ({ mean: values.reduce((sum, value) => sum + value, 0) / values.length, count: values.length }));
  if (clusterValues.length < 2) throw new Error('at least two independent clusters are required');
  if (!['ROW_EQUAL', 'CLUSTER_EQUAL'].includes(pointWeighting)) throw new Error('pointWeighting must be ROW_EQUAL or CLUSTER_EQUAL');
  const pointEstimate = pointWeighting === 'ROW_EQUAL'
    ? rows.reduce((sum, row) => sum + row.baseline_loss - row.model_loss, 0) / rows.length
    : clusterValues.reduce((sum, cluster) => sum + cluster.mean, 0) / clusterValues.length;
  const random = xorshift32(seed);
  const samples = [];
  for (let draw = 0; draw < resamples; draw += 1) {
    let weightedSum = 0;
    let weight = 0;
    for (let index = 0; index < clusterValues.length; index += 1) {
      const selected = clusterValues[Math.floor(random() * clusterValues.length)];
      const selectedWeight = pointWeighting === 'ROW_EQUAL' ? selected.count : 1;
      weightedSum += selected.mean * selectedWeight;
      weight += selectedWeight;
    }
    samples.push(weightedSum / weight);
  }
  samples.sort((left, right) => left - right);
  const alpha = 1 - confidenceLevel;
  const clusterSizes = clusterValues.map((cluster) => cluster.count);
  const total = clusterSizes.reduce((sum, value) => sum + value, 0);
  const effectiveN = total ** 2 / clusterSizes.reduce((sum, value) => sum + value ** 2, 0);
  return {
    estimand: pointWeighting === 'ROW_EQUAL'
      ? 'row-equal mean paired baseline_loss_minus_model_loss over production opportunities'
      : 'cluster-equal mean of event-cluster paired baseline_loss_minus_model_loss means',
    point_estimate: pointEstimate,
    interval_type: 'event-cluster percentile bootstrap',
    confidence_level: confidenceLevel,
    lower: quantile(samples, alpha / 2),
    upper: quantile(samples, 1 - alpha / 2),
    cluster_count: clusterValues.length,
    cluster_size_concentration_n: effectiveN,
    cluster_size_concentration_note: 'describes row-weight concentration only; it is not a dependence-adjusted effective sample size',
    point_weighting: pointWeighting,
    resampling_unit: 'EVENT_CLUSTER',
    prng: 'xorshift32_v1',
    resamples,
    seed,
  };
}

export function holmDecisions(pValues, alpha = 0.05) {
  if (!Array.isArray(pValues) || pValues.length === 0) throw new Error('at least one hypothesis is required');
  if (!(alpha > 0 && alpha < 1)) throw new Error('alpha must be in (0,1)');
  const ids = new Set();
  for (const item of pValues) {
    if (!item.hypothesis_id || ids.has(item.hypothesis_id)) throw new Error('hypothesis IDs must be unique and nonempty');
    ids.add(item.hypothesis_id);
    if (!(item.p_value >= 0 && item.p_value <= 1)) throw new Error('p-values must be in [0,1]');
  }
  const ordered = pValues.map((item) => ({ ...item })).sort((left, right) => left.p_value - right.p_value);
  let stillRejecting = true;
  ordered.forEach((item, index) => {
    const threshold = alpha / (ordered.length - index);
    item.holm_threshold = threshold;
    item.reject = stillRejecting && item.p_value <= threshold;
    if (!item.reject) stillRejecting = false;
  });
  const byId = new Map(ordered.map((item) => [item.hypothesis_id, item]));
  return pValues.map((item) => byId.get(item.hypothesis_id));
}

export function validateExperimentLedger(rows) {
  const errors = [];
  if (!Array.isArray(rows)) return ['experiment ledger must be an array'];
  const ids = new Set();
  const spentByFamilyAndManifest = new Set();
  const statuses = new Set(['PLANNED_UNTOUCHED', 'SPENT', 'INVALIDATED']);
  for (const row of rows) {
    if (!row.experiment_id) errors.push('blank experiment_id');
    else if (ids.has(row.experiment_id)) errors.push(`duplicate experiment_id ${row.experiment_id}`);
    ids.add(row.experiment_id);
    if (!row.hypothesis_family_id) errors.push(`${row.experiment_id}: hypothesis_family_id required`);
    if (!row.model_id || !row.model_version || !isSha256(row.model_config_hash)) errors.push(`${row.experiment_id}: exact model/version/config hash required`);
    if (!isSha256(row.event_manifest_hash) || !isSha256(row.preregistered_rule_hash)) errors.push(`${row.experiment_id}: manifest and preregistration hashes required`);
    if (!statuses.has(row.test_status)) errors.push(`${row.experiment_id}: invalid test_status`);
    if (!['UNTOUCHED_TEST', 'PROSPECTIVE_SHADOW'].includes(row.test_role)) errors.push(`${row.experiment_id}: invalid test_role`);
    try {
      const registered = parseUtc(row.preregistered_at_utc, `${row.experiment_id}.preregistered_at_utc`);
      if (row.first_viewed_at_utc && registered >= parseUtc(row.first_viewed_at_utc, `${row.experiment_id}.first_viewed_at_utc`)) {
        errors.push(`${row.experiment_id}: preregistration must precede first view`);
      }
    } catch (error) { errors.push(error.message); }
    if (row.first_viewed_at_utc && row.test_status !== 'SPENT') errors.push(`${row.experiment_id}: viewed test must be SPENT`);
    if (row.test_status === 'SPENT') {
      if (!row.first_viewed_at_utc || !row.viewed_by || !isSha256(row.results_artifact_hash)) {
        errors.push(`${row.experiment_id}: SPENT requires first view, viewer and results artifact hash`);
      }
      spentByFamilyAndManifest.add(`${row.hypothesis_family_id}:${row.event_manifest_hash}`);
    }
    if (row.test_status === 'PLANNED_UNTOUCHED' && (row.first_viewed_at_utc || row.viewed_by || row.results_artifact_hash)) {
      errors.push(`${row.experiment_id}: PLANNED_UNTOUCHED cannot contain viewed/results fields`);
    }
  }
  for (const row of rows) {
    if (row.test_status === 'PLANNED_UNTOUCHED'
      && spentByFamilyAndManifest.has(`${row.hypothesis_family_id}:${row.event_manifest_hash}`)) {
      errors.push(`${row.experiment_id}: attempts to reuse a spent manifest in the same hypothesis family`);
    }
  }
  return errors;
}
