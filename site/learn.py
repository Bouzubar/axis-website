"""Learn: short, sourced articles (Abdullah asked for articles on 11 Oct 2026).

Copy lives in data/learn/<slug>.{en,ar}.md: a JSON meta header (title, dek, tag, minutes, short;
the English file also holds order, programs and refs) followed by markdown. Arabic pages reuse the
English references and program list. Rendered to /learn/ and /ar/learn/ by build.py.
"""
import json
import re

import markdown

L = {
    "en": {"tag": "Learn", "h": "Training, explained.",
           "p": "Short reads on the questions people ask most, written from the research and honest about its limits.",
           "min": "min read", "short": "The short answer", "uses": "Programs that use this",
           "refs": "References", "more": "Keep reading", "all": "All articles", "home": "Home",
           "programs": "Programs", "learn": "Learn",
           "cta_h": "Ready to put it into practice?", "cta_b": "Find your program",
           "note": "General information, not medical advice. If something hurts, see a doctor or physiotherapist."},
    "ar": {"tag": "تعلّم", "h": "التدريب، بشرح واضح.",
           "p": "مقالات قصيرة عن أكثر الأسئلة شيوعًا، مكتوبة من الأبحاث وصريحة بشأن حدودها.",
           "min": "دقائق قراءة", "short": "الإجابة المختصرة", "uses": "برامج تطبّق ذلك",
           "refs": "المراجع", "more": "تابع القراءة", "all": "كل المقالات", "home": "الرئيسية",
           "programs": "البرامج", "learn": "تعلّم",
           "cta_h": "جاهز لتطبيق ذلك؟", "cta_b": "اعثر على برنامجك",
           "note": "معلومات عامة وليست نصيحة طبية. إذا كان لديك ألم، راجع طبيبًا أو أخصائي علاج طبيعي."},
}


def load(root, lang):
    """All articles in one language, ordered as in the English meta."""
    d = root / "data" / "learn"
    out = []
    for f in sorted(d.glob("*.en.md")):
        slug = f.name[:-6]
        en_meta, _ = _read(f)
        src = d / f"{slug}.{lang}.md"
        if not src.exists():
            continue
        meta, body = _read(src)
        for k in ("order", "programs", "refs"):
            meta.setdefault(k, en_meta[k])
        meta["slug"] = slug
        meta["html"] = _md(body, lang)
        out.append(meta)
    return sorted(out, key=lambda a: a["order"])


def _read(f):
    raw = f.read_text()
    m = re.match(r"<!--meta\n(.*?)\nmeta-->\n", raw, re.S)
    return json.loads(m.group(1)), raw[m.end():]


def _md(body, lang):
    html = markdown.markdown(body, extensions=["sane_lists"])
    if lang == "ar":
        html = re.sub(r"(?<![\w/])(\d+(?:\.\d+)?/10)(?![\d])", r'<span dir="ltr">\1</span>', html)
    return html


def _head(t, title, desc, p):
    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#12100D">
<link rel="icon" href="{p}mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
</head>
<body class="learn">
<div class="progress" aria-hidden="true"></div>
<div class="note">{t['preview_note']}</div>
"""


def _foot(t, p, num):
    return f"""<footer>
  <img src="{p}mark.png" alt="">
  <div class="mono gold">{t['foot']}</div>
  <div class="dim small"><a href="https://instagram.com/a_bouzubar">@a_bouzubar</a> · © {num(2026)} AXIS Performance</div>
</footer>
</body>
</html>
"""


def card(a, lang, href, i=0, hx="h3"):
    s = L[lang]
    return (f'<a class="lcard rv" style="--d:{i}" href="{href}"><span class="ln" aria-hidden="true">{a["order"]:02d}</span>'
            f'<span class="k">{a["tag"]}</span><{hx}>{a["title"]}</{hx}><p>{a["dek"]}</p>'
            f'<span class="mono dim">{a["minutes"]} {s["min"]} <span class="arr">→</span></span></a>')


def index(lang, ctx, arts):
    t, s = ctx["T"][lang], L[lang]
    p = "../" + t["prefix"]
    other = "../ar/learn/" if lang == "en" else "../../learn/"
    cards = "".join(card(a, lang, f"{a['slug']}/", i, "h2") for i, a in enumerate(arts))
    return (_head(t, f"{s['tag']} · AXIS Performance", s["p"], p) + f"""<header class="nav">
  <a class="brand" href="../"><img src="{p}mark.png" alt=""><span>AXIS</span></a>
  <nav><a href="../">{s['home']}</a><a href="../programs/">{s['programs']}</a></nav>
  <a class="lang" href="{other}">{t['other_label']}</a>
</header>
<main>
  <section class="wrap l-head">
    <div class="k rv">{s['tag']}</div>
    <h1 class="rv" style="--d:1">{s['h']}</h1>
    <p class="lead rv" style="--d:2">{s['p']}</p>
  </section>
  <section class="wrap lgrid">{cards}</section>
  <section class="h-end rv"><h2>{s['cta_h']}</h2><a class="btn gold" href="../finder/">{s['cta_b']}</a></section>
</main>
""" + _foot(t, p, lambda n: ctx["num"](lang, n)))


def article(lang, ctx, a, arts):
    t, s = ctx["T"][lang], L[lang]
    p = "../../" + t["prefix"]
    other = f"../../ar/learn/{a['slug']}/" if lang == "en" else f"../../../learn/{a['slug']}/"
    progs = {x["slug"]: x for x in ctx["DATA"]["programs"]}
    chips = "".join(
        f'<a class="pchip" href="../../programs/{sl}/"><b>{progs[sl]["name"][lang]}</b><span>{ctx["price_html"](lang, progs[sl])}</span></a>'
        for sl in a["programs"])
    refs = "".join(
        f'<li><span dir="ltr">{r["cite"]}</span> <a href="https://pubmed.ncbi.nlm.nih.gov/{r["pmid"]}/" target="_blank" rel="noopener">PMID {r["pmid"]}</a>'
        f' · <a href="https://doi.org/{r["doi"]}" target="_blank" rel="noopener">DOI</a></li>'
        for r in a["refs"])
    rest = [x for x in arts if x["slug"] != a["slug"]]
    k = next(i for i, x in enumerate(arts) if x["slug"] == a["slug"])
    more = [arts[(k + j) % len(arts)] for j in (1, 2)] if len(arts) > 2 else rest
    more_html = "".join(card(x, lang, f"../{x['slug']}/", i) for i, x in enumerate(more))
    return (_head(t, f"{a['title']} · AXIS Performance", a["dek"], p) + f"""<header class="nav">
  <a class="brand" href="../../"><img src="{p}mark.png" alt=""><span>AXIS</span></a>
  <nav><a href="../../programs/">{s['programs']}</a><a href="../">{s['learn']}</a></nav>
  <a class="lang" href="{other}">{t['other_label']}</a>
</header>
<main>
  <article class="art wrap">
    <a class="crumb mono" href="../">← {s['all']}</a>
    <div class="k">{a['tag']} · {a['minutes']} {s['min']}</div>
    <h1>{a['title']}</h1>
    <p class="lead">{a['dek']}</p>
    <aside class="short rv"><div class="k">{s['short']}</div><p>{a['short']}</p></aside>
    <div class="abody">{a['html']}</div>
    <section class="uses rv"><div class="k">{s['uses']}</div><div class="pchips">{chips}</div></section>
    <section class="refs rv"><div class="k">{s['refs']}</div><ol>{refs}</ol><p class="dim small">{s['note']}</p></section>
  </article>
  <section class="wrap more"><div class="k rv">{s['more']}</div><div class="lgrid two">{more_html}</div></section>
  <section class="h-end rv"><h2>{s['cta_h']}</h2><a class="btn gold" href="../../finder/">{s['cta_b']}</a></section>
</main>
""" + _foot(t, p, lambda n: ctx["num"](lang, n)))


def write(ctx, root_site):
    for lang, base in (("en", root_site / "learn"), ("ar", root_site / "ar" / "learn")):
        arts = load(ctx["ROOT"], lang)
        base.mkdir(parents=True, exist_ok=True)
        (base / "index.html").write_text(index(lang, ctx, arts))
        for a in arts:
            d = base / a["slug"]
            d.mkdir(exist_ok=True)
            (d / "index.html").write_text(article(lang, ctx, a, arts))
