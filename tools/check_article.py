#!/usr/bin/env python3
"""发布前校验: 痕迹词 grep + 汉字计数。用法: check_article.py <index.md> [<index.md> ...]"""
import re
import sys

TRACES = ["元宝", "它说", "我问它", "这场对话", "跟AI聊", "跟 AI 聊"]

for path in sys.argv[1:]:
    text = open(path, encoding="utf-8").read()
    body = re.sub(r"^---.*?---", "", text, flags=re.S)  # 不计 front matter
    hits = [t for t in TRACES if t in text]
    han = len(re.findall(r"[\u4e00-\u9fff]", body))
    status = "OK " if not hits else "!!!"
    print(f"{status} {path}  汉字={han}  痕迹词={hits if hits else '无'}")
    if hits:
        for t in hits:
            i = text.find(t)
            print(f"    -> …{text[max(0,i-30):i+30]}…")
