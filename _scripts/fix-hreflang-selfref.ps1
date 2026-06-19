# Fix missing hreflang self-references in blog posts
# Each page must have its own hreflang self-reference per SEO rules
# Use .NET file I/O to preserve original encoding and line endings

$projectRoot = "C:\Users\a8881\Desktop\fengyuwang_com"

# Fix en blog posts - add hreflang="en" after canonical
$enPosts = Get-ChildItem "$projectRoot\en\blog\posts\*\index.html"
$fixedEn = 0
foreach ($file in $enPosts) {
    $path = $file.FullName
    $content = [System.IO.File]::ReadAllText($path)
    if ($content -match '<link rel="canonical" href="(?<url>/en/blog/posts/[^"]+/)">') {
        $canonUrl = $matches['url']
        if ($content -notmatch 'hreflang="en" href="/en/blog/posts/') {
            $selfRef = "    <link rel=""alternate"" hreflang=""en"" href=""$canonUrl"">"
            $content = $content -replace '(<link rel="canonical" href="/en/blog/posts/[^"]+/">)', "`$1`n$selfRef"
            [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
            $fixedEn++
        }
    }
}
Write-Host "Fixed en posts: $fixedEn"

# Fix zh-cn blog posts - add hreflang="zh-CN" after canonical
$zhCnPosts = Get-ChildItem "$projectRoot\zh-cn\blog\posts\*\index.html"
$fixedZhCn = 0
foreach ($file in $zhCnPosts) {
    $path = $file.FullName
    $content = [System.IO.File]::ReadAllText($path)
    if ($content -match '<link rel="canonical" href="(?<url>/zh-cn/blog/posts/[^"]+/)">') {
        $canonUrl = $matches['url']
        if ($content -notmatch 'hreflang="zh-CN" href="/zh-cn/blog/posts/') {
            $selfRef = "    <link rel=""alternate"" hreflang=""zh-CN"" href=""$canonUrl"">"
            $content = $content -replace '(<link rel="canonical" href="/zh-cn/blog/posts/[^"]+/">)', "`$1`n$selfRef"
            [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
            $fixedZhCn++
        }
    }
}
Write-Host "Fixed zh-cn posts: $fixedZhCn"

# Fix zh-hk blog posts - add hreflang="zh-HK" after canonical
$zhHkPosts = Get-ChildItem "$projectRoot\zh-hk\blog\posts\*\index.html"
$fixedZhHk = 0
foreach ($file in $zhHkPosts) {
    $path = $file.FullName
    $content = [System.IO.File]::ReadAllText($path)
    if ($content -match '<link rel="canonical" href="(?<url>/zh-hk/blog/posts/[^"]+/)">') {
        $canonUrl = $matches['url']
        if ($content -notmatch 'hreflang="zh-HK" href="/zh-hk/blog/posts/') {
            $selfRef = "    <link rel=""alternate"" hreflang=""zh-HK"" href=""$canonUrl"">"
            $content = $content -replace '(<link rel="canonical" href="/zh-hk/blog/posts/[^"]+/">)', "`$1`n$selfRef"
            [System.IO.File]::WriteAllText($path, $content, [System.Text.Encoding]::UTF8)
            $fixedZhHk++
        }
    }
}
Write-Host "Fixed zh-hk posts: $fixedZhHk"

# Fix zh-cn/blog/index.html
$cnBlogIndex = "$projectRoot\zh-cn\blog\index.html"
$content = [System.IO.File]::ReadAllText($cnBlogIndex)
if ($content -match '<link rel="canonical" href="/zh-cn/blog/">' -and $content -notmatch 'hreflang="zh-CN"') {
    $selfRef = "    <link rel=""alternate"" hreflang=""zh-CN"" href=""/zh-cn/blog/"">"
    $content = $content -replace '(<link rel="canonical" href="/zh-cn/blog/">)', "`$1`n$selfRef"
    [System.IO.File]::WriteAllText($cnBlogIndex, $content, [System.Text.Encoding]::UTF8)
    Write-Host "Fixed: zh-cn/blog/index.html"
}

# Fix zh-hk/blog/index.html
$hkBlogIndex = "$projectRoot\zh-hk\blog\index.html"
$content = [System.IO.File]::ReadAllText($hkBlogIndex)
if ($content -match '<link rel="canonical" href="/zh-hk/blog/">' -and $content -notmatch 'hreflang="zh-HK"') {
    $selfRef = "    <link rel=""alternate"" hreflang=""zh-HK"" href=""/zh-hk/blog/"">"
    $content = $content -replace '(<link rel="canonical" href="/zh-hk/blog/">)', "`$1`n$selfRef"
    [System.IO.File]::WriteAllText($hkBlogIndex, $content, [System.Text.Encoding]::UTF8)
    Write-Host "Fixed: zh-hk/blog/index.html"
}

Write-Host "`nDone!"
