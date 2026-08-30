[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$root = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
$results = [System.Collections.Generic.List[object]]::new()

function Add-Result {
    param(
        [Parameter(Mandatory = $true)][string]$Id,
        [Parameter(Mandatory = $true)][bool]$Passed,
        [Parameter(Mandatory = $true)][string]$Detail
    )

    $status = 'FAIL'
    if ($Passed) { $status = 'PASS' }
    $script:results.Add([pscustomobject]@{ Test = $Id; Status = $status; Detail = $Detail })
}

function Read-Text {
    param([Parameter(Mandatory = $true)][string]$RelativePath)
    return Get-Content -LiteralPath (Join-Path $script:root $RelativePath) -Raw
}

function Test-ContainsAll {
    param(
        [Parameter(Mandatory = $true)][string]$Text,
        [Parameter(Mandatory = $true)][string[]]$Tokens
    )

    foreach ($token in $Tokens) {
        if ($Text.IndexOf($token, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
            return $false
        }
    }
    return $true
}

function Get-NormalizedBrier {
    param(
        [Parameter(Mandatory = $true)][double[]]$Probabilities,
        [Parameter(Mandatory = $true)][int]$ObservedIndex
    )

    $sum = 0.0
    for ($i = 0; $i -lt $Probabilities.Count; $i++) {
        $observed = 0.0
        if ($i -eq $ObservedIndex) { $observed = 1.0 }
        $difference = $Probabilities[$i] - $observed
        $sum += $difference * $difference
    }
    # Half the multiclass sum preserves the familiar binary-event Brier scale
    # while remaining comparable when a push/void branch is explicit.
    return $sum / 2.0
}

function Test-Near {
    param(
        [Parameter(Mandatory = $true)][double]$Actual,
        [Parameter(Mandatory = $true)][double]$Expected,
        [double]$Tolerance = 1e-12
    )
    return [math]::Abs($Actual - $Expected) -le $Tolerance
}

$requiredFiles = @(
    'SPORTS_RESEARCH_AUTHORITY_MANIFEST.md',
    'SPORTS_RELEASE_MANIFEST_v1.json',
    'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv',
    'combined_sports_doc_v3.md',
    'SPORTS_DATA_DICTIONARY_v3.md',
    'SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md',
    'SPORTS_SOURCE_REGISTRY_v3.md',
    'SPORTS_DEVELOPMENT_MODEL_CATALOG_v1.md',
    'SPORTS_SCORING_SPECIFICATION_v3.md',
    'SPORTS_ACCEPTANCE_TESTS_v3.md',
    'SPORTS_MODEL_REGISTRY_v1.csv',
    'SPORTS_ANALYSIS_MODEL_REGISTRY_v1.json',
    'SPORTS_ACTIVE_ANALYSIS_MODELS_v1.md',
    'SPORTS_REGISTERED_SOURCES_v1.csv',
    'schema\controlled_vocabularies_v1.json',
    'schema\contract_registry_v1.csv',
    'schema\source_maps_v1.csv',
    'schema\test_evaluations_v1.csv',
    'schema\decision_packet.schema.json',
    'schema\analysis_request.schema.json',
    'schema\analysis_output.schema.json',
    'schema\analysis_acceptance_traceability_v1.csv',
    'src\analysis.mjs',
    'scripts\validate_v3_system.ps1'
)

$missingFiles = @($requiredFiles | Where-Object { -not (Test-Path -LiteralPath (Join-Path $root $_) -PathType Leaf) })
Add-Result -Id 'SPEC-FILES-001' -Passed ($missingFiles.Count -eq 0) -Detail $(
    if ($missingFiles.Count -eq 0) { 'All canonical controls plus numeric-development and analysis-only model artifacts exist.' }
    else { 'Missing: ' + ($missingFiles -join ', ') }
)

if ($missingFiles.Count -gt 0) {
    $results | Format-Table -AutoSize -Wrap
    Write-Error 'Specification is incomplete. Operational status remains SUSPENDED - NO ACTIVE MODELS.'
    exit 1
}

$release = Get-Content -LiteralPath (Join-Path $root 'SPORTS_RELEASE_MANIFEST_v1.json') -Raw | ConvertFrom-Json
$releaseMode = [string]$release.release_mode
$expectedOperationalStatus = [string]$release.operational_status
$releaseModes = @('SUSPENDED','VALIDATION_CANDIDATE','OPERATIONAL')
Add-Result -Id 'SPEC-RELEASE-001' -Passed ($releaseMode -in $releaseModes) -Detail "release_id=$($release.release_id); mode=$releaseMode; operational_status=$expectedOperationalStatus"

$markdownSpecs = @(
    'SPORTS_RESEARCH_AUTHORITY_MANIFEST.md',
    'combined_sports_doc_v3.md',
    'SPORTS_DATA_DICTIONARY_v3.md',
    'SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md',
    'SPORTS_SOURCE_REGISTRY_v3.md',
    'SPORTS_SCORING_SPECIFICATION_v3.md',
    'SPORTS_ACCEPTANCE_TESTS_v3.md'
)

$statusFailures = [System.Collections.Generic.List[string]]::new()
foreach ($file in $markdownSpecs) {
    $text = Read-Text -RelativePath $file
    if ($text -notmatch '(?im)^Status:\s*CANONICAL SPECIFICATION\s*$') {
        $statusFailures.Add("$file lacks canonical-specification status")
    }
    if ($releaseMode -ne 'OPERATIONAL' -and $text -notmatch '(?im)^Operational status:\s*\*\*SUSPENDED[^\r\n]*NO ACTIVE MODELS\*\*\s*$') {
        $statusFailures.Add("$file lacks suspended operational status required by release manifest")
    }
    if ($releaseMode -eq 'OPERATIONAL' -and $text.IndexOf($expectedOperationalStatus, [System.StringComparison]::OrdinalIgnoreCase) -lt 0) {
        $statusFailures.Add("$file does not match operational release status $expectedOperationalStatus")
    }
}
Add-Result -Id 'SPEC-STATUS-001' -Passed ($statusFailures.Count -eq 0) -Detail $(
    if ($statusFailures.Count -eq 0) { 'All canonical Markdown specifications explicitly remain suspended.' }
    else { $statusFailures -join '; ' }
)

$manifest = Read-Text -RelativePath 'SPORTS_RESEARCH_AUTHORITY_MANIFEST.md'
$manifestTokens = @(
    'single source of authority',
    'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv',
    'POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md',
    'PREDICTION_RESULTS_LOG_v3.md',
    'non-operative',
    'fail closed'
)
Add-Result -Id 'SPEC-AUTH-001' -Passed (Test-ContainsAll -Text $manifest -Tokens $manifestTokens) -Detail 'Authority precedence and legacy non-operation are explicit.'

$coveragePath = Join-Path $root 'SPORTS_MODEL_COVERAGE_REGISTRY_v3.csv'
$coverage = @(Import-Csv -LiteralPath $coveragePath)
$requiredColumns = @(
    'coverage_id','sport_family','competition_scope','market_scope','forecast_state','analysis_mode','status',
    'model_id','model_version','source_map_id','test_report_id','shadow_report_id','approved_by','approval_utc','expires_utc','reason'
)
$actualColumns = @()
if ($coverage.Count -gt 0) { $actualColumns = @($coverage[0].PSObject.Properties.Name) }
$missingColumns = @($requiredColumns | Where-Object { $_ -notin $actualColumns })
$duplicateIds = @($coverage | Group-Object coverage_id | Where-Object { $_.Count -ne 1 })
$invalidStatuses = @($coverage | Where-Object { $_.status -notin @('UNSUPPORTED','DEVELOPMENT','SHADOW','ACTIVE','SUSPENDED','RETIRED') })
$activeRows = @($coverage | Where-Object { $_.status -eq 'ACTIVE' })
$expectedCoverage = @(
    'SOCCER_GOALS_ALL','SOCCER_COUNTS_ALL','BASEBALL_ALL','BASKETBALL_ALL','CRICKET_ALL',
    'AUSTRALIAN_FOOTBALL_ALL','ICE_HOCKEY_ALL','AMERICAN_FOOTBALL_ALL','RUGBY_LEAGUE_ALL',
    'RUGBY_UNION_ALL','TENNIS_ALL','VOLLEYBALL_ALL','GOLF_ALL','MOTORSPORT_ALL','COMBAT_ALL','OTHER_SPORT_ALL'
)
$missingCoverage = @($expectedCoverage | Where-Object { $_ -notin $coverage.coverage_id })
$releaseCoverageValid = $false
if ($releaseMode -in @('SUSPENDED','VALIDATION_CANDIDATE')) {
    $releaseCoverageValid = $activeRows.Count -eq 0 -and [int]$release.expected_active_coverage_count -eq 0 -and $release.activation_authorized -eq $false
} elseif ($releaseMode -eq 'OPERATIONAL') {
    $releaseCoverageValid = $activeRows.Count -gt 0 -and $activeRows.Count -eq [int]$release.expected_active_coverage_count -and $release.activation_authorized -eq $true
}
$activeEvidenceErrors = [System.Collections.Generic.List[string]]::new()
foreach ($row in $activeRows) {
    foreach ($field in @('model_id','model_version','source_map_id','test_report_id','shadow_report_id','approved_by','approval_utc','expires_utc')) {
        if ([string]::IsNullOrWhiteSpace($row.$field)) { $activeEvidenceErrors.Add("$($row.coverage_id): ACTIVE missing $field") }
    }
    foreach ($field in @('competition_scope','market_scope','forecast_state','analysis_mode')) {
        if ($row.$field -match '(^|\|)ALL($|\|)' -or $row.$field -match '\|') { $activeEvidenceErrors.Add("$($row.coverage_id): ACTIVE $field is not exact") }
    }
}
$coveragePassed = (
    $coverage.Count -ge $expectedCoverage.Count -and
    $missingColumns.Count -eq 0 -and
    $duplicateIds.Count -eq 0 -and
    $invalidStatuses.Count -eq 0 -and
    $releaseCoverageValid -and
    $activeEvidenceErrors.Count -eq 0 -and
    $missingCoverage.Count -eq 0
)
$coverageDetail = "rows=$($coverage.Count); mode=$releaseMode; active=$($activeRows.Count); invalid_status=$($invalidStatuses.Count); active_evidence_errors=$($activeEvidenceErrors.Count); duplicate_id=$($duplicateIds.Count); missing_scope=$($missingCoverage.Count); missing_column=$($missingColumns.Count)"
Add-Result -Id 'SPEC-COVERAGE-001' -Passed $coveragePassed -Detail $coverageDetail

$developmentCatalog = Read-Text -RelativePath 'SPORTS_DEVELOPMENT_MODEL_CATALOG_v1.md'
$developmentRows = @($coverage | Where-Object { $_.status -eq 'DEVELOPMENT' })
$unsupportedRows = @($coverage | Where-Object { $_.status -eq 'UNSUPPORTED' })
$expectedDevelopmentModels = @(
    'DEV_SOCCER_SCORE_V0','DEV_SOCCER_COUNTS_V0','DEV_BASEBALL_PA_V0','DEV_BASKETBALL_POSSESSION_V0',
    'DEV_CRICKET_BALL_STATE_V0','DEV_AFL_SCORE_V0','DEV_ICE_HOCKEY_STATE_V0','DEV_AMERICAN_FOOTBALL_DRIVE_V0',
    'DEV_RUGBY_LEAGUE_SCORE_V0','DEV_RUGBY_UNION_SCORE_V0','DEV_TENNIS_POINT_V0','DEV_VOLLEYBALL_RALLY_V0',
    'DEV_GOLF_HOLE_V0','DEV_MOTORSPORT_RACE_V0','DEV_COMBAT_HAZARD_V0'
)
$developmentErrors = [System.Collections.Generic.List[string]]::new()
$activationEvidenceFields = @('source_map_id','test_report_id','shadow_report_id','approved_by','approval_utc','expires_utc')
foreach ($row in $developmentRows) {
    if ([string]::IsNullOrWhiteSpace($row.model_id) -or [string]::IsNullOrWhiteSpace($row.model_version)) {
        $developmentErrors.Add("$($row.coverage_id): missing model ID/version")
    }
    foreach ($field in $activationEvidenceFields) {
        if (-not [string]::IsNullOrWhiteSpace($row.$field)) {
            $developmentErrors.Add("$($row.coverage_id): DEVELOPMENT row has $field")
        }
    }
    if ($row.reason -notmatch '(?i)not fitted') {
        $developmentErrors.Add("$($row.coverage_id): reason does not explicitly say not fitted")
    }
    if ($developmentCatalog.IndexOf($row.model_id, [System.StringComparison]::Ordinal) -lt 0) {
        $developmentErrors.Add("$($row.coverage_id): model ID absent from development catalog")
    }
}
foreach ($row in $unsupportedRows) {
    if (-not [string]::IsNullOrWhiteSpace($row.model_id) -or -not [string]::IsNullOrWhiteSpace($row.model_version)) {
        $developmentErrors.Add("$($row.coverage_id): UNSUPPORTED row must not name a model")
    }
}
$missingDevelopmentModels = @($expectedDevelopmentModels | Where-Object { $_ -notin $developmentRows.model_id })
$unexpectedDevelopmentModels = @($developmentRows.model_id | Where-Object { $_ -notin $expectedDevelopmentModels })
$developmentPassed = (
    $developmentRows.Count -eq $expectedDevelopmentModels.Count -and
    $unsupportedRows.Count -eq 1 -and
    $developmentErrors.Count -eq 0 -and
    $missingDevelopmentModels.Count -eq 0 -and
    $unexpectedDevelopmentModels.Count -eq 0
)
$developmentDetail = "development=$($developmentRows.Count); unsupported=$($unsupportedRows.Count); errors=$($developmentErrors.Count); missing_model=$($missingDevelopmentModels.Count); unexpected_model=$($unexpectedDevelopmentModels.Count)"
Add-Result -Id 'SPEC-DEVELOPMENT-MODELS-001' -Passed $developmentPassed -Detail $developmentDetail

$analysisRegistry = Get-Content -LiteralPath (Join-Path $root 'SPORTS_ANALYSIS_MODEL_REGISTRY_v1.json') -Raw | ConvertFrom-Json
$analysisModels = @($analysisRegistry.models)
$analysisTraceability = @(Import-Csv -LiteralPath (Join-Path $root 'schema\analysis_acceptance_traceability_v1.csv'))
$expectedAnalysisSports = @('Baseball','Cricket','Soccer','Australian football','Rugby league')
$analysisErrors = [System.Collections.Generic.List[string]]::new()
if ($analysisRegistry.schema_version -ne 'SPORTS_ANALYSIS_MODEL_REGISTRY_V1') { $analysisErrors.Add('registry schema version mismatch') }
if ($analysisRegistry.tier_status -ne 'ACTIVE_ANALYSIS_ONLY') { $analysisErrors.Add('registry tier is not ACTIVE_ANALYSIS_ONLY') }
if ($analysisRegistry.numeric_forecast_authorized -ne $false) { $analysisErrors.Add('numeric forecasts are not explicitly prohibited') }
if ($analysisModels.Count -ne 5) { $analysisErrors.Add("expected 5 analysis models; found $($analysisModels.Count)") }
if ($analysisTraceability.Count -ne [int]$analysisRegistry.expected_acceptance_requirement_count) { $analysisErrors.Add('analysis acceptance requirement count mismatch') }
if (@($analysisTraceability | Group-Object requirement_id | Where-Object { $_.Count -ne 1 }).Count -gt 0) { $analysisErrors.Add('analysis acceptance requirement IDs are not unique') }
if (@($analysisTraceability | Where-Object { $_.status -ne 'COVERED' -or [string]::IsNullOrWhiteSpace($_.test_file) -or [string]::IsNullOrWhiteSpace($_.test_name) }).Count -gt 0) { $analysisErrors.Add('analysis acceptance matrix is not fully covered') }
if (@($analysisModels | Group-Object model_id | Where-Object { $_.Count -ne 1 }).Count -gt 0) { $analysisErrors.Add('analysis model IDs are not unique') }
foreach ($sport in $expectedAnalysisSports) {
    if (@($analysisModels | Where-Object { $_.sport_family -eq $sport -and $_.status -eq 'ACTIVE_ANALYSIS_ONLY' }).Count -ne 1) {
        $analysisErrors.Add("$sport does not have exactly one ACTIVE_ANALYSIS_ONLY model")
    }
}
$analysisCodeHash = (Get-FileHash -LiteralPath (Join-Path $root 'src\analysis.mjs') -Algorithm SHA256).Hash.ToLowerInvariant()
$analysisRequestHash = (Get-FileHash -LiteralPath (Join-Path $root 'schema\analysis_request.schema.json') -Algorithm SHA256).Hash.ToLowerInvariant()
$analysisOutputHash = (Get-FileHash -LiteralPath (Join-Path $root 'schema\analysis_output.schema.json') -Algorithm SHA256).Hash.ToLowerInvariant()
foreach ($model in $analysisModels) {
    if ($model.forecast_state -ne 'LIVE' -or $model.market_family -ne 'winner') { $analysisErrors.Add("$($model.model_id): non-LIVE/winner scope") }
    if ($model.code_hash -ne $analysisCodeHash) { $analysisErrors.Add("$($model.model_id): code hash mismatch") }
    if ($model.request_schema_hash -ne $analysisRequestHash -or $model.output_schema_hash -ne $analysisOutputHash) { $analysisErrors.Add("$($model.model_id): schema hash mismatch") }
    if (@($model.approved_source_ids).Count -lt 1 -or [int]$model.max_source_age_seconds -le 0) { $analysisErrors.Add("$($model.model_id): source policy incomplete") }
}
if ([int]$release.current_truth.active_analysis_only_models -ne 5 -or $release.current_truth.authorized_qualitative_live_analysis -ne $true) {
    $analysisErrors.Add('release current_truth does not authorize exactly five qualitative analysis models')
}
if ([int]$release.analysis_only_tier.expected_acceptance_requirement_count -ne $analysisTraceability.Count) { $analysisErrors.Add('release analysis acceptance count mismatch') }
if ($release.analysis_only_tier.numeric_forecast_authorized -ne $false) { $analysisErrors.Add('release analysis tier does not prohibit numeric forecasts') }
Add-Result -Id 'SPEC-ANALYSIS-001' -Passed ($analysisErrors.Count -eq 0) -Detail $(
    if ($analysisErrors.Count -eq 0) { 'Five analysis-only LIVE models are hash-bound and numeric forecast claims remain prohibited.' }
    else { $analysisErrors -join '; ' }
)

$dictionary = Read-Text -RelativePath 'SPORTS_DATA_DICTIONARY_v3.md'
$schemaTokens = @(
    'request record','decision snapshot','prediction record','candidate universe','candidate record','settlement-state record',
    'source observation','feature snapshot','model version record','test evaluation record','calibration evidence',
    'uncertainty component','simulation run','market price snapshot','execution record','settlement version','evaluation run',
    'snapshot_id','prediction_id','forecast_series_id','parent_snapshot_id','raw_request_text','live-state record'
)
Add-Result -Id 'SPEC-SCHEMA-001' -Passed (Test-ContainsAll -Text $dictionary -Tokens $schemaTokens) -Detail 'All required normalized entities and immutable identifiers are specified.'

$manual = Read-Text -RelativePath 'combined_sports_doc_v3.md'
$modeTokens = @(
    'analysis_mode = RESEARCH_ONLY | PRICE_ENABLED',
    'forecast_state = PREGAME_PROJECTED | PREGAME_CONFIRMED | LIVE',
    'MODEL_UNAVAILABLE',
    'null model/probability/edge/EV fields'
)
$modePassed = (Test-ContainsAll -Text $manual -Tokens $modeTokens) -and (Test-ContainsAll -Text $dictionary -Tokens @('Conditional nullability','RESEARCH_ONLY','PRICE_ENABLED','PREGAME_PROJECTED','PREGAME_CONFIRMED','LIVE'))
Add-Result -Id 'SPEC-MODES-001' -Passed $modePassed -Detail 'Analysis mode, forecast state and fail-closed nullability are specified independently.'

$acceptance = Read-Text -RelativePath 'SPORTS_ACCEPTANCE_TESTS_v3.md'
$requiredGates = @(
    'GATE-AUTH-001','GATE-CONTRACT-001','GATE-MODE-001','GATE-CUTOFF-001','GATE-SOURCE-001',
    'GATE-UNIVERSE-001','GATE-MODEL-001','GATE-TEST-001','GATE-PROB-001','GATE-COHERENCE-001','GATE-UNCERTAINTY-001',
    'GATE-PRICE-001','GATE-EXECUTION-001','GATE-SETTLEMENT-001','GATE-LEGACY-001'
)
$missingManualGates = @($requiredGates | Where-Object { $manual.IndexOf($_, [System.StringComparison]::OrdinalIgnoreCase) -lt 0 })
$missingAcceptanceGates = @($requiredGates | Where-Object { $acceptance.IndexOf($_, [System.StringComparison]::OrdinalIgnoreCase) -lt 0 })
$missingDictionaryGates = @($requiredGates | Where-Object { $dictionary.IndexOf($_, [System.StringComparison]::OrdinalIgnoreCase) -lt 0 })
$gatePassed = $missingManualGates.Count -eq 0 -and $missingAcceptanceGates.Count -eq 0 -and $missingDictionaryGates.Count -eq 0
Add-Result -Id 'SPEC-GATES-001' -Passed $gatePassed -Detail "missing_manual=$($missingManualGates.Count); missing_dictionary=$($missingDictionaryGates.Count); missing_acceptance=$($missingAcceptanceGates.Count)"

$framework = Read-Text -RelativePath 'SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md'
$activationTokens = @(
    'Prospective shadow is not optional',
    'SPENT',
    'minimum practically relevant improvement',
    'effective N',
    'point estimate',
    'MODEL_UNAVAILABLE'
)
Add-Result -Id 'SPEC-ACTIVATION-001' -Passed (Test-ContainsAll -Text $framework -Tokens $activationTokens) -Detail 'Prospective shadow, spent-test, effect/precision and fail-closed activation rules are present.'

$canonicalTexts = @{}
foreach ($file in $markdownSpecs) { $canonicalTexts[$file] = Read-Text -RelativePath $file }
$brokenReferences = [System.Collections.Generic.List[string]]::new()
$referencePattern = '`([^`]+\.(?:md|csv|ps1))`'
foreach ($entry in $canonicalTexts.GetEnumerator()) {
    foreach ($match in [regex]::Matches($entry.Value, $referencePattern, [System.Text.RegularExpressions.RegexOptions]::IgnoreCase)) {
        $relativeReference = $match.Groups[1].Value -replace '/', '\'
        if ($relativeReference -match '[*?]') { continue }
        $referencePath = Join-Path $root $relativeReference
        if (-not (Test-Path -LiteralPath $referencePath -PathType Leaf)) {
            $brokenReferences.Add("$($entry.Key) -> $relativeReference")
        }
    }
}
Add-Result -Id 'SPEC-NO-BROKEN-REF-001' -Passed ($brokenReferences.Count -eq 0) -Detail $(
    if ($brokenReferences.Count -eq 0) { 'All backtick-delimited operative file references resolve.' }
    else { $brokenReferences -join '; ' }
)

$brierWin = Get-NormalizedBrier -Probabilities @(0.7,0.3) -ObservedIndex 0
$logWin = -[math]::Log(0.7)
$brierLoss = Get-NormalizedBrier -Probabilities @(0.7,0.3) -ObservedIndex 1
$logLoss = -[math]::Log(0.3)
$brierPush = Get-NormalizedBrier -Probabilities @(0.55,0.35,0.10) -ObservedIndex 2
$logPush = -[math]::Log(0.10)
$brierZero = Get-NormalizedBrier -Probabilities @(1.0,0.0) -ObservedIndex 1
$logZero = [double]::PositiveInfinity
$evNoPush = 0.55 * (2.0 - 1.0) - 0.45
$evWithPush = 0.45 * (2.0 - 1.0) - 0.45
$invalidPushShortcut = 0.45 * 2.0 - 1.0

$scorePassed = (
    (Test-Near -Actual $brierWin -Expected 0.09) -and
    (Test-Near -Actual $logWin -Expected 0.35667494393873245) -and
    (Test-Near -Actual $brierLoss -Expected 0.49) -and
    (Test-Near -Actual $logLoss -Expected 1.2039728043259361) -and
    (Test-Near -Actual $brierPush -Expected 0.6175) -and
    (Test-Near -Actual $logPush -Expected 2.302585092994046) -and
    (Test-Near -Actual $brierZero -Expected 1.0) -and
    [double]::IsPositiveInfinity($logZero) -and
    (Test-Near -Actual $evNoPush -Expected 0.10) -and
    (Test-Near -Actual $evWithPush -Expected 0.0) -and
    (Test-Near -Actual $invalidPushShortcut -Expected -0.10)
)
Add-Result -Id 'SPEC-SCORING-001' -Passed $scorePassed -Detail "binary_win_brier=$brierWin; three_branch_push_brier=$brierPush; ev_with_push=$evWithPush; invalid_shortcut=$invalidPushShortcut"

$results | Format-Table -AutoSize -Wrap
$failures = @($results | Where-Object { $_.Status -eq 'FAIL' })
if ($failures.Count -gt 0) {
    Write-Error "Static v3 validation failed ($($failures.Count) failure(s)). Operational status remains SUSPENDED - NO ACTIVE MODELS."
    exit 1
}

Write-Host ''
Write-Host 'STATIC SPECIFICATION VALIDATION PASSED.' -ForegroundColor Green
Write-Host "Release mode: $releaseMode; operational status: $expectedOperationalStatus" -ForegroundColor Yellow
Write-Host "Active quantitative model count: $($activeRows.Count). Active analysis-only model count: $($analysisModels.Count)." -ForegroundColor Yellow
exit 0
