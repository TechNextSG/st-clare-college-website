# St. Clare College site content. Facts come only from stclareonline.com (Oct 2026 snapshot).
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

FB_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M9.101 23.691v-7.98H6.627v-3.667h2.474v-1.58c0-4.085 1.848-5.978 5.858-5.978.401 0 .955.042 1.468.103a8.68 8.68 0 0 1 1.141.195v3.325a8.623 8.623 0 0 0-.653-.036 26.805 26.805 0 0 0-.733-.009c-.707 0-1.259.096-1.675.309a1.686 1.686 0 0 0-.679.622c-.258.42-.374.995-.374 1.752v1.297h3.919l-.386 2.103-.287 1.564h-3.246v8.245C19.396 23.238 24 18.179 24 12.044c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.628 3.874 10.35 9.101 11.647Z"/></svg>'
YT_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>'

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

