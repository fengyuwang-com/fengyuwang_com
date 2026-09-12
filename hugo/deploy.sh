#!/bin/bash
echo "[1/3] Building..."
hugo --cleanDestinationDir
if [ $? -ne 0 ]; then exit 1; fi

echo "[2/3] Copying blog files..."
for lang in zh-cn zh-hk en; do
    src="../_site/$lang/blog"
    dst="../$lang/blog"
    if [ -d "$src" ]; then
        rm -rf "$dst"
        cp -r "$src" "$dst"
        echo "  $lang/blog deployed"
    fi
    tagsrc="../_site/$lang/tags"
    tagdst="../$lang/tags"
    if [ -d "$tagsrc" ]; then
        rm -rf "$tagdst"
        cp -r "$tagsrc" "$tagdst"
        echo "  $lang/tags deployed"
    fi
    asrc="../_site/$lang/archive"
    adst="../$lang/archive"
    if [ -d "$asrc" ]; then
        rm -rf "$adst"
        cp -r "$asrc" "$adst"
        echo "  $lang/archive deployed"
    fi
done

echo "[3/3] Regenerating sitemap..."
python3 ../tools/gen_sitemap.py || exit 1

rm -rf ../_site
echo "Done."