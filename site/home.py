"""AXIS homepage, "Finder first" look (Abdullah picked option C on 11 Oct 2026).

Opens on the Program Finder question, then: counters, sports marquee, the library,
how every program works (with the Foundation Strength block drawing itself), the science,
real pages from a program, the free guide, FAQ, and a short about. Motion lives in
motion.js and is switched off for people who ask their device for reduced motion.
Rendered by build.py, which passes its helpers in `ctx`.
"""
import json
from pathlib import Path

H = {
    "en": {
        "kicker": "Abdullah Bouzubar · Exercise Scientist",
        "value": "Evidence-based training programs as phone PDFs, from {kd} KD.",
        "mq_pause": "Pause", "mq_play": "Play", "phones_lbl": "Sample pages",
        "h1": "What are you |training for?", "cta": "Find your program",
        "sub": "Pick one and answer three more questions. You get the program that fits your goal, your body and your week.",
        "tiles": [
            ("pain", "Pain or an old injury", "Knee, back, shoulder and more"),
            ("general", "General strength", "New to lifting, or already training"),
            ("sport", "My sport", "Football, padel, boxing, running and more, a full season"),
            ("muscle", "Muscle and physique", "3 to 6 days a week, for men and women"),
        ],
        "go": "Start", "browse_q": "Already know what you want?", "browse": "Browse all programs",
        "stats": [("S", "series"), (4, "phases per sport"), (12, "weeks per block")],
        "sports": ["Football", "Basketball", "Handball", "Padel", "Tennis", "Squash", "BJJ", "Wrestling", "Boxing",
                   "Muay Thai", "MMA", "Sprinting", "Rugby", "Running", "Cycling", "Triathlon"],
        "lib_tag": "The library", "lib_h": "Five series, built from |the research.", "see_all": "See all",
        "from": "from",
        "m_tag": "How every program works", "m_h": "Screen. Load. |Progress.",
        "m_p": "Every program follows the same three steps, written out so you never have to guess.",
        "steps": [
            ("Screen", "Simple tests in week 1 show where you start and what to work on first. You retest later to see the change."),
            ("Load", "Sets, reps, rest and effort are written for every session, so each workout is sized to you."),
            ("Progress", "Clear rules tell you when to add weight and when to hold. Lighter weeks are planned in, not skipped."),
        ],
        "ch_h": "Foundation Strength, week by week",
        "ch_p": "Working sets per week. Weeks 6 and 12 are lighter on purpose, and effort climbs from 6 to about 8 out of 10.",
        "phases": ["Movement competence", "Muscle", "Maximal strength"],
        "wk": "Week",
        "s_tag": "The science", "s_h": "Built on published research, |with the limits stated.",
        "s_p": "Every program page lists its studies with PubMed IDs, and says what each study does not show.",
        "s_limit": "What it does not show",
        "i_tag": "Inside a program", "i_h": "What you |actually get.",
        "i_p": "Each program is a PDF made for your phone. These are real pages from Foundation Strength.",
        "pages": [("p1", "The cover"), ("p4", "Quick start"), ("p12", "A training day")],
        "feat": ["Every set, rep, rest and effort written out", "Every exercise linked to a demo video",
                 "A swap for every exercise if the equipment is taken", "Benchmark tests to retest your progress"],
        "w_line": "Also in Physique: glute-emphasis programs for women,", "w_days": ("3 days", "4 days"),
        "l_tag": "Learn", "l_h": "Training, |explained.", "l_all": "All articles",
        "f_tag": "Questions", "f_h": "Before you |start.",
        "faq": [
            ("Which program should I start with?",
             "Use the Program Finder. It takes under a minute and explains why it picked each program. If something hurts, it puts the matching corrective program first."),
            ("Do I need a gym?",
             "Most programs are written for a gym. Each program page lists the equipment before you buy, and every exercise has a listed swap."),
            ("How do I get my program?",
             "For now, you buy by sending a message on Instagram and the PDF is sent to you directly. Online checkout is coming."),
            ("Can I follow a program if something hurts?",
             "The corrective programs are for common aches and stiffness. Every program page has a short medical check. If any point applies, see a doctor or physiotherapist first."),
            ("What does an effort of 7/10 mean?",
             "It is how hard a set feels. At 7/10 you could have done about 3 more clean reps."),
            ("Do you offer 1:1 coaching?",
             'Individual coaching is limited to a few clients and is currently full. To join the waiting list, DM "WAITLIST" to @a_bouzubar.'),
        ],
        "b1_k": "The programs", "b1_h": "Strength you can see. |Fitness you can measure.",
        "b2_k": "The science", "b2_h": "Every set has |a reason.",
        "b3_k": "Learn", "b3_h": "Know why. |Then train.",
        "end_h": "Not sure yet? |Answer four questions.", "end_b": "Find your program",
        "about_tag": "About", "about_h": "Abdullah Bouzubar", "about_role": "Exercise Scientist",
        "about_p": "Abdullah builds every AXIS program from the research literature, not from trends. The same principles guide his work with individual athletes and his ready-made library.",
    },
    "ar": {
        "kicker": "عبدالله بوزبر · أخصائي علوم التمارين",
        "value": "برامج تدريبية قائمة على الأدلة العلمية بصيغة PDF للهاتف، تبدأ من {kd} د.ك.",
        "mq_pause": "إيقاف", "mq_play": "تشغيل", "phones_lbl": "صفحات من البرامج",
        "h1": "ما الذي |تتدرّب من أجله؟", "cta": "اعثر على برنامجك",
        "sub": "اختر إجابة وأجب عن ثلاثة أسئلة أخرى، لتحصل على البرنامج المناسب لهدفك وجسمك وأسبوعك.",
        "tiles": [
            ("pain", "ألم أو إصابة قديمة", "الركبة والظهر والكتف وغيرها"),
            ("general", "قوة عامة", "مبتدئ في الأوزان أو تتدرّب أصلًا"),
            ("sport", "رياضتي", "كرة القدم والبادل والملاكمة والجري وغيرها، موسم كامل"),
            ("muscle", "العضلات وشكل الجسم", "من 3 إلى 6 أيام أسبوعيًا، للرجال والنساء"),
        ],
        "go": "ابدأ", "browse_q": "تعرف ما تريد؟", "browse": "تصفّح كل البرامج",
        "stats": [("S", "سلاسل"), (4, "مراحل لكل رياضة"), (12, "أسبوعًا لكل مرحلة")],
        "sports": ["كرة القدم", "كرة السلة", "كرة اليد", "البادل", "التنس", "الاسكواش", "الجوجيتسو البرازيلي", "المصارعة",
                   "الملاكمة", "المواي تاي", "الفنون القتالية المختلطة", "العدو", "الرغبي", "الجري", "الدراجات", "الترايثلون"],
        "lib_tag": "مكتبة البرامج", "lib_h": "خمس سلاسل مبنية |على الأبحاث العلمية.", "see_all": "عرض الكل",
        "from": "ابتداءً من",
        "m_tag": "كيف يعمل كل برنامج", "m_h": "قيّم. حمّل. |تقدّم.",
        "m_p": "كل برنامج يتبع الخطوات الثلاث نفسها، مكتوبة بوضوح حتى لا تضطر إلى التخمين.",
        "steps": [
            ("التقييم", "اختبارات بسيطة في الأسبوع الأول تبيّن من أين تبدأ وما الذي تعمل عليه أولًا، ثم تعيدها لاحقًا لترى الفرق."),
            ("الحمل", "المجموعات والتكرارات والراحة والجهد مكتوبة لكل جلسة، فيكون كل تمرين على مقاسك."),
            ("التقدّم", "قواعد واضحة تخبرك متى تزيد الوزن ومتى تثبت عليه. والأسابيع الأخف مخطط لها، لا متروكة."),
        ],
        "ch_h": "القوة التأسيسية، أسبوعًا بأسبوع",
        "ch_p": "المجموعات الفعلية في كل أسبوع. الأسبوعان 6 و12 أخف عمدًا، والجهد يرتفع من 6 إلى نحو 8 من 10.",
        "phases": ["إتقان الحركة", "العضلات", "القوة القصوى"],
        "wk": "الأسبوع",
        "s_tag": "الأدلة العلمية", "s_h": "مبنية على أبحاث منشورة، |مع ذكر حدودها.",
        "s_p": "كل صفحة برنامج تذكر دراساتها مع أرقام PubMed، وتوضح ما لا تُظهره كل دراسة.",
        "s_limit": "ما لا تُظهره",
        "i_tag": "من داخل البرنامج", "i_h": "ما الذي تحصل |عليه فعلًا.",
        "i_p": "كل برنامج ملف PDF مصمَّم للهاتف. هذه صفحات حقيقية من برنامج القوة التأسيسية (بالإنجليزية).",
        "pages": [("p1", "الغلاف"), ("p4", "البداية السريعة"), ("p12", "يوم تدريب")],
        "feat": ["كل مجموعة وتكرار وراحة وجهد مكتوبة بوضوح", "كل تمرين مرتبط بفيديو توضيحي",
                 "بديل لكل تمرين إذا كانت الأداة مشغولة", "اختبارات معيارية لقياس تقدّمك"],
        "w_line": "وفي سلسلة بناء الجسم أيضًا: برامج تركيز الأرداف للنساء،", "w_days": ("3 أيام", "4 أيام"),
        "l_tag": "تعلّم", "l_h": "التدريب، |بشرح واضح.", "l_all": "كل المقالات",
        "f_tag": "أسئلة", "f_h": "قبل أن |تبدأ.",
        "faq": [
            ("بأي برنامج أبدأ؟",
             "استخدم دليل اختيار البرنامج. يستغرق أقل من دقيقة ويشرح سبب اختيار كل برنامج. وإذا كان لديك ألم، يضع البرنامج التصحيحي المناسب أولًا."),
            ("هل أحتاج إلى صالة رياضية؟",
             "معظم البرامج مكتوبة للصالة الرياضية. كل صفحة برنامج تذكر الأدوات المطلوبة قبل الشراء، ولكل تمرين بديل مذكور."),
            ("كيف أحصل على برنامجي؟",
             "حاليًا تشتري عبر رسالة على إنستغرام، ويُرسل إليك ملف البرنامج مباشرة. الدفع الإلكتروني قادم قريبًا."),
            ("هل أستطيع اتباع برنامج إذا كان لدي ألم؟",
             "البرامج التصحيحية مخصصة للآلام والتيبّس الشائعة. وفي كل صفحة برنامج فحص طبي قصير، فإذا انطبقت عليك أي نقطة، راجع طبيبًا أو أخصائي علاج طبيعي أولًا."),
            ("ماذا يعني جهد 7/10؟",
             "هو مدى صعوبة المجموعة. عند جهد 7/10 كان بإمكانك أداء نحو 3 تكرارات نظيفة إضافية."),
            ("هل تقدّم تدريبًا شخصيًا؟",
             "التدريب الشخصي محدود بعدد قليل من العملاء ومكتمل حاليًا. للانضمام إلى قائمة الانتظار، أرسل «WAITLIST» إلى @a_bouzubar."),
        ],
        "b1_k": "البرامج", "b1_h": "قوة تراها. |ولياقة تقيسها.",
        "b2_k": "العلم", "b2_h": "لكل مجموعة |سبب.",
        "b3_k": "تعلّم", "b3_h": "افهم السبب. |ثم تمرّن.",
        "end_h": "لم تحسم بعد؟ |أجب عن أربعة أسئلة.", "end_b": "اعثر على برنامجك",
        "about_tag": "من نحن", "about_h": "عبدالله بوزبر", "about_role": "أخصائي علوم التمارين",
        "about_p": "يبني عبدالله كل برنامج من برامج أكسس على الأبحاث العلمية لا على الصيحات. المبادئ نفسها توجّه عمله مع الرياضيين بشكل فردي ومكتبة برامجه الجاهزة.",
    },
}

ICON = {
    "pain": '<path d="M12 3v6m0 0c-3 0-5 2-5 5v7h10v-7c0-3-2-5-5-5zM9 14h6"/>',
    "general": '<path d="M3 9v6M6 7v10M18 7v10M21 9v6M6 12h12"/>',
    "sport": '<circle cx="12" cy="12" r="8"/><path d="M4.5 9.5c4 1 11 1 15 0M4.5 14.5c4-1 11-1 15 0M12 4c-2.5 3-2.5 13 0 16"/>',
    "muscle": '<path d="M7 20c0-5 2-7 5-7s5 2 5 7M8 8a4 4 0 1 0 8 0 4 4 0 0 0-8 0"/>',
}

# Foundation Strength, from data/product_numbers.json (key "foundation"); weeks 6 and 12 halved
# exactly as the product-page chart draws them.
def block_chart(lang, numbers):
    h = H[lang]
    x = numbers["foundation"]
    deload = set(x.get("deload_weeks") or [])
    weeks, rpe = [], []
    for p in x["phases"]:
        for i, t in enumerate(p["working_sets_by_week"]):
            w = len(weeks) + 1
            weeks.append(t / 2 if w in deload else t)
            rpe.append(p["rpe_by_week"][i])
    W, Ht, L, R, T, B = 360, 170, 8, 8, 26, 22
    n = len(weeks)
    cw = (W - L - R) / n
    top = 80
    bars = []
    for i, v in enumerate(weeks):
        bh = (Ht - T - B) * v / top
        cls = "lt" if (i + 1) in deload else ""
        bars.append(f'<rect class="bar {cls}" style="--i:{i}" x="{L + i*cw + cw*.18:.1f}" y="{Ht-B-bh:.1f}" width="{cw*.64:.1f}" height="{bh:.1f}" rx="2"/>')
    yr = lambda v: T + (Ht - T - B) * (1 - (v - 5) / 4)
    pts = " ".join(f"{L + i*cw + cw/2:.1f},{yr(v):.1f}" for i, v in enumerate(rpe))
    lab = "".join(f'<text x="{L + i*cw + cw/2:.1f}" y="{Ht-6}" text-anchor="middle">{i+1}</text>' for i in range(n))
    ph = "".join(f'<text class="ph" x="{L + (k*4+2)*cw:.1f}" y="12" text-anchor="middle">{t}</text>' for k, t in enumerate(h["phases"]))
    sep = "".join(f'<line x1="{L + k*4*cw:.1f}" x2="{L + k*4*cw:.1f}" y1="18" y2="{Ht-B}" class="sep"/>' for k in (1, 2))
    return (f'<svg viewBox="0 0 {W} {Ht}" class="h-chart" role="img" aria-label="{h["ch_h"]}" direction="ltr">'
            f'{sep}{"".join(bars)}<polyline class="rpe" points="{pts}" pathLength="1"/><g class="ax">{lab}</g><g class="phs">{ph}</g></svg>')


def science(lang, root):
    """First three rows of Foundation Strength's science table, from its EN/AR page."""
    rows = []
    for line in (root / "data" / "pages" / f"foundation-strength.{lang}.md").read_text().splitlines():
        if line.startswith("| ") and "PMID" in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            rows.append(cells)
    return rows[:3]


def acc(text):
    """Headline accent: the words after "|" are set in gold (plain, no italic)."""
    a, _, b = text.partition("|")
    return f"{a}<em>{b}</em>" if b else a


def home(lang, ctx):
    t, h = ctx["T"][lang], H[lang]
    p = t["prefix"]
    num = lambda n: str(n)
    tiles = "".join(
        f'<a class="tile rv" style="--d:{i}" href="finder/index.html?goal={g}"><span class="no" aria-hidden="true">0{i+1}</span>'
        f'<div><b>{a}</b><span>{b}</span></div><span class="arr" aria-hidden="true">→</span></a>'
        for i, (g, a, b) in enumerate(h["tiles"]))
    # one phrase of each headline in the editorial italic (Oura-style accent); "|" marks where it starts
    plain, accent = h["h1"].split("|")
    ws = [(w, False) for w in plain.split()] + [(w, True) for w in accent.split()]
    words = "".join(f'<span class="w" style="--d:{i}">' + (f"<em>{w}</em>" if a else w) + "</span> " for i, (w, a) in enumerate(ws))
    total, nser = sum(ctx["COUNT"].values()), len(ctx["COUNT"])
    h = dict(h, browse=h["browse"].format(n=total),
             stats=[({"N": total, "S": nser}.get(n, n), l) for n, l in h["stats"]])
    stats = "".join(f'<div class="rv" style="--d:{i}"><b data-count="{n}">{num(n)}</b><span>{l}</span></div>' for i, (n, l) in enumerate(h["stats"]))
    sports = "".join(f"<span>{s}</span><i>/</i>" for s in h["sports"])
    cards = "".join(
        f'<a class="card rv" style="--d:{i}" href="programs/index.html#{k}"><div class="ci"><img src="{p}img/series_{k}.jpg" alt="" loading="lazy"></div><div class="bd">'
        f'<h3>{name}</h3><p>{blurb}</p><div class="m"><span>{meta.split(" · ")[0]}</span>'
        f'<span>{h["from"]} {ctx["price_html"](lang, ctx["CHEAPEST"][k])}</span></div></div></a>'
        for i, (k, (name, blurb, meta)) in enumerate(t["series"].items()))
    steps = "".join(f'<li class="rv" style="--d:{i}"><span class="n">{i+1}</span><div><h3>{a}</h3><p>{b}</p></div></li>' for i, (a, b) in enumerate(h["steps"]))
    sci = "".join(
        f'<article class="sci rv" style="--d:{i}"><p class="fd">{f}</p><p class="src" dir="ltr">{s.replace("*", "")}</p><p class="lim"><b>{h["s_limit"]}:</b> {l}</p></article>'
        for i, (f, s, l) in enumerate(science(lang, ctx["ROOT"])))
    pages = "".join(
        f'<figure class="phone rv" style="--d:{i}"><div class="scr"><img src="{p}img/sample/{f}.jpg" alt="{c}" loading="lazy"></div><figcaption>{c}</figcaption></figure>'
        for i, (f, c) in enumerate(h["pages"]))
    feat = "".join(f"<li>{x}</li>" for x in h["feat"])
    faq = "".join(f'<details class="rv"><summary>{q}<span class="pm" aria-hidden="true"></span></summary><p>{a}</p></details>' for q, a in h["faq"])
    nav = "".join(f'<a href="#{a}">{l}</a>' for a, l in zip(["library", "method", "science", "learn", "faq"],
                  (["Programs", "How it works", "Science", "Learn", "FAQ"] if lang == "en" else ["البرامج", "طريقة العمل", "العلم", "تعلّم", "أسئلة"])))
    arts = ctx["LEARN"][lang][:3]
    progs = {x["slug"]: x for x in ctx["DATA"]["programs"]}
    wbtn = " · ".join(f'<a href="programs/{sl}/index.html">{d}</a>'
                      for sl, d in zip(("glute-emphasis-3day", "glute-emphasis-4day"), h["w_days"]))
    # full-screen photographs (img/hero/<name>.jpg wide, <name>_ph.jpg tall crop for phones)
    def bg(name, load="lazy"):
        pri = ' fetchpriority="high"' if load == "eager" else ""
        return (f'<picture class="bg" data-hero="{name}"><source media="(max-width:700px)" srcset="{p}img/hero/{name}_ph.jpg">'
                f'<img src="{p}img/hero/{name}.jpg" alt="" loading="{load}"{pri}></picture>')

    # The page is cut into segments, each with ONE photo that stays still behind it (position:fixed
    # inside a clipped layer), so a band and the sections after it share exactly the same picture.
    # The next photo comes up with its own band and fades in over the last one as you scroll.
    # No photo is used twice (Abdullah, 15 Oct).
    def seg(name, body, first=False):
        return (f'<div class="seg{" seg1" if first else ""}"><div class="seg-bg" aria-hidden="true">'
                f'{bg(name, "eager" if first else "lazy")}</div>{body}</div>')

    def band(k, line):
        return (f'<section class="band" aria-label="{k}">'
                f'<div class="band-copy rv"><div class="k">{k}</div><p class="band-h">{acc(line)}</p></div></section>')
    has_squat = (Path(__file__).parent / "img" / "hero" / "squat.jpg").exists()
    lcards = "".join(ctx["learn_card"](a, lang, f"learn/{a['slug']}/index.html", i) for i, a in enumerate(arts))
    html = f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t['title']}</title>
<meta name="description" content="{t['desc']}">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#12100D">
<link rel="icon" href="{p}mark.png">
<link rel="alternate" hreflang="{'ar' if lang == 'en' else 'en'}" href="{t['other']}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
<script>document.documentElement.classList.add('js')</script>
</head>
<body class="home">
<div class="progress" aria-hidden="true"></div>
<div class="note">{t['preview_note']}</div>
<header class="nav">
  <a class="brand" href="#hero"><img src="{p}mark.png" alt=""><span>AXIS</span></a>
  <nav>{nav}</nav>
  <a class="lang" href="{t['other']}">{t['other_label']}</a>
</header>
<main id="main">
  <!--SEG home 1--><section class="h-hero" id="hero">
    <div class="h-copy">
      <div class="k rv">{h['kicker']}</div>
      <h1 class="h-title">{words}</h1>
      <p class="value rv" style="--d:2">{h['value'].format(n=total, kd=f"{min(x['price_kwd'] for x in ctx['DATA']['programs']):.3f}")}</p>
      <div class="h-cta rv" style="--d:3"><a class="btn gold" href="finder/index.html">{h['cta']}</a><a class="link" href="programs/index.html">{h['browse']} <span class="arr">→</span></a></div>
    </div>
  </section>
  <section class="h-goals" aria-labelledby="goals-h">
    <p class="sub rv" id="goals-h">{h['sub']}</p>
    <div class="tiles">{tiles}</div>
  </section>

  <section class="h-stats wrap0">{stats}</section><!--/SEG-->
  <!--SEG physique-->{band(h['b1_k'], h['b1_h'])}

  <section id="library" class="h-sec">
    <div class="row rv"><div><div class="k">{h['lib_tag']}</div><h2>{acc(h['lib_h'])}</h2></div><a class="link" href="programs/index.html">{h['see_all']} <span class="arr">→</span></a></div>
    <div class="scroll">{cards}</div>
    <p class="h-avail rv">{h['w_line']} {wbtn}.</p>
  </section>

  <section id="method" class="h-sec h-method">
    <div class="sticky rv"><div class="k">{h['m_tag']}</div><h2>{acc(h['m_h'])}</h2><p class="lead2">{h['m_p']}</p>
      <figure class="chartcard rv">{block_chart(lang, ctx['NUMBERS'])}<figcaption><b>{h['ch_h']}</b><br>{h['ch_p']}</figcaption></figure></div>
    <ol class="steps2">{steps}</ol>
  </section><!--/SEG-->

  <!--SEG science-->{band(h['b2_k'], h['b2_h'])}

  <section id="science" class="h-sec">
    <div class="rv"><div class="k">{h['s_tag']}</div><h2>{acc(h['s_h'])}</h2><p class="lead2">{h['s_p']}</p></div>
    <div class="scis">{sci}</div>
  </section>

  <section id="inside" class="h-sec h-inside">
    <div class="rv"><div class="k">{h['i_tag']}</div><h2>{acc(h['i_h'])}</h2><p class="lead2">{h['i_p']}</p></div>
    <div class="phones" role="region" aria-label="{h['phones_lbl']}" tabindex="0">{pages}</div>
    <ul class="feat rv">{feat}</ul>
  </section>{'<!--/SEG--><!--SEG squat-->' + band(h['b3_k'], h['b3_h']) if has_squat else ''}

  <section id="learn" class="h-sec">
    <div class="row rv"><div><div class="k">{h['l_tag']}</div><h2>{acc(h['l_h'])}</h2></div><a class="link" href="learn/index.html">{h['l_all']} <span class="arr">→</span></a></div>
    <div class="lgrid three">{lcards}</div>
  </section>

  {ctx['guide_section'](lang)}

  <section id="faq" class="h-sec h-faq">
    <div class="rv"><div class="k">{h['f_tag']}</div><h2>{acc(h['f_h'])}</h2></div>
    <div class="faqs">{faq}</div>
  </section><!--/SEG-->

  <!--SEG performance--><section class="band h-end">
    <div class="band-copy rv"><h2>{acc(h['end_h'])}</h2>
    <a class="btn gold" href="finder/index.html">{h['end_b']}</a></div>
  </section>

  <section id="about" class="h-sec h-about rv">
    <img src="{p}img/coaching.jpg" alt="" loading="lazy">
    <div><div class="k">{h['about_tag']}</div><h2>{h['about_h']}</h2><div class="mono gold">{h['about_role']}</div><p>{h['about_p']}</p></div>
  </section><!--/SEG-->
</main>
<footer>
  <img src="{p}mark.png" alt="">
  <div class="mono gold">{t['foot']}</div>
  <div class="dim small"><a href="https://instagram.com/a_bouzubar">@a_bouzubar</a> · © {ctx['num'](lang, 2026)} AXIS Performance</div>
</footer>
<script src="{p}signup.js"></script>
<script src="{p}motion.js"></script>
</body>
</html>"""
    # wrap the marked runs of sections into photo segments
    import re
    return re.sub(r'<!--SEG (\w+)( 1)?-->(.*?)<!--/SEG-->',
                  lambda m: seg(m.group(1), m.group(3), bool(m.group(2))), html, flags=re.S)
