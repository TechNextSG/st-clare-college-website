# St. Clare College website - "Paper Campus" builder. Run: python build.py
import os, html, json, random, math
from data import *

V = "7"  # asset cache-buster
LIBS = [
    "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js",
    "https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js",
]
PAUSE = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M3 1h4v14H3zM9 1h4v14H9z"/></svg>'
FLAME = ('<svg class="flame" viewBox="0 0 120 170" aria-hidden="true">'
         '<path fill="#d7141a" d="M60 4C78 40 112 62 112 108c0 32-23 58-52 58S8 140 8 108C8 74 32 58 40 30c10 18 6 34 20 44C64 50 52 28 60 4z"/>'
         '<path fill="#ffd400" d="M60 52c10 22 32 38 32 66 0 22-14 38-32 38s-32-16-32-38c0-20 14-30 18-48 6 12 4 22 14 28 2-16-6-30 0-46z"/>'
         '<path fill="#ffffff" d="M60 100c6 12 16 20 16 34 0 11-7 20-16 20s-16-9-16-20c0-10 8-16 9-26 3 6 3 10 7 12 1-8-3-14 0-20z"/></svg>')
# scissor-cut filter, referenced by CSS as url(#rough)
DEFS = ('<svg class="defs" aria-hidden="true" focusable="false"><filter id="rough" x="-5%" y="-5%" width="110%" height="110%">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7" result="n"/>'
        '<feDisplacementMap in="SourceGraphic" in2="n" scale="5" xChannelSelector="R" yChannelSelector="G"/></filter></svg>')

PEEPS = [f"p{i}.svg" for i in range(1, 17)]

def esc(s): return html.escape(s, quote=True)

def edge(seed):
    """Hand-cut paper edge: a jittered wave the width of the page."""
    r = random.Random(seed)
    pts, x = [], 0
    while x <= 1440:
        pts.append((x, 14 + r.uniform(-9, 9) + 6 * math.sin(x / r.uniform(120, 220))))
        x += r.uniform(40, 90)
    pts.append((1440, 16))
    d = f"M0 46 L0 {pts[0][1]:.1f} " + " ".join(f"L{px:.0f} {py:.1f}" for px, py in pts) + " L1440 46 Z"
    return f'<svg class="edge" viewBox="0 0 1440 46" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path d="{d}"/></svg>'

_band_n = [0]
def band(cls, inner, id_=None):
    _band_n[0] += 1
    i = f' id="{id_}"' if id_ else ""
    return f'<section class="band {cls}"{i}><div class="bg"></div>{edge(_band_n[0] * 13)}<div class="wrap">{inner}</div></section>\n'

def crowd(ids):
    return '<div class="crowd" aria-hidden="true">' + "".join(f'<img class="peep" src="img/peeps/{PEEPS[i % 16]}" alt="" width="160" height="160">' for i in ids) + "</div>"

def head(title, desc):
    libs = "".join(f'\n<script src="{u}" defer></script>' for u in LIBS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#1f4fc4">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="img/campus-building.jpg">
<link rel="icon" href="img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/bricolage.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/figtree.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/paper.css?v={V}">{libs}
<script src="assets/paper.js?v={V}" defer></script>
</head>
<body>
{DEFS}
<a class="skip" href="#main">Skip to content</a>
"""

def header(page):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="bar"><div class="wrap">
  <a class="brand" href="index.html" aria-label="St. Clare College, home">
    <img src="img/seal-200.webp" alt="" width="50" height="50">
    <span><b>St. Clare College</b><span>The School of Life Skills</span></span>
  </a>
  <nav class="menu" id="menu" aria-label="Main">{links}<a class="btn" href="admissions.html">How to enroll {ARROW}</a></nav>
  <a class="btn sm b-white portal-quick" href="portals.html">Portals</a>
  <a class="btn top" href="admissions.html">How to enroll</a>
  <button class="btn sm b-ink menu-btn" aria-expanded="false" aria-controls="menu"><span>Menu</span></button>
</div></header>
<main id="main">
"""

def footer():
    portals = "".join(f'<li><a href="{SRC}/{p[3]}" rel="noopener">{p[0]}: {p[1]}</a></li>' for p in PORTALS)
    return f"""</main>
<footer class="foot on-dark"><div class="bg"></div>{edge(999)}
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="brand-f"><img src="img/seal-200.webp" alt="" width="64" height="64"><b>St. Clare<br>College</b></div>
        <p>The School of Life Skills. Serving Caloocan since 1985; online through St. Clare Online since 2020.</p>
        <div class="socials"><a href="{FB}" rel="noopener" aria-label="St. Clare College on Facebook">{FB_SVG}</a><a href="{YT}" rel="noopener" aria-label="St. Clare College on YouTube">{YT_SVG}</a></div>
      </div>
      <div><h3>Explore</h3><ul><li><a href="about.html">About St. Clare</a></li><li><a href="academics.html">Academics</a></li><li><a href="admissions.html">Admissions</a></li><li><a href="campus-life.html">Campus life</a></li><li><a href="news.html">News</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h3>St. Clare Online</h3><ul>{portals}<li><a href="{SRC}/downloadable-forms" rel="noopener">Downloadable forms</a></li></ul></div>
      <div><h3>Visit</h3><ul><li>{ADDRESS}</li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Office hours 9:00 AM - 5:00 PM</li></ul></div>
    </div>
    <div class="foot-bottom"><span>&copy; <span data-year>2026</span> St. Clare College of Caloocan &middot; St. Clare Online Education System&reg;</span><span>People illustrations: Open Peeps by Pablo Stanley (CC0)</span></div>
  </div>
</footer>
</body>
</html>
"""

def page(name, title, desc, body):
    _band_n[0] = 0
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(head(title, desc) + header(name) + body + footer())
    print("wrote", name)

def lines(*parts): return "".join(f'<span class="l">{p}</span>' for p in parts)

# ---------------------------------------------------------------- paper scenes
def sun_rays(cx, cy, r0, r1, n=14):
    out = []
    for k in range(n):
        a = 2 * math.pi * k / n
        a1, a2 = a - .1, a + .1
        out.append(f"M{cx + r0 * math.cos(a1):.0f} {cy + r0 * math.sin(a1):.0f} L{cx + r1 * math.cos(a):.0f} {cy + r1 * math.sin(a):.0f} L{cx + r0 * math.cos(a2):.0f} {cy + r0 * math.sin(a2):.0f}Z")
    return " ".join(out)

def cloud(x, y, s):
    return "".join(f'<ellipse cx="{x + dx * s:.0f}" cy="{y + dy * s:.0f}" rx="{rx * s:.0f}" ry="{ry * s:.0f}"/>' for dx, dy, rx, ry in [(0, 0, 70, 38), (55, -22, 52, 40), (110, 2, 64, 34), (40, 16, 90, 24)])

def bunting_svg(y0=70):
    cols = ["#ffd400", "#ffffff", "#d7141a", "#0b2a8f"]
    tri = []
    for k in range(26):
        x = 20 + k * 56
        y = y0 + 22 * math.sin(math.pi * x / 1440)
        tri.append(f'<path fill="{cols[k % 4]}" d="M{x} {y:.0f} L{x + 46} {y + 2:.0f} L{x + 23} {y + 46:.0f}Z"/>')
    line = f'<path d="M0 {y0} Q720 {y0 + 44} 1440 {y0}" stroke="#141414" stroke-width="3" fill="none"/>'
    return line + "".join(tri)

def hero_scene():
    windows = "".join(f'<rect x="{652 + c * 54}" y="{586 + r * 26}" width="40" height="16" rx="2" fill="#24314f"/>' for r in range(2) for c in range(12))
    slats = "".join(f'<rect x="{660 + c * 22}" y="300" width="9" height="262" fill="#9c6440"/>' for c in range(28))
    trees = ('<rect x="566" y="560" width="16" height="110" fill="#6b3e22"/><circle cx="574" cy="540" r="62" fill="#2b7a2e"/><circle cx="534" cy="575" r="44" fill="#3d9a3a"/>'
             '<rect x="1352" y="560" width="16" height="110" fill="#6b3e22"/><circle cx="1360" cy="530" r="70" fill="#3d9a3a"/><circle cx="1405" cy="575" r="48" fill="#2b7a2e"/>')
    return f"""<svg class="scene" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
  <g class="lyr" data-depth=".15"><circle cx="1180" cy="200" r="74" fill="#ffd400"/><path fill="#ffe880" d="{sun_rays(1180, 200, 92, 140)}"/></g>
  <g class="lyr" data-depth=".3" fill="#ffffff">{cloud(880, 170, .8)}{cloud(1330, 340, .7)}</g>
  <g class="lyr" data-depth=".45"><path fill="#2b7a2e" d="M0 560 C200 470 380 520 560 500 S900 440 1100 480 S1340 450 1440 470 V900 H0Z"/></g>
  <g class="lyr" data-depth=".6">
    <rect x="640" y="286" width="660" height="290" fill="#8a5232"/>{slats}
    <rect x="620" y="562" width="700" height="96" fill="#f2efe8"/>{windows}
    <rect x="700" y="318" width="160" height="116" rx="4" fill="#d7141a"/>
    <text x="780" y="384" text-anchor="middle" font-family="Bricolage, Arial" font-weight="800" font-size="52" fill="#fff">SCO</text>
    <text x="780" y="418" text-anchor="middle" font-family="Bricolage, Arial" font-weight="800" font-size="22" letter-spacing="3" fill="#fff">ONLINE</text>
    <text x="1010" y="540" text-anchor="middle" font-family="Bricolage, Arial" font-weight="800" font-size="50" fill="#f2efe8" transform="rotate(-4 1010 540)">ST. CLARE COLLEGE</text>
  </g>
  <g class="lyr" data-depth=".75">{trees}</g>
  <g class="lyr" data-depth=".85">{bunting_svg(64)}</g>
  <g class="lyr" data-depth="1"><path fill="#3d9a3a" d="M0 720 C240 650 520 700 760 670 S1200 630 1440 660 V900 H0Z"/></g>
</svg>"""

def front_grass():
    return '<svg class="front" viewBox="0 0 1440 120" preserveAspectRatio="none" aria-hidden="true" focusable="false"><path fill="#7cc46a" d="M0 60 C200 20 420 70 640 40 S1060 10 1260 44 S1400 30 1440 36 V120 H0Z" style="filter:url(#rough) drop-shadow(0 -4px 6px rgba(0,0,0,.15))"/></svg>'

def small_scene():
    return f"""<svg class="scene" viewBox="0 0 1440 600" preserveAspectRatio="xMidYMax slice" aria-hidden="true" focusable="false">
  <g class="lyr" data-depth=".2"><circle cx="1240" cy="140" r="54" fill="#ffd400"/><path fill="#ffe880" d="{sun_rays(1240, 140, 68, 104, 12)}"/></g>
  <g class="lyr" data-depth=".35" fill="#ffffff">{cloud(980, 110, .7)}{cloud(1340, 260, .55)}</g>
  <g class="lyr" data-depth=".6"><path fill="#2b7a2e" d="M0 470 C260 400 520 450 760 420 S1180 380 1440 410 V600 H0Z"/></g>
  <g class="lyr" data-depth="1"><path fill="#3d9a3a" d="M0 530 C300 480 640 520 900 500 S1300 470 1440 490 V600 H0Z"/></g>
</svg>"""

def phero(crumb, h1_parts, lede, cls="", peep_ids=(0, 1, 2, 3, 4), extra=""):
    return f"""<section class="phero {cls}">
  {small_scene()}
  <div class="wrap">
    <p class="crumbs"><a href="index.html">Home</a> / {crumb}</p>
    <h1>{lines(*h1_parts)}</h1>
    <p class="lede">{lede}</p>{extra}
  </div>
  {crowd(peep_ids)}
</section>
"""

def closer(word="Become a Clarean", line="Basic Education, Senior High School and College, on campus or fully online.", seed=0):
    return band("b-sun closer", f"""<h2>{word}</h2>
    <p class="lede">{line}</p>
    <div class="actions"><a class="btn b-ink" href="admissions.html">How to enroll {ARROW}</a><a class="btn b-red" href="contact.html">Ask admissions</a></div>
    {crowd([(seed + k) % 16 for k in range(9)])}""")

def checklist(items): return '<ul class="checklist">' + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"

def tickets():
    out = []
    for i, (h, where, items) in enumerate(STEPS):
        out.append(f"""<article class="ticket cut c-white {['tilt-l', 'tilt-r', 'tilt-l'][i]}">
  <span class="where">{where}</span><span class="no" aria-hidden="true">{i + 1}</span>
  <h3>{h}</h3><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul>
</article>""")
    out.append('<div class="after cut c-yellow tilt-r"><h3>What happens next</h3><p>Your Program Head posts your section and schedule on the website and emails them to you. Office hours are 9:00 AM to 5:00 PM; call ahead to confirm this school year\'s enrollment dates and fees.</p></div>')
    return '<div class="steps">' + "".join(out) + "</div>"

def route_inner(title="Bring the brown envelope"):
    return f"""<div class="head"><h2>{title}</h2><p class="lede">Every St. Clare enrollment starts with a long brown envelope and three stops on campus.</p></div>
    <div class="route">
      <div class="envelope">
        <div class="env" role="img" aria-label="A long brown envelope holding the enrollment documents">
          <div class="env-back"></div><div class="env-flap"></div>
          <div class="env-docs"><div class="env-doc"><b>PSA birth certificate</b>Photocopy</div><div class="env-doc"><b>Form 138</b>Report card</div><div class="env-doc"><b>2x2 photos</b>2 pcs., recent</div></div>
          <div class="env-front"><span class="hand">For: Enrollment Officer<br>St. Clare College</span></div>
        </div>
        {checklist(REQ["freshmen"][2][2:7])}
        <p class="mt"><a class="textlink" href="admissions.html#requirements">Full checklist for every level</a></p>
      </div>
      {tickets()}
    </div>"""

FLAG_COLS = ["f-sun", "f-white", "f-royal"]
def flags_html():
    items = ['<div class="flag f-white logo" style="--i:0"><img src="img/sco-online.webp" alt="SCO Online" width="512" height="512" loading="lazy"></div>']
    items += [f'<div class="flag {FLAG_COLS[i % 3]}" style="--i:{i + 1}"><b>{n}</b><small>{k}</small></div>' for i, (n, k) in enumerate(CHANNELS)]
    return f'<div class="bunting"><span class="line" aria-hidden="true"></span><div class="flags">{"".join(items)}</div></div>'

def img_tag(name, alt, w, h, lazy=True, sizes="(max-width: 900px) 100vw, 50vw"):
    base = name.rsplit(".", 1)[0]
    ss = f' srcset="img/{base}-800.webp 800w, img/{name} {w}w" sizes="{sizes}"' if os.path.exists(os.path.join(OUT, "img", base + "-800.webp")) else ""
    return f'<img src="img/{name}"{ss} alt="{esc(alt)}" width="{w}" height="{h}"{" loading=\"lazy\"" if lazy else ""}>'

def collage():
    return f"""<div class="collage">
  <div>
    <h2>Campus that feels alive</h2>
    <p class="eq" role="img" aria-label="Virtual reality plus augmented reality equals mixed reality"><span>VR</span><span class="op">+</span><span>AR</span><span class="op">=</span><span>MR</span></p>
    <p class="lede">The St. Clare Virtual Lab brings the Predator Thronos and the Mixed Reality facility by Acer into class, opened in 2021. Every one of our 95 classrooms has an e-board.</p>
    <div class="actions mt"><a class="btn b-ink" href="campus-life.html">Explore campus life {ARROW}</a></div>
  </div>
  <div class="prints">
    <figure class="print p1 cut c-white">{img_tag("campus-building.jpg", "St. Clare College building on Zabarte Road", 1600, 900)}<figcaption>Our campus, Zabarte Road</figcaption></figure>
    <figure class="print p2 cut c-white"><span class="tape" aria-hidden="true"></span>{img_tag("virtual-lab-predator.jpg", "Predator stations in the St. Clare Virtual Lab", 1600, 1066)}<figcaption>Inside the Virtual Lab</figcaption></figure>
    <div class="label l1 cut c-sun"><b>95</b>classrooms with e-boards</div>
    <div class="label l2 cut c-red"><b>1985</b>serving Caloocan since</div>
  </div>
</div>"""

FLAME_INNER = f"""{FLAME}
    <h2>The eternal flame of professionalism</h2>
    <blockquote>&ldquo;A beacon of professionalism and culture of excellence.&rdquo;</blockquote>
    <cite>St. Clare College Professional Mace &middot; 23 September 2023</cite>"""

VM = """<div class="vm">
  <div class="cut c-royal tilt-l" data-pop style="--rest:-1.2deg"><h3>Vision</h3><p>To become the leading institution for professional development and the first and foremost provider of quality, affordable and sustainable development education.</p></div>
  <div class="cut c-white tilt-r" data-pop style="--rest:1deg"><h3 class="red">Mission</h3><p>To provide quality and excellent global education for the total development of a responsible, innovative, skillful and professional global workforce whose values and dignity are beyond par.</p></div>
</div>"""

def level_rows(level):
    if level == "college":
        return "".join(f'<li><span class="c">{c}</span><span class="n">{n}<small>{s}</small></span></li>' for c, n, _, s, *_ in TERTIARY)
    if level == "shs":
        return "".join(f'<li><span class="c">{k}</span><span class="n">{n}<small>{t}{(": " + ", ".join(sp)) if sp else ""}</small></span></li>' for k, n, t, _, sp in SHS)
    return "".join(f'<li><span class="c">{k}</span><span class="n">{n}<small>{d}</small></span></li>' for k, n, d in BASIC)

def picker():
    lv = [("college", "College", "Eight degree programmes"), ("shs", "Senior High", "Five tracks"), ("basic", "Basic Ed", "Nursery to Grade 10")]
    tabs = "".join(f'<button role="tab" id="lt-{k}" aria-controls="lp-{k}" aria-selected="{"true" if k == "college" else "false"}"{"" if k == "college" else " tabindex=\"-1\""} data-v="{k}"><b>{n}</b><small>{s}</small></button>' for k, n, s in lv)
    figs = {
        "college": "".join(f'<img class="peep" src="img/peeps/{PEEPS[i]}" alt="" width="160" height="160">' for i in (1, 2, 5)),
        "shs": "".join(f'<img class="peep" src="img/peeps/{PEEPS[i]}" alt="" width="160" height="160">' for i in (3, 8, 12)),
        "basic": '<img src="img/cut-girl.webp" alt="Girl in the St. Clare Basic Education uniform" width="254" height="786" loading="lazy"><img src="img/cut-boy.webp" alt="Boy in the St. Clare Basic Education uniform" width="260" height="767" loading="lazy">',
    }
    reqkey = {"basic": "basic", "shs": "shs", "college": "freshmen"}
    panels = "".join(f"""<div class="deal" role="tabpanel" id="lp-{k}" aria-labelledby="lt-{k}"{"" if k == "college" else " hidden"}>
  <div class="deal-grid">
    <ul class="rows">{level_rows(k)}</ul>
    <aside><div class="deal-figs">{figs[k]}</div>
      <div class="actions mt"><a class="btn" href="admissions.html#{reqkey[k]}">What to bring {ARROW}</a><a class="textlink" href="academics.html#{k if k != 'college' else 'tertiary'}">Programme details</a></div></aside>
  </div>
</div>""" for k, *_ in lv)
    return f'<div class="picker" role="tablist" aria-label="Choose a school level">{tabs}</div>{panels}'

def ribbon():
    words = ["BSCS Computer Science", "BSHM Hospitality", "BSTM Tourism", "BSBA Business Administration", "BEEd Elementary Education", "BSEd English", "BSEd Math", "AB Political Science",
             "SHS ABM", "SHS HUMSS", "SHS Arts & Design", "SHS TVL-ICT", "SHS TVL-HE", "Nursery to Grade 10"]
    t = "".join(f"<span>{esc(w)}</span>" for w in words)
    t2 = "".join(f'<span aria-hidden="true">{esc(w)}</span>' for w in words)
    return f'<div class="ribbon" role="region" aria-label="Programmes offered"><div class="strip"><div class="track-wrap"><div class="track">{t}{t2}</div></div><button class="pause" type="button" aria-label="Pause the programme ribbon">{PAUSE}</button></div></div>'

# ---------------------------------------------------------------- pages
def build_home():
    body = f"""<section class="hero">
  {hero_scene()}
  <div class="wrap hero-copy">
    <h1>{lines("The school", "<span class='sun'>of life skills</span>")}</h1>
    <p class="lede">St. Clare College of Caloocan. Nursery to College on one campus, and the leading edge in online education.</p>
    <div class="actions"><a class="btn" href="admissions.html">How to enroll {ARROW}</a><a class="btn b-white" href="#levels">Find your level</a></div>
  </div>
  <img class="hero-seal" src="img/seal-400.webp" alt="St. Clare College of Caloocan seal" width="392" height="396">
  {crowd([0, 1, 2, 3, 4, 5, 6, 7])}
  {front_grass()}
</section>
{ribbon()}
""" + band("b-chalk", f"""<div class="head"><h2>Pick your level</h2><p class="lede">From a child's first school day to a college degree, everything happens under one St. Clare roof.</p></div>
    {picker()}""", "levels") + band("b-white", route_inner(), "steps") + band("b-kraft", collage()) + band("b-red on-dark", f"""<div class="head"><h2>Tune in to SCO Online</h2><p class="lede">St. Clare runs its own channels: wellness, sport, leadership, innovation and Clarean stories, plus a virtual flag ceremony every Monday at 7:00 AM.</p></div>
    {flags_html()}""") + band("b-chalk", f"""<div class="congrats cut lg c-royal" data-pop style="--rest:-.6deg">
      <div class="inner">
        <div class="ph">{img_tag("graduates.jpg", "St. Clare College graduates applauding at commencement", 1230, 640, sizes="(max-width: 900px) 100vw, 60vw")}</div>
        <div class="txt"><h2><span class="sun">Congratulations,</span> Stars of 2024!</h2><p>St. Clare College held its 38th Commencement Exercises in June 2024.</p></div>
      </div>
    </div>""") + band("b-ink on-dark mace", FLAME_INNER) + closer()
    page("index.html", "St. Clare College of Caloocan | The School of Life Skills",
         "St. Clare College of Caloocan: Nursery to College, full online or blended. BSCS, BSHM, BSTM, BSBA, BEEd, BSEd, AB Political Science and Senior High tracks.", body)


def build_about():
    tl = [
        ("1985", "St. Clare College is founded", "Founded on 31 August 1985 in Caloocan City, Metro Manila, as a school of life skills."),
        ("2020", "St. Clare Online keeps learning going", "During the pandemic the college moved classes to its own online platform so no student got left behind. UniFAST-TES applications opened for A.Y. 2020-2021."),
        ("2021", "The Virtual Lab and the 36th anniversary", "The Virtual Lab (VR + AR = MR) opened, Teacher-DJs went live on Zoom Monday to Saturday, and the college marked its 36th founding anniversary."),
        ("2023", "The Professional Mace", "On 23 September 2023 St. Clare College introduced its Professional Mace, the eternal flame of professionalism."),
        ("2024", "The Stars of 2024", "The 38th Commencement Exercises, and the President's Scholarship with zero down payment for the SHS Class of 2024."),
    ]
    yrs = "".join(f'<div class="yr cut c-white" data-pop style="--rest:{[-.8, .6, -.4, .8, -.6][i]}deg"><b>{y}</b><div><h3>{h}</h3><p>{p}</p></div></div>' for i, (y, h, p) in enumerate(tl))
    fac = ["E-boards in all 95 classrooms", "Air-conditioned classrooms and restrooms", "Virtual Lab with Acer Mixed Reality", "Computer laboratories", "Library and Learning Resource Center, 3rd floor", "St. Clare Virtual Studio"]
    body = phero("About", ["Building", "<span class='sun'>our future</span>"],
                 "Transforming education since 1985: the School of Life Skills and a leading institution for professional development.", "ph-royal", (5, 6, 7, 8, 9)) \
        + band("b-white", f"""<div class="split">
    <figure class="photo cut c-white tilt-l"><span class="tape" aria-hidden="true"></span>{img_tag("campus-building.jpg", "St. Clare College building on Zabarte Road with the SCO Online sign", 1600, 900)}<figcaption>Zabarte Road, Caloocan City</figcaption></figure>
    <div><h2>One campus, built to learn</h2><ul class="ticks">{"".join(f"<li>{x}</li>" for x in fac)}</ul></div>
  </div>""") + band("b-chalk", f'<div class="head"><h2>What we stand for</h2><p class="lede">Quality, affordable and sustainable education for the total development of every Clarean.</p></div>{VM}') \
        + band("b-ink on-dark mace", FLAME_INNER) \
        + band("b-royal on-dark", f"""<div class="split"><div><h2>No one gets left behind</h2></div>
  <div><p class="lede">When colleges around the world moved to online and open distance learning, St. Clare's own platform made sure its students could continue and finish their education.</p>
  <p>Learning management, the e-Library, enrollment, personal transactions and virtual broadcasting all live on one system: St. Clare Online.</p>
  <a class="btn" href="portals.html">The five systems {ARROW}</a></div></div>""") \
        + band("b-kraft", f'<div class="head"><h2>Our story</h2><p class="lede">Four decades of firsts for Caloocan.</p></div><div class="years">{yrs}</div>') \
        + closer("Come visit", "Zabarte Road, Caloocan City. Office hours 9:00 AM to 5:00 PM.", 4)
    page("about.html", "About St. Clare College | Vision, Mission & History",
         "Founded in 1985 in Caloocan City, St. Clare College is the School of Life Skills: vision, mission, the Professional Mace and our milestones.", body)


def build_academics():
    ter = "".join(f"""<details><summary><span class="c">{c}</span><span class="t">{n}<small>{school}</small></span><span class="plus" aria-hidden="true">+</span></summary>
<div class="body"><p>{short} {longd}</p><div class="chips">{"".join(f"<span>{t}</span>" for t in tags)}</div></div></details>""" for c, n, ic, school, short, longd, tags in TERTIARY)
    colors = ["c-red", "c-sun", "c-royal", "c-leaf", "c-white"]
    strands = "".join(f"""<div class="cut {colors[i]}" data-pop style="--rest:{[-1, .8, -.6, 1, -.8][i]}deg"><span class="k">{k}</span><h3>{n}</h3><p>{d}</p>{("<ul>" + "".join(f"<li>{s}</li>" for s in sp) + "</ul>") if sp else ""}</div>""" for i, (k, n, t, d, sp) in enumerate(SHS))
    basic = "".join(f'<div class="note cut {["c-blue", "c-yellow", "c-pink"][i]}"><span class="tape" aria-hidden="true"></span><span class="big">{k}</span><h3>{n}</h3><p>{d}</p></div>' for i, (k, n, d) in enumerate(BASIC))
    body = phero("Academics", ["Every stage,", "<span class='sun'>one school</span>"],
                 "Basic Education, Senior High School and eight college degrees, taught on campus, online or blended.", "ph-red", (10, 11, 12, 13, 14)) \
        + band("b-white", f'<div class="head"><h2>College degrees</h2><p class="lede">Theory in class, mastery in the laboratory, kitchen and field. Open a programme to read more.</p></div><div class="board">{ter}</div>', "tertiary") \
        + band("b-chalk", f'<div class="head"><h2>Senior High tracks</h2><p class="lede">Five ways to prepare for college, a career or a business, including TESDA National Certification for TVL-HE.</p></div><div class="strands">{strands}</div>', "shs") \
        + band("b-kraft", f"""<div class="head"><h2>Basic Education</h2><p class="lede">Nursery to Grade 10, with care, curiosity and a proper school uniform.</p></div>
  <div class="split top"><div class="wall one">{basic}</div>
  <div class="deal-figs tall"><img src="img/cut-girl.webp" alt="Girl in the St. Clare Basic Education uniform" width="254" height="786" loading="lazy"><img src="img/cut-boy.webp" alt="Boy in the St. Clare Basic Education uniform" width="260" height="767" loading="lazy"></div></div>""", "basic") \
        + closer("Find your path", "Talk to admissions about the programme that fits your goals.", 8)
    page("academics.html", "Academics | St. Clare College Programmes",
         "College degrees (BSCS, BSHM, BSTM, BSBA, BEEd, BSEd, AB PolSci), Senior High tracks (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and Basic Education at St. Clare College.", body)


def build_admissions():
    tabs, sheets = [], []
    for i, (k, (label, ab, items)) in enumerate(REQ.items()):
        sel = i == 0
        tabs.append(f'<button role="tab" id="rt-{k}" aria-controls="rp-{k}" aria-selected="{"true" if sel else "false"}"{"" if sel else " tabindex=\"-1\""} data-hash="{k}">{label}</button>')
        sheets.append(f'<div class="req-sheet cut lg c-white" role="tabpanel" id="rp-{k}" aria-labelledby="rt-{k}"{"" if sel else " hidden"}><span class="stamp-mark">Long brown envelope</span><h3 class="h3-lg">{label}</h3>{checklist(items)}</div>')
    forms = "".join(f'<li><a href="{SRC}/downloadable-forms" rel="noopener"><span class="ext{" doc" if e == "DOC" else ""}">{e}</span><span><b>{n}</b><small>{c}</small></span><span class="arr" aria-hidden="true">&darr;</span></a></li>' for e, n, c in FORMS)
    faq = [
        ("Can I study fully online?", "Yes. St. Clare College offers two modalities: full online and blended (online plus on-campus days). Choose one when you enroll."),
        ("How do I get my class schedule?", "After paying the matriculation fee and filling up your registration form, go to the Library on the 3rd floor for enlistment at stclareonline.com/ims. Your section and schedule are posted on the website and emailed by your Program Head."),
        ("When does enrollment open, and how much are the fees?", f"Call the admissions office at {PHONE} or email {EMAIL} to confirm this school year's enrollment dates and fees before your visit."),
        ("Are there scholarships?", "Ask the admissions office for this school year's offers. Submit a certificate of indigency with your requirements for scholarship consideration. UniFAST-TES grantees can verify their status and disbursement schedule on the PMS."),
        ("How do I request my Transcript of Records or diploma?", "Only through the Official Document Request Portal on the Personal Management System (PMS). Do not transact with fixers."),
    ]
    faqs = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in faq)
    body = phero("Admissions", ["Enroll", "<span class='sun'>with ease</span>"],
                 "Three stops on campus, one brown envelope, and you're a Clarean.", "ph-red", (2, 4, 6, 8, 10),
                 f'<div class="actions mt-l"><a class="btn" href="#steps">See the 3 steps {ARROW}</a><a class="btn b-white" href="{SRC}/ims" rel="noopener">Returning students: enlist on IMS</a></div>') \
        + band("b-white", route_inner("Three stops on campus"), "steps") \
        + band("b-chalk", f"""<div class="head"><h2>What to bring</h2><p class="lede">Pick your level. All documents become property of the school once submitted for admission.</p></div>
  <div class="req-tabs" role="tablist" aria-label="Requirement type">{"".join(tabs)}</div>
  {"".join(sheets)}""", "requirements") \
        + band("b-royal on-dark", f"""<div class="head"><h2>Full online or blended</h2><p class="lede">Personalized learning pathways: choose the modality that fits your life.</p></div>
  <div class="vm">
    <div class="cut c-sun tilt-l" data-pop style="--rest:-1.2deg"><h3>Full online</h3><p>Learn from anywhere through St. Clare Online: LMS classes, the e-Library and virtual broadcasts.</p></div>
    <div class="cut c-white tilt-r" data-pop style="--rest:1deg"><h3 class="red">Blended</h3><p>Combine online learning with on-campus days in air-conditioned classrooms with e-boards, laboratories and the Virtual Lab.</p></div>
  </div>""", "modality") \
        + band("b-kraft", f"""<div class="head"><h2>Scholarships</h2><p class="lede">&ldquo;An investment in knowledge pays the best interest.&rdquo; Benjamin Franklin</p></div>
  <div class="wall">
    <div class="note cut c-white"><span class="tape" aria-hidden="true"></span><span class="stamp-mark red">SY 2024-2025</span><h3 class="mt">President's Scholarship</h3><p>Offered to the St. Clare SHS Class of 2024, with zero down payment. Ask admissions about this year's scholarships.</p></div>
    <div class="note cut c-yellow"><span class="tape r" aria-hidden="true"></span><h3>UniFAST-TES</h3><p>Tertiary Education Subsidy grantees verify their status and disbursement schedule on the PMS.</p><a class="more" href="{SRC}/pms" rel="noopener">Go to PMS</a></div>
    <div class="note cut c-blue"><span class="tape" aria-hidden="true"></span><h3>Certificate of indigency</h3><p>Optional. Submit it with your requirements to be considered for scholarship.</p></div>
  </div>""", "scholarships") \
        + band("b-white", f"""<div class="split top">
  <div><h2>Forms</h2><p class="lede mt gap-b">Institutional forms, guidelines and memoranda on St. Clare Online.</p><ul class="files">{forms}</ul></div>
  <div><h2>Good to know</h2><div class="faq mt-l">{faqs}</div></div>
</div>""") \
        + band("b-chalk", f"""<div class="split"><div><h2>The uniform</h2><p class="lede mt">Pre-school to Grade 10 learners wear the official St. Clare College uniform.</p></div>
  <div class="deal-figs tall"><img src="img/cut-girl.webp" alt="Girl in the St. Clare Basic Education uniform" width="254" height="786" loading="lazy"><img src="img/cut-boy.webp" alt="Boy in the St. Clare Basic Education uniform" width="260" height="767" loading="lazy"></div></div>""") \
        + closer("Your turn", "Take the first step towards a brighter tomorrow.", 2)
    page("admissions.html", "Admissions | Enroll at St. Clare College",
         "How to enroll at St. Clare College: three steps on campus, requirements for college freshmen, transferees, Basic Education and SHS, scholarships and forms.", body)


def build_campus():
    ev = "".join(f'<div class="ev cut c-white"><span class="d">{m} {dd}</span><div><h3>{h}</h3><p>{p}</p></div><span class="w">{w}</span></div>' for m, dd, h, p, w in EVENTS)
    hb = "".join(f'<li><a href="{SRC}/cms" rel="noopener"><span class="ext">PDF</span><span><b>{h}</b><small>Handbooks &amp; manuals</small></span><span class="arr" aria-hidden="true">&darr;</span></a></li>' for h in HANDBOOKS)
    body = phero("Campus life", ["Life on", "<span class='sun'>campus</span>"],
                 "E-boards in every classroom, a Virtual Lab, our own channels, and a community that keeps learning online.", "ph-leaf", (11, 13, 15, 0, 2)) \
        + band("b-kraft", collage(), "virtual-lab") \
        + band("b-red on-dark", f'<div class="head"><h2>SCO Online channels</h2><p class="lede">Broadcasting and Teacher-DJs are part of the St. Clare Online Education System, from the Monday virtual flag ceremony to commencement exercises.</p></div>{flags_html()}') \
        + band("b-white", f"""<div class="split">
  <figure class="photo cut c-white tilt-r"><span class="tape" aria-hidden="true"></span>{img_tag("campus-building.jpg", "St. Clare College campus building", 1600, 900)}<figcaption>The campus on Zabarte Road</figcaption></figure>
  <div><h2>Built for focus</h2><ul class="ticks"><li>E-boards in all 95 classrooms</li><li>Air-conditioned classrooms and restrooms</li><li>Computer laboratories for programming and networking</li><li>Library and enlistment area on the 3rd floor</li><li>St. Clare Virtual Studio for webinars and broadcasts</li></ul></div>
</div>""") \
        + band("b-ink on-dark", f'<div class="head"><h2>On the calendar</h2><p class="lede">Key dates for students, parents and faculty. <a href="{SRC}/calendar" rel="noopener">Full calendar</a></p></div><div class="events">{ev}</div>') \
        + band("b-chalk", f'<div class="split top"><div><h2>Digital citizenship</h2><p class="lede mt">Online learning comes with responsibilities. These policies guide life on St. Clare Online.</p></div><ul class="files">{hb}</ul></div>', "digital-citizenship") \
        + closer("See it yourself", "Tour the campus on Zabarte Road. We're open 9:00 AM to 5:00 PM.", 6)
    page("campus-life.html", "Campus Life | Virtual Lab, SCO Online & Events",
         "The St. Clare College Virtual Lab (VR + AR = MR), SCO Online channels, campus facilities, calendar and digital citizenship.", body)


def build_portals():
    kc = ["c-red", "c-sun", "c-royal", "c-ink", "c-white"]
    keys = "".join(f'<a class="key cut {kc[i]}" href="{SRC}/{slug}" rel="noopener"><b>{k}</b><h3>{n}</h3><p>{d}</p><span class="go">Open {k}</span></a>' for i, (k, n, d, slug) in enumerate(PORTALS))
    quick = [("Enroll and enlist online", "Students: register for your section and schedule.", "ims", "c-yellow"),
             ("Faculty attendance", "Basic Ed, SHS and Tertiary attendance monitoring.", "ims", "c-white"),
             ("Official Document Request Portal", "Transcripts, diplomas and other documents. No fixers.", "pms", "c-pink"),
             ("Enrollment status and sections", "College corner and the Program Heads directory.", "lms", "c-blue"),
             ("e-Library", "Learning Resource Center, powered by ProQuest.", "cms", "c-yellow"),
             ("Virtual flag ceremony", "Every Monday, 7:00 AM, plus commencement broadcasts.", "vms", "c-white")]
    qs = "".join(f'<a class="note cut {c}" href="{SRC}/{s}" rel="noopener"><span class="tape{" r" if i % 2 else ""}" aria-hidden="true"></span><span class="meta">{s.upper()}</span><h3>{h}</h3><p>{p}</p><span class="more">Open</span></a>' for i, (h, p, s, c) in enumerate(quick))
    body = phero("Portals", ["St. Clare", "<span class='sun'>Online</span>"],
                 "Five connected systems for learning, content, enrollment, personal transactions and virtual broadcasting.", "ph-royal", (1, 3, 5, 7, 9)) \
        + band("b-chalk", f'<div class="head"><h2>Grab your key</h2><p class="lede">Each system opens on stclareonline.com.</p></div><div class="keys">{keys}</div>') \
        + band("b-kraft", f'<div class="head"><h2>Most requested</h2><p class="lede">Shortcuts for students, parents and faculty.</p></div><div class="wall">{qs}</div>') \
        + closer("Need a hand?", f"Call {PHONE} or email {EMAIL}, 9:00 AM to 5:00 PM.", 10)
    page("portals.html", "St. Clare Online Portals | LMS, CMS, IMS, PMS, VMS",
         "Access the St. Clare Online Education System: Learning, Content, Institutional, Personal and Virtual Management Systems.", body)


def build_news():
    cols = ["c-white", "c-yellow", "c-blue", "c-pink"]
    cards = []
    for i, (date, cat, h, p, img, gen, link) in enumerate(NEWS):
        top = img_tag(img, "", 1230, 640) if img else f'<span class="big">{esc((gen if gen != "mace" else "Mace").upper())}</span>'
        cards.append(f'<a class="note cut {cols[i % 4]}" href="{link}" rel="noopener"><span class="tape{" r" if i % 2 else ""}" aria-hidden="true"></span>{top}<span class="meta">{cat} &middot; {date}</span><h3>{h}</h3><p>{p}</p><span class="more">Read more</span></a>')
    body = phero("News", ["News &amp;", "<span class='sun'>notices</span>"],
                 "Milestones, scholarships, advisories and stories from the St. Clare community.", "ph-royal", (12, 14, 0, 3, 6)) \
        + band("b-kraft", f'<h2 class="sr-only">Latest notices</h2><div class="wall">{"".join(cards)}</div>') \
        + band("b-red on-dark", flags_html()) \
        + closer("Be a Clarean", "Basic Education, Senior High School and College, on campus or online.", 12)
    page("news.html", "News | St. Clare College", "Latest news, scholarships, advisories and events from St. Clare College of Caloocan.", body)


def build_contact():
    body = phero("Contact", ["Let's talk", "<span class='sun'>enrollment</span>"],
                 "Questions about programmes, requirements, dates or fees? We're here 9:00 AM to 5:00 PM.", "ph-red", (4, 9, 13, 15, 1)) \
        + band("b-ink on-dark", f"""<div class="split top">
  <div class="addr">
    <h2>Visit, call, write</h2>
    <div><b>Campus</b>{ADDRESS}</div>
    <div><b>Phone</b><a href="tel:{PHONE_TEL}">{PHONE}</a></div>
    <div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div><b>Office hours</b>9:00 AM - 5:00 PM</div>
    <div class="socials"><a href="{FB}" rel="noopener" aria-label="Facebook">{FB_SVG}</a><a href="{YT}" rel="noopener" aria-label="YouTube">{YT_SVG}</a></div>
  </div>
  <form class="regform cut lg c-white" data-mailto="{EMAIL}">
    <div class="rf-head"><b>Inquiry form</b><img src="img/seal-200.webp" alt="" width="54" height="54"></div>
    <div class="rf-grid">
      <div class="rf"><label for="f-name">Full name <em>(required)</em></label><input id="f-name" name="Name" autocomplete="name" required></div>
      <div class="rf"><label for="f-email">Email <em>(required)</em></label><input id="f-email" name="Email" type="email" autocomplete="email" required></div>
      <div class="rf"><label for="f-level">Interested in</label><select id="f-level" name="Level"><option>Basic Education</option><option>Senior High School</option><option selected>College</option><option>Other</option></select></div>
      <div class="rf"><label for="f-src">Where did you hear about us?</label><select id="f-src" name="Source"><option>Facebook</option><option>YouTube</option><option>Friend or family</option><option>Search</option><option>Other</option></select></div>
      <div class="rf full"><label for="f-sub">Subject</label><input id="f-sub" name="subject" value="Enrollment inquiry"></div>
      <div class="rf full"><label for="f-msg">Message <em>(required)</em></label><textarea id="f-msg" name="Message" required></textarea></div>
    </div>
    <div class="rf-foot"><button class="btn b-red" type="submit">Send inquiry {ARROW}</button><p>Opens your email app, addressed to {EMAIL}. No email app? Call {PHONE}.</p><p class="form-status" role="status"></p></div>
  </form>
</div>""") \
        + band("b-chalk", '<div class="map cut c-white"><iframe title="Map to St. Clare College of Caloocan" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=St.+Clare+College+of+Caloocan,+Zabarte+Road,+Caloocan+City&output=embed"></iframe></div>')
    page("contact.html", "Contact St. Clare College | Caloocan City",
         f"Contact St. Clare College of Caloocan: {ADDRESS}. Phone {PHONE}, email {EMAIL}, 9:00 AM - 5:00 PM.", body)


if __name__ == "__main__":
    build_home(); build_about(); build_academics(); build_admissions()
    build_campus(); build_portals(); build_news(); build_contact()
