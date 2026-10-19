# St. Clare College website - "Collegiate" (corporate college) builder. Run: python build.py
import os, html
from data import *

V = "11"

def esc(s): return html.escape(s, quote=True)

ICON = {
    "book": '<path d="M4 5a2 2 0 0 1 2-2h12v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/><path d="M8 7h7"/>',
    "steps": '<path d="M4 20h4v-4h4v-4h4V8h4"/><path d="M4 4v16"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6h.01M4 12h.01M4 18h.01"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M10.8 12.2 20 3M16 7l3 3M18 5l2 2"/>',
}
def icon(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[n]}</svg>'

def img(name, alt, w, h, lazy=True, sizes="(max-width: 900px) 100vw, 50vw", cls=""):
    base = name.rsplit(".", 1)[0]
    ss = f' srcset="img/{base}-800.webp 800w, img/{name} {w}w" sizes="{sizes}"' if os.path.exists(os.path.join(OUT, "img", base + "-800.webp")) else ""
    return f'<img src="img/{name}"{ss} alt="{esc(alt)}" width="{w}" height="{h}"{" loading=\"lazy\"" if lazy else " fetchpriority=\"high\""}{f" class=\"{cls}\"" if cls else ""}>'

def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#0b2265">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="img/campus-building.jpg">
<link rel="icon" href="img/seal.svg" type="image/svg+xml">
<link rel="icon" href="img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preload" href="fonts/jakarta.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/college.css?v={V}">
<script src="assets/college.js?v={V}" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""

def header(page):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>' for h, t in NAV if h not in ("index.html", "portals.html"))
    return f"""<div class="util"><div class="wrap">
  <div class="l"><a href="tel:{PHONE_TEL}">{PHONE}</a><a class="hide-sm" href="mailto:{EMAIL}">{EMAIL}</a></div>
  <div class="r"><b class="hide-sm">Students &amp; faculty:</b><a href="portals.html">St. Clare Online portals</a><a href="{SRC}/lms" rel="noopener">LMS</a><a href="{SRC}/ims" rel="noopener">IMS</a></div>
</div></div>
<header class="head"><div class="wrap">
  <a class="brand" href="index.html" aria-label="St. Clare College of Caloocan, home">
    <img src="img/seal.svg" alt="" width="56" height="56">
    <span><b>St. Clare College</b><small>of Caloocan &middot; The School of Life Skills</small></span>
  </a>
  <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn" href="admissions.html">How to enroll</a></nav>
  <button class="menu-btn" aria-expanded="false" aria-controls="nav"><i aria-hidden="true"></i><span>Menu</span></button>
</div></header>
<main id="main">
"""

def footer():
    portals = "".join(f'<li><a href="{SRC}/{p[3]}" rel="noopener">{p[0]}: {p[1]}</a></li>' for p in PORTALS)
    return f"""</main>
<footer class="foot on-navy">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="fb"><img src="img/seal.svg" alt="" width="64" height="64"><b>St. Clare College<br>of Caloocan</b></div>
        <p>The School of Life Skills. Serving Caloocan since 1985; online through St. Clare Online since 2020.</p>
        <div class="socials"><a href="{FB}" rel="noopener" aria-label="St. Clare College on Facebook">{FB_SVG}</a><a href="{YT}" rel="noopener" aria-label="St. Clare College on YouTube">{YT_SVG}</a></div>
      </div>
      <div><h3>The college</h3><ul><li><a href="about.html">About St. Clare</a></li><li><a href="academics.html">Academics</a></li><li><a href="admissions.html">Admissions</a></li><li><a href="campus-life.html">Campus life</a></li><li><a href="news.html">News</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h3>St. Clare Online</h3><ul>{portals}<li><a href="{SRC}/downloadable-forms" rel="noopener">Downloadable forms</a></li></ul></div>
      <div><h3>Visit</h3><ul><li><a href="contact.html">{ADDRESS}</a></li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li></ul><p class="mt">Office hours 9:00 AM - 5:00 PM</p></div>
    </div>
    <div class="foot-bottom"><span>&copy; <span data-year>2026</span> St. Clare College of Caloocan &middot; St. Clare Online Education System&reg;</span><a href="https://sdgs.un.org/goals/goal4" rel="noopener" style="color:inherit">UN SDG 4: Quality Education</a></div>
  </div>
</footer>
</body>
</html>
"""

def page(name, title, desc, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(head(title, desc) + header(name) + body + footer())
    print("wrote", name)

def sec(inner, cls="", id_=None):
    i = f' id="{id_}"' if id_ else ""
    return f'<section class="sec {cls}"{i}><div class="wrap">{inner}</div></section>\n'

def shead(title, lede="", solo=False):
    return f'<div class="sec-head{" solo" if solo or not lede else ""} rv"><div><h2>{title}</h2></div>{f"<p class=\"lede\">{lede}</p>" if lede else ""}</div>'

def ph(crumb, title, lede, photo=None, alt="", extra=""):
    pic = f'<div class="ph-img">{img(photo, alt, 1600, 900, lazy=False, sizes="(max-width: 900px) 0px, 40vw")}</div>' if photo else "<div></div>"
    return f"""<section class="ph on-navy">
  <img class="seal-watermark" src="img/seal.svg" alt="" width="420" height="420">
  <div class="wrap">
    <div><p class="crumbs"><a href="index.html">Home</a> / {crumb}</p><span class="rule" aria-hidden="true"></span><h1>{title}</h1><p class="lede">{lede}</p>{extra}</div>
    {pic}
  </div>
</section>
"""

def cta(title="Begin your journey at St. Clare", line="Basic Education, Senior High School and College, on campus or fully online."):
    return sec(f"""<div class="cta on-navy rv"><h2>{title}</h2><p class="lede">{line}</p>
  <div class="actions"><a class="btn gold" href="admissions.html">How to enroll {ARROW}</a><a class="btn line" href="contact.html">Contact admissions</a></div></div>""", "navy")

def steps_html():
    items = "".join(f'<li class="rv" style="--d:{i}"><h3>{h}</h3><p class="where">Where: {w}</p><ul>{"".join(f"<li>{x}</li>" for x in its)}</ul></li>' for i, (h, w, its) in enumerate(STEPS))
    return f'<ol class="steps">{items}</ol><p class="next rv"><b>What happens next:</b> your Program Head posts your section and schedule on the website and emails them to you. Call {PHONE} to confirm this school year\'s enrollment dates and fees.</p>'

def checklist(items): return '<ul class="checklist">' + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>"

def levels_html():
    col = "".join(f'<li><a href="academics.html#tertiary"><b>{c}</b>{n.replace("Bachelor of Science in ", "BS ").replace("Bachelor of Secondary Education, ", "Secondary Education, ").replace("Bachelor of Elementary Education", "Elementary Education").replace("Bachelor of Arts in ", "AB ")}</a></li>' for c, n, *_ in TERTIARY)
    shs = "".join(f'<li><a href="academics.html#shs"><b>{k}</b>{n}</a></li>' for k, n, *_ in SHS)
    bas = "".join(f'<li><a href="academics.html#basic"><b>{k}</b>{n}</a></li>' for k, n, _ in BASIC)
    return f"""<div class="levels">
  <div class="level rv"><h3>College</h3><p class="sub">Eight bachelor's degree programmes</p><ul class="plist">{col}</ul><a class="more" href="academics.html#tertiary">College programmes</a></div>
  <div class="level rv" style="--d:1"><h3>Senior High School</h3><p class="sub">Academic, Arts &amp; Design and TVL tracks</p><ul class="plist">{shs}</ul><a class="more" href="academics.html#shs">Senior High tracks</a></div>
  <div class="level rv" style="--d:2"><h3>Basic Education</h3><p class="sub">Nursery to Grade 10</p><ul class="plist">{bas}</ul><a class="more" href="academics.html#basic">Basic Education</a></div>
</div>"""

FACTS = """<dl class="facts">
  <div><dt>1985</dt><dd>Founded 31 August in Caloocan City</dd></div>
  <div><dt>95</dt><dd>Classrooms, every one with an e-board</dd></div>
  <div><dt>38th</dt><dd>Commencement exercises, June 2024</dd></div>
  <div><dt>2</dt><dd>Learning modalities: full online or blended</dd></div>
</dl>"""

VM = """<div class="grid2">
  <div class="panel rv"><h3>Vision</h3><p>To become the leading institution for professional development and the first and foremost provider of quality, affordable and sustainable development education.</p></div>
  <div class="panel rv" style="--d:1"><h3>Mission</h3><p>To provide quality and excellent global education for the total development of a responsible, innovative, skillful and professional global workforce whose values and dignity are beyond par.</p></div>
</div>"""

def news_cards(items):
    out = []
    for i, (date, cat, h, p, im, gen, link) in enumerate(items):
        th = f'<div class="thumb">{img(im, "", 1230, 640)}</div>' if im else ""
        out.append(f'<a class="post rv{"" if im else " text"}" style="--d:{i % 3}" href="{link}" rel="noopener">{th}<h3>{h}</h3><p>{p}</p><span class="date">{date} &middot; {cat}</span></a>')
    return f'<div class="news">{"".join(out)}</div>'

# ---------------------------------------------------------------- pages
def build_home():
    quick = [("academics.html", "book", "Programmes", "College, SHS, Basic Ed"), ("admissions.html#steps", "steps", "How to enroll", "Three steps on campus"),
             ("admissions.html#requirements", "list", "Requirements", "What to bring"), ("portals.html", "key", "Student portals", "LMS, IMS, PMS and more")]
    q = "".join(f'<li><a href="{h}">{icon(i)}<span><b>{t}</b><small>{s}</small></span></a></li>' for h, i, t, s in quick)
    body = f"""<section class="hero on-navy">
  <div class="hero-img">{img("campus-building.jpg", "", 1600, 900, lazy=False, sizes="100vw")}</div>
  <div class="wrap"><div class="hero-card">
    <span class="rule" aria-hidden="true"></span><h1>The School of Life Skills</h1>
    <p class="lede">St. Clare College of Caloocan educates learners from Nursery to College, on one campus in Caloocan City and online through St. Clare Online.</p>
    <div class="actions"><a class="btn" href="admissions.html">How to enroll {ARROW}</a><a class="btn line" href="academics.html">Explore programmes</a></div>
  </div></div>
</section>
<nav class="quick" aria-label="Quick access"><ul class="wrap">{q}</ul></nav>
""" + sec(shead("Academic programmes", "From a child's first school day to a bachelor's degree, every stage of learning happens at St. Clare.") + levels_html()) \
        + sec(f"""<div class="split">
  <div class="rv"><h2>A college built for professional life</h2>
    <p class="lede mt">St. Clare aims to be the leading institution for professional development, with lessons on e-boards, laboratories for hands-on practice and a Virtual Lab for mixed reality.</p>
    {FACTS}
    <p class="mt-l"><a class="more" href="about.html">About St. Clare</a></p></div>
  <figure class="photo rv" style="--d:1">{img("virtual-lab-predator.jpg", "Predator stations in the St. Clare Virtual Lab", 1600, 1066)}<figcaption>The St. Clare Virtual Lab: VR + AR = mixed reality</figcaption></figure>
</div>""", "alt") \
        + sec(shead("How to enroll", "Bring your requirements in a long brown envelope and complete three steps on campus.") + steps_html() + '<div class="actions mt-l rv"><a class="btn" href="admissions.html#requirements">See the requirements</a><a class="btn line" href="admissions.html">Admissions</a></div>') \
        + sec(f"""<div class="split rev">
  <div class="rv"><h2>Learning that continues online</h2>
    <p class="lede mt">St. Clare Online connects learning, the e-Library, enrollment and broadcasting in one platform, so students can study fully online or blended.</p>
    <ul class="checklist" style="columns:1;margin-top:18px"><li>LMS for schedules, materials and progress</li><li>e-Library powered by ProQuest</li><li>Virtual flag ceremony every Monday, 7:00 AM</li></ul>
    <p class="mt"><a class="more" href="portals.html">St. Clare Online portals</a></p></div>
  <figure class="photo rv" style="--d:1">{img("campus-building.jpg", "St. Clare College building with the SCO Online sign", 1600, 900)}<figcaption>Zabarte Road, Caloocan City</figcaption></figure>
</div>""", "alt") \
        + sec(shead("News and announcements") + news_cards(NEWS[:3]) + '<p class="mt-l rv"><a class="more" href="news.html">All news</a></p>') \
        + sec(f'<div class="banner rv">{img("graduates.jpg", "St. Clare College graduates at the 2024 commencement", 1230, 640, sizes="100vw")}<div class="txt"><h2>Congratulations, Stars of 2024</h2><p>St. Clare College held its 38th Commencement Exercises in June 2024.</p></div></div>', "tight") \
        + cta()
    page("index.html", "St. Clare College of Caloocan | The School of Life Skills",
         "St. Clare College of Caloocan: Nursery to College, full online or blended. BSCS, BSHM, BSTM, BSBA, BEEd, BSEd, AB Political Science and Senior High tracks.", body)


def build_about():
    tl = [
        ("1985", "St. Clare College is founded", "Founded on 31 August 1985 in Caloocan City, Metro Manila, as a school of life skills."),
        ("2020", "St. Clare Online keeps learning going", "During the pandemic the college moved classes to its own online platform so no student got left behind. UniFAST-TES applications opened for A.Y. 2020-2021."),
        ("2021", "The Virtual Lab and the 36th anniversary", "The Virtual Lab (VR + AR = MR) opened, Teacher-DJs went live on Zoom Monday to Saturday, and the college marked its 36th founding anniversary."),
        ("2023", "The Professional Mace", "On 23 September 2023 St. Clare College introduced its Professional Mace, “the eternal flame of professionalism” and “a beacon of professionalism and culture of excellence.”"),
        ("2024", "The Stars of 2024", "The 38th Commencement Exercises, and the President's Scholarship with zero down payment for the SHS Class of 2024."),
    ]
    tlh = "".join(f'<li class="rv"><span class="y">{y}</span><h3>{h}</h3><p>{p}</p></li>' for y, h, p in tl)
    fac = ["E-boards in all 95 classrooms", "Air-conditioned classrooms and restrooms", "Virtual Lab with Acer Mixed Reality", "Computer laboratories", "Library and Learning Resource Center, 3rd floor", "St. Clare Virtual Studio"]
    body = ph("About", "Transforming education, building our future", "St. Clare College of Caloocan is the School of Life Skills and a leading institution for professional development, serving Caloocan since 1985.", "campus-building.jpg", "St. Clare College building on Zabarte Road") \
        + sec(shead("Vision and mission", "Quality, affordable and sustainable education for the total development of every Clarean.") + VM) \
        + sec(f"""<div class="split"><div class="rv"><h2>Our campus</h2><ul class="checklist" style="columns:1;margin-top:18px">{"".join(f"<li>{x}</li>" for x in fac)}</ul></div>
  <figure class="photo rv" style="--d:1">{img("virtual-lab-predator.jpg", "The St. Clare Virtual Lab", 1600, 1066)}<figcaption>Virtual Lab, opened 2021</figcaption></figure></div>""", "alt") \
        + sec(f'<div class="split" style="align-items:start"><div class="rv"><h2>Milestones</h2><p class="lede mt">Four decades of firsts for Caloocan.</p></div><ol class="timeline">{tlh}</ol></div>') \
        + sec(f"""<div class="split"><div class="rv"><h2>No one gets left behind</h2></div>
  <div class="rv"><p class="lede">When colleges around the world moved to online and open distance learning, St. Clare's own platform made sure its students could continue and finish their education.</p><a class="more" href="portals.html">St. Clare Online portals</a></div></div>""", "alt") \
        + cta("Visit the campus", "Zabarte Road, Caloocan City. Office hours 9:00 AM to 5:00 PM.")
    page("about.html", "About St. Clare College | Vision, Mission & History",
         "Founded in 1985 in Caloocan City, St. Clare College is the School of Life Skills: vision, mission, milestones and campus.", body)


def build_academics():
    ter = "".join(f"""<details class="rv"><summary><span class="c">{c}</span><span class="t">{n}<small>{school}</small></span><span class="pm" aria-hidden="true"></span></summary>
<div class="body"><p>{short} {longd}</p><div class="chips">{"".join(f"<span>{t}</span>" for t in tags)}</div></div></details>""" for c, n, ic, school, short, longd, tags in TERTIARY)
    shs = "".join(f'<div class="panel rv" style="--d:{i % 3}"><span class="tag">{k}</span><h3>{n}</h3><p>{d}</p>{("<ul>" + "".join(f"<li>{s}</li>" for s in sp) + "</ul>") if sp else ""}</div>' for i, (k, n, t, d, sp) in enumerate(SHS))
    bas = "".join(f'<div class="panel rv" style="--d:{i}"><span class="tag">{k}</span><h3>{n}</h3><p>{d}</p></div>' for i, (k, n, d) in enumerate(BASIC))
    body = ph("Academics", "Programmes for every stage", "Basic Education, Senior High School and eight college degrees, taught on campus, online or blended.", "virtual-lab-predator.jpg", "The St. Clare Virtual Lab") \
        + sec(shead("College degrees", "Theory in class, mastery in the laboratory, kitchen and field. Select a programme for details.") + f'<div class="acc">{ter}</div>', "", "tertiary") \
        + sec(shead("Senior High School tracks", "Five ways to prepare for college, a career or a business, including TESDA National Certification for TVL-HE.") + f'<div class="grid3">{shs}</div>', "alt", "shs") \
        + sec(shead("Basic Education", "Nursery to Grade 10, with care, curiosity and the official St. Clare uniform.") + f'<div class="grid3">{bas}</div>', "", "basic") \
        + cta("Find the right programme", "Talk to admissions about the programme that fits your goals.")
    page("academics.html", "Academics | St. Clare College Programmes",
         "College degrees (BSCS, BSHM, BSTM, BSBA, BEEd, BSEd, AB PolSci), Senior High tracks (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and Basic Education at St. Clare College.", body)


def build_admissions():
    tabs, panels = [], []
    for i, (k, (label, ab, items)) in enumerate(REQ.items()):
        sel = i == 0
        tabs.append(f'<button role="tab" id="rt-{k}" aria-controls="rp-{k}" aria-selected="{"true" if sel else "false"}"{"" if sel else " tabindex=\"-1\""} data-hash="{k}">{label}</button>')
        panels.append(f'<div role="tabpanel" id="rp-{k}" aria-labelledby="rt-{k}"{"" if sel else " hidden"}>{checklist(items)}</div>')
    forms = "".join(f'<li><a href="{SRC}/downloadable-forms" rel="noopener"><span class="ext">{e}</span><span><b>{n}</b><small>{c}</small></span><span class="arr" aria-hidden="true">&darr;</span></a></li>' for e, n, c in FORMS)
    faq = [
        ("Can I study fully online?", "Yes. St. Clare College offers two modalities: full online and blended (online plus on-campus days). Choose one when you enroll."),
        ("How do I get my class schedule?", "After paying the matriculation fee and filling up your registration form, go to the Library on the 3rd floor for enlistment at stclareonline.com/ims. Your section and schedule are posted on the website and emailed by your Program Head."),
        ("When does enrollment open, and how much are the fees?", f"Call the admissions office at {PHONE} or email {EMAIL} to confirm this school year's enrollment dates and fees before your visit."),
        ("Are there scholarships?", "Ask the admissions office for this school year's offers. Submit a certificate of indigency with your requirements for scholarship consideration. UniFAST-TES grantees can verify their status and disbursement schedule on the PMS."),
        ("How do I request my Transcript of Records or diploma?", "Only through the Official Document Request Portal on the Personal Management System (PMS). Do not transact with fixers."),
    ]
    faqs = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in faq)
    body = ph("Admissions", "Enroll at St. Clare", "Three steps on campus, one long brown envelope of requirements, and you are a Clarean.", "graduates.jpg", "St. Clare College graduates",
              f'<div class="actions"><a class="btn gold" href="#steps">See the 3 steps {ARROW}</a><a class="btn line" href="{SRC}/ims" rel="noopener">Returning students: enlist on IMS</a></div><p class="note-line">Dates and fees for this school year: call <a href="tel:{PHONE_TEL}">{PHONE}</a></p>') \
        + sec(shead("Enrollment procedure", "Proceed in order; each step happens at a specific place on campus.") + steps_html(), "alt", "steps") \
        + sec(shead("Admission requirements", "Select your level. All documents are considered property of the school once submitted for admission.") + f'<div class="tabs" role="tablist" aria-label="Requirement type">{"".join(tabs)}</div>{"".join(panels)}<p class="notebox">Place photocopies of all documents in a long brown envelope.</p>', "", "requirements") \
        + sec(shead("Learning modality", "Personalized learning pathways: choose the modality that fits your life.") + """<div class="grid2">
  <div class="panel rv"><h3>Full online</h3><p>Learn from anywhere through St. Clare Online: LMS classes, the e-Library and virtual broadcasts.</p></div>
  <div class="panel rv" style="--d:1"><h3>Blended</h3><p>Combine online learning with on-campus days in air-conditioned classrooms with e-boards, laboratories and the Virtual Lab.</p></div></div>""", "alt", "modality") \
        + sec(shead("Scholarships and financial aid", "“An investment in knowledge pays the best interest.” Benjamin Franklin") + f"""<div class="grid3">
  <div class="panel rv"><span class="dated">SY 2024-2025</span><h3>President's Scholarship</h3><p>Offered to the St. Clare SHS Class of 2024 with zero down payment. Ask admissions about this year's scholarships.</p></div>
  <div class="panel rv" style="--d:1"><h3>UniFAST-TES</h3><p>Tertiary Education Subsidy grantees verify their status and disbursement schedule on the PMS.</p><p class="mt"><a class="more" href="{SRC}/pms" rel="noopener">Go to PMS</a></p></div>
  <div class="panel rv" style="--d:2"><h3>Certificate of indigency</h3><p>Optional. Submit it with your requirements to be considered for scholarship.</p></div></div>""", "", "scholarships") \
        + sec(f'<div class="split" style="align-items:start"><div class="rv"><h2>Forms</h2><p class="lede mt" style="margin-bottom:22px">Institutional forms, guidelines and memoranda on St. Clare Online.</p><ul class="files">{forms}</ul></div><div class="rv" style="--d:1"><h2>Frequently asked questions</h2><div class="faq mt-l">{faqs}</div></div></div>', "alt") \
        + cta("Ready to enroll?", "Take the first step towards a brighter tomorrow.")
    page("admissions.html", "Admissions | Enroll at St. Clare College",
         "How to enroll at St. Clare College: three steps on campus, requirements for college freshmen, transferees, Basic Education and SHS, scholarships, forms and FAQ.", body)


def build_campus():
    day = [("Monday, 7:00 AM", "Virtual flag ceremony", "The whole community gathers online to start the week."),
           ("Classes", "E-boards in all 95 classrooms", "Air-conditioned classrooms with lessons on e-boards."),
           ("Lab time", "Virtual Lab", "VR + AR = MR with the Predator Thronos and the Mixed Reality facility by Acer, opened in 2021."),
           ("3rd floor", "Library and Learning Resource Center", "Study space, enlistment and the ProQuest-powered e-Library."),
           ("Broadcasts", "St. Clare Virtual Studio", "Webinars, parents' orientations and commencement broadcasts."),
           ("Every week", "SCO Online channels", ", ".join(n for n, _ in CHANNELS) + ".")]
    dh = "".join(f'<div class="panel rv" style="--d:{i % 3}"><span class="where" style="font-size:.78rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--navy-2)">{t}</span><h3 class="mt" style="margin-top:6px">{h}</h3><p>{p}</p></div>' for i, (t, h, p) in enumerate(day))
    ev = "".join(f'<li class="rv"><span class="d">{m} {dd}</span><div><h3>{h}</h3><p>{p}</p></div><span class="w">{w}</span></li>' for m, dd, h, p, w in EVENTS)
    hb = "".join(f'<li><a href="{SRC}/cms" rel="noopener"><span class="ext">PDF</span><span><b>{h}</b><small>Handbooks and manuals</small></span><span class="arr" aria-hidden="true">&darr;</span></a></li>' for h in HANDBOOKS)
    body = ph("Campus life", "Life at St. Clare", "E-boards in every classroom, a Virtual Lab, our own broadcast channels and a community that keeps learning online.", "virtual-lab-predator.jpg", "The St. Clare Virtual Lab") \
        + sec(shead("A week on campus", "From the Monday flag ceremony to the Virtual Studio.") + f'<div class="grid3">{dh}</div>', "", "virtual-lab") \
        + sec(f'<div class="split"><figure class="photo rv">{img("campus-building.jpg", "St. Clare College campus building", 1600, 900)}<figcaption>The campus on Zabarte Road</figcaption></figure><div class="rv" style="--d:1"><h2>Facilities</h2><ul class="checklist" style="columns:1;margin-top:18px"><li>E-boards in all 95 classrooms</li><li>Air-conditioned classrooms and restrooms</li><li>Computer laboratories for programming and networking</li><li>Library and enlistment area on the 3rd floor</li><li>St. Clare Virtual Studio</li></ul></div></div>', "alt") \
        + sec(shead("Calendar", f'Key dates for students, parents and faculty. <a href="{SRC}/calendar" rel="noopener">Full calendar</a>') + f'<ul class="events">{ev}</ul>') \
        + sec(f'<div class="split" style="align-items:start"><div class="rv"><h2>Digital citizenship</h2><p class="lede mt">Online learning comes with responsibilities. These policies guide life on St. Clare Online.</p></div><ul class="files">{hb}</ul></div>', "alt", "digital-citizenship") \
        + cta("See the campus", "Visit Zabarte Road, Caloocan City, 9:00 AM to 5:00 PM.")
    page("campus-life.html", "Campus Life | St. Clare College",
         "Campus life at St. Clare College: the Virtual Lab, e-board classrooms, SCO Online channels, facilities, calendar and digital citizenship.", body)


def build_portals():
    rows = "".join(f'<a class="portal rv" href="{SRC}/{slug}" rel="noopener"><span class="acr">{k}</span><span><h3>{n}</h3><p>{d}</p></span><span class="go">Open {k} &rarr;</span></a>' for k, n, d, slug in PORTALS)
    quick = [("Enroll and enlist online", "Students: register for your section and schedule.", "ims"),
             ("Faculty attendance", "Basic Ed, SHS and Tertiary attendance monitoring.", "ims"),
             ("Official Document Request Portal", "Transcripts, diplomas and other official documents. No fixers.", "pms"),
             ("Enrollment status and sections", "College corner and the Program Heads directory.", "lms"),
             ("e-Library", "Learning Resource Center, powered by ProQuest.", "cms"),
             ("Virtual flag ceremony", "Every Monday, 7:00 AM, plus commencement broadcasts.", "vms")]
    qs = "".join(f'<a class="panel rv" style="--d:{i % 3}" href="{SRC}/{s}" rel="noopener"><span class="tag" style="font-size:.85rem">{s.upper()}</span><h3>{h}</h3><p>{p}</p></a>' for i, (h, p, s) in enumerate(quick))
    body = ph("Portals", "St. Clare Online", "Five connected systems for learning, content, enrollment, personal transactions and virtual broadcasting.") \
        + sec(shead("Systems", "Each system opens on stclareonline.com.") + f'<div class="portal-list">{rows}</div>') \
        + sec(shead("Most requested", "Shortcuts for students, parents and faculty.") + f'<div class="grid3">{qs}</div>', "alt") \
        + cta("Need help?", f"Call {PHONE} or email {EMAIL}, 9:00 AM to 5:00 PM.")
    page("portals.html", "St. Clare Online Portals | LMS, CMS, IMS, PMS, VMS",
         "Access the St. Clare Online Education System: Learning, Content, Institutional, Personal and Virtual Management Systems.", body)


def build_news():
    body = ph("News", "News and announcements", "Milestones, scholarships, advisories and stories from the St. Clare community.") \
        + sec('<h2 class="sr-only">All news</h2>' + news_cards(NEWS)) + cta()
    page("news.html", "News | St. Clare College", "Latest news, scholarships, advisories and events from St. Clare College of Caloocan.", body)


def build_contact():
    body = ph("Contact", "Contact the college", "Questions about programmes, requirements, dates or fees? The admissions office is open 9:00 AM to 5:00 PM.") \
        + sec(f"""<div class="split" style="align-items:start">
  <div class="info rv"><h2>Visit, call or write</h2>
    <dl class="mt-l"><div><dt>Campus</dt><dd>{ADDRESS}</dd></div><div><dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>Messenger</dt><dd><a href="https://m.me/stclarecollege" rel="noopener">St. Clare College on Facebook</a></dd></div><div><dt>Office hours</dt><dd>9:00 AM - 5:00 PM</dd></div></dl>
    <div class="socials"><a href="{FB}" rel="noopener" aria-label="Facebook">{FB_SVG}</a><a href="{YT}" rel="noopener" aria-label="YouTube">{YT_SVG}</a></div></div>
  <form class="form rv" style="--d:1" data-mailto="{EMAIL}">
    <h2 style="font-size:1.4rem;margin-bottom:18px">Send an inquiry</h2>
    <div class="fld-row"><div class="fld"><label for="f-name">Full name <em>(required)</em></label><input id="f-name" name="Name" autocomplete="name" required></div>
    <div class="fld"><label for="f-email">Email <em>(required)</em></label><input id="f-email" name="Email" type="email" autocomplete="email" required></div></div>
    <div class="fld-row"><div class="fld"><label for="f-level">Interested in</label><select id="f-level" name="Level"><option>Basic Education</option><option>Senior High School</option><option selected>College</option><option>Other</option></select></div>
    <div class="fld"><label for="f-src">Where did you hear about us?</label><select id="f-src" name="Source"><option>Facebook</option><option>YouTube</option><option>Friend or family</option><option>Search</option><option>Other</option></select></div></div>
    <div class="fld"><label for="f-sub">Subject</label><input id="f-sub" name="subject" value="Enrollment inquiry"></div>
    <div class="fld"><label for="f-msg">Message <em>(required)</em></label><textarea id="f-msg" name="Message" required></textarea></div>
    <button class="btn" type="submit">Send inquiry {ARROW}</button>
    <p class="hint">Opens your email app, addressed to {EMAIL}. No email app? Call {PHONE}.</p><p class="form-status" role="status"></p>
  </form>
</div>""") + sec('<div class="map rv"><iframe title="Map to St. Clare College of Caloocan" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=St.+Clare+College+of+Caloocan,+Zabarte+Road,+Caloocan+City&output=embed"></iframe></div>', "alt")
    page("contact.html", "Contact St. Clare College | Caloocan City",
         f"Contact St. Clare College of Caloocan: {ADDRESS}. Phone {PHONE}, email {EMAIL}, 9:00 AM - 5:00 PM.", body)


if __name__ == "__main__":
    build_home(); build_about(); build_academics(); build_admissions()
    build_campus(); build_portals(); build_news(); build_contact()
