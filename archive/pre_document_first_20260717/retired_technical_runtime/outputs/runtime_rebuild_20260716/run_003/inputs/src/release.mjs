import { isSha256, parseUtc } from './canonical.mjs';

export const RELEASE_MODES = new Set(['SUSPENDED', 'VALIDATION_CANDIDATE', 'OPERATIONAL']);

export function validateReleaseManifest(release, coverageRows) {
  const errors = [];
  if (release?.schema_version !== 'SPORTS_RELEASE_MANIFEST_V1') errors.push('release schema_version is invalid');
  if (!release?.release_id) errors.push('release_id is required');
  if (!RELEASE_MODES.has(release?.release_mode)) errors.push(`unsupported release_mode ${release?.release_mode}`);
  try { parseUtc(release?.effective_at_utc, 'release.effective_at_utc'); } catch (error) { errors.push(error.message); }

  const activeCount = coverageRows.filter((row) => row.status === 'ACTIVE').length;
  if (!Number.isInteger(release?.expected_active_coverage_count) || release.expected_active_coverage_count < 0) {
    errors.push('expected_active_coverage_count must be a nonnegative integer');
  } else if (release.expected_active_coverage_count !== activeCount) {
    errors.push(`release expects ${release.expected_active_coverage_count} ACTIVE coverage row(s), registry has ${activeCount}`);
  }
  if (!Number.isInteger(release?.expected_acceptance_requirement_count) || release.expected_acceptance_requirement_count < 1) {
    errors.push('expected_acceptance_requirement_count must be a positive integer');
  }

  if (release?.release_mode === 'SUSPENDED' || release?.release_mode === 'VALIDATION_CANDIDATE') {
    if (release.activation_authorized !== false) errors.push(`${release.release_mode} cannot authorize activation`);
    if (activeCount !== 0) errors.push(`${release.release_mode} must contain zero ACTIVE coverage rows`);
    if (release.operational_status !== 'SUSPENDED_NO_ACTIVE_MODELS') errors.push(`${release.release_mode} has inconsistent operational_status`);
  }

  if (release?.release_mode === 'OPERATIONAL') {
    if (release.activation_authorized !== true) errors.push('OPERATIONAL requires activation_authorized=true');
    if (activeCount < 1) errors.push('OPERATIONAL requires at least one exact ACTIVE coverage row');
    if (release.operational_status !== 'OPERATIONAL_EXACT_SCOPES_ONLY') errors.push('OPERATIONAL has inconsistent operational_status');
    if (!release.review_ticket_id || !release.reviewed_by) errors.push('OPERATIONAL requires a review ticket and named reviewer');
    try { parseUtc(release.reviewed_at_utc, 'release.reviewed_at_utc'); } catch (error) { errors.push(error.message); }
    if (!isSha256(release.release_bundle_hash)) errors.push('OPERATIONAL requires a release_bundle_hash');
  }

  if (release?.current_truth?.active_models !== activeCount) errors.push('current_truth.active_models does not match coverage registry');
  if (release?.release_mode !== 'OPERATIONAL' && release?.current_truth?.authorized_numeric_forecasts !== false) {
    errors.push('non-operational release cannot authorize numeric forecasts');
  }
  return { valid: errors.length === 0, active_count: activeCount, errors };
}
