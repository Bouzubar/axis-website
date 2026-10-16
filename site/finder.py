"""AXIS Program Finder: a short questionnaire that recommends which library program to buy.

Replaces the earlier standalone finder (4 questions, English only). The logic is the same
(pain sends you to a corrective first, under a year of lifting sends you to Foundation
Strength first, season phase picks the Performance block) with extra questions for goal,
training days and focus so the result reads as tailored. Rendered by build.py.
"""
import json

Q = {
    "en": {
        "title": "Program Finder · AXIS Performance",
        "tag": "Program Finder", "h": "Find the program that fits you.",
        "p": "Answer a few questions about your goal, your body and your week. You get a recommendation and the reasons behind it. Nothing is saved or sent.",
        "start": "Start", "back": "Back", "restart": "Start again", "step": "Question", "of": "of",
        "goal": ("What do you want most from training?", [
            ("sport", "Perform better in my sport"),
            ("muscle", "Build muscle and change how I look"),
            ("general", "Get strong and athletic, no particular sport"),
            ("pain", "Get rid of pain or stiffness first"),
        ]),
        "pain": ("Is anything hurting or holding you back right now?", [
            ("none", "Nothing, I am good to train"),
            ("knee-pain", "Knee"), ("lower-back-pain", "Lower back"), ("shoulder-pain", "Shoulder or shoulder blade"),
            ("hip-groin-pain", "Hip or groin"), ("ankle-foot-pain", "Ankle or foot"), ("neck-pain", "Neck"),
            ("elbow-wrist-pain", "Elbow or wrist"),
            ("anterior-pelvic-tilt", "Arched low back that aches after long sitting or standing"),
            ("lateral-pelvic-tilt", "One hip higher than the other, or one-sided low back ache"),
            ("acl-reconstruction", "Coming back from ACL surgery (6+ months, physio done)"),
            ("shoulder-dislocation", "Coming back from a shoulder dislocation (physio done)"),
            ("hamstring-strain", "Coming back from a hamstring strain (cleared to run)"),
        ]),
        "pain_hint": "Sharp or new pain, numbness, or pain at night needs a doctor or physiotherapist before any program.",
        "sport": ("Which sport do you play?", [
            ("multidirectional", "Football, basketball or handball"),
            ("rotational", "Padel, tennis or squash"),
            ("grappling", "BJJ, wrestling, or MMA with more grappling"),
            ("striking", "Boxing, Muay Thai, or MMA with more striking"),
            ("linear_speed", "Sprinting or rugby"),
            ("endurance", "Running, cycling or triathlon"),
        ]),
        "season": ("Where are you in your season?", [
            ("base", "Off-season, months before competition"),
            ("build", "Two to three months out from the season or a big event"),
            ("compete", "In season, competing most weeks"),
            ("restore", "The season just finished"),
        ]),
        "days": ("How many days a week can you lift?", [("3", "3 days"), ("4", "4 days"), ("5", "5 days"), ("6", "6 days")]),
        "focus": ("What should the program put first?", [
            ("balanced", "The whole body, evenly"),
            ("glutes", "Glutes and legs"),
            ("split", "One body area per day (5 days only)"),
        ]),
        "exp": ("How long have you been lifting weights consistently?", [
            ("new", "Less than a year, or coming back after a long break"),
            ("mid", "One to three years"),
            ("adv", "More than three years"),
        ]),
        "result_tag": "Your recommendation", "result_h": "Here is where to start.",
        "you_said": "Based on your answers",
        "first": "Start with", "then": "Then", "view": "View program", "weeks": "weeks",
        "bundle": "Bought together, the corrective costs only 15.000 KD more:",
        "year": "Your training year", "year_p": "Run the blocks in order to cover a full year. Start with the block that matches today.",
        "ask": "Not sure? Ask on Instagram", "note": "This is a guide, not a medical assessment.",
        "why": {
            "rts": "Finish the comeback first. This program takes you from the end of physiotherapy back to full sport, and you only move on when you pass each test.",
            "corrective": "Your {area} comes first. Six weeks screens the patterns most often behind it and strengthens what is under-built, so the next program is not built on a sore spot.",
            "foundation": "With less than a year of consistent lifting, twelve weeks of technique and machine-first strength gives everything after it a base. Most people should start here.",
            "perf": "{sport} {season}: this is the block for that part of your year. It trains around your sport, not on top of it.",
            "athletic": "No sport attached, but you want to move, jump and run like an athlete as well as lift. This block trains power, speed and strength together.",
            "phys": "{days} lifting days a week{focus}. This split is built for exactly that week.",
            "phys_adv": "Six days is for experienced lifters, so with one to three years behind you the five-day version spreads the same work more safely.",
        },
        "focus_txt": {"balanced": "", "glutes": ", glutes first", "split": ", one area per day"},
        "season_txt": {"base": "in the off-season", "build": "with the season two to three months away", "compete": "in season", "restore": "with the season just finished"},
        "sport_txt": {"multidirectional": "Field and court sport", "rotational": "Racket sport", "grappling": "Grappling",
                      "striking": "Striking", "linear_speed": "Sprinting", "endurance": "Endurance sport"},
        "area_txt": {"knee-pain": "knee", "lower-back-pain": "lower back", "shoulder-pain": "shoulder", "hip-groin-pain": "hip or groin",
                     "ankle-foot-pain": "ankle or foot", "neck-pain": "neck", "elbow-wrist-pain": "elbow or wrist",
                     "anterior-pelvic-tilt": "low back and pelvis position", "lateral-pelvic-tilt": "hip and pelvis balance"},
        "block": {"base": "Base", "build": "Build", "compete": "Compete", "restore": "Restore"},
    },
    "ar": {
        "title": "دليل اختيار البرنامج · AXIS Performance",
        "tag": "دليل اختيار البرنامج", "h": "اعثر على البرنامج المناسب لك.",
        "p": "أجب عن أسئلة قليلة عن هدفك وجسمك وأسبوعك، لتحصل على توصية مع أسبابها. لا يُحفظ شيء ولا يُرسل.",
        "start": "ابدأ", "back": "رجوع", "restart": "ابدأ من جديد", "step": "السؤال", "of": "من",
        "goal": ("ما أكثر ما تريده من التمرين؟", [
            ("sport", "أداء أفضل في رياضتي"),
            ("muscle", "بناء العضلات وتغيير شكل جسمي"),
            ("general", "القوة واللياقة الرياضية دون رياضة معيّنة"),
            ("pain", "التخلّص من ألم أو تيبّس أولًا"),
        ]),
        "pain": ("هل هناك ما يؤلمك أو يعيقك الآن؟", [
            ("none", "لا شيء، أنا جاهز للتمرين"),
            ("knee-pain", "الركبة"), ("lower-back-pain", "أسفل الظهر"), ("shoulder-pain", "الكتف أو لوح الكتف"),
            ("hip-groin-pain", "الورك أو الفخذ الداخلي"), ("ankle-foot-pain", "الكاحل أو القدم"), ("neck-pain", "الرقبة"),
            ("elbow-wrist-pain", "المرفق أو الرسغ"),
            ("anterior-pelvic-tilt", "تقوّس في أسفل الظهر يؤلم بعد الجلوس أو الوقوف الطويل"),
            ("lateral-pelvic-tilt", "ورك أعلى من الآخر، أو ألم في جهة واحدة من أسفل الظهر"),
            ("acl-reconstruction", "عائد بعد جراحة الرباط الصليبي (6 أشهر أو أكثر، وانتهى العلاج الطبيعي)"),
            ("shoulder-dislocation", "عائد بعد خلع الكتف (وانتهى العلاج الطبيعي)"),
            ("hamstring-strain", "عائد بعد شدّ العضلة الخلفية للفخذ (ومسموح لك بالجري)"),
        ]),
        "pain_hint": "الألم الحاد أو الجديد أو التنميل أو الألم ليلًا يحتاج إلى طبيب أو أخصائي علاج طبيعي قبل أي برنامج.",
        "sport": ("ما رياضتك؟", [
            ("multidirectional", "كرة القدم أو السلة أو اليد"),
            ("rotational", "البادل أو التنس أو الإسكواش"),
            ("grappling", "الجوجيتسو أو المصارعة، أو MMA بطابع المصارعة"),
            ("striking", "الملاكمة أو المواي تاي، أو MMA بطابع الضرب"),
            ("linear_speed", "العدو السريع أو الرغبي"),
            ("endurance", "الجري أو الدراجات أو الترايثلون"),
        ]),
        "season": ("أين أنت من موسمك؟", [
            ("base", "خارج الموسم، قبل المنافسات بأشهر"),
            ("build", "قبل الموسم أو حدث مهم بشهرين إلى ثلاثة"),
            ("compete", "داخل الموسم، أنافس معظم الأسابيع"),
            ("restore", "انتهى الموسم للتو"),
        ]),
        "days": ("كم يومًا في الأسبوع تستطيع التمرين بالأوزان؟", [("3", "3 أيام"), ("4", "4 أيام"), ("5", "5 أيام"), ("6", "6 أيام")]),
        "focus": ("ما الذي تريد أن يركّز عليه البرنامج؟", [
            ("balanced", "الجسم كله بالتساوي"),
            ("glutes", "الأرداف والساقان"),
            ("split", "منطقة واحدة من الجسم كل يوم (5 أيام فقط)"),
        ]),
        "exp": ("منذ متى تتمرّن بالأوزان بانتظام؟", [
            ("new", "أقل من سنة، أو أعود بعد انقطاع طويل"),
            ("mid", "من سنة إلى ثلاث سنوات"),
            ("adv", "أكثر من ثلاث سنوات"),
        ]),
        "result_tag": "توصيتك", "result_h": "من هنا تبدأ.",
        "you_said": "بناءً على إجاباتك",
        "first": "ابدأ بـ", "then": "ثم", "view": "عرض البرنامج", "weeks": "أسابيع",
        "bundle": "عند شرائهما معًا، يكلّف البرنامج التصحيحي 15.000 د.ك إضافية فقط:",
        "year": "سنتك التدريبية", "year_p": "نفّذ المراحل بالترتيب لتغطي سنة كاملة، وابدأ بالمرحلة التي تناسب وقتك الآن.",
        "ask": "لست متأكدًا؟ اسأل على إنستغرام", "note": "هذا دليل إرشادي، وليس تقييمًا طبيًا.",
        "why": {
            "rts": "أكمل عودتك أولًا. هذا البرنامج ينقلك من نهاية العلاج الطبيعي إلى رياضتك كاملة، ولا تنتقل إلى المرحلة التالية إلا بعد اجتياز كل اختبار.",
            "corrective": "{area} أولًا. ستة أسابيع تفحص الأنماط التي تقف غالبًا وراء المشكلة وتقوّي ما هو ضعيف، حتى لا يُبنى البرنامج التالي على منطقة متألمة.",
            "foundation": "مع أقل من سنة من التمرين المنتظم، تمنحك اثنا عشر أسبوعًا من التقنية والقوة بالأجهزة أولًا أساسًا لكل ما بعدها. معظم الناس يبدؤون من هنا.",
            "perf": "{sport} {season}: هذه هي المرحلة المناسبة لهذا الجزء من سنتك، وهي تتدرّب حول رياضتك لا فوقها.",
            "athletic": "لا رياضة معيّنة، لكنك تريد أن تتحرك وتقفز وتجري كرياضي إلى جانب رفع الأوزان. هذه المرحلة تدرّب القدرة الانفجارية والسرعة والقوة معًا.",
            "phys": "{days} أيام تمرين في الأسبوع{focus}. هذا التقسيم مصمّم لهذا الأسبوع بالضبط.",
            "phys_adv": "ستة أيام مخصّصة لأصحاب الخبرة الطويلة، لذلك مع سنة إلى ثلاث سنوات من الخبرة توزّع نسخة الأيام الخمسة العمل نفسه بأمان أكبر.",
        },
        "focus_txt": {"balanced": "", "glutes": "، والأولوية للأرداف", "split": "، منطقة واحدة كل يوم"},
        "season_txt": {"base": "خارج الموسم", "build": "والموسم على بُعد شهرين إلى ثلاثة", "compete": "داخل الموسم", "restore": "بعد نهاية الموسم مباشرة"},
        "sport_txt": {"multidirectional": "رياضات الملاعب", "rotational": "رياضات المضرب", "grappling": "المصارعة والجوجيتسو",
                      "striking": "رياضات الضرب", "linear_speed": "العدو السريع", "endurance": "رياضات التحمّل"},
        "area_txt": {"knee-pain": "الركبة", "lower-back-pain": "أسفل الظهر", "shoulder-pain": "الكتف", "hip-groin-pain": "الورك والفخذ الداخلي",
                     "ankle-foot-pain": "الكاحل والقدم", "neck-pain": "الرقبة", "elbow-wrist-pain": "المرفق والرسغ",
                     "anterior-pelvic-tilt": "وضعية أسفل الظهر والحوض", "lateral-pelvic-tilt": "توازن الورك والحوض"},
        "block": {"base": "الأساس", "build": "البناء", "compete": "المنافسة", "restore": "الاستشفاء"},
    },
}


def finder(lang, T, DATA, kd, IG_DM, OFFERS, price_html, count_label):
    """Return the finder page HTML. Helpers come from build.py so prices and names stay in one place."""
    t, q = T[lang], Q[lang]
    p = "../" + t["prefix"]
    progs = {x["slug"]: {"name": x["name"][lang], "weeks": x["weeks"], "series": x["series"],
                         "family": x.get("family"), "block": x.get("block"),
                         "wl": count_label(lang, x["weeks"], "weeks", "أسابيع", "أسبوعًا", "أسبوعان"),
                         "price": kd(lang, x["price_kwd"]),
                         "combo": price_html(lang, {"price_kwd": x["price_kwd"] + OFFERS["corrective-plus-12wk"]["price_kwd"],
                                                    "compare_kwd": x["price_kwd"] + OFFERS["corrective-plus-12wk"]["compare_kwd"]},
                                             "compare_kwd", strike=True) if x["weeks"] == 12 else ""} for x in DATA["programs"]}
    data = {k: q[k] for k in ("goal", "pain", "sport", "season", "days", "focus", "exp", "why", "focus_txt",
                               "season_txt", "sport_txt", "area_txt", "block", "first", "then", "view", "weeks",
                               "bundle", "year", "year_p", "step", "of", "pain_hint")}
    data["progs"] = progs
    data["kd"] = t["kd"]
    data["lang"] = lang
    data["prefix"] = p
    data["base"] = "../programs/"
    other = "../../finder/" if lang == "ar" else "../ar/finder/"
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    return f"""<!doctype html>
<html lang="{t['lang']}" dir="{t['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{q['title']}</title>
<meta name="description" content="{q['p']}">
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
  <nav><a href="../programs/">{t['nav'][0]}</a></nav>
  <a class="lang" href="{other}">{t['other_label']}</a>
</header>
<main>
  <section class="wrap finder" id="finder">
    <div class="eyebrow">{q['tag']}</div>
    <h1>{q['h']}</h1>
    <p class="lead">{q['p']}</p>
    <div class="fd-box">
      <div class="fd-q" hidden>
        <div class="mono dim fd-count"></div>
        <h2 class="fd-title"></h2>
        <p class="dim small fd-hint" hidden></p>
        <div class="fd-opts"></div>
        <button class="link fd-back" type="button">{q['back']}</button>
      </div>
      <div class="fd-intro"><button class="btn gold fd-start" type="button">{q['start']}</button></div>
      <div class="fd-res" hidden>
        <div class="eyebrow">{q['result_tag']}</div>
        <h2>{q['result_h']}</h2>
        <p class="mono dim">{q['you_said']}</p>
        <ul class="fd-chips"></ul>
        <div class="fd-cards"></div>
        <div class="fd-extra"></div>
        <div class="fd-actions">
          <button class="btn ghost fd-restart" type="button">{q['restart']}</button>
          <a class="link" href="{IG_DM}" target="_blank" rel="noopener">{q['ask']} <span class="arr">→</span></a>
        </div>
        <p class="dim small">{q['note']}</p>
      </div>
    </div>
  </section>
</main>
<footer>
  <img src="{p}mark.png" alt="">
  <div class="mono gold">{t['foot']}</div>
  <div class="dim small"><a href="https://instagram.com/a_bouzubar">@a_bouzubar</a></div>
</footer>
<script id="fd-data" type="application/json">{blob}</script>
<script src="{p}finder.js"></script>
</body>
</html>
"""
