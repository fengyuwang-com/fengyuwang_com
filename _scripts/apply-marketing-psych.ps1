$html = Get-Content "en\index.html" -Raw -Encoding UTF8
$changes = 0

# 1. About h2 + p — Authority Bias + Clarity
$old1 = '<h2>I bridge market strategy, investing, and code</h2> 						<p>Three disciplines, one integrated perspective — helping teams make sharper decisions where markets, capital, and technology intersect.</p>'
$new1 = '<h2>Market strategy, investing, and code — one integrated perspective</h2> 						<p>Three disciplines inform every project I take on. Whether it is a product launch, an investment thesis, or a software build, I bring the same cross-section lens — markets, capital, and technology — and use it to help teams reach sharper, more grounded decisions.</p>'
if ($html -match [regex]::Escape($old1)) {
    $html = $html -replace [regex]::Escape($old1), $new1
    $changes++
    Write-Host "Changed: about h2 + p"
} else {
    Write-Host "NOT FOUND: about h2"
}

# 2. LinkedIn header + description — Social Proof
$old2 = '<h3 style="font-size:1.3rem; font-weight:700; margin:8px 0 4px; color:#1d1d1f;">Professional Updates</h3> 				<p style="color:#6e6e73; font-size:.95rem; line-height:1.5; margin:0;">Thoughts on markets, technology, and the connections between them — posted regularly on LinkedIn.</p> 				<span style="display:inline-block; margin-top:12px; color:#0071e3; font-weight:600; font-size'
$new2 = '<h3 style="font-size:1.3rem; font-weight:700; margin:8px 0 4px; color:#1d1d1f;">Articles &amp; Updates</h3> 				<p style="color:#6e6e73; font-size:.95rem; line-height:1.5; margin:0;">Thoughts on markets, technology, and the connections between them — I publish regularly on LinkedIn.</p> 				<span style="display:inline-block; margin-top:12px; color:#0071e3; font-weight:600; font-size'
if ($html -match [regex]::Escape($old2)) {
    $html = $html -replace [regex]::Escape($old2), $new2
    $changes++
    Write-Host "Changed: LinkedIn header + desc"
} else {
    Write-Host "NOT FOUND: LinkedIn header"
}

# 3. LinkedIn CTA — Action verb
$old3 = 'font-size:.95rem;">View LinkedIn &rarr;</span>'
$new3 = 'font-size:.95rem;">Follow on LinkedIn &rarr;</span>'
if ($html -match [regex]::Escape($old3)) {
    $html = $html -replace [regex]::Escape($old3), $new3
    $changes++
    Write-Host "Changed: LinkedIn CTA"
} else {
    Write-Host "NOT FOUND: LinkedIn CTA"
}

# 4. Blog CTA — Action verb
$old4 = 'font-size:.95rem;">Read the blog &rarr;</span>'
$new4 = 'font-size:.95rem;">Browse articles &rarr;</span>'
if ($html -match [regex]::Escape($old4)) {
    $html = $html -replace [regex]::Escape($old4), $new4
    $changes++
    Write-Host "Changed: Blog CTA"
} else {
    Write-Host "NOT FOUND: Blog CTA"
}

if ($changes -gt 0) {
    [System.IO.File]::WriteAllText("en\index.html", $html, [System.Text.UTF8Encoding]::new($false))
    Write-Host "Total changes: $changes"
} else {
    Write-Host "No changes made"
}
