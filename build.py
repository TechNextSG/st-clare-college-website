# St. Clare College website - static page builder.
# Facts come only from stclareonline.com (Oct 2026 snapshot). Run: python build.py
import os, html

OUT = os.path.dirname(os.path.abspath(__file__))
SRC = "https://stclareonline.com"
PHONE = "(02) 8232-4483"
PHONE_TEL = "+63282324483"
EMAIL = "stclarecollege.ph@gmail.com"
ADDRESS = "Zabarte Road, Barangay 172, Camarin, Caloocan City 1400, Metro Manila"
FB = "https://www.facebook.com/stclarecollege"
YT = "https://www.youtube.com/channel/UCxlcF5cS_spNnil5pp5-aNQ"

FONTS = ("https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,700..900"
         "&family=Figtree:wght@400;600;700;800&family=Fraunces:ital,opsz,wght@1,9..144,400&display=swap")

NAV = [("index.html", "Home"), ("about.html", "About"), ("academics.html", "Academics"),
       ("admissions.html", "Admissions"), ("campus-life.html", "Campus Life"),
       ("portals.html", "Portals"), ("news.html", "News"), ("contact.html", "Contact")]

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

ICONS = {
    "code": '<path d="M8 6l-6 6 6 6M16 6l6 6-6 6M14 4l-4 16"/>',
    "chef": '<path d="M6 13.9A4 4 0 1 1 7.5 6a5 5 0 0 1 9 0A4 4 0 1 1 18 13.9V20H6z"/><path d="M6 17h12"/>',
    "plane": '<path d="M2 16l20-8-4 12-6-4-4 4v-6"/>',
    "chart": '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    "book": '<path d="M2 4h7a3 3 0 0 1 3 3v14a2 2 0 0 0-2-2H2z"/><path d="M22 4h-7a3 3 0 0 0-3 3v14a2 2 0 0 1 2-2h8z"/>',
    "abc": '<path d="M4 20l4-12 4 12M5.5 16h5"/><path d="M15 8h3a2 2 0 0 1 0 4h-3zM15 12h3.5a2 2 0 0 1 0 4H15z"/>',
    "sigma": '<path d="M18 4H6l6 8-6 8h12"/>',
    "column": '<path d="M3 21h18M5 21V10M9 21V10M15 21V10M19 21V10M2 10l10-6 10 6z"/>',
}

def icon(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

FB_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v8h4v-8h3l1-4h-4V8z"/></svg>'
YT_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23 7.5a3 3 0 0 0-2.1-2.1C19 5 12 5 12 5s-7 0-8.9.4A3 3 0 0 0 1 7.5 31 31 0 0 0 .6 12 31 31 0 0 0 1 16.5a3 3 0 0 0 2.1 2.1C5 19 12 19 12 19s7 0 8.9-.4a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .4-4.5 31 31 0 0 0-.4-4.5zM9.8 15V9l5.2 3z"/></svg>'

# ---------------------------------------------------------------- content
TERTIARY = [
    ("BSCS", "Bachelor of Science in Computer Science", "code", "College of Computing",
     "Proficiency in designing, writing and developing computer programs and computer networks: algorithms, software applications, data processing, web development, programming and computer architecture.",
     "Lectures build the theory; the key learning happens in the computer laboratories, working hands-on with software, programming tools and real hardware.",
     ["Programming", "Web development", "Networks", "Computer architecture"]),
    ("BSHM", "Bachelor of Science in Hospitality Management", "chef", "Hospitality & Tourism",
     "Competencies to run operations and management functions across the hospitality industry.",
     "Covers food production (culinary), accommodation, food and beverage service, tourism planning and product development, events planning, and travel and tour operations.",
     ["Culinary", "Accommodation", "F&B service", "Events"]),
    ("BSTM", "Bachelor of Science in Tourism Management", "plane", "Hospitality & Tourism",
     "Operational and management competencies for hospitality, tourism and their emerging sectors.",
     "Food production, accommodation, food and beverage service, tourism planning and product development, events planning, transportation services, and travel and tour operations.",
     ["Tourism planning", "Travel & tours", "Transport services", "Events"]),
    ("BSBA", "Bachelor of Science in Business Administration", "chart", "Business",
     "Knowledge, skills and attitude to provide quality service in business and industry.",
     "Students practise the basic functions of management (planning, organizing, leading and controlling) through theory classes, practicum exercises and experiential learning.",
     ["Management", "Practicum", "Experiential learning"]),
    ("BEEd", "Bachelor of Elementary Education", "book", "Teacher Education",
     "An undergraduate teacher-education degree designed to prepare individuals intending to teach at the elementary level.",
     "",
     ["Teaching", "Elementary level"]),
    ("BSEd-Eng", "Bachelor of Secondary Education, Major in English", "abc", "Teacher Education",
     "Competencies to teach English at the secondary level.",
     "An undergraduate teacher-education programme with adequate and relevant competencies for your chosen specialization.",
     ["Teaching", "English", "Secondary level"]),
    ("BSEd-Math", "Bachelor of Secondary Education, Major in Math", "sigma", "Teacher Education",
     "Competencies to teach Mathematics at the secondary level.",
     "An undergraduate teacher-education programme with adequate and relevant competencies for your chosen specialization.",
     ["Teaching", "Mathematics", "Secondary level"]),
    ("AB PolSci", "Bachelor of Arts in Political Science", "column", "Social Sciences",
     "Prepares you for a professional career in government service, or for careers dealing with public issues and problems.",
     "Core competencies are expressed as observable behaviours, and the curriculum exposes students to a variety of programme work and activities for a broad understanding of the field.",
     ["Government", "Public issues", "Policy"]),
]

SHS = [
    ("ABM", "Accountancy, Business & Management", "Academic track",
     "Foundational concepts in corporate operations, financial management and business management.", []),
    ("HUMSS", "Humanities & Social Sciences", "Academic track",
     "Human behaviour and societal change, and the analysis of arts, culture, literature and politics: political science, anthropology, linguistics, psychology and communication.", []),
    ("A&D", "Arts & Design", "Arts & Design track",
     "For the design, performance and creative industries. Exposure to architecture, interior and industrial design, graphic design, animation, painting, fashion design, photography and film, with employment skills to start a creative career after graduation.", []),
    ("ICT", "TVL - Information & Communications Technology", "Technical-Vocational-Livelihood",
     "Uses information and communications technology to support, enhance and optimize the delivery of information, with a focus on communication.",
     ["Computer Programming", "Animation"]),
    ("HE", "TVL - Home Economics", "Technical-Vocational-Livelihood",
     "Hands-on livelihood skills with TESDA competency-based assessment for National Certification (NC), which raises employability after SHS and leads into business, culinary, hospitality, tourism, nutrition, fashion and interior-design degrees.",
     ["Bread & Pastry Production", "Food & Beverage Services", "Housekeeping", "Local Guiding Services", "Travel Services"]),
]

BASIC = [
    ("K", "Nursery & Kindergarten", "Nurturing young minds: where curiosity and growth blossom."),
    ("1-6", "Elementary", "Building strong foundations: empowering students for lifelong learning."),
    ("7-10", "Junior High School", "Unlocking potential, shaping futures: a journey of growth and discovery."),
]

CHANNELS = [("Health Talk", "Wellness"), ("Sports Desk", "Athletics"), ("Leading Women", "Voices"),
            ("Virtual Lab", "Innovation"), ("Digital First", "Technology"), ("Heart of a Champion", "Stories"),
            ("Education That Matters", "Learning")]

STEPS = [
    ("Pay the matriculation fee", "Cashier",
     ["Proceed to the cashier and pay the matriculation fee (designated cashier only).", "Get and keep your OFFICIAL RECEIPT."]),
    ("Fill up the registration form", "Lobby",
     ["Go to the LOBBY and present your Official Receipt to the Enrollment Officer.", "Fill up the REGISTRATION FORM.", "Check that your SUBJECTS are listed on the registration form."]),
    ("Register online for your schedule", "Library, 3rd floor",
     ["Proceed to the LIBRARY on the 3rd floor for ENLISTMENT at stclareonline.com/ims.", "Your section and schedule are posted on the website and sent by email by your Program Head."]),
]

REQ = {
    "freshmen": ("College freshmen", "CF", [
        "Senior High School graduate of a public or private school",
        "SHS diploma or certificate of completion",
        "Graduating SHS students: latest grading report card as reflected in the original F138 or report card",
        "PSA or local civil registry birth certificate",
        "2x2 ID photos, recent (2 pcs.)",
        "Certificate of indigency (optional, for scholarship)",
        "Photocopies of all the documents above",
        "1 long brown envelope"]),
    "transferees": ("College transferees", "TR", [
        "PSA or local civil registry birth certificate",
        "2x2 ID photos, recent (2 pcs.)",
        "Transcript of records",
        "Certificate of honorable dismissal",
        "Course description for evaluation",
        "Certificate of indigency (optional, for scholarship)",
        "Photocopies of all the documents above",
        "1 long brown envelope"]),
    "basic": ("Pre-school to Grade 10", "BE", [
        "Photocopy of PSA birth certificate",
        "2 pcs. 2x2 photo",
        "Form 138 or report card (new / transferee)",
        "Form 137 (new / transferee)",
        "Good moral certificate",
        "Long brown envelope"]),
    "shs": ("Senior High School", "SH", [
        "Photocopy of PSA birth certificate",
        "Photocopy of Grade 10 diploma",
        "Form 138 or report card",
        "2 pcs. 2x2 photo",
        "Long brown envelope",
        "Secondary requirements: Form 137 and good moral certificate",
        "Voucher certificate (for private school completers only)"]),
}

FORMS = [
    ("PDF", "Fillable Registration / Enrollment Form", "Admissions"),
    ("PDF", "Health Declaration Form", "Admissions"),
    ("PDF", "SCC Clearance Form 2023", "Registrar"),
    ("PDF", "Guidelines for the Releasing of Curriculum Guide", "Registrar"),
    ("PDF", "Exit Interview Form (CGS-0010)", "Guidance"),
    ("PDF", "Waiver & Application for Graduation 2024", "Registrar"),
    ("DOC", "TES Sharing Agreement, 2023-2024 onwards", "UniFAST-TES"),
    ("PDF", "Memo: Requirements for Graduation (4 May 2023)", "Memorandum"),
    ("PDF", "Memo: Guidelines on Off-Campus Activities (5 May 2023)", "Memorandum"),
]

HANDBOOKS = ["SCC ID Policy", "Student Handbook", "St. Clare College Digital Passport Policy",
             "Digital Citizenship (students' copy)", "Institutional Email", "SCC Data Privacy Manual 2021"]

PORTALS = [
    ("LMS", "Learning Management System", "Courses, materials, tests and progress tracking. Check class schedules, teachers, sectioning and your enrollment status.", "lms"),
    ("CMS", "Content Management System", "The e-Library of the St. Clare College Learning Resource Center, powered by ProQuest, plus downloadable handbooks and manuals.", "cms"),
    ("IMS", "Institutional Management System", "Online enrollment for students, and log-in / time-in attendance for faculty in virtual classes.", "ims"),
    ("PMS", "Personal Management System", "Your personal account for transactions: UniFAST-TES verification and scheduling, and the Official Document Request Portal.", "pms"),
    ("VMS", "Virtual Management System", "Broadcasting and Teacher-DJ: the virtual flag ceremony, commencement exercises and the St. Clare College broadcast.", "vms"),
]

NEWS = [
    ("Sept 23, 2023", "Institution", "The Professional Mace: the eternal flame of professionalism",
     "St. Clare College introduced its Professional Mace, “a beacon of professionalism and culture of excellence.”", "", "mace", SRC + "/"),
    ("Class of 2024", "Scholarship", "SHS Alumni VIP Package for St. Clare graduates",
     "St. Clare SHS Class of 2024 graduates who continued to college could avail of the President's Scholarship with zero down payment for SY 2024-2025.", "graduates.jpg", "", SRC + "/news"),
    ("June 2024", "Commencement", "The Stars of 2024: 38th Commencement Exercises",
     "St. Clare College celebrated its 38th Commencement Exercises in June 2024, streamed on the Virtual Management System.", "", "38th", SRC + "/vms"),
    ("SY 2023-2024", "UniFAST-TES", "Releasing of UniFAST-TES guidelines",
     "Verify your TES grantee status, then secure your official disbursement schedule through the Personal Management System.", "", "TES", SRC + "/pms"),
    ("Advisory", "Registrar", "Official Document Request Portal",
     "Requests for official school documents, such as Transcripts of Records and diplomas, are processed only through the Official Document Request Portal. Do not transact with fixers.", "", "TOR", SRC + "/pms"),
    ("See IMS", "Careers", "We are hiring teachers and instructors",
     "Basic Education teachers, SHS teachers and college instructors: NC II holder or equivalent, Licensed Professional Teacher, good communication and computer skills, good moral character and trainable.", "", "Hiring", SRC + "/ims"),
    ("2025", "Parents", "Parents' Webinar Orientation",
     "Webinar orientations for tertiary, Basic Education and Senior High parents, held at the St. Clare Virtual Studio.", "", "Live", SRC + "/calendar"),
    ("Every Monday", "Broadcast", "Virtual Flag Ceremony at 7:00 AM",
     "The St. Clare College community gathers online every Monday at 7:00 AM.", "", "7AM", SRC + "/vms"),
    ("e-Library", "Learning resources", "Better learning anytime, anywhere, anyhow",
     "The St. Clare College Learning Resource Center e-Library is powered by ProQuest.", "", "e-Lib", SRC + "/cms"),
]

EVENTS = [
    ("Aug", "31", "Foundation Day", "St. Clare College was founded in 1985 (36th anniversary in 2021).", "Campus"),
    ("Sep 2025", "1-4", "Class Orientation & Sectioning", "Meet & greet with your teachers, advisers, instructors and professors. Sectioning for students not yet enlisted.", "St. Clare College"),
    ("Mon", "7AM", "Virtual Flag Ceremony", "Every Monday, streamed for the whole community.", "Online"),
    ("2025", "Web", "Parents' Webinar Orientation", "Tertiary 1-3 PM; Basic Education 9 AM; Senior High 1 PM.", "Virtual Studio"),
]

# ---------------------------------------------------------------- layout
def head(title, desc, page):
    three = ""
    return f"""<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="#070a2b">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="img/campus-building.jpg">
<link rel="icon" href="img/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="assets/site.css">{three}
<script src="assets/site.js" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
"""

def header(page):
    links = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == page else ""}>{t}</a>' for h, t in NAV)
    return f"""<div class="topbar"><div class="wrap">
  <div class="tb-left"><a href="tel:{PHONE_TEL}">{PHONE}</a><a class="hide-sm" href="mailto:{EMAIL}">{EMAIL}</a><span class="hide-sm">Office hours 9:00 AM - 5:00 PM</span></div>
  <div class="tb-right"><span class="pill">SCO Online</span><a href="{SRC}/lms" rel="noopener">LMS</a><a href="{SRC}/ims" rel="noopener">IMS</a><a href="{SRC}/downloadable-forms" rel="noopener">Forms</a></div>
</div></div>
<header class="site-header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="St. Clare College home">
    <img src="img/seal-200.webp" alt="St. Clare College of Caloocan seal" width="50" height="50">
    <span><b>St. Clare College</b><small>The School of Life Skills</small></span>
  </a>
  <button class="menu-btn" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span></button>
  <nav class="nav" id="nav" aria-label="Main">{links}<a class="btn" href="admissions.html">Enroll now</a></nav>
</div></header>
<main id="main">
"""

def footer():
    return f"""</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="foot-brand"><img src="img/seal-200.webp" alt="" width="64" height="64"><div><b>St. Clare College</b><span>of Caloocan</span></div></div>
        <p>The School of Life Skills and leading institution for professional development. Serving Caloocan since 1985; online through St. Clare Online since 2020.</p>
        <div class="socials"><a href="{FB}" rel="noopener" aria-label="St. Clare College on Facebook">{FB_SVG}</a><a href="{YT}" rel="noopener" aria-label="St. Clare College on YouTube">{YT_SVG}</a></div>
      </div>
      <div><h3>Explore</h3><ul><li><a href="about.html">About St. Clare</a></li><li><a href="academics.html">Academics</a></li><li><a href="admissions.html">Admissions</a></li><li><a href="campus-life.html">Campus Life</a></li><li><a href="news.html">News</a></li></ul></div>
      <div><h3>St. Clare Online</h3><ul>{"".join(f'<li><a href="{SRC}/{p[3]}" rel="noopener">{p[0]} - {p[1].split()[0]}</a></li>' for p in PORTALS)}<li><a href="{SRC}/downloadable-forms" rel="noopener">Downloadable forms</a></li></ul></div>
      <div><h3>Visit</h3><ul><li>{ADDRESS}</li><li><a href="tel:{PHONE_TEL}">{PHONE}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li>9:00 AM - 5:00 PM</li></ul></div>
    </div>
    <div class="foot-bottom"><span>&copy; <span data-year>2026</span> St. Clare College of Caloocan &middot; St. Clare Online Education System&reg;</span><a class="sdg" href="https://sdgs.un.org/goals/goal4" rel="noopener" style="padding:6px 14px 6px 6px"><b style="width:32px;height:32px;font-size:1rem">4</b><span>Quality Education</span></a></div>
  </div>
  <p class="big" aria-hidden="true">St. Clare</p>
</footer>
<button class="to-top" aria-label="Back to top">&uarr;</button>
</body>
</html>
"""

def page(name, title, desc, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(head(title, desc, name) + header(name) + body + footer())
    print("wrote", name)

def phero(crumb, h1, lead, img=None, extra=""):
    im = f'<div class="ph-img"><img src="img/{img}" alt="" loading="eager"></div>' if img else ""
    return f"""<section class="phero noise">
  <canvas class="fx-canvas" aria-hidden="true"></canvas><div class="grid-floor" aria-hidden="true"></div>{im}
  <div class="wrap">
    <div class="crumbs"><a href="index.html">Home</a><span>/</span><span>{crumb}</span></div>
    <h1 data-split>{h1}</h1>
    <p class="lead rv" style="--d:3">{lead}</p>{extra}
  </div>
</section>
"""

def cta(h, p):
    return f"""<section class="cta brandband pad noise">
  <canvas class="fx-canvas" data-tone="gold" aria-hidden="true"></canvas><div class="grid-floor" aria-hidden="true"></div>
  <div class="wrap" style="position:relative">
    <h2 data-split>{h}</h2>
    <p class="lead rv">{p}</p>
    <div class="btn-row rv" style="--d:2"><a class="btn" href="admissions.html">Start your enrollment {ARROW}</a><a class="btn ghost" href="contact.html">Talk to admissions</a></div>
  </div>
</section>
"""

def prog_card(p, i):
    code, name, ic, school, short, _, tags = p
    return f"""<article class="prog rv" style="--d:{i % 4}">
  <span class="ico">{icon(ic)}</span>
  <span class="code">{code}</span>
  <h3>{name}</h3>
  <p>{short}</p>
  <div class="tags">{"".join(f"<span>{t}</span>" for t in tags[:3])}</div>
</article>"""

def steps_html():
    out = []
    for i, (h, where, items) in enumerate(STEPS):
        out.append(f"""<article class="step" style="--i:{i}">
  <span class="n">0{i + 1}</span>
  <div><h3>{h}</h3><ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>
  <span class="where">{where}</span>
</article>""")
    return '<div class="steps">' + "".join(out) + "</div>"

VM = """<div class="vm">
  <article class="rv" data-big="Vision"><span class="tag">Vision</span><p>To become the leading institution for professional development and the first and foremost provider of quality, affordable and sustainable development education.</p></article>
  <article class="rv" style="--d:1" data-big="Mission"><span class="tag">Mission</span><p>To provide quality and excellent global education for the total development of a responsible, innovative, skillful and professional global workforce whose values and dignity are beyond par.</p></article>
</div>"""

MACE = """<section class="mace dark pad noise">
  <div class="glow" aria-hidden="true"></div>
  <div class="wrap">
    <div class="flame rv-s" aria-hidden="true"><i></i><i></i><i></i></div>
    <span class="eyebrow">St. Clare College Professional Mace</span>
    <h2 data-split>The eternal flame <span class="grad-text">of professionalism</span></h2>
    <blockquote class="rv">&ldquo;A beacon of professionalism and culture of excellence.&rdquo;</blockquote>
    <cite class="rv">By ERA &amp; EJA &middot; September 23, 2023</cite>
  </div>
</section>
"""

def channels_html():
    tiles = ['<div class="chan logo rv-s"><img src="img/sco-online.webp" alt="SCO Online logo" width="256" height="256" loading="lazy"></div>']
    for i, (n, k) in enumerate(CHANNELS):
        tiles.append(f'<article class="chan rv-s" style="--d:{(i + 1) % 4}"><span class="k">SCO &middot; {k}</span><h3>{n}</h3></article>')
    return '<div class="channels">' + "".join(tiles) + "</div>"

VLAB = f"""<div class="split">
  <div>
    <span class="eyebrow">St. Clare Virtual Lab</span>
    <h2 data-split>Immersion, <span class="grad-text">reimagined</span></h2>
    <p class="lead rv">Another first from St. Clare College: a Virtual Lab that brings immersive technology into the classroom.</p>
    <div class="equation rv" aria-label="Virtual Reality plus Augmented Reality equals Mixed Reality">
      <span class="term">VR<small>Virtual reality</small></span><span class="op">+</span>
      <span class="term">AR<small>Augmented reality</small></span><span class="op">=</span>
      <span class="term res">MR<small>Mixed reality</small></span>
    </div>
    <p class="rv" style="color:var(--on-dark-muted);margin-top:40px">Experience the technology behind the <b style="color:#fff">Predator Thronos</b> and the <b style="color:#fff">Mixed Reality facility by Acer</b>. Opened in 2021, the Virtual Lab welcomed visitors from 10:00 AM to 5:00 PM. Ask admissions about a visit.</p>
    <a class="btn rv" href="campus-life.html#virtual-lab">Explore the Virtual Lab {ARROW}</a>
  </div>
  <div class="media-stack rv-s">
    <div class="media tall"><img src="img/virtual-lab-predator.jpg" alt="Predator gaming stations inside the St. Clare Virtual Lab" loading="lazy" width="1600" height="1066"></div>
    <div class="float"><img src="img/vr-student.jpg" alt="Student wearing a VR headset" loading="lazy" width="868" height="1030"></div>
  </div>
</div>"""

MODALITY = """<div class="modality">
  <article class="mode rv" data-tilt>
    <span class="eyebrow">Modality 01</span>
    <div class="big">Full<br>online</div>
    <p>Learn from anywhere through St. Clare Online: LMS classes, the e-Library and virtual broadcasts.</p>
    <div class="meter" style="--w:100%"><i></i></div><div class="meter-l"><span>Online</span><span>On campus</span></div>
  </article>
  <article class="mode rv" style="--d:1" data-tilt>
    <span class="eyebrow">Modality 02</span>
    <div class="big">Blended</div>
    <p>Combine online learning with on-campus days in air-conditioned classrooms, laboratories and the Virtual Lab.</p>
    <div class="meter" style="--w:55%"><i></i></div><div class="meter-l"><span>Online</span><span>On campus</span></div>
  </article>
</div>"""

# ---------------------------------------------------------------- pages
def build_home():
    rail = "".join(prog_card(p, i) for i, p in enumerate(TERTIARY))
    marquee_items = ["Nursery & Kindergarten", "Elementary", "Junior High", "Senior High"] + [p[0] for p in TERTIARY]
    mq = "".join(f"<span>{html.escape(x)}</span>" for x in marquee_items) + "".join(f'<span aria-hidden="true">{html.escape(x)}</span>' for x in marquee_items)
    body = f"""<section class="hero noise">
  <canvas class="fx-canvas" aria-hidden="true"></canvas>
  <div class="grid-floor" aria-hidden="true"></div>
  <div class="wrap">
    <div>
      <span class="hero-tag rv"><b>Enroll online</b> Full online or blended learning</span>
      <h1 data-split>The School <span class="grad-text">of Life</span> Skills</h1>
      <p class="lead rv" style="--d:4">St. Clare College of Caloocan: the leading edge in online education. Nursery to College, one campus on Zabarte Road and one online platform where no one gets left behind.</p>
      <div class="btn-row rv" style="--d:6"><a class="btn" href="admissions.html">Enroll now {ARROW}</a><a class="btn ghost" href="about.html">Take a tour</a></div>
    </div>
    <div class="hero-globe rv-s" id="globe" aria-hidden="true">
      <span class="orbit-label">SCO ONLINE<small>the leading edge in online education</small></span>
      <img class="seal-badge" src="img/seal-200.webp" alt="" width="200" height="202">
    </div>
  </div>
  <a class="hero-scroll" href="#levels"><i></i>Scroll</a>
</section>
<div class="marquee" role="marquee" aria-label="Programmes offered"><div class="track">{mq}</div></div>

<section class="pad-s white">
  <div class="wrap">
    <div class="stats">
      <div class="stat rv"><b>1985</b><span>Serving Caloocan since 31 August 1985</span></div>
      <div class="stat rv" style="--d:1"><b><span data-count="38">38</span><em>th</em></b><span>Commencement Exercises, held in 2024</span></div>
      <div class="stat rv" style="--d:2"><b><span data-count="8">8</span></b><span>College degree programmes</span></div>
      <div class="stat rv" style="--d:3"><b><span data-count="547806" data-comma>547,806</span></b><span>Views of the 2020 St. Clare Online start-up module</span></div>
    </div>
  </div>
</section>

<section class="pad" id="levels">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Three schools, one campus</span><h2 data-split>From first steps <span class="grad-text-brand">to first job</span></h2></div>
      <p class="lead rv">St. Clare College carries learners from Nursery all the way to a college degree, with life skills built in at every level.</p>
    </div>
    <div class="levels">
      <a class="level lv-1 rv" href="academics.html#basic" data-tilt><span class="num">01</span><h3>Basic Education</h3><p>Nursery &amp; Kindergarten, Elementary (Grades 1-6) and Junior High (Grades 7-10).</p><ul><li>Nursery</li><li>Kinder</li><li>Grades 1-10</li></ul><span class="go">Explore Basic Ed</span></a>
      <a class="level lv-2 rv" style="--d:1" href="academics.html#shs" data-tilt><span class="num">02</span><h3>Senior High School</h3><p>Academic, Arts &amp; Design and TVL tracks with TESDA-assessed specializations.</p><ul><li>ABM</li><li>HUMSS</li><li>Arts &amp; Design</li><li>TVL-ICT</li><li>TVL-HE</li></ul><span class="go">Explore SHS</span></a>
      <a class="level lv-3 rv" style="--d:2" href="academics.html#tertiary" data-tilt><span class="num">03</span><h3>Tertiary</h3><p>Eight degree programmes in computing, hospitality, tourism, business, education and political science.</p><ul><li>BSCS</li><li>BSHM</li><li>BSTM</li><li>BSBA</li><li>BEEd</li><li>BSEd</li><li>AB PolSci</li></ul><span class="go">Explore College</span></a>
    </div>
  </div>
</section>

<section class="pad paper-2" data-rail>
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">College programmes</span><h2 data-split>Degrees built <span class="grad-text-brand">for the industry</span></h2></div>
      <div><p class="lead rv">Theory in the classroom, mastery in the laboratory, kitchen and field. Choose the path that fits your future.</p>
        <div class="rail-ctrl rv" style="margin-top:22px" data-rail-ctrl><button data-dir="-1" aria-label="Previous programmes">&larr;</button><button data-dir="1" aria-label="Next programmes">&rarr;</button></div></div>
    </div>
  </div>
  <div class="rail-wrap"><div class="rail" tabindex="0" aria-label="College programmes">{rail}</div></div>
  <div class="wrap"><a class="link-arrow" href="academics.html#tertiary">See full programme details</a></div>
</section>

<section class="dusk pad noise" style="overflow:hidden">
  <canvas class="fx-canvas" aria-hidden="true"></canvas>
  <div class="wrap" style="position:relative">
    <div class="sec-head">
      <div><span class="eyebrow">Choose your modality</span><h2 data-split>Learn your way, <span class="grad-text">succeed your way</span></h2></div>
      <p class="lead rv">Personalized learning pathways: choose the modality that fits your life, full online or blended.</p>
    </div>
    {MODALITY}
  </div>
</section>

<section class="dark pad" style="overflow:hidden"><div class="wrap" style="position:relative">{VLAB}</div></section>

<section class="pad white">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">SCO Online</span><h2 data-split>Stay connected, <span class="grad-text-brand">stay inspired</span></h2></div>
      <p class="lead rv">St. Clare Online is the college's own channel network: wellness, sport, leadership, innovation and the stories of Clareans.</p>
    </div>
    {channels_html()}
  </div>
</section>

{MACE}

<section class="pad">
  <div class="wrap">
    <div class="vip rv-s">
      <div class="txt">
        <span class="eyebrow" style="color:var(--gold)">SHS Alumni VIP Package &middot; SY 2024-2025</span>
        <div class="stamp grad-text">VIP</div>
        <h3 class="vip-h">President's Scholarship + zero down payment</h3>
        <p style="color:var(--on-dark-muted)">To value and support its Senior High graduates moving on to college, St. Clare offered the SHS Class of 2024 the President's Scholarship with zero down payment for SY 2024-2025. Ask admissions about this year's scholarships.</p>
        <a class="btn" href="admissions.html#scholarships">See scholarships {ARROW}</a>
      </div>
      <div class="media"><img src="img/graduates.jpg" alt="St. Clare College graduates applauding at commencement" loading="lazy" width="1230" height="640"></div>
    </div>
  </div>
</section>

<section class="pad white">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Vision &amp; Mission</span><h2 data-split>Why we <span class="grad-text-brand">teach</span></h2></div>
      <p class="lead rv">A responsible, innovative, skillful and professional global workforce, starting here in Caloocan.</p>
    </div>
    {VM}
  </div>
</section>

<section class="pad paper-2">
  <div class="wrap">
    <div class="sec-head">
      <div><span class="eyebrow">Enrollment procedure</span><h2 data-split>Enroll in <span class="grad-text-brand">three steps</span></h2></div>
      <p class="lead rv">Simplified and seamless. Bring your requirements, follow the three steps, and your schedule arrives by email.</p>
    </div>
    {steps_html()}
    <p style="margin-top:34px"><a class="link-arrow" href="admissions.html#requirements">Check the admission requirements</a></p>
  </div>
</section>

{cta("Make your <span class='gold'>mark</span> today", "Join a thriving community of achievers and unlock a world of possibilities at St. Clare College.")}
"""
    page("index.html", "St. Clare College of Caloocan | The School of Life Skills",
         "St. Clare College of Caloocan: Nursery to College, full online or blended learning. BSCS, BSHM, BSTM, BSBA, BEEd, BSEd and AB Political Science, plus Senior High tracks.", body)


def build_about():
    tl = [
        ("1985", "St. Clare College is founded", "Founded on 31 August 1985 in Caloocan City, Metro Manila, as a school of life skills."),
        ("2020", "St. Clare Online keeps learning going", "During the pandemic the college moved classes to its own online platform so no student got left behind. Applications for UniFAST-TES opened for A.Y. 2020-2021."),
        ("2021", "Virtual Lab and the 36th anniversary", "The Virtual Lab (VR + AR = MR) opened, Teacher-DJs went live on Zoom, Monday to Saturday, and the college marked its 36th founding anniversary."),
        ("2023", "The Professional Mace", "On 23 September 2023 St. Clare College introduced its Professional Mace, the eternal flame of professionalism."),
        ("2024", "38th Commencement + SHS Alumni VIP", "The Stars of 2024 graduated at the 38th Commencement Exercises, and the SHS Class of 2024 was offered the President's Scholarship with zero down payment."),
    ]
    tls = "".join(f'<div class="tl rv"><span class="y">{y}</span><div class="c"><h3>{h}</h3><p>{p}</p></div></div>' for y, h, p in tl)
    fac = ["E-boards in all 95 classrooms", "Air-conditioned classrooms", "Air-conditioned restrooms", "Virtual Lab with Acer Mixed Reality", "Computer laboratories",
           "Library and Learning Resource Center (3rd floor)", "St. Clare Virtual Studio"]
    body = phero("About", "Transforming education, <span class='grad-text'>building our future</span>",
                 "St. Clare College of Caloocan is the School of Life Skills and a leading institution for professional development, serving Caloocan since 1985.",
                 "campus-building.jpg") + f"""
<section class="pad">
  <div class="wrap split">
    <div class="media-stack rv-s">
      <div class="media wide"><img src="img/campus-building.jpg" alt="St. Clare College building on Zabarte Road with the SCO Online sign" width="1600" height="900" loading="lazy"></div>
      <div class="float"><img src="img/sco-online.webp" alt="SCO Online logo" width="512" height="512" loading="lazy"></div>
    </div>
    <div>
      <span class="eyebrow">Welcome to St. Clare</span>
      <h2 data-split>Begin with a <span class="grad-text-brand">warm embrace</span></h2>
      <p class="lead rv">Explore our campus, our facilities and our supportive community. Join us as we empower you to thrive, learn and succeed.</p>
      <ul class="checks rv">{"".join(f"<li>{x}</li>" for x in fac)}</ul>
    </div>
  </div>
</section>

<section class="pad white"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Vision &amp; Mission</span><h2 data-split>What we <span class="grad-text-brand">stand for</span></h2></div><p class="lead rv">Quality, affordable and sustainable education for the total development of every Clarean.</p></div>
  {VM}
</div></section>

{MACE}

<section class="pad"><div class="wrap split">
  <div>
    <span class="eyebrow">Continuity of learning</span>
    <h2 data-split>No one gets <span class="grad-text-brand">left behind</span></h2>
    <p class="lead rv">When colleges around the world moved to online and open distance learning, St. Clare's own platform made sure its students could continue and finish their education.</p>
    <p class="rv">Education is the gateway to creating professionals and a global workforce. The St. Clare Online Education System connects learning management, content and the e-Library, enrollment, personal transactions and virtual broadcasting in one place.</p>
    <a class="link-arrow rv" href="portals.html">Meet the five St. Clare Online systems</a>
  </div>
  <div class="media wide rv-s"><img src="img/sco-graphic.jpg" alt="St. Clare Online title graphic" width="1600" height="900" loading="lazy"></div>
</div></section>

<section class="pad white"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Milestones</span><h2 data-split>Our <span class="grad-text-brand">story</span></h2></div><p class="lead rv">Four decades of firsts for Caloocan.</p></div>
  <div class="timeline">{tls}</div>
</div></section>

<section class="pad"><div class="wrap">
  <div class="media wide rv-s" style="aspect-ratio:21/9"><img src="img/graduates.jpg" alt="Graduates at the St. Clare College commencement exercises" width="1230" height="640" loading="lazy"><div class="cap"><span>The Stars: St. Clare College commencement</span><span>Caloocan City</span></div></div>
</div></section>
""" + cta("Come see <span class='gold'>St. Clare</span>", "Visit the campus on Zabarte Road, 9:00 AM to 5:00 PM.")
    page("about.html", "About St. Clare College | Vision, Mission & History",
         "Founded in 1985 in Caloocan City, St. Clare College is the School of Life Skills: vision, mission, the Professional Mace and our milestones.", body)


def build_academics():
    items = []
    for code, name, ic, school, short, longd, tags in TERTIARY:
        items.append(f"""<article class="pitem rv">
  <div class="code">{code}<small>{school}</small></div>
  <div><h3>{name}</h3><p>{short} {longd}</p><div class="chips">{"".join(f"<span>{t}</span>" for t in tags)}</div></div>
</article>""")
    strands = "".join(f"""<article class="strand rv" style="--d:{i % 3}"><span class="k">{k}</span><h3>{n}</h3><p class="t">{t}</p><p>{d}</p>{("<ul>" + "".join(f"<li>{s}</li>" for s in sp) + "</ul>") if sp else ""}</article>""" for i, (k, n, t, d, sp) in enumerate(SHS))
    basic = "".join(f'<a class="level lv-{i + 1} rv" style="--d:{i};min-height:340px" href="admissions.html#requirements" data-tilt><span class="num">{k}</span><h3>{n}</h3><p>{d}</p><span class="go">Admission requirements</span></a>' for i, (k, n, d) in enumerate(BASIC))
    body = phero("Academics", "Programmes for <span class='grad-text'>every stage</span>",
                 "Basic Education, Senior High School and eight college degrees, taught on campus, online or blended.") + f"""
<section class="pad">
  <div class="wrap">
    <div class="tabs" role="tablist" aria-label="School levels">
      <button role="tab" id="t-ter" aria-controls="p-ter" aria-selected="true" data-hash="tertiary">Tertiary</button>
      <button role="tab" id="t-shs" aria-controls="p-shs" aria-selected="false" tabindex="-1" data-hash="shs">Senior High School</button>
      <button role="tab" id="t-bas" aria-controls="p-bas" aria-selected="false" tabindex="-1" data-hash="basic">Basic Education</button>
    </div>
    <div role="tabpanel" id="p-ter" aria-labelledby="t-ter">
      <div class="sec-head"><div><span class="eyebrow">Tertiary</span><h2>Eight degree <span class="grad-text-brand">programmes</span></h2></div><p class="lead">BSCS, BSHM, BSTM, BSBA, BEEd, BSEd-English, BSEd-Math and AB Political Science.</p></div>
      <div class="plist">{"".join(items)}</div>
    </div>
    <div role="tabpanel" id="p-shs" aria-labelledby="t-shs" hidden>
      <div class="dark" style="border-radius:var(--r-l);padding:clamp(24px,4vw,56px)">
        <div class="sec-head"><div><span class="eyebrow">Senior High School</span><h2>Tracks &amp; <span class="grad-text">strands</span></h2></div><p class="lead">Five ways to prepare for college, a career or a business, including TESDA National Certification for TVL-HE.</p></div>
        <div class="strands">{strands}</div>
      </div>
    </div>
    <div role="tabpanel" id="p-bas" aria-labelledby="t-bas" hidden>
      <div class="sec-head"><div><span class="eyebrow">Basic Education</span><h2>Strong <span class="grad-text-brand">foundations</span></h2></div><p class="lead">Nursery to Grade 10, with care, curiosity and a proper school uniform.</p></div>
      <div class="levels">{basic}</div>
    </div>
  </div>
</section>

<section class="pad white"><div class="wrap split">
  <div>
    <span class="eyebrow">How you learn</span>
    <h2 data-split>Theory in class, <span class="grad-text-brand">mastery in the lab</span></h2>
    <p class="lead rv">Every programme pairs lectures with practice: computer laboratories, practicum exercises, experiential learning and the Virtual Lab.</p>
    <ul class="checks rv"><li>Full online or blended modality</li><li>LMS for schedules, materials and progress</li><li>e-Library powered by ProQuest</li><li>TESDA NC assessment for TVL-HE</li></ul>
  </div>
  <div class="media tall rv-s"><img src="img/vr-student.jpg" alt="Student exploring mixed reality with a headset" width="868" height="1030" loading="lazy"></div>
</div></section>
""" + cta("Find your <span class='gold'>path</span>", "Talk to our admissions team about the programme that fits your goals.")
    page("academics.html", "Academics | St. Clare College Programmes",
         "College degrees (BSCS, BSHM, BSTM, BSBA, BEEd, BSEd, AB PolSci), Senior High tracks (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and Basic Education at St. Clare College.", body)


def build_admissions():
    tabs, panels = [], []
    for i, (k, (label, ab, items)) in enumerate(REQ.items()):
        sel = "true" if i == 0 else "false"
        tabs.append(f'<button role="tab" id="rt-{k}" aria-controls="rp-{k}" aria-selected="{sel}"{"" if i == 0 else " tabindex=\"-1\""} data-hash="{k}">{label}</button>')
        panels.append(f'<div role="tabpanel" id="rp-{k}" aria-labelledby="rt-{k}"{"" if i == 0 else " hidden"}><div class="req"><h3><i>{ab}</i>{label}</h3><ol>{"".join(f"<li>{x}</li>" for x in items)}</ol></div></div>')
    forms = "".join(f'<a href="{SRC}/downloadable-forms" rel="noopener"><span class="ext{" doc" if e == "DOC" else ""}">{e}</span><span><b>{n}</b><small>{c}</small></span><span class="arr">&darr;</span></a>' for e, n, c in FORMS)
    faq = [
        ("Can I study fully online?", "Yes. St. Clare College offers two modalities: full online and blended (online plus on-campus days). Choose the one that fits you when you enroll."),
        ("How do I get my class schedule?", "After paying the matriculation fee and filling up your registration form, register online for enlistment at the Library on the 3rd floor (stclareonline.com/ims). Your section and schedule are posted on the website and sent by email by your Program Head."),
        ("Are there scholarships?", "Ask the admissions office for this school year's offers. A certificate of indigency can be submitted with your requirements for scholarship consideration, and UniFAST-TES grantees can verify their status and disbursement schedule on the PMS."),
        ("How do I request my Transcript of Records or diploma?", "Only through the Official Document Request Portal on the Personal Management System (PMS). Do not transact with fixers or unauthorized persons."),
        ("When is the admissions office open?", f"9:00 AM to 5:00 PM. Call {PHONE} or email {EMAIL}."),
    ]
    faqs = "".join(f'<details class="rv"><summary>{q}</summary><div class="ans">{a}</div></details>' for q, a in faq)
    body = phero("Admissions", "Enroll with <span class='grad-text'>ease</span>",
                 "Simplified and seamless: enroll for a bright academic journey, Pre-school to Junior High, Senior High School and Tertiary.",
                 None, f'<div class="btn-row rv" style="--d:4;margin-top:30px"><a class="btn" href="{SRC}/ims" rel="noopener">Enroll online (IMS) {ARROW}</a><a class="btn ghost" href="#requirements">See requirements</a></div>') + f"""
<section class="pad paper-2"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Enrollment procedure</span><h2 data-split>Three steps <span class="grad-text-brand">to St. Clare</span></h2></div><p class="lead rv">Bring your requirements in a long brown envelope and follow these steps on campus.</p></div>
  {steps_html()}
</div></section>

<section class="pad" id="requirements"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Admission requirements</span><h2 data-split>What to <span class="grad-text-brand">bring</span></h2></div><p class="lead rv">Choose your level to see the checklist.</p></div>
  <div class="tabs" role="tablist" aria-label="Requirement type">{"".join(tabs)}</div>
  {"".join(panels)}
  <p class="note">All documents are considered property of the school once submitted as a requirement for admission.</p>
</div></section>

<section class="dusk pad noise" style="overflow:hidden"><canvas class="fx-canvas" aria-hidden="true"></canvas><div class="wrap" style="position:relative">
  <div class="sec-head"><div><span class="eyebrow">Choose your modality</span><h2 data-split>Full online <span class="grad-text">or blended</span></h2></div><p class="lead rv">Personalized learning pathways that empower you to choose your ideal modality for success.</p></div>
  {MODALITY}
</div></section>

<section class="pad white" id="scholarships"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Scholarships &amp; financial aid</span><h2 data-split>Invest in <span class="grad-text-brand">your future</span></h2></div><p class="lead rv">&ldquo;An investment in knowledge pays the best interest.&rdquo; Benjamin Franklin</p></div>
  <div class="cards">
    <article class="card rv"><div class="thumb"><img src="img/graduates.jpg" alt="" loading="lazy" width="1230" height="640"></div><div class="body"><span class="meta">SHS Alumni VIP</span><h3>President's Scholarship</h3><p>Offered to the St. Clare SHS Class of 2024 for SY 2024-2025, with zero down payment.</p></div></article>
    <article class="card rv" style="--d:1"><div class="thumb"><span class="gen" style="background:var(--grad-brand)">UniFAST<br>TES</span></div><div class="body"><span class="meta">Government subsidy</span><h3>Tertiary Education Subsidy</h3><p>Verify your TES grantee status and secure your disbursement schedule on the PMS.</p><a class="link-arrow" href="{SRC}/pms" rel="noopener">Go to PMS</a></div></article>
    <article class="card rv" style="--d:2"><div class="thumb"><span class="gen" style="background:linear-gradient(140deg,#d7141a,#6b23d6)">Need-<br>based</span></div><div class="body"><span class="meta">Optional document</span><h3>Certificate of indigency</h3><p>Submit a certificate of indigency with your requirements to be considered for scholarship.</p></div></article>
  </div>
</div></section>

<section class="pad"><div class="wrap split rev">
  <div>
    <span class="eyebrow">Basic Education</span>
    <h2 data-split>The school <span class="grad-text-brand">uniform</span></h2>
    <p class="lead rv">Pre-school to Grade 10 learners wear the official St. Clare College uniform. Thank you for considering St. Clare College, the School of Life Skills!</p>
  </div>
  <div class="media wide rv-s" style="aspect-ratio:13/10"><img src="img/uniforms.jpg" alt="Girl and boy wearing the St. Clare College Basic Education uniforms" width="1080" height="830" loading="lazy"></div>
</div></section>

<section class="pad white"><div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">Downloadable forms</span>
    <h2 data-split>Forms &amp; <span class="grad-text-brand">memos</span></h2>
    <p class="lead rv">Institutional forms, guidelines and memoranda, available on St. Clare Online.</p>
    <div class="dl-list rv" style="margin-top:26px">{forms}</div>
  </div>
  <div>
    <span class="eyebrow">Questions</span>
    <h2 data-split>Good to <span class="grad-text-brand">know</span></h2>
    <div class="faq" style="margin-top:26px">{faqs}</div>
  </div>
</div></section>
""" + cta("Your future <span class='gold'>starts here</span>", "Take the first step towards a brighter tomorrow.")
    page("admissions.html", "Admissions | Enroll at St. Clare College",
         "How to enroll at St. Clare College: three-step procedure, requirements for college freshmen, transferees, Basic Education and SHS, scholarships and forms.", body)


def build_campus():
    ev = "".join(f'<article class="event rv"><div class="d">{m}<b>{dd}</b></div><div><h3>{h}</h3><p>{p}</p></div><span class="where">{w}</span></article>' for m, dd, h, p, w in EVENTS)
    hb = "".join(f'<a href="{SRC}/cms" rel="noopener"><span class="ext">PDF</span><span><b>{h}</b><small>Handbooks &amp; manuals</small></span><span class="arr">&darr;</span></a>' for h in HANDBOOKS)
    body = phero("Campus Life", "Where innovation <span class='grad-text'>feels like home</span>",
                 "A vibrant campus, cutting-edge facilities and a supportive community, on Zabarte Road and online.", "virtual-lab-predator.jpg") + f"""
<section class="dark pad" id="virtual-lab" style="overflow:hidden"><div class="wrap" style="position:relative">{VLAB}</div></section>

<section class="pad white"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">SCO Online channels</span><h2 data-split>Our own <span class="grad-text-brand">broadcast network</span></h2></div><p class="lead rv">Broadcasting and Teacher-DJs are part of the St. Clare Online Education System, from the Monday virtual flag ceremony to commencement exercises.</p></div>
  {channels_html()}
</div></section>

<section class="pad"><div class="wrap split">
  <div class="media wide rv-s"><img src="img/campus-building.jpg" alt="St. Clare College campus building" width="1600" height="900" loading="lazy"></div>
  <div>
    <span class="eyebrow">On campus</span>
    <h2 data-split>Built for <span class="grad-text-brand">comfort &amp; focus</span></h2>
    <ul class="checks rv"><li>Air-conditioned classrooms and restrooms</li><li>Computer laboratories for hands-on programming and networking</li><li>Library and enlistment area on the 3rd floor</li><li>St. Clare Virtual Studio for webinars and broadcasts</li><li>E-boards in all 95 classrooms</li><li>Virtual Lab with Acer Mixed Reality (since 2021)</li></ul>
  </div>
</div></section>

<section class="dusk pad noise" style="overflow:hidden"><canvas class="fx-canvas" aria-hidden="true"></canvas><div class="wrap" style="position:relative">
  <div class="sec-head"><div><span class="eyebrow">Calendar of activities</span><h2 data-split>What's <span class="grad-text">happening</span></h2></div><p class="lead rv">Key dates for students, parents and faculty. <a class="link-arrow" href="{SRC}/calendar" rel="noopener">Full calendar</a></p></div>
  <div class="events">{ev}</div>
</div></section>

<section class="pad white" id="digital-citizenship"><div class="wrap split" style="align-items:start">
  <div>
    <span class="eyebrow">Digital citizenship</span>
    <h2 data-split>Safe, smart, <span class="grad-text-brand">responsible online</span></h2>
    <p class="lead rv">Online learning comes with responsibilities. Every Clarean gets the policies that guide life on St. Clare Online: digital passport, institutional email, data privacy and the student handbook.</p>
  </div>
  <div class="dl-list rv">{hb}</div>
</div></section>
""" + cta("See it for <span class='gold'>yourself</span>", "Tour the campus on Zabarte Road. We're open 9:00 AM to 5:00 PM.")
    page("campus-life.html", "Campus Life | Virtual Lab, SCO Online & Events",
         "The St. Clare College Virtual Lab (VR + AR = MR), SCO Online channels, campus facilities, calendar of activities and digital citizenship.", body)


def build_portals():
    tiles = "".join(f'<a class="portal rv" style="--d:{i}" href="{SRC}/{slug}" rel="noopener"><b>{k}</b><h3>{n}</h3><p>{d}</p><span class="go">Open {k}</span></a>' for i, (k, n, d, slug) in enumerate(PORTALS))
    body = phero("Portals", "St. Clare Online <span class='grad-text'>Education System</span>",
                 "Five connected systems for learning, content, enrollment, personal transactions and virtual broadcasting.") + f"""
<section class="dark pad" style="overflow:hidden"><div class="wrap" style="position:relative">
  <div class="sec-head"><div><span class="eyebrow">Five systems</span><h2 data-split>One <span class="grad-text">platform</span></h2></div><p class="lead rv">Pick a system to sign in or find what you need. Each opens on stclareonline.com.</p></div>
  <div class="portals">{tiles}</div>
</div></section>

<section class="pad"><div class="wrap">
  <div class="sec-head"><div><span class="eyebrow">Quick links</span><h2 data-split>Most <span class="grad-text-brand">requested</span></h2></div><p class="lead rv">Shortcuts for students, parents and faculty.</p></div>
  <div class="cards">
    <a class="card rv" href="{SRC}/ims" rel="noopener"><div class="thumb"><span class="gen" style="background:var(--grad-brand)">Online<br>enrollment</span></div><div class="body"><span class="meta">Students &middot; IMS</span><h3>Enroll and enlist online</h3><p>Register for your section and schedule.</p><span class="link-arrow">Open</span></div></a>
    <a class="card rv" style="--d:1" href="{SRC}/ims" rel="noopener"><div class="thumb"><span class="gen" style="background:linear-gradient(140deg,#1d2fc4,#070a2b)">Faculty<br>corner</span></div><div class="body"><span class="meta">Faculty &middot; IMS</span><h3>Attendance monitoring</h3><p>Basic Ed, SHS and Tertiary faculty attendance and online attendance.</p><span class="link-arrow">Open</span></div></a>
    <a class="card rv" style="--d:2" href="{SRC}/pms" rel="noopener"><div class="thumb"><span class="gen" style="background:linear-gradient(140deg,#d7141a,#6b23d6)">Document<br>request</span></div><div class="body"><span class="meta">Alumni &middot; PMS</span><h3>Official Document Request Portal</h3><p>Transcripts, diplomas and other official documents. No fixers.</p><span class="link-arrow">Open</span></div></a>
    <a class="card rv" href="{SRC}/lms" rel="noopener"><div class="thumb"><span class="gen" style="background:linear-gradient(140deg,#6b23d6,#d4177e)">College<br>corner</span></div><div class="body"><span class="meta">Students &middot; LMS</span><h3>Enrollment status &amp; sections</h3><p>Check your enrollment status, section and Program Heads directory.</p><span class="link-arrow">Open</span></div></a>
    <a class="card rv" style="--d:1" href="{SRC}/cms" rel="noopener"><div class="thumb"><span class="gen" style="background:linear-gradient(140deg,#0d1450,#3d9a3a)">e-Library</span></div><div class="body"><span class="meta">Everyone &middot; CMS</span><h3>Learning Resource Center</h3><p>Better learning anytime, anywhere, anyhow, powered by ProQuest.</p><span class="link-arrow">Open</span></div></a>
    <a class="card rv" style="--d:2" href="{SRC}/vms" rel="noopener"><div class="thumb"><span class="gen" style="background:linear-gradient(140deg,#e2b417,#d7141a)">Live<br>broadcast</span></div><div class="body"><span class="meta">Community &middot; VMS</span><h3>Virtual flag ceremony</h3><p>Every Monday, 7:00 AM, plus commencement exercises and events.</p><span class="link-arrow">Open</span></div></a>
  </div>
</div></section>
""" + cta("Need a <span class='gold'>hand</span>?", f"Call {PHONE} or email {EMAIL}, 9:00 AM to 5:00 PM.")
    page("portals.html", "St. Clare Online Portals | LMS, CMS, IMS, PMS, VMS",
         "Access the St. Clare Online Education System: Learning, Content, Institutional, Personal and Virtual Management Systems.", body)


def build_news():
    cards = []
    for i, (date, cat, h, p, img, gen, link) in enumerate(NEWS):
        if img:
            th = f'<img src="img/{img}" alt="" loading="lazy">'
        elif gen == "mace":
            th = '<span class="gen" style="background:radial-gradient(circle at 50% 70%,#ff8a1a,#d4177e 45%,#070a2b 80%)">Eternal<br>flame</span>'
        else:
            bgs = ["var(--grad-brand)", "linear-gradient(140deg,#d7141a,#6b23d6)", "linear-gradient(140deg,#1d2fc4,#070a2b)", "linear-gradient(140deg,#6b23d6,#d4177e)"]
            th = f'<span class="gen" style="background:{bgs[i % 4]}">{gen}</span>'
        cards.append(f'<a class="card rv" style="--d:{i % 3}" href="{link}" rel="noopener"><div class="thumb">{th}</div><div class="body"><span class="meta">{cat} &middot; {date}</span><h3>{h}</h3><p>{p}</p><span class="link-arrow">Read more</span></div></a>')
    body = phero("News", "News &amp; <span class='grad-text'>announcements</span>",
                 "Milestones, scholarships, advisories and stories from the St. Clare College community.") + f"""
<section class="pad"><div class="wrap">
  <div class="cards">{"".join(cards)}</div>
</div></section>
<div class="marquee red" aria-hidden="true"><div class="track">{"".join(f"<span>{n}</span>" for n, _ in CHANNELS) * 2}</div></div>
""" + cta("Be part of the <span class='gold'>story</span>", "Basic Education, Senior High School and College, on campus or online.")
    page("news.html", "News | St. Clare College", "Latest news, scholarships, advisories and events from St. Clare College of Caloocan.", body)


def build_contact():
    body = phero("Contact", "Let's talk about <span class='grad-text'>your future</span>",
                 "Questions about enrollment, programmes or scholarships? We're here 9:00 AM to 5:00 PM.") + f"""
<section class="pad"><div class="wrap">
  <div class="contact-grid">
    <div class="info-card rv">
      <span class="eyebrow">St. Clare College of Caloocan</span>
      <h2 style="font-size:clamp(1.8rem,3.4vw,2.6rem)">Visit, call <span class="grad-text">or write</span></h2>
      <dl>
        <div><dt>Campus</dt><dd>{ADDRESS}</dd></div>
        <div><dt>Phone</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd></div>
        <div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
        <div><dt>Office hours</dt><dd>9:00 AM - 5:00 PM</dd></div>
      </dl>
      <div class="socials"><a href="{FB}" rel="noopener" aria-label="Facebook">{FB_SVG}</a><a href="{YT}" rel="noopener" aria-label="YouTube">{YT_SVG}</a></div>
    </div>
    <form class="form rv" style="--d:1" data-mailto="{EMAIL}">
      <span class="eyebrow">Send an inquiry</span>
      <div class="field-row">
        <div class="field"><label for="f-name">Full name</label><input id="f-name" name="Name" autocomplete="name" required></div>
        <div class="field"><label for="f-email">Email</label><input id="f-email" name="Email" type="email" autocomplete="email" required></div>
      </div>
      <div class="field-row">
        <div class="field"><label for="f-level">Interested in</label><select id="f-level" name="Level"><option>Basic Education</option><option>Senior High School</option><option selected>College / Tertiary</option><option>Other</option></select></div>
        <div class="field"><label for="f-src">Where did you hear about us?</label><select id="f-src" name="Source"><option>Facebook</option><option>YouTube</option><option>Friend or family</option><option>Search</option><option>Other</option></select></div>
      </div>
      <div class="field"><label for="f-sub">Subject</label><input id="f-sub" name="subject" value="Enrollment inquiry"></div>
      <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="Message" required></textarea></div>
      <button class="btn royal" type="submit">Send inquiry {ARROW}</button>
      <p class="form-status" role="status"></p>
      <p class="hint">Opens your email app with the message ready to send to {EMAIL}.</p>
    </form>
  </div>
  <div class="map rv" style="margin-top:24px"><iframe title="Map to St. Clare College of Caloocan" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=St.+Clare+College+of+Caloocan,+Zabarte+Road,+Caloocan+City&output=embed"></iframe></div>
</div></section>
"""
    page("contact.html", "Contact St. Clare College | Caloocan City",
         f"Contact St. Clare College of Caloocan: {ADDRESS}. Phone {PHONE}, email {EMAIL}, 9:00 AM - 5:00 PM.", body)


if __name__ == "__main__":
    build_home(); build_about(); build_academics(); build_admissions()
    build_campus(); build_portals(); build_news(); build_contact()
