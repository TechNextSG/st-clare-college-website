# St. Clare College website - "Campus Tarpaulin" builder. Run: python build.py
import os, html, json
from data import *

V = "5"  # asset cache-buster
LIBS = [
    "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js",
    "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js",
    "https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js",
]
PAUSE = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M3 1h4v14H3zM9 1h4v14H9z"/></svg>'
STAR = '<svg class="star" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 1l3.1 7.6L23 9.3l-6 5.3 1.8 8L12 18.4 5.2 22.6 7 14.6 1 9.3l7.9-.7z"/></svg>'
GROM = '<span class="grommets" aria-hidden="true"><i></i><i></i><i></i><i></i></span>'
TIES2 = '<span class="tie" aria-hidden="true"></span><span class="tie" aria-hidden="true"></span>'
TIES3 = TIES2 + '<span class="tie" aria-hidden="true"></span>'
FLAME = ('<svg class="flame" viewBox="0 0 120 170" aria-hidden="true">'
         '<path fill="#d7141a" d="M60 4C78 40 112 62 112 108c0 32-23 58-52 58S8 140 8 108C8 74 32 58 40 30c10 18 6 34 20 44C64 50 52 28 60 4z"/>'
         '<path fill="#ffd400" d="M60 52c10 22 32 38 32 66 0 22-14 38-32 38s-32-16-32-38c0-20 14-30 18-48 6 12 4 22 14 28 2-16-6-30 0-46z"/>'
         '<path fill="#ffffff" d="M60 100c6 12 16 20 16 34 0 11-7 20-16 20s-16-9-16-20c0-10 8-16 9-26 3 6 3 10 7 12 1-8-3-14 0-20z"/></svg>')

def esc(s): return html.escape(s, quote=True)

def head(title, desc):
    libs = "".join(f'\n<script src="{u}" defer></script>' for u in LIBS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#d7141a">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="img/campus-building.jpg">
<link rel="icon" href="img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/bigshoulders.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/figtree.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/tarp.css?v={V}">{libs}
<script src="assets/tarp.js?v={V}" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(page):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>' for h, t in NAV)
    return f"""<header class="bar"><div class="wrap">
  <a class="brand" href="index.html" aria-label="St. Clare College, home">
    <img src="img/seal-200.webp" alt="" width="52" height="52">
    <span><b>St. Clare College</b><span>The School of Life Skills</span></span>
  </a>
  <nav class="menu" id="menu" aria-label="Main">{links}<a class="tag-btn" href="admissions.html">Enroll now {ARROW}</a></nav>
  <a class="tag-btn top" href="admissions.html">Enroll now</a>
  <button class="menu-btn" aria-expanded="false" aria-controls="menu"><span>Menu</span></button>
</div></header>
<main id="main">
"""

def footer():
    portals = "".join(f'<li><a href="{SRC}/{p[3]}" rel="noopener">{p[0]}: {p[1]}</a></li>' for p in PORTALS)
    return f"""</main>
<footer class="foot on-dark">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="brand-f"><img src="img/seal-200.webp" alt="" width="66" height="66"><b>St. Clare<br>College</b></div>
        <p>The School of Life Skills. Serving Caloocan since 1985; online through St. Clare Online since 2020.</p>
        <div class="socials"><a href="{FB}" rel="noopener" aria-label="St. Clare College on Facebook">{FB_SVG}</a><a href="{YT}" rel="noopener" aria-label="St. Clare College on YouTube">{YT_SVG}</a></div>
      </div>
      <div><h3>Explore</h3><ul><li><a href="about.html">About St. Clare</a></li><li><a href="academics.html">Academics</a></li><li><a href="admissions.html">Admissions</a></li><li><a href="campus-life.html">Campus life</a></li><li><a href="news.html">News</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h3>St. Clare Online</h3><ul>{portals}<li><a href="{SRC}/downloadable-forms" rel="noopener">Downloadable forms</a></li></ul></div>
      <div><h3>Visit</h3><ul><li>{ADDRESS}</li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>Office hours 9:00 AM - 5:00 PM</li></ul></div>
    </div>
    <div class="foot-bottom"><span>&copy; <span data-year>2026</span> St. Clare College of Caloocan &middot; St. Clare Online Education System&reg;</span><a href="https://sdgs.un.org/goals/goal4" rel="noopener">UN SDG 4: Quality Education</a></div>
  </div>
  <p class="foot-word" aria-hidden="true">Clareans</p>
</footer>
</body>
</html>
"""

def page(name, title, desc, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(head(title, desc) + header(name) + body + footer())
    print("wrote", name)

def lines(*parts):
    return "".join(f'<span class="l"><span>{p}</span></span>' for p in parts)

def phero(crumb, h1_parts, lede, color="red-v", photo=None, cut=None, extra=""):
    ph = f'<div class="phero-photo"><img src="img/{photo}" alt="" fetchpriority="high"></div>' if photo else ""
    bg = "" if photo else ' style="background:var(--paper)"'
    ct = f'<img class="cut" src="img/{cut}" alt="">' if cut else ""
    return f"""<section class="phero"{bg}>
  {ph}<div class="pipe" aria-hidden="true"></div>
  <div class="wrap">
    <div class="tarp {color}">{TIES2}{GROM}
      <p class="crumbs"><a href="index.html">Home</a> / {crumb}</p>
      <h1>{lines(*h1_parts)}</h1>
      <p class="lede">{lede}</p>{extra}
    </div>
  </div>{ct}
</section>
"""

def closer(word="Enroll now", line="Basic Education, Senior High School and College, on campus or fully online."):
    return f"""<section class="sec closer on-sun">
  <div class="wrap">
    <h2>{word}</h2>
    <p class="lede">{line}</p>
    <div class="hero-actions"><a class="tag-btn ink-t" href="admissions.html">Start enrollment {ARROW}</a><a class="tag-btn red-t" href="contact.html">Ask admissions</a></div>
  </div>
</section>
"""

def checklist(items): return '<ul class="checklist">' + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"

def tickets():
    out = []
    for i, (h, where, items) in enumerate(STEPS):
        out.append(f"""<article class="ticket" style="--r:{[-1.2, .8, -.6][i]}deg">
  <span class="where">{where}</span><span class="no" aria-hidden="true">{i + 1}</span>
  <h3>{h}</h3><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul>
</article>""")
    return '<div class="steps">' + "".join(out) + "</div>"

def route_section(title="Bring the brown envelope"):
    return f"""<section class="sec on-white" id="steps">
  <div class="wrap">
    <div class="head"><h2 data-letters>{title}</h2><p class="lede">Every St. Clare enrollment starts with a long brown envelope and three stops on campus.</p></div>
    <div class="route">
      <div class="envelope">
        <div class="env" role="img" aria-label="A long brown envelope holding the enrollment documents">
          <div class="env-flap"></div>
          <div class="env-docs"><div class="env-doc"><b>PSA birth certificate</b>Photocopy</div><div class="env-doc"><b>Form 138</b>Report card</div><div class="env-doc"><b>2x2 photos</b>2 pcs., recent</div></div>
          <div class="env-front"><span class="hand">For: Enrollment Officer<br>St. Clare College</span></div>
        </div>
        {checklist(REQ["freshmen"][2][2:7])}
        <p style="margin-top:14px"><a href="admissions.html#requirements">Full checklist for every level</a></p>
      </div>
      {tickets()}
    </div>
  </div>
</section>
"""

def flags_html():
    items = ['<div class="flag logo"><img src="img/sco-online.webp" alt="SCO Online" width="512" height="512" loading="lazy"></div>']
    items += [f'<div class="flag"><b>{n}</b><small>{k}</small></div>' for n, k in CHANNELS]
    return f'<div class="bunting"><span class="line" aria-hidden="true"></span><div class="flags">{"".join(items)}</div></div>'

VLAB = f"""<div class="vlab">
  <div>
    <h2 class="sr-only">The St. Clare Virtual Lab</h2>
    <p class="eq" aria-label="Virtual reality plus augmented reality equals mixed reality"><span>VR</span><span class="op">+</span><span>AR</span><span class="op">=</span><span class="res">MR</span></p>
    <h3 style="font-size:clamp(2rem,4vw,3.2rem);margin-bottom:14px">The Virtual Lab</h3>
    <p class="lede">Another first from St. Clare College: an immersive lab with the Predator Thronos and the Mixed Reality facility by Acer, opened in 2021.</p>
    <a class="tag-btn ink-t" href="campus-life.html#virtual-lab">See the lab {ARROW}</a>
  </div>
  <figure class="photo-print" style="--r:2.5deg" data-pin>
    <span class="pin y" aria-hidden="true"></span>
    <img src="img/virtual-lab-predator.jpg" alt="Predator gaming stations in the St. Clare Virtual Lab" width="1600" height="1066" loading="lazy">
    <figcaption>Predator Thronos + Acer Mixed Reality</figcaption>
  </figure>
</div>"""

FLAME_SEC = f"""<section class="sec mace on-ink on-dark">
  <div class="wrap">
    {FLAME}
    <h2 data-letters>The eternal flame of professionalism</h2>
    <blockquote>&ldquo;A beacon of professionalism and culture of excellence.&rdquo;</blockquote>
    <cite>St. Clare College Professional Mace &middot; 23 September 2023</cite>
  </div>
</section>
"""

VM = f"""<div class="vm">
  <div class="tarp royal-v" data-unfurl>{TIES2}{GROM}<h3>Vision</h3><p>To become the leading institution for professional development and the first and foremost provider of quality, affordable and sustainable development education.</p></div>
  <div class="tarp white-v" data-unfurl>{TIES2}{GROM}<h3 class="red">Mission</h3><p>To provide quality and excellent global education for the total development of a responsible, innovative, skillful and professional global workforce whose values and dignity are beyond par.</p></div>
</div>"""

def level_rows(level):
    if level == "college":
        return "".join(f'<li><span class="c">{c}</span><span class="n">{n}<small>{s}</small></span></li>' for c, n, _, s, *_ in TERTIARY)
    if level == "shs":
        return "".join(f'<li><span class="c">{k}</span><span class="n">{n}<small>{t}{(": " + ", ".join(sp)) if sp else ""}</small></span></li>' for k, n, t, _, sp in SHS)
    return "".join(f'<li><span class="c">{k}</span><span class="n">{n}<small>{d}</small></span></li>' for k, n, d in BASIC)

def picker():
    lv = [("basic", "Basic Ed", "Nursery to Grade 10"), ("shs", "Senior High", "Grades 11-12, five tracks"), ("college", "College", "Eight degree programmes")]
    tabs = "".join(f'<button role="tab" id="lt-{k}" aria-controls="lp-{k}" aria-selected="{"true" if k == "college" else "false"}"{"" if k == "college" else " tabindex=\"-1\""} data-v="{k}"><b>{n}</b><small>{s}</small></button>' for k, n, s in lv)
    figs = {
        "basic": '<img src="img/cut-girl.webp" alt="Girl in the St. Clare Basic Education uniform" width="254" height="786" loading="lazy"><img src="img/cut-boy.webp" alt="Boy in the St. Clare Basic Education uniform" width="260" height="767" loading="lazy">',
        "shs": '<div class="note-card yellow" style="--r:-2deg"><span class="pin" aria-hidden="true"></span><h3>TESDA-assessed</h3><p>TVL-HE students take TESDA competency assessment for National Certification (NC).</p></div>',
        "college": '<figure class="photo-print" style="--r:-2deg;margin:0"><span class="pin" aria-hidden="true"></span><img src="img/graduates.jpg" alt="St. Clare College graduates at the 2024 commencement" width="1230" height="640" loading="lazy"><figcaption>The Stars of 2024</figcaption></figure>',
    }
    reqkey = {"basic": "basic", "shs": "shs", "college": "freshmen"}
    panels = "".join(f"""<div class="deal" role="tabpanel" id="lp-{k}" aria-labelledby="lt-{k}"{"" if k == "college" else " hidden"}>
  <div class="deal-grid">
    <ul class="rows">{level_rows(k)}</ul>
    <aside><div class="deal-figs">{figs[k]}</div>
      <p style="margin-top:18px"><a class="tag-btn" href="admissions.html#{reqkey[k]}">What to bring {ARROW}</a></p>
      <p><a href="academics.html#{k if k != 'college' else 'tertiary'}">Programme details</a></p></aside>
  </div>
</div>""" for k, *_ in lv)
    return f'<div class="picker" role="tablist" aria-label="Choose a school level">{tabs}</div>{panels}'

# ---------------------------------------------------------------- pages
def build_home():
    flap_words = ["BSCS Computer Science", "BSHM Hospitality", "BSTM Tourism", "BSBA Business Admin", "BEEd Elementary Ed", "BSEd English", "BSEd Math", "AB Political Science",
                  "SHS ABM", "SHS HUMSS", "SHS Arts & Design", "SHS TVL-ICT", "SHS TVL-HE", "Nursery to Grade 10", "Now enrolling"]
    facts = ['Since <span class="r">1985</span>', 'E-boards in all <span class="b">95</span> classrooms', '<span class="r">38th</span> commencement, June 2024', 'Full online <span class="b">or</span> blended', '<span class="r">547,806</span> views of our 2020 start-up module']
    fb = STAR.join(f"<span>{x}</span>" for x in facts)
    body = f"""<section class="hero">
  <div class="hero-photo"><img src="img/campus-building.jpg" alt="" fetchpriority="high" width="1600" height="900"></div>
  <div class="pipe" aria-hidden="true"></div>
  <div class="wrap">
    <div class="tarp red-v hero-tarp">{TIES3}{GROM}
      <h1>{lines("The school", "<span class='sun'>of life skills</span>")}</h1>
      <p class="lede">St. Clare College of Caloocan. Nursery to College on one campus, and the leading edge in online education.</p>
      <div class="hero-actions"><a class="plain" href="#levels">Find your level</a></div>
      <span class="hang"><span class="cord" aria-hidden="true"></span><a class="tag-btn" href="admissions.html">Enroll now {ARROW}</a></span>
      <img class="stamp" src="img/seal-400.webp" alt="St. Clare College of Caloocan seal" width="392" height="396">
    </div>
  </div>
  <img class="hero-vr" src="img/cut-vr.webp" alt="" width="888" height="875">
  <div class="flap-strip on-dark"><div class="wrap"><span class="lbl">Programmes</span><div class="flaps" data-flaps='{esc(json.dumps(flap_words))}' data-len="21"></div><button class="mq-btn" type="button" aria-label="Pause programme ticker">{PAUSE}</button></div></div>
</section>

<section class="sec" id="levels">
  <div class="wrap">
    <div class="head"><h2 data-letters>Pick your level</h2><p class="lede">From a child's first school day to a college degree, everything happens under one St. Clare roof.</p></div>
    {picker()}
  </div>
</section>

<div class="factband"><p class="facttrack">{fb}</p></div>

{route_section()}

<section class="sec on-sun">
  <div class="wrap">{VLAB}</div>
</section>

<section class="sec on-red on-dark">
  <div class="wrap">
    <div class="head"><h2 data-letters>Tune in to SCO Online</h2><p class="lede">St. Clare runs its own channels: wellness, sport, leadership, innovation and the stories of Clareans, plus a virtual flag ceremony every Monday at 7:00 AM.</p></div>
    {flags_html()}
  </div>
</section>

<section class="sec-tight on-white">
  <div class="wrap">
    <div class="tarp royal-v congrats" data-unfurl>{TIES2}{GROM}
      <div class="inner">
        <div class="ph"><img src="img/graduates.jpg" alt="St. Clare College graduates applauding at commencement" width="1230" height="640" loading="lazy"></div>
        <div class="txt"><h2><span class="sun">Congratulations,</span> Stars of 2024!</h2><p>St. Clare College held its 38th Commencement Exercises in June 2024.</p></div>
      </div>
    </div>
  </div>
</section>

{FLAME_SEC}

<section class="sec on-cork">
  <div class="wrap">
    <div class="split top">
      <div class="note-card" style="--r:-1.5deg" data-pin><span class="pin" aria-hidden="true"></span>
        <span class="rubber red" style="float:right">SY 2024-2025</span>
        <h3>SHS Alumni VIP Package</h3>
        <p>For the St. Clare SHS Class of 2024: the President's Scholarship with zero down payment.</p>
        <p class="hand" style="font-size:1.2rem">Ask admissions about this year's scholarships.</p>
      </div>
      <div class="note-card blue" style="--r:1.2deg" data-pin><span class="pin b" aria-hidden="true"></span>
        <h3>Full online or blended</h3>
        <p>Learn from anywhere on St. Clare Online, or combine online days with air-conditioned classrooms, e-boards and the Virtual Lab.</p>
        <a class="more" href="admissions.html#modality">Compare the two</a>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="head"><h2 data-letters>Why we teach</h2><p class="lede">A responsible, innovative, skillful and professional global workforce, starting here in Caloocan.</p></div>
    {VM}
  </div>
</section>

{closer()}
"""
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
    yrs = "".join(f'<div class="yr"><b>{y}</b><div><h3>{h}</h3><p>{p}</p></div></div>' for y, h, p in tl)
    fac = ["E-boards in all 95 classrooms", "Air-conditioned classrooms and restrooms", "Virtual Lab with Acer Mixed Reality", "Computer laboratories", "Library and Learning Resource Center, 3rd floor", "St. Clare Virtual Studio"]
    body = phero("About", ["Building", "<span class='sun'>our future</span>"],
                 "Transforming education since 1985: the School of Life Skills and a leading institution for professional development.",
                 "red-v", "campus-building.jpg") + f"""
<section class="sec on-white">
  <div class="wrap split">
    <figure class="photo-print" style="--r:-2deg" data-pin><span class="pin" aria-hidden="true"></span>
      <img src="img/campus-building.jpg" alt="St. Clare College building on Zabarte Road with the SCO Online sign" width="1600" height="900" loading="lazy">
      <figcaption>Zabarte Road, Caloocan City</figcaption></figure>
    <div>
      <h2 data-letters>One campus, built to learn</h2>
      <ul class="ticks">{"".join(f"<li>{x}</li>" for x in fac)}</ul>
    </div>
  </div>
</section>
<section class="sec"><div class="wrap">
  <div class="head"><h2 data-letters>What we stand for</h2><p class="lede">Quality, affordable and sustainable education for the total development of every Clarean.</p></div>
  {VM}
</div></section>
{FLAME_SEC}
<section class="sec on-royal on-dark"><div class="wrap split">
  <div><h2 data-letters>No one gets left behind</h2></div>
  <div><p class="lede">When colleges around the world moved to online and open distance learning, St. Clare's own platform made sure its students could continue and finish their education.</p>
  <p>Learning management, the e-Library, enrollment, personal transactions and virtual broadcasting all live on one system: St. Clare Online.</p>
  <a class="tag-btn" href="portals.html">The five systems {ARROW}</a></div>
</div></section>
<section class="sec on-white"><div class="wrap">
  <div class="head"><h2 data-letters>Our story</h2><p class="lede">Four decades of firsts for Caloocan.</p></div>
  <div class="years">{yrs}</div>
</div></section>
""" + closer("Come visit", "Zabarte Road, Caloocan City. Office hours 9:00 AM to 5:00 PM.")
    page("about.html", "About St. Clare College | Vision, Mission & History",
         "Founded in 1985 in Caloocan City, St. Clare College is the School of Life Skills: vision, mission, the Professional Mace and our milestones.", body)


def build_academics():
    ter = "".join(f"""<details><summary><span class="c">{c}</span><span class="t">{n}<small>{school}</small></span><span class="plus" aria-hidden="true">+</span></summary>
<div class="body"><p>{short} {longd}</p><div class="chips">{"".join(f"<span>{t}</span>" for t in tags)}</div></div></details>""" for c, n, ic, school, short, longd, tags in TERTIARY)
    colors = ["red-v", "sun-v", "royal-v", "ink-v", "white-v"]
    strands = "".join(f"""<div class="tarp {colors[i]}" data-unfurl>{TIES2}{GROM}<span class="k">{k}</span><h3>{n}</h3><p>{d}</p>{("<ul>" + "".join(f"<li>{s}</li>" for s in sp) + "</ul>") if sp else ""}</div>""" for i, (k, n, t, d, sp) in enumerate(SHS))
    basic = "".join(f'<div class="note-card {["blue","yellow","pinkish"][i]}" style="--r:{[-1.5,1,-.6][i]}deg" data-pin><span class="pin" aria-hidden="true"></span><span class="big">{k}</span><h3>{n}</h3><p>{d}</p></div>' for i, (k, n, d) in enumerate(BASIC))
    body = phero("Academics", ["Every stage,", "<span class='sun'>one school</span>"],
                 "Basic Education, Senior High School and eight college degrees, taught on campus, online or blended.", "royal-v", None, "cut-vr.webp") + f"""
<section class="sec on-white" id="tertiary"><div class="wrap">
  <div class="head"><h2 data-letters>College degrees</h2><p class="lede">Theory in class, mastery in the laboratory, kitchen and field. Open a programme to read more.</p></div>
  <div class="board">{ter}</div>
</div></section>
<section class="sec" id="shs"><div class="wrap">
  <div class="head"><h2 data-letters>Senior High tracks</h2><p class="lede">Five ways to prepare for college, a career or a business, including TESDA National Certification for TVL-HE.</p></div>
  <div class="strands">{strands}</div>
</div></section>
<section class="sec on-cork" id="basic"><div class="wrap">
  <div class="head"><h2 data-letters>Basic Education</h2><p class="lede">Nursery to Grade 10, with care, curiosity and a proper school uniform.</p></div>
  <div class="split top"><div class="wall" style="columns:1">{basic}</div>
  <div class="deal-figs" style="min-height:420px"><img src="img/cut-girl.webp" alt="Girl in the St. Clare Basic Education uniform" width="254" height="786" loading="lazy" style="max-height:480px"><img src="img/cut-boy.webp" alt="Boy in the St. Clare Basic Education uniform" width="260" height="767" loading="lazy" style="max-height:470px"></div></div>
</div></section>
""" + closer("Find your path", "Talk to admissions about the programme that fits your goals.")
    page("academics.html", "Academics | St. Clare College Programmes",
         "College degrees (BSCS, BSHM, BSTM, BSBA, BEEd, BSEd, AB PolSci), Senior High tracks (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and Basic Education at St. Clare College.", body)


def build_admissions():
    tabs, sheets = [], []
    for i, (k, (label, ab, items)) in enumerate(REQ.items()):
        sel = i == 0
        tabs.append(f'<button role="tab" id="rt-{k}" aria-controls="rp-{k}" aria-selected="{"true" if sel else "false"}"{"" if sel else " tabindex=\"-1\""} data-hash="{k}">{label}</button>')
        sheets.append(f'<div class="req-sheet" role="tabpanel" id="rp-{k}" aria-labelledby="rt-{k}"{"" if sel else " hidden"}><span class="rubber royal">Long brown envelope</span><h3>{label}</h3>{checklist(items)}</div>')
    forms = "".join(f'<li><a href="{SRC}/downloadable-forms" rel="noopener"><span class="ext{" doc" if e == "DOC" else ""}">{e}</span><span><b>{n}</b><small>{c}</small></span><span class="arr" aria-hidden="true">&darr;</span></a></li>' for e, n, c in FORMS)
    faq = [
        ("Can I study fully online?", "Yes. St. Clare College offers two modalities: full online and blended (online plus on-campus days). Choose one when you enroll."),
        ("How do I get my class schedule?", "After paying the matriculation fee and filling up your registration form, go to the Library on the 3rd floor for enlistment at stclareonline.com/ims. Your section and schedule are posted on the website and emailed by your Program Head."),
        ("Are there scholarships?", "Ask the admissions office for this school year's offers. Submit a certificate of indigency with your requirements for scholarship consideration. UniFAST-TES grantees can verify their status and disbursement schedule on the PMS."),
        ("How do I request my Transcript of Records or diploma?", "Only through the Official Document Request Portal on the Personal Management System (PMS). Do not transact with fixers."),
        ("When is the admissions office open?", f"9:00 AM to 5:00 PM. Call {PHONE} or email {EMAIL}."),
    ]
    faqs = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in faq)
    body = phero("Admissions", ["Enroll", "<span class='sun'>with ease</span>"],
                 "Three stops on campus, one brown envelope, and you're a Clarean.", "red-v", None, "cut-girl.webp",
                 f'<div class="hero-actions" style="margin-top:26px"><a class="tag-btn" href="{SRC}/ims" rel="noopener">Enroll online (IMS) {ARROW}</a><a class="plain" style="color:#fff;font-weight:700" href="#requirements">What to bring</a></div>') + route_section("Three stops on campus") + f"""
<section class="sec" id="requirements"><div class="wrap">
  <div class="head"><h2 data-letters>What to bring</h2><p class="lede">Pick your level. All documents become property of the school once submitted for admission.</p></div>
  <div class="req-tabs" role="tablist" aria-label="Requirement type">{"".join(tabs)}</div>
  {"".join(sheets)}
</div></section>
<section class="sec on-royal on-dark" id="modality"><div class="wrap">
  <div class="head"><h2 data-letters>Full online or blended</h2><p class="lede">Personalized learning pathways: choose the modality that fits your life.</p></div>
  <div class="vm">
    <div class="tarp sun-v" data-unfurl>{TIES2}{GROM}<h3>Full online</h3><p>Learn from anywhere through St. Clare Online: LMS classes, the e-Library and virtual broadcasts.</p></div>
    <div class="tarp white-v" data-unfurl>{TIES2}{GROM}<h3 class="red">Blended</h3><p>Combine online learning with on-campus days in air-conditioned classrooms with e-boards, laboratories and the Virtual Lab.</p></div>
  </div>
</div></section>
<section class="sec on-cork" id="scholarships"><div class="wrap">
  <div class="head"><h2 data-letters>Scholarships</h2><p class="lede">&ldquo;An investment in knowledge pays the best interest.&rdquo; Benjamin Franklin</p></div>
  <div class="wall">
    <div class="note-card" style="--r:-1.5deg" data-pin><span class="pin" aria-hidden="true"></span><span class="rubber red" style="float:right">SY 2024-2025</span><h3>President's Scholarship</h3><p>Offered to the St. Clare SHS Class of 2024, with zero down payment.</p></div>
    <div class="note-card yellow" style="--r:1deg" data-pin><span class="pin b" aria-hidden="true"></span><h3>UniFAST-TES</h3><p>Tertiary Education Subsidy grantees verify their status and disbursement schedule on the PMS.</p><a class="more" href="{SRC}/pms" rel="noopener">Go to PMS</a></div>
    <div class="note-card blue" style="--r:-.8deg" data-pin><span class="pin y" aria-hidden="true"></span><h3>Certificate of indigency</h3><p>Optional. Submit it with your requirements to be considered for scholarship.</p></div>
  </div>
</div></section>
<section class="sec on-white"><div class="wrap split top">
  <div><h2 data-letters>Forms</h2><p class="lede" style="margin:18px 0 26px">Institutional forms, guidelines and memoranda on St. Clare Online.</p><ul class="files">{forms}</ul></div>
  <div><h2 data-letters>Good to know</h2><div class="faq" style="margin-top:26px">{faqs}</div></div>
</div></section>
<section class="sec-tight"><div class="wrap split">
  <div><h2 data-letters>The uniform</h2><p class="lede" style="margin-top:18px">Pre-school to Grade 10 learners wear the official St. Clare College uniform.</p></div>
  <div class="deal-figs" style="min-height:380px"><img src="img/cut-girl.webp" alt="Girl in the St. Clare Basic Education uniform" width="254" height="786" loading="lazy" style="max-height:430px"><img src="img/cut-boy.webp" alt="Boy in the St. Clare Basic Education uniform" width="260" height="767" loading="lazy" style="max-height:420px"></div>
</div></section>
""" + closer("Your turn", "Take the first step towards a brighter tomorrow.")
    page("admissions.html", "Admissions | Enroll at St. Clare College",
         "How to enroll at St. Clare College: three steps on campus, requirements for college freshmen, transferees, Basic Education and SHS, scholarships and forms.", body)


def build_campus():
    ev = "".join(f'<div class="ev"><span class="d">{m} {dd}</span><div><h3>{h}</h3><p>{p}</p></div><span class="w">{w}</span></div>' for m, dd, h, p, w in EVENTS)
    hb = "".join(f'<li><a href="{SRC}/cms" rel="noopener"><span class="ext">PDF</span><span><b>{h}</b><small>Handbooks &amp; manuals</small></span><span class="arr" aria-hidden="true">&darr;</span></a></li>' for h in HANDBOOKS)
    body = phero("Campus life", ["Life on", "<span class='sun'>campus</span>"],
                 "E-boards in every classroom, a Virtual Lab, our own channels, and a community that keeps learning online.", "ink-v", "virtual-lab-predator.jpg") + f"""
<section class="sec on-sun" id="virtual-lab"><div class="wrap">{VLAB}</div></section>
<section class="sec on-red on-dark"><div class="wrap">
  <div class="head"><h2 data-letters>SCO Online channels</h2><p class="lede">Broadcasting and Teacher-DJs are part of the St. Clare Online Education System, from the Monday virtual flag ceremony to commencement exercises.</p></div>
  {flags_html()}
</div></section>
<section class="sec on-white"><div class="wrap split">
  <figure class="photo-print" style="--r:1.5deg" data-pin><span class="pin b" aria-hidden="true"></span><img src="img/campus-building.jpg" alt="St. Clare College campus building" width="1600" height="900" loading="lazy"><figcaption>The campus on Zabarte Road</figcaption></figure>
  <div><h2 data-letters>Built for focus</h2><ul class="ticks"><li>E-boards in all 95 classrooms</li><li>Air-conditioned classrooms and restrooms</li><li>Computer laboratories for programming and networking</li><li>Library and enlistment area on the 3rd floor</li><li>St. Clare Virtual Studio for webinars and broadcasts</li></ul></div>
</div></section>
<section class="sec on-ink on-dark"><div class="wrap">
  <div class="head"><h2 data-letters>On the calendar</h2><p class="lede">Key dates for students, parents and faculty. <a href="{SRC}/calendar" rel="noopener">Full calendar</a></p></div>
  <div class="events">{ev}</div>
</div></section>
<section class="sec" id="digital-citizenship"><div class="wrap split top">
  <div><h2 data-letters>Digital citizenship</h2><p class="lede" style="margin-top:18px">Online learning comes with responsibilities. These policies guide life on St. Clare Online.</p></div>
  <ul class="files">{hb}</ul>
</div></section>
""" + closer("See it yourself", "Tour the campus on Zabarte Road. We're open 9:00 AM to 5:00 PM.")
    page("campus-life.html", "Campus Life | Virtual Lab, SCO Online & Events",
         "The St. Clare College Virtual Lab (VR + AR = MR), SCO Online channels, campus facilities, calendar and digital citizenship.", body)


def build_portals():
    keys = "".join(f'<a class="key" href="{SRC}/{slug}" rel="noopener"><b>{k}</b><h3>{n}</h3><p>{d}</p><span class="go">Open {k}</span></a>' for k, n, d, slug in PORTALS)
    quick = [("Enroll and enlist online", "Students: register for your section and schedule.", "ims", "yellow"),
             ("Faculty attendance", "Basic Ed, SHS and Tertiary attendance monitoring.", "ims", ""),
             ("Official Document Request Portal", "Transcripts, diplomas and other documents. No fixers.", "pms", "pinkish"),
             ("Enrollment status and sections", "College corner and the Program Heads directory.", "lms", "blue"),
             ("e-Library", "Learning Resource Center, powered by ProQuest.", "cms", "yellow"),
             ("Virtual flag ceremony", "Every Monday, 7:00 AM, plus commencement broadcasts.", "vms", "")]
    qs = "".join(f'<a class="note-card {c}" style="--r:{[-1.2,.8,-.5,1.1,-.9,.6][i]}deg" href="{SRC}/{s}" rel="noopener" data-pin><span class="pin{" b" if i % 2 else ""}" aria-hidden="true"></span><span class="meta">{s.upper()}</span><h3>{h}</h3><p>{p}</p><span class="more">Open</span></a>' for i, (h, p, s, c) in enumerate(quick))
    body = phero("Portals", ["St. Clare", "<span class='sun'>Online</span>"],
                 "Five connected systems for learning, content, enrollment, personal transactions and virtual broadcasting.", "red-v") + f"""
<section class="sec"><div class="wrap">
  <div class="head"><h2 data-letters>Grab your key</h2><p class="lede">Each system opens on stclareonline.com.</p></div>
  <div class="keys">{keys}</div>
</div></section>
<section class="sec on-cork"><div class="wrap">
  <div class="head"><h2 data-letters>Most requested</h2><p class="lede">Shortcuts for students, parents and faculty.</p></div>
  <div class="wall">{qs}</div>
</div></section>
""" + closer("Need a hand?", f"Call {PHONE} or email {EMAIL}, 9:00 AM to 5:00 PM.")
    page("portals.html", "St. Clare Online Portals | LMS, CMS, IMS, PMS, VMS",
         "Access the St. Clare Online Education System: Learning, Content, Institutional, Personal and Virtual Management Systems.", body)


def build_news():
    cols = ["", "yellow", "blue", "pinkish"]
    cards = []
    for i, (date, cat, h, p, img, gen, link) in enumerate(NEWS):
        top = f'<img src="img/{img}" alt="" loading="lazy" width="1230" height="640">' if img else f'<span class="big">{esc(gen if gen != "mace" else "Mace")}</span>'
        cards.append(f'<a class="note-card {cols[i % 4]}" style="--r:{[-1.4,1,-.6,1.3,-1,.7,-1.2,.9,-.4][i]}deg" href="{link}" rel="noopener" data-pin><span class="pin{["", " y", " b"][i % 3]}" aria-hidden="true"></span>{top}<span class="meta">{cat} &middot; {date}</span><h3>{h}</h3><p>{p}</p><span class="more">Read more</span></a>')
    body = phero("News", ["News &amp;", "<span class='sun'>notices</span>"],
                 "Milestones, scholarships, advisories and stories from the St. Clare community.", "royal-v") + f"""
<section class="sec on-cork"><div class="wrap"><h2 class="sr-only">Latest notices</h2><div class="wall">{"".join(cards)}</div></div></section>
<section class="sec on-red on-dark"><div class="wrap">{flags_html()}</div></section>
""" + closer("Be a Clarean", "Basic Education, Senior High School and College, on campus or online.")
    page("news.html", "News | St. Clare College", "Latest news, scholarships, advisories and events from St. Clare College of Caloocan.", body)


def build_contact():
    body = phero("Contact", ["Let's talk", "<span class='sun'>enrollment</span>"],
                 "Questions about programmes, requirements or scholarships? We're here 9:00 AM to 5:00 PM.", "red-v", None, "cut-boy.webp") + f"""
<section class="sec on-ink on-dark"><div class="wrap split top">
  <div class="addr">
    <h2 data-letters>Visit, call, write</h2>
    <div><b>Campus</b>{ADDRESS}</div>
    <div><b>Phone</b><a href="tel:{PHONE_TEL}">{PHONE}</a></div>
    <div><b>Email</b><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    <div><b>Office hours</b>9:00 AM - 5:00 PM</div>
    <div class="socials"><a href="{FB}" rel="noopener" aria-label="Facebook">{FB_SVG}</a><a href="{YT}" rel="noopener" aria-label="YouTube">{YT_SVG}</a></div>
  </div>
  <form class="regform" data-mailto="{EMAIL}">
    <div class="rf-head"><b>Inquiry form</b><img src="img/seal-200.webp" alt="" width="54" height="54"></div>
    <div class="rf-grid">
      <div class="rf"><label for="f-name">Full name</label><input id="f-name" name="Name" autocomplete="name" required></div>
      <div class="rf"><label for="f-email">Email</label><input id="f-email" name="Email" type="email" autocomplete="email" required></div>
      <div class="rf"><label for="f-level">Interested in</label><select id="f-level" name="Level"><option>Basic Education</option><option>Senior High School</option><option selected>College</option><option>Other</option></select></div>
      <div class="rf"><label for="f-src">Where did you hear about us?</label><select id="f-src" name="Source"><option>Facebook</option><option>YouTube</option><option>Friend or family</option><option>Search</option><option>Other</option></select></div>
      <div class="rf full"><label for="f-sub">Subject</label><input id="f-sub" name="subject" value="Enrollment inquiry"></div>
      <div class="rf full"><label for="f-msg">Message</label><textarea id="f-msg" name="Message" required></textarea></div>
    </div>
    <div class="rf-foot"><button class="tag-btn red-t" type="submit">Send inquiry {ARROW}</button><p>Opens your email app, addressed to {EMAIL}.</p><p class="form-status" role="status"></p></div>
  </form>
</div></section>
<section class="sec-tight"><div class="wrap">
  <div class="map"><iframe title="Map to St. Clare College of Caloocan" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=St.+Clare+College+of+Caloocan,+Zabarte+Road,+Caloocan+City&output=embed"></iframe></div>
</div></section>
"""
    page("contact.html", "Contact St. Clare College | Caloocan City",
         f"Contact St. Clare College of Caloocan: {ADDRESS}. Phone {PHONE}, email {EMAIL}, 9:00 AM - 5:00 PM.", body)


if __name__ == "__main__":
    build_home(); build_about(); build_academics(); build_admissions()
    build_campus(); build_portals(); build_news(); build_contact()
