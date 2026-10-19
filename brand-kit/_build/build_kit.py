# Builds src/brand-kit/index.html (St. Clare College brand kit) + a ZIP of every file. Client-branded; facts only from stclareonline.com.
import os, json, zipfile, html
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
KIT = os.path.join(SRC, "brand-kit")
E = html.escape
META = json.load(open(os.path.join(HERE, "materials.json"), encoding="utf-8"))
import materials as MT

def rgb(h): h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def cmyk(h):
    r, g, b = [x / 255 for x in rgb(h)]; k = 1 - max(r, g, b)
    if k >= 1: return (0, 0, 0, 100)
    return tuple(round(100 * x) for x in ((1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k))
def lum(h):
    def c(v): v /= 255; return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    r, g, b = rgb(h); return .2126 * c(r) + .7152 * c(g) + .0722 * c(b)
def contrast(a, b): la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + .05) / (lb + .05)

COLORS = [  # name, hex, role, group
    ("Maroon 950", "#24040a", "Deepest ground, hero shadows", "core"), ("Maroon 900", "#3d0610", "Hero and banner ground", "core"),
    ("Maroon 800", "#5c0a17", "Dark section bands", "core"), ("Maroon 700", "#7a0c1e", "Primary brand colour", "core"),
    ("Crimson 600", "#a6192e", "Links, primary buttons", "core"), ("Red 500", "#c8102e", "Actions, highlights, focus", "core"),
    ("Seal Gold", "#e0ad1c", "Accent: rules, numbers, CTAs on dark", "accent"), ("Ebony", "#141211", "Ribbons and footer", "accent"),
    ("Rose 100", "#f6e1e4", "Soft tints, chips", "neutral"), ("Rose 50", "#fcf3f4", "Hover and card tints", "neutral"),
    ("Warm White", "#f8f5f5", "Light section ground", "neutral"), ("Ink", "#1d1416", "Headings on light", "neutral"), ("Muted", "#675a5e", "Body copy on light", "neutral")]
SEAL_COLORS = [("Seal Yellow", "#fee600"), ("Seal Blue", "#003cff"), ("Seal Red", "#fe0013"), ("Seal Green", "#178d00")]  # sampled from img/seal.png

GROUP_TITLES = {"01-logo": "Logo files", "02-social-posts": "Social media posts (1080 x 1440, 3:4)", "03-stories": "Stories and reels covers (1080 x 1920)",
                "04-covers-banners": "Covers, banners and screens", "05-print": "Print: posters, flyer, stationery, cards"}

def kb(n): return f"{n / 1024:.0f} KB" if n < 1024 * 1024 else f"{n / 1048576:.1f} MB"

def materials_html():
    out = []
    for g, title in GROUP_TITLES.items():
        items = [m for m in META if m["group"] == g]
        cards = []
        for m in items:
            dls = "".join(f'<a class="dl" href="{m["files"][i]}" download>{k.upper()} <small>{kb(m["sizes"][k])}</small></a>' for i, k in enumerate(m["sizes"]))
            cards.append(f'<figure class="mat"><button class="mat-pic" type="button" data-full="{m["files"][0]}" aria-label="Preview {E(m["title"])}"><img src="{m["thumb"]}" alt="{E(m["title"])}" loading="lazy"></button>'
                         f'<figcaption><b>{E(m["title"])}</b><small>{m["w"]} x {m["h"]} px</small><span class="dls">{dls}</span></figcaption></figure>')
        out.append(f'<div class="mat-group" id="m-{g}"><h3>{E(title)} <span>{len(items)}</span></h3><div class="mats">{"".join(cards)}</div></div>')
    return "".join(out)

def swatch(n, h, role):
    r, g, b = rgb(h); c, m, y, k = cmyk(h)
    cw, cb = contrast(h, "#ffffff"), contrast(h, "#1d1416")
    fg = "#fff" if cw >= cb else "#1d1416"
    best = f"{max(cw, cb):.1f}:1 with {'white' if cw >= cb else 'ink'} text"
    return f'''<button class="sw" type="button" data-copy="{h}" style="--c:{h};--fg:{fg}" aria-label="Copy {n} {h}">
  <span class="chipc"><b>{n}</b><i>{h.upper()}</i></span>
  <span class="meta"><span>{E(role)}</span><code>RGB {r} {g} {b}</code><code>CMYK {c} {m} {y} {k}</code><em>{best}</em></span></button>'''

def build():
    core = "".join(swatch(n, h, r) for n, h, r, g in COLORS if g == "core")
    acc = "".join(swatch(n, h, r) for n, h, r, g in COLORS if g == "accent")
    neu = "".join(swatch(n, h, r) for n, h, r, g in COLORS if g == "neutral")
    seal = "".join(f'<div class="sc"><span style="background:{h}"></span><b>{n}</b><code>{h.upper()}</code></div>' for n, h in SEAL_COLORS)
    total = sum(sum(m["sizes"].values()) for m in META)
    sig = MT.SIG
    page = f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow">
<meta name="color-scheme" content="light"><title>St. Clare College Brand Kit</title>
<meta name="description" content="St. Clare College of Caloocan brand kit: seal, colours, typography, graphic elements, photography, voice and ready-to-use marketing materials.">
<link rel="icon" href="../img/seal-256.webp" type="image/webp"><link rel="preload" href="../fonts/jakarta.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="kit.css?v=1"><script src="kit.js?v=1" defer></script></head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap"><a class="brand" href="#main"><img src="../img/seal-128.webp" alt="" width="40" height="40"><span><b>St. Clare College</b><small>Brand kit</small></span></a>
<nav aria-label="Brand kit sections"><a href="#logo">Logo</a><a href="#colour">Colour</a><a href="#type">Type</a><a href="#elements">Elements</a><a href="#photo">Photography</a><a href="#voice">Voice</a><a href="#materials">Materials</a></nav>
<a class="zip" href="files/st-clare-brand-kit.zip" download>Download all <small>{kb(total)} ZIP</small></a></div></header>
<main id="main">
<section class="hero"><div class="gridfloor" aria-hidden="true"><i></i></div><img class="hero-seal" src="../img/seal.png" alt="St. Clare College of Caloocan seal" width="420" height="434">
 <div class="wrap"><p class="crumb">St. Clare College of Caloocan</p><h1>Brand kit</h1>
 <p class="lede">Everything needed to make St. Clare materials look and sound like the website: the official seal, the crimson and maroon palette, type, graphic elements, photography, voice and {len(META)} ready-to-use templates.</p>
 <div class="hero-meta"><span><b>{len(META)}</b> materials</span><span><b>13</b> colours</span><span><b>2</b> typefaces</span><span><b>1</b> seal</span></div></div></section>

<section class="sec" id="logo"><div class="wrap"><div class="sh"><h2>Logo: the official seal</h2><p>The seal is the only logo. It is used exactly as supplied by the college, in full colour, never redrawn, recoloured or cropped.</p></div>
 <div class="logo-grid">
  <figure class="lg lg-white"><img src="../img/seal.png" alt="Seal on white"><figcaption>On white or warm white</figcaption></figure>
  <figure class="lg lg-dark"><img src="../img/seal.png" alt="Seal on maroon"><figcaption>On maroon and crimson</figcaption></figure>
  <figure class="lg lg-photo"><img src="../img/seal.png" alt="Seal on photo"><figcaption>On photos: only on a dark scrim</figcaption></figure></div>
 <div class="rules">
  <div class="rule-card"><div class="clear"><span class="cs"><img src="../img/seal.png" alt=""></span></div><h3>Clear space</h3><p>Keep a margin of one quarter of the seal's width on every side. Nothing (text, edges, other logos) enters this space.</p></div>
  <div class="rule-card"><div class="minsz"><img src="../img/seal.png" alt="" style="width:96px"><img src="../img/seal.png" alt="" style="width:48px"><img src="../img/seal.png" alt="" style="width:24px"></div><h3>Minimum size</h3><p>Print: 18 mm wide. Screen: 48 px wide (24 px only for browser icons). Below that the ring lettering is unreadable.</p></div>
  <div class="rule-card"><div class="lockup-demo"><img src="../img/seal.png" alt=""><span><b>St. Clare College</b><small>of Caloocan &middot; The School of Life Skills</small></span></div><h3>Lockup</h3><p>Seal + "St. Clare College" in Plus Jakarta Sans ExtraBold, with "of Caloocan" and the tagline beneath. Use the files below; don't retype it.</p></div></div>
 <h3 class="h3">Don't</h3>
 <div class="donts">
  <figure><img src="../img/seal.png" alt="" style="filter:hue-rotate(160deg)"><figcaption>Recolour it</figcaption></figure>
  <figure><img src="../img/seal.png" alt="" style="transform:scaleX(1.35)"><figcaption>Stretch or squash it</figcaption></figure>
  <figure><img src="../img/seal.png" alt="" style="transform:rotate(-18deg)"><figcaption>Rotate it</figcaption></figure>
  <figure><img src="../img/seal.png" alt="" style="clip-path:inset(0 0 40% 0)"><figcaption>Crop it</figcaption></figure>
  <figure class="busy"><img src="../img/seal.png" alt=""><figcaption>Place it on busy photos</figcaption></figure>
  <figure><img src="../img/seal.png" alt="" style="opacity:.35;filter:blur(1px)"><figcaption>Fade, blur or add effects</figcaption></figure></div>
 <p class="files-line">Logo files: {" &middot; ".join(f'<a href="{m["files"][0]}" download>{E(m["title"])}</a>' for m in META if m["group"] == "01-logo")} &middot; <a href="../img/seal.png" download>Seal PNG, transparent (1024 px)</a></p>
</div></section>

<section class="sec alt" id="colour"><div class="wrap"><div class="sh"><h2>Colour</h2><p>A tonal scale of deep crimson and maroon carries the brand; the seal's gold is the accent; ebony grounds ribbons and the footer. Select a swatch to copy its HEX.</p></div>
 <h3 class="h3">Core reds</h3><div class="sws">{core}</div>
 <h3 class="h3">Accent</h3><div class="sws two">{acc}</div>
 <h3 class="h3">Neutrals</h3><div class="sws">{neu}</div>
 <h3 class="h3">Seal colours <small>(inside the seal only, never as brand colours)</small></h3><div class="seal-cols">{seal}</div>
 <div class="ratio"><div><b>Proportion</b><p>On every piece: about 60% maroon/crimson grounds, 25% white and warm white, 10% ebony, 5% gold. Gold is for one or two accents, never large fields of text.</p></div>
  <div class="bar"><span style="flex:60;background:linear-gradient(160deg,#24040a,#5c0a17)"></span><span style="flex:25;background:#f8f5f5"></span><span style="flex:10;background:#141211"></span><span style="flex:5;background:#e0ad1c"></span></div></div>
 <div class="grads"><figure style="background:radial-gradient(60% 55% at 100% 0%,rgba(200,16,46,.45),transparent 62%),radial-gradient(50% 50% at 0% 100%,rgba(224,173,28,.13),transparent 60%),linear-gradient(160deg,#24040a,#5c0a17 55%,#3d0610)"><figcaption>Hero gradient: maroon 950 → 800 → 900 with a crimson glow top-right and a gold glow bottom-left</figcaption></figure>
  <figure style="background:linear-gradient(90deg,#24040a,#7a0c1e 60%,#e0ad1c)"><figcaption>Accent rule: maroon to gold, for thin bars only</figcaption></figure></div>
</div></section>

<section class="sec" id="type"><div class="wrap"><div class="sh"><h2>Typography</h2><p>Two typefaces, both free (Google Fonts). Headings are tight and bold; body text is calm and readable.</p></div>
 <div class="fonts">
  <div class="font"><span class="tag">Headings</span><p class="spec j">Aa</p><h3>Plus Jakarta Sans</h3><p>ExtraBold 800 for headlines, Bold 700 for labels and buttons. Tracking -2.5%, line height 1.02 to 1.1.</p><a href="https://fonts.google.com/specimen/Plus+Jakarta+Sans" target="_blank" rel="noopener">Get the font</a></div>
  <div class="font"><span class="tag">Body</span><p class="spec i">Aa</p><h3>Inter</h3><p>Regular 400 for body, SemiBold 600 for emphasis. Line height 1.6; never below 12 px on screens or 8 pt in print.</p><a href="https://fonts.google.com/specimen/Inter" target="_blank" rel="noopener">Get the font</a></div></div>
 <div class="scale">
  <div><span>Display &middot; 72-96 px</span><p class="j" style="font-size:clamp(2.4rem,6vw,4.6rem)">The School of Life Skills</p></div>
  <div><span>H2 &middot; 40 px</span><p class="j" style="font-size:2.4rem">Programmes for every stage</p></div>
  <div><span>H3 &middot; 22 px</span><p class="j" style="font-size:1.4rem">Senior High School tracks</p></div>
  <div><span>Body &middot; 17 px</span><p class="i" style="font-size:1.06rem;max-width:62ch">St. Clare College of Caloocan educates learners from Nursery to College, on one campus in Caloocan City and online through St. Clare Online.</p></div>
  <div><span>Label &middot; 12 px caps</span><p class="i" style="font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:#a6192e">Admissions &middot; Founded 31 August 1985</p></div></div>
 <div class="tester"><label for="tt">Try a headline</label><input id="tt" value="Become a Clarean" maxlength="60"><p class="j tt-out">Become a Clarean</p></div>
</div></section>

<section class="sec alt" id="elements"><div class="wrap"><div class="sh"><h2>Graphic elements</h2><p>The pieces that make a St. Clare layout recognisable. Combine two or three; never all at once.</p></div>
 <div class="els">
  <figure class="el"><div class="el-box crimsonbox"><div class="gridfloor" aria-hidden="true"><i></i></div></div><figcaption><b>Running grid floor</b><span>Fine gold perspective grid on dark grounds, fading upward. Small cells (22-56 px). Moves slowly on screen; static in print.</span></figcaption></figure>
  <figure class="el"><div class="el-box crimsonbox wmbox"><img src="../img/seal-512.webp" alt=""></div><figcaption><b>Seal watermark</b><span>The seal at 5-8% opacity, greyed, bleeding off a corner of dark bands.</span></figcaption></figure>
  <figure class="el"><div class="el-box lightbox dotsbox"></div><figcaption><b>Dot lattice</b><span>Crimson (light grounds) or gold (dark grounds) 18 px dots, fading out from one corner.</span></figcaption></figure>
  <figure class="el"><div class="el-box lightbox"><span class="demo-rule"></span><b class="j" style="font-size:1.6rem;color:#1d1416;display:block;margin-top:14px">Section title</b></div><figcaption><b>Accent rule</b><span>A short 40-52 px bar above titles: red on light, gold on dark.</span></figcaption></figure>
  <figure class="el"><div class="el-box ebonybox"><div class="rib"><span><em>College</em>BS Computer Science</span><span><em class="f">Since</em>1985 in Caloocan City</span></div></div><figcaption><b>Ribbon and chips</b><span>Ebony band with gold-outlined level tags; solid gold chips mark facts.</span></figcaption></figure>
  <figure class="el"><div class="el-box lightbox btns"><span class="b1">How to enroll &rarr;</span><span class="b2">How to enroll &rarr;</span><span class="b3">Contact admissions</span></div><figcaption><b>Buttons</b><span>Pills. Crimson on light, gold on dark, outline as the secondary action. Arrow means "go".</span></figcaption></figure>
  <figure class="el"><div class="el-box lightbox"><div class="icons"><svg viewBox="0 0 24 24"><path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg><svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></div></div><figcaption><b>Icons</b><span>Bare 1.7-2 px line icons in crimson. Never inside tiles or circles.</span></figcaption></figure>
  <figure class="el"><div class="el-box crimsonbox numbox"><b class="j">95</b><span>classrooms with e-boards</span></div><figcaption><b>Big numbers</b><span>Gold ExtraBold figures for facts: 1985, 95, 8, 38th. Outlined style for years.</span></figcaption></figure></div>
</div></section>

<section class="sec" id="photo"><div class="wrap"><div class="sh"><h2>Photography</h2><p>Real St. Clare people and places: the campus, the Virtual Lab, classrooms, graduation. Warm, bright and candid.</p></div>
 <div class="photos">{"".join(f'<figure><img src="../{p}" alt="{E(c)}" loading="lazy"><figcaption>{E(c)}</figcaption></figure>' for p, c in [("img/hero/web/hero-01-campus-building.webp", "Campus, Zabarte Road"), ("img/hero/web/hero-02-virtual-lab.webp", "Virtual Lab"), ("img/hero/web/hero-03-graduates-2024.webp", "The Stars of 2024"), ("img/hero/web/hero-04-library.webp", "Library and Learning Resource Center"), ("img/site/prog-bshm.webp", "Hospitality students"), ("img/site/basic-kinder.webp", "Basic Education")])}</div>
 <div class="dodont"><div><h3>Do</h3><ul><li>Use real photos of St. Clare students, staff and campus.</li><li>Put text over photos only on a maroon scrim (dark at the text side).</li><li>Leave room on the left or bottom for headlines.</li><li>Keep skin tones natural; no heavy filters.</li></ul></div>
  <div><h3>Don't</h3><ul><li>Use stock photos of other schools or foreign campuses.</li><li>Use cartoon or clip-art people.</li><li>Put white text straight on bright photos.</li><li>Use photos with old dated offers visible as if they were current.</li></ul></div></div>
</div></section>

<section class="sec alt" id="voice"><div class="wrap"><div class="sh"><h2>Voice and messaging</h2><p>Warm, proud and clear. A college for professional life that still knows every student by name.</p></div>
 <div class="voice">
  <div class="vcard big"><span class="tag">Tagline</span><p class="j">The School of Life Skills</p></div>
  <div class="vcard"><span class="tag">Brand line</span><p>Transforming education, building our future.</p></div>
  <div class="vcard"><span class="tag">Student name</span><p>Students are <b>Clareans</b>. "Become a Clarean" is the enrollment call to action.</p></div>
  <div class="vcard wide"><span class="tag">Boilerplate (copy this)</span><p id="boil">St. Clare College of Caloocan is the School of Life Skills and a leading institution for professional development. Founded on 31 August 1985 in Caloocan City, Metro Manila, it educates learners from Nursery to College, on campus or fully online through St. Clare Online, with e-boards in all 95 classrooms and a Virtual Lab for mixed reality.</p><button class="copy" type="button" data-copy-el="boil">Copy text</button></div>
  <div class="vcard"><span class="tag">Vision</span><p>To become the leading institution for professional development and the first and foremost provider of quality, affordable and sustainable development education.</p></div>
  <div class="vcard"><span class="tag">Mission</span><p>To provide quality and excellent global education for the total development of a responsible, innovative, skillful and professional global workforce whose values and dignity are beyond par.</p></div></div>
 <div class="facts"><h3>Approved facts</h3><ul>
  <li><b>Founded</b> 31 August 1985, Caloocan City</li><li><b>Levels</b> Nursery to Grade 10, Senior High School, College</li><li><b>College</b> BSHM, BSBA, BSCS, BEEd, BSEd (English, Math), BSTM, AB PolSci</li>
  <li><b>SHS</b> ABM, HUMSS, Arts &amp; Design, TVL-ICT, TVL-HE</li><li><b>Campus</b> E-boards in all 95 classrooms; Virtual Lab (VR + AR = MR)</li><li><b>Learning</b> Full online or blended</li>
  <li><b>Phone</b> (02) 8232-4483</li><li><b>Email</b> stclarecollege.ph@gmail.com</li><li><b>Address</b> Zabarte Road, Barangay 172, Camarin, Caloocan City 1400</li></ul>
  <p class="note">Fees, enrollment dates and scholarships change every school year: always say "call (02) 8232-4483 to confirm" rather than printing a figure.</p></div>
 <div class="ctas"><h3>Calls to action</h3><div><span>How to enroll</span><span>Become a Clarean</span><span>Explore programmes</span><span>See the requirements</span><span>Contact admissions</span><span>Enroll online (IMS)</span></div></div>
</div></section>

<section class="sec" id="materials"><div class="wrap"><div class="sh"><h2>Marketing materials</h2><p>{len(META)} ready-to-use files built from the website's design. Replace the placeholder text (names, dates) before printing. Select a preview to enlarge it.</p></div>
 <nav class="mat-nav">{"".join(f'<a href="#m-{g}">{E(t.split(" (")[0])}</a>' for g, t in GROUP_TITLES.items())}<a href="#m-email">Email signature</a></nav>
 {materials_html()}
 <div class="mat-group" id="m-email"><h3>Email signature</h3><div class="sigbox"><div class="sig-prev">{sig}</div><div><p>Select the signature, copy and paste it into Gmail settings &rarr; Signature. Replace the name and position.</p><button class="copy" type="button" data-copy-html="sig">Copy signature</button> <a class="dl" href="files/06-email/email-signature.html" download>HTML file</a></div></div><template id="sig">{sig}</template></div>
 <p class="zipline"><a class="zipbtn" href="files/st-clare-brand-kit.zip" download>Download every file ({kb(total)} ZIP)</a></p>
</div></section>
</main>
<footer class="foot"><div class="wrap"><span>St. Clare College of Caloocan &middot; Brand kit</span><a href="../index.html">Visit the website</a></div></footer>
<dialog class="lb" aria-label="Preview"><button class="x" type="button" aria-label="Close preview">&times;</button><img alt=""></dialog>
<p class="toast" role="status" aria-live="polite"></p>
</body></html>'''
    open(os.path.join(KIT, "index.html"), "w", encoding="utf-8", newline="\n").write(page)
    # ZIP of every material + seal + fonts note
    zp = os.path.join(KIT, "files", "st-clare-brand-kit.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(os.path.join(KIT, "files")):
            for f in files:
                if f.endswith(".zip"): continue
                p = os.path.join(root, f); z.write(p, os.path.join("St Clare Brand Kit", os.path.relpath(p, os.path.join(KIT, "files"))))
        z.write(os.path.join(SRC, "img", "seal.png"), "St Clare Brand Kit/01-logo/seal-transparent-1024.png")
        z.writestr("St Clare Brand Kit/README.txt", "St. Clare College of Caloocan brand kit\n\nColours: Maroon 700 #7a0c1e (primary), Crimson 600 #a6192e, Red 500 #c8102e, Seal Gold #e0ad1c, Ebony #141211, Maroon 950/900/800 #24040a/#3d0610/#5c0a17.\nFonts: Plus Jakarta Sans (headings), Inter (body) - free on Google Fonts.\nUse the seal only as supplied. Confirm fees and dates with admissions (02) 8232-4483 before printing.\nFull guide: brand-kit/index.html on the website.\n")
    print("kit built; zip", os.path.getsize(zp) // 1024, "KB")

if __name__ == "__main__":
    build()
