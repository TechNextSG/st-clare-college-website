# DESIGN: St. Clare College, "Crimson University" (v5, 19 Oct 2026)

Supersedes the navy "Collegiate" system below. Source of truth: assets/univ.css.

- **Palette (red tonal scale):** maroon-950 #24040a (footer), 900 #3d0610 (hero ground), 800 #5c0a17 (dark bands), 700 #7a0c1e (primary), crimson-600 #a6192e (links), red-500 #c8102e (actions), rose-100 #f6e1e4 / rose-50 #fcf3f4 (tints), seal gold #e0ad1c (accent only), warm white #f8f5f5.
- **Logo:** the ORIGINAL St. Clare College of Caloocan seal, restored HD (img/seal.svg: AI-upscaled original emblem + vector ring and lettering). Never redraw or recolour it.
- **Type:** Plus Jakarta Sans 800 headings (tight tracking), Inter body. No eyebrows, no gradient text.
- **Masthead:** transparent over every hero (gradient scrim), turns solid white on scroll, hides on scroll-down, returns on scroll-up.
- **Heroes:** one per header page: Home slideshow (Ken Burns + progress dots), About split frames + seal + 1985 counter, Academics expanding level panels, Admissions photo + "Enrollment at a glance" card, Campus Life photo mosaic, News featured story + headlines, Contact photo + four action cards. Student-service pages use the compact crimson banner + sticky sub-nav.
- **Buttons:** pill, fill-wipe on hover, sheen sweep, arrow slide, ripple on press, magnetic follow on fine pointers, scale .97 on active.
- **Motion:** GSAP 3.12.5 + ScrollTrigger (cdnjs): masked line-rise headlines, batched section reveals, image clip-reveals, counters, hero parallax. IntersectionObserver fallback; prefers-reduced-motion shows everything static.
- **Footer:** compact: brand + 3 short link columns + one bottom line.

---

---
name: St. Clare College of Caloocan
description: Collegiate - a corporate college site in navy and white with a gold hairline accent, real campus photography and quiet motion.
colors:
  navy: "#0b2265"
  navy-2: "#13308a"
  navy-3: "#061642"
  gold: "#e2b417"
  gold-hover: "#f0c62a"
  gold-soft: "#fbf3d5"
  gold-line: "#efdfa0"
  gold-ink: "#7a5d00"
  ink: "#0f172a"
  text: "#1f2937"
  muted: "#566074"
  line: "#e2e6ee"
  bg: "#ffffff"
  bg-2: "#f4f6fa"
  on-navy: "#e8ecf8"
  on-navy-muted: "#b9c3e3"
typography:
  display:
    fontFamily: "Plus Jakarta Sans, Jakarta Fallback, system-ui, sans-serif"
    fontSize: "clamp(2.3rem, 4.8vw, 3.9rem)"
    fontWeight: 800
    lineHeight: 1.06
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Plus Jakarta Sans, Jakarta Fallback, system-ui, sans-serif"
    fontSize: "clamp(1.75rem, 3vw, 2.5rem)"
    fontWeight: 800
    lineHeight: 1.12
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Plus Jakarta Sans, Jakarta Fallback, system-ui, sans-serif"
    fontSize: "clamp(1.12rem, 1.5vw, 1.3rem)"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.02em"
  numeral:
    fontFamily: "Plus Jakarta Sans, Jakarta Fallback, system-ui, sans-serif"
    fontSize: "1.7rem"
    fontWeight: 800
    lineHeight: 1.1
  lede:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.06rem, 1.3vw, 1.2rem)"
    fontWeight: 400
    lineHeight: 1.65
  body:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.65
  ui:
    fontFamily: "Plus Jakarta Sans, Jakarta Fallback, system-ui, sans-serif"
    fontSize: "0.98rem"
    fontWeight: 700
    lineHeight: 1.2
  label:
    fontFamily: "Inter, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 700
    letterSpacing: "0.06em"
rounded:
  hairline: "3px"
  sm: "6px"
  md: "8px"
  lg: "10px"
  xl: "12px"
  2xl: "16px"
  pill: "999px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "26px"
  xl: "40px"
  gutter: "clamp(16px, 4vw, 40px)"
  section: "clamp(64px, 8vw, 112px)"
  wrap: "1200px"
components:
  button-primary:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.bg}"
    typography: "{typography.ui}"
    rounded: "{rounded.md}"
    padding: "0 22px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.navy-2}"
    textColor: "{colors.bg}"
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.ink}"
    typography: "{typography.ui}"
    rounded: "{rounded.md}"
    padding: "0 22px"
    height: "48px"
  button-gold-hover:
    backgroundColor: "{colors.gold-hover}"
    textColor: "{colors.ink}"
  button-line:
    backgroundColor: "transparent"
    textColor: "{colors.navy}"
    typography: "{typography.ui}"
    rounded: "{rounded.md}"
    padding: "0 22px"
    height: "48px"
  button-line-hover:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.bg}"
  input:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "12px 14px"
    height: "48px"
  chip:
    backgroundColor: "{colors.bg-2}"
    textColor: "{colors.navy}"
    rounded: "{rounded.pill}"
    padding: "5px 12px"
  chip-dated:
    backgroundColor: "{colors.gold-soft}"
    textColor: "{colors.gold-ink}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  panel:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.text}"
    rounded: "{rounded.2xl}"
    padding: "26px"
  hero-card:
    backgroundColor: "{colors.bg}"
    textColor: "{colors.navy}"
    rounded: "{rounded.2xl}"
    padding: "clamp(28px, 4vw, 48px)"
  note-callout:
    backgroundColor: "{colors.gold-soft}"
    textColor: "{colors.text}"
    rounded: "{rounded.lg}"
    padding: "18px 22px"
  page-header:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.bg}"
    padding: "clamp(48px, 6vw, 84px) 0"
  footer:
    backgroundColor: "{colors.navy-3}"
    textColor: "{colors.on-navy-muted}"
    padding: "64px 0 44px"
---

# Design System: St. Clare College of Caloocan

## Overview

**Creative North Star: "The Registrar's Letterhead"**

Collegiate is the visual language of an established Philippine college presenting itself to families: navy and white like an official letterhead, with gold used the way a seal uses foil, as a thin line and never a field. The tone is corporate-institutional (the user's reference points are Ateneo, De La Salle and Mapua): clean, legible, calm, and specific to St. Clare through its vector seal (`img/seal.svg`) and real campus photography (the building, commencement, the Virtual Lab). Nothing is playful, illustrated or childlike.

Density is generous. Sections breathe on a white / cool-grey alternation, content sits in a 1200px column, and information is organised the way a prospectus is: programme lists with code + name, numbered enrollment steps, fact grids, accordions, file lists. Hierarchy comes from Plus Jakarta Sans at heavy weights in ink or navy against Inter body text in slate, not from colour or decoration.

Motion is quiet: content rises 18px and fades in once as it enters the viewport, the hero photograph settles from 104% to 100% over six seconds, and hovers nudge by 1-3px. Content is fully visible without JavaScript and all motion collapses under reduced-motion.

**Key Characteristics:**
- Navy and white carry the page; gold appears as hairlines, underlines, dots and one CTA per navy band.
- A 48 x 3px gold rule above every section heading is the system's signature mark.
- Real photography in rounded frames with navy-tinted overlays; the seal as a 7%-opacity watermark on navy page headers.
- Plus Jakarta Sans 700-800 for headings and UI, Inter 400-600 for reading.
- Flat surfaces bordered by a cool hairline; soft ink-tinted shadows only on photos, the hero card, forms and hover states.
- Quiet reveal motion on one easing curve, cubic-bezier(.2, .8, .2, 1).

## Colors

A restrained institutional palette: deep academic navy and white, a cool grey ground, and a single warm gold accent used in thin measure.

### Primary
- **Academic Navy** (navy): The institution colour. Primary buttons, the closing `sec navy` CTA band, inner page headers, heading text inside the hero card, programme codes, numerals, accordion and checklist marks, the theme-color meta.
- **Bright Navy** (navy-2): The interactive navy. Links, button and nav hover, the 3px focus outline, input focus border, small uppercase labels, quick-access icons, card hover borders.
- **Midnight Navy** (navy-3): The deepest ground. Utility bar, footer, hero backdrop, and (as `rgba(6, 22, 66, .35 / .82 / .88)`) every photo overlay and caption strip.

### Secondary
- **Seal Gold** (gold): The accent. Section rules, active-nav and active-tab underlines, the hero card's 4px top edge, timeline dots, news-thumb monogram bars, focus outline and link hover on navy, the skip link, and the `btn gold` CTA.
- **Bright Gold** (gold-hover): Hover state of the gold button only.
- **Gold Wash** (gold-soft): Text selection, the "What happens next" callout ground, dated-offer pill ground.
- **Gold Hairline** (gold-line): Border of the gold-wash callout.
- **Old Gold Ink** (gold-ink): Text on the dated-offer pill (legible gold on Gold Wash).

### Neutral
- **Ink** (ink): Headings, labels, form values, strong text.
- **Slate Text** (text): Body copy.
- **Muted Slate** (muted): Ledes, sub-lines, card body, captions, meta, inactive tabs.
- **Cool Hairline** (line): Every border and divider: header bottom, list rows, card outlines, inputs, accordion rows, the timeline spine.
- **White** (bg): Page ground, cards, header (at 97% opacity), hero card, form.
- **Cool Grey** (bg-2): Alternate section ground (`sec alt`), chips, nav/list hover fill, file-type badges, notebox, photo placeholder.
- **On-Navy** (on-navy): Body text, ledes and links on navy and midnight grounds.
- **On-Navy Muted** (on-navy-muted): Secondary text on navy: utility bar, footer copy, breadcrumbs, note lines.
- On-navy translucent whites are fixed tints, not tokens: `rgba(255,255,255,.55)` line-button border on navy, `.08` social-button ground, `.12` footer divider.

### Named Rules
**The Foil Rule.** Gold is a line, a dot or a single button, never a section ground or a large fill. If gold covers more than a CTA's worth of area on a screen, it has stopped being an accent.

**The Two Navies Rule.** Academic Navy states the institution; Bright Navy means "you can act here". Keep links, hovers and focus on Bright Navy so interactivity reads consistently.

**The Ground Alternation Rule.** Sections alternate white and Cool Grey, with one full navy band per page (the closing CTA). Navy is otherwise reserved for the page header, the utility bar and the footer.

## Typography

**Display Font:** Plus Jakarta Sans (self-hosted `fonts/jakarta.woff2`, weights 500-800, with a size-adjusted Arial fallback "Jakarta Fallback")
**Body Font:** Inter (self-hosted `fonts/inter.woff2`, weights 400-700, with system-ui)

**Character:** TechNext's pairing: a confident geometric grotesk at 700-800 for headings and every interactive label, over a neutral, highly legible Inter for reading. Tight negative tracking on headings, balanced wrapping, no italics, no serif.

### Hierarchy
- **Display** (800, clamp(2.3rem, 4.8vw, 3.9rem), 1.06): Page H1 only: hero card and inner page headers.
- **Headline** (800, clamp(1.75rem, 3vw, 2.5rem), 1.12): Section H2s, always preceded by the gold rule. CTA headings cap at 22ch.
- **Title** (700, clamp(1.12rem, 1.5vw, 1.3rem), 1.3): Card, step, post, portal and timeline titles. Programme column titles step up to 1.35rem.
- **Numeral** (800, 1.7rem, 1.1, navy): Fact figures; the same face at 1.1-1.5rem for programme codes, years, event dates, track tags and portal acronyms.
- **Lede** (400, clamp(1.06rem, 1.3vw, 1.2rem), muted, max 60ch): The one-sentence deck under H1/H2.
- **Body** (400, 1.0625rem / 17px, 1.65): Reading text; FAQ answers and accordion bodies cap at 68ch, timeline text at 62ch. Card copy steps down to .92-.95rem.
- **UI** (Plus Jakarta Sans 600-700, .9-1.02rem): Buttons (700, .98rem), nav links (600, .95rem), tabs, FAQ summaries, "more" links.
- **Label** (Inter 700, .78-.8rem, letter-spacing .05-.06em, uppercase, Bright Navy or muted): Metadata only: post category and date, event weekday, contact field names, step location.

### Named Rules
**The Heavy Head Rule.** Headings are always Plus Jakarta Sans at 700 or 800 in ink, navy or white; hierarchy comes from size and weight, never from colour washes or decoration.

**The Metadata-Only Caps Rule.** Uppercase tracked labels describe a fact about the item (date, category, place); they never introduce or tease a heading.

## Layout

Single centred column: `width: min(1200px, 100% - 2 * gutter)` with a fluid gutter of clamp(16px, 4vw, 40px). Sections pad clamp(64px, 8vw, 112px) top and bottom. A section opens with a section head: a two-column grid (heading left, lede right, bottom-aligned) that collapses to one column below 860px, or a single 760px column (`solo`).

Content grids are explicit and few: three-up (programme levels, steps, news, panels), two-up (split photo + text, facts, forms), four-up (quick-access bar). They step to two columns at 900px and one column at 600-640px. Gaps are fluid, clamp(16-20px, 2.4-3vw, 28-36px). The header is sticky at 80px under a 40px utility bar; below 1080px the nav becomes a full-screen white sheet with 1.3rem links. Touch targets are at least 44px everywhere (buttons 48px, small buttons 42px).

Rhythm: 8 / 12 / 16 / 26 / 40px for internal gaps and padding; 16px and 28px block-spacing utilities.

## Elevation & Depth

Flat by default and hairline-separated, with soft ink-tinted shadows (always `rgba(15, 23, 42, ...)`) reserved for photographic and floating surfaces.

### Shadow Vocabulary
- **Soft** (`box-shadow: 0 1px 2px rgba(15,23,42,.06), 0 8px 24px -12px rgba(15,23,42,.18)`): Photos, the contact form, panels on Cool Grey sections, and card/portal hover.
- **Lifted** (`box-shadow: 0 2px 4px rgba(15,23,42,.06), 0 24px 48px -24px rgba(15,23,42,.28)`): The hero card and page-header photo.
- **Header scrolled** (`box-shadow: 0 6px 20px -12px rgba(15,23,42,.25)`): Appears on the sticky header after 10px of scroll.
- **Focus glow** (`box-shadow: 0 0 0 4px rgba(19,48,138,.14)`): Input focus, with a Bright Navy border.
- **Ground ring** (`box-shadow: 0 0 0 4-5px <section ground>`): Cuts step numbers and timeline dots out of the line they sit on.

### Named Rules
**The Flat-At-Rest Rule.** Cards on white sit on a 1px Cool Hairline with no shadow; a shadow appears only for photographs, floating cards, or as a hover response (with a 2px lift).

## Shapes

Gently rounded, never pill-shaped except for chips. The radius scale: 3px (focus outline; rule ends at 2px), 6px (nav link hover, file badges, skip link), 8px (buttons, inputs, menu button, social buttons), 10px (news thumbnails, callouts, notebox), 12px (portal acronym tiles), 16px (cards, photos, hero card, banner, form, map), 999px (chips and dated pills), and 50% circles (step numbers, timeline dots, checklist marks, accordion toggles).

Borders are 1px Cool Hairline for containers and rows, 1.5px for interactive outlines (buttons, inputs, menu button, accordion toggle). Accent edges are gold or navy bars: the 48 x 3px section rule, a 4px gold top edge on the hero card, 3px navy top borders on programme columns, 2-3px gold underlines for current nav and selected tab. Photos are clipped to 16px and cropped with `object-fit: cover` at 4:3, 16:9 or 16:10. Under 700px the hero card goes square-cornered and full-bleed.

## Components

### Buttons
Confident and plain: solid blocks in Plus Jakarta Sans 700.
- **Shape:** gently rounded (8px), 48px tall, 22px side padding, 1.5px border; optional 18px trailing arrow icon.
- **Primary:** Academic Navy with white text. Hover: Bright Navy, 1px lift, arrow nudges 3px right.
- **Gold:** Seal Gold with ink text; the enrollment action on the navy CTA band. Hover: Bright Gold.
- **Line:** transparent with navy text and navy border; hover fills navy. On navy grounds the border is 55% white and hover fills white with navy text.
- **Small:** 42px tall, 16px padding, .9rem.
- **More link:** Bright Navy UI text with a drawn chevron that nudges 3px on hover; gold on navy.

### Chips
- **Style:** Cool Grey ground, navy text, .8rem 600, pill radius, 5px 12px. Used for course outcomes in the programme accordion.
- **Dated pill:** Gold Wash ground, Old Gold Ink text, .78rem 700; marks offers tied to a past school year.

### Cards / Containers
- **Panel:** white, 1px Cool Hairline, 16px radius, 26px padding; muted body at .95rem. On Cool Grey sections the border drops and the Soft shadow takes over. As a link: hover border Bright Navy, Soft shadow, 2px lift.
- **Step card:** panel with a 40px navy numbered disc overlapping the top edge, a Bright Navy uppercase location label, and a muted bullet list.
- **Hero card:** white, 16px radius, Lifted shadow, 4px gold top edge, max 680px, floated over the bottom of a full-bleed campus photograph tinted 35% Midnight Navy.
- **Photo frame:** 16px radius, Soft shadow, 4:3 crop, slow 3% zoom on hover, optional caption strip in 82% Midnight Navy.
- **Callout ("What happens next"):** Gold Wash ground, Gold Hairline border, 10px radius. **Notebox:** Cool Grey, 10px radius, muted text.

### Inputs / Fields
- **Style:** white, 1.5px Cool Hairline border, 8px radius, 48px min height (textarea 130px), 12px 14px padding, 1rem Inter in ink. Labels 600 .92rem ink above; optional hint in muted.
- **Focus:** border Bright Navy plus the 4px Focus glow; no outline.

### Navigation
- **Utility bar:** Midnight Navy, 40px, .85rem on-navy links that turn gold on hover.
- **Header:** sticky white (97%), 80px, hairline bottom; seal (56px) plus the college name in Plus Jakarta Sans 800 navy and a muted sub-line.
- **Links:** Plus Jakarta Sans 600 .95rem ink, 10px 12px padding, 6px radius; hover Bright Navy on Cool Grey; current page navy with a 2px gold underline.
- **Mobile (under 1080px):** a labelled Menu/Close button with an animated burger opens a full-screen white sheet; focus is trapped, the rest of the page is inert, Escape closes.
- **Tabs:** Plus Jakarta Sans 700 muted; selected is navy with a 3px gold underline on the hairline; arrow-key, Home/End and URL-hash support.

### Lists and Disclosure
- **Programme list / accordion:** rows on Cool Hairline dividers with a navy Plus Jakarta Sans code column and the name beside it; the accordion uses a 28px circular plus/minus toggle.
- **Checklist:** navy 20px discs with a white tick, two columns on desktop.
- **Files:** grid rows with a Cool Grey file-type badge, title and size, and a Bright Navy arrow; hover fills Cool Grey.
- **FAQ:** Plus Jakarta Sans 700 summaries with a navy chevron that rotates open.
- **Timeline:** 2px hairline spine, gold dots ringed in the section ground, navy year numerals.
- **Events:** date / description / weekday grid on hairline rows.

### Quick-Access Bar (signature)
A four-cell white strip directly under the home hero, divided by hairlines: 30px Bright Navy line icon, a Plus Jakarta Sans 700 title and a muted sub-line. Hover fills Cool Grey. Two-by-two under 900px.

### Page Header (signature)
Inner pages open on Academic Navy: breadcrumbs, a white display H1, an on-navy lede, a rounded photograph with the Lifted shadow on the right (hidden under 900px), and the seal as a 420px, 7%-opacity watermark bleeding off the bottom-right corner.

### Portal Row
White row card (16px radius, hairline) with an 84px navy acronym tile (12px radius, Plus Jakarta Sans 800 white), title and description, and a Bright Navy "go" link; hover Bright Navy border and Soft shadow.

## Do's and Don'ts

### Do:
- **Do** open every section heading with the 48 x 3px gold rule and keep H2s in Plus Jakarta Sans 800 ink.
- **Do** keep gold to hairlines, underlines, dots and the single gold CTA on a navy band (The Foil Rule).
- **Do** use Bright Navy for every link, hover and focus state; on navy grounds switch focus and hover to gold.
- **Do** use real St. Clare photography and the vector seal; tint photo overlays with Midnight Navy at .35 (hero), .82 (captions) or a .88-to-.15 gradient (banner).
- **Do** separate content with 1px Cool Hairline rows and alternate white / Cool Grey section grounds.
- **Do** animate with the single easing cubic-bezier(.2, .8, .2, 1): .2-.3s for state changes, .7s for reveals with 80ms stagger steps; keep content visible without JavaScript and static under reduced-motion.
- **Do** keep touch targets at 44px or more and buttons at 48px.

### Don't:
- **Don't** fill sections, cards or large areas with gold, or set gold text on white.
- **Don't** introduce playful, illustrated, cartoon or kindergarten-like devices; this is a corporate college, per the user's direction.
- **Don't** use any typeface other than Plus Jakarta Sans and Inter, or set headings below 700.
- **Don't** add hard, offset or coloured shadows; shadows are soft and tinted with ink.
- **Don't** use uppercase tracked labels as kickers above headings; they are reserved for metadata.
- **Don't** present a dated offer without the Gold Wash dated pill and its school year.
