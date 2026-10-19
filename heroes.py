# v6 heroes: one creative concept per header page, plus the inner-page banner.
# Every hero sits on the crimson ground with the running grid floor; facts only from stclareonline.com.
import build as B
from build import esc, lines, ARROW, PHONE, PHONE_TEL, EMAIL
from pages_full import simg
from content import NEWS_FULL, HISTORY, FACILITIES, TERTIARY_FULL
from data import STEPS

GRID = '<div class="gridfloor" aria-hidden="true"><i></i></div>'

def crumbs(name): return f'<p class="crumbs"><a href="index.html">Home</a> / {name}</p>'

def lowfetch(html_img):
    return html_img.replace(' src="', ' data-src="').replace(' srcset="', ' data-srcset="').replace("<img ", '<img fetchpriority="low" ')

PAUSE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6 4h4v16H6zM14 4h4v16h-4z"/></svg>'

# ---------------------------------------------------------------- HOME: the arched window
def home(slides, hero_img, ico):
    sl, th = [], []
    for i, (s, c) in enumerate(slides):
        im = hero_img(s, lazy=i > 0)
        sl.append(f'<div class="slide{" on" if i == 0 else ""}" data-cap="{esc(c)}">{lowfetch(im) if i > 0 else im}</div>')
        th.append(f'<button type="button" aria-label="Show photo {i + 1}: {esc(c)}"><img src="img/hero/{s}-800.webp" alt="" width="96" height="64" loading="lazy"><i></i></button>')
    return f"""<section class="hero h-home">{GRID}
  <div class="wrap h-grid">
    <div class="h-copy">
      <h1>{lines("The School|of <em>Life Skills</em>")}</h1>
      <p class="lede">St. Clare College of Caloocan educates learners from Nursery to College, on one campus in Caloocan City and online through St. Clare Online.</p>
      <div class="actions"><a class="btn gold" href="admissions.html"><span>How to enroll</span> {ARROW}</a><a class="btn ghost" href="academics.html"><span>Explore programmes</span></a></div>
      <dl class="h-stats">
        <div><dt data-count="1985">1985</dt><dd>Founded in Caloocan City</dd></div>
        <div><dt data-count="95">95</dt><dd>Classrooms with e-boards</dd></div>
        <div><dt data-count="8">8</dt><dd>Bachelor's degrees</dd></div>
      </dl>
    </div>
    <div class="arch-wrap h-art">
      <svg class="arch-line" viewBox="0 0 500 640" aria-hidden="true"><path d="M8 632V250a242 242 0 0 1 484 0v382"/></svg>
      <div class="arch"><div class="slides">{"".join(sl)}</div></div>
      <span class="keystone"><img src="img/seal-128.webp" srcset="img/seal-128.webp 1x, img/seal-256.webp 2x" alt="" width="72" height="72"></span>
      <span class="chip c1">Nursery to College</span>
      <span class="chip c2">Full online or blended</span>
      <div class="slide-ui"><p class="slide-cap"></p>
        <div class="slide-ctrl"><button class="slide-pause" type="button" aria-label="Pause slideshow" aria-pressed="false">{PAUSE}</button><div class="dots thumbs">{"".join(th)}</div></div></div>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- ABOUT: the medallion
def about():
    years = "".join(f'<li><a href="#history"><b>{esc(y)}</b><span>{esc(h)}</span></a></li>' for y, h, _ in HISTORY if y[0].isdigit())
    ring = "TRANSFORMING EDUCATION &#183; BUILDING OUR FUTURE &#183; THE SCHOOL OF LIFE SKILLS &#183; "
    return f"""<section class="hero h-about">{GRID}
  <span class="ghost-year" aria-hidden="true">1985</span>
  <div class="wrap h-grid">
    <div class="h-copy">{crumbs("About")}<h1>{lines("Transforming education,|building our future")}</h1>
      <p class="lede">St. Clare College of Caloocan is the School of Life Skills and a leading institution for professional development, founded 31 August 1985.</p>
      <ol class="yearline">{years}</ol></div>
    <div class="medallion h-art" aria-hidden="true">
      <span class="orbit o1"></span><span class="orbit o2"></span>
      <svg class="ring-text" viewBox="0 0 400 400"><defs><path id="rt" d="M200 200m-168 0a168 168 0 1 1 336 0a168 168 0 1 1-336 0"/></defs><text><textPath href="#rt">{ring}{ring}</textPath></text></svg>
      <img class="m-seal" src="img/seal-256.webp" srcset="img/seal-256.webp 1x, img/seal-512.webp 2x" alt="" width="190" height="190">
      <span class="bubble b1">{B.img("campus-building.jpg", "", 1600, 900, lazy=False, sizes="160px")}</span>
      <span class="bubble b2">{simg("fac-library", "", "140px", lazy=False)}</span>
      <span class="bubble b3">{simg("fac-virtual-lab-thronos", "", "120px", lazy=False)}</span>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- ACADEMICS: the staircase
def academics():
    steps = [("basic", "basic-elementary", "01", "Basic Education", "Nursery to Grade 10", "Kindergarten, Elementary, Junior High"),
             ("shs", "shs-ict-virtual-lab", "02", "Senior High School", "Grades 11 and 12", "ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE"),
             ("tertiary", "prog-bscs-lab", "03", "College", "Eight bachelor's degrees", "BSHM, BSBA, BSCS, BEEd, BSEd, BSTM, AB PolSci")]
    st = "".join(f'<a class="stp s{i + 1}" href="#{h}"><span class="stp-img">{simg(img, "", "(max-width: 760px) 100vw, 30vw", lazy=False)}</span><span class="stp-body"><span class="stp-n">{n}</span><b>{t}</b><span class="stp-sub">{sub}</span><small>{d}</small><em>View programmes &rarr;</em></span></a>' for i, (h, img, n, t, sub, d) in enumerate(steps))
    return f"""<section class="hero h-acad">{GRID}
  <div class="wrap">
    <div class="h-copy narrow">{crumbs("Academics")}<h1>{lines("Programmes for|every stage")}</h1>
      <p class="lede">Basic Education, Senior High School and eight college degrees, taught on campus, online or blended. Climb from a child's first school day to a bachelor's degree.</p></div>
    <div class="stair h-art">
      <svg class="stair-path" viewBox="0 0 1200 300" preserveAspectRatio="none" aria-hidden="true"><path d="M0 290 L400 290 L400 190 L800 190 L800 90 L1200 90"/></svg>
      {st}
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- ADMISSIONS: the admission pass
def admissions():
    rows = "".join(f'<li><span class="sn">{i + 1:02d}</span><span><b>{h}</b><small>{w}</small></span><span class="box" aria-hidden="true"></span></li>' for i, (h, w, _) in enumerate(STEPS))
    return f"""<section class="hero h-adm">{GRID}
  <div class="bgimg">{B.img("graduates.jpg", "", 1230, 640, lazy=False, sizes="100vw")}</div><div class="scrim"></div>
  <div class="wrap h-grid">
    <div class="h-copy">{crumbs("Admissions")}<h1>{lines("Become a|<em>Clarean</em>")}</h1>
      <p class="lede">Three steps on campus or online through the IMS, one long brown envelope of requirements, and you are part of St. Clare.</p>
      <div class="actions"><a class="btn gold" href="#requirements"><span>See requirements</span> {ARROW}</a><a class="btn ghost" href="ims.html"><span>Enroll online (IMS)</span></a></div>
      <p class="note-line">Dates and fees for this school year: call <a href="tel:{PHONE_TEL}">{PHONE}</a></p></div>
    <div class="pass-wrap h-art">
      <article class="pass" aria-label="Enrollment at a glance">
        <header><img src="img/seal-128.webp" alt="" width="44" height="44"><span><b>St. Clare College</b><small>Admission pass &middot; enrollment at a glance</small></span></header>
        <ol>{rows}</ol>
        <div class="perf" aria-hidden="true"></div>
        <footer><span><small>Bring</small><b>Photocopies in a long brown envelope</b></span><a class="btn sm" href="#steps"><span>Full procedure</span> {ARROW}</a></footer>
        <span class="code" aria-hidden="true"></span>
      </article>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- CAMPUS LIFE: the moving gallery wall
def campus():
    a = [("campus-sco-sign", "The campus on Zabarte Road")] + list(FACILITIES[:4]) + [("prog-bscs-lab", "Computer laboratory"), ("prog-bshm", "Hospitality kitchen")]
    b = [("basic-kinder", "Basic Education"), ("shs-tvl-he", "TVL Home Economics"), ("virtual-lab-predator-units", "Predator units"), ("prog-education", "Teacher education"), ("i-love-st-clare", "I love St. Clare"), ("prog-bstm", "Tourism management")]
    def row(items, cls):
        cards = "".join(f'<figure>{simg(s, c, "300px", lazy=k > 3)}<figcaption>{esc(c)}</figcaption></figure>' for k, (s, c) in enumerate(items))
        dup = cards.replace("<figure>", '<figure aria-hidden="true">')
        return f'<div class="reel-row {cls}"><div class="reel-track">{cards}{dup}</div></div>'
    return f"""<section class="hero h-camp">{GRID}
  <div class="wrap"><div class="h-copy center">{crumbs("Campus life")}<h1>{lines("Life at|St. Clare")}</h1>
    <p class="lede">E-boards in every classroom, a Virtual Lab, our own broadcast channels and a community that keeps learning online.</p></div></div>
  <div class="reel h-art">{row(a, "r1")}{row(b, "r2")}
    <button class="tick-btn reel-btn" type="button" aria-label="Pause photo reel" aria-pressed="false">{PAUSE}</button></div>
</section>
"""

# ---------------------------------------------------------------- NEWS: the broadsheet
def news(thumb):
    lead = NEWS_FULL[0]
    col = "".join(f'<a class="bs-story" href="#n{i}">{thumb(im, vid, "(max-width: 900px) 100vw, 25vw")}<span class="bs-date">{esc(dt)}</span><b>{esc(t)}</b></a>' for i, (dt, t, tx, im, vid) in list(enumerate(NEWS_FULL))[1:3])
    heads = "".join(f'<li><a href="#n{i}"><span class="hn">{k + 1:02d}</span><span><b>{esc(t)}</b><small>{esc(dt)}</small></span></a></li>' for k, (i, (dt, t, tx, im, vid)) in enumerate(list(enumerate(NEWS_FULL))[3:8]))
    tick = "".join(f"<span>{esc(t)}</span>" for _, t, _, _, _ in NEWS_FULL[:10])
    return f"""<section class="hero h-news">{GRID}
  <div class="wrap">
    <div class="nameplate h-copy">{crumbs("News")}
      <div class="np-row"><span class="np-side">St. Clare College of Caloocan</span><h1>{lines("News and announcements")}</h1><span class="np-side r">Posts from 2020 to 2024</span></div>
      <nav class="np-tabs" aria-label="News by year"><a href="#y2024">2024</a><a href="#y2023">2023</a><a href="#y2021">2021</a><a href="#y2020">2020 and earlier</a></nav></div>
    <div class="broadsheet h-art">
      <a class="bs-lead" href="#n0"><span class="pic">{simg(lead[3], "", "(max-width: 900px) 100vw, 50vw", lazy=False).replace("<img ", "<img fetchpriority=\"high\" ")}</span><span class="tag">Featured &middot; {esc(lead[0])}</span><b>{esc(lead[1])}</b><span class="dek">{esc(lead[2])}</span></a>
      <div class="bs-col">{col}</div>
      <div class="bs-heads"><p class="bs-h">More headlines</p><ol>{heads}</ol></div>
    </div>
  </div>
  <div class="ticker news-tick" aria-label="Recent headlines"><div class="track" aria-hidden="true">{tick}{tick}</div><button class="tick-btn" type="button" aria-label="Pause headline ticker" aria-pressed="false">{PAUSE}</button></div>
</section>
"""

# ---------------------------------------------------------------- CONTACT: the campus locator
def contact(cards):
    maps = "https://www.google.com/maps?q=St.+Clare+College+of+Caloocan,+Zabarte+Road,+Caloocan+City"
    return f"""<section class="hero h-contact">{GRID}
  <div class="wrap h-grid">
    <div class="h-copy">{crumbs("Contact")}<h1>{lines("We'd love to|hear from you")}</h1>
      <p class="lede">Questions about programmes, requirements, dates or fees? The admissions office is open 9:00 AM to 5:00 PM.</p>
      <div class="cards4">{cards}</div></div>
    <div class="locator h-art">
      <svg class="streets" viewBox="0 0 500 500" aria-hidden="true">
        <path class="rd" d="M-20 330 C120 300 260 260 520 140"/><path class="rd" d="M120 -20 C150 140 210 300 250 520"/>
        <path class="ln" d="M-20 140 L520 210"/><path class="ln" d="M-20 440 L520 380"/><path class="ln" d="M360 -20 L330 520"/><path class="ln" d="M40 -20 L-10 520"/><path class="ln" d="M-20 60 L520 40"/>
        <text x="300" y="196" transform="rotate(-24 300 196)">ZABARTE ROAD</text>
      </svg>
      <span class="radar" aria-hidden="true"><i></i><i></i><i></i></span>
      <span class="pin" aria-hidden="true"><img src="img/seal-128.webp" alt="" width="46" height="46"></span>
      <div class="loc-card"><b>St. Clare College of Caloocan</b><small>Zabarte Road, Barangay 172, Camarin, Caloocan City</small><a class="more" href="{maps}" rel="noopener" target="_blank">Open in Google Maps</a></div>
      <span class="loc-note">Illustration, not to scale</span>
    </div>
  </div>
</section>
"""

# ---------------------------------------------------------------- inner pages: giant outlined system mark
MARKS = {"LMS": "LMS", "CMS": "CMS", "IMS": "IMS", "PMS": "PMS", "VMS": "VMS", "Downloads": "DOCS", "Calendar": "CAL", "Student services": "SCO"}
