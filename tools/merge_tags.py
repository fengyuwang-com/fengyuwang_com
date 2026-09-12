#!/usr/bin/env python3
"""把博文标签收敛到 6 大领域, 三语以 zh-cn 为准一一对应。

6 大领域: 投资 / 商业 / 技术 / 市场 / 经济 / 社会
合并规则 (zh): 市场学→市场, 科技→技术, 风险→投资, 数学→技术, 组织→商业, 金融→经济, 立场→删除
草稿不动; 每篇标签去重后按 CANON 顺序输出, 简体/繁体/英文三语同步重写。

用法: python3 tools/merge_tags.py [--dry]
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ["zh-cn", "zh-hk", "en"]
DRY = "--dry" in sys.argv

CANON = ["投资", "商业", "技术", "市场", "经济", "社会"]
MERGE = {"市场学": "市场", "科技": "技术", "风险": "投资", "数学": "技术",
         "组织": "商业", "金融": "经济", "立场": None}
TRAD = {"投资": "投資", "商业": "商業", "技术": "技術", "市场": "市場",
        "经济": "經濟", "社会": "社會"}
EN = {"投资": "Investing", "商业": "Business", "技术": "Tech", "市场": "Marketing",
      "经济": "Economy", "社会": "Society"}
TAG_RE = re.compile(r"^tags:\s*\[.*?\]\s*$", re.M)


def parse_tags(txt):
    m = TAG_RE.search(txt)
    if not m:
        sys.exit(f"FATAL: 无 inline tags 行")
    return [t.strip().strip("'\"") for t in m.group(0).split("[", 1)[1].rsplit("]", 1)[0].split(",") if t.strip()]


def main():
    zh_root = ROOT / "hugo/content/zh-cn/blog/posts"
    n_changed = 0
    for zh_idx in sorted(zh_root.glob("*/index.md")):
        slug = zh_idx.parent.name
        zh_txt = zh_idx.read_text(encoding="utf-8")
        if "draft: true" in zh_txt.split("\n---")[0]:
            continue
        old = parse_tags(zh_txt)
        merged = []
        for t in old:
            m = MERGE.get(t, t if t in CANON else None)
            if m is None and t not in MERGE:
                sys.exit(f"FATAL: zh-cn 出现未知标签 {t!r} ({slug}) — 先加进 CANON/MERGE")
            if m and m not in merged:
                merged.append(m)
        merged.sort(key=CANON.index)
        if not merged:
            sys.exit(f"FATAL: {slug} 合并后无标签")
        if DRY:
            if old != merged and n_changed < 8:
                print(f"  {old} -> {merged}  {slug[:36]}")
            n_changed += old != merged
            continue
        for l in LANGS:
            path = ROOT / f"hugo/content/{l}/blog/posts" / slug / "index.md"
            txt = path.read_text(encoding="utf-8")
            tags = merged if l == "zh-cn" else ([TRAD[t] for t in merged] if l == "zh-hk" else [EN[t] for t in merged])
            txt2 = TAG_RE.sub("tags: [" + ", ".join(f'"{t}"' for t in tags) + "]", txt, count=1)
            if txt2 != txt:
                path.write_text(txt2, encoding="utf-8")
        n_changed += merged != old
    print(("将改写 %d 篇 (dry)" if DRY else "完成: 改写 %d 篇") % n_changed)


if __name__ == "__main__":
    main()
