# Full-content pages: everything captured from stclareonline.com (videos, documents, link directories, images).
import json, os
import build as B
from build import esc, sec, shead, ph, cta, steps_html, checklist, page, OUT, ARROW, SRC, PHONE, PHONE_TEL, EMAIL, ADDRESS, FB, YT
from data import REQ, FORMS, PORTALS, EVENTS
from content import *

SIZES = json.load(open(os.path.join(OUT, "img", "site", "sizes.json")))

def simg(slug, alt, sizes="(max-width: 900px) 100vw, 50vw", lazy=True):
    s = SIZES[slug]
    ss = f' srcset="img/site/{slug}-800.webp 800w, img/site/{slug}.webp {s["w"]}w" sizes="{sizes}"' if s["small"] else ""
    return f'<img src="img/site/{slug}.webp"{ss} alt="{esc(alt)}" width="{s["w"]}" height="{s["h"]}"{" loading=\"lazy\"" if lazy else ""}>'

def zoom(slug, cap, cls="media-btn"):
    return f'<button class="{cls}" type="button" data-full="img/site/{slug}.webp" data-cap="{esc(cap)}" aria-label="Enlarge: {esc(cap)}">{simg(slug, cap, "(max-width: 800px) 50vw, 33vw")}</button>'

def gallery(items, cls=""):
    return f'<div class="gallery {cls}">' + "".join(f'<figure>{zoom(s, c, "")}<figcaption>{esc(c)}</figcaption></figure>' for s, c in items) + "</div>"

def yt(vid, title, start=None):
    st = f' data-start="{start}"' if start else ""
    return f'<div class="yt" data-id="{vid}"{st}><button type="button" aria-label="Play video: {esc(title)}"><img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy" width="480" height="360"></button></div>'

def vcard(title, vid, when=""):
    return f'<div class="vid">{yt(vid, title)}<h3>{esc(title)}</h3>{f"<p class=\"when\">{esc(when)}</p>" if when else ""}</div>'

def links(items):
    out = []
    for t, u in items:
        out.append(f'<li><a href="{esc(u)}" rel="noopener" target="_blank">{esc(t)}</a></li>' if u else f'<li><span>{esc(t)}: not yet posted</span></li>')
    return '<ul class="links">' + "".join(out) + "</ul>"

def docs(items):
    return '<ul class="docs">' + "".join(f'<li><a href="docs/{f}" download><span class="ty{" docx" if t == "DOCX" else ""}">{t}</span><span><b>{esc(n)}</b><small>{t} &middot; {sz}</small></span><span class="dl">Download</span></a></li>' for n, f, t, sz in items) + "</ul>"

SRC_NOTE = '<p class="src-note">Spreadsheets, forms and files open on Google (Sheets, Forms or Drive), as published by St. Clare College.</p>'

def portal_nav(cur):
    items = [("portals.html", "All services"), ("lms.html", "LMS"), ("cms.html", "CMS"), ("ims.html", "IMS"), ("pms.html", "PMS"), ("vms.html", "VMS"), ("downloads.html", "Downloads"), ("calendar.html", "Calendar")]
    return '<nav class="subnav" aria-label="Student services"><div class="wrap">' + "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in items) + "</div></nav>\n"

# ======================================================================= pages
def build_home():
    quick = [("academics.html", "book", "Programmes", "College, SHS, Basic Ed"), ("admissions.html#steps", "steps", "How to enroll", "Three steps on campus"),
             ("downloads.html", "list", "Forms & downloads", "Registration form, memos"), ("portals.html", "key", "Student services", "LMS, IMS, PMS, VMS")]
    q = "".join(f'<li><a href="{h}">{B.icon(i)}<span><b>{t}</b><small>{s}</small></span></a></li>' for h, i, t, s in quick)
    progs = "".join(f'<a class="cp rv" style="--d:{i % 3}" href="academics.html#tertiary"><figure class="photo">{simg(img, name)}</figure><h3>{name}</h3><p>{code}</p></a>' for i, (code, name, img, _) in enumerate(TERTIARY_FULL))
    body = f"""<section class="hero on-navy">
  <div class="hero-img">{B.img("campus-building.jpg", "", 1600, 900, lazy=False, sizes="100vw")}</div>
  <div class="wrap"><div class="hero-card">
    <span class="rule" aria-hidden="true"></span><h1>The School of Life Skills</h1>
    <p class="lede">St. Clare College of Caloocan educates learners from Nursery to College, on one campus in Caloocan City and online through St. Clare Online.</p>
    <div class="actions"><a class="btn" href="admissions.html">How to enroll {ARROW}</a><a class="btn line" href="academics.html">Explore programmes</a></div>
  </div></div>
</section>
<nav class="quick" aria-label="Quick access"><ul class="wrap">{q}</ul></nav>
""" + sec(shead("Academic programmes", "From a child's first school day to a bachelor's degree, every stage of learning happens at St. Clare.") + B.levels_html()) \
        + sec(shead("College degrees", "Theory in class, mastery in the laboratory, kitchen and field.") + f'<div class="cards-photo">{progs}</div><p class="mt-l rv"><a class="more" href="academics.html">All programme details</a></p>', "alt") \
        + sec(f"""<div class="split">
  <div class="rv"><h2>The Eternal Flame of Professionalism</h2><p class="lede mt">The St. Clare College Professional Mace, introduced on 23 September 2023: &ldquo;a beacon of professionalism and culture of excellence.&rdquo;</p><p class="mt"><a class="more" href="vms.html">Watch more on the VMS</a></p></div>
  <div class="vid rv" style="--d:1">{yt("0RI2tMRZf8w", "St. Clare College Professional Mace")}<h3>St. Clare College Professional Mace</h3><p class="when">By ERA &amp; EJA &middot; September 23, 2023</p></div>
</div>""") \
        + sec(f"""<div class="split">
  <div class="rv"><h2>A college built for professional life</h2>
    <p class="lede mt">The first college in the country to use e-boards in all 95 classrooms, with computer laboratories and a Virtual Lab for mixed reality.</p>
    {B.FACTS}
    <p class="mt-l"><a class="more" href="about.html">About St. Clare</a></p></div>
  <figure class="photo rv" style="--d:1">{simg("virtual-lab-predator-units", "Predator gaming units in the St. Clare Virtual Lab")}<figcaption>The St. Clare Virtual Lab: VR + AR = mixed reality</figcaption></figure>
</div>""", "alt") \
        + sec(shead("How to enroll", "Bring your requirements in a long brown envelope and complete three steps on campus.") + steps_html() + '<div class="actions mt-l rv"><a class="btn" href="admissions.html#requirements">See the requirements</a><a class="btn line" href="downloads.html">Download the registration form</a></div>') \
        + sec(shead("News and announcements") + B.news_cards(B.NEWS[:3]) + '<p class="mt-l rv"><a class="more" href="news.html">All news</a></p>', "alt") \
        + sec(f'<div class="banner rv">{B.img("graduates.jpg", "St. Clare College graduates at the 2024 commencement", 1230, 640, sizes="100vw")}<div class="txt"><h2>Congratulations, Stars of 2024</h2><p>St. Clare College held its 38th Commencement Exercises in June 2024. <a href="vms.html#commencement" style="color:#fff">Watch the ceremonies</a></p></div></div>') \
        + cta()
    page("index.html", "St. Clare College of Caloocan | The School of Life Skills",
         "St. Clare College of Caloocan: Nursery to College, full online or blended. BSCS, BSHM, BSTM, BSBA, BEEd, BSEd, AB Political Science and Senior High tracks.", body)


def build_about():
    hist = "".join(f'<li class="rv"><span class="y">{y}</span><h3>{h}</h3><p>{p}</p></li>' for y, h, p in HISTORY)
    leaders = "".join(f"<div><b>{n}</b><span>{r}</span></div>" for n, r in LEADERS)
    partners = "".join(f'<figure>{simg(s, n, "120px")}<figcaption>{n}</figcaption></figure>' for s, n in PARTNERS)
    chans = "".join(f'<figure>{simg(s, n, "150px")}<figcaption>{n}</figcaption></figure>' for s, n in SCO_CHANNELS)
    vids = [("SCC Administrators, Officials & Staff 2021", "zDYPFpB0pK0", "School officials"), ("Welcome to St. Clare", "f4jWTiXrIOs", "2021"),
            ("St. Clare College Facilities 2021", "ENCCIBqdPMs", "State-of-the-art facilities"), ("The leading edge in online education system", "S_SYZ1X5Thk", "2021"),
            ("Continuity of Learning", "jwzbf0naZyE", "No one gets left behind"), ("Our Future", "1_vsofl20fQ", "")]
    body = ph("About", "Transforming education, building our future", "St. Clare College of Caloocan is the School of Life Skills and a leading institution for professional development, serving Caloocan since 1985.", "campus-building.jpg", "St. Clare College building on Zabarte Road") \
        + sec(shead("Vision and mission", "Quality, affordable and sustainable education for the total development of every Clarean.") + B.VM) \
        + sec(shead("Leadership") + f'<div class="leaders rv">{leaders}</div>', "alt") \
        + sec(f'<div class="split" style="align-items:start"><div class="rv"><h2>The leading edge in online education</h2><p class="lede mt">Long before the COVID-19 crisis, St. Clare College prepared its ICT capability, so that it was ready to embrace the new normal in education while continuing to provide quality, affordable and sustainable development education.</p></div><ol class="timeline">{hist}</ol></div>') \
        + sec(shead("St. Clare in video", "Officials, facilities and the story of St. Clare Online.") + '<div class="vids">' + "".join(vcard(t, v, w) for t, v, w in vids) + '</div><p class="mt-l rv"><a class="more" href="vms.html">Full video library</a></p>', "alt") \
        + sec(shead("Center for Online Education System", "The technology partners and SCO Online channels behind St. Clare Online.") + f'<div class="logos rv">{partners}</div><h3 class="mt-l" style="margin-bottom:14px">SCO Online channels</h3><div class="channels rv">{chans}</div>') \
        + cta("Visit the campus", "Zabarte Road, Caloocan City. Office hours 9:00 AM to 5:00 PM.")
    page("about.html", "About St. Clare College | Vision, Mission, History & Leadership",
         "Founded in 1985 in Caloocan City, St. Clare College is the School of Life Skills: vision, mission, leadership, history, videos and technology partners.", body)


def build_academics():
    ter = "".join(f'<article class="prog-row rv" id="{code.split()[0].lower().replace("/", "")}"><figure class="photo">{simg(img, name)}</figure><div><span class="code">{code}</span><h3>{name}</h3><p>{desc}</p></div></article>' for code, name, img, desc in TERTIARY_FULL)
    shs = "".join(f'<article class="prog-row rv"><figure class="photo">{simg(img, name)}</figure><div><h3>{name}</h3><p>{desc}</p></div></article>' if img else f'<article class="prog-row rv"><div class="noimg">{name}</div><div><h3>{name}</h3><p>{desc}</p></div></article>' for name, img, desc in SHS_FULL)
    bas = "".join(f'<div class="cp rv" style="--d:{i}"><figure class="photo">{simg(img, n)}</figure><h3>{n}</h3><p>{d}</p></div>' for i, (n, img, d) in enumerate(BASIC_FULL))
    body = ph("Academics", "Programmes for every stage", "Basic Education, Senior High School and eight college degrees, taught on campus, online or blended.", "virtual-lab-predator.jpg", "The St. Clare Virtual Lab") \
        + sec(shead("College degrees", "Eight bachelor's degree programmes: BSHM, BSBA, BSCS, BEEd, BSEd-English, BSEd-Math, BSTM and AB Political Science.") + f'<div class="prog-rows">{ter}</div>', "", "tertiary") \
        + sec(shead("Senior High School", "Academic, Arts & Design and Technical-Vocational-Livelihood tracks.") + f'<div class="prog-rows">{shs}</div>', "alt", "shs") \
        + sec(shead("Basic Education", "Nursery to Grade 10.") + f'<div class="cards-photo">{bas}</div>', "", "basic") \
        + sec(shead("Programme fliers") + gallery(FLIERS, "contain"), "alt") \
        + cta("Find the right programme", "Talk to admissions about the programme that fits your goals.")
    page("academics.html", "Academics | St. Clare College Programmes",
         "College degrees (BSHM, BSBA, BSCS, BEEd, BSEd, BSTM, AB PolSci), Senior High tracks (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and Basic Education at St. Clare College.", body)


def build_admissions():
    tabs, panels = [], []
    for i, (k, (label, ab, items)) in enumerate(REQ.items()):
        sel = i == 0
        tabs.append(f'<button role="tab" id="rt-{k}" aria-controls="rp-{k}" aria-selected="{"true" if sel else "false"}"{"" if sel else " tabindex=\"-1\""} data-hash="{k}">{label}</button>')
        panels.append(f'<div role="tabpanel" id="rp-{k}" aria-labelledby="rt-{k}"{"" if sel else " hidden"}>{checklist(items)}</div>')
    faq = [
        ("Can I enroll online?", f'Yes. Online enrollment is through the IMS: <a href="ims.html">St. Clare IMS</a>. You can also enroll on campus in three steps.'),
        ("Can I study fully online?", "Yes. St. Clare College offers two modalities: full online and blended (online plus on-campus days)."),
        ("How do I get my class schedule?", 'After paying the matriculation fee and filling up your registration form, go to the Library on the 3rd floor for enlistment. Schedules and sectioning are posted in the <a href="lms.html">LMS</a> and emailed by your Program Head.'),
        ("When does enrollment open, and how much are the fees?", f"Call the admissions office at {PHONE} or email {EMAIL} to confirm this school year's enrollment dates and fees."),
        ("Are there scholarships?", 'Ask admissions for this school year\'s offers. Submit a certificate of indigency for scholarship consideration. UniFAST-TES grantees verify their status and schedule on the <a href="pms.html#tes">PMS</a>.'),
        ("How do I request my Transcript of Records or diploma?", 'Only through the <a href="pms.html#documents">Official Document Request Portal</a>. Do not transact with fixers.'),
    ]
    faqs = "".join(f'<details><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in faq)
    body = ph("Admissions", "Enroll at St. Clare", "Three steps on campus or online through the IMS, one long brown envelope of requirements, and you are a Clarean.", "graduates.jpg", "St. Clare College graduates",
              f'<div class="actions"><a class="btn gold" href="#steps">See the 3 steps {ARROW}</a><a class="btn line" href="ims.html">Enroll online (IMS)</a></div><p class="note-line">Dates and fees for this school year: call <a href="tel:{PHONE_TEL}">{PHONE}</a></p>') \
        + sec(shead("Enrollment procedure", "Proceed in order; each step happens at a specific place on campus.") + steps_html(), "alt", "steps") \
        + sec(shead("Admission requirements", "Select your level. All documents are considered property of the school once submitted for admission.") + f'<div class="tabs" role="tablist" aria-label="Requirement type">{"".join(tabs)}</div>{"".join(panels)}<p class="notebox">Place photocopies of all documents in a long brown envelope. College students can also check the <a href="{LMS["college_corner"][2][1][1]}" rel="noopener" target="_blank">admission requirements sheet</a> in the College Corner; Basic Education families can open the <a href="https://drive.google.com/file/d/1mVPzklhSi-ifSS8QPBUZc8ky0_UkCQiw/view?usp=sharing" rel="noopener" target="_blank">list of school requirements</a>.</p>', "", "requirements") \
        + sec(shead("Enrollment guide", "The official enrollment slides: procedure, requirements, programmes and uniform. Select a slide to enlarge it.") + gallery(ENROLL_SLIDES, "contain"), "alt", "guide") \
        + sec(shead("Forms you will need") + docs(FORMS_DOCS[:2]) + '<p class="mt"><a class="more" href="downloads.html">All forms and memoranda</a></p>') \
        + sec(shead("Learning modality", "Personalized learning pathways: choose full online or blended.") + f"""<div class="callout rv"><div><h3>Full online or blended</h3><p>Learn from anywhere through St. Clare Online (LMS classes, the e-Library and virtual broadcasts), or combine online learning with on-campus days in air-conditioned classrooms with e-boards, laboratories and the Virtual Lab.</p></div>{zoom("poster-flexible-study", "Flexible study options")}</div>""", "alt", "modality") \
        + sec(shead("Scholarships and financial aid", "“An investment in knowledge pays the best interest.” Benjamin Franklin") + f"""<div class="grid3">
  <div class="panel rv"><span class="dated">SY 2024-2025</span><h3>President's Scholarship</h3><p>The SHS Alumni VIP Package for the St. Clare SHS Class of 2024: President's Scholarship and zero down payment. Ask admissions about this year's scholarships.</p></div>
  <div class="panel rv" style="--d:1"><h3>UniFAST-TES</h3><p>Tertiary Education Subsidy grantees verify their status and secure a disbursement schedule on the PMS.</p><p class="mt"><a class="more" href="pms.html#tes">TES guidelines</a></p></div>
  <div class="panel rv" style="--d:2"><h3>Certificate of indigency</h3><p>Optional. Submit it with your requirements to be considered for scholarship.</p></div></div>""", "", "scholarships") \
        + sec(f'<div class="rv"><h2 style="margin-bottom:24px">Frequently asked questions</h2><div class="faq">{faqs}</div></div>', "alt") \
        + cta("Ready to enroll?", "Take the first step towards a brighter tomorrow.")
    page("admissions.html", "Admissions | Enroll at St. Clare College",
         "How to enroll at St. Clare College: three steps on campus or online, requirements by level, the official enrollment guide, forms, modality, scholarships and FAQ.", body)


def build_campus():
    day = [("Monday, 7:00 AM", "Virtual flag ceremony", "The whole community gathers online to start the week."),
           ("Classes", "E-boards in all 95 classrooms", "The first college in the country to replace every blackboard with an e-board."),
           ("Lab time", "Virtual Lab", "VR + AR = MR with the Predator Thronos and the Mixed Reality facility by Acer."),
           ("3rd floor", "Library and Learning Resource Center", "Study space, enlistment and the ProQuest-powered e-Library."),
           ("Broadcasts", "St. Clare Virtual Studio", "Webinars, parents' orientations and commencement broadcasts."),
           ("Every week", "SCO Online channels", ", ".join(n for _, n in SCO_CHANNELS) + ".")]
    dh = "".join(f'<div class="panel rv" style="--d:{i % 3}"><h3>{h}</h3><p class="when">{t}</p><p>{p}</p></div>' for i, (t, h, p) in enumerate(day))
    photos = [("prog-bscs-lab", "Computer laboratory"), ("shs-ict-virtual-lab", "The Virtual Lab"), ("virtual-lab-predator-units", "Predator units in the Virtual Lab"),
              ("prog-bshm", "Hospitality students"), ("shs-tvl-he", "TVL Home Economics"), ("prog-education", "Teacher education"),
              ("basic-kinder", "Kindergarten"), ("prog-bstm", "Tourism management"), ("i-love-st-clare", "I love St. Clare")]
    vids = [("St. Clare College Virtual Lab", "Ncj3mlHUiok", "2021"), ("St. Clare Online: Virtual Lab", "avbXu3J7PoI", "Predator Thronos & Mixed Reality by Acer"), ("St. Clare College Virtual Flag Ceremony", "QSRZvHk7TMA", "Every Monday, 7:00 AM")]
    body = ph("Campus life", "Life at St. Clare", "E-boards in every classroom, a Virtual Lab, our own broadcast channels and a community that keeps learning online.", "virtual-lab-predator.jpg", "The St. Clare Virtual Lab") \
        + sec(shead("A week on campus", "From the Monday flag ceremony to the Virtual Studio.") + f'<div class="grid3">{dh}</div>', "", "virtual-lab") \
        + sec(shead("Campus in pictures") + gallery(photos), "alt") \
        + sec(shead("The Virtual Lab", "Visit St. Clare College and experience the immersive technology behind the Predator Thronos and the Mixed Reality facility by Acer.") + '<div class="vids">' + "".join(vcard(t, v, w) for t, v, w in vids) + "</div>") \
        + sec(f'<div class="split"><figure class="photo rv">{B.img("campus-building.jpg", "St. Clare College campus building", 1600, 900)}<figcaption>The campus on Zabarte Road</figcaption></figure><div class="rv" style="--d:1"><h2>Facilities</h2><ul class="checklist" style="columns:1;margin-top:18px"><li>E-boards in all 95 classrooms</li><li>Air-conditioned classrooms and restrooms</li><li>Computer laboratories with stacked servers</li><li>Library and enlistment area on the 3rd floor</li><li>St. Clare Virtual Studio</li></ul></div></div>', "alt") \
        + sec(f'<div class="split" style="align-items:start"><div class="rv"><h2>Digital citizenship</h2><p class="lede mt">Online learning comes with responsibilities. These policies guide life on St. Clare Online.</p></div>{docs(HANDBOOKS)}</div>', "", "digital-citizenship") \
        + cta("See the campus", "Visit Zabarte Road, Caloocan City, 9:00 AM to 5:00 PM.")
    page("campus-life.html", "Campus Life | St. Clare College",
         "Campus life at St. Clare College: e-board classrooms, the Virtual Lab, SCO Online channels, facilities, photos, videos and digital citizenship policies.", body)


def build_portals():
    svc = [("lms.html", "LMS", "Learning Management System", "Class schedules, class lists and sectioning; College, SHS and Basic Education corners."),
           ("cms.html", "CMS", "Content Management System", "The ProQuest e-Library and downloadable handbooks and manuals."),
           ("ims.html", "IMS", "Institutional Management System", "Online enrollment, faculty attendance and job openings."),
           ("pms.html", "PMS", "Personal Management System", "UniFAST-TES, document requests, digital passport, ePayments and e-grades."),
           ("vms.html", "VMS", "Virtual Management System", "Commencement, broadcasts, webinars and the St. Clare video library."),
           ("downloads.html", "DOC", "Downloadable forms", "Registration, clearance and graduation forms, memoranda and handbooks.")]
    rows = "".join(f'<a class="portal rv" href="{h}"><span class="acr">{k}</span><span><h3>{n}</h3><p>{d}</p></span><span class="go">Open &rarr;</span></a>' for h, k, n, d in svc)
    body = ph("Student services", "St. Clare Online Education System", "Five connected systems for learning, content, enrollment, personal transactions and virtual broadcasting, plus forms and the calendar.") \
        + portal_nav("portals.html") \
        + sec(f'<h2 class="sr-only">Systems</h2><div class="portal-list">{rows}</div>') \
        + sec(shead("Most requested") + f"""<div class="grid3">
  <a class="panel rv" href="lms.html#college"><span class="tag" style="font-size:.85rem">LMS</span><h3>Class schedules and sections</h3><p>College, SHS and Basic Education corners.</p></a>
  <a class="panel rv" style="--d:1" href="pms.html#documents"><span class="tag" style="font-size:.85rem">PMS</span><h3>Official Document Request Portal</h3><p>Transcripts, diplomas and other documents. No fixers.</p></a>
  <a class="panel rv" style="--d:2" href="pms.html#grades"><span class="tag" style="font-size:.85rem">PMS</span><h3>e-Grades</h3><p>Grades by programme and semester.</p></a>
  <a class="panel rv" href="ims.html#faculty"><span class="tag" style="font-size:.85rem">IMS</span><h3>Faculty attendance</h3><p>Basic Ed, SHS and Tertiary online attendance.</p></a>
  <a class="panel rv" style="--d:1" href="cms.html"><span class="tag" style="font-size:.85rem">CMS</span><h3>e-Library</h3><p>Learning Resource Center, powered by ProQuest.</p></a>
  <a class="panel rv" style="--d:2" href="pms.html#epayments"><span class="tag" style="font-size:.85rem">PMS</span><h3>ePayments dropbox</h3><p>Send proof of payment and request your receipt.</p></a></div>""", "alt") \
        + cta("Need help?", f"Call {PHONE} or email {EMAIL}, 9:00 AM to 5:00 PM.")
    page("portals.html", "Student Services | St. Clare Online Education System",
         "St. Clare Online Education System: LMS, CMS, IMS, PMS, VMS, downloadable forms and the calendar.", body)


def build_lms():
    cc_t, cc_s, cc_l = LMS["college_corner"]
    groups = "".join(f'<div class="linkset rv"><h3>{esc(t)}</h3>{links(items)}</div>' for t, items in LMS["groups"])
    body = ph("LMS", "Learning Management System", LMS["intro"]) + portal_nav("lms.html") \
        + sec(f'<div class="callout rv" id="college"><div><h2>{cc_t}</h2><p>{cc_s}</p>{links(cc_l)}</div>{zoom("online-learning", "Online learning")}</div>') \
        + sec(shead("Welcome Clareans!", LMS["welcome"]) + f'<div class="linkgrid">{groups}</div>' + SRC_NOTE, "alt") \
        + cta("Questions about your schedule?", f"Contact your Program Head or call {PHONE}.")
    page("lms.html", "LMS | St. Clare College Learning Management System",
         "St. Clare College LMS: College Corner, class schedules, class lists and sectioning, SHS Corner and Basic Education Corner.", body)


def build_cms():
    t, s, url = CMS["elibrary"]
    body = ph("CMS", "Content Management System", CMS["intro"]) + portal_nav("cms.html") \
        + sec(f'<div class="callout rv"><div><h2>{t}</h2><p>{s}</p><a class="btn" href="{url}" rel="noopener" target="_blank">Open the e-Library {ARROW}</a></div>{zoom("poster-elibrary-proquest", "St. Clare College Learning Resource Center, powered by ProQuest")}</div>') \
        + sec(shead("Downloadable handbooks and manuals") + docs(HANDBOOKS), "alt") \
        + cta("Need a document?", 'Forms and memoranda are on the downloads page.')
    page("cms.html", "CMS | St. Clare College e-Library & Handbooks",
         "St. Clare College CMS: the ProQuest e-Library and downloadable handbooks (Student Handbook, ID Policy, Digital Passport, Digital Citizenship, Institutional Email, Data Privacy Manual).", body)


def build_ims():
    ft, fitems = IMS["faculty"]
    fac = "".join(f'<div class="linkset rv"><h3>{esc(h)}</h3>{links([(lab, u)])}</div>' for h, lab, u in fitems)
    ht, hs, quals, mail, addr = IMS["hiring"]
    body = ph("IMS", "Institutional Management System", IMS["intro"]) + portal_nav("ims.html") \
        + sec(shead("Online enrollment", "Simplified and seamless: enroll online with ease. Pre-school to Junior High, Senior High School (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and Tertiary (BEEd, BSEd-Eng, BSEd-Math, BSCS, BSBA, BSHM, BSTM, AB PolSci).") + gallery([("poster-online-enrollment", "Online enrollment"), ("poster-enrolment-2023", "Enrolment going on, SY 2023-2024"), ("slide-enrollment-procedure", "Enrollment procedure")], "contain") + '<p class="mt-l"><a class="more" href="admissions.html#steps">Step-by-step enrollment guide</a></p>') \
        + sec(shead(ft, "Faculty log-in / time-in for virtual classes' attendance.") + f'<div class="grid3">{fac}</div>' + SRC_NOTE, "alt", "faculty") \
        + sec(f'<div class="callout rv" id="hiring"><div><h3>{ht}</h3><p>{hs}</p>{checklist(quals)}<p class="mt"><a class="btn" href="{mail}">Submit your application {ARROW}</a></p><p class="src-note">Email: {addr}</p></div>{zoom("poster-hiring", "We are hiring: Basic Education and Senior High School teachers")}</div>') \
        + cta()
    page("ims.html", "IMS | St. Clare College Institutional Management System",
         "St. Clare College IMS: online enrollment, faculty attendance monitoring and teaching job openings.", body)


def build_pms():
    tt, steps = PMS["tes"]
    st = "".join(f'<li class="rv"><h3>{h}</h3><p>{p}</p><a class="btn sm" href="{u}" rel="noopener" target="_blank">{b}</a></li>' for h, p, b, u in steps)
    def call(key, id_):
        t, s, u, im = PMS[key]
        return f'<div class="callout rv" id="{id_}"><div><h3>{t}</h3><p>{s}</p><a class="btn" href="{u}" rel="noopener" target="_blank">Open the form {ARROW}</a></div>{zoom(im, t)}</div>'
    grades = "".join(f'<div class="linkset rv"><h3>{esc(t)}</h3>{links(items)}</div>' for t, items in PMS["grades"])
    tes_archive = gallery([("poster-tes-late-claims-f2f", "UniFAST-TES late claims: face-to-face"), ("poster-tes-late-claims-bank", "UniFAST-TES late claims: bank transfer"), ("poster-tes-2020", "Application for TES, A.Y. 2020-2021")], "contain")
    body = ph("PMS", "Personal Management System", PMS["intro"]) + portal_nav("pms.html") \
        + sec(shead(tt) + f'<ol class="steps2">{st}</ol><h3 class="mt-l" style="margin-bottom:14px">Earlier TES notices</h3>{tes_archive}', "", "tes") \
        + sec(call("docreq", "documents"), "alt") \
        + sec(call("passport", "passport")) \
        + sec(call("epay", "epayments"), "alt") \
        + sec(shead("e-Grades", "Grades by programme and semester.") + f'<div class="linkgrid">{grades}</div>' + SRC_NOTE, "", "grades") \
        + cta("Need help with a transaction?", f"Call {PHONE} or email {EMAIL}, 9:00 AM to 5:00 PM.")
    page("pms.html", "PMS | St. Clare College Personal Management System",
         "St. Clare College PMS: UniFAST-TES verification and scheduling, Official Document Request Portal, digital passport, ePayments dropbox and e-grades.", body)


def build_vms():
    def slug(t): return t.lower().split(":")[0].replace("&", "and").replace(" ", "-").replace(",", "")
    jump = '<nav class="jump" aria-label="Video categories">' + "".join(f'<a href="#{slug(g)}">{esc(g)}</a>' for g, _ in VIDEOS) + "</nav>"
    groups = "".join(f'<div class="vgroup" id="{slug(g)}"><h3>{esc(g)}</h3><div class="vids">' + "".join(vcard(t, v, w) for t, v, w in vs) + "</div></div>" for g, vs in VIDEOS)
    n = sum(len(v) for _, v in VIDEOS)
    body = ph("VMS", "Virtual Management System", VMS_INTRO) + portal_nav("vms.html") \
        + sec(shead("Video library", f"{n} videos from St. Clare College: commencement exercises, broadcasts, webinars and more.") + jump + groups) \
        + sec(f'<div class="split rv"><div><h2>Subscribe on YouTube</h2><p class="lede mt">Follow St. Clare College for new broadcasts and ceremonies.</p></div><div><a class="btn" href="{YT}" rel="noopener" target="_blank">St. Clare College on YouTube {ARROW}</a></div></div>', "alt")
    page("vms.html", "VMS | St. Clare College Video Library",
         "St. Clare College VMS video library: commencement exercises 2020-2024, the Professional Mace, Virtual Lab, broadcasts, linkages, Start Up Module and webinar series.", body)


def build_downloads():
    body = ph("Downloads", "Forms and documents", "Institutional forms, guidelines, memoranda and handbooks from St. Clare College.") + portal_nav("downloads.html") \
        + sec(shead("Institutional forms and guidelines") + docs(FORMS_DOCS)) \
        + sec(shead("Institutional memoranda") + docs(MEMOS), "alt") \
        + sec(shead("Handbooks and manuals") + docs(HANDBOOKS)) \
        + sec(shead("Health survey form", "For the students, parents, teachers and non-teaching personnel of St. Clare College only.") + f'<a class="btn" href="{HEALTH_SURVEY}" rel="noopener" target="_blank">Open the health survey form {ARROW}</a>', "alt") \
        + cta()
    page("downloads.html", "Downloadable Forms | St. Clare College",
         "Download St. Clare College forms: registration, health declaration, clearance, curriculum guide guidelines, exit interview, graduation waiver, TES sharing agreement, memoranda and handbooks.", body)


def build_calendar():
    def rows(items): return '<ul class="events">' + "".join(f'<li class="rv"><span class="d">{esc(d)}</span><div><h3>{esc(h)}</h3><p>{esc(p)}</p></div><span class="w">{esc(w)}</span></li>' for d, h, w, p in items) + "</ul>"
    body = ph("Calendar", "Calendar of activities", "Key dates for students, parents and faculty of St. Clare College.") + portal_nav("calendar.html") \
        + sec(shead("2025") + rows(CAL_2025)) \
        + sec(shead("2020 archive") + rows(CAL_2020), "alt") \
        + cta("Questions about a schedule?", f"Call {PHONE}, 9:00 AM to 5:00 PM.")
    page("calendar.html", "Calendar | St. Clare College", "St. Clare College calendar of activities: classes, orientations, webinars, Foundation Day and Feast of St. Clare.", body)


def build_news():
    items = []
    for i, (date, title, text, imgslug, vid) in enumerate(NEWS_FULL):
        if vid: media = yt(vid, title)
        elif imgslug: media = zoom(imgslug, title)
        else: media = ""
        extra = ""
        if title.startswith("Health Survey"): extra = f'<p><a class="more" href="{HEALTH_SURVEY}" rel="noopener" target="_blank">Open the health survey form</a></p>'
        if "UniFAST guidelines" in title: extra = '<p><a class="more" href="pms.html#tes">TES guidelines on the PMS</a></p>'
        if "leading edge" in title: extra = '<p><a class="more" href="about.html">Read the full history</a></p>'
        items.append(f'<article class="item rv"><div class="media">{media}</div><div><span class="date">{esc(date)}</span><h3>{esc(title)}</h3><p>{esc(text)}</p>{extra}</div></article>')
    body = ph("News", "News and announcements", "Milestones, scholarships, advisories and stories from the St. Clare community.") \
        + sec(f'<h2 class="sr-only">All news</h2><div class="archive">{"".join(items)}</div>') + cta()
    page("news.html", "News | St. Clare College", "News and announcements from St. Clare College of Caloocan: enrollment, scholarships, UniFAST-TES, the Professional Mace and more.", body)


def build_all():
    B.build_contact()
    build_home(); build_about(); build_academics(); build_admissions(); build_campus(); build_portals()
    build_lms(); build_cms(); build_ims(); build_pms(); build_vms(); build_downloads(); build_calendar(); build_news()

if __name__ == "__main__":
    build_all()
