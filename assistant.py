# Builds assets/kb.json: the St. Clare Assistant's knowledge, taken only from this website's own content.
# The assistant (assets/assistant.js) matches a visitor's question to these entries in the browser; no server, no AI API.
import json, os, re, html
from data import REQ, STEPS, PHONE, PHONE_TEL, EMAIL, ADDRESS, FB, YT
from content import (TERTIARY_FULL, SHS_FULL, BASIC_FULL, HISTORY, LEADERS, PMS, IMS, CMS, LMS, HEALTH_SURVEY,
                     CAL_2025, NEWS_FULL, FORMS_DOCS, HANDBOOKS, MEMOS, VIDEOS)

OUT = os.path.dirname(os.path.abspath(__file__))
E = html.escape

def a(href, label): return f'<a href="{E(href)}"{" target=\"_blank\" rel=\"noopener\"" if href.startswith("http") else ""}>{E(label)}</a>'
def ul(items): return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
def short(t, n=260):
    t = re.sub(r"\s+", " ", t).strip()
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0] + "..."

K = []
def add(id_, q, keys, ans, links=(), weight=1.0):
    K.append({"id": id_, "q": q, "k": [k.lower() for k in keys], "a": ans, "l": [list(x) for x in links], "w": weight})

CALL = f'Call {a("tel:" + PHONE_TEL, PHONE)} or email {a("mailto:" + EMAIL, EMAIL)}, 9:00 AM to 5:00 PM.'

# ---------------- conversation
add("hello", "Hi!", ["hi", "hello", "hey", "good morning", "good afternoon", "good evening", "kumusta", "musta"],
    "Hi! I'm the St. Clare Assistant. I can help with programmes, enrollment, requirements, student services, forms and contact details. What would you like to know?", weight=.6)
add("thanks", "Thank you", ["thank", "thanks", "salamat", "ty"], "You're welcome! Anything else I can help with?", weight=.6)
add("who", "What can you do?", ["what can you do", "help", "who are you", "bot", "assistant"],
    "I answer questions using the information on this website: programmes, how to enroll, requirements, scholarships, student services (LMS, CMS, IMS, PMS, VMS), forms, the calendar and contact details. For anything I can't answer, the admissions office can help: " + CALL, weight=.7)

# ---------------- admissions
steps = ul([f"<b>{h}</b> ({w}): " + " ".join(x for x in its) for h, w, its in STEPS])
add("enroll", "How do I enroll?", ["enroll", "enrol", "enrollment", "enrolment", "register", "registration", "apply", "admission", "admissions", "how to enroll", "sign up", "mag enroll", "steps"],
    f"Enrollment takes three steps on campus:{steps}You can also enroll online through the IMS. Bring photocopies of your requirements in a long brown envelope.",
    [("admissions.html#steps", "Enrollment procedure"), ("ims.html", "Enroll online (IMS)"), ("admissions.html#requirements", "Requirements")], 1.2)
add("online-enroll", "Can I enroll online?", ["enroll online", "online enrollment", "online enrolment", "ims", "enlist", "enlistment"],
    "Yes. Online enrollment is through the IMS (Institutional Management System), from Pre-school to Junior High, Senior High School and Tertiary. On campus, enlistment happens at the Library on the 3rd floor.",
    [("ims.html", "Open the IMS page"), ("admissions.html#steps", "On-campus steps")])
for k, (label, _ab, items) in REQ.items():
    keys = {"freshmen": ["freshman", "freshmen", "college requirements", "first year", "incoming college"],
            "transferees": ["transferee", "transferees", "transfer", "shift school", "lipat"],
            "basic": ["basic education requirements", "preschool", "pre-school", "kinder", "kindergarten", "elementary", "grade school", "grade 1", "junior high", "grade 7", "nursery"],
            "shs": ["senior high requirements", "shs requirements", "grade 11", "grade 12", "senior high school requirements"]}[k]
    add("req-" + k, f"Requirements: {label}", ["requirements", "documents needed", "what to bring", "requirement"] + keys,
        f"<b>{E(label)}</b> requirements:{ul([E(x) for x in items])}Place photocopies in a long brown envelope. All documents become school property once submitted.",
        [(f"admissions.html#{k}", f"{label} requirements"), ("admissions.html#guide", "Official enrollment slides")], 1.1)
add("req", "What are the requirements?", ["requirements", "requirement", "documents", "what to bring", "needed", "kailangan"],
    "Requirements depend on your level. Which one are you?" + ul([a(f"admissions.html#{k}", v[0]) for k, v in REQ.items()]),
    [("admissions.html#requirements", "All requirements")], .9)
add("fees", "How much is the tuition?", ["tuition", "fee", "fees", "cost", "price", "how much", "magkano", "payment", "matriculation", "bayad"],
    f"Fees change each school year, so please confirm with the admissions office before your visit: {CALL} The enrollment slides on the Admissions page include tuition slides from earlier school years, for reference only.",
    [("admissions.html#guide", "Enrollment slides"), ("contact.html", "Contact admissions")], 1.1)
add("dates", "When is enrollment?", ["when", "enrollment date", "schedule of enrollment", "deadline", "open", "start of classes", "opening of classes", "kailan"],
    f"Enrollment dates are set each school year. Please confirm with the admissions office: {CALL} You can also check the calendar of activities.",
    [("calendar.html", "Calendar"), ("contact.html", "Contact admissions")], .9)
add("modality", "Can I study fully online?", ["study online", "full online", "online class", "online classes", "modality", "blended", "distance learning", "face to face", "f2f", "remote", "study from home"],
    "Yes. St. Clare offers two learning modalities: <b>full online</b> through St. Clare Online (LMS classes, the e-Library and virtual broadcasts), or <b>blended</b>, which combines online learning with on-campus days in air-conditioned classrooms with e-boards, laboratories and the Virtual Lab.",
    [("admissions.html#modality", "Learning modality")])
add("scholar", "Are there scholarships?", ["scholarship", "scholarships", "discount", "financial aid", "grant", "iskolar", "free tuition", "assistance"],
    "Ask the admissions office for this school year's scholarships. Submitting a certificate of indigency with your requirements lets you be considered for a scholarship. In SY 2024-2025 the SHS Class of 2024 was offered the President's Scholarship with zero down payment (shown for the record). Tertiary students can also check UniFAST-TES on the PMS.",
    [("admissions.html#scholarships", "Scholarships"), ("pms.html#tes", "UniFAST-TES")])
tes_t, tes_steps = PMS["tes"]
add("tes", "What is UniFAST-TES?", ["tes", "unifast", "tertiary education subsidy", "subsidy", "grantee", "disbursement", "chedtes"],
    f"UniFAST-TES (Tertiary Education Subsidy) grantees verify their status and secure a disbursement schedule on the PMS:{ul([E(h) + ': ' + E(short(p, 140)) for h, p, _b, _u in tes_steps])}",
    [("pms.html#tes", "TES guidelines on the PMS")])

# ---------------- academics
coll = ul([f"<b>{E(code)}</b> {E(name)}" for code, name, _i, _d in TERTIARY_FULL])
add("programs", "What programmes do you offer?", ["program", "programs", "programme", "programmes", "course", "courses", "degree", "degrees", "offer", "kurso", "strand", "strands", "track", "tracks"],
    f"St. Clare offers Basic Education (Nursery to Grade 10), Senior High School (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE) and these college degrees:{coll}",
    [("academics.html", "All programmes"), ("academics.html#tertiary", "College degrees"), ("academics.html#shs", "Senior High tracks")], 1.1)
SYN = {"BSHM": ["hospitality", "hm", "hotel", "restaurant"], "BSBA": ["business", "ba", "business administration", "marketing", "management"],
       "BSCS": ["computer science", "cs", "programming", "coding", "computer", "information technology"], "BEEd": ["elementary education", "teacher", "teaching", "education", "beed"],
       "BSEd": ["secondary education", "teacher", "english", "math", "mathematics", "bsed"], "BSTM": ["tourism", "tm", "travel"], "AB": ["political science", "polsci", "politics", "ab"]}
for code, name, _img, desc in TERTIARY_FULL:
    keys = [code.lower(), name.lower()] + next((v for kk, v in SYN.items() if code.startswith(kk)), [])
    add("prog-" + re.sub(r"\W+", "-", code.lower()), name, keys, f"<b>{E(name)}</b> ({E(code)}): {E(short(desc, 420))}",
        [("academics.html#" + code.split()[0].lower().replace("/", ""), "Read more on Academics"), ("admissions.html#freshmen", "College requirements")], 1.15)
add("shs", "What Senior High tracks do you offer?", ["senior high", "shs", "strand", "strands", "track", "tracks", "grade 11", "grade 12"],
    "Senior High School at St. Clare offers:" + ul(["<b>Academic Track</b>: ABM and HUMSS", "<b>Arts & Design</b>", "<b>TVL - Information, Communication Technology</b>", "<b>TVL - Home Economics</b> (with TESDA National Certification)"]),
    [("academics.html#shs", "Senior High tracks"), ("admissions.html#shs", "SHS requirements")], 1.3)
for name, _img, desc in SHS_FULL:
    keys = [name.lower()] + [w.lower() for w in re.findall(r"[A-Z&]{2,}|Arts & Design|Home Economics|Information", name)]
    add("shs-" + re.sub(r"\W+", "-", name.lower())[:30], name, keys, f"<b>{E(name)}</b> (Senior High School): {E(short(desc, 380))}",
        [("academics.html#shs", "Senior High tracks"), ("admissions.html#shs", "SHS requirements")], 1.05)
for name, _img, desc in BASIC_FULL:
    add("basic-" + re.sub(r"\W+", "-", name.lower())[:30], name, [name.lower(), "basic education", "nursery", "kinder", "elementary", "junior high", "grade school"],
        f"<b>{E(name)}</b>: {E(short(desc, 320))}", [("academics.html#basic", "Basic Education")], .95)

# ---------------- about
hist = ul([f"<b>{E(y)}</b>: {E(h)}" for y, h, _p in HISTORY])
add("history", "When was St. Clare founded?", ["history", "founded", "founding", "established", "since", "anniversary", "1985", "background", "about st clare", "about the school"],
    f"St. Clare College of Caloocan was founded on <b>31 August 1985</b> in Caloocan City, Metro Manila. Key milestones:{hist}", [("about.html#history", "Full history")])
add("vm", "What is the vision and mission?", ["vision", "mission", "philosophy", "goal", "values"],
    "<b>Vision:</b> To become the leading institution for professional development and the first and foremost provider of quality, affordable and sustainable development education.<br><b>Mission:</b> To provide quality and excellent global education for the total development of a responsible, innovative, skillful and professional global workforce whose values and dignity are beyond par.",
    [("about.html", "About St. Clare")])
add("leaders", "Who leads St. Clare?", ["president", "founder", "dean", "chairman", "leadership", "head", "owner", "adalem", "tenedero"],
    ul([f"<b>{E(n)}</b>, {E(r)}" for n, r in LEADERS]), [("about.html", "Leadership")])
add("facilities", "What facilities do you have?", ["facilities", "facility", "campus", "classroom", "classrooms", "e-board", "eboard", "aircon", "air-conditioned", "laboratory", "lab", "computer lab"],
    "The campus on Zabarte Road has e-boards in all 95 classrooms (the first college in the country to do so), air-conditioned classrooms and restrooms, computer laboratories, the Library and Learning Resource Center on the 3rd floor, the St. Clare Virtual Studio and the Virtual Lab.",
    [("campus-life.html#facilities", "Facilities"), ("about.html#facilities", "Photos")])
add("vlab", "What is the Virtual Lab?", ["virtual lab", "vr", "ar", "mixed reality", "predator", "thronos", "acer", "gaming"],
    "The St. Clare Virtual Lab (VR + AR = mixed reality) opened in 2021 with the Predator Thronos and the Mixed Reality facility by Acer.",
    [("campus-life.html#virtual-lab", "Inside the Virtual Lab (videos)")])
add("library", "Is there a library or e-Library?", ["library", "elibrary", "e-library", "proquest", "books", "learning resource", "research"],
    f"The Library and Learning Resource Center is on the 3rd floor. Online, the e-Library is powered by ProQuest: {E(CMS['elibrary'][1])}",
    [("cms.html", "e-Library (CMS)"), (CMS["elibrary"][2], "Open the e-Library")])

# ---------------- student services
add("portals", "What are LMS, CMS, IMS, PMS and VMS?", ["portal", "portals", "student services", "st clare online", "sco", "system", "systems", "lms cms ims pms vms"],
    "St. Clare Online has five connected systems:" + ul(["<b>LMS</b>: class schedules, class lists and sectioning", "<b>CMS</b>: the ProQuest e-Library and handbooks", "<b>IMS</b>: online enrollment, faculty attendance and job openings",
                                                          "<b>PMS</b>: UniFAST-TES, document requests, digital passport, ePayments and e-grades", "<b>VMS</b>: commencement, broadcasts, webinars and the video library"]),
    [("portals.html", "Student services")])
add("schedule", "Where is my class schedule?", ["schedule", "class schedule", "section", "sectioning", "class list", "lms", "my class", "program head"],
    "Class schedules, class lists and sectioning are on the LMS (College Corner, SHS Corner and Basic Education Corner). Your Program Head also emails your section and schedule.",
    [("lms.html", "Open the LMS page")])
t, s_, u = PMS["docreq"][:3]
add("docs", "How do I request my TOR or diploma?", ["tor", "transcript", "diploma", "records", "certificate", "document request", "good moral", "form 137", "credentials", "request documents"],
    f"{E(s_)}", [("pms.html#documents", "Document request (PMS)"), (u, "Open the request form")], 1.1)
add("grades", "Where can I see my grades?", ["grade", "grades", "e-grades", "egrades", "marks", "report card"],
    "e-Grades are on the PMS, listed by programme and semester.", [("pms.html#grades", "e-Grades")])
t2, s2, u2, _ = PMS["epay"]
add("epay", "How do I pay online?", ["pay online", "pay", "payment", "epayment", "e-payment", "gcash", "bank", "receipt", "dropbox", "proof of payment"],
    f"<b>{E(t2)}</b>: {E(short(s2, 300))}", [("pms.html#epayments", "ePayments dropbox"), (u2, "Open the form")])
t3, s3, u3, _ = PMS["passport"]
add("passport", "What is the digital passport?", ["passport", "digital passport", "id", "school id"],
    f"<b>{E(t3)}</b>: {E(short(s3, 300))}", [("pms.html#passport", "Digital passport"), (u3, "Open the form")])
ht, hs, quals, mail, addr = IMS["hiring"]
add("jobs", "Are you hiring?", ["hiring", "job", "jobs", "career", "careers", "teacher vacancy", "vacancy", "apply as teacher", "work", "employment", "hr"],
    f"<b>{E(ht)}</b>: {E(hs)}{ul([E(q) for q in quals])}Send your application to {a('mailto:' + addr, addr)}.", [("ims.html#hiring", "Job openings")])
add("faculty", "Faculty attendance", ["faculty attendance", "attendance", "time in", "log in faculty", "teacher attendance"],
    "Faculty log-in / time-in for virtual classes is on the IMS, with separate links for Basic Education, SHS and Tertiary.", [("ims.html#faculty", "Faculty attendance (IMS)")])
add("forms", "Where can I download forms?", ["form", "forms", "download", "registration form", "clearance", "memo", "memorandum", "handbook", "student handbook", "pdf"],
    "Downloadable forms include:" + ul([E(n) for n, _f, _t, _s in FORMS_DOCS]) + f"Plus {len(MEMOS)} memoranda and {len(HANDBOOKS)} handbooks and manuals.",
    [("downloads.html", "All downloads"), ("docs/student-handbook.pdf", "Student Handbook (PDF)")])
add("health", "Health survey form", ["health", "health survey", "health declaration", "medical"],
    "The health survey form is for the students, parents, teachers and non-teaching personnel of St. Clare College only.", [(HEALTH_SURVEY, "Open the health survey form"), ("downloads.html", "Downloads")])
cal = ul([f"<b>{E(d)}</b>: {E(h)}" for d, h, _w, _p in CAL_2025[:6]])
add("calendar", "What's on the calendar?", ["calendar", "events", "activities", "holiday", "foundation day", "feast", "orientation", "class opening"],
    f"From the 2025 calendar of activities:{cal}", [("calendar.html", "Full calendar")])
nv = sum(len(v) for _g, v in VIDEOS)
add("videos", "Where are the videos?", ["video", "videos", "youtube", "commencement", "graduation", "broadcast", "webinar", "flag ceremony", "mace", "vms"],
    f"The VMS video library has {nv} videos: commencement exercises, the Professional Mace, the Virtual Lab, broadcasts, webinars and more. The virtual flag ceremony is every Monday at 7:00 AM.",
    [("vms.html", "Video library (VMS)"), (YT, "YouTube channel")])
latest = ul([f"<b>{E(t)}</b> ({E(d)})" for d, t, _x, _i, _v in NEWS_FULL[:4]])
add("news", "What's the latest news?", ["news", "latest", "announcement", "announcements", "update", "updates", "advisory"],
    f"Recent posts:{latest}", [("news.html", "All news")])

# ---------------- contact
add("contact", "How can I contact you?", ["contact", "phone", "number", "call", "email", "telephone", "landline", "reach", "inquire", "inquiry", "message"],
    f"Phone: {a('tel:' + PHONE_TEL, PHONE)}<br>Email: {a('mailto:' + EMAIL, EMAIL)}<br>Office hours: 9:00 AM to 5:00 PM<br>Messenger: {a('https://m.me/stclarecollege', 'St. Clare College on Facebook')}",
    [("contact.html", "Contact page")], 1.1)
add("address", "Where is the campus?", ["where", "address", "location", "located", "map", "directions", "saan", "zabarte", "camarin", "caloocan"],
    f"St. Clare College of Caloocan is at <b>{E(ADDRESS)}</b>.",
    [("contact.html#map", "Map"), ("https://www.google.com/maps?q=St.+Clare+College+of+Caloocan,+Zabarte+Road,+Caloocan+City", "Open in Google Maps")], 1.05)
add("hours", "What are your office hours?", ["office hours", "hours", "open", "time", "schedule office", "closing"],
    "The office is open 9:00 AM to 5:00 PM.", [("contact.html", "Contact page")])
add("social", "Are you on Facebook?", ["facebook", "fb", "social media", "page", "instagram", "messenger"],
    f"Follow St. Clare College on {a(FB, 'Facebook')} and {a(YT, 'YouTube')}.")

PAGES = [("index.html", "Home"), ("about.html", "About"), ("academics.html", "Academics"), ("admissions.html", "Admissions"), ("campus-life.html", "Campus life"),
         ("news.html", "News"), ("contact.html", "Contact"), ("portals.html", "Student services"), ("lms.html", "LMS"), ("cms.html", "CMS"), ("ims.html", "IMS"),
         ("pms.html", "PMS"), ("vms.html", "VMS"), ("downloads.html", "Downloads"), ("calendar.html", "Calendar")]
SUGGEST = ["How do I enroll?", "What programmes do you offer?", "What are the requirements?", "How much is the tuition?", "Are there scholarships?", "Where is the campus?"]

def build():
    kb = {"v": 1, "intents": K, "pages": PAGES, "suggest": SUGGEST, "fallback": f"I couldn't find that on the website. The admissions office can help: {CALL}"}
    with open(os.path.join(OUT, "assets", "kb.json"), "w", encoding="utf-8") as f:
        json.dump(kb, f, ensure_ascii=False, separators=(",", ":"))
    print("kb.json", len(K), "entries")

if __name__ == "__main__":
    build()
