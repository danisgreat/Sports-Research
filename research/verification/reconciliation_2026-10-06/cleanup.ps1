$ErrorActionPreference = 'Stop'
$taskRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '../../..')).Path
$taskPlan = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'csv_cleanup_plan.json') -Raw | ConvertFrom-Json
foreach ($taskItem in $taskPlan.files) {
    $taskSource = (Resolve-Path -LiteralPath (Join-Path $taskRoot $taskItem.source)).Path
    $taskDestination = (Resolve-Path -LiteralPath (Join-Path $taskRoot $taskItem.destination)).Path
    if (-not $taskSource.StartsWith($taskRoot + '\', [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Source outside workspace' }
    if (-not $taskDestination.StartsWith((Join-Path $taskRoot 'Previous Sports Results') + '\', [System.StringComparison]::OrdinalIgnoreCase)) { throw 'Destination outside archive' }
    if ((Get-FileHash -LiteralPath $taskSource -Algorithm SHA256).Hash.ToLower() -ne $taskItem.sha256) { throw "Changed source: $taskSource" }
    if ((Get-FileHash -LiteralPath $taskDestination -Algorithm SHA256).Hash.ToLower() -ne $taskItem.sha256) { throw "Changed destination: $taskDestination" }
}
Add-Type -AssemblyName Microsoft.VisualBasic
$taskRemoved = @()
foreach ($taskGroup in ($taskPlan.files | Group-Object {($_.source -split '\\')[0]})) {
    $taskFolder = (Resolve-Path -LiteralPath (Join-Path $taskRoot $taskGroup.Name)).Path
    if (-not $taskFolder.StartsWith($taskRoot + '\', [System.StringComparison]::OrdinalIgnoreCase) -or (Split-Path -Leaf $taskFolder) -notlike '*_CSVs') { throw 'Invalid export directory' }
    $taskFiles = @(Get-ChildItem -LiteralPath $taskFolder -File -Recurse -Force)
    $taskExpected = @($taskGroup.Group | ForEach-Object {(Join-Path $taskRoot $_.source)})
    if ($taskFiles.Count -eq $taskExpected.Count -and @($taskFiles | Where-Object {$_.FullName -notin $taskExpected}).Count -eq 0) {
        [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteDirectory($taskFolder, [Microsoft.VisualBasic.FileIO.UIOption]::OnlyErrorDialogs, [Microsoft.VisualBasic.FileIO.RecycleOption]::SendToRecycleBin)
        $taskRemoved += $taskFolder
    } else {
        foreach ($taskPath in $taskExpected) {
            [Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($taskPath, [Microsoft.VisualBasic.FileIO.UIOption]::OnlyErrorDialogs, [Microsoft.VisualBasic.FileIO.RecycleOption]::SendToRecycleBin)
            $taskRemoved += $taskPath
        }
    }
}
foreach ($taskItem in $taskPlan.files) {
    if (Test-Path -LiteralPath (Join-Path $taskRoot $taskItem.source)) { throw "Source still present: $($taskItem.source)" }
    if ((Get-FileHash -LiteralPath (Join-Path $taskRoot $taskItem.destination) -Algorithm SHA256).Hash.ToLower() -ne $taskItem.sha256) { throw 'Archive changed during removal' }
}
$taskReceipt = [ordered]@{ completed_utc = [DateTime]::UtcNow.ToString('o'); duplicate_csv_count = $taskPlan.count; preserved_data_rows = $taskPlan.data_rows; removal = 'Windows Recycle Bin'; recycled_targets = $taskRemoved; archive_hashes_rechecked = $true }
$taskReceipt | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'csv_cleanup_receipt.json') -Encoding UTF8
$taskReceipt | ConvertTo-Json -Depth 4
