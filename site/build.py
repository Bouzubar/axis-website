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
PRICE = {s: min(p["price_kwd"] for p in DATA["programs"] if p["series"] == s) for s in COUNT}
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


def page(lang):
    t = T[lang]
    p = t["prefix"]
    cards = "".join(
        f"""
      <article class="card">
        <div class="card-img"><img src="{p}img/series_{k}.jpg" alt="" loading="lazy"></div>
        <div class="card-body">
          <div class="card-top"><span class="mono">{count_label(lang, COUNT[k], "programs", "برامج", "برنامجًا", "برنامجان")}</span><span class="price">{t['from']} <b>{num(lang, PRICE[k])}</b> {t['kd']}</span></div>
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
        return (f'<li class="prog"><div><h4>{x["name"][lang]}</h4><span class="mono dim">{meta}</span></div>'
                f'<span class="price"><b>{num(lang, x["price_kwd"])}</b> {t["kd"]}</span>'
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


(ROOT / "index.html").write_text(page("en"))
(ROOT / "programs").mkdir(exist_ok=True)
(ROOT / "programs" / "index.html").write_text(library("en"))
(ROOT / "ar" / "programs").mkdir(parents=True, exist_ok=True)
(ROOT / "ar" / "programs" / "index.html").write_text(library("ar"))
(ROOT / "ar").mkdir(exist_ok=True)
(ROOT / "ar" / "index.html").write_text(page("ar"))
print("built", TOTAL, "programs", dict(COUNT), PRICE)
