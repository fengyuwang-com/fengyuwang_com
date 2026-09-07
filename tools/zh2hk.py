#!/usr/bin/env python3
"""zh-cn -> zh-hk: opencc s2hk, 保持姓名 王丰羽 不变。用法: zh2hk.py <src> <dst>"""
import sys
from opencc import OpenCC

src, dst = sys.argv[1], sys.argv[2]
text = open(src, encoding="utf-8").read()
out = OpenCC("s2hk").convert(text).replace("王豐羽", "王丰羽")
open(dst, "w", encoding="utf-8").write(out)
print(f"{dst} written ({len(out)} chars)")
