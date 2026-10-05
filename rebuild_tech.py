# -*- coding: utf-8 -*-
"""Rebuild tech.html: (1) swap #domains below #method, (2) graphical five-stage cards."""
import io, sys

CSS_ADD = """		.aut-lead{ margin:0 0 9px; font-size:12.5px; color:#475569; line-height:1.7; }
		.aut-lanes{ display:flex; flex-direction:column; gap:8px; margin:0 0 10px; }
		.aut-lane{ display:flex; flex-wrap:wrap; align-items:center; gap:6px; }
		.aut-lane-tag{ display:inline-flex; align-items:center; padding:3px 9px; border-radius:7px; background:#eef4fb; border:1px solid rgba(0,113,227,.28); color:#0071e3; font-size:11px; font-weight:800; }
		.aut-node{ display:inline-flex; align-items:center; padding:6px 11px; border-radius:9px; background:#ffffff; border:1px solid rgba(148,163,184,.28); color:#0f172a; font-size:12px; font-weight:600; line-height:1.35; }
		.aut-node.hl{ background:#eef4fb; border-color:rgba(0,113,227,.35); color:#0071e3; }
		.aut-arr-sm{ color:#0071e3; font-size:12px; font-weight:700; }
		.aut-loop{ display:flex; flex-wrap:wrap; align-items:center; gap:6px; margin:0 0 9px; }
		.aut-chips{ display:flex; flex-wrap:wrap; gap:6px; margin-top:9px; }
		.aut-chip{ display:inline-flex; align-items:center; font-size:11.5px; font-weight:700; color:#2563eb; background:#eef4fb; border-radius:999px; padding:3px 10px; }
		.aut-chip.muted{ color:#64748b; background:#eef1f5; }
		.aut-mods{ display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:8px; }
		.aut-mod{ display:flex; flex-direction:column; gap:2px; padding:10px 12px; border-radius:11px; background:#ffffff; border:1px solid rgba(148,163,184,.28); min-width:0; }
		.aut-mod-k{ font-size:12px; font-weight:800; color:#0f172a; }
		.aut-mod-s{ font-size:11.5px; color:#475569; line-height:1.5; }
		.aut-mod-d{ font-size:11px; font-weight:700; color:#2563eb; }
		.aut-mod-d.off{ color:#94a3b8; }
		body[data-theme="dark"] .aut-node{ background:#0f172a; border-color:rgba(148,163,184,.18); color:#e5ecf4; }
		body[data-theme="dark"] .aut-node.hl{ background:rgba(41,151,255,.14); border-color:rgba(41,151,255,.35); color:#2997ff; }
		body[data-theme="dark"] .aut-lane-tag{ background:rgba(41,151,255,.14); border-color:rgba(41,151,255,.30); color:#2997ff; }
		body[data-theme="dark"] .aut-arr-sm{ color:#2997ff; }
		body[data-theme="dark"] .aut-chip{ background:rgba(41,151,255,.14); color:#2997ff; }
		body[data-theme="dark"] .aut-chip.muted{ background:rgba(148,163,184,.16); color:#94a3b8; }
		body[data-theme="dark"] .aut-mod{ background:#0f172a; border-color:rgba(148,163,184,.18); }
		body[data-theme="dark"] .aut-mod-k{ color:#f5f5f7; }
		body[data-theme="dark"] .aut-mod-s, body[data-theme="dark"] .aut-lead{ color:#c7d2e0; }
		body[data-theme="dark"] .aut-mod-d{ color:#2997ff; }
		.dom-flow{ display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:8px; margin:6px 0 12px; }
		.dom-node{ display:inline-flex; align-items:center; padding:8px 16px; border-radius:10px; background:#f5f5f7; border:1px solid rgba(148,163,184,.22); color:#0f172a; font-size:13px; font-weight:700; }
		.dom-arr{ color:#0071e3; font-weight:700; }
		.dom-pipe{ display:flex; flex-wrap:wrap; align-items:center; justify-content:center; gap:8px; }
		.dom-step{ display:inline-flex; align-items:center; padding:7px 14px; border-radius:999px; background:#ffffff; border:1px solid rgba(148,163,184,.28); color:#475569; font-size:12.5px; font-weight:700; }
		.dom-step.hl{ background:#eef4fb; border-color:rgba(0,113,227,.35); color:#0071e3; }
		.dom-arr2{ color:#94a3b8; font-weight:700; }
		body[data-theme="dark"] .dom-node{ background:#0f172a; border-color:rgba(148,163,184,.18); color:#f5f5f7; }
		body[data-theme="dark"] .dom-step{ background:#0f172a; border-color:rgba(148,163,184,.18); color:#c7d2e0; }
		body[data-theme="dark"] .dom-step.hl{ color:#2997ff; border-color:rgba(41,151,255,.35); }
"""

A = lambda t="→": '<span class="aut-arr-sm" aria-hidden="true">%s</span>' % t
def N(s, hl=False): return '<span class="aut-node%s">%s</span>' % (" hl" if hl else "", s)
def LANE(tag, *p): return '<div class="aut-lane"><span class="aut-lane-tag">%s</span>%s</div>' % (tag, "".join(p))
def CHIP(s, m=False): return '<span class="aut-chip%s">%s</span>' % (" muted" if m else "", s)
def CHIPS(*c): return '<div class="aut-chips">%s</div>' % "".join(c)
def MOD(k, s, d, off=False): return '<div class="aut-mod"><span class="aut-mod-k">%s</span><span class="aut-mod-s">%s</span><span class="aut-mod-d%s">%s</span></div>' % (k, s, " off" if off else "", d)
def MODS(*m): return '<div class="aut-mods">%s</div>' % "".join(m)
def LEAD(t): return '<p class="aut-lead">%s</p>' % t

# per-language pieces: (research card, think card, create card, act card, si card, dom graphic)
L = {}

L["zh-cn"] = dict(
    research_lanes=[("主车道", [N("market APIs"), A(), N("FengInvest scripts"), A(), N("自建本地 SQL 库", True)]),
                    ("副车道", [N("自建通用系统"), A(), N("先授权"), A(), N("再调 API")])],
    research_chips=["FengInvest 91 scripts", "generic retrieval 6 backends", "AIExport 13 dirs · 36 scripts",
                    "自建 SQL 库 1 .db", "settled corpus 862 ch · 5.7 MB", "research ledger 37 records · done 27", "Search King 搜任何站点"],
    think_flow=[N("读 MD docs"), A(), N("身份 · 规则 · 任务"), A(), N("执行"), A(), N("写回 ledger · log", True)],
    think_chips=["9 guides", "117 scripts", "12 docs", "2 skills"],
    think_muted="GUI autopilot · planned / read-only",
    create_lead="做出一件东西，尚未分发——FengMedia 37 个项目（2026-10-05《强将手下无弱兵》）是由选题到成片的创作中枢；FengInvest 91 scripts 也算 create（行情研究 / 资产分析报告）。",
    create_mods=[("Text", "文本生成", "作品留在本地", False), ("Image", "图像生成", "—", True),
                 ("Music", "音乐生成 · FengMusician", "12 tools · gate ✓", False),
                 ("Voice", "TTS · TTS-UI bundled", "桌面捆绑包留在本地", False),
                 ("Avatars", "数字人", "live ✓ · anime 验证中", False),
                 ("Video", "视频生成 · HyperFrames", "— 草稿可自 MoneyPrinterTurbo", True)],
    create_chips=["FengMedia 37 projects", "Music 12 tools · gate ✓", "Avatars live ✓", "FengInvest 91 scripts"],
    act_lanes=[("表单", [N("JobHunter"), A(), N("通用批量表单执行 / 自动填表"), A(), N("授权范围内对外提交", True), N("CLI ✓ · 1 profiles · confirmed local")]),
               ("邮件", [N("FengMail / FENGmailMac"), A(), N("authorized → API 投递", True), N("confirmed local")]),
               ("渠道", [N("Git 双推 GitHub + gitee"), N("read-only documented"), N("authorized → external APIs"), N("credentials never shown")]),
               ("执行器", [N("GUI agent"), A("+"), N("CLI agent"), A("+"), N("MD docs"), N("CLI · 1 profiles · planned")])],
    si_flow=[N("每轮记录 · FENGMEM 追加 · todo 销账 · 复盘写回"), A(), N("规则在 AGENTS.md 重写 · 下一轮立即生效"), A("↻"), N("回到 Research", True)],
    si_lead="Docs are the control plane——每轮迭代重写宪法，宪法塑造下一轮循环；AI 是最严格的读者，它按字面执行。",
    si_chips=["FengOrchestrator 12 docs · 2 skills", "FengASNI 一机一份 MD profile"],
    dom_flow=["Web", "桌面 Desktop", "嵌入式 Embedded"],
    dom_pipe=["结构设计", "代码", "交付"],
)

L["zh-hk"] = dict(
    research_lanes=[("主車道", [N("market APIs"), A(), N("FengInvest scripts"), A(), N("自建本地 SQL 庫", True)]),
                    ("副車道", [N("自建通用系統"), A(), N("先授權"), A(), N("再調 API")])],
    research_chips=["FengInvest 91 scripts", "generic retrieval 6 backends", "AIExport 13 dirs · 36 scripts",
                    "自建 SQL 庫 1 .db", "settled corpus 862 ch · 5.7 MB", "research ledger 37 records · done 27", "Search King 由任何地方搜尋任何網站"],
    think_flow=[N("讀 MD docs"), A(), N("身份 · 規則 · 任務"), A(), N("執行"), A(), N("寫回 ledger · log", True)],
    think_chips=["9 guides", "117 scripts", "12 docs", "2 skills"],
    think_muted="GUI autopilot · planned / read-only",
    create_lead="做出一件東西，尚未分發——FengMedia 37 個項目（2026-10-05《強將手下無弱兵》）是由選題到成片的創作中樞；FengInvest 91 scripts 都算 create（市場研究 / 資產分析報告）。",
    create_mods=[("Text", "文字生成", "作品留在本地", False), ("Image", "圖像生成", "—", True),
                 ("Music", "音樂生成 · FengMusician", "12 tools · gate ✓", False),
                 ("Voice", "TTS · TTS-UI bundled", "桌面捆綁包留在本地", False),
                 ("Avatars", "數碼人", "live ✓ · anime 驗證中", False),
                 ("Video", "影片生成 · HyperFrames", "— 草稿可由 MoneyPrinterTurbo 起步", True)],
    create_chips=["FengMedia 37 projects", "Music 12 tools · gate ✓", "Avatars live ✓", "FengInvest 91 scripts"],
    act_lanes=[("表單", [N("JobHunter"), A(), N("通用批量表單執行 / 自動填表"), A(), N("授權範圍內對外提交", True), N("CLI ✓ · 1 profiles · confirmed local")]),
               ("郵件", [N("FengMail / FENGmailMac"), A(), N("authorized → API 投遞", True), N("confirmed local")]),
               ("渠道", [N("Git 雙推 GitHub + gitee"), N("read-only documented"), N("authorized → external APIs"), N("credentials never shown")]),
               ("執行器", [N("GUI agent"), A("+"), N("CLI agent"), A("+"), N("MD docs"), N("CLI · 1 profiles · planned")])],
    si_flow=[N("每輪記錄 · FENGMEM 追加 · todo 銷帳 · 複盤寫回"), A(), N("規則在 AGENTS.md 重寫 · 下一輪立即生效"), A("↻"), N("回到 Research", True)],
    si_lead="Docs are the control plane——每輪迭代重寫憲法，憲法塑造下一輪循環；AI 是更嚴格的讀者，它按字面執行。",
    si_chips=["FengOrchestrator 12 docs · 2 skills", "FengASNI 一機一份 MD profile"],
    dom_flow=["Web", "桌面 Desktop", "嵌入式 Embedded"],
    dom_pipe=["結構設計", "代碼", "交付"],
)

L["en"] = dict(
    research_lanes=[("Main lane", [N("market APIs"), A(), N("FengInvest scripts"), A(), N("self-built local SQL", True)]),
                    ("Second lane", [N("self-built generic system"), A(), N("authorized first"), A(), N("then calls APIs")])],
    research_chips=["FengInvest 91 scripts", "generic retrieval 6 backends", "AIExport 13 dirs · 36 scripts",
                    "self-built SQL 1 .db", "settled corpus 862 ch · 5.7 MB", "research ledger 37 records · done 27", "Search King searches any site"],
    think_flow=[N("read MD docs"), A(), N("identity · rules · tasks"), A(), N("execute"), A(), N("write back to ledger · log", True)],
    think_chips=["9 guides", "117 scripts", "12 docs", "2 skills"],
    think_muted="GUI autopilot · planned / read-only",
    create_lead="CREATE = you make a thing, not yet distributed — FengMedia 37 projects (2026-10-05, “Under a strong general there are no weak soldiers”), the hub from topic to finished video; FengInvest 91 scripts counts as create too (market research / asset analysis reports).",
    create_mods=[("Text", "text generation", "works stay local", False), ("Image", "image generation", "—", True),
                 ("Music", "music generation · FengMusician", "12 tools · gate ✓", False),
                 ("Voice", "TTS · TTS-UI bundled", "desktop bundle stays local", False),
                 ("Avatars", "digital humans", "live ✓ · anime verifying", False),
                 ("Video", "video generation · HyperFrames", "— drafts may start from MoneyPrinterTurbo", True)],
    create_chips=["FengMedia 37 projects", "Music 12 tools · gate ✓", "Avatars live ✓", "FengInvest 91 scripts"],
    act_lanes=[("Forms", [N("JobHunter"), A(), N("generic batch form execution / auto-fill"), A(), N("outward submission within scope", True), N("CLI ✓ · 1 profiles · confirmed local")]),
               ("Mail", [N("FengMail / FENGmailMac"), A(), N("authorized → API delivery", True), N("confirmed local")]),
               ("Channels", [N("Git dual push GitHub + gitee"), N("read-only documented"), N("authorized → external APIs"), N("credentials never shown")]),
               ("Executors", [N("GUI agent"), A("+"), N("CLI agent"), A("+"), N("MD docs"), N("CLI · 1 profiles · planned")])],
    si_flow=[N("every round recorded · FENGMEM append · todo write-off · retrospective"), A(), N("rules rewritten in AGENTS.md · effective next round"), A("↻"), N("back to Research", True)],
    si_lead="Docs are the control plane — each iteration rewrites the constitution, the constitution shapes the next loop; AI is the stricter reader, it executes literally.",
    si_chips=["FengOrchestrator 12 docs · 2 skills", "FengASNI one MD profile per machine"],
    dom_flow=["Web", "Desktop", "Embedded"],
    dom_pipe=["Structure", "Code", "Delivery"],
)

def build_grid(d):
    parts = []
    parts.append('					<div class="aut-grid">')
    parts.append('						<div class="aut-card">')
    parts.append('							<h3>Research%s</h3>' % (" · 研究" if False else ""))
    parts.append('</div>')
    return parts

def research_h(lang):
    return {"zh-cn": "Research · 研究", "zh-hk": "Research · 研究", "en": "Research"}[lang]
def think_h(lang):
    return {"zh-cn": "Think · 思考", "zh-hk": "Think · 思考", "en": "Think"}[lang]
def create_h(lang):
    return {"zh-cn": "Create · 创作", "zh-hk": "Create · 創作", "en": "Create"}[lang]
def act_h(lang):
    return {"zh-cn": "Act · 行动", "zh-hk": "Act · 行動", "en": "Act"}[lang]
def si_h(lang):
    return {"zh-cn": "Self-Improve · 自我改进", "zh-hk": "Self-Improve · 自我改進", "en": "Self-Improve"}[lang]

def grid_html(lang):
    d = L[lang]
    def c(h3, inner, wide=False):
        return '						<div class="aut-card%s">\n							<h3>%s</h3>\n%s\n						</div>' % (" aut-wide" if wide else "", h3, inner)
    r = c(research_h(lang), '<div class="aut-lanes">%s</div>\n%s' % (
        "".join(LANE(t, *p) for t, p in d["research_lanes"]),
        CHIPS(*[CHIP(x) for x in d["research_chips"]])))
    t = c(think_h(lang), '<div class="aut-loop">%s</div>\n%s' % (
        "".join(d["think_flow"]),
        CHIPS(*[CHIP(x) for x in d["think_chips"]] + [CHIP(d["think_muted"], True)])))
    cr = c(create_h(lang), "%s\n%s\n%s" % (
        LEAD(d["create_lead"]),
        MODS(*[MOD(*m) for m in d["create_mods"]]),
        CHIPS(*[CHIP(x) for x in d["create_chips"]])), wide=True)
    ac = c(act_h(lang), '<div class="aut-lanes">%s</div>' % "".join(LANE(t, *p) for t, p in d["act_lanes"]), wide=True)
    si = c(si_h(lang), '<div class="aut-loop">%s</div>\n%s\n%s' % (
        "".join(d["si_flow"]), LEAD(d["si_lead"]), CHIPS(*[CHIP(x) for x in d["si_chips"]])), wide=True)
    return '					<div class="aut-grid">\n' + "\n".join([r, t, cr, ac, si]) + '\n					</div>'

def dom_html(lang):
    d = L[lang]
    return ('						<div class="dom-flow">%s</div>\n'
            '						<div class="dom-pipe">%s</div>\n') % (
        "".join([N_HTML(d["dom_flow"][0], "dom-node"), '<span class="dom-arr" aria-hidden="true">→</span>',
                 N_HTML(d["dom_flow"][1], "dom-node"), '<span class="dom-arr" aria-hidden="true">→</span>',
                 N_HTML(d["dom_flow"][2], "dom-node")]),
        "".join([N_HTML(d["dom_pipe"][0], "dom-step"), '<span class="dom-arr2" aria-hidden="true">→</span>',
                 N_HTML(d["dom_pipe"][1], "dom-step"), '<span class="dom-arr2" aria-hidden="true">→</span>',
                 N_HTML(d["dom_pipe"][2], "dom-step hl")]))

def N_HTML(s, cls):
    return '<span class="%s">%s</span>' % (cls, s)

ANCHOR_TAGLINE = '\t\t.aut-tagline{ margin:18px 0 0; text-align:center; font-size:14px; font-weight:700; color:#0f172a; line-height:1.7; }'
ANCHOR_MQ = '\t\t@media (max-width:767px){ .aut-grid, .tl-grid{ grid-template-columns:minmax(0,1fr); } }'

def process(lang):
    path = "%s/tech.html" % lang
    s = io.open(path, encoding="utf-8").read()
    orig = s

    # 1) CSS inject (idempotent)
    if ".aut-mods{" not in s:
        assert ANCHOR_TAGLINE in s, "tagline anchor missing " + lang
        s = s.replace(ANCHOR_TAGLINE, ANCHOR_TAGLINE + "\n" + CSS_ADD, 1)
    if ".aut-mods{" in s and "aut-mods{ grid-template-columns:minmax(0,1fr); }" not in s:
        assert ANCHOR_MQ in s, "mq anchor missing " + lang
        s = s.replace(ANCHOR_MQ, '\t\t@media (max-width:767px){ .aut-grid, .tl-grid, .aut-mods{ grid-template-columns:minmax(0,1fr); } }', 1)

    # 2) replace aut-grid
    gs = s.index('<div class="aut-grid">')
    ge = s.index('<p class="aut-tagline">')
    s = s[:gs] + grid_html(lang) + "\n" + s[ge:]

    # 3) domains graphic: insert after subtitle </p>
    ds = s.index('<div id="domains" class="content-block">')
    de = s.index('<div id="method" class="content-block">')
    seg = s[ds:de]
    p_end = seg.index('</p>') + len('</p>')
    nl = seg.index('\n', p_end) + 1
    seg = seg[:nl] + dom_html(lang) + seg[nl:]
    s = s[:ds] + seg + s[de:]

    # 4) reorder: method before domains
    ds = s.index('<div id="domains" class="content-block">')
    ds_c = s.rindex('<!--', 0, ds)
    ms = s.index('<div id="method" class="content-block">')
    js = s.index('<div id="jingxin"')
    # method end: a comment for jingxin if present right before it
    cand = s.rindex('<!--', ms, js) if '<!--' in s[ms:js] else js
    me = cand if (js - cand) < 200 else js
    s = s[:ds_c] + s[ms:me] + s[ds_c:ms] + s[me:]

    # 5) rail swap domains/method
    lines = s.split("\n")
    i_d = next(i for i, l in enumerate(lines) if 'data-rail="domains"' in l)
    i_m = next(i for i, l in enumerate(lines) if 'data-rail="method"' in l)
    lines[i_d], lines[i_m] = lines[i_m], lines[i_d]
    s = "\n".join(lines)

    assert s != orig
    io.open(path, "w", encoding="utf-8").write(s)
    print("done", lang, "len", len(s))

for lg in ["zh-cn", "zh-hk", "en"]:
    process(lg)
print("OK")
