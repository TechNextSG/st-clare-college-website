# St. Clare College brand kit: marketing material templates (HTML) rendered to PNG / PDF with headless Chrome.
# Output: ../src/brand-kit/files/<group>/<name>.png|pdf  (+ thumbnails in ../src/brand-kit/thumbs)
import os, subprocess, tempfile, shutil, json, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.abspath(os.path.join(HERE, "..", "src"))
OUT = os.path.join(SRC, "brand-kit", "files")
THUMBS = os.path.join(SRC, "brand-kit", "thumbs")
WORK = os.path.join(HERE, "_tpl")
CH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
U = "file:///" + SRC.replace("\\", "/")

PHONE, EMAIL = "(02) 8232-4483", "stclarecollege.ph@gmail.com"
ADDR = "Zabarte Road, Barangay 172, Camarin, Caloocan City 1400, Metro Manila"
FB, YT, WEB = "facebook.com/stclarecollege", "youtube.com · St. Clare College", "stclareonline.com"

BASE = f"""
@font-face {{ font-family: J; src: url({U}/fonts/jakarta.woff2) format("woff2"); font-weight: 500 800; }}
@font-face {{ font-family: I; src: url({U}/fonts/inter.woff2) format("woff2"); font-weight: 400 700; }}
:root {{ --m950:#24040a; --m900:#3d0610; --m800:#5c0a17; --m700:#7a0c1e; --c600:#a6192e; --r500:#c8102e; --gold:#e0ad1c; --rose:#f6e1e4; --ebony:#141211; --ink:#1d1416; --muted:#675a5e; }}
* {{ box-sizing: border-box; margin: 0; }}
html, body {{ width: 100%; height: 100%; }}
body {{ font-family: I, Arial, sans-serif; color: #fff; overflow: hidden; -webkit-font-smoothing: antialiased; }}
h1, h2, h3, b.h {{ font-family: J, Arial, sans-serif; letter-spacing: -.025em; line-height: 1.02; font-weight: 800; }}
.crimson {{ color: #fff; background:
   radial-gradient(60% 55% at 100% 0%, rgba(200,16,46,.45), transparent 62%),
   radial-gradient(50% 50% at 0% 100%, rgba(224,173,28,.13), transparent 60%),
   linear-gradient(160deg, var(--m950) 0%, var(--m800) 55%, var(--m900) 100%); }}
.grid {{ position: absolute; left: 0; right: 0; bottom: 0; height: 46%; overflow: hidden; perspective: 900px; perspective-origin: 50% 0;
   -webkit-mask-image: linear-gradient(to top, #000 10%, rgba(0,0,0,.5) 55%, transparent); }}
.grid i {{ position: absolute; left: -60%; right: -60%; top: 0; height: 420%; transform-origin: 50% 0; transform: rotateX(72deg);
   background-image: linear-gradient(rgba(240,196,96,.22) 1px, transparent 1px), linear-gradient(90deg, rgba(240,196,96,.15) 1px, transparent 1px); background-size: VAR VAR; }}
.grid::before {{ content: ""; position: absolute; left: 0; right: 0; top: 0; height: 1px; background: linear-gradient(90deg, transparent, rgba(240,196,96,.6), transparent); }}
.photo {{ position: absolute; inset: 0; background-size: cover; background-position: center; }}
.scrim {{ position: absolute; inset: 0; background: linear-gradient(0deg, rgba(36,4,10,.96) 0%, rgba(36,4,10,.72) 42%, rgba(36,4,10,.2) 75%), linear-gradient(90deg, rgba(36,4,10,.55), transparent 70%); }}
.seal {{ display: block; }}
.wm {{ position: absolute; opacity: .07; filter: grayscale(1) brightness(2.4); }}
.brand {{ display: flex; align-items: center; gap: .5em; }}
.brand b {{ display: block; font-family: J; font-weight: 800; letter-spacing: -.01em; line-height: 1.05; }}
.brand small {{ display: block; opacity: .85; }}
.rule {{ display: block; width: 3em; height: .22em; background: var(--gold); border-radius: 2px; }}
.chip {{ display: inline-block; padding: .3em .9em; border-radius: 999px; border: 1px solid rgba(224,173,28,.7); color: var(--gold); font-family: J; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }}
.chip.solid {{ background: var(--gold); color: var(--ebony); border-color: var(--gold); }}
.btn {{ display: inline-flex; align-items: center; gap: .5em; padding: .65em 1.4em; border-radius: 999px; background: var(--gold); color: var(--m950); font-family: J; font-weight: 800; }}
.btn.red {{ background: var(--r500); color: #fff; }}
.foot {{ display: flex; gap: 1.6em; flex-wrap: wrap; opacity: .92; }}
.gold {{ color: var(--gold); }}
"""

def page(w, h, body, css="", grid=48, print_size=None):
    pg = f"@page {{ size: {print_size}; margin: 0; }}" if print_size else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{BASE.replace('VAR', f'{grid}px')}{pg}
html, body {{ width: {w}px; height: {h}px; }} body {{ position: relative; }}{css}</style></head><body>{body}</body></html>"""

def img(rel): return f"{U}/{rel}"
SEAL = img("img/seal.png")
HERO = {"campus": img("img/hero/web/hero-01-campus-building.webp"), "vlab": img("img/hero/web/hero-02-virtual-lab.webp"),
        "grads": img("img/hero/web/hero-03-graduates-2024.webp"), "library": img("img/hero/web/hero-04-library.webp")}
SITE = lambda s: img(f"img/site/{s}.webp")

def brand(size=1, light=True, sub=True):
    return f'<div class="brand" style="font-size:{size}em"><img class="seal" src="{SEAL}" style="width:2.6em;height:2.6em"><span><b style="font-size:1.05em">St. Clare College</b>{"<small style=font-size:.6em>of Caloocan &middot; The School of Life Skills</small>" if sub else ""}</span></div>'

M = []   # (group, name, title, w, h, html, kinds)
def add(group, name, title, w, h, html, kinds=("png",)): M.append((group, name, title, w, h, html, kinds))

# ------------------------------------------------------------------ logos
def logo_sheet(bg, fg, dark):
    return page(1600, 1600, f'<div style="position:absolute;inset:0;background:{bg};display:grid;place-items:center"><img src="{SEAL}" style="width:1180px;height:auto"></div>')
add("01-logo", "seal-on-white", "Seal on white", 1600, 1600, logo_sheet("#fff", "", False))
add("01-logo", "seal-on-maroon", "Seal on maroon", 1600, 1600, page(1600, 1600, f'<div class="crimson" style="position:absolute;inset:0;display:grid;place-items:center"><img src="{SEAL}" style="width:1180px"></div>'))
def lockup(bg, dark):
    col = "#fff" if dark else "var(--m700)"; sub = "rgba(255,255,255,.8)" if dark else "var(--muted)"
    return page(2400, 900, f'''<div style="position:absolute;inset:0;background:{bg};display:flex;align-items:center;justify-content:center;gap:70px">
  <img src="{SEAL}" style="width:560px"><div><b class="h" style="display:block;font-size:170px;color:{col};line-height:1">St. Clare College</b>
  <span style="display:block;font-family:J;font-weight:700;font-size:76px;color:{col};margin-top:14px">of Caloocan</span>
  <span style="display:block;font-size:46px;color:{sub};margin-top:22px;letter-spacing:.14em;text-transform:uppercase">The School of Life Skills</span></div></div>''')
add("01-logo", "lockup-horizontal-light", "Horizontal lockup (light)", 2400, 900, lockup("#fff", False))
add("01-logo", "lockup-horizontal-dark", "Horizontal lockup (dark)", 2400, 900, lockup("var(--m900)", True))
add("01-logo", "lockup-stacked", "Stacked lockup", 1400, 1600, page(1400, 1600, f'''<div style="position:absolute;inset:0;background:#fff;display:grid;place-content:center;justify-items:center;text-align:center">
  <img src="{SEAL}" style="width:760px"><b class="h" style="display:block;font-size:120px;color:var(--m700);margin-top:50px">St. Clare College</b>
  <span style="display:block;font-family:J;font-weight:700;font-size:60px;color:var(--m700);margin-top:8px">of Caloocan</span>
  <span style="display:block;font-size:34px;color:var(--muted);margin-top:22px;letter-spacing:.16em;text-transform:uppercase">The School of Life Skills</span></div>'''))

# ------------------------------------------------------------------ social posts 1080x1440 (3:4)
def post(name, title, html_body, grid=40, photo=None):
    ph = f'<div class="photo" style="background-image:url({photo})"></div><div class="scrim"></div>' if photo else '<div class="grid"><i></i></div>'
    add("02-social-posts", name, title, 1080, 1440, page(1080, 1440, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden">{ph}
  <img class="wm" src="{SEAL}" style="width:760px;right:-200px;top:-180px">
  <div style="position:absolute;left:72px;top:64px;color:#fff">{brand(1.5)}</div>
  {html_body}
  <div style="position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;font-size:26px;color:rgba(255,255,255,.88);border-top:1px solid rgba(255,255,255,.2);padding-top:24px"><span>{WEB}</span><span>{PHONE}</span></div>
</div>''', grid=grid))

post("post-01-life-skills", "The School of Life Skills", f'''<div style="position:absolute;left:72px;right:72px;top:420px">
  <span class="rule" style="font-size:30px"></span><h1 style="font-size:150px;margin-top:40px">The School<br>of <span class="gold">Life Skills</span></h1>
  <p style="font-size:38px;line-height:1.45;margin-top:40px;max-width:900px;color:#f5e9eb">Nursery to College, on one campus in Caloocan City and online through St. Clare Online.</p>
  <span class="btn" style="font-size:36px;margin-top:50px">Enroll at St. Clare &rarr;</span></div>''', photo=HERO["campus"])
post("post-02-programmes", "Programmes", '''<div style="position:absolute;left:72px;right:72px;top:300px">
  <span class="chip" style="font-size:24px">Academics</span><h1 style="font-size:118px;margin-top:34px">Programmes for<br>every stage</h1>
  <div style="display:grid;gap:22px;margin-top:56px;font-size:36px">
   <div style="padding:30px 36px;border-radius:26px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16)"><b class="h gold" style="font-size:44px">College</b><br>BSHM &middot; BSBA &middot; BSCS &middot; BEEd &middot; BSEd &middot; BSTM &middot; AB PolSci</div>
   <div style="padding:30px 36px;border-radius:26px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16)"><b class="h gold" style="font-size:44px">Senior High School</b><br>ABM &middot; HUMSS &middot; Arts &amp; Design &middot; TVL-ICT &middot; TVL-HE</div>
   <div style="padding:30px 36px;border-radius:26px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16)"><b class="h gold" style="font-size:44px">Basic Education</b><br>Nursery to Grade 10</div></div></div>''')
post("post-03-virtual-lab", "Virtual Lab", '''<div style="position:absolute;left:72px;right:72px;bottom:190px">
  <span class="chip solid" style="font-size:24px">Virtual Lab</span><h1 style="font-size:132px;margin-top:34px">VR + AR<br>= <span class="gold">mixed reality</span></h1>
  <p style="font-size:36px;line-height:1.45;margin-top:34px;color:#f5e9eb">The Predator Thronos and the Mixed Reality facility by Acer, at St. Clare College.</p></div>''', photo=HERO["vlab"])
post("post-04-eboards", "E-boards in all 95 classrooms", '''<div style="position:absolute;left:72px;right:72px;top:330px">
  <b class="h gold" style="display:block;font-size:430px;line-height:.85;letter-spacing:-.05em">95</b>
  <h1 style="font-size:96px;margin-top:20px">classrooms,<br>every one with an <span style="white-space:nowrap">e-board</span></h1>
  <p style="font-size:36px;line-height:1.45;margin-top:36px;color:#f5e9eb;max-width:880px">The first college in the country to replace every blackboard with an e-board.</p></div>''')
post("post-05-since-1985", "Since 1985", '''<div style="position:absolute;left:72px;right:72px;top:330px">
  <span class="chip" style="font-size:24px">Founded 31 August 1985</span>
  <b class="h" style="display:block;font-size:330px;line-height:.9;margin-top:40px;color:transparent;-webkit-text-stroke:3px var(--gold)">1985</b>
  <h1 style="font-size:96px;margin-top:30px">Transforming education,<br>building our future</h1></div>''')
post("post-06-enroll", "How to enroll", '''<div style="position:absolute;left:72px;right:72px;top:300px">
  <span class="chip solid" style="font-size:24px">Admissions</span><h1 style="font-size:124px;margin-top:34px">Become a<br><span class="gold">Clarean</span></h1>
  <div style="display:grid;gap:18px;margin-top:50px;font-size:34px">
   <div style="display:flex;gap:26px;align-items:center"><b class="h gold" style="font-size:64px;width:90px">01</b>Pay the matriculation fee &middot; Cashier</div>
   <div style="display:flex;gap:26px;align-items:center"><b class="h gold" style="font-size:64px;width:90px">02</b>Fill up the registration form &middot; Lobby</div>
   <div style="display:flex;gap:26px;align-items:center"><b class="h gold" style="font-size:64px;width:90px">03</b>Register online for your schedule &middot; Library</div></div>
  <p style="font-size:30px;margin-top:44px;color:#dcc7cb">Bring photocopies of your requirements in a long brown envelope. Dates and fees: call (02) 8232-4483.</p></div>''')

# ------------------------------------------------------------------ stories 1080x1920
def story(name, title, body, photo=None):
    ph = f'<div class="photo" style="background-image:url({photo})"></div><div class="scrim"></div>' if photo else '<div class="grid" style="height:40%"><i></i></div>'
    add("03-stories", name, title, 1080, 1920, page(1080, 1920, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden">{ph}
  <div style="position:absolute;left:80px;top:250px">{brand(1.55)}</div>{body}
  <div style="position:absolute;left:80px;right:80px;bottom:300px;text-align:center"><span class="btn" style="font-size:40px">stclareonline.com</span></div></div>''', grid=44))
story("story-01-programmes", "Story: programmes", '''<div style="position:absolute;left:80px;right:80px;top:560px"><span class="rule" style="font-size:34px"></span>
  <h1 style="font-size:150px;margin-top:44px">Nursery<br>to <span class="gold">College</span></h1><p style="font-size:44px;line-height:1.4;margin-top:44px;color:#f5e9eb">Basic Education, Senior High School and eight college degrees, on campus, online or blended.</p></div>''')
story("story-02-graduates", "Story: Stars of 2024", '''<div style="position:absolute;left:80px;right:80px;top:1020px"><span class="chip solid" style="font-size:28px">38th Commencement</span>
  <h1 style="font-size:140px;margin-top:40px">The Stars<br>of <span class="gold">2024</span></h1></div>''', HERO["grads"])

# ------------------------------------------------------------------ covers / banners
add("04-covers-banners", "facebook-cover", "Facebook cover (1702x630)", 1702, 630, page(1702, 630, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden">
  <div class="photo" style="left:auto;width:58%;background-image:url({HERO['campus']})"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,var(--m950) 34%,rgba(36,4,10,.75) 55%,rgba(36,4,10,.1) 85%)"></div><div class="grid" style="width:60%"><i></i></div>
  <div style="position:absolute;left:330px;top:150px"><span class="rule" style="font-size:22px"></span><h1 style="font-size:92px;margin-top:26px">The School<br>of <span class="gold">Life Skills</span></h1>
  <p style="font-size:28px;margin-top:22px;color:#f5e9eb">Nursery to College &middot; Caloocan City &middot; Full online or blended</p></div></div>''', grid=36))
add("04-covers-banners", "youtube-banner", "YouTube channel banner (2560x1440)", 2560, 1440, page(2560, 1440, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden"><div class="grid"><i></i></div>
  <img class="wm" src="{SEAL}" style="width:1100px;right:-200px;top:-260px">
  <div style="position:absolute;left:507px;right:507px;top:509px;height:423px;display:flex;align-items:center;justify-content:center;gap:56px">
   <img src="{SEAL}" style="width:300px"><div><h1 style="font-size:110px">St. Clare College</h1><p style="font-size:40px;margin-top:16px;color:#f5e9eb">Commencement &middot; Broadcasts &middot; Webinars &middot; Virtual Lab</p></div></div></div>''', grid=60))
add("04-covers-banners", "web-share-1200x630", "Link preview / web banner (1200x630)", 1200, 630, page(1200, 630, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden">
  <div class="photo" style="background-image:url({HERO['library']})"></div><div class="scrim"></div>
  <div style="position:absolute;left:64px;top:56px">{brand(1.1)}</div>
  <div style="position:absolute;left:64px;bottom:70px"><h1 style="font-size:82px">Programmes for<br>every stage</h1><p style="font-size:26px;margin-top:16px;color:#f5e9eb">stclareonline.com</p></div></div>'''))
add("04-covers-banners", "tarpaulin-6x3ft", "Tarpaulin 6 x 3 ft (3600x1800)", 3600, 1800, page(3600, 1800, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden">
  <div class="photo" style="left:auto;width:50%;background-image:url({HERO['grads']})"></div>
  <div style="position:absolute;inset:0;background:linear-gradient(90deg,var(--m950) 40%,rgba(36,4,10,.6) 60%,transparent)"></div><div class="grid" style="width:56%"><i></i></div>
  <div style="position:absolute;left:180px;top:170px">{brand(3.2)}</div>
  <div style="position:absolute;left:180px;top:620px"><span class="chip solid" style="font-size:56px">Enrollment</span>
   <h1 style="font-size:260px;margin-top:60px">Become a<br><span class="gold">Clarean</span></h1>
   <p style="font-size:78px;margin-top:60px;color:#f5e9eb">College &middot; Senior High School &middot; Basic Education</p></div>
  <div style="position:absolute;left:0;right:0;bottom:0;padding:60px 180px;background:var(--ebony);display:flex;gap:120px;font-size:64px;font-family:J;font-weight:700"><span class="gold">{PHONE}</span><span>{WEB}</span><span>Zabarte Road, Caloocan City</span></div></div>''', grid=90))
add("04-covers-banners", "presentation-title-16x9", "Presentation title slide (1920x1080)", 1920, 1080, page(1920, 1080, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden"><div class="grid"><i></i></div>
  <img class="wm" src="{SEAL}" style="width:900px;right:-160px;top:-160px"><div style="position:absolute;left:140px;top:110px">{brand(1.6)}</div>
  <div style="position:absolute;left:140px;top:400px"><span class="rule" style="font-size:28px"></span><h1 style="font-size:130px;margin-top:36px">Presentation title</h1>
  <p style="font-size:42px;margin-top:28px;color:#f5e9eb">Subtitle or speaker &middot; Date</p></div></div>''', grid=54))
add("04-covers-banners", "virtual-background", "Zoom / Meet virtual background (1920x1080)", 1920, 1080, page(1920, 1080, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden"><div class="grid" style="height:40%"><i></i></div>
  <div style="position:absolute;right:90px;top:70px">{brand(1.3)}</div><img class="wm" src="{SEAL}" style="width:700px;left:-180px;bottom:-200px"></div>''', grid=54))

# ------------------------------------------------------------------ print (PDF + PNG)
A4 = (1240, 1754)   # px at 150 dpi
add("05-print", "poster-a4-enrollment", "Enrollment poster (A4)", *A4, page(*A4, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden">
  <div class="photo" style="height:52%;background-image:url({HERO['campus']})"></div><div style="position:absolute;left:0;right:0;top:0;height:52%;background:linear-gradient(0deg,var(--m950),transparent 60%)"></div>
  <div style="position:absolute;left:90px;top:80px">{brand(1.75)}</div>
  <div style="position:absolute;left:90px;right:90px;top:800px"><span class="chip solid" style="font-size:26px">Admissions</span><h1 style="font-size:150px;margin-top:30px">Become a <span class="gold">Clarean</span></h1>
   <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:50px">
    {"".join(f'<div style="padding:30px;border-radius:24px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16)"><b class="h gold" style="font-size:60px">{n}</b><p style="font-size:30px;margin-top:10px;line-height:1.35">{t}</p><p style="font-size:24px;margin-top:8px;color:#dcc7cb">{wh}</p></div>' for n,t,wh in [("01","Pay the matriculation fee","Cashier"),("02","Fill up the registration form","Lobby"),("03","Register online for your schedule","Library, 3rd floor")])}</div>
   <p style="font-size:30px;margin-top:40px;color:#f5e9eb">Bring photocopies of your requirements in a long brown envelope. You can also enroll online through the IMS.</p></div>
  <div style="position:absolute;left:0;right:0;bottom:0;padding:40px 90px;background:var(--ebony);display:flex;justify-content:space-between;font-family:J;font-weight:700;font-size:30px"><span class="gold">{PHONE}</span><span>{EMAIL}</span><span>{WEB}</span></div></div>''', print_size="A4"), ("png", "pdf"))
add("05-print", "flyer-a4-programmes", "Programmes flyer (A4)", *A4, page(*A4, f'''<div style="position:absolute;inset:0;background:#fff;color:var(--ink)">
  <div class="crimson" style="position:absolute;left:0;right:0;top:0;height:560px;overflow:hidden"><div class="grid"><i></i></div><div style="position:absolute;left:90px;top:80px">{brand(1.7)}</div>
   <h1 style="position:absolute;left:90px;top:300px;font-size:116px">Programmes for every stage</h1></div>
  <div style="position:absolute;left:90px;right:90px;top:640px;display:grid;gap:40px">
   {"".join(f'<div style="display:grid;grid-template-columns:300px 1fr;gap:36px;align-items:start;padding-bottom:36px;border-bottom:2px solid #ebe2e3"><div><span style="display:block;width:60px;height:6px;background:var(--r500);border-radius:3px"></span><b class="h" style="display:block;font-size:52px;color:var(--m700);margin-top:22px">{t}</b><span style="font-size:24px;color:var(--muted)">{s}</span></div><div style="font-size:28px;line-height:1.7;color:var(--ink)">{l}</div></div>' for t,s,l in [("College","Eight bachelor's degrees","BS Hospitality Management<br>BS Business Administration<br>BS Computer Science<br>Bachelor of Elementary Education<br>BSEd English &middot; BSEd Mathematics<br>BS Tourism Management<br>AB Political Science"),("Senior High School","Grades 11 and 12","Academic Track: ABM and HUMSS<br>Arts &amp; Design<br>TVL - Information, Communication Technology<br>TVL - Home Economics"),("Basic Education","Nursery to Grade 10","Nursery &amp; Kindergarten<br>Elementary, Grade 1 to 6<br>Junior High School, Grade 7 to 10")])}</div>
  <div style="position:absolute;left:0;right:0;bottom:0;padding:40px 90px;background:var(--ebony);color:#fff;display:flex;justify-content:space-between;font-family:J;font-weight:700;font-size:28px"><span class="gold">{PHONE}</span><span>Full online or blended</span><span>{WEB}</span></div></div>''', print_size="A4"), ("png", "pdf"))
add("05-print", "letterhead-a4", "Letterhead (A4)", *A4, page(*A4, f'''<div style="position:absolute;inset:0;background:#fff;color:var(--ink)">
  <div style="position:absolute;left:100px;right:100px;top:80px;display:flex;justify-content:space-between;align-items:center;padding-bottom:30px;border-bottom:4px solid var(--m700)">
   <div class="brand" style="font-size:1.7em;color:var(--m700)"><img src="{SEAL}" style="width:2.7em"><span><b>St. Clare College</b><small style="font-size:.6em;color:var(--muted)">of Caloocan &middot; The School of Life Skills</small></span></div>
   <div style="text-align:right;font-size:20px;line-height:1.6;color:var(--muted)">{ADDR.replace(", Caloocan", "<br>Caloocan")}<br>{PHONE} &middot; {EMAIL}</div></div>
  <div style="position:absolute;left:100px;right:100px;top:330px;font-size:22px;line-height:1.8;color:#b8aeb0">Date<br><br>Recipient name<br>Address<br><br>Dear ...,<br><br>Letter text starts here.</div>
  <img src="{SEAL}" style="position:absolute;right:-160px;bottom:-160px;width:760px;opacity:.05">
  <div style="position:absolute;left:0;right:0;bottom:0;height:24px;background:linear-gradient(90deg,var(--m950),var(--m700) 60%,var(--gold))"></div></div>''', print_size="A4"), ("png", "pdf"))
add("05-print", "certificate-a4-landscape", "Certificate (A4 landscape)", 1754, 1240, page(1754, 1240, f'''<div style="position:absolute;inset:0;background:#fffdf8;color:var(--ink)">
  <div style="position:absolute;inset:40px;border:3px solid var(--gold);border-radius:8px"></div><div style="position:absolute;inset:58px;border:1px solid rgba(122,12,30,.35);border-radius:4px"></div>
  <img src="{SEAL}" style="position:absolute;left:50%;top:-80px;transform:translateX(-50%);width:900px;opacity:.05">
  <div style="position:absolute;left:0;right:0;top:120px;text-align:center"><img src="{SEAL}" style="width:200px"><p style="font-family:J;font-weight:800;font-size:40px;color:var(--m700);margin-top:18px">St. Clare College of Caloocan</p>
   <p style="font-size:22px;letter-spacing:.3em;text-transform:uppercase;color:var(--muted);margin-top:8px">The School of Life Skills</p>
   <h1 style="font-size:108px;color:var(--ink);margin-top:60px">Certificate of Recognition</h1><p style="font-size:28px;color:var(--muted);margin-top:30px">is proudly presented to</p>
   <p style="font-family:J;font-weight:800;font-size:76px;color:var(--m700);margin-top:24px;display:inline-block;padding:0 60px 12px;border-bottom:3px solid var(--gold)">Recipient Name</p>
   <p style="font-size:26px;color:var(--muted);margin-top:30px">for ... &middot; Given this ... day of ..., ... at St. Clare College, Caloocan City.</p></div>
  <div style="position:absolute;left:260px;right:260px;bottom:130px;display:flex;justify-content:space-between;text-align:center;font-size:22px;color:var(--muted)">
   <div style="width:420px;border-top:2px solid var(--ink);padding-top:12px">Name<br>Title</div><div style="width:420px;border-top:2px solid var(--ink);padding-top:12px">Name<br>Title</div></div></div>''', print_size="A4 landscape"), ("png", "pdf"))
BC = (1050, 600)   # 3.5 x 2 in at 300 dpi
add("05-print", "business-card-front", "Business card front (3.5x2 in)", *BC, page(*BC, f'''<div class="crimson" style="position:absolute;inset:0;overflow:hidden"><div class="grid" style="height:50%"><i></i></div>
  <img class="wm" src="{SEAL}" style="width:520px;right:-140px;top:-140px"><div style="position:absolute;left:70px;top:70px">{brand(1.25)}</div>
  <div style="position:absolute;left:70px;bottom:70px"><b class="h" style="font-size:52px">Full Name</b><p style="font-size:26px;color:var(--gold);margin-top:8px;font-family:J;font-weight:700">Position / Office</p></div></div>''', grid=30, print_size="3.5in 2in"), ("png", "pdf"))
add("05-print", "business-card-back", "Business card back (3.5x2 in)", *BC, page(*BC, f'''<div style="position:absolute;inset:0;background:#fff;color:var(--ink)">
  <div style="position:absolute;left:0;top:0;bottom:0;width:22px;background:linear-gradient(180deg,var(--m700),var(--gold))"></div>
  <div style="position:absolute;left:80px;top:80px;display:grid;gap:22px;font-size:28px">
   <div><b style="color:var(--c600);font-family:J">Phone</b>&nbsp; {PHONE}</div><div><b style="color:var(--c600);font-family:J">Email</b>&nbsp; {EMAIL}</div>
   <div><b style="color:var(--c600);font-family:J">Web</b>&nbsp; {WEB}</div><div style="font-size:24px;color:var(--muted);line-height:1.4;max-width:620px">{ADDR}</div></div>
  <img src="{SEAL}" style="position:absolute;right:60px;bottom:60px;width:190px"></div>''', print_size="3.5in 2in"), ("png", "pdf"))
add("05-print", "id-card-portrait", "ID card (CR80 portrait)", 638, 1012, page(638, 1012, f'''<div style="position:absolute;inset:0;background:#fff;color:var(--ink);overflow:hidden">
  <div class="crimson" style="position:absolute;left:0;right:0;top:0;height:380px;overflow:hidden"><div class="grid"><i></i></div>
   <div style="position:absolute;left:0;right:0;top:44px;text-align:center"><img src="{SEAL}" style="width:120px"><p style="font-family:J;font-weight:800;font-size:30px;margin-top:10px">St. Clare College</p><p style="font-size:16px;opacity:.85">of Caloocan</p></div></div>
  <div style="position:absolute;left:50%;top:300px;transform:translateX(-50%);width:250px;height:300px;border-radius:20px;background:#f4eded;border:6px solid #fff;box-shadow:0 10px 30px rgba(0,0,0,.2);display:grid;place-items:center;color:#b8aeb0;font-size:22px">Photo</div>
  <div style="position:absolute;left:0;right:0;top:640px;text-align:center"><b class="h" style="font-size:44px">Full Name</b><p style="font-size:22px;color:var(--c600);font-family:J;font-weight:700;margin-top:8px">Programme / Year level</p><p style="font-size:20px;color:var(--muted);margin-top:22px">ID No. 0000-0000</p></div>
  <div style="position:absolute;left:0;right:0;bottom:0;height:70px;background:var(--ebony);color:var(--gold);display:grid;place-items:center;font-family:J;font-weight:700;font-size:20px;letter-spacing:.2em">STUDENT</div></div>''', grid=28))

# ------------------------------------------------------------------ email signature (HTML file, not rendered)
SIG = f'''<table cellpadding="0" cellspacing="0" style="font-family:Arial,sans-serif;color:#1d1416;font-size:13px;line-height:1.5">
<tr><td style="padding-right:16px;border-right:3px solid #7a0c1e;vertical-align:top"><img src="https://technextsg.github.io/st-clare-college-website/img/seal-256.webp" width="72" height="72" alt="St. Clare College seal"></td>
<td style="padding-left:16px;vertical-align:top"><b style="font-size:15px">Full Name</b><br><span style="color:#a6192e;font-weight:bold">Position / Office</span><br>
St. Clare College of Caloocan &middot; The School of Life Skills<br>{PHONE} &middot; <a href="mailto:{EMAIL}" style="color:#a6192e">{EMAIL}</a><br>
<span style="color:#675a5e">{ADDR}</span></td></tr></table>'''

def render(only=None):
    os.makedirs(WORK, exist_ok=True); os.makedirs(THUMBS, exist_ok=True)
    meta = []
    for group, name, title, w, h, html, kinds in M:
        if only and name not in only: continue
        gdir = os.path.join(OUT, group); os.makedirs(gdir, exist_ok=True)
        tpl = os.path.join(WORK, name + ".html"); open(tpl, "w", encoding="utf-8").write(html)
        url = "file:///" + tpl.replace("\\", "/")
        ud = tempfile.mkdtemp(prefix="bk")
        try:
            png = os.path.join(gdir, name + ".png")
            subprocess.run([CH, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--allow-file-access-from-files", f"--user-data-dir={ud}", f"--window-size={w},{h}",
                            "--force-device-scale-factor=1", "--virtual-time-budget=3000", "--default-background-color=00000000", f"--screenshot={png}", url], timeout=120, capture_output=True)
            if "pdf" in kinds:
                pdf = os.path.join(gdir, name + ".pdf")
                subprocess.run([CH, "--headless=new", "--disable-gpu", "--allow-file-access-from-files", f"--user-data-dir={ud}", "--no-pdf-header-footer",
                                "--virtual-time-budget=3000", f"--print-to-pdf={pdf}", url], timeout=120, capture_output=True)
        finally:
            shutil.rmtree(ud, ignore_errors=True)
        im = Image.open(png); im.convert("RGB").thumbnail((900, 900)) if False else None
        t = Image.open(png).convert("RGBA"); t.thumbnail((720, 720), Image.LANCZOS)
        bg = Image.new("RGBA", t.size, (255, 255, 255, 255)); bg.alpha_composite(t); bg.convert("RGB").save(os.path.join(THUMBS, name + ".jpg"), quality=82)
        files = [f"files/{group}/{name}.{k}" for k in kinds]
        meta.append({"group": group, "name": name, "title": title, "w": w, "h": h, "files": files, "thumb": f"thumbs/{name}.jpg",
                     "sizes": {k: os.path.getsize(os.path.join(gdir, f"{name}.{k}")) for k in kinds}})
        print("rendered", name)
    sigdir = os.path.join(OUT, "06-email"); os.makedirs(sigdir, exist_ok=True)
    open(os.path.join(sigdir, "email-signature.html"), "w", encoding="utf-8").write("<!doctype html><meta charset=utf-8><title>Email signature</title><body style='padding:30px'>" + SIG + "</body>")
    if not only:
        json.dump(meta, open(os.path.join(HERE, "materials.json"), "w", encoding="utf-8"), indent=1)
    return meta

if __name__ == "__main__":
    render(sys.argv[1:] or None)
