"""Search and sharing tags for every built page (run last by build.py).

One place decides the public address and whether search engines may index the site:
data/site.json "seo". While the site is a private draft, indexable stays false, so every page
keeps noindex and robots.txt blocks crawlers. At launch: set base_url to the real domain
(with a trailing slash, pointing at this site/ folder) and indexable to true, then rebuild.

Per page this writes canonical, hreflang en/ar/x-default, Open Graph and Twitter tags, the
icons, and JSON-LD (Organization/Person/WebSite/FAQ on home, Product + Offer + breadcrumbs
on programs, Article + breadcrumbs on Learn). It also makes 1200x630 share images per program
in img/og/, square icons, site.webmanifest, sitemap.xml and robots.txt.
"""
import html
import json
import re
from pathlib import Path

from PIL import Image, ImageFilter, ImageEnhance

SKIP = ("links", "guide")
INK = (18, 16, 13)
THEME = "#12100D"
BLOCK = re.compile(r"\n?<!--seo-->.*?<!--/seo-->", re.S)
OLD = [re.compile(p) for p in (
    r'\n?<meta name="robots"[^>]*>', r'\n?<meta name="theme-color"[^>]*>',
    r'\n?<link rel="icon"[^>]*>', r'\n?<link rel="alternate" hreflang[^>]*>')]


def _text(s):
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


def _jsonld(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    return f'<script type="application/ld+json">{s}</script>'


# ---------- images ----------

def _share_image(src, out, size=(1200, 630)):
    """Portrait cover on a blurred, darkened copy of itself, so link previews never crop a face."""
    if out.exists() and out.stat().st_mtime >= src.stat().st_mtime:
        return
    im = Image.open(src).convert("RGB")
    W, H = size
    bg = im.resize((W, int(im.height * W / im.width)))
    bg = bg.crop((0, (bg.height - H) // 2, W, (bg.height - H) // 2 + H))
    bg = ImageEnhance.Brightness(bg.filter(ImageFilter.GaussianBlur(28))).enhance(0.45)
    fg = im.resize((int(im.width * H / im.height), H), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, 0))
    out.parent.mkdir(parents=True, exist_ok=True)
    bg.save(out, "JPEG", quality=80, optimize=True, progressive=True)


def _icons(root):
    mark = Image.open(root / "mark.png").convert("RGBA")
    for n in (32, 180, 192, 512):
        out = root / f"icon-{n}.png"
        if out.exists() and out.stat().st_mtime >= (root / "mark.png").stat().st_mtime:
            continue
        sq = Image.new("RGBA", (n, n), INK + (255,))
        pad = round(n * 0.16)
        m = mark.copy()
        m.thumbnail((n - 2 * pad, n - 2 * pad), Image.LANCZOS)
        sq.alpha_composite(m, ((n - m.width) // 2, (n - m.height) // 2))
        sq.convert("RGB").save(out, "PNG", optimize=True)


# ---------- main pass ----------

def add_seo(root, data, look, learn_load, faq, cfg):
    base = cfg["base_url"].rstrip("/") + "/"
    index = cfg.get("indexable", False)
    brand, ig = cfg["brand"], cfg["instagram"]
    person = {"@type": "Person", "name": cfg["person"]["name"], "jobTitle": cfg["person"]["job"], "sameAs": [ig]}
    org = {"@type": "Organization", "name": brand, "url": base, "logo": base + "icon-512.png",
           "sameAs": [ig], "founder": person}
    progs = {p["slug"]: p for p in data["programs"]}
    arts = {lang: {a["slug"]: a for a in learn_load(root.parent, lang)} for lang in ("en", "ar")}

    _icons(root)
    for slug, e in look["c"].items():
        _share_image(root / "img" / e[e["d"]], root / "img" / "og" / f"{slug}.jpg")
    _share_image(root / "img" / "series_physique.jpg", root / "img" / "og" / "default.jpg")
    (root / "site.webmanifest").write_text(json.dumps({
        "name": brand, "short_name": "AXIS", "start_url": "./", "display": "standalone",
        "background_color": THEME, "theme_color": THEME,
        "icons": [{"src": f"icon-{n}.png", "sizes": f"{n}x{n}", "type": "image/png"} for n in (192, 512)]}, indent=1))

    def url(rel):
        r = str(rel).replace("\\", "/")
        return base + (r[:-len("index.html")] if r.endswith("index.html") else r)

    urls = []
    for f in sorted(root.rglob("index.html")):
        rel = f.relative_to(root)
        if rel.parts[0] in SKIP:
            continue
        s = f.read_text()
        lang = "ar" if rel.parts[0] == "ar" else "en"
        en_rel = Path(*rel.parts[1:]) if lang == "ar" else rel
        ar_rel = Path("ar", *en_rel.parts)
        pair = {"en": en_rel, "ar": ar_rel}
        alts = {k: v for k, v in pair.items() if (root / v).exists()}
        up = "../" * (len(rel.parts) - 1)
        title = _text(re.search(r"<title>(.*?)</title>", s, re.S).group(1))
        dm = re.search(r'<meta name="description" content="([^"]*)"', s)
        desc = _text(dm.group(1)) if dm else cfg["desc"][lang]
        me = url(rel)
        parts = en_rel.parts
        kind = ("home" if parts == ("index.html",) else
                "program" if parts[0] == "programs" and len(parts) == 3 else
                "article" if parts[0] == "learn" and len(parts) == 3 else "page")
        slug = parts[1] if len(parts) == 3 else None
        img = f"{base}img/og/{slug}.jpg" if kind == "program" and slug in look["c"] else f"{base}img/og/default.jpg"
        crumbs_home = {"en": "Home", "ar": "الرئيسية"}[lang]

        tags = [f'<meta name="robots" content="{"index, follow" if index else "noindex, nofollow"}">',
                f'<link rel="canonical" href="{me}">']
        tags += [f'<link rel="alternate" hreflang="{k}" href="{url(v)}">' for k, v in alts.items()]
        if "en" in alts:
            tags.append(f'<link rel="alternate" hreflang="x-default" href="{url(alts["en"])}">')
        tags += [f'<meta name="theme-color" content="{THEME}">',
                 f'<link rel="icon" type="image/png" sizes="32x32" href="{up}icon-32.png">',
                 f'<link rel="apple-touch-icon" href="{up}icon-180.png">',
                 f'<link rel="manifest" href="{up}site.webmanifest">',
                 f'<meta property="og:site_name" content="{brand}">',
                 f'<meta property="og:type" content="{"product" if kind == "program" else "article" if kind == "article" else "website"}">',
                 f'<meta property="og:title" content="{html.escape(title)}">',
                 f'<meta property="og:description" content="{html.escape(desc)}">',
                 f'<meta property="og:url" content="{me}">',
                 f'<meta property="og:image" content="{img}">',
                 '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">',
                 f'<meta property="og:locale" content="{"ar_KW" if lang == "ar" else "en_US"}">',
                 '<meta name="twitter:card" content="summary_large_image">']

        ld = []
        if kind == "home":
            ld.append({"@context": "https://schema.org", "@graph": [
                dict(org, **{"@id": base + "#org"}),
                {"@type": "WebSite", "name": brand, "url": base, "inLanguage": lang, "publisher": {"@id": base + "#org"}},
                {"@type": "FAQPage", "mainEntity": [
                    {"@type": "Question", "name": _text(q), "acceptedAnswer": {"@type": "Answer", "text": _text(a)}}
                    for q, a in faq[lang]]}]})
        elif kind == "program" and slug in progs:
            p = progs[slug]
            lib = url(Path(*rel.parts[:-2], "index.html"))
            ld.append({"@context": "https://schema.org", "@graph": [
                {"@type": "Product", "name": p["name"][lang], "description": desc, "image": img, "url": me,
                 "sku": slug, "brand": {"@type": "Brand", "name": brand},
                 "category": "Training program (PDF)" if lang == "en" else "برنامج تدريبي (PDF)",
                 "offers": {"@type": "Offer", "price": f'{p["price_kwd"]:.3f}', "priceCurrency": "KWD",
                            "availability": "https://schema.org/InStock", "url": me, "seller": person}},
                {"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": crumbs_home, "item": url(Path(*rel.parts[:-3], "index.html"))},
                    {"@type": "ListItem", "position": 2, "name": {"en": "Programs", "ar": "البرامج"}[lang], "item": lib},
                    {"@type": "ListItem", "position": 3, "name": p["name"][lang], "item": me}]}]})
        elif kind == "article" and slug in arts[lang]:
            a = arts[lang][slug]
            ld.append({"@context": "https://schema.org", "@graph": [
                {"@type": "Article", "headline": a["title"], "description": a["dek"], "inLanguage": lang,
                 "image": img, "author": person, "publisher": org, "mainEntityOfPage": me,
                 "datePublished": a.get("published", cfg["learn_published"]),
                 "dateModified": a.get("updated", a.get("published", cfg["learn_published"]))},
                {"@type": "BreadcrumbList", "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": crumbs_home, "item": url(Path(*rel.parts[:-3], "index.html"))},
                    {"@type": "ListItem", "position": 2, "name": {"en": "Learn", "ar": "تعلّم"}[lang], "item": url(Path(*rel.parts[:-2], "index.html"))},
                    {"@type": "ListItem", "position": 3, "name": a["title"], "item": me}]}]})
        tags += [_jsonld(x) for x in ld]

        s = BLOCK.sub("", s)
        for rx in OLD:
            s = rx.sub("", s)
        s = s.replace("</head>", "<!--seo-->\n" + "\n".join(tags) + "\n<!--/seo-->\n</head>", 1)
        f.write_text(s)
        urls.append((me, {k: url(v) for k, v in alts.items()}))

    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for me, alts in urls:
        sm.append(f"<url><loc>{me}</loc>" + "".join(
            f'<xhtml:link rel="alternate" hreflang="{k}" href="{v}"/>' for k, v in alts.items()) + "</url>")
    sm.append("</urlset>")
    (root / "sitemap.xml").write_text("\n".join(sm) + "\n")
    (root / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {base}sitemap.xml\n" if index else
        "# Private draft: no crawling until launch (data/site.json seo.indexable).\nUser-agent: *\nDisallow: /\n")
