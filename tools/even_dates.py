#!/usr/bin/env python3
"""把全部已发布博文的发布日期在"终点=最新日期"基础上按固定间隔均匀重排。

规则:
  - 三语 (zh-cn / zh-hk / en) 同一目录名视为同文, 赋相同新日期;
  - 排序保持原有相对顺序 (旧日期升序, 同日期按目录名);
  - draft: true 的文章不参与, 原日期不动;
  - 幂等: 重复运行结果一致 (顺序不变时)。

用法: python3 tools/even_dates.py [--step-days N] [--dry]
"""
import datetime
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LANGS = ["zh-cn", "zh-hk", "en"]
STEP_DAYS = 2
DRY = "--dry" in sys.argv
for i, a in enumerate(sys.argv):
    if a == "--step-days":
        STEP_DAYS = int(sys.argv[i + 1])

DATE_RE = re.compile(r"^date: (\d{4}-\d{2}-\d{2}).*$", re.M)


def collect():
    """返回 {lang: {slug: (path, old_date)}} 与 {slug: old_date} (以 zh-cn 为序准)。"""
    per_lang = {}
    for l in LANGS:
        d = {}
        posts = ROOT / "hugo/content" / l / "blog/posts"
        for idx in sorted(posts.glob("*/index.md")):
            txt = idx.read_text(encoding="utf-8")
            m = DATE_RE.search(txt)
            if not m:
                sys.exit(f"FATAL: {idx} 无 date 行")
            if "draft: true" in txt.split("\n---")[0]:
                continue  # 草稿不动
            d[idx.parent.name] = (idx, datetime.date.fromisoformat(m.group(1)), txt)
        per_lang[l] = d
    sets = {l: set(per_lang[l]) for l in LANGS}
    if not (sets["zh-cn"] == sets["zh-hk"] == sets["en"]):
        for a in LANGS:
            for b in LANGS:
                if a != b:
                    diff = sets[a] - sets[b]
                    if diff:
                        sys.exit(f"FATAL: {a} 已发布独有 {len(diff)} 篇: {sorted(diff)[:5]}")
    return per_lang


def main():
    per_lang = collect()
    slugs = sorted(per_lang["zh-cn"], key=lambda s: (per_lang["zh-cn"][s][1], s))
    n = len(slugs)
    end = max(d for l in LANGS for _, d, _ in per_lang[l].values())
    new_dates = [end - datetime.timedelta(days=STEP_DAYS * (n - 1 - i)) for i in range(n)]
    print(f"共 {n} 篇已发布, 均匀重排: {new_dates[0]} → {new_dates[-1]} (每 {STEP_DAYS} 天一篇)")
    if DRY:
        for slug, nd in list(zip(slugs, new_dates))[:5] + list(zip(slugs, new_dates))[-3:]:
            print(f"  {per_lang['zh-cn'][slug][1]} -> {nd}  {slug[:40]}")
        return
    changed = 0
    for slug, nd in zip(slugs, new_dates):
        for l in LANGS:
            path, old, txt = per_lang[l][slug]
            if old != nd:
                path.write_text(DATE_RE.sub(f"date: {nd}", txt, count=1), encoding="utf-8")
                changed += 1
    print(f"改写 {changed} 个文件 (三语同步)")


if __name__ == "__main__":
    main()
