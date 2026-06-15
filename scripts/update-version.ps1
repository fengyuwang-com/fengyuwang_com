# Update VERSION file with current date-time: yy.MM.dd.HH.mm
$version = Get-Date -Format "yy.MM.dd.HH.mm"
$version | Out-File -FilePath "$PSScriptRoot\..\VERSION" -Encoding UTF8 -NoNewline
Write-Output "Version updated to: $version"