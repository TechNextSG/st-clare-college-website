# v5 "Crimson University": a designed hero per header page + context-specific sections.
# Student-service pages (LMS, CMS, IMS, PMS, VMS, downloads, calendar, portals) come from pages_full with the crimson banner.
import os, json
import build as B
import pages_full as P
from build import esc, sec, shead, cta, steps_html, checklist, page, lines, ARROW, PHONE, PHONE_TEL, EMAIL, ADDRESS, FB, YT, FB_SVG, YT_SVG
from pages_full import simg, zoom, gallery, yt, vcard, docs
from data import REQ, STEPS
from content import *

def crumbs(name): return f'<p class="crumbs"><a href="index.html">Home</a> / {name}</p>'

def vid_side(t, v, w=""):
    return f'<div class="vid">{yt(v, t)}<div><h3>{esc(t)}</h3>{f"<p class=\"when\">{esc(w)}</p>" if w else ""}</div></div>'

PROGRAM_TICKER = ["BS Hospitality Management", "BS Business Administration", "BS Computer Science", "Bachelor of Elementary Education",
                  "BSEd English", "BSEd Mathematics", "BS Tourism Management", "AB Political Science", "SHS: ABM", "SHS: HUMSS",
                  "SHS: Arts & Design", "SHS: TVL-ICT", "SHS: TVL-HE", "Nursery to Grade 10"]

def theater(items, label):
    """Stage + clickable playlist. items = [(title, video_id, when)]."""
    import html as _h
    items = [(t, v, _h.unescape(w)) for t, v, w in items]
    t0, v0, w0 = items[0]
    pl = "".join(f'<li><button type="button" class="pl{" on" if i == 0 else ""}" data-id="{v}" data-title="{esc(t)}" data-when="{esc(w)}" aria-pressed="{"true" if i == 0 else "false"}"><span class="n">{i + 1:02d}</span><span class="th"><img src="{"img/seal-256.webp" if v in P.NO_THUMB else f"https://i.ytimg.com/vi/{v}/mqdefault.jpg"}" alt="" loading="lazy" width="320" height="180"></span><span class="tx"><b>{esc(t)}</b><small>{esc(w)}</small></span></button></li>' for i, (t, v, w) in enumerate(items))
    return f"""<div class="theater on-dark rv">
  <div class="stage"><div class="frame">{yt(v0, t0)}</div>
    <div class="stage-meta"><span class="now">Now showing &middot; <b class="idx">01</b> / {len(items):02d}</span><h3 class="st-title">{esc(t0)}</h3><p class="when st-when">{esc(w0)}</p></div></div>
  <div class="playlist"><p class="pl-head"><b>{label}</b><span>{len(items)} videos</span></p><ol>{pl}</ol></div>
</div>"""

def ticker():
    items = "".join(f"<span>{esc(x)}</span>" for x in PROGRAM_TICKER)
    return f'<div class="ticker" aria-label="Programmes offered"><div class="track" aria-hidden="true">{items}{items}</div><p class="sr-only">{esc(", ".join(PROGRAM_TICKER))}</p><button class="tick-btn" type="button" aria-label="Pause programme ticker" aria-pressed="false"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg></button></div>\n'

ICO = {
    "book": '<path d="M4 5a2 2 0 0 1 2-2h12v16H6a2 2 0 0 0-2 2z"/><path d="M4 19V5"/><path d="M8 7h7"/>',
    "steps": '<path d="M4 20h4v-4h4v-4h4V8h4"/><path d="M4 4v16"/>',
    "doc": '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
    "key": '<circle cx="8" cy="15" r="4"/><path d="M10.8 12.2 20 3M16 7l3 3M18 5l2 2"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "brief": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
    "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
}
def ico(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICO[n]}</svg>'


# ---------- home hero slideshow: every img/hero/hero-NN-*.webp, in file-name order ----------
HERO_DIR = os.path.join(B.OUT, "img", "hero")

def hero_slides():
    """Captions come from img/hero/hero.json; a photo without an entry gets one from its file name."""
    meta = {}
    jp = os.path.join(HERO_DIR, "hero.json")
    if os.path.exists(jp):
        meta = {m["file"]: m for m in json.load(open(jp, encoding="utf-8"))}
    files = sorted(f[:-5] for f in os.listdir(HERO_DIR) if f.startswith("hero-") and f.endswith(".webp") and not f.endswith("-800.webp"))
    return [(f, meta.get(f, {}).get("caption") or f.split("-", 2)[-1].replace("-", " ").capitalize()) for f in files]

def hero_img(name, lazy=True):
    from PIL import Image
    w, h = Image.open(os.path.join(HERO_DIR, name + ".webp")).size
    small = os.path.exists(os.path.join(HERO_DIR, name + "-800.webp"))
    ss = f' srcset="img/hero/{name}-800.webp 800w, img/hero/{name}.webp {w}w" sizes="100vw"' if small else ""
    return f'<img src="img/hero/{name}.webp"{ss} alt="" width="{w}" height="{h}"{" loading=\"lazy\"" if lazy else " fetchpriority=\"high\""}>'

# ======================================================================= HOME
def build_home():
    slides = hero_slides()
    sl = []
    for i, (s, c) in enumerate(slides):
        im = hero_img(s, lazy=i > 0)
        if i > 0: im = im.replace(' src="', ' data-src="').replace(' srcset="', ' data-srcset="').replace("<img ", '<img fetchpriority="low" ')
        sl.append(f'<div class="slide{" on" if i == 0 else ""}" data-cap="{esc(c)}">{im}</div>')
    dots = "".join(f'<button type="button" aria-label="Show photo {i + 1}: {esc(c)}"><i></i></button>' for i, (_, c) in enumerate(slides))
    quick = [("academics.html", "book", "Programmes", "College, SHS, Basic Ed"), ("admissions.html#steps", "steps", "How to enroll", "Three steps on campus"),
             ("downloads.html", "doc", "Forms", "Registration form, memos"), ("portals.html", "key", "Student services", "LMS, IMS, PMS, VMS")]
    q = "".join(f'<li><a href="{h}">{ico(i)}<span><b>{t}</b><small>{s}</small></span></a></li>' for h, i, t, s in quick)
    progs = "".join(f'<a class="cp rv" href="academics.html#{code.split()[0].lower().replace("/", "")}"><figure class="photo rv-img">{simg(img, name)}</figure><h3>{name}</h3><p>{code}</p></a>' for code, name, img, _ in TERTIARY_FULL[:6])
    news = []
    for date, title, text, im, vid in NEWS_FULL[:3]:
        th = f'<div class="thumb">{simg(im, "", "(max-width: 900px) 100vw, 33vw")}</div>' if im else f'<div class="thumb"><img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360"></div>'
        news.append(f'<a class="post rv" href="news.html">{th}<h3>{esc(title)}</h3><p>{esc(text[:150])}{"..." if len(text) > 150 else ""}</p><span class="date">{esc(date)}</span></a>')
    body = f"""<section class="hero hero-home">
  <div class="slides">{"".join(sl)}</div><div class="scrim"></div>
  <div class="wrap"><div class="copy">
    <h1>{lines("The School|of Life Skills")}</h1>
    <p class="lede">St. Clare College of Caloocan educates learners from Nursery to College, on one campus in Caloocan City and online through St. Clare Online.</p>
    <div class="actions"><a class="btn" href="admissions.html"><span>How to enroll</span> {ARROW}</a><a class="btn ghost" href="academics.html"><span>Explore programmes</span></a></div>
  </div></div>
  <div class="slide-ui"><p class="slide-cap"></p><div class="slide-ctrl"><button class="slide-pause" type="button" aria-label="Pause slideshow" aria-pressed="false"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg></button><div class="dots">{dots}</div></div></div>
</section>
<nav class="quick" aria-label="Quick access"><ul class="wrap">{q}</ul></nav>
<div style="height:clamp(48px,6vw,80px)"></div>
""" + ticker() \
        + sec(shead("Academic programmes", "From a child's first school day to a bachelor's degree, every stage of learning happens at St. Clare.") + B.levels_html()) \
        + sec(f"""<div class="sec-head on-dark rv"><div><h2>Proud moments, on video</h2></div><p class="lede">The Professional Mace, the Virtual Lab and the commencement of the Stars of 2024, from the St. Clare College channel.</p></div>
{theater([("The Eternal Flame of Professionalism", "0RI2tMRZf8w", "The Professional Mace &middot; September 23, 2023"), ("The Stars of 2024: 38th Commencement Exercises", "z_bUjTOihzA", "June 2024"), ("St. Clare College Virtual Lab", "Ncj3mlHUiok", "2021"), ("Welcome to St. Clare", "f4jWTiXrIOs", "2021"), ("St. Clare College Facilities 2021", "ENCCIBqdPMs", "State-of-the-art facilities")], "St. Clare College channel")}<p class="mt-l rv"><a class="more" href="vms.html">All 46 videos</a></p>""", "dark") \
        + sec(f"""<div class="split">
  <div class="rv"><h2>A college built for professional life</h2>
    <p class="lede mt">The first college in the country to use e-boards in all 95 classrooms, with computer laboratories, a library and learning resource center, and a Virtual Lab for mixed reality.</p>
    {B.FACTS}
    <p class="mt-l"><a class="more" href="campus-life.html">Tour the facilities</a></p></div>
  <figure class="photo rv-img">{simg("prog-bscs-lab", "Computer laboratory at St. Clare College")}<figcaption>Computer laboratory: lessons on e-boards in all 95 classrooms</figcaption></figure>
</div>""", "alt") \
        + sec(shead("College degrees", "Theory in class, mastery in the laboratory, kitchen and field.") + f'<div class="cards-photo">{progs}</div><p class="mt-l rv"><a class="more" href="academics.html">All eight degrees and SHS tracks</a></p>') \
        + sec(shead("How to enroll", "Bring your requirements in a long brown envelope and complete three steps on campus, or enroll online through the IMS.") + steps_html() + f'<div class="actions mt-l rv"><a class="btn" href="admissions.html#requirements"><span>See the requirements</span> {ARROW}</a><a class="btn line" href="downloads.html"><span>Download the registration form</span></a></div>', "alt") \
        + sec(shead("News and announcements", "Dates shown are when each item was posted by St. Clare College.") + f'<div class="news">{"".join(news)}</div><p class="mt-l rv"><a class="more" href="news.html">All news</a></p>') \
        + sec(f'<div class="banner rv">{B.img("graduates.jpg", "St. Clare College graduates at the 2024 commencement", 1230, 640, sizes="100vw")}<div class="txt"><h2>Congratulations, Stars of 2024</h2><p>St. Clare College held its 38th Commencement Exercises in June 2024.</p><div class="actions mt"><a class="btn gold sm" href="vms.html#commencement"><span>Watch the ceremonies</span> {ARROW}</a></div></div></div>', "tight") \
        + cta()
    page("index.html", "St. Clare College of Caloocan | The School of Life Skills",
         "St. Clare College of Caloocan: Nursery to College, full online or blended. BSCS, BSHM, BSTM, BSBA, BEEd, BSEd, AB Political Science and Senior High tracks.", body)

# ======================================================================= ABOUT
REDS = [("#24040a", "Maroon 950", "Footer"), ("#3d0610", "Maroon 900", "Hero ground"), ("#5c0a17", "Maroon 800", "Dark bands"), ("#7a0c1e", "Maroon 700", "Primary"),
        ("#a6192e", "Crimson 600", "Links, text"), ("#c8102e", "Red 500", "Actions"), ("#f6e1e4", "Rose 100", "Tints", True), ("#e0ad1c", "Seal gold", "Accent", True)]

def build_about():
    hist = "".join(f'<li class="rv"><span class="y">{y}</span><h3>{h}</h3><p>{p}</p></li>' for y, h, p in HISTORY)
    leaders = "".join(f'<div class="rv"><b>{n}</b><span>{r}</span></div>' for n, r in LEADERS)
    partners = "".join(f'<figure>{simg(s, n, "120px")}<figcaption>{n}</figcaption></figure>' for s, n in PARTNERS)
    chans = "".join(f'<figure>{simg(s, n, "150px")}<figcaption>{n}</figcaption></figure>' for s, n in SCO_CHANNELS)
    vids = [("SCC Administrators, Officials & Staff 2021", "zDYPFpB0pK0", "School officials"), ("Welcome to St. Clare", "f4jWTiXrIOs", "2021"),
            ("St. Clare College Facilities 2021", "ENCCIBqdPMs", "State-of-the-art facilities"), ("The leading edge in online education system", "S_SYZ1X5Thk", "2021"),
            ("Continuity of Learning", "jwzbf0naZyE", "No one gets left behind"), ("Our Future", "1_vsofl20fQ", "")]
    pal = "".join(f'<div class="{"lt" if len(r) > 3 else ""}" style="background:{r[0]}"><b>{r[1]}</b><span>{r[0]} &middot; {r[2]}</span></div>' for r in REDS)
    body = f"""<section class="hero hero-about"><div class="gridfloor" aria-hidden="true"><i></i></div>
  <div class="wrap grid">
    <div>{crumbs("About")}<h1>{lines("Transforming education,|building our future")}</h1>
      <p class="lede" style="margin-top:20px">St. Clare College of Caloocan is the School of Life Skills and a leading institution for professional development.</p>
      <div class="since"><b data-count="1985">1985</b><span>Founded 31 August 1985 in Caloocan City, Metro Manila</span></div></div>
    <div class="frames">
      <figure class="f1">{B.img("campus-building.jpg", "St. Clare College building on Zabarte Road", 1600, 900, lazy=False, sizes="(max-width: 900px) 90vw, 45vw")}</figure>
      <figure class="f2">{simg("fac-library", "The Library and Learning Resource Center", "(max-width: 900px) 60vw, 30vw", lazy=False)}</figure>
      <div class="badge"><img src="img/seal.svg" alt="St. Clare College of Caloocan seal" width="112" height="112"></div>
    </div>
  </div>
</section>
""" + sec(shead("Vision and mission", "Quality, affordable and sustainable education for the total development of every Clarean.") + """<div class="vm2">
  <article class="rv" data-w="Vision"><h3>Vision</h3><p>To become the leading institution for professional development and the first and foremost provider of quality, affordable and sustainable development education.</p></article>
  <article class="rv" data-w="Mission"><h3>Mission</h3><p>To provide quality and excellent global education for the total development of a responsible, innovative, skillful and professional global workforce whose values and dignity are beyond par.</p></article>
</div>""") \
        + sec(shead("Leadership") + f'<div class="leaders">{leaders}</div>', "alt") \
        + sec(f'<div class="split" style="align-items:start"><div class="rv"><h2>The leading edge in online education</h2><p class="lede mt">Long before the COVID-19 crisis, St. Clare College prepared its ICT capability, so that it was ready to embrace the new normal in education while continuing to provide quality, affordable and sustainable development education.</p></div><ol class="timeline">{hist}</ol></div>') \
        + sec(shead("State-of-the-art facilities", "Transforming education, building our future. Select a photo to enlarge it.") + gallery([f for f in FACILITIES if f[0] != "fac-state-of-the-art"] + [("prog-bscs-lab", "Computer laboratory"), ("virtual-lab-predator-units", "Predator units in the Virtual Lab")]), "alt", "facilities") \
        + sec(shead("St. Clare in video", "Officials, facilities and the story of St. Clare Online.") + '<div class="vids">' + "".join(f'<div class="rv">{vcard(t, v, w)}</div>' for t, v, w in vids) + '</div><p class="mt-l rv"><a class="more" href="vms.html">Full video library</a></p>') \
        + sec(f"""<div class="split"><div class="rv"><h2>The seal and the St. Clare reds</h2><p class="lede mt">The original college seal, restored in high definition, leads a palette built on deep crimson and maroon, with the seal's gold as the accent.</p></div>
  <div class="rv" style="display:grid;place-items:center"><img src="img/seal.svg" alt="St. Clare College of Caloocan seal" width="300" height="300" loading="lazy" style="width:min(300px,70vw);filter:drop-shadow(0 18px 30px rgba(61,6,16,.25))"></div></div>
<div class="palette mt-l rv">{pal}</div>""", "alt", "seal") \
        + sec(shead("Center for Online Education System", "The technology partners and SCO Online channels behind St. Clare Online.") + f'<div class="logos rv">{partners}</div><h3 class="mt-l" style="margin-bottom:14px">SCO Online channels</h3><div class="channels rv">{chans}</div>') \
        + cta("Visit the campus", "Zabarte Road, Caloocan City. Office hours 9:00 AM to 5:00 PM.")
    page("about.html", "About St. Clare College | Vision, Mission, History & Leadership",
         "Founded in 1985 in Caloocan City, St. Clare College is the School of Life Skills: vision, mission, leadership, history, facilities, videos and technology partners.", body)

# ======================================================================= ACADEMICS
def build_academics():
    ter = "".join(f'<article class="prog-row rv" id="{code.split()[0].lower().replace("/", "")}"><figure class="photo rv-img">{simg(img, name)}</figure><div><span class="code">{code}</span><h3>{name}</h3><p>{desc}</p></div></article>' for code, name, img, desc in TERTIARY_FULL)
    shs = "".join(f'<article class="prog-row rv"><figure class="photo rv-img">{simg(img, name)}</figure><div><h3>{name}</h3><p>{desc}</p></div></article>' if img else f'<article class="prog-row rv"><div class="noimg">{name}</div><div><h3>{name}</h3><p>{desc}</p></div></article>' for name, img, desc in SHS_FULL)
    bas = "".join(f'<div class="cp rv"><figure class="photo rv-img">{simg(img, n)}</figure><h3>{n}</h3><p>{d}</p></div>' for n, img, d in BASIC_FULL)
    doors = [("tertiary", "prog-bscs-lab", "College", "Eight bachelor's degrees: BSHM, BSBA, BSCS, BEEd, BSEd, BSTM, AB PolSci"),
             ("shs", "shs-ict-virtual-lab", "Senior High School", "ABM, HUMSS, Arts & Design, TVL-ICT and TVL-HE"),
             ("basic", "basic-elementary", "Basic Education", "Nursery and Kindergarten, Elementary and Junior High School")]
    dh = "".join(f'<a class="panel-x" href="#{h}">{simg(s, "", "(max-width: 760px) 100vw, 60vw", lazy=False).replace("<img ", "<img fetchpriority=\"high\" " if h == "tertiary" else "<img ")}<span class="in"><b>{t}</b><span>{d}</span><em>View programmes &rarr;</em></span></a>' for h, s, t, d in doors)
    body = f"""<section class="hero hero-acad"><div class="gridfloor" aria-hidden="true"><i></i></div>
  <div class="wrap"><div class="head-copy">{crumbs("Academics")}<h1>{lines("Programmes for|every stage")}</h1>
    <p class="lede" style="margin-top:18px">Basic Education, Senior High School and eight college degrees, taught on campus, online or blended. Choose a level.</p></div>
    <div class="panels">{dh}</div></div>
</section>
""" + ticker() \
        + sec(shead("College degrees", "Eight bachelor's degree programmes: BSHM, BSBA, BSCS, BEEd, BSEd-English, BSEd-Math, BSTM and AB Political Science.") + f'<div class="prog-rows">{ter}</div>', "", "tertiary") \
        + sec(shead("Senior High School", "Academic, Arts & Design and Technical-Vocational-Livelihood tracks.") + f'<div class="prog-rows">{shs}</div>', "alt", "shs") \
        + sec(shead("Basic Education", "Nursery to Grade 10.") + f'<div class="cards-photo">{bas}</div>', "", "basic") \
        + sec(shead("Programme fliers", "Select a flier to enlarge it.") + gallery(list(FLIERS) + [("fac-state-of-the-art", "State of the Art Facilities: Transforming Education, Building our Future")], "contain four"), "alt") \
        + cta("Find the right programme", "Talk to admissions about the programme that fits your goals.")
    page("academics.html", "Academics | St. Clare College Programmes",
         "College degrees (BSHM, BSBA, BSCS, BEEd, BSEd, BSTM, AB PolSci), Senior High tracks (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and Basic Education at St. Clare College.", body)

# ======================================================================= ADMISSIONS
def build_admissions():
    tabs, panels = [], []
    for i, (k, (label, ab, items)) in enumerate(REQ.items()):
        sel = i == 0
        tabs.append(f'<button role="tab" id="rt-{k}" aria-controls="rp-{k}" aria-selected="{"true" if sel else "false"}"{"" if sel else " tabindex=\"-1\""} data-hash="{k}">{label}</button>')
        panels.append(f'<div role="tabpanel" id="rp-{k}" aria-labelledby="rt-{k}">{checklist(items)}</div>')
    faq = [
        ("Can I enroll online?", 'Yes. Online enrollment is through the IMS: <a href="ims.html">St. Clare IMS</a>. You can also enroll on campus in three steps.'),
        ("Can I study fully online?", "Yes. St. Clare College offers two modalities: full online and blended (online plus on-campus days)."),
        ("How do I get my class schedule?", 'After paying the matriculation fee and filling up your registration form, go to the Library on the 3rd floor for enlistment. Schedules and sectioning are posted in the <a href="lms.html">LMS</a> and emailed by your Program Head.'),
        ("When does enrollment open, and how much are the fees?", f"Call the admissions office at {PHONE} or email {EMAIL} to confirm this school year's enrollment dates and fees. Fee slides on this page are from earlier school years."),
        ("Are there scholarships?", 'Ask admissions for this school year\'s offers. Submit a certificate of indigency for scholarship consideration. UniFAST-TES grantees verify their status and schedule on the <a href="pms.html#tes">PMS</a>.'),
        ("How do I request my Transcript of Records or diploma?", 'Only through the <a href="pms.html#documents">Official Document Request Portal</a>. Do not transact with fixers.'),
    ]
    faqs = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in faq)
    have = {s for s, _ in ENROLL_SLIDES}
    guide = list(ENROLL_SLIDES) + [(s, c) for s, c in IMS_GALLERY if s.startswith("slide-") and s not in have]
    steps_short = "".join(f'<li><span><b>{h}</b><small>{w}</small></span></li>' for h, w, _ in STEPS)
    body = f"""<section class="hero hero-adm">
  <div class="bgimg">{B.img("graduates.jpg", "", 1230, 640, lazy=False, sizes="100vw")}</div><div class="scrim"></div>
  <div class="wrap grid">
    <div>{crumbs("Admissions")}<h1>{lines("Become a|Clarean")}</h1>
      <p class="lede" style="margin:20px 0 28px">Three steps on campus or online through the IMS, one long brown envelope of requirements, and you are part of St. Clare.</p>
      <div class="actions"><a class="btn gold" href="#requirements"><span>See requirements</span> {ARROW}</a><a class="btn ghost" href="ims.html"><span>Enroll online (IMS)</span></a></div></div>
    <aside class="apply-card" aria-label="Enrollment at a glance"><h2>Enrollment at a glance</h2><ol>{steps_short}</ol>
      <a class="btn sm" href="#steps"><span>Full procedure</span> {ARROW}</a>
      <p class="fine">Dates and fees for this school year: call <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p></aside>
  </div>
</section>
""" + sec(shead("Enrollment procedure", "Proceed in order; each step happens at a specific place on campus.") + steps_html(), "alt", "steps") \
        + sec(shead("Admission requirements", "Select your level. All documents are considered property of the school once submitted for admission.") + f'<div class="tabs" role="tablist" aria-label="Requirement type">{"".join(tabs)}</div>{"".join(panels)}<p class="notebox">Place photocopies of all documents in a long brown envelope. College students can also check the <a href="{LMS["college_corner"][2][1][1]}" rel="noopener" target="_blank">admission requirements sheet</a> in the College Corner; Basic Education families can open the <a href="https://drive.google.com/file/d/1mVPzklhSi-ifSS8QPBUZc8ky0_UkCQiw/view?usp=sharing" rel="noopener" target="_blank">list of school requirements</a>.</p>', "", "requirements") \
        + sec(shead("Enrollment guide", "The official enrollment slides: procedure, requirements, programmes, room assignment and uniform. Fee slides are from the school year shown on each slide. Select a slide to enlarge it.") + gallery(guide, "contain"), "alt", "guide") \
        + sec(shead("Forms you will need") + docs(FORMS_DOCS[:2]) + '<p class="mt"><a class="more" href="downloads.html">All forms and memoranda</a></p>') \
        + sec(shead("Learning modality", "Personalized learning pathways: choose full online or blended.") + f"""<div class="callout rv"><div><h3>Full online or blended</h3><p>Learn from anywhere through St. Clare Online (LMS classes, the e-Library and virtual broadcasts), or combine online learning with on-campus days in air-conditioned classrooms with e-boards, laboratories and the Virtual Lab.</p></div>{zoom("poster-flexible-study", "Flexible study options")}</div>""", "alt", "modality") \
        + sec(shead("Scholarships and financial aid", "“An investment in knowledge pays the best interest.” Benjamin Franklin") + f"""<div class="grid3">
  <div class="panel rv"><span class="dated">SY 2024-2025</span><h3>President's Scholarship</h3><p>The SHS Alumni VIP Package for the St. Clare SHS Class of 2024: President's Scholarship and zero down payment. Ask admissions about this year's scholarships.</p></div>
  <div class="panel rv"><h3>UniFAST-TES</h3><p>Tertiary Education Subsidy grantees verify their status and secure a disbursement schedule on the PMS.</p><p class="mt"><a class="more" href="pms.html#tes">TES guidelines</a></p></div>
  <div class="panel rv"><h3>Certificate of indigency</h3><p>Optional. Submit it with your requirements to be considered for scholarship.</p></div></div>""", "", "scholarships") \
        + sec(f'<div class="rv"><h2 style="margin-bottom:24px">Frequently asked questions</h2><div class="faq">{faqs}</div></div>', "alt") \
        + cta("Ready to enroll?", "Take the first step towards a brighter tomorrow.")
    page("admissions.html", "Admissions | Enroll at St. Clare College",
         "How to enroll at St. Clare College: three steps on campus or online, requirements by level, the official enrollment guide, forms, modality, scholarships and FAQ.", body)

# ======================================================================= CAMPUS LIFE
def build_campus():
    day = [("Monday, 7:00 AM", "Virtual flag ceremony", "The whole community gathers online to start the week."),
           ("Classes", "E-boards in all 95 classrooms", "The first college in the country to replace every blackboard with an e-board."),
           ("Lab time", "Virtual Lab", "VR + AR = MR with the Predator Thronos and the Mixed Reality facility by Acer."),
           ("3rd floor", "Library and Learning Resource Center", "Study space, enlistment and the ProQuest-powered e-Library."),
           ("Broadcasts", "St. Clare Virtual Studio", "Webinars, parents' orientations and commencement broadcasts."),
           ("Every week", "SCO Online channels", ", ".join(n for _, n in SCO_CHANNELS) + ".")]
    dh = "".join(f'<div class="panel rv"><p class="when">{t}</p><h3>{h}</h3><p>{p}</p></div>' for t, h, p in day)
    photos = [("prog-bscs-lab", "Computer laboratory"), ("shs-ict-virtual-lab", "The Virtual Lab"), ("virtual-lab-predator-units", "Predator units in the Virtual Lab"),
              ("prog-bshm", "Hospitality students"), ("shs-tvl-he", "TVL Home Economics"), ("prog-education", "Teacher education"),
              ("basic-kinder", "Kindergarten"), ("prog-bstm", "Tourism management"), ("i-love-st-clare", "I love St. Clare")]
    mosaic = [("fac-virtual-lab-thronos", "Virtual Lab"), ("fac-library", "Library"), ("prog-bshm", "Hospitality kitchen"), ("fac-vr-headset", "Mixed reality"), ("basic-kinder", "Basic Education")]
    mz = "".join(f'<figure>{simg(s, c, "(max-width: 760px) 50vw, 25vw", lazy=False).replace("<img ", "<img fetchpriority=\"high\" " if s == mosaic[0][0] else "<img ")}<figcaption>{c}</figcaption></figure>' for s, c in mosaic)
    vids = [("St. Clare College Virtual Lab", "Ncj3mlHUiok", "2021"), ("St. Clare Online: Virtual Lab", "avbXu3J7PoI", "Predator Thronos & Mixed Reality by Acer"), ("St. Clare College Virtual Flag Ceremony", "QSRZvHk7TMA", "Every Monday, 7:00 AM")]
    body = f"""<section class="hero hero-camp"><div class="gridfloor" aria-hidden="true"><i></i></div>
  <div class="wrap">{crumbs("Campus life")}<h1>{lines("Life at|St. Clare")}</h1>
    <p class="lede" style="margin-top:18px">E-boards in every classroom, a Virtual Lab, our own broadcast channels and a community that keeps learning online.</p>
    <div class="mosaic">{mz}</div></div>
</section>
""" + sec(shead("A week on campus", "From the Monday flag ceremony to the Virtual Studio.") + f'<div class="grid3">{dh}</div>', "", "week") \
        + sec(f"""<div class="sec-head on-dark rv"><div><h2>Inside the Virtual Lab</h2></div><p class="lede">Visit St. Clare College and experience the immersive technology behind the Predator Thronos and the Mixed Reality facility by Acer.</p></div>
{theater(vids, "Virtual Lab")}""", "dark", "virtual-lab") \
        + sec(shead("State-of-the-art facilities", "The library, the Virtual Lab and mixed-reality learning. Select a photo to enlarge it.") + gallery([f for f in FACILITIES if f[0] != "fac-state-of-the-art"] + [("virtual-lab-predator-units", "Predator units in the Virtual Lab"), ("shs-ict-virtual-lab", "TVL-ICT in the Virtual Lab")]), "", "facilities") \
        + sec(shead("Campus in pictures") + gallery(photos), "alt") \
        + sec(f'<div class="split"><figure class="photo rv-img">{B.img("campus-building.jpg", "St. Clare College campus building", 1600, 900)}<figcaption>The campus on Zabarte Road</figcaption></figure><div class="rv"><h2>Facilities at a glance</h2><ul class="checklist" style="columns:1;margin-top:18px"><li>E-boards in all 95 classrooms</li><li>Air-conditioned classrooms and restrooms</li><li>Computer laboratories with stacked servers</li><li>Library and enlistment area on the 3rd floor</li><li>Virtual Lab: Predator Thronos and Mixed Reality by Acer</li><li>St. Clare Virtual Studio</li></ul></div></div>') \
        + sec(f'<div class="split" style="align-items:start"><div class="rv"><h2>Digital citizenship</h2><p class="lede mt">Online learning comes with responsibilities. These policies guide life on St. Clare Online.</p></div>{docs(HANDBOOKS)}</div>', "alt", "digital-citizenship") \
        + cta("See the campus", "Visit Zabarte Road, Caloocan City, 9:00 AM to 5:00 PM.")
    page("campus-life.html", "Campus Life | St. Clare College",
         "Campus life at St. Clare College: e-board classrooms, the Virtual Lab, facilities, SCO Online channels, photos, videos and digital citizenship policies.", body)

# ======================================================================= NEWS
def build_news():
    def thumb(im, vid, sizes):
        return simg(im, "", sizes) if im else f'<img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360">' if vid else simg("campus-sco-sign", "", sizes)
    lead = NEWS_FULL[0]
    heads = "".join(f'<li><a href="#n{i}">{thumb(im, vid, "76px")}<span><b>{esc(t)}</b><small>{esc(dt)}</small></span></a></li>' for i, (dt, t, tx, im, vid) in list(enumerate(NEWS_FULL))[1:6])
    items, last_year = [], None
    def yr_of(dt): return next((y for y in ("2024", "2023", "2021", "2020") if y in dt), "2020")
    order = sorted(range(len(NEWS_FULL)), key=lambda i: -int(yr_of(NEWS_FULL[i][0])))
    for i in order:
        date, title, text, imgslug, vid = NEWS_FULL[i]
        media = yt(vid, title) if vid else zoom(imgslug, title) if imgslug else ""
        extra = ""
        if title.startswith("Health Survey"): extra = f'<p><a class="more" href="{HEALTH_SURVEY}" rel="noopener" target="_blank">Open the health survey form</a></p>'
        if "UniFAST guidelines" in title: extra = '<p><a class="more" href="pms.html#tes">TES guidelines on the PMS</a></p>'
        if "leading edge" in title: extra = '<p><a class="more" href="about.html">Read the full history</a></p>'
        if "AI technology" in title: extra = '<p><a class="more" href="campus-life.html#virtual-lab">Inside the Virtual Lab</a></p>'
        yr = yr_of(date)
        if yr != last_year:
            items.append(f'<h2 class="year rv">{yr if yr != "2020" else "2020 and earlier"}</h2>'); last_year = yr
        items.append(f'<article class="item rv" id="n{i}"><div class="media">{media or '<div class="noimg" aria-hidden="true"></div>'}</div><div><span class="date">{esc(date)}</span><h3>{esc(title)}</h3><p>{esc(text)}</p>{extra}</div></article>')
    body = f"""<section class="hero hero-news"><div class="gridfloor" aria-hidden="true"><i></i></div>
  <div class="wrap">{crumbs("News")}<p class="news-strip"><b>Latest</b>{esc(lead[1])} &middot; {esc(lead[0])}</p><h1>{lines("News and|announcements")}</h1>
    <div class="feature">
      <a class="lead-story" href="#n0"><span class="pic">{simg(lead[3], "", "(max-width: 900px) 100vw, 60vw", lazy=False).replace("<img ", "<img fetchpriority=\"high\" ")}</span><span class="in"><span class="tag">Featured &middot; {esc(lead[0])}</span><b>{esc(lead[1])}</b><span style="color:var(--on-dark)">{esc(lead[2])}</span></span></a>
      <ul class="headlines">{heads}</ul>
    </div></div>
</section>
""" + sec(shead("All stories", "Milestones, scholarships, advisories and stories from the St. Clare community, newest first. Dated offers are shown for the record; call admissions for this year's.") + f'<div class="archive">{"".join(items)}</div>') + cta()
    page("news.html", "News | St. Clare College", "News and announcements from St. Clare College of Caloocan: enrollment, scholarships, UniFAST-TES, the Professional Mace, AI technology and more.", body)

# ======================================================================= CONTACT
def build_contact():
    qa = [(f"tel:{PHONE_TEL}", "phone", "Call admissions", PHONE), (f"mailto:{EMAIL}", "mail", "Email", EMAIL),
          ("https://m.me/stclarecollege", "chat", "Messenger", "St. Clare College on Facebook"), ("#map", "pin", "Visit", "Zabarte Road, Caloocan City")]
    cards = "".join(f'<a class="qa" href="{h}"{" rel=\"noopener\"" if h.startswith("http") else ""}>{ico(i)}<span><b>{t}</b><small>{s}</small></span></a>' for h, i, t, s in qa)
    body = f"""<section class="hero hero-contact">
  <div class="bgimg">{simg("campus-sco-sign", "", "100vw", lazy=False).replace("<img ", "<img fetchpriority=\"high\" ")}</div><div class="scrim"></div>
  <div class="wrap grid">
    <div>{crumbs("Contact")}<h1>{lines("We'd love to|hear from you")}</h1>
      <p class="lede" style="margin-top:20px">Questions about programmes, requirements, dates or fees? The admissions office is open 9:00 AM to 5:00 PM.</p></div>
    <div class="cards4">{cards}</div>
  </div>
</section>
""" + sec(f"""<div class="split" style="align-items:start">
  <div class="info rv"><h2>Visit, call or write</h2>
    <dl class="mt-l contact-list"><div><dt><span class="ic">{ico("pin")}</span>Campus</dt><dd>{ADDRESS}</dd></div><div><dt><span class="ic">{ico("phone")}</span>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd></div><div><dt><span class="ic">{ico("mail")}</span>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt><span class="ic">{ico("clock")}</span>Office hours</dt><dd>9:00 AM - 5:00 PM</dd></div><div><dt><span class="ic">{ico("brief")}</span>Careers (Human Resource)</dt><dd><a href="mailto:stclarecollege.humanresource@gmail.com">stclarecollege.humanresource@gmail.com</a></dd></div></dl>
    <p class="follow">Follow St. Clare College</p>{B.socials()}</div>
  <form class="form rv" data-mailto="{EMAIL}">
    <h2 style="font-size:1.4rem;margin-bottom:18px">Send an inquiry</h2>
    <div class="fld-row"><div class="fld"><label for="f-name">Full name <em>(required)</em></label><input id="f-name" name="Name" autocomplete="name" required></div>
    <div class="fld"><label for="f-email">Email <em>(required)</em></label><input id="f-email" name="Email" type="email" autocomplete="email" required></div></div>
    <div class="fld-row"><div class="fld"><label for="f-level">Interested in</label><select id="f-level" name="Level"><option>Basic Education</option><option>Senior High School</option><option selected>College</option><option>Other</option></select></div>
    <div class="fld"><label for="f-src">Where did you hear about us?</label><select id="f-src" name="Source"><option>Facebook</option><option>YouTube</option><option>Friend or family</option><option>Search</option><option>Other</option></select></div></div>
    <div class="fld"><label for="f-sub">Subject</label><input id="f-sub" name="subject" value="Enrollment inquiry"></div>
    <div class="fld"><label for="f-msg">Message <em>(required)</em></label><textarea id="f-msg" name="Message" required></textarea></div>
    <button class="btn" type="submit"><span>Send inquiry</span> {ARROW}</button>
    <p class="hint">Opens your email app, addressed to {EMAIL}. No email app? Call {PHONE}.</p><p class="form-status" role="status"></p>
  </form>
</div>""") + sec('<div class="map rv" id="map"><iframe title="Map to St. Clare College of Caloocan" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=St.+Clare+College+of+Caloocan,+Zabarte+Road,+Caloocan+City&output=embed"></iframe></div>', "alt")
    page("contact.html", "Contact St. Clare College | Caloocan City",
         f"Contact St. Clare College of Caloocan: {ADDRESS}. Phone {PHONE}, email {EMAIL}, 9:00 AM - 5:00 PM.", body)

# ======================================================================= IMS (adds the full enrollment gallery)
def build_ims():
    ft, fitems = IMS["faculty"]
    fac = "".join(f'<div class="linkset rv"><h3>{esc(h)}</h3>{P.links([(lab, u)])}</div>' for h, lab, u in fitems)
    ht, hs, quals, mail, addr = IMS["hiring"]
    gal = [("poster-online-enrollment", "Online enrollment"), ("poster-enrolment-2023", "Enrolment going on, SY 2023-2024")] + list(IMS_GALLERY)
    body = B.ph("IMS", "Institutional Management System", IMS["intro"]) + P.portal_nav("ims.html") \
        + sec(shead("Online enrollment", "Simplified and seamless: enroll online with ease. Pre-school to Junior High, Senior High School (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and Tertiary (BEEd, BSEd-Eng, BSEd-Math, BSCS, BSBA, BSHM, BSTM, AB PolSci). Slides show the school year they were published for.") + gallery(gal, "contain four") + '<p class="mt-l"><a class="more" href="admissions.html#steps">Step-by-step enrollment guide</a></p>') \
        + sec(shead(ft, "Faculty log-in / time-in for virtual classes' attendance.") + f'<div class="grid3">{fac}</div>' + P.SRC_NOTE, "alt", "faculty") \
        + sec(f'<div class="callout rv" id="hiring"><div><h3>{ht}</h3><p>{hs}</p>{checklist(quals)}<p class="mt"><a class="btn" href="{mail}"><span>Submit your application</span> {ARROW}</a></p><p class="src-note">Email: {addr}</p></div>{zoom("poster-hiring", "We are hiring: Basic Education and Senior High School teachers")}</div>') \
        + cta()
    page("ims.html", "IMS | St. Clare College Institutional Management System",
         "St. Clare College IMS: online enrollment, enrollment slides, faculty attendance monitoring and teaching job openings.", body)


def build_all():
    build_home(); build_about(); build_academics(); build_admissions(); build_campus(); build_news(); build_contact()
    P.build_portals(); P.build_lms(); P.build_cms(); build_ims(); P.build_pms(); P.build_vms(); P.build_downloads(); P.build_calendar()

if __name__ == "__main__":
    build_all()
