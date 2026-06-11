#!/bin/bash
echo "[1/2] Building..."
hugo --cleanDestinationDir
if [ $? -ne 0 ]; then exit 1; fi

echo "[2/2] Copying blog files..."
for lang in zh-cn zh-hk en; do
    src="../_site/$lang/blog"
    dst="../$lang/blog"
    if [ -d "$src" ]; then
        rm -rf "$dst"
        cp -r "$src" "$dst"
        echo "  $lang/blog deployed"
    fi
done

rm -rf ../_site
echo "Done."