"""Three alternative homepage looks for Abdullah to compare (English only, mockups, not part of the build).
Writes designs/{a,b,c}/index.html into the preview folder given as argv[1]; image/font paths assume that layout."""
import sys, pathlib
OUT = pathlib.Path(sys.argv[1]) / "designs"
I = "../../img/"
F = "../../links/"
FONTS = f"""@font-face{{font-family:'Montserrat';src:url({F}montserrat.woff2) format('woff2');font-weight:100 900;font-display:swap}}
@font-face{{font-family:'Manrope';src:url({F}manrope.woff2) format('woff2');font-weight:200 800;font-display:swap}}
@font-face{{font-family:'JetBrains Mono';src:url({F}jetbrains.woff2) format('woff2');font-weight:100 800;font-display:swap}}
*{{box-sizing:border-box;margin:0;padding:0}}html{{-webkit-text-size-adjust:100%}}img{{display:block;max-width:100%}}a{{color:inherit}}"""
SERIES = [
    ("corrective", "Corrective", "For an area that hurts, stiffens or keeps failing. Screens five common patterns, then loads what is under-built.", "9 programs", "6 weeks", "24.990"),
    ("fundamentals", "Fundamentals", "Where most people should start. General strength and athleticism, no sport attached.", "2 programs", "12 weeks", "39.990"),
    ("performance", "Performance", "A full training year for your sport family: Base, Build, Compete and Restore.", "24 programs", "12-week blocks", "39.990"),
    ("physique", "Physique", "Muscle-building splits organised by how many days you can train, from 3 to 6.", "7 programs", "12 weeks", "44.990"),
]
LABEL = '<div class="mock">Design option {k} · mockup only</div>'
BARS = [10,12,14,16,8,14,16,18,9,16,18,10]  # illustrative weekly sets, week 5/9 lighter, 12 deload

def chart(color, dim, h=150):
    w = 12 * 26
    rects = "".join(
        f'<rect x="{i*26+4}" y="{h-v*7}" width="18" height="{v*7}" rx="2" fill="{dim if v < 11 else color}"/>'
        for i, v in enumerate(BARS))
    labels = "".join(f'<text x="{i*26+13}" y="{h+14}" text-anchor="middle">{i+1}</text>' for i in range(12))
    return f'<svg viewBox="0 0 {w} {h+20}" class="fig" role="img" aria-label="Weekly training volume across 12 weeks">{rects}<g class="ax">{labels}</g></svg>'

def guide_form(cls=""):
    return f"""<form class="gform {cls}" onsubmit="return false">
      <input type="email" placeholder="Your email" aria-label="Your email">
      <select aria-label="What do you train for?"><option>What do you train for?</option><option>Moving without pain</option><option>Getting stronger</option><option>My sport</option><option>Building muscle</option></select>
      <button type="submit">Send me the guide</button>
    </form>"""

def page(k, title, css, body):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><meta name="robots" content="noindex">
<title>{title}</title><style>{FONTS}
.mock{{position:fixed;bottom:12px;left:50%;transform:translateX(-50%);z-index:99;background:#C7AD7A;color:#0B0B0D;font:600 11px 'Manrope',sans-serif;padding:6px 12px;border-radius:99px;white-space:nowrap;box-shadow:0 4px 16px rgba(0,0,0,.25)}}
{css}</style></head><body>{LABEL.format(k=k)}{body}</body></html>"""

# ---------- A: Editorial light ----------
A_CSS = """
:root{--paper:#F4F0E8;--paper2:#ECE6DA;--ink:#141414;--ink2:#4A4740;--ink3:#7D786E;--gold:#8F743F;--line:#D8D0C0}
body{background:var(--paper);color:var(--ink);font-family:'Manrope',system-ui,sans-serif;line-height:1.6}
.w{max-width:1120px;margin:0 auto;padding:0 20px}
header{display:flex;align-items:center;justify-content:space-between;padding:18px 20px;max-width:1120px;margin:0 auto;border-bottom:1px solid var(--line)}
.logo{font:600 15px 'Montserrat';letter-spacing:.5em}
header nav{display:flex;gap:22px;font-size:14px;color:var(--ink2)}header nav a{text-decoration:none}
.k{font:500 11px 'JetBrains Mono';letter-spacing:.16em;text-transform:uppercase;color:var(--gold)}
h1{font:600 clamp(40px,7vw,84px)/1.02 'Montserrat';letter-spacing:-.03em;margin:18px 0 22px}
h1 i{font-style:normal;color:var(--gold)}
h2{font:600 clamp(28px,4vw,44px)/1.1 'Montserrat';letter-spacing:-.02em}
.hero{display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:end;padding:64px 20px 56px}
.lead{font-size:18px;color:var(--ink2);max-width:520px}
.cta{display:flex;flex-wrap:wrap;gap:18px;align-items:center;margin-top:30px}
.b{display:inline-block;background:var(--ink);color:var(--paper);text-decoration:none;font:600 15px 'Montserrat';padding:15px 24px;border-radius:2px}
.tl{font-weight:600;text-decoration:underline;text-underline-offset:4px;text-decoration-color:var(--gold)}
figure{border-top:2px solid var(--ink);padding-top:14px}
.fig{width:100%;height:auto}.fig .ax{font:9px 'JetBrains Mono';fill:var(--ink3)}
figcaption{font-size:13px;color:var(--ink3);margin-top:10px}figcaption b{color:var(--ink)}
.sec{padding:72px 20px;border-top:1px solid var(--line)}
.rows{margin-top:30px;border-top:2px solid var(--ink)}
.row{display:grid;grid-template-columns:56px 120px 1.2fr 1.6fr auto;gap:24px;align-items:center;padding:22px 0;border-bottom:1px solid var(--line);text-decoration:none}
.row .n{font:500 13px 'JetBrains Mono';color:var(--gold)}
.row img{width:120px;height:84px;object-fit:cover;object-position:70% 30%;filter:grayscale(1) contrast(1.1)}
.row:hover img{filter:none}
.row h3{font:600 22px 'Montserrat'}
.row p{color:var(--ink2);font-size:14.5px}
.row .m{font:500 11px 'JetBrains Mono';letter-spacing:.08em;text-transform:uppercase;color:var(--ink3);margin-top:4px}
.row .p{text-align:right;font-size:13px;color:var(--ink3);white-space:nowrap}.row .p b{display:block;font:600 20px 'Montserrat';color:var(--ink)}
.method{display:grid;grid-template-columns:repeat(3,1fr);gap:0;margin-top:34px;border-top:2px solid var(--ink)}
.method div{padding:22px 24px 0 0}.method div+div{padding-left:24px;border-left:1px solid var(--line)}
.method h3{font:600 20px 'Montserrat';margin:8px 0 6px}.method p{color:var(--ink2);font-size:15px}
.guide{display:grid;grid-template-columns:1fr 1fr;gap:48px;background:var(--ink);color:var(--paper);padding:48px;margin:0 20px;max-width:1080px}
@media(min-width:1120px){.guide{margin:0 auto}}
.guide .k{color:#C7AD7A}.guide p{color:#BDB6A8;margin-top:12px}
.gform{display:grid;gap:10px}
.gform input,.gform select{font:inherit;font-size:15px;padding:14px;border:1px solid #3A3833;background:#1E1D1A;color:var(--paper);border-radius:2px}
.gform button{font:600 15px 'Montserrat';padding:15px;border:0;background:#C7AD7A;color:var(--ink);border-radius:2px;cursor:pointer}
.about{display:grid;grid-template-columns:280px 1fr;gap:48px;align-items:start}
.about img{filter:grayscale(1);aspect-ratio:4/5;object-fit:cover;width:100%}
.about p{color:var(--ink2);font-size:17px;margin-top:14px;max-width:620px}
.quiet{font-size:14px;color:var(--ink3);margin-top:24px}.quiet a{color:var(--ink)}
footer{padding:48px 20px 80px;text-align:center;font:500 10px 'Montserrat';letter-spacing:.2em;color:var(--ink3);border-top:1px solid var(--line);margin-top:72px}
@media(max-width:820px){
 header nav{display:none}.hero{grid-template-columns:1fr;gap:36px;padding-top:40px}
 .row{grid-template-columns:72px 1fr auto;gap:14px;align-items:start}.row .n{display:none}.row img{width:72px;height:72px}.row p{display:none}.row .p b{font-size:16px}
 .row>div:nth-of-type(1){grid-column:2}.method{grid-template-columns:1fr}.method div+div{padding-left:0;border-left:0;border-top:1px solid var(--line);margin-top:20px}
 .guide{grid-template-columns:1fr;gap:24px;padding:32px 22px}.about{grid-template-columns:1fr;gap:24px}.about img{max-width:220px}
}"""
rowsA = "".join(f"""<a class="row" href="#"><span class="n">0{i+1}</span><img src="{I}series_{s}.jpg" alt="">
  <div><h3>{n}</h3><div class="m">{c} · {wk}</div></div><p>{d}</p><div class="p">from<b>{p} KD</b></div></a>""" for i,(s,n,d,c,wk,p) in enumerate(SERIES))
A_BODY = f"""<header><div class="logo">AXIS</div><nav><a href="#">Programs</a><a href="#">Program Finder</a><a href="#">Free guide</a><a href="#">About</a></nav></header>
<section class="hero w"><div><div class="k">Performance science</div><h1>Train on evidence,<br><i>not on trends.</i></h1>
<p class="lead">Ready-made training programs designed by an exercise scientist. Every program screens you, loads you and progresses you with written rules, so you always know what to do next.</p>
<div class="cta"><a class="b" href="#">Find your program</a><a class="tl" href="#">Browse all 42 programs</a></div></div>
<figure>{chart('#141414','#BFB5A1')}<figcaption><b>Fig. 1</b> Weekly working sets across a 12-week block. Lighter weeks are planned, not skipped.</figcaption></figure></section>
<section class="sec w"><div class="k">The library</div><h2>Four series. One system.</h2><div class="rows">{rowsA}</div></section>
<section class="sec w"><div class="k">How every program works</div><h2>Screen. Load. Progress.</h2><div class="method">
<div><div class="k">01</div><h3>Screen</h3><p>Simple tests show where you start and what to work on first.</p></div>
<div><div class="k">02</div><h3>Load</h3><p>Sets, reps and effort written for every session, sized to your level.</p></div>
<div><div class="k">03</div><h3>Progress</h3><p>Clear rules tell you when to add weight and when to hold.</p></div></div></section>
<section class="guide"><div><div class="k">Free guide</div><h2>Knee Pain Starter Guide</h2><p>A two-week plan for pain at the front of the knee. Join the AXIS list and download it straight away.</p></div>{guide_form()}</section>
<section class="sec w about" style="border:0"><img src="{I}coaching.jpg" alt=""><div><div class="k">About</div><h2>Abdullah Bouzubar</h2><div class="k" style="color:var(--ink3);margin-top:6px">Exercise Scientist</div>
<p>Abdullah builds every AXIS program from the research literature, not from trends. The same principles guide his work with individual athletes and his ready-made library.</p>
<p class="quiet">1:1 coaching is waitlist only. <a href="#">Join the waiting list</a></p></div></section>
<footer>MOVE BETTER · TRAIN SMARTER · PERFORM LONGER</footer>"""

# ---------- B: Athletic bold ----------
B_CSS = """
:root{--bk:#070708;--ink:#F2F0EC;--dim:#8E8C88;--gold:#C7AD7A;--gold2:#E2C98F}
body{background:var(--bk);color:var(--ink);font-family:'Manrope',system-ui,sans-serif;line-height:1.55}
header{position:absolute;top:0;left:0;right:0;z-index:5;display:flex;justify-content:space-between;align-items:center;padding:20px 22px}
.logo{font:700 16px 'Montserrat';letter-spacing:.5em}
.menu{font:600 12px 'Montserrat';letter-spacing:.2em;border:1px solid rgba(255,255,255,.3);padding:8px 14px;border-radius:99px}
.hero{position:relative;min-height:100svh;display:flex;align-items:flex-end;padding:0 22px 56px;overflow:hidden}
.hero img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:68% 30%}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,var(--bk) 8%,rgba(7,7,8,.35) 55%,rgba(7,7,8,.1))}
.hero>div{position:relative;z-index:2;max-width:900px}
.k{font:600 11px 'JetBrains Mono';letter-spacing:.22em;text-transform:uppercase;color:var(--gold)}
h1{font:800 clamp(52px,12vw,150px)/.88 'Montserrat';letter-spacing:-.04em;text-transform:uppercase;margin:16px 0 22px}
h1 span{color:var(--gold);display:block}
.lead{font-size:17px;color:#CFCCC6;max-width:460px}
.cta{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap}
.b{display:inline-block;text-decoration:none;font:700 14px 'Montserrat';letter-spacing:.08em;text-transform:uppercase;padding:17px 26px;background:var(--gold);color:var(--bk)}
.b.o{background:transparent;color:var(--ink);border:1px solid rgba(255,255,255,.4)}
.tick{overflow:hidden;border-block:1px solid rgba(199,173,122,.35);padding:16px 0;white-space:nowrap;font:700 22px 'Montserrat';letter-spacing:.06em;text-transform:uppercase;color:var(--dim)}
.tick span{display:inline-block;animation:m 26s linear infinite}.tick b{color:var(--gold);margin:0 18px}
@keyframes m{to{transform:translateX(-50%)}}
.band{position:relative;min-height:78svh;display:flex;align-items:flex-end;padding:0 22px 40px;overflow:hidden;border-bottom:1px solid #1a1a1a;text-decoration:none}
.band img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:70% 30%;transition:transform .8s}
.band:hover img{transform:scale(1.04)}
.band::after{content:"";position:absolute;inset:0;background:linear-gradient(to top,rgba(7,7,8,.95) 10%,rgba(7,7,8,.2) 60%,transparent)}
.band>div{position:relative;z-index:2;width:100%;max-width:1100px;display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}
.band .num{font:800 13px 'JetBrains Mono';color:var(--gold)}
.band h2{font:800 clamp(44px,9vw,110px)/.9 'Montserrat';text-transform:uppercase;letter-spacing:-.03em;margin:8px 0 12px}
.band p{max-width:420px;color:#CFCCC6}
.band .pr{text-align:right;font:600 12px 'JetBrains Mono';letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.band .pr b{display:block;font:800 34px 'Montserrat';color:var(--ink);letter-spacing:0}
.finder{background:var(--gold);color:var(--bk);padding:64px 22px}
.finder h2{font:800 clamp(36px,7vw,80px)/.95 'Montserrat';text-transform:uppercase;letter-spacing:-.03em;max-width:900px}
.finder p{max-width:520px;margin:16px 0 26px;font-size:17px}
.finder .b{background:var(--bk);color:var(--gold)}
.sec{padding:72px 22px;max-width:1140px;margin:0 auto}
.guide{display:grid;grid-template-columns:1fr 1fr;gap:40px;border:1px solid rgba(199,173,122,.4);padding:36px}
.guide h2,.about h2{font:800 clamp(30px,5vw,52px)/1 'Montserrat';text-transform:uppercase;letter-spacing:-.02em;margin:12px 0}
.guide p{color:#BDBAB3}
.gform{display:grid;gap:10px}
.gform input,.gform select{font:inherit;font-size:15px;padding:15px;border:1px solid #2A2A2A;background:#111;color:var(--ink)}
.gform button{font:700 14px 'Montserrat';letter-spacing:.08em;text-transform:uppercase;padding:17px;border:0;background:var(--gold);color:var(--bk);cursor:pointer}
.about{display:grid;grid-template-columns:1fr 1.2fr;gap:40px;align-items:center}
.about img{width:100%;aspect-ratio:4/5;object-fit:cover}
.about p{color:#BDBAB3;font-size:17px}.quiet{font-size:14px;color:var(--dim);margin-top:20px}.quiet a{color:var(--ink)}
footer{text-align:center;padding:40px 22px 90px;font:700 11px 'Montserrat';letter-spacing:.22em;color:var(--gold);border-top:1px solid #1a1a1a}
@media(max-width:760px){.guide,.about{grid-template-columns:1fr}.band .pr{text-align:left}.guide{padding:24px}}"""
bandsB = "".join(f"""<a class="band" href="#"><img src="{I}series_{s}.jpg" alt=""><div><div><div class="num">0{i+1} / 04 · {c} · {wk}</div><h2>{n}</h2><p>{d}</p></div>
<div class="pr">from<b>{p} KD</b></div></div></a>""" for i,(s,n,d,c,wk,p) in enumerate(SERIES))
B_BODY = f"""<header><div class="logo">AXIS</div><div class="menu">MENU</div></header>
<section class="hero"><img src="{I}series_performance.jpg" alt=""><div><div class="k">Performance science · Abdullah Bouzubar</div>
<h1>Built on<span>evidence.</span></h1><p class="lead">42 training programs designed by an exercise scientist. For pain, strength, sport and physique.</p>
<div class="cta"><a class="b" href="#">Find your program</a><a class="b o" href="#">Browse all</a></div></div></section>
<div class="tick"><span>{'Corrective <b>/</b> Fundamentals <b>/</b> Performance <b>/</b> Physique <b>/</b> '*6}</span></div>
{bandsB}
<section class="finder"><div class="k" style="color:var(--bk)">Program Finder</div><h2>Not sure where to start?</h2><p>Answer four quick questions about your goal, your body and your week. Get the program that fits.</p><a class="b" href="#">Start the finder</a></section>
<div class="sec"><section class="guide"><div><div class="k">Free guide</div><h2>Knee Pain Starter Guide</h2><p>A two-week plan for pain at the front of the knee. Join the AXIS list and download it now.</p></div>{guide_form()}</section></div>
<div class="sec"><section class="about"><img src="{I}coaching.jpg" alt=""><div><div class="k">Exercise Scientist</div><h2>Abdullah Bouzubar</h2>
<p>Every AXIS program is built from the research literature, not from trends. Written rules for every session, so you always know what to do next.</p>
<p class="quiet">1:1 coaching is waitlist only. <a href="#">Join the waiting list</a></p></div></section></div>
<footer>MOVE BETTER · TRAIN SMARTER · PERFORM LONGER</footer>"""

# ---------- C: Finder first ----------
C_CSS = """
:root{--bg:#12100D;--card:#1B1814;--card2:#221E19;--ink:#EEE7DA;--dim:#A39B8C;--dim2:#6F685C;--gold:#C7AD7A;--line:rgba(238,231,218,.09)}
body{background:var(--bg);color:var(--ink);font-family:'Manrope',system-ui,sans-serif;line-height:1.6}
.w{max-width:1040px;margin:0 auto;padding:0 20px}
header{display:flex;justify-content:space-between;align-items:center;padding:20px}
.logo{font:600 15px 'Montserrat';letter-spacing:.5em}.lng{font-size:13px;color:var(--dim)}
.hero{text-align:center;padding:56px 20px 40px}
.k{font:500 11px 'JetBrains Mono';letter-spacing:.18em;text-transform:uppercase;color:var(--gold)}
h1{font:600 clamp(34px,6vw,64px)/1.08 'Montserrat';letter-spacing:-.02em;margin:16px auto 14px;max-width:760px}
.sub{color:var(--dim);font-size:17px;max-width:520px;margin:0 auto}
.tiles{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;max-width:1000px;margin:36px auto 0;text-align:left}
.tile{display:flex;flex-direction:column;justify-content:space-between;gap:28px;min-height:170px;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px;text-decoration:none;transition:.2s}
.tile:hover{border-color:var(--gold);background:var(--card2);transform:translateY(-2px)}
.tile svg{width:30px;height:30px;color:var(--gold)}
.tile b{display:block;font:600 18px/1.25 'Montserrat'}.tile span{font-size:13px;color:var(--dim)}
.tile .go{font:500 11px 'JetBrains Mono';letter-spacing:.12em;color:var(--gold);text-transform:uppercase}
.note{margin-top:18px;font-size:13.5px;color:var(--dim2)}.note a{color:var(--dim)}
.sec{padding:72px 0 0}
.sec h2{font:600 clamp(26px,3.6vw,38px)/1.15 'Montserrat';letter-spacing:-.01em;margin:10px 0 6px}
.row{display:flex;justify-content:space-between;align-items:end;gap:16px}.row a{color:var(--gold);font-weight:600;font-size:14px;text-decoration:none;white-space:nowrap}
.scroll{display:grid;grid-auto-flow:column;grid-auto-columns:minmax(240px,1fr);gap:14px;overflow-x:auto;padding:24px 20px 8px;margin:0 -20px;scroll-snap-type:x mandatory}
.card{scroll-snap-align:start;background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;text-decoration:none}
.card img{aspect-ratio:4/3;object-fit:cover;object-position:70% 30%;width:100%}
.card .bd{padding:16px 18px 18px}.card h3{font:600 19px 'Montserrat'}.card p{font-size:13.5px;color:var(--dim);margin:6px 0 12px}
.card .m{display:flex;justify-content:space-between;gap:4px 10px;flex-wrap:wrap;font-size:13px;color:var(--dim2)}.card .m b{color:var(--ink);font-family:'Montserrat'}
.three{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:24px}
.three>div{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:22px}
.three .n{font:600 34px 'Montserrat';color:var(--gold)}.three h3{font:600 17px 'Montserrat';margin:6px 0 4px}.three p{font-size:14px;color:var(--dim)}
.guide{margin-top:72px;background:linear-gradient(135deg,#2A2319,#1B1814 60%);border:1px solid rgba(199,173,122,.35);border-radius:22px;padding:36px;display:grid;grid-template-columns:1fr 1fr;gap:36px;align-items:center}
.guide h2{font:600 30px/1.15 'Montserrat';margin:10px 0}.guide p{color:var(--dim)}
.gform{display:grid;gap:10px}
.gform input,.gform select{font:inherit;font-size:15px;padding:14px;border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:12px}
.gform button{font:600 15px 'Montserrat';padding:15px;border:0;background:var(--gold);color:var(--bg);border-radius:12px;cursor:pointer}
.about{display:flex;gap:22px;align-items:center;margin-top:72px;padding:24px;border-top:1px solid var(--line)}
.about img{width:84px;height:84px;border-radius:50%;object-fit:cover;object-position:40% 20%}
.about p{font-size:14.5px;color:var(--dim)}.about b{color:var(--ink);font-family:'Montserrat'}
footer{text-align:center;padding:48px 20px 90px;font:500 10px 'Montserrat';letter-spacing:.2em;color:var(--dim2)}
@media(max-width:820px){.scroll{grid-auto-columns:82%}.tiles{grid-template-columns:1fr 1fr}.tile{min-height:150px}.three,.guide{grid-template-columns:1fr}.guide{padding:24px}.about{flex-direction:column;text-align:center}}"""
ICON = {
 "pain": '<path d="M12 3v6m0 0c-3 0-5 2-5 5v7h10v-7c0-3-2-5-5-5zM9 14h6"/>',
 "str": '<path d="M3 9v6M6 7v10M18 7v10M21 9v6M6 12h12"/>',
 "sport": '<circle cx="12" cy="12" r="8"/><path d="M4.5 9.5c4 1 11 1 15 0M4.5 14.5c4-1 11-1 15 0M12 4c-2.5 3-2.5 13 0 16"/>',
 "mus": '<path d="M7 20c0-5 2-7 5-7s5 2 5 7M8 8a4 4 0 1 0 8 0 4 4 0 0 0-8 0"/>',
}
tilesC = "".join(f"""<a class="tile" href="#"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">{ICON[i]}</svg><div><b>{t}</b><span>{s}</span></div><div class="go">Start →</div></a>"""
 for i,t,s in [("pain","Pain or an old injury","Knee, back, shoulder and more"),("str","General strength","New to lifting, or already training"),("sport","My sport","Six sport families, full season"),("mus","Muscle and physique","3 to 6 days a week")])
cardsC = "".join(f"""<a class="card" href="#"><img src="{I}series_{s}.jpg" alt=""><div class="bd"><h3>{n}</h3><p>{d}</p><div class="m"><span>{c} · {wk}</span><span>from <b>{p}</b> KD</span></div></div></a>""" for s,n,d,c,wk,p in SERIES)
C_BODY = f"""<header><div class="logo">AXIS</div><div class="lng">عربي</div></header>
<section class="hero"><div class="k">Abdullah Bouzubar · Exercise Scientist</div><h1>What are you training for?</h1>
<p class="sub">Pick one and answer three more questions. You get the program that fits your goal, your body and your week.</p>
<div class="tiles">{tilesC}</div><p class="note">Already know what you want? <a href="#">Browse all 42 programs</a></p></section>
<div class="w"><section class="sec"><div class="row"><div><div class="k">The library</div><h2>Four series, built from the research.</h2></div><a href="#">See all →</a></div><div class="scroll">{cardsC}</div></section>
<section class="sec"><div class="k">Every program</div><h2>Screen. Load. Progress.</h2><div class="three">
<div><div class="n">1</div><h3>Screen</h3><p>Simple tests show where you start and what to fix first.</p></div>
<div><div class="n">2</div><h3>Load</h3><p>Sets, reps and effort written for every session.</p></div>
<div><div class="n">3</div><h3>Progress</h3><p>Clear rules for when to add weight and when to hold.</p></div></div></section>
<section class="guide"><div><div class="k">Free guide</div><h2>Knee Pain Starter Guide</h2><p>A two-week plan for pain at the front of the knee. Join the AXIS list and download it now.</p></div>{guide_form()}</section>
<section class="about"><img src="{I}coaching.jpg" alt=""><p><b>Abdullah Bouzubar</b>, Exercise Scientist. Every AXIS program comes from the research literature, not from trends. 1:1 coaching is waitlist only.</p></section></div>
<footer>MOVE BETTER · TRAIN SMARTER · PERFORM LONGER</footer>"""

for k, t, css, body in (("a", "AXIS · Option A, Editorial", A_CSS, A_BODY), ("b", "AXIS · Option B, Athletic", B_CSS, B_BODY), ("c", "AXIS · Option C, Finder first", C_CSS, C_BODY)):
    d = OUT / k
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page(k.upper(), t, css, body))
print("wrote", OUT)
