"""Builds the bilingual AXIS homepage preview: site/index.html (English) and site/ar/index.html (Arabic, RTL).

Run: python3 site/build.py
Program counts and prices come from data/programs.json.
"""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT.parent / "data" / "programs.json").read_text())
COUNT = Counter(p["series"] for p in DATA["programs"])
PRICING = DATA["pricing"]
LAUNCH = PRICING["launch_active"]
OFFERS = {o["id"]: o for o in PRICING["offers"]}
CHEAPEST = {s: min((p for p in DATA["programs"] if p["series"] == s), key=lambda p: p["price_kwd"]) for s in COUNT}
TOTAL = len(DATA["programs"])

IG_DM = "https://ig.me/m/a_bouzubar"

T = {
    "en": {
        "dir": "ltr", "lang": "en", "other": "ar/", "other_label": "العربية", "prefix": "",
        "title": "AXIS Performance · Evidence-based training programs",
        "desc": "Ready-made training programs and 1:1 coaching built on sports science by Exercise Scientist Abdullah Bouzubar.",
        "nav": ["Programs", "How it works", "Coaching", "About"],
        "eyebrow": "Performance science",
        "h1": ["Train on evidence,", "not on trends."],
        "lead": "Ready-made programs and 1:1 coaching designed by an exercise scientist. Every program screens, loads and progresses you with written rules, so you always know what to do next.",
        "cta1": "Browse programs", "cta2": "Apply for coaching",
        "stats": [(str(TOTAL), "programs"), ("4", "series"), ("6–12", "weeks each")],
        "lib_tag": "The program library", "lib_h": "Four series. One system.",
        "lib_p": "Pick the series that matches where you are. Each program arrives as a phone edition and a print edition.",
        "series": {
            "corrective": ("Corrective", "For an area that hurts, stiffens or keeps failing. Screens five common patterns, then loads what is under-built.", "6 weeks · 3 days a week"),
            "fundamentals": ("Fundamentals", "Where most people should start. General strength and athleticism, no sport attached.", "12 weeks · 3 days a week"),
            "performance": ("Performance", "A full training year for your sport family: Base, Build, Compete and Restore.", "12-week blocks · 6 sport families"),
            "physique": ("Physique", "Muscle-building splits organised by how many days you can train, from 3 to 6.", "12 weeks · 3–6 days a week"),
        },
        "programs": "programs", "from": "From", "kd": "KD", "view": "View programs",
        "how_tag": "How it works", "how_h": "From choosing to training in minutes.",
        "steps": [
            ("Preview", "Look through sample pages of any program before you buy."),
            ("Buy", "Pay securely online in KD."),
            ("Train", "Your PDFs arrive by email straight away, sized for your phone and for print."),
        ],
        "coach_tag": "1:1 coaching", "coach_h": "A program built around you.",
        "coach_p": "For athletes and lifters who want more than a ready-made plan. You get an assessment, an individual program and weekly check-ins, all delivered through the Trainerize app.",
        "coach_list": ["Initial assessment and goal setting", "Individual program, adjusted as you progress", "Weekly check-ins and nutrition targets", "Workouts and tracking in the Trainerize app"],
        "coach_cta": "Apply on Instagram", "coach_note": "Limited spots each month.",
        "about_tag": "About", "about_h": "Abdullah Bouzubar", "about_role": "Exercise Scientist",
        "about_p": "Abdullah is an exercise and sports scientist who builds every AXIS program from the research literature, not from trends. The same principles guide his work with individual athletes and his ready-made library.",
        "principles": [("Evidence-led", "Research decides what goes in."), ("Movement first", "Quality before load."), ("Individual", "Clear rules that adapt to you."), ("Built to perform", "In the gym and in sport.")],
        "foot": "MOVE BETTER · TRAIN SMARTER · PERFORM LONGER",
        "preview_note": "Design preview. The store opens soon; for now, message on Instagram to buy a program.",
    },
    "ar": {
        "dir": "rtl", "lang": "ar", "other": "../", "other_label": "English", "prefix": "../",
        "title": "أكسس بيرفورمانس · برامج تدريب قائمة على الأدلة العلمية",
        "desc": "برامج تدريب جاهزة وتدريب شخصي مبنية على علوم الرياضة، من إعداد أخصائي علوم التمارين عبدالله بوزبر.",
        "nav": ["البرامج", "طريقة العمل", "التدريب الشخصي", "من نحن"],
        "eyebrow": "علوم الأداء",
        "h1": ["تدرّب على أساس العلم،", "لا على أساس الموضة."],
        "lead": "برامج جاهزة وتدريب شخصي من إعداد أخصائي علوم التمارين. كل برنامج يقيّمك ويحمّلك ويطوّرك وفق قواعد مكتوبة، لتعرف دائمًا خطوتك التالية.",
        "cta1": "تصفّح البرامج", "cta2": "قدّم على التدريب الشخصي",
        "stats": [(str(TOTAL), "برنامجًا"), ("٤", "سلاسل"), ("٦–١٢", "أسبوعًا لكل برنامج")],
        "lib_tag": "مكتبة البرامج", "lib_h": "أربع سلاسل. نظام واحد.",
        "lib_p": "اختر السلسلة التي تناسب مستواك. يصلك كل برنامج بنسخة للهاتف ونسخة للطباعة.",
        "series": {
            "corrective": ("التصحيحية", "لمنطقة تؤلمك أو تتيبّس أو تتكرر إصابتها. تفحص خمسة أنماط شائعة، ثم تقوّي ما هو ضعيف فعلًا.", "٦ أسابيع · ٣ أيام في الأسبوع"),
            "fundamentals": ("الأساسيات", "نقطة البداية لمعظم الناس. قوة ولياقة رياضية عامة دون ارتباط برياضة معيّنة.", "١٢ أسبوعًا · ٣ أيام في الأسبوع"),
            "performance": ("الأداء الرياضي", "سنة تدريبية كاملة لعائلة رياضتك: الأساس، البناء، المنافسة، الاستشفاء.", "مراحل من ١٢ أسبوعًا · ٦ عائلات رياضية"),
            "physique": ("بناء الجسم", "تقسيمات لبناء العضلات حسب عدد الأيام المتاحة لك، من ٣ إلى ٦ أيام.", "١٢ أسبوعًا · ٣–٦ أيام في الأسبوع"),
        },
        "programs": "برامج", "from": "ابتداءً من", "kd": "د.ك", "view": "عرض البرامج",
        "how_tag": "طريقة العمل", "how_h": "من الاختيار إلى التمرين خلال دقائق.",
        "steps": [
            ("استعرض", "تصفّح صفحات نموذجية من أي برنامج قبل الشراء."),
            ("اشترِ", "ادفع بأمان عبر الإنترنت بالدينار الكويتي."),
            ("تدرّب", "تصلك ملفات البرنامج فورًا على بريدك، بمقاس الهاتف ومقاس الطباعة."),
        ],
        "coach_tag": "التدريب الشخصي", "coach_h": "برنامج مصمَّم لك أنت.",
        "coach_p": "للرياضيين ومحبي الحديد الذين يريدون أكثر من خطة جاهزة. تحصل على تقييم وبرنامج فردي ومتابعة أسبوعية، وكلها عبر تطبيق Trainerize.",
        "coach_list": ["تقييم أوّلي وتحديد الأهداف", "برنامج فردي يتعدّل مع تقدّمك", "متابعة أسبوعية وأهداف غذائية", "التمارين والمتابعة في تطبيق Trainerize"],
        "coach_cta": "قدّم عبر إنستغرام", "coach_note": "عدد المقاعد محدود كل شهر.",
        "about_tag": "من نحن", "about_h": "عبدالله بوزبر", "about_role": "أخصائي علوم التمارين",
        "about_p": "عبدالله أخصائي في علوم التمارين والرياضة، يبني كل برنامج من برامج أكسس على الأبحاث العلمية لا على الصيحات. المبادئ نفسها توجّه عمله مع الرياضيين بشكل فردي ومكتبة برامجه الجاهزة.",
        "principles": [("قائم على الأدلة", "البحث العلمي يحدد المحتوى."), ("الحركة أولًا", "الجودة قبل الحمل."), ("فردي", "قواعد واضحة تتكيّف معك."), ("مبني للأداء", "في الصالة وفي الملعب.")],
        "foot": "تحرّك أفضل · تدرّب أذكى · أدِّ لفترة أطول",
        "preview_note": "معاينة للتصميم. المتجر يفتح قريبًا؛ حاليًا راسلنا على إنستغرام لشراء أي برنامج.",
    },
}

AR_DIGITS = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")


def count_label(lang, n, en_word, ar_few, ar_many, ar_two):
    """Number + noun with Arabic plural agreement (3-10 plural, 11+ singular accusative)."""
    if lang != "ar":
        return f"{n} {en_word}"
    if n == 2:
        return ar_two
    return f"{num(lang, n)} {ar_few if 3 <= n <= 10 else ar_many}"


def num(lang, n):
    s = str(n)
    return s.translate(AR_DIGITS) if lang == "ar" else s


def price_html(lang, x, list_key="list_price_kwd"):
    """Price with the regular price struck through while the launch price runs."""
    kd = T[lang]["kd"]
    now = f'<b>{num(lang, x["price_kwd"])}</b> {kd}'
    was = x.get(list_key)
    if LAUNCH and was and was != x["price_kwd"]:
        return f'<s>{num(lang, was)}</s> {now}'
    return now


OFF = {
    "en": {"tag": "Bundles", "h": "Bundles and coaching credit",
           "p": "Launch prices run for the first six weeks of the store, or until the first 50 programs are sold.",
           "perf_d": "All four blocks of one sport family: Base, Build, Compete and Restore. A full training year.",
           "perf_was": "160 KD bought one by one",
           "combo_d": "Fix what hurts, then build on it. Any corrective program plus any 12-week program.",
           "combo_was": "65 KD bought separately",
           "credit_h": "Upgrade to coaching", "credit_d": "Move to 1:1 coaching within 30 days and the program price comes off your first coaching month.",
           "ask": "Ask on Instagram"},
    "ar": {"tag": "الباقات", "h": "الباقات ورصيد التدريب الشخصي",
           "p": "أسعار الإطلاق سارية خلال أول ستة أسابيع من افتتاح المتجر، أو حتى بيع أول ٥٠ برنامجًا.",
           "perf_d": "المراحل الأربع لعائلة رياضية واحدة: الأساس، البناء، المنافسة، الاستشفاء. سنة تدريبية كاملة.",
           "perf_was": "١٦٠ د.ك عند الشراء منفردة",
           "combo_d": "عالج ما يؤلمك ثم ابنِ عليه. أي برنامج تصحيحي مع أي برنامج من ١٢ أسبوعًا.",
           "combo_was": "٦٥ د.ك عند الشراء منفصلة",
           "credit_h": "الترقية إلى التدريب الشخصي", "credit_d": "انتقل إلى التدريب الشخصي خلال ٣٠ يومًا ويُخصم سعر البرنامج من أول شهر تدريب.",
           "ask": "اسأل على إنستغرام"},
}


def offers_block(lang):
    o = OFF[lang]
    perf, combo = OFFERS["performance-year"], OFFERS["corrective-plus-12wk"]
    def card(off, desc, was):
        return (f'<div class="offer"><h3>{off["name"][lang]}</h3><p>{desc}</p>'
                f'<div class="price">{price_html(lang, off)}</div><p class="dim small">{was}</p>'
                f'<a class="btn ghost sm" href="{IG_DM}" target="_blank" rel="noopener">{o["ask"]}</a></div>')
    credit = f'<div class="offer"><h3>{o["credit_h"]}</h3><p>{o["credit_d"]}</p></div>'
    head = f'<div class="eyebrow">{o["tag"]}</div><h2>{o["h"]}</h2><p class="sub">{o["p"]}</p>' if LAUNCH else f'<div class="eyebrow">{o["tag"]}</div><h2>{o["h"]}</h2>'
    return (f'<section id="offers" class="wrap offers">{head}<div class="offer-grid">'
            f'{card(perf, o["perf_d"], o["perf_was"])}{card(combo, o["combo_d"], o["combo_was"])}{credit}</div></section>')


def page(lang):
    t = T[lang]
    p = t["prefix"]
    cards = "".join(
        f"""
      <article class="card">
        <div class="card-img"><img src="{p}img/series_{k}.jpg" alt="" loading="lazy"></div>
        <div class="card-body">
          <div class="card-top"><span class="mono">{count_label(lang, COUNT[k], "programs", "برامج", "برنامجًا", "برنامجان")}</span><span class="price">{t['from']} {price_html(lang, CHEAPEST[k])}</span></div>
          <h3>{name}</h3>
          <p>{blurb}</p>
          <div class="mono dim">{meta}</div>
          <a class="link" href="programs/#{k}">{t['view']} <span class="arr">→</span></a>
        </div>
      </article>"""
        for k, (name, blurb, meta) in t["series"].items()
    )
    steps = "".join(
        f'<li><span class="n">{num(lang, i + 1)}</span><h3>{h}</h3><p>{d}</p></li>'
        for i, (h, d) in enumerate(t["steps"])
    )
    stats = "".join(f"<div><b>{num(lang, a)}</b><span>{b}</span></div>" for a, b in t["stats"])
    clist = "".join(f"<li>{x}</li>" for x in t["coach_list"])
    princ = "".join(f"<div><h4>{a}</h4><p>{b}</p></div>" for a, b in t["principles"])
    nav = "".join(f'<a href="#{a}">{l}</a>' for a, l in zip(["programs", "how", "coaching", "about"], t["nav"]))
    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0B0B0D">
<link rel="icon" href="{p}mark.png">
<link rel="alternate" hreflang="{'ar' if lang == 'en' else 'en'}" href="{t['other']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
</head>
<body>
<div class="note">{t['preview_note']}</div>
<header class="nav">
  <a class="brand" href="#top"><img src="{p}mark.png" alt=""><span>AXIS</span></a>
  <nav>{nav}</nav>
  <a class="lang" href="{t['other']}">{t['other_label']}</a>
</header>
<main id="top">
  <section class="hero">
    <div class="hero-img"><img src="{p}img/series_physique.jpg" alt=""></div>
    <div class="hero-txt">
      <div class="eyebrow">{t['eyebrow']}</div>
      <h1>{t['h1'][0]}<br><em>{t['h1'][1]}</em></h1>
      <p class="lead">{t['lead']}</p>
      <div class="ctas"><a class="btn gold" href="#programs">{t['cta1']}</a><a class="btn ghost" href="{IG_DM}" target="_blank" rel="noopener">{t['cta2']}</a></div>
      <div class="stats">{stats}</div>
    </div>
  </section>

  <section id="programs" class="wrap">
    <div class="eyebrow">{t['lib_tag']}</div>
    <h2>{t['lib_h']}</h2>
    <p class="sub">{t['lib_p']}</p>
    <div class="grid">{cards}
    </div>
  </section>

  <section id="how" class="wrap">
    <div class="eyebrow">{t['how_tag']}</div>
    <h2>{t['how_h']}</h2>
    <ol class="steps">{steps}</ol>
  </section>

  <section id="coaching" class="wrap coach">
    <div class="coach-img"><img src="{p}img/coaching.jpg" alt="" loading="lazy"></div>
    <div>
      <div class="eyebrow">{t['coach_tag']}</div>
      <h2>{t['coach_h']}</h2>
      <p class="sub">{t['coach_p']}</p>
      <ul class="ticks">{clist}</ul>
      <a class="btn gold" href="{IG_DM}" target="_blank" rel="noopener">{t['coach_cta']}</a>
      <p class="mono dim small">{t['coach_note']}</p>
    </div>
  </section>

  <section id="about" class="wrap">
    <div class="eyebrow">{t['about_tag']}</div>
    <h2>{t['about_h']}</h2>
    <div class="mono gold">{t['about_role']}</div>
    <p class="sub">{t['about_p']}</p>
    <div class="princ">{princ}</div>
  </section>
</main>
<footer>
  <img src="{p}mark.png" alt="">
  <div class="mono gold">{t['foot']}</div>
  <div class="dim small"><a href="https://instagram.com/a_bouzubar">@a_bouzubar</a> · © {num(lang, 2026)} AXIS Performance</div>
</footer>
</body>
</html>
"""


LIB = {
    "en": {"title": "Program Library · AXIS Performance", "h": "The Program Library", "p": "Every program comes as a phone edition and a print edition. Prices are in Kuwaiti dinar.",
           "buy": "Buy", "back": "Home", "weeks": "weeks", "days": "days a week", "blocks": "Run the four blocks in order for a full training year.",
           "fam": {"multidirectional": "Football, basketball, handball, volleyball, rugby", "rotational": "Padel, tennis, squash, badminton, baseball", "grappling": "BJJ, wrestling, judo, sambo, MMA", "striking": "Boxing, muay thai, kickboxing, karate, taekwondo", "linear_speed": "Sprinting, American football, rugby, cricket, athletics", "endurance": "Running, cycling, triathlon, swimming, Hyrox"},
           "catalogue": "Download the full catalogue (PDF)"},
    "ar": {"title": "مكتبة البرامج · أكسس بيرفورمانس", "h": "مكتبة البرامج", "p": "يصلك كل برنامج بنسخة للهاتف ونسخة للطباعة. الأسعار بالدينار الكويتي.",
           "buy": "اشترِ", "back": "الرئيسية", "weeks": "أسبوعًا", "days": "أيام في الأسبوع", "blocks": "نفّذ المراحل الأربع بالترتيب لسنة تدريبية كاملة.",
           "fam": {"multidirectional": "كرة القدم، السلة، اليد، الطائرة، الرجبي", "rotational": "البادل، التنس، الإسكواش، الريشة، البيسبول", "grappling": "الجوجيتسو، المصارعة، الجودو، السامبو، الفنون القتالية المختلطة", "striking": "الملاكمة، المواي تاي، الكيك بوكسينغ، الكاراتيه، التايكوندو", "linear_speed": "العدو، كرة القدم الأمريكية، الرجبي، الكريكيت، ألعاب القوى", "endurance": "الجري، الدراجات، الترايثلون، السباحة، هايروكس"},
           "catalogue": "حمّل الكتالوج الكامل (PDF)"},
}


def library(lang):
    t, L = T[lang], LIB[lang]
    p = "../" + t["prefix"]
    progs = DATA["programs"]

    def row(x):
        meta = count_label(lang, x["weeks"], "weeks", "أسابيع", "أسبوعًا", "أسبوعان") + (f" · {num(lang, x['days'])} {L['days']}" if x.get("days") else "")
        return (f'<li class="prog"><div><h4><a href="{x["slug"]}/">{x["name"][lang]}</a></h4><span class="mono dim">{meta}</span></div>'
                f'<span class="price">{price_html(lang, x)}</span>'
                f'<a class="btn ghost sm" href="{IG_DM}" target="_blank" rel="noopener">{L["buy"]}</a></li>')

    secs = []
    for k, (name, blurb, meta) in t["series"].items():
        items = [x for x in progs if x["series"] == k]
        if k == "performance":
            body = ""
            for fam in dict.fromkeys(x["family"] for x in items):
                fi = [x for x in items if x["family"] == fam]
                fname = fi[0]["name"][lang].split(" · ")[0]
                body += f'<div class="fam"><h3>{fname}</h3><p class="dim">{L["fam"][fam]}</p><ul class="plist">{"".join(row(x) for x in fi)}</ul></div>'
            body = f'<p class="sub">{L["blocks"]}</p>' + body
        else:
            body = f'<ul class="plist">{"".join(row(x) for x in items)}</ul>'
        secs.append(f'<section id="{k}" class="wrap"><div class="eyebrow">{count_label(lang, len(items), "programs", "برامج", "برنامجًا", "برنامجان")}</div><h2>{name}</h2><p class="sub">{blurb}</p>{body}</section>')
    other = "../../programs/" if lang == "ar" else "../ar/programs/"
    tabs = "".join(f'<a href="#{k}">{v[0]}</a>' for k, v in t["series"].items())
    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{L['title']}</title>
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0B0B0D">
<link rel="icon" href="{p}mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
</head>
<body>
<div class="note">{t['preview_note']}</div>
<header class="nav">
  <a class="brand" href="../"><img src="{p}mark.png" alt=""><span>AXIS</span></a>
  <nav>{tabs}</nav>
  <a class="lang" href="{other}">{t['other_label']}</a>
</header>
<main>
  <section class="wrap libhead">
    <div class="eyebrow">{t['lib_tag']}</div>
    <h1>{L['h']}</h1>
    <p class="lead">{L['p']}</p>
    <div class="tabs">{tabs}</div>
  </section>
  {offers_block(lang)}
  {''.join(secs)}
  <section class="wrap"><a class="btn ghost" href="{p}../links/AXIS_Program_Library.pdf">{L['catalogue']}</a></section>
</main>
<footer>
  <img src="{p}mark.png" alt="">
  <div class="mono gold">{t['foot']}</div>
  <div class="dim small"><a href="https://instagram.com/a_bouzubar">@a_bouzubar</a> · © {num(lang, 2026)} AXIS Performance</div>
</footer>
</body>
</html>
"""


# ---------- product pages ----------
import re
import markdown

PAGES = ROOT.parent / "data" / "pages"

PT = {
    "en": {"home": "Home", "library": "Program library", "buy": "Buy", "kd": "KD",
           "weeks_lbl": "Duration", "days_lbl": "Training days", "format_lbl": "Format",
           "format": "Mobile PDF, every exercise linked to a demo video",
           "soon": "The full program guide for this page is being written. Message on Instagram with any question before you buy.",
           "ar_soon": "",
           "screen_h": "Before you buy: get cleared first if",
           "screen": ["You have chest pain, unusual breathlessness, palpitations or dizziness with exertion.",
                      "You have uncontrolled high blood pressure, a known heart condition, or recent surgery.",
                      "You are pregnant or recently post-partum. Get clearance and a tailored program first."],
           "screen_corr": "Your pain started with a specific injury (a pop, the joint giving way, or swelling within hours), or you have numbness, weakness, fever or pain that wakes you at night.",
           "screen_gen": "You have sharp joint pain in one spot that won't settle. Start with the matching AXIS corrective program.",
           "screen_foot": "This program is general fitness guidance. It does not replace a medical assessment.",
           "buy_note": "The store opens soon. For now, Buy opens an Instagram message and you receive the PDF there.",
           "launch": "Launch price",
           "deal_perf": "Get all four blocks of this sport family for 120 KD (160 bought one by one).",
           "deal_corr": "Add any 12-week program for 55 KD in total (65 bought separately).",
           "deal_12": "Pair it with any corrective program for 55 KD in total (65 bought separately).",
           "credit": "Upgrade to 1:1 coaching within 30 days and this price comes off your first month.",
           "en_link": ""},
    "ar": {"home": "الرئيسية", "library": "مكتبة البرامج", "buy": "اشترِ", "kd": "د.ك",
           "weeks_lbl": "المدة", "days_lbl": "أيام التدريب", "format_lbl": "الصيغة",
           "format": "ملف PDF للهاتف، وكل تمرين مرتبط بفيديو توضيحي",
           "soon": "دليل البرنامج الكامل لهذه الصفحة قيد الكتابة. راسلنا على إنستغرام بأي سؤال قبل الشراء.",
           "ar_soon": "التفاصيل الكاملة لهذا البرنامج متاحة حاليًا بالإنجليزية، والنسخة العربية قريبًا.",
           "screen_h": "قبل الشراء: احصل على موافقة طبية أولًا إذا",
           "screen": ["كان لديك ألم في الصدر، أو ضيق تنفس غير معتاد، أو خفقان، أو دوخة أثناء المجهود.",
                      "كان لديك ضغط دم مرتفع غير منضبط، أو مرض قلبي معروف، أو خضعت لعملية جراحية مؤخرًا.",
                      "كنتِ حاملًا أو بعد الولادة بفترة قصيرة. احصلي على موافقة وبرنامج مخصص أولًا."],
           "screen_corr": "بدأ الألم بإصابة محددة (صوت فرقعة، أو انهيار المفصل، أو تورم خلال ساعات)، أو لديك تنميل أو ضعف أو حرارة أو ألم يوقظك ليلًا.",
           "screen_gen": "كان لديك ألم حاد في مفصل واحد لا يهدأ. ابدأ ببرنامج أكسس التصحيحي المناسب.",
           "screen_foot": "هذا البرنامج إرشاد عام للياقة البدنية، ولا يغني عن التقييم الطبي.",
           "buy_note": "المتجر يفتح قريبًا. حاليًا يفتح زر الشراء رسالة على إنستغرام وتستلم الملف هناك.",
           "launch": "سعر الإطلاق",
           "deal_perf": "احصل على المراحل الأربع لهذه العائلة الرياضية بـ ١٢٠ د.ك (١٦٠ عند الشراء منفردة).",
           "deal_corr": "أضف أي برنامج من ١٢ أسبوعًا بمجموع ٥٥ د.ك (٦٥ عند الشراء منفصلة).",
           "deal_12": "أضف أي برنامج تصحيحي بمجموع ٥٥ د.ك (٦٥ عند الشراء منفصلة).",
           "credit": "انتقل إلى التدريب الشخصي خلال ٣٠ يومًا ويُخصم هذا السعر من أول شهر.",
           "en_link": "اقرأ التفاصيل الكاملة بالإنجليزية"},
}


def load_page(slug, lang):
    f = PAGES / f"{slug}.{lang}.md"
    if not f.exists():
        return None
    raw = f.read_text()
    m = re.match(r"<!--meta\n(.*?)\nmeta-->\n", raw, re.S)
    meta = json.loads(m.group(1))
    body = raw[m.end():]
    # a list straight after a paragraph line needs a blank line for markdown
    body = re.sub(r"(?m)^([^\n|#>\-\d][^\n]*)\n(?=(?:- |\d+\. ))", r"\1\n\n", body)
    html = markdown.markdown(body, extensions=["tables", "sane_lists"])
    html = re.sub(r"<h3>Terms \(expandable\)</h3>\s*(<ul>.*?</ul>)",
                  r'<details class="terms"><summary>Terms</summary>\1</details>', html, flags=re.S)
    # "What's next": link program and series names to their pages
    names = {x["name"]["en"]: f'../{x["slug"]}/' for x in DATA["programs"]}
    def link_next(m):
        sec = m.group(0)
        for n, href in names.items():
            sec = sec.replace(f"</strong> {n}</li>", f'</strong> <a class="link" href="{href}">{n}</a></li>')
        for key in ("Corrective", "Fundamentals", "Performance", "Physique"):
            sec = sec.replace(f"the {key} series", f'<a class="link" href="../#{key.lower()}">the {key} series</a>')
        return sec.replace("DM @a_bouzubar", f'<a class="link" href="{IG_DM}">DM @a_bouzubar</a>')
    html = re.sub(r"<h2>What's next</h2>.*", link_next, html, flags=re.S)
    parts = re.split(r"(?=<h2>)", html)
    out = []
    for part in parts:
        if not part.strip():
            continue
        cls = "screen" if part.startswith("<h2>Before you buy") else ""
        out.append(f'<section class="pp-sec {cls}">{part}</section>')
    return meta, "".join(out)


def screen_box(lang, series):
    t = PT[lang]
    items = t["screen"] + [t["screen_corr"] if series == "corrective" else t["screen_gen"]]
    lis = "".join(f"<li>{x}</li>" for x in items)
    return f'<section class="pp-sec screen"><h2>{t["screen_h"]}</h2><ul>{lis}</ul><p>{t["screen_foot"]}</p></section>'


def buy_block(lang, prog):
    t = PT[lang]
    tag = f'<span class="launch">{t["launch"]}</span>' if LAUNCH and prog.get("list_price_kwd", 0) > prog["price_kwd"] else ""
    if prog["series"] == "performance":
        deal = t["deal_perf"]
    elif prog["series"] == "corrective":
        deal = t["deal_corr"]
    else:
        deal = t["deal_12"]
    lib = "../#offers"
    return (f'<div class="buy">{tag}<span class="price">{price_html(lang, prog)}</span>'
            f'<a class="btn gold" href="{IG_DM}" target="_blank" rel="noopener">{t["buy"]}</a>'
            f'<ul class="deals"><li><a href="{lib}">{deal}</a></li><li>{t["credit"]}</li></ul>'
            f'<p class="dim small">{t["buy_note"]}</p></div>')


def product(lang, prog):
    t, P = T[lang], PT[lang]
    p = "../../" + t["prefix"]
    sname, sblurb, smeta = t["series"][prog["series"]]
    page = load_page(prog["slug"], lang)
    en_page = load_page(prog["slug"], "en") if lang == "ar" else None
    weeks = count_label(lang, prog["weeks"], "weeks", "أسابيع", "أسبوعًا", "أسبوعان")
    kicker = f"{sname} · {weeks}"
    if page:
        meta, body = page
        tagline = meta["tagline"]
        facts = meta["facts"]
        if not body.count('class="pp-sec screen"'):
            body += screen_box(lang, prog["series"])
    else:
        tagline = sblurb
        facts = [(P["weeks_lbl"], weeks)] + ([(P["days_lbl"], f'{num(lang, prog["days"])} {LIB[lang]["days"]}')] if prog.get("days") else []) + [(P["format_lbl"], P["format"])]
        note = P["ar_soon"] if en_page else P["soon"]
        link = f'<p><a class="link" href="../../../programs/{prog["slug"]}/">{P["en_link"]} <span class="arr">→</span></a></p>' if en_page else ""
        body = f'<section class="pp-sec"><p>{note}</p>{link}</section>' + screen_box(lang, prog["series"])
    # put the buy block straight after the clinical screen
    body = re.sub(r'(<section class="pp-sec screen">.*?</section>)', lambda m: m.group(1) + buy_block(lang, prog), body, count=1, flags=re.S)
    fl = "".join(f"<li><span>{a}</span>{b}</li>" for a, b in facts)
    other = f"../../ar/programs/{prog['slug']}/" if lang == "en" else f"../../../programs/{prog['slug']}/"
    name = prog["name"][lang]
    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{name} · AXIS Performance</title>
<meta name="description" content="{tagline}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#0B0B0D">
<link rel="icon" href="{p}mark.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
</head>
<body>
<div class="note">{t['preview_note']}</div>
<header class="nav">
  <a class="brand" href="../../"><img src="{p}mark.png" alt=""><span>AXIS</span></a>
  <nav><a href="../../">{P['home']}</a><a href="../#{prog['series']}">{P['library']}</a></nav>
  <a class="lang" href="{other}">{t['other_label']}</a>
</header>
<main>
  <section class="pp-hero wrap">
    <div class="pp-cover"><img src="{p}img/covers/{prog['slug']}.jpg" alt=""></div>
    <div>
      <a class="crumb mono" href="../#{prog['series']}">← {sname}</a>
      <div class="eyebrow">{kicker}</div>
      <h1>{name}</h1>
      <p class="lead">{tagline}</p>
      <ul class="facts">{fl}</ul>
      {buy_block(lang, prog)}
    </div>
  </section>
  <div class="pp-body">{body}</div>
</main>
<footer>
  <img src="{p}mark.png" alt="">
  <div class="mono gold">{t['foot']}</div>
  <div class="dim small"><a href="https://instagram.com/a_bouzubar">@a_bouzubar</a> · © {num(lang, 2026)} AXIS Performance</div>
</footer>
</body>
</html>
"""


def write_products():
    for prog in DATA["programs"]:
        for lang, base in (("en", ROOT / "programs"), ("ar", ROOT / "ar" / "programs")):
            d = base / prog["slug"]
            d.mkdir(parents=True, exist_ok=True)
            (d / "index.html").write_text(product(lang, prog))


(ROOT / "index.html").write_text(page("en"))
(ROOT / "programs").mkdir(exist_ok=True)
(ROOT / "programs" / "index.html").write_text(library("en"))
(ROOT / "ar" / "programs").mkdir(parents=True, exist_ok=True)
(ROOT / "ar" / "programs" / "index.html").write_text(library("ar"))
(ROOT / "ar").mkdir(exist_ok=True)
(ROOT / "ar" / "index.html").write_text(page("ar"))
print("built", TOTAL, "programs", dict(COUNT), {k: v["price_kwd"] for k, v in CHEAPEST.items()})
write_products()
