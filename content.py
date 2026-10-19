# Full content captured from stclareonline.com (crawl of 19 Oct 2026: 12 pages, 46 videos, 15 documents, 53 images,
# all Google Sheets / Forms / Drive links). Source of truth for the rebuilt pages.

GS = "https://docs.google.com/spreadsheets/d/"

# ---------------- documents (hosted in /docs, mirrored from the school's downloads) ----------------
FORMS_DOCS = [
    ("Fillable Registration / Enrollment Form", "registration-enrollment-form.pdf", "PDF", "1.4 MB"),
    ("Health Declaration Form", "health-declaration-form.pdf", "PDF", "190 KB"),
    ("SCC Clearance Form 2023", "scc-clearance-form-2023.pdf", "PDF", "600 KB"),
    ("Guidelines for the Releasing of Curriculum Guide", "guidelines-releasing-curriculum-guide.pdf", "PDF", "560 KB"),
    ("Exit Interview Form (CGS-0010)", "exit-interview-form-cgs-0010.pdf", "PDF", "66 KB"),
    ("Waiver & Application for Graduation 2024", "waiver-application-for-graduation-2024.pdf", "PDF", "553 KB"),
    ("TES Sharing Agreement, 2023-2024 onwards", "tes-sharing-agreement-2023-2024.docx", "DOCX", "23 KB"),
]
MEMOS = [
    ("Memo: Requirements for Graduation (4 May 2023)", "memo-requirements-for-graduation-2023-05-04.pdf", "PDF", "569 KB"),
    ("Memo: Guidelines on Off-Campus Activities (5 May 2023)", "memo-off-campus-activities-2023-05-05.pdf", "PDF", "265 KB"),
]
HANDBOOKS = [
    ("SCC ID Policy", "scc-id-policy.pdf", "PDF", "498 KB"),
    ("Student Handbook", "student-handbook.pdf", "PDF", "3.1 MB"),
    ("St. Clare College Digital Passport Policy", "digital-passport-policy.pdf", "PDF", "498 KB"),
    ("Digital Citizenship (students' copy)", "digital-citizenship-students-copy.pdf", "PDF", "500 KB"),
    ("Institutional Email", "institutional-email.pdf", "PDF", "528 KB"),
    ("SCC Data Privacy Manual 2021", "scc-data-privacy-manual-2021.pdf", "PDF", "1.4 MB"),
]

# ---------------- programmes with photos and the school's full descriptions ----------------
TERTIARY_FULL = [
    ("BSHM", "Bachelor of Science in Hospitality Management", "prog-bshm",
     "Bachelor of Science in Hospitality Management will equip the students with competencies that are needed to execute operational tasks and maintain management functions in food production (culinary), accommodation, food and beverage service, tourism planning and product development, events planning, travel and tour operations and other sectors of the hospitality industry."),
    ("BSBA", "Bachelor of Science in Business Administration", "prog-bsba",
     "The Bachelor of Science in Business Administration (BSBA) program is geared towards equipping students with the necessary knowledge, skills and attitude to provide quality service in the field of business and industry, such as perform the basic functions of management such as planning, organizing, leading and controlling, demonstrate knowledge of business industry, local product and services. Its primary concentration is on development of theoretical classes, practicum exercises and experiential learning."),
    ("BSCS", "Bachelor of Science in Computer Science", "prog-bscs-lab",
     "The BS in Computer Science course prepares you for proficiency in designing, writing and developing computer programs and computer networks. The field incorporates the study of computer algorithms and their implementation through computer software applications, data processing, web development, programming and computer architecture. You will also attain skills in building computer networks. Classroom lectures will equip you with theoretical framework of computer science, but the key learning experiences will take place in computer laboratories where you will experiment with software applications, programming tools and actual computer design using hardware."),
    ("BEEd / BSEd", "Bachelor of Elementary Education; Bachelor of Secondary Education, Major in English & Math", "prog-education",
     "The BEEd is an undergraduate teacher education degree program designed to prepare individuals intending to teach in the elementary level. The BSEd is an undergraduate teacher education program designed to equip learners with adequate and relevant competencies to teach in their chosen area of specialization/major in the secondary level."),
    ("BSTM", "Bachelor of Science in Tourism Management", "prog-bstm",
     "The program related to the fields of hospitality and tourism education will equip students with competencies that are needed to execute operational tasks and management functions in food production (culinary), accommodation, food and beverage service, tourism planning and product development, events planning, transportation services, travel and tour operations and other emerging sectors of hospitality and tourism industry."),
    ("AB PolSci", "Bachelor of Arts in Political Science", "prog-polsci",
     "Bachelor of Arts in Political Science will equip the students with core competencies expressed as behaviors that can be observed and assessed, and prepare them for a professional career in government service, or for careers dealing with public issues and problems. The curriculum is designed to expose the students to a variety of program work and activities that will provide a broad understanding of the curriculum."),
]
SHS_FULL = [
    ("Arts & Design", None,
     "The Arts & Design track will prepare you as you wander around the design, performative, and creative industry. What this track aims is to get you a career in the creative field after you graduate. To instill the right employment skills so that you can get a job immediately after graduation, part of the curriculum of this track is to expose you to various forms of media such as architecture, interior design, industrial design, graphic design, animation, painting, fashion design, photography, and film."),
    ("Academic Track (ABM & HUMSS)", "shs-academic",
     "ABM refers to the accountancy, business, and management academic programs that concentrate on the foundational concepts in corporate operations, financial management, business management, and every factor that revolves around those central fields. HUMSS stands for Humanities and Social Sciences: the study of human behavior and societal changes, and analysis of arts, culture, literature, and politics, involving political science, anthropology, linguistics, psychology, and communication."),
    ("TVL - Information, Communication Technology", "shs-ict-virtual-lab",
     "Information and Communication Technology (ICT) in education is the mode of education that uses information and communications technology to support, enhance, and optimize the delivery of information. It refers to technologies that provide access to information through telecommunications; it is similar to Information Technology (IT), but focuses primarily on communication."),
    ("TVL - Home Economics", "shs-tvl-he",
     "TVL-HE is designed to develop students' skills useful for livelihood projects at home. It combines core courses required for all SHS strands with specialized hands-on courses that meet the standard hour requirement and competency-based assessment of TESDA. Students undergo TESDA assessment for National Certification (NC), which increases their employability after SHS. TVL-HE offers three specializations: Bread and Pastry Production, Food and Beverage Service, and Housekeeping."),
]
BASIC_FULL = [
    ("Nursery & Kindergarten", "basic-kinder", "Nurturing Young Minds: Where Curiosity and Growth Blossom in Kindergarten!"),
    ("Elementary, Grade 1 to 6", "basic-elementary", "Building Strong Foundations: Empowering Students for Lifelong Learning in Elementary School."),
    ("Junior High School, Grade 7 to 10", "shs-academic", "Unlocking Potential, Shaping Futures: Thriving in Junior High School's Journey of Growth and Discovery!"),
]

# ---------------- LMS ----------------
LMS = {
    "intro": "Learning Management System (LMS) is a software application for managing, archiving, monitoring, reporting and delivering training courses or training programs. LMS helps the instructor deliver material to students, manage tests and other tasks, monitor students' progress and ensure record keeping.",
    "welcome": "Welcome Clareans! Get to know your class schedules and teachers.",
    "college_corner": ("College Corner 2025-2026", "Check your enrollment status, section and other enrollment-related information for Academic Year 2025-2026, first semester.", [
        ("Program Heads Directory", GS + "1lH16-6Rh1F7cvZYTN7JQ8FjeRrgs491SIQKUVlfZZa0/edit?usp=sharing"),
        ("Admission Requirements", GS + "18GWAUyUpLMubOaUcSI5o0AGTlwioVQeRMak7wsLhrv8/edit?usp=sharing")]),
    "groups": [
        ("Class schedule, SY 2024-2025 (1st semester)", [
            ("BS Computer Science", GS + "1QSB45x2Dm24Mj7B8ksWGxDVpVAjH_taP2i4SVjpOHg4/edit?usp=sharing"),
            ("BS Hospitality Management", GS + "1Phylr_dE7AZGWLFw3qfPBvcVeeQrsdI8l6cCPRElOgA/edit?usp=sharing"),
            ("BS Tourism Management", GS + "1ybU7rMda8qLQzBbcikInDdTZwH7ntk_lPGQ9x0v3lW4/edit?usp=sharing"),
            ("AB Political Science", GS + "14isI0G9n88Hy0GqR-o4bCUJ6AX1o0tK3ryQIwGkLJNQ/edit?usp=sharing"),
            ("BS Business Administration", GS + "1lMTNIYuA-ViS2WzJMP3QJU5YxcBciSJzK_SLHePgG8I/edit?usp=sharing"),
            ("Education (BEEd, BSEd-Eng, BSEd-Math)", GS + "1YLHmBOg77oyQZ6PW67iMMDNGGTEkVT_F6l7Ud13T9pk/edit?usp=sharing")]),
        ("Class list & sectioning, SY 2024-2025 (1st semester)", [
            ("BS Computer Science", GS + "10Rk-fW_reT1sc1fX3nWpvs3wFnPMLcNGQ40ajHI0Ft4/edit?usp=sharing"),
            ("BS Business Administration", GS + "1lMTNIYuA-ViS2WzJMP3QJU5YxcBciSJzK_SLHePgG8I/edit?usp=sharing"),
            ("Education (BEEd, BSEd-Eng, BSEd-Math)", GS + "1pRcBdObJm75dFBXbRgMoKYxSfmtImgLsPcNBKbNxwkU/edit?usp=sharing"),
            ("BS Hospitality Management, BS Tourism Management, AB Political Science", None)]),
        ("SHS Corner 2025-2026", [
            ("Class schedules 2024-2025", GS + "1pfCUvPUHg4Wk36rMaf1O5TR7_4WRfvjodxaEq298_pw/edit?usp=sharing"),
            ("Grade 11 sectioning 2024-2025", GS + "1TM4neufKJ6Jvka_a5IgRsiSCColUijlZT5GpullXebg/edit?usp=sharing"),
            ("Grade 12 sectioning 2024-2025", GS + "1X2rt8-IdAeYgsVYW9SeQKk5KeJqm8OpEQAjArKKhv4w/edit?usp=sharing")]),
        ("Basic Education Corner 2025-2026", [
            ("SCC class schedule 2024-2025", "https://drive.google.com/file/d/1YA3n7qa6BiTLX5rC_ShXc0SPYo_B9ML1/view?usp=sharing"),
            ("Better Children class schedule 2024-2025", "https://drive.google.com/file/d/116WDvuquFs64qffpNB3aEGkIbfnFwRrI/view?usp=sharing"),
            ("Class list 2024-2025", "https://drive.google.com/file/d/1RGME0mTFWp7Go8gaL0j1amUep4KqnXTr/view?usp=sharing"),
            ("List of school requirements", "https://drive.google.com/file/d/1mVPzklhSi-ifSS8QPBUZc8ky0_UkCQiw/view?usp=sharing"),
            ("Schedule of activities", None)]),
    ],
}

# ---------------- CMS ----------------
CMS = {
    "intro": "CMS is one of the elements of St. Clare Online Education System. A Content Management System is a software application used to manage the creation and modification of digital content.",
    "elibrary": ("Welcome to our e-Library", "St. Clare College Learning Resource Center. Better Learning Anytime, Anywhere, Anyhow. Powered by ProQuest.", "https://www.proquest.com/login"),
}

# ---------------- IMS ----------------
IMS = {
    "intro": "The Institutional Management System (IMS) enables the school to facilitate the storage, organization and retrieval of information. This is where students complete their enrollment procedures, and where faculty log in and time in for their virtual classes' attendance.",
    "faculty": ("Faculty Corner 2026-2027", [
        ("Basic Ed faculty attendance monitoring", "Basic Ed online attendance", "https://docs.google.com/forms/d/1EGr_cO_fz8lmK9GH_lSb2p-SzfYWlhq7MHBluitpGXk/edit"),
        ("SHS faculty attendance monitoring", "SHS online attendance", "https://forms.gle/BC6B454wvAuf7dDt8"),
        ("Tertiary faculty attendance monitoring", "Tertiary online attendance", "https://forms.gle/aHUV165Mh4V5uRcF8")]),
    "hiring": ("We are hiring", "We are in need of Basic Education teachers, SHS teachers and College Instructors with the following qualifications:",
               ["NC II holder or its equivalent", "Licensed Professional Teacher", "Good communication skills", "Computer and technological skills", "Good moral character and trainable"],
               "mailto:stclarecollege.humanresource@gmail.com?subject=SHS%20APPLICANT%202023", "stclarecollege.humanresource@gmail.com"),
}

# ---------------- PMS ----------------
PMS = {
    "intro": "The Personal Management System (PMS) provides a platform for students and teachers to conduct their personal transactions. Students and teachers can set up their personal account; it provides an easy solution for online clients with an efficient response time.",
    "tes": ("Releasing of UniFAST guidelines for SY 2023-2024", [
        ("Step 1: Verification of TES grantee status", "Verify if you are officially listed as a TES grantee. Input your FULL NAME (e.g. DELA CRUZ, JUAN).", "Verify here", GS + "1FNLfCn24sx_M4myy19p2-vbNFY7haidyhz6jT3kSl0Y/edit?usp=sharing"),
        ("Step 2: Secure a disbursement schedule", "Once verified as a TES grantee, obtain your official disbursement schedule. Follow the assigned date and time strictly to avoid delays.", "Scheduler", "https://forms.gle/ro39GwPe6bwyDgb5A")]),
    "docreq": ("Official Document Request Portal", "All requests for official school documents (such as Transcript of Records, Diplomas, and others) must be processed only through the Official Document Request Portal of St. Clare College. Do NOT transact with fixers or unauthorized individuals.", "https://forms.gle/t7ixtaxJoEcc8rdz8", "poster-document-request"),
    "passport": ("Student Digital Passport 2023", "Fill out the form to receive your pictorial schedule. After completing the Google Form scheduler, wait for a notification of the date, time and assigned room for your ID pictorial. The schedule will be posted in the LMS (College Corner & SHS Corner).", "https://docs.google.com/forms/d/e/1FAIpQLSeAbuiMLGVpvBi6VctWh0mELsTTvZ50lr3dQGkeTx75V-JXcQ/viewform", "poster-digital-passport"),
    "epay": ("Dropbox for ePayments", "After paying online, send or attach proof of payment here. Please do not send proof of payment that is still being processed; upload the confirmation that the transaction was processed successfully.", "https://docs.google.com/forms/d/e/1FAIpQLSeYcitEs2uV4-nsbAc8QHhzm2MfHd_Ut1Sru5weRyl6s7hMUA/viewform", "poster-epayments-dropbox"),
    "grades": [
        ("e-Grades, SY 2023-2024 (2nd semester)", [
            ("BS Computer Science", GS + "1WXCiE8k8L5KnGkCUxwtctDSX9QZ1zjh2BsCR7qp7Gy8/edit#gid=1478829890"),
            ("BS Hospitality Management, BS Tourism Management, AB Political Science, BS Business Administration, BEEd / BSEd", None)]),
        ("e-Grades, SY 2023-2024 (1st semester)", [
            ("BS Computer Science", GS + "11yeDp54jGYae8KlX7xyzx2GnvvPgoasX0fUfR0Lq4N8/edit#gid=0"),
            ("BS Hospitality Management", GS + "1-qopd8bsrUcSBwVwW_gGZsHziXkZ_hoXFtCfU7lABMY/edit#gid=0"),
            ("BS Tourism Management", GS + "1PNqHVprh6mwR0tNRc-agjmRNgvQORSegjxmZRWYclJ4/edit#gid=0"),
            ("AB Political Science", GS + "1iMwwkPBhaowAdsRvmvTVohxJX7lUvgdbFZIVPKBFNGY/edit#gid=0"),
            ("BS Business Administration", GS + "1s9y-NLPGAVxqdFzSn7rhyL1KLMAcZDccvBSDmqhh_SQ/edit#gid=0")]),
        ("e-Grades, SY 2022-2023 (1st semester)", [
            ("BS Computer Science", GS + "1RtIHhK3qKuCqTHJuCey0uleW7nW8la0jfyQq0g0G_sI/edit?usp=sharing"),
            ("BS Hospitality Management", GS + "1EOjCh9BP5UsiXXj1anQxaUdjSUdMELeXHVgUjPqhP8s/edit?usp=sharing"),
            ("BS Tourism Management", GS + "1FwFZPjEOCvL_jsCXljSHoSWJ1EQIQFu2CSh5SQSoJsA/edit?usp=sharing"),
            ("AB Political Science", GS + "1bzsaY-z1DHfW_lvw7aAFT71i_mWN2plP6C2dBhfKnW8/edit?usp=sharing"),
            ("Bachelor of Elementary Education", GS + "1pb9OQ7kHJw1pezFy0L-iwrtkdpISUwtuxJQJpQwu5Z4/edit?usp=sharing"),
            ("BS Business Administration", GS + "1sG5k0wD18c0FJoeuQBJ2BitZo-scccloWoVd_0Bv2GA/edit?usp=sharing"),
            ("BSEd, Major in English", GS + "1AoN66R35MIfTbBlVvKFVIa6UHkvccmZdHSRuPCrmV8A/edit?usp=sharing"),
            ("BSEd, Major in Math", GS + "1IRKWHWQ8RYf2w0E194rPAiB32yN6Y7Als_-xnIv-v28/edit?usp=sharing")]),
        ("e-Grades, AY 2021-2022 (1st semester)", [
            ("BS Computer Science", GS + "1kP4OZ1y_uB7J8bGQmT1-cVljvkRPud3xIaHE7kbgxZY/edit?usp=sharing"),
            ("BS Hospitality Management", GS + "1kDKIFRTf_IcagFdrxrm9fcWNH_E6PInxjfTGicVdVWg/edit?usp=sharing"),
            ("BS Tourism Management", GS + "1WIjGPviHIIKywByDxqNg8X8Na5RLTfCa4drmuarUUcM/edit?usp=sharing"),
            ("AB Political Science", GS + "1-JrUgsqd1Kn9bVPsCIyGkuXe_H3H8f6swK3BMnCJ_XM/edit?usp=sharing"),
            ("Bachelor of Elementary Education", GS + "1I2qsA8g3Yp3scLi-GYgCmAfIni4ilRWc9iYarF7-mUk/edit?usp=sharing"),
            ("BS Business Administration", GS + "1mnt7DKqv6KE28YRK9tBW04KImpq37lokoF3WfzI_xZI/edit#gid=1564072974"),
            ("BSEd, Major in English", GS + "1JDzGXzXjzJD8G9LWZOW84LQyIfWuOSy_FuQ2AhMEWmw/edit?usp=sharing"),
            ("BSEd, Major in Math", GS + "1rr_GoaJP3J7lr3GjO0KS_FZNyZ5KZoZpmr_o0i0z2Cs/edit?usp=sharing")]),
    ],
}

# ---------------- VMS: video library (title, video id, date / note) ----------------
VMS_INTRO = "VMS is one of the elements of St. Clare Online Education System: a web-based platform for the digital aspects of courses of study. Broadcasting and Teacher-DJ are also part of the St. Clare OES-VMS."
VIDEOS = [
    ("Commencement", [
        ("The Stars of 2024: 38th Commencement Exercises", "z_bUjTOihzA", "June 17, 2024"),
        ("The Stars of 2024: 38th Commencement Exercises", "tbti8sIvU0c", "June 24, 2024"),
        ("The Stars of 2023: 37th Commencement Exercises (Tertiary)", "QJz-kf89UuY", "June 19, 2023"),
        ("The Stars of 2023: 37th Commencement Exercises (Senior High School)", "C97smHW4aXQ", "June 12, 2023"),
        ("The Stars of 2022: 36th Commencement Exercises @PICC", "NXxxWLRnops", "June 13, 2022"),
        ("Senior High School Stars of 2022 @PICC", "FRm-1v5DPzM", "June 10, 2022"),
        ("St. Clare College Virtual Graduation 2021 (BSCS, BSBA, BSHRM, BSTM, AB PolSci, Education)", "_t9fSNFCtKs", "2021"),
        ("Virtual Recognition 2021: St. Clare College & Better Children of Montessori Center", "XT0TDQKPRt4", "2021"),
        ("SHS Virtual Graduation 2021 (HUMSS, ABM, Arts & Design)", "Y_Xz1eUDAe8", "2021"),
        ("SHS Virtual Graduation 2021 (Sports, HE, ICT)", "5FSwG5EGPX8", "2021"),
        ("The Stars of 2020 & 2021: 34th Commencement Exercises", "SgLwY01FU_g", "2020-2021")]),
    ("Institution", [
        ("St. Clare College Professional Mace: The Eternal Flame of Professionalism", "0RI2tMRZf8w", "September 23, 2023"),
        ("St. Clare College Virtual Flag Ceremony (every Monday, 7:00 AM)", "QSRZvHk7TMA", "2022"),
        ("St. Clare College 36th Founding Anniversary", "CgWseRZfAK4", "August 31, 2021"),
        ("SCC Administrators, Officials & Staff 2021", "zDYPFpB0pK0", "2021"),
        ("Welcome to St. Clare (SCC Ads 2021)", "f4jWTiXrIOs", "2021"),
        ("St. Clare College Facilities 2021", "ENCCIBqdPMs", "2021"),
        ("St. Clare College 2021: the leading edge in online education system", "S_SYZ1X5Thk", "2021"),
        ("Dr. Ernesto Miguel Adalem (December 6, 1946 - July 25, 2010)", "8HnKxvZOuiw", "Tribute")]),
    ("Virtual Lab & online education", [
        ("St. Clare College Virtual Lab", "Ncj3mlHUiok", "2021"),
        ("St. Clare Online: Virtual Lab, Predator Thronos & Mixed Reality by Acer", "avbXu3J7PoI", "2021"),
        ("Continuity of Learning", "jwzbf0naZyE", "With St. Clare Online, no one gets left behind"),
        ("Online Education", "6mQrraOlI8o", "Trailer"),
        ("Our Future", "1_vsofl20fQ", ""),
        ("St. Clare College Learning Continuity Plan 2020", "gJ8XkyIbQcE", "2020"),
        ("Stay Connected 2021: Teacher-DJs during ECQ", "N1GZAgusopU", "2021"),
        ("SMNI News: private schools prepare for online learning", "ti21lo9x93Y", "News coverage")]),
    ("St. Clare College broadcast", [
        ("SAMA KA? Mental Health Awareness", "wgVNfrSFpAc", "Oct. 30, 2021"),
        ("United Nations Celebration 2021: No One Left Behind in Post-Pandemic Philippines", "WXqFvEkmYcA", "Oct. 25, 2021"),
        ("Happy World Teacher's Day 2021", "CVVwzWbc5Bk", "Oct. 5, 2021"),
        ("Feast Day of St. Padre Pio", "AInM_XLe3VQ", "Sept. 23, 2021"),
        ("Becoming the BEST YOU: A Life Coaching Program", "cn62ryejSD4", "September 21, 2021")]),
    ("Linkages", [
        ("COVID-19 Pediatric Vaccination: A Town Hall for Parents/Guardians (SDO-Caloocan City & DOH)", "me7VeF0Q9Lo", ""),
        ("Harnessing our Mutual Responsibilities to Solve Global Changes (One Shared World)", "YKo-qhGousg", "")]),
    ("Start Up Module 2020", [
        ("Start Up Module Day 1: Dr. Clarita G. Adalem, President", "JlzZtYSAB_E", "August 24, 2020"),
        ("Start Up Module Day 1, Part 1", "OKNf6diqfY4", "August 24, 2020"),
        ("Start Up Module Day 1, Part 2: Orientation Seminar for Students and Parents", "-XhxoQVIxGk", "August 24, 2020"),
        ("Start Up Module Day 2: Rules and Regulations, Life Skills Overview, Qualities of a St. Clare Student", "hB5K610SMc8", "August 26, 2020"),
        ("Start Up Module Day 3: Making Online Learning Effective, St. Clare Core Values", "_gBG3XkPWYk", "August 28, 2020"),
        ("Start Up Module Day 4: Parenting Seminar", "CDukiooHMIc", "August 29, 2020")]),
    ("St. Clare Feast Day 2020", [
        ("President's Greetings: Dr. Clarita G. Adalem", "jMJxFrDZgO4", "August 11, 2020"),
        ("St. Clare Feast Day Virtual Mass: Rev. Fr. John Harvey Bagos", "6QfD8wObP_U", "August 11, 2020"),
        ("Life of Saint Clare", "SJ-Af-JAsWw", "")]),
    ("Webinar series: Life Skills & Technology in Virtual Learning", [
        ("Episode 03: The Role of the Parents in the Virtual Learning (Dr. Clarita G. Adalem, President)", "1ZgTVo6yjt0", ""),
        ("Episode 02: Essentials in Online Learning and Champion SCC Students (Prof. Dr. Samuel M. Salvador, Chancellor, Royal Institution, Singapore)", "WBaac9Lo8Sg", ""),
        ("Episode 01: From Face to Face Classroom Learning to \"Heart to Heart\" Home Learning (Dean Henry S. Tenedero)", "GRGahlbw5E8", "")]),
]

# ---------------- History (from the school's article "The leading edge in Online Education System") ----------------
HISTORY = [
    ("Early '80s", "Computer literacy from pre-school", "St. Clare's preparation for digital learning, through the efforts of its founder Dr. Clarita G. Adalem and the late chairman Dr. Ernesto M. Adalem, started with basic computer literacy as a subject in the pre-school and elementary levels."),
    ("1985", "St. Clare College is founded", "Founded on 31 August 1985 in Caloocan City, Metro Manila."),
    ("2013", "E-books and tablets", "St. Clare adopted e-learning by shifting to e-books, making it the 3rd school in the country to use tablets in lieu of physical textbooks."),
    ("2016", "E-boards in all 95 classrooms", "St. Clare College became the first college in the country to use e-boards in all 95 classrooms, removing all blackboards and eliminating chalk dust. That year, Taiwan's ICT Division visited to help strengthen its ICT capability."),
    ("2019", "Education 4.0 and a wired campus", "Development plans for 2019-2025 call for the entire campus to become a \"wired college\" meeting the 3 I's of online education: infrastructure, infostructure and infoculture. St. Clare launched its preparations for Education 4.0, collaborating with Optimus IT Solutions, Acer and Bicore One, provider of the FNET platform."),
    ("2020", "St. Clare Online keeps learning going", "During the pandemic the college moved classes to its own online platform so no student got left behind. Its Start Up Module reached 547,806 views."),
    ("2021", "The Virtual Lab", "The Virtual Lab (VR + AR = MR) opened with the Predator Thronos and the Mixed Reality facility by Acer, and the college marked its 36th founding anniversary."),
    ("2023", "The Professional Mace", "On 23 September 2023 St. Clare College introduced its Professional Mace: \"The Eternal Flame of Professionalism\", \"a beacon of professionalism and culture of excellence\"."),
    ("2024", "The Stars of 2024", "The 38th Commencement Exercises were held in June 2024."),
]
LEADERS = [
    ("Dr. Clarita G. Adalem", "Founder and President, St. Clare College"),
    ("Dr. Ernesto M. Adalem", "Late Chairman (December 6, 1946 - July 25, 2010)"),
    ("Dean Henry S. Tenedero", "Dean, St. Clare College Life Skills for Life Success"),
]
PARTNERS = [("partner-fnet", "FNET by Bicore One"), ("partner-predator", "Acer Predator"), ("partner-mixed-reality", "Mixed Reality"), ("partner-microsoft", "Microsoft"), ("partner-google", "Google"), ("partner-unesco", "UNESCO")]
SCO_CHANNELS = [("sco-online-logo", "SCO Online"), ("sco-live", "SCO Live"), ("sco-education-that-matters", "Education That Matters"), ("sco-heart-of-a-champion", "Heart of a Champion"), ("sco-sports-desk", "Sports Desk"), ("sco-virtual-lab", "Virtual Lab"), ("sco-leading-women", "Leading Women"), ("sco-health-talk", "Health Talk"), ("sco-digital-first", "Digital First")]

# ---------------- News & announcements (newest first, dated as on the source) ----------------
NEWS_FULL = [
    ("2024", "Opening of classes, Academic Year 2024-2025", "Opening of classes for Basic Education, Senior High School and Tertiary, Academic Year 2024-2025.", "poster-opening-of-classes-2024", None),
    ("Class of 2024", "SHS Alumni VIP Package", "To all SHS graduates of St. Clare College Class 2024: in our commitment to value and support our senior high school graduates as they embark on their journey to college, we present the SHS Alumni VIP Package, which includes the President's Scholarship and zero down payment for the school year 2024-2025.", "poster-shs-alumni-vip", None),
    ("Sept 23, 2023", "The Professional Mace: The Eternal Flame of Professionalism", "\"A beacon of professionalism and culture of excellence.\" By ERA & EJA.", None, "0RI2tMRZf8w"),
    ("SY 2023-2024", "Releasing of UniFAST guidelines", "Verify your TES grantee status, then secure your official disbursement schedule on the PMS.", None, None),
    ("SY 2023-2024", "Enrollment for School Year 2023-2024", "Online enrollment: simplified and seamless. Pre-school to Junior High; Senior High School (ABM, HUMSS, Arts & Design, TVL-ICT, TVL-HE); Tertiary (BEEd, BSEd-Eng, BSEd-Math, BSCS, BSBA, BSHM, BSTM, AB PolSci).", "poster-online-enrollment", None),
    ("2023", "Choose your modality", "Personalized Learning Pathways: Empowering Students to Choose Their Ideal Modality for Success - Full Online or Blended!", "poster-flexible-study", None),
    ("Dec 6, 2021", "Learning Resource Center e-Library", "St. Clare College Learning Resource Center: Better Learning Anytime, Anywhere, Anyhow. Powered by ProQuest.", "poster-elibrary-proquest", None),
    ("2020", "Health Survey Form", "This form is intended for the students, parents, teachers and non-teaching personnel of St. Clare College only.", None, None),
    ("2020", "547,806 views", "Thank you for making St. Clare Online \"the leading edge in online education system\": Start Up Module, 547,806 views.", "poster-547806-views", None),
    ("Oct 26, 2020", "Class suspension: typhoon Quinta", "As per advisory from the Office of City Mayor Oca Malapitan, all classes were suspended due to typhoon Quinta that may cause interruption in internet connectivity and electricity. UniFAST TES distribution continued.", "poster-walang-pasok-2020", None),
    ("Oct 2020", "UniFAST TES distribution", "All slots for the first 4 batches of releasing for UniFAST TES grantees were filled on a first-come, first-served basis. Only qualified grantees were allowed to register.", "poster-tes-announcement", None),
    ("2020", "UniFAST-TES late claims schedule", "Procedures for face-to-face and bank transfer transactions.", "poster-tes-late-claims-f2f", None),
    ("A.Y. 2020-2021", "Application for UniFAST-TES is now open", "Complete requirements were submitted directly to the registrar's office.", "poster-tes-2020", None),
    ("2020", "The leading edge in Online Education System", "Long before the COVID-19 crisis, St. Clare College prepared its ICT capability and development, from computer literacy in the '80s to e-boards in all 95 classrooms and Education 4.0.", "virtual-lab-predator-units", None),
    ("News coverage", "SMNI News: private schools prepare for online learning", "\"Ilang Private School, tinututukan ang Online Learning para sa pasukan\" - SMNI news coverage.", None, "ti21lo9x93Y"),
]
HEALTH_SURVEY = "https://docs.google.com/forms/d/e/1FAIpQLSfg1n_vhsY0xhUKjLutY4BOs83hfSZX36Hwtae-Hs2oai5fog/viewform"

# ---------------- Calendar ----------------
CAL_2025 = [
    ("2025", "Regular class: all levels", "St. Clare Online Education System", ""),
    ("September 1-4, 2025", "Class orientation & sectioning", "St. Clare College", "Meet & greet with your teachers, advisers, instructors and professors. Sectioning for new and old students who are not yet enlisted."),
    ("August 31, 2025", "President's Birthday", "St. Clare College", ""),
    ("2025", "Parents' webinar orientation: Tertiary", "St. Clare Virtual Studio", "1:00 PM - 3:00 PM"),
    ("2025", "Parents' webinar orientation: Basic Education & SHS", "St. Clare Virtual Studio", "Basic Education 9:00 AM; Senior High School 1:00 PM"),
]
CAL_2020 = [
    ("September 1, 2020", "Regular academic class", "St. Clare College, Caloocan City", "7:00 AM - 7:00 PM; Virtual Thanksgiving Mass"),
    ("August 31, 2020", "Foundation Day festivities", "Online", "St. Clare Flix infomercial making contest; St. Clare Spoken Poetry online competition; St. Clare Idol online singing"),
    ("August 29, 2020", "Parenting seminar", "Online", "9:00 AM - 12:00 NN; Tertiary, Senior High, Junior High, Elementary, Kindergarten"),
    ("August 24, 2020", "Start Up Module", "Online", ""),
    ("August 11, 2020", "Feast of St. Clare", "Online", "10:00 AM - 1:00 PM"),
]

ENROLL_SLIDES = [("slide-enrollment-open", "SY 2023-2024 enrollment is now open"), ("slide-enrollment-procedure", "Enrollment procedure"),
                 ("slide-college-programs", "College programs"), ("slide-college-requirements", "College admission requirements"),
                 ("slide-shs-tracks", "Senior High School tracks & strands"), ("slide-shs-requirements", "Senior High School admission requirements"),
                 ("slide-basic-ed-requirements", "Basic Education admission requirements"), ("slide-basic-ed-uniform", "Basic Education school uniform"),
                 ("slide-vision-mission", "Vision & mission")]
FLIERS = [("flier-tertiary", "Tertiary programs"), ("flier-shs", "Senior High School"), ("flier-basic-ed", "Basic Education")]
