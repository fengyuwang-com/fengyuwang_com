$hugo = "hugo"
$target = ".."

Write-Output "[1/2] Building..."
& $hugo --cleanDestinationDir
if ($LASTEXITCODE -ne 0) { exit 1 }

Write-Output "[2/2] Copying blog files..."
$langs = @("zh-cn", "zh-hk", "en")
foreach ($lang in $langs) {
    $src = "..\_site\$lang\blog"
    $dst = "..\$lang\blog"
    if (Test-Path $src) {
        Remove-Item "$dst" -Recurse -Force -ErrorAction SilentlyContinue
        Copy-Item "$src" "$dst" -Recurse -Force
        Write-Output "  $lang/blog deployed"
    }
}

# Clean up
Remove-Item "..\_site" -Recurse -Force -ErrorAction SilentlyContinue
Write-Output "Done."