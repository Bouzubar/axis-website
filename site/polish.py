"""Site-wide finishing pass on the built pages (run by build.py after add_look, before seo).

From the 15 Oct 2026 design, accessibility and performance audits:
- a "Skip to content" link and <main id="main"> on every page
- preloaded fonts (stops the layout jump when they arrive); the Arabic face is self-hosted, no Google Fonts
- one header menu on inner pages: Programs · Program Finder · Learn (the same words go to the same place)
- product tables get column labels on each cell, so phones show them as stacked rows instead of clipping
- width/height on every image (no jumps while loading); the product cover loads first
"""
import re
from pathlib import Path
from urllib.parse import quote

from PIL import Image

SKIP_TXT = {"en": "Skip to content", "ar": "تخطَّ إلى المحتوى"}
NAV = {"en": [("programs/", "Programs"), ("finder/", "Program Finder"), ("learn/", "Learn")],
       "ar": [("programs/", "البرامج"), ("finder/", "اختر برنامجك"), ("learn/", "تعلّم")]}
BRAND_LBL = {"en": "AXIS home", "ar": "الصفحة الرئيسية لأكسس"}
HOME_KEEP = ("#library",)   # the one home anchor that stays visible in the phone header
FONTS = ("montserrat.woff2", "manrope.woff2")


def _sizes(root):
    cache = {}

    def size(path):
        if path not in cache:
            try:
                cache[path] = Image.open(path).size
            except (OSError, FileNotFoundError):
                cache[path] = None
        return cache[path]
    return size


def _labels(table):
    heads = [re.sub(r"<[^>]+>", "", h).strip() for h in re.findall(r"<th[^>]*>(.*?)</th>", table, re.S)]
    if not heads:
        return table

    def row(m):
        i = [0]

        def cell(c):
            k = i[0]; i[0] += 1
            lab = heads[k] if k < len(heads) else ""
            return f'<td data-label="{lab}"' if lab else "<td"
        return re.sub(r"<td(?=[\s>])", cell, m.group(0))
    return re.sub(r"<tr>.*?</tr>", row, table, flags=re.S)


def add_polish(root):
    size = _sizes(root)
    for f in root.rglob("index.html"):
        rel = f.relative_to(root)
        if rel.parts[0] in ("links", "guide"):
            continue
        s = f.read_text()
        if 'class="skip"' in s:
            continue
        lang = "ar" if rel.parts[0] == "ar" else "en"
        up = "../" * (len(rel.parts) - 1)
        lroot = up + ("ar/" if lang == "ar" else "")
        en_parts = rel.parts[1:] if lang == "ar" else rel.parts
        is_home = en_parts == ("index.html",)
        is_lib = en_parts == ("programs", "index.html")

        # brand link keeps a name when its word is hidden on phones; the store banner sits in a landmark
        s = s.replace('<a class="brand"', f'<a class="brand" aria-label="{BRAND_LBL[lang]}"', 1)
        s = re.sub(r'<div class="note">(.*?)</div>', r'<aside class="note" aria-label="Store">\1</aside>' if lang == "en" else r'<aside class="note" aria-label="المتجر">\1</aside>', s, count=1)

        # skip link + main landmark
        s = re.sub(r"(<body[^>]*>)", rf'\1\n<a class="skip" href="#main">{SKIP_TXT[lang]}</a>', s, count=1)
        s = re.sub(r"<main(?![^>]*\bid=)", '<main id="main"', s, count=1)

        # fonts: preload the two Latin faces; the Arabic Google font only fully on Arabic pages
        pre = "".join(f'<link rel="preload" href="{up}{n}" as="font" type="font/woff2" crossorigin>' for n in FONTS)
        s = s.replace(f'<link rel="stylesheet" href="{up}style.css">', pre + f'\n<link rel="stylesheet" href="{up}style.css">', 1)
        # Arabic face is self-hosted now (plexar-*.woff2, OFL): drop the Google Fonts request everywhere
        s = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">.*?\n', "", s)
        s = re.sub(r'<link href="https://fonts\.googleapis\.com/css2[^>]*>\n?', "", s)
        if lang == "ar":
            s = s.replace(pre, pre + f'<link rel="preload" href="{up}plexar-400.woff2" as="font" type="font/woff2" crossorigin>', 1)

        # one header menu
        if is_home:
            for a in HOME_KEEP:
                s = s.replace(f'<a href="{a}">', f'<a class="keep" href="{a}">', 1)
        elif not is_lib:
            here = "/".join(en_parts[:1])
            def link(h, t):
                cls = ' class="keep"' if h == "programs/" else ""
                cur = ' aria-current="page"' if h.rstrip("/") == here and len(en_parts) == 2 else ""
                return f'<a{cls} href="{lroot}{h}"{cur}>{t}</a>'
            links = "".join(link(h, t) for h, t in NAV[lang])
            s = re.sub(r'(<header class="nav">.*?)<nav>.*?</nav>', lambda m: m.group(1) + f"<nav>{links}</nav>", s, count=1, flags=re.S)

        # product tables: per-cell column labels for the phone layout
        s = re.sub(r'<table>.*?</table>', lambda m: _labels(m.group(0)), s, flags=re.S)

        # image dimensions
        first = ['class="pp-cover"' in s]

        def dims(m):
            tag = m.group(0)
            if " width=" in tag:
                return tag
            src = re.search(r'src="([^"]+)"', tag)
            if not src or src.group(1).startswith(("http", "data:")) or "mark.png" in src.group(1):
                return tag
            wh = size((f.parent / src.group(1)).resolve())
            if not wh:
                return tag
            extra = f' width="{wh[0]}" height="{wh[1]}"'
            if first[0] and "img/covers/" in src.group(1):
                extra += ' fetchpriority="high"'
                first[0] = False
            elif "mark.png" not in src.group(1):
                extra += ' loading="lazy"' if "loading=" not in tag else ""
            return tag[:-1].rstrip("/").rstrip() + extra + ">"
        s = re.sub(r"<img\b[^>]*>", dims, s)
        f.write_text(s)
