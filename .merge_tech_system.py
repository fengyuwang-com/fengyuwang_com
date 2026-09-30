"""Fold system.html and system-graph.html into tech.html.

The three pages are fragments of one page. system.html and
system-graph.html carry the *same* h1 and, once comments are stripped, the
same 148 selectors with zero value differences — graph just adds 9 `.sn2-*`
canvas rules. They were one page, split. tech.html is the survivor because
it holds 51 inbound links and 5 redirects; the other 51 links need no rewrite.

Order (system/graph's own reading contract: orient, then method, then the
work):

    snapshot hero -> #domains -> #method -> #net -> tech's 12 blocks -> link-card

Why system keeps the hero: it is 1191 chars carrying an eyebrow, a live
counter triple and an EKG heartbeat. tech's hero is an h1 and a sentence.
Keeping tech's would mean demoting the site's most distinctive asset to a
section label. So tech's "技术" becomes #domains' h2 and its one-liner folds
into that block's subtitle.

Why the 1200px rule is scoped, not global: it was added to give the canvas
room, written globally. Carried verbatim it widens all 15 content blocks'
text measure, which is exactly what DESIGN §6 sets at 720px. `#net
.block-inner` wins on specificity (id+class vs class) and the rule sits
last, so no !important is needed.

Why scroll-margin-top must survive: tech.html fires 8 scrollIntoView calls
from its 9 cards but never declared the rule itself — it got away with it
only because its cards are tall. Once the system blocks sit above them, a
missing 76px offset puts every card target under the fixed navbar.

Structural assertions, not regex matches, are the safety net: a previous
one-off regex script died mid-run after already writing half a file, so
every check here is a count or a depth that cannot be fooled by a pattern.
"""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

NL, Q, TAB = chr(10), chr(34), chr(9)

VOID = {"br", "img", "input", "meta", "link", "hr", "source", "path", "circle",
        "use", "rect", "line", "polyline", "polygon", "ellipse", "stop"}
TAG = re.compile(r"<(/?)([a-zA-Z][\w-]*)([^>]*?)(/?)>")

LANG = ("zh-cn", "zh-hk", "en")


RAW_TEXT = {"style", "script", "textarea", "title"}


def element_span(src, pos):
    """Span of the element opening at pos.

    <style>/<script> hold raw text, not markup: a "<" inside their body is not
    a tag, and a "</div>" in a CSS string or a JS string does not close
    anything. Depth-walking straight through them makes the walk run away — on
    tech.html it deleted ~9KB of real body markup. Skip to the matching close
    tag instead of counting.
    """
    m = TAG.match(src, pos)
    if not m or m.group(1):
        return None
    if m.group(2) in VOID or m.group(4):
        return (m.start(), m.end())
    if m.group(2) in RAW_TEXT:
        close = src.index("</%s>" % m.group(2), m.end())
        return (m.start(), close + len(m.group(2)) + 3)
    depth = 0
    for k in TAG.finditer(src, m.start()):
        closing, name, _, selfclose = k.groups()
        if name in VOID or selfclose:
            continue
        depth += -1 if closing else 1
        if depth == 0:
            return (m.start(), k.end())
    return None


def block_span(src, block_id):
    """Span of the whole top-level element carrying id=block_id."""
    i = src.find('id="%s"' % block_id)
    assert i >= 0, "id=%s not found" % block_id
    st = src.rindex("<div", 0, i)
    assert src[st:i].count("<div") == 1, "%s: id is not on the outer div" % block_id
    span = element_span(src, st)
    assert span, "%s: no closing tag" % block_id
    return span


def read(f):
    return open(f, encoding="utf-8", newline="").read()


def write(f, s):
    open(f, "w", encoding="utf-8", newline="").write(s)


def strip_noise(s):
    s = re.sub(r"<script[\s\S]*?</script>", "", s)
    s = re.sub(r"<!--[\s\S]*?-->", "", s)
    return s


def div_balance(s):
    body = strip_noise(s[s.index("<body"):s.index("</body>")])
    return body.count("<div") - body.count("</div>")


# ---------------------------------------------------------------- per-language

# Each language supplies its own strings; nothing is translated here.
HERO_SUFFIX = {
    "zh-cn": "从结构到交付。",
    "zh-hk": "從結構到交付。",
    "en": "From structure to delivery.",
}

DOMAINS_H2 = {
    "zh-cn": "技术不是孤岛",
    "zh-hk": "技術不是孤島",
    "en": "Tech is not an island",
}

RAIL = {
    "zh-cn": [("domains", "六大领域，不是六个孤岛"),
              ("method", "方法，三句话"),
              ("net", "项目关系图")],
    "zh-hk": [("domains", "六大領域，不是六個孤島"),
              ("method", "方法，三句話"),
              ("net", "項目關係圖")],
    "en":    [("domains", "Six domains, not six islands"),
              ("method", "The method, in three lines"),
              ("net", "Project relation graph")],
}

LINKCARD = {
    "zh-cn": dict(cap="工具需要有商业场景才有价值",
                  rows=[("项目全清单", "/system-projects.html"),
                        ("投资框架", "/invest.html")]),
    "zh-hk": dict(cap="工具需要有商業場景才有價值",
                  rows=[("項目全清單", "/system-projects.html"),
                        ("投資框架", "/invest.html")]),
    "en":    dict(cap="Tools need a business context to create value",
                  rows=[("Full project list", "/system-projects.html"),
                        ("Investment framework", "/invest.html")]),
}


def style_blocks(src):
    return [m for m in re.finditer(r"<style[^>]*>([\s\S]*?)</style>", src)]


def build_linkcard(lang, w):
    """One card, one cta-row per row. Every row is opened and closed once —
    an earlier version opened cta-row only for the second row and then closed
    it unconditionally, which left one stray </div> and unbalanced the page."""
    inner = TAB * 3
    out = [TAB * 2 + '<div class="link-card">' + NL,
           inner + "<p>" + w["cap"] + "</p>" + NL]
    for n, (label, href) in enumerate(w["rows"]):
        style = "" if n == 0 else ' style="margin-top:14px"'
        cls = "default-btn" if n == 0 else "default-btn-one"
        out.append(inner + '<div class="cta-row"' + style + ">" + NL)
        out.append(inner + TAB + '<a class="%s" href="/%s%s">%s</a>' % (cls, lang, href, label) + NL)
        out.append(inner + "</div>" + NL)
    out.append(TAB * 2 + "</div>" + NL)
    return "".join(out)


def build_rail(lang, links):
    inner = TAB * 2
    out = [TAB + '<nav class="fx-rail" aria-label="本页段落导航">' + NL]
    for target, tip in links:
        out.append(inner + '<a href="#%s" data-rail="%s">' % (target, target)
                   + '<span class="fx-dot" aria-hidden="true"></span>'
                   + '<span class="fx-tip">%s</span></a>' % tip + NL)
    out.append(TAB + "</nav>" + NL)
    return "".join(out)


for lang in LANG:
    f_tech = "%s/tech.html" % lang
    f_sys = "%s/system.html" % lang
    f_graph = "%s/system-graph.html" % lang

    tech = read(f_tech)
    if 'id="sn2Data"' in tech:
        print("%-24s already merged" % f_tech)
        continue

    sys_src = read(f_sys)
    graph = read(f_graph)

    # ---- 1. slices out of the two source pages -------------------------
    # The hero must be extracted by depth, not by a lazy regex: it contains
    # nested divs (sys-snapshot > sys-stat), and [\s\S]*?</div> stops at the
    # first close and truncates the counter triple.
    c_m = re.search(r'<div class="container">', sys_src)
    assert c_m, "%s: container not found" % f_sys
    c_span = element_span(sys_src, c_m.start())
    assert c_span, "%s: container is unclosed" % f_sys
    container = sys_src[c_m.start():c_span[1]]
    h_m = re.search(r'<div class="marketing-hero">', container)
    assert h_m, "%s: snapshot hero not found" % f_sys
    h_span = element_span(container, h_m.start())
    assert h_span, "%s: hero is unclosed" % f_sys
    hero = container[h_span[0]:h_span[1]]
    # the hero must be the container's only child, or the other children are
    # being dropped on the floor
    rest = strip_noise(container[len('<div class="container">'):h_span[0]] + container[h_span[1]:-len("</div>")])
    assert not rest.strip(), "%s: container has children besides the hero: %r" % (f_sys, rest[:120])

    domains = sys_src[slice(*block_span(sys_src, "domains"))]
    method = sys_src[slice(*block_span(sys_src, "method"))]
    net = graph[slice(*block_span(graph, "net"))]

    sn2 = re.search(r'<script type="application/json" id="sn2Data">[\s\S]*?</script>', graph)
    assert sn2, "%s: sn2Data block not found" % f_graph
    sn2data = sn2.group(0)

    # The canvas IIFE is the inline block that follows the sn2Data block and
    # does not touch the DOM in a way the reveal IIFE does. Locate it by
    # signature: it is the longest inline script referencing sn2.
    inlines = [m for m in re.finditer(r"<script(?![^>]*src=)(?![^>]*json)[^>]*>([\s\S]*?)</script>", graph)]
    canvas = max((m for m in inlines if "sn2Data" in m.group(1)), key=lambda m: len(m.group(1)), default=None)
    assert canvas, "%s: canvas script not found" % f_graph
    canvas_js = canvas.group(0)

    reveal = max((m for m in inlines if "IntersectionObserver" in m.group(1)),
                 key=lambda m: len(m.group(1)), default=None)
    assert reveal, "%s: reveal script not found" % f_sys

    sn2_css = max((m for m in style_blocks(graph) if "sn2-stage" in m.group(1)), key=lambda m: len(m.group(1)))
    sys_css = max((m for m in style_blocks(sys_src) if ".block-inner" in m.group(1)), key=lambda m: len(m.group(1)))

    # ---- 2. scoped width rule replaces the global one -----------------
    wide = re.search(r"[ \t]*\.block-inner\{ max-width: 1200px; \}\n[ \t]*\.block-inner h2, \.block-subtitle\{ max-width: 720px; \}\n", sn2_css.group(1))
    assert wide, "%s: the 1200px rule is gone — check the scope fix" % f_graph
    scoped = (NL + "/* The canvas is a fixed 1440x920 raster target and needs the"
              + NL + "   room; every other block on this page keeps the 720px measure"
              + NL + "   (DESIGN §6). id+class beats the base .block-inner, and this"
              + NL + "   block is last, so no !important is needed. */" + NL
              + TAB + "#net .block-inner{ max-width: 1200px; }" + NL
              + TAB + "#net .block-inner h2, #net .block-subtitle{ max-width: 720px; }" + NL)
    sn2_css_txt = sn2_css.group(1).replace(wide.group(0), scoped)

    # ---- 3. CSS: system base, then tech's unique layer ----------------
    # Concatenating is deliberate. Hand-merging 148+78 rules by hand is how
    # values get silently dropped; the cascade does the work instead. The
    # six tech/system disagreements are resolved by source order, and every
    # one of them favours system (measured, not assumed):
    #   .content-block      +scroll-margin-top:76px  <- required by 8 scrollIntoView calls
    #   .marketing-hero     +position:relative       <- FX heading layer
    #   .block-inner h2     +position:relative       <- same
    #   .marketing-hero h1  margin-bottom 10->12px   <- tuned against the snapshot stack
    #   .marketing-hero p   max-width 640->660px     <- same
    #   dark .content-text-card border .03->.04 + box-shadow:none  <- DESIGN §9, commit 2820f7ee
    # .punchline exists only in tech and stays live; system's copy is inside
    # a DEAD CODE wrapper tuned to a layout that no longer exists.
    tech_styles = style_blocks(tech)
    tech_css = max((m for m in tech_styles if ".mkt-card" in m.group(1)), key=lambda m: len(m.group(1)))
    # tech ships a second sheet (467 chars) holding prefers-reduced-motion and
    # the .img-caption rules. It is not the .mkt-card sheet, so selecting by
    # that selector alone would silently drop both on the floor.
    tech_extra = [m.group(1) for m in tech_styles if m is not tech_css]
    assert len(tech_extra) == 1, "%s: unexpected tech sheet count" % f_tech
    assert "prefers-reduced-motion" in tech_extra[0] and "img-caption" in tech_extra[0], \
        "%s: tech's second sheet is not the one expected" % f_tech
    # That sheet opens a nested <style> mid-way and never closes it (the same
    # quirk as the source). Carried verbatim it would swallow the rest of the
    # merged sheet, so the stray tag is dropped — the rules around it are kept.
    tech_extra[0] = tech_extra[0].replace("<style>", "")
    assert "<style" not in tech_extra[0], "%s: nested <style> survived" % f_tech
    # merged_css is the *inner* CSS text of all three sheets, with no <style>
    # tags of its own — the caller wraps it once. The sn2 block is graph's
    # third sheet with the global 1200px rule swapped for the scoped one.
    #
    # Two bugs lived here and both were invisible in the file: sn2's text used
    # to be appended after sys_css.group(0)'s closing tag, parking the whole
    # canvas stylesheet in the body as orphaned text; and sys/tech were
    # spliced in as whole <style>…</style> elements, so the head ended up with
    # a doubled <style><style> and the browser swallowed the nested content as
    # raw text. Group(1) is the inner text; the tags come from one wrapper.
    merged_css = (sys_css.group(1) + NL + tech_css.group(1) + NL
                  + tech_extra[0] + NL + sn2_css_txt)
    assert "<style" not in merged_css, "%s: merged_css must be bare CSS text" % f_tech
    assert "#net .block-inner{ max-width: 1200px; }" in merged_css, \
        "%s: scoped width rule missing from the merged sheet" % f_tech
    assert ".sn2-stage" in merged_css and ".mkt-card" in merged_css, \
        "%s: a source sheet was dropped" % f_tech
    # canvas CSS last, so it wins the cascade against tech's rules
    assert merged_css.rindex(".sn2-stage") > merged_css.rindex(".mkt-card"), \
        "%s: canvas CSS must come last" % f_tech

    # ---- 4. head: keep tech's skeleton, rewrite the SEO --------------
    # Both roles now live at /tech, so the description has to carry both.
    SEO = {
        "zh-cn": dict(
            title="技术 · 体系全景 | 王丰羽 Fengyu WANG",
            desc="六个领域的关系图与方法三句话，一张可交互的项目关系图（78 个项目、135 组引用），"
                 "以及静心、FengOffice、Search-King 等技术项目的实现与能力清单。",
            kw="王丰羽 技术, 体系全景, 项目关系图, 自有项目, 软件交付, 自动化, Web, Python, 架构, 工程",
            og="78 个自有项目、135 组有据可查的引用关系，配六大领域关系图与方法三句话。"),
        "zh-hk": dict(
            title="技術 · 體系全景 | 王丰羽 Fengyu WANG",
            desc="六個領域的關係圖與方法三句話，一張可互動的項目關係圖（78 個項目、135 組引用），"
                 "以及靜心、FengOffice、Search-King 等技術項目的實現與能力清單。",
            kw="王豐羽 技術, 體系全景, 項目關係圖, 自有項目, 軟件交付, 自動化, Web, Python, 架構, 工程",
            og="78 個自有項目、135 組有據可查的引用關係，配六大領域關係圖與方法三句話。"),
        "en": dict(
            title="Tech · System Overview | 王丰羽 Fengyu WANG",
            desc="A relation map of six domains and the method in three lines, an interactive graph of "
                 "78 projects and 135 cited relations, plus how the shipped software — Jingxin, "
                 "FengOffice, Search-King — actually gets built.",
            kw="Fengyu WANG tech, system overview, project graph, shipped projects, software delivery, automation, Web, Python, architecture",
            og="78 shipped projects and 135 cited relations, with a six-domain map and the method in three lines."),
    }
    seo = SEO[lang]
    out = tech
    out = re.sub(r"<title>[^<]*</title>", "<title>" + seo["title"] + "</title>", out, count=1)
    out = re.sub(r'(<meta name="description" content=")[^"]*(")',
                 lambda m: m.group(1) + seo["desc"] + m.group(2), out, count=1)
    out = re.sub(r'(<meta name="keywords" content=")[^"]*(")',
                 lambda m: m.group(1) + seo["kw"] + m.group(2), out, count=1)
    out = re.sub(r'(<meta property="og:title" content=")[^"]*(")',
                 lambda m: m.group(1) + seo["title"] + m.group(2), out, count=1)
    out = re.sub(r'(<meta property="og:description" content=")[^"]*(")',
                 lambda m: m.group(1) + seo["og"] + m.group(2), out, count=1)
    out = re.sub(r'(<meta name="twitter:title" content=")[^"]*(")',
                 lambda m: m.group(1) + seo["title"] + m.group(2), out, count=1)
    out = re.sub(r'(<meta name="twitter:description" content=")[^"]*(")',
                 lambda m: m.group(1) + seo["desc"] + m.group(2), out, count=1)
    out = re.sub(r'"name":"技术[^"]*"', '"name":"技术 · 体系全景"', out, count=1)
    out = re.sub(r'"name":"技術[^"]*"', '"name":"技術 · 體系全景"', out, count=1)
    out = re.sub(r'"name":"Tech[^"]*"', '"name":"Tech · System Overview"', out, count=1)

    # navbar cache-bust (pitfalls §14: a nav change without a bump ships stale)
    out = out.replace("shared-subpage-navbar.js?v=26.09.26.08.40",
                      "shared-subpage-navbar.js?v=26.09.30.01.00")

    # ---- 5. body: one hero, three blocks, one link-card ---------------
    # tech's hero is replaced, not appended to: a second .marketing-hero
    # would open a 52px empty band mid-page — the "white patch" this whole
    # exercise started from.
    # These two must match against `out`, not `tech`: the SEO rewrites above
    # already changed the length, so offsets taken from `tech` slice the wrong
    # span and eat the container.
    old_hero = re.search(r"[ \t]*<!-- Hero -->\n[ \t]*<div class=\"marketing-hero\">[\s\S]*?</div>\n", out)
    assert old_hero, "%s: tech hero not found" % f_tech
    tech_lede = re.search(r"<div class=\"marketing-hero\">\s*<h1>[^<]*</h1>\s*<p>([^<]*)</p>", out)
    assert tech_lede, "%s: tech hero lede not found" % f_tech

    out = out[:old_hero.start()] + out[old_hero.end():]
    # Anchor on the container, not on what follows it: tech's hero (already
    # removed above) used to be the first child.
    out = out.replace('<div class="container">' + NL, '<div class="container">' + NL + hero + NL, 1)
    assert "sys-snapshot" in out, "%s: snapshot hero was not spliced in" % f_tech

    # tech's "技术" survives as a section label; its one-liner joins the subtitle
    domains_new = re.sub(r"(<h2>)[^<]*(</h2>)",
                         lambda m: m.group(1) + DOMAINS_H2[lang] + m.group(2), domains, count=1)
    sub = re.search(r'(<p class="block-subtitle"[^>]*>)([^<]*)(</p>)', domains_new)
    assert sub, "%s: #domains subtitle not found" % f_sys
    domains_new = (domains_new[:sub.start(2)] + sub.group(2).rstrip()
                   + " " + tech_lede.group(1) + " " + HERO_SUFFIX[lang] + " "
                   + domains_new[sub.end(2):])

    # The three orientation blocks go after the container, as page-wrap
    # siblings like every other content block. tech's card-grid is lifted out
    # of the container first so it lands after them: the reading order is
    # orient -> method -> flagship projects, and the widest, most expensive
    # block on the page is deliberately not the landing block.
    cont = element_span(out, out.index('<div class="container">'))
    assert cont, "%s: container is unclosed" % f_tech
    grid = re.search(r'<div class="card-grid">', out)
    assert grid, "%s: card-grid not found" % f_tech
    grid_span = element_span(out, grid.start())
    assert grid_span, "%s: card-grid is unclosed" % f_tech
    grid_html = out[grid_span[0]:grid_span[1]]
    out = out[:grid_span[0]] + out[grid_span[1]:]

    cont = element_span(out, out.index('<div class="container">'))
    at = cont[1]
    out = (out[:at] + NL + domains_new + NL + method + NL + net + NL
           + "<!-- Card grid -->" + NL + grid_html + out[at:])

    # fx-rail: one instance, three static dots (system-projects.html sets the
    # precedent; graph's rail was an empty <nav> and never had links).
    #
    # These two mount points live *outside* .marketing-hero — between the
    # navbar <script> and .page-wrap. The hero is the only thing this
    # function lifted out of system.html, so they never came along. A
    # str.replace whose needle is missing returns the string unchanged and
    # says nothing, which is exactly how they were dropped in the first run;
    # hence the explicit count check rather than a bare replace.
    rail_old = re.search(r"[ \t]*<nav class=\"fx-rail\"[\s\S]*?</nav>\n", out)
    assert not rail_old, "%s: tech already has a rail" % f_tech
    assert out.count('<div class="page-wrap">') == 1, "%s: page-wrap anchor not unique" % f_tech
    mounts = (build_rail(lang, RAIL[lang])
              + TAB + '<div class="fx-progress" aria-hidden="true"><i id="fxProgress"></i></div>' + NL)
    assert out.count("<div class=\"page-wrap\">") == 1, "%s: no page-wrap to anchor to" % f_tech
    out = out.replace("<div class=\"page-wrap\">", mounts + TAB + "<div class=\"page-wrap\">", 1)
    assert 'id="fxProgress"' in out and out.count('class="fx-rail"') == 1, \
        "%s: fx mounts did not land" % f_tech

    # Drop tech's original stylesheet (lines 38-158 in the source) — the
    # merged sheet replaces it. This must run BEFORE the merged sheet is
    # injected: the removal anchors on "the last <style> before the navbar
    # script", and once the merged sheet is in the head that anchor points at
    # the merged sheet instead of tech's. Anchored on the navbar script rather
    # than on "<style> followed by <script src=>": between the two sit a
    # prefers-reduced-motion block, a nested img-caption <style>, and a
    # JSON-LD <script>, so the looser pattern matched nothing at all and
    # dropped tech's rules silently.
    navbar_anchor = '<script src="../assets/js/shared-subpage-navbar.js'
    assert out.count(navbar_anchor) == 1, "%s: navbar anchor not unique" % f_tech
    n_before = out.count("<style>")
    # Remove the whole run of tech's own sheets, from the first <style> open
    # before the anchor through the last </style> before it. tech.html's head
    # has three opens and two closes (verified in git HEAD, predates this work):
    # the img-caption sheet is opened *inside* the prefers-reduced-motion sheet
    # and the two share one </style>. Walking depth from the outer open stops
    # at that shared close and orphans the inner sheet, which then swallows
    # everything after it — including the merged sheet. So the run is cut by
    # position, not by nesting.
    pre = out[:out.index(navbar_anchor)]
    opens = [m.start() for m in re.finditer(r"<style[^>]*>", pre)]
    closes = [m.end() for m in re.finditer(r"</style>", pre)]
    assert opens and closes, "%s: no stylesheet to remove" % f_tech
    assert max(closes) < out.index(navbar_anchor), "%s: style run is not contiguous" % f_tech
    out = out[:opens[0]] + out[max(closes):]
    head_end = out[:out.index(navbar_anchor)]
    assert "<style" not in head_end, "%s: a stylesheet survived the removal" % f_tech
    # The removed rules now live only in merged_css (built earlier, injected
    # just below), so that is where they must still be found.
    assert "prefers-reduced-motion" in merged_css and "img-caption-1" in merged_css, \
        "%s: tech's second sheet was dropped" % f_tech
    assert out.count("<style>") < n_before, "%s: tech's stylesheet not removed" % f_tech

    out = out.replace("</head>", "<style>" + merged_css + "</style>" + NL + "</head>", 1)
    assert merged_css in out, "%s: merged stylesheet did not land" % f_tech
    # A doubled "<style><style>" is the failure this whole rewrite exists to
    # prevent: the browser treats everything after the inner tag as raw text
    # and silently drops the rest of the sheet. Check the assembled head, not
    # the variables — each of them looks fine on its own.
    #
    # Counting <style> against </style> is not a usable check here: tech.html
    # ships 3 opens and 2 closes in <head> (verified in git HEAD, predates
    # this work) because the img-caption sheet is opened inside the
    # prefers-reduced-motion sheet and they share one close tag. That is a
    # pre-existing quirk carried in verbatim. What must hold is that the
    # merged sheet's own rules all fall inside a style element.
    head = out[:out.index("</head>")]
    assert "<style><style>" not in head, "%s: doubled <style> in head" % f_tech
    sheet_at = out.index(merged_css)
    assert sheet_at < out.index("</head>"), "%s: merged sheet is not in the head" % f_tech
    assert out[sheet_at - 7:sheet_at] == "<style>", "%s: merged sheet has no opening tag" % f_tech
    assert merged_css not in out[out.index("</head>"):], "%s: merged sheet leaked into the body" % f_tech

    # One card, union of what is not already on the page. Extracted by
    # depth: a lazy regex stops at the first "\n\t\t</div>\n", which is the
    # cta-row's close, and leaves the card's own </div> behind as a stray.
    c_m2 = re.search(r'<div class="link-card">', out)
    assert c_m2, "%s: link-card not found" % f_tech
    c_span2 = element_span(out, c_m2.start())
    assert c_span2, "%s: link-card is unclosed" % f_tech
    assert out.count('<div class="link-card">') == 1, "%s: more than one link-card" % f_tech
    out = out[:c_span2[0]] + build_linkcard(lang, LINKCARD[lang]) + out[c_span2[1]:]

    # ---- 6. scripts ----------------------------------------------------
    # html.fx-js is the master switch for the whole reveal layer: the merged
    # stylesheet's `html.fx-js .fx-rv{opacity:0}` keeps every reveal element
    # hidden until this one-liner adds the class. Both halves come from
    # system.html — the CSS via merged_css, the setter from system.html's own
    # head. Without it the hero's five reveal elements sit at opacity 0.
    fx_js = TAB + '<script>document.documentElement.className+=" fx-js";</script>' + NL
    if out.count('className+=" fx-js"') == 0:
        out = out.replace("</body>", fx_js + "</body>", 1)
    assert out.count('className+=" fx-js"') == 1, "%s: fx-js guard did not land" % f_tech

    # The #net block carries sn2Data and closes; the renderer follows it as a
    # sibling. Re-appending the JSON here would put a second 15KB blob on the
    # page, so only the renderer moves into the tail.
    tail = (NL + "<!-- project relation graph renderer: must follow its data -->" + NL
            + canvas_js + NL
            + "<!-- reveal, progress, rail, counters -->" + NL + reveal.group(0) + NL)
    out = out.replace("</body>", tail + "</body>", 1)
    sn2_id = 'id=' + Q + 'sn2Data' + Q
    reader = 'JSON.parse(document.getElementById(' + Q + 'sn2Data' + Q + ')'
    assert out.count(sn2_id) == 1, "%s: sn2Data is not unique" % f_tech
    # The renderer must come after the data or getElementById returns null,
    # the try/catch swallows it, and the canvas paints a blank white rect —
    # the exact symptom pitfalls §15 documents.
    assert out.index(sn2_id) < out.index(reader), \
        "%s: sn2Data must precede the renderer" % f_tech

    # ---- 7. assertions -------------------------------------------------
    ids = re.findall(r'\sid="([^"]+)"', strip_noise(out))
    dupes = {i for i in ids if ids.count(i) > 1}
    assert not dupes, "%s: duplicate ids %s" % (f_tech, sorted(dupes))
    assert len(re.findall(r"<h1[\s>]", out)) == 1, "%s: not exactly one h1" % f_tech
    assert out.count('<script src="../assets/js/') == 6, "%s: external script count" % f_tech
    assert "sn2Data" in out and 'class="accent"' in out, "%s: lost a load-bearing block" % f_tech
    # Assert on the rule *without* the #net prefix, so the scoped form (which
    # ends in the same text) does not satisfy it.
    assert not re.search(r"(?m)^[ \t]*\.block-inner\{ max-width: 1200px; \}", out), \
        "%s: 1200px rule is still global" % f_tech
    assert "#net .block-inner{ max-width: 1200px; }" in out, "%s: scoped rule missing" % f_tech
    assert div_balance(out) == 0, "%s: div balance %+d" % (f_tech, div_balance(out))
    for block_id in ("domains", "method", "net", "jingxin", "tech-capability"):
        assert 'id="%s"' % block_id in out, "%s: lost #%s" % (f_tech, block_id)
    assert 'class="card-grid"' in out, "%s: lost the card grid" % f_tech
    assert out.index('id="domains"') < out.index('id="method"') < out.index('id="net"') < out.index('class="card-grid"'), \
        "%s: block order is wrong" % f_tech
    assert "@keyframes storm-flow" in out, "%s: tech's storm-bg keyframe was lost" % f_tech
    assert ".punchline" in out, "%s: tech's punchline rule was lost" % f_tech

    write(f_tech, out)
    print("%-22s merged  blocks=%d  css=%d chars  id-unique OK  div-balance 0"
          % (f_tech, len(re.findall(r'class="content-block', out)), len(merged_css)))
