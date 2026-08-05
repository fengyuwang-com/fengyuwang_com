# migrate-fengproj.ps1
# Migrate working projects from C:\Users\a8881\FenglinProj to C:\FengProj,
# leaving a directory junction at each old path so legacy references still work.
# Rule: never touch a folder that is in use. Locked folders are skipped & logged.
# Usage: powershell -ExecutionPolicy Bypass -File scripts/migrate-fengproj.ps1
#
# NOTE: this file is ASCII-only (English comments) to avoid PowerShell
# ANSI/UTF-8 BOM parsing issues on this system.

$ErrorActionPreference = 'Continue'

$src = 'C:\Users\a8881\FenglinProj'
$dst = 'C:\FengProj'
$log = Join-Path $PSScriptRoot 'migrate.log'

# Never migrate: in-use / sandbox / backup / tool dirs (per user decision)
$exclude = @(
  'fengyuwang_com',                     # this session's sandbox (server running)
  'DiannaLee55-yb-export-tool-cc8b17f', # YB Export scan in progress
  'Lecoo Backup',                       # backup area
  'FengProj.7z',                        # archive inside backup (not a dir here)
  '.claude',                            # moved separately to ~/.claude
  '.zcode',                             # ZCode tool - leave
  '.playwright-cli',                    # logs - leave
  '.agently-cli-backup'                 # tool backup - leave
)

$total = 0; $moved = 0; $skipped = 0

"===== migrate start $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') =====" | Out-File -FilePath $log -Encoding utf8 -Append

$items = Get-ChildItem -LiteralPath $src -Directory -Force
foreach ($it in $items) {
  $name = $it.Name
  if ($exclude -contains $name) {
    "[SKIP-EXCLUDE] $name" | Out-File -FilePath $log -Encoding utf8 -Append
    $skipped++
    continue
  }

  $s = $it.FullName
  $d = Join-Path $dst $name
  $total++

  if (Test-Path -LiteralPath $d) {
    if ((Get-ChildItem -LiteralPath $s -Force | Measure-Object).Count -eq 0) {
      # destination exists and source is empty => already migrated; ensure junction
      if (!(Test-Path -LiteralPath $s)) { New-Item -ItemType Junction -Path $s -Target $d -Force | Out-Null }
      "[DONE-RESUME] $name (dst exists, src empty, junction ensured)" | Out-File -FilePath $log -Encoding utf8 -Append
      $moved++
    } else {
      "[WARN-EXISTS] $name (dst exists but src NOT empty - skip, manual action needed)" | Out-File -FilePath $log -Encoding utf8 -Append
      $skipped++
    }
    continue
  }

  Write-Host "Migrating: $name"
  robocopy $s $d /MOVE /E /COPY:DAT /XJ 2>&1 | Out-Null
  $rc = $LASTEXITCODE

  if ($rc -lt 8) {
    # robocopy 0-7 = success; >=8 = failure (e.g. locked)
    if (Test-Path -LiteralPath $d) {
      # replace leftover source shell with a junction
      Remove-Item -LiteralPath $s -Force -Recurse -ErrorAction SilentlyContinue
      New-Item -ItemType Junction -Path $s -Target $d -Force -ErrorAction SilentlyContinue | Out-Null
      $linkType = (Get-Item $s -Force -ErrorAction SilentlyContinue).LinkType
      if ($linkType -eq 'Junction') {
        "[MOVED] $name (rc=$rc, junction ok)" | Out-File -FilePath $log -Encoding utf8 -Append
        $moved++
      } else {
        "[MOVED-WARN] $name (rc=$rc, data in dst, junction NOT built linkType='$linkType')" | Out-File -FilePath $log -Encoding utf8 -Append
        $moved++
      }
    } else {
      "[SKIP-LOCKED] $name (robocopy rc=$rc, dst missing)" | Out-File -FilePath $log -Encoding utf8 -Append
      $skipped++
    }
  } else {
    "[SKIP-LOCKED] $name (robocopy rc=$rc)" | Out-File -FilePath $log -Encoding utf8 -Append
    $skipped++
  }
}

"===== end $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') | total=$total moved=$moved skipped=$skipped =====" | Out-File -FilePath $log -Encoding utf8 -Append
Write-Host "Done. total=$total moved=$moved skipped=$skipped (see $log)"
