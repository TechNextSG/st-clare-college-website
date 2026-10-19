---
name: St. Clare College of Caloocan
description: Campus Tarpaulin - flat gloss-vinyl fields, hardware and paper notices, hung on a spring.
colors:
  tarp-red: "#d7141a"
  tarp-red-deep: "#a50f14"
  sunflower: "#ffd400"
  sunflower-hover: "#ffe347"
  seal-royal: "#0b2a8f"
  seal-royal-deep: "#071d66"
  ink: "#111111"
  vinyl-white: "#ffffff"
  wall-paper: "#eceef1"
  kraft: "#b98b55"
  kraft-deep: "#8e6638"
  cork: "#c9a66b"
  steel: "#9aa0a6"
  muted-ink: "#45454b"
  note-yellow: "#fff6b8"
  note-pink: "#ffe1dc"
  note-blue: "#dfe8ff"
  flap-cell: "#1d1d1f"
typography:
  display:
    fontFamily: "Big Shoulders, Shoulders Fallback, Arial Narrow, sans-serif"
    fontSize: "clamp(3.4rem, 11vw, 9.5rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.005em"
  headline:
    fontFamily: "Big Shoulders, Shoulders Fallback, Arial Narrow, sans-serif"
    fontSize: "clamp(2.8rem, 7vw, 6rem)"
    fontWeight: 900
    lineHeight: 0.86
    letterSpacing: "-0.005em"
  title:
    fontFamily: "Big Shoulders, Shoulders Fallback, Arial Narrow, sans-serif"
    fontSize: "clamp(1.6rem, 2.4vw, 2.2rem)"
    fontWeight: 900
    lineHeight: 0.95
  lede:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.1rem, 1.5vw, 1.32rem)"
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.74rem"
    fontWeight: 800
    letterSpacing: "0.08em"
  hand:
    fontFamily: "Kalam, Comic Sans MS, cursive"
    fontSize: "1.15rem"
    fontWeight: 700
    lineHeight: 1.1
rounded:
  none: "0px"
  hardware: "2px"
  flap: "3px"
  ring: "50%"
spacing:
  gutter: "clamp(16px, 4vw, 44px)"
  wrap: "1280px"
  section: "clamp(80px, 11vw, 150px)"
  section-tight: "clamp(56px, 8vw, 100px)"
  head-gap: "clamp(40px, 6vw, 80px)"
components:
  tag-button:
    backgroundColor: "{colors.sunflower}"
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    rounded: "{rounded.none}"
    padding: "0 22px 0 40px"
    height: "50px"
  tag-button-hover:
    backgroundColor: "{colors.sunflower-hover}"
  tag-button-red:
    backgroundColor: "{colors.tarp-red}"
    textColor: "{colors.vinyl-white}"
  tag-button-red-hover:
    backgroundColor: "{colors.tarp-red-deep}"
  tag-button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.sunflower}"
  tarp-red:
    backgroundColor: "{colors.tarp-red}"
    textColor: "{colors.vinyl-white}"
    rounded: "{rounded.none}"
    padding: "clamp(46px, 6vw, 80px) clamp(24px, 5vw, 64px) clamp(40px, 5vw, 60px)"
  note-card:
    backgroundColor: "{colors.vinyl-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "26px 24px 22px"
  requirement-sheet:
    backgroundColor: "{colors.kraft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "clamp(26px, 4vw, 50px)"
  level-picker-tab:
    backgroundColor: "{colors.vinyl-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "18px 22px"
    height: "120px"
  form-field:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "6px 0"
    height: "40px"
  form-field-focus:
    backgroundColor: "{colors.note-yellow}"
  menu-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.sunflower}"
    rounded: "{rounded.none}"
    padding: "0 16px"
    height: "48px"
---

# Design System: St. Clare College of Caloocan

## Overview

**Creative North Star: "The Campus Tarpaulin"**

The site is the printed vinyl a Filipino family reads on a school facade, set with poster-house discipline. Every major surface is a flat sheet of gloss vinyl in one of four loud colours (tarp red, sunflower, seal royal, ink), hung from a steel pipe with zip-ties and punched with metal grommets. Admissions material shifts to the paper world of the same campus: a long brown kraft envelope, cork boards, coloured notice slips with push-pins, rubber stamps and torn queue tickets.

Depth is physical, not atmospheric. Things overlap and hang; the only shadows are the soft offset-blur shadows a hung sheet or pinned slip actually casts. There are no colour gradients and no glows. Type shouts in a condensed 900-weight display face set huge and uppercase, while body copy stays plain, generous and readable in Figtree. A marker hand appears only where a person would have written something.

Motion is the material obeying physics: tarps unfurl, sway on a spring that responds to scroll velocity and the pointer, notices drop onto pins, stamps thud, split-flap cells clatter, and the level picker re-deals its content. With reduced motion, everything stands still and fully visible.

**Key Characteristics:**
- Flat full-bleed colour fields; section backgrounds alternate red, sunflower, royal, ink, white vinyl and cork.
- Hardware as ornament with a job: grommets, zip-ties, pipe, pins, cords, key-tag holes.
- Square corners everywhere; only hardware is round.
- Heavy ink rules (3-4px) as structure for boards, pickers, forms and the header.
- Condensed uppercase display at poster scale; plain humanist body.
- Spring-hung motion with a strict reduced-motion fallback.

## Colors

Four printed vinyl inks at full saturation, a paper/kraft secondary world for admissions, and a cool wall grey that everything hangs against.

### Primary
- **Tarp Red** (tarp-red): the signature field. Hero tarp, alternating section grounds, the open mobile menu, pins, file-type chips, menu underline, checklist ticks, the giant footer wordmark. White text on it.
- **Deep Tarp Red** (tarp-red-deep): hover state of red tags and the inner shading of red pins only.

### Secondary
- **Sunflower** (sunflower): the action and highlight colour. Primary ENROLL tag, flap-strip top rule, `.sun` highlight words on red/royal/ink, focus halo, selection, open-board plus marks. Ink text on it, never white.
- **Sunflower Hover** (sunflower-hover): the tag-button hover fill only.

### Tertiary
- **Seal Royal** (seal-royal): the school-seal blue. Hero photo ground, congratulations tarp, Basic Education level, big numerals on notice cards, DOC file chips. White text on it.
- **Deep Seal Royal** (seal-royal-deep): photo scrim tint and royal pin shading.

### Neutral
- **Ink** (ink): text, every structural rule and border, the footer, the flap strip, menu and FAQ buttons, ticket location labels.
- **White Vinyl** (vinyl-white): white tarps, cards, tickets, boards, form sheets, the header bar.
- **Wall Grey** (wall-paper): the page background and the "hole" inside every grommet and tag punch.
- **Kraft** (kraft) / **Deep Kraft** (kraft-deep): the brown envelope, its flap, and requirement sheets.
- **Cork** (cork): notice-wall section grounds.
- **Steel** (steel) and the grommet greys (#d9dadc, #b4b7bb, #8d9095, pipe #c9ccd0): metal hardware only.
- **Muted Ink** (muted-ink): secondary text such as sub-labels and form footnotes on light grounds.
- **Notice tints** (note-yellow, note-pink, note-blue): paper slips on the notice wall and envelope documents; note-yellow is also the form-field focus fill.
- **Flap Cell** (flap-cell): the split-flap character cells.

### Named Rules
**The Flat Vinyl Rule.** Colour fields are flat. No colour gradients, no glows, no translucent glass. The only gradient functions allowed are drawing tools for physical marks: the envelope's diagonal crease hairlines and the ticket's perforated bottom edge.

**The Ink-On-Sunflower Rule.** Sunflower always carries ink text. White on sunflower is forbidden.

**The Photo Scrim Rule.** Photos under a tarp take a single flat tint (royal at 38% on the home hero, ink at 35% on inner heroes), never a gradient fade.

## Typography

**Display Font:** Big Shoulders, variable 600-900 (with a size-adjusted Arial Narrow fallback "Shoulders Fallback" so the swap does not reflow)
**Body Font:** Figtree, 400-800 with italic
**Hand Font:** Kalam 700

**Character:** A condensed, flat-sided poster grotesk shouting in uppercase, against a friendly, open humanist sans that does the reading. The marker hand is a person's annotation on printed material.

### Hierarchy
- **Display** (900, clamp(3.4rem, 11vw, 9.5rem), 0.86): page h1 inside the hero tarp, split into masked lines. The home hero runs clamp(3.4rem, 8.2vw, 8.4rem); the closing "Enroll now" and footer wordmark go larger still (up to 15rem and 22rem).
- **Headline** (900, clamp(2.8rem, 7vw, 6rem), 0.86): section h2, uppercase, balanced wrap.
- **Title** (900, clamp(1.6rem, 2.4vw, 2.2rem), 0.95): card, ticket and banner h3. Display face also sets nav links (800, 1.22rem), tag buttons, picker labels, programme codes, big numerals and years.
- **Lede** (400-600, clamp(1.1rem, 1.5vw, 1.32rem), 1.5): section intros, max 58ch (46ch in the hero).
- **Body** (400, 17px, 1.6): all reading text; FAQ answers capped at 70ch, timeline copy at 62ch.
- **Label** (800, 0.74-0.78rem, 0.08em, uppercase): form field labels and notice-card meta lines only.
- **Hand** (Kalam 700, 1.1-2.4rem, 1.1): photo-print captions, the envelope addressee, short handwritten asides.

### Named Rules
**The Shout Rule.** Display type is always Big Shoulders 900, uppercase, line-height 0.8-0.95. Never set it in sentence case or at body weight.

**The Marker Rule.** Kalam appears only where a hand would write: captions, addressees, one-line asides. Never a headline, never body, never a button.

## Layout

A single 1280px wrap (`min(1280px, 100% - 2 * gutter)`) with a fluid gutter of clamp(16px, 4vw, 44px). Sections are full-bleed colour bands with generous vertical rhythm, clamp(80px, 11vw, 150px), or clamp(56px, 8vw, 100px) for tight bands. Section heads use an asymmetric two-column grid (1.3fr / 0.9fr, headline left, lede right, bottom-aligned) that collapses to one column at 860px.

Content layouts are grids of hung or pinned objects: two-column splits (1fr/1fr, collapsing at 900px), an eight-flag bunting row (four per row under 900px), a five-up key-tag row (two at 1000px, one at 520px), a three-column masonry notice wall (`columns: 3 300px`), and the envelope-plus-tickets route (envelope sticky at top 150px on desktop). The header is sticky; at 1100px the nav becomes a full-screen red sheet that unrolls from the top. Body text never drops below 17px on phones, and the page never scrolls horizontally (`overflow-x: clip`).

## Elevation & Depth

Depth comes from overlapping flat layers and the shadow a hung or pinned object would cast. Shadows are offset downward with negative spread, so they read as weight under a sheet, never as a halo around it. Surfaces lying flat on the page (boards, picker, rows, footer) have no shadow and are defined by ink rules instead.

### Shadow Vocabulary
- **Hang** (`box-shadow: 0 18px 24px -12px rgba(17,17,17,.45), 0 2px 3px rgba(17,17,17,.18)`): small hung objects at rest, such as tag buttons and key tags.
- **Hang Large** (`box-shadow: 0 34px 44px -22px rgba(17,17,17,.55), 0 3px 6px rgba(17,17,17,.2)`): tarps, the envelope, requirement sheets, photo prints, the registration form, and hover state of key tags and notice cards.
- **Paper** (`box-shadow: 0 10px 18px -10px rgba(17,17,17,.5), 0 1px 2px rgba(17,17,17,.2)`): paper slips, tickets and envelope documents.
- **Cut-out drop** (`filter: drop-shadow(-14px 10px 18px rgba(0,0,0,.35))`): photo cut-outs of real Clareans and the printed seal stamp.

### Named Rules
**The Hung Shadow Rule.** A shadow means something is hanging or pinned. Flat-on-the-page elements get an ink rule, not a shadow. No coloured shadows, no glows.

## Shapes

Square-cut vinyl and paper: corner radius is 0 on every sheet, card, button, field and tab. Round forms belong only to hardware: grommets, pins, tag punch holes and key-tag holes (50%), plus 2-3px softening on zip-ties and split-flap cells. Silhouettes come from clip-path cuts that mimic die-cut print: the tag button's pointed left end with a punched hole, bunting pennants with a notched V, and the envelope's triangular flap. Structure is drawn with ink rules: 4px for frames (header, picker, board, form, map, factband), 3px for internal dividers, 1-2px or dashed for list rows and form underlines.

## Components

### Tag Button (primary action)
A die-cut hang tag. **Shape:** square with a pointed left end (`clip-path` 16px point) and a punched grommet hole at 16px. **Primary:** sunflower with ink text, Big Shoulders 900 1.35rem uppercase, min-height 50px, padding 0 22px 0 40px, Hang shadow. **Hover:** rotates -3deg and lifts 2px on the out-expo ease, fill goes to sunflower-hover. **Variants:** red (white text, hover deep red) and ink (sunflower text). **Hung tag:** the hero ENROLL tag hangs on a 3px ink cord below the tarp edge, 1.6rem, 60px tall, swaying at 2.2x the tarp's angle.

### Tarp (signature container)
A flat vinyl sheet in red, sunflower, royal, ink or white variants, with four corner grommets (plus an optional centre grommet), zip-ties to the pipe above, and the Hang Large shadow. Transform origin is the top edge; JavaScript writes a `--sway` angle (rotation plus a slight counter-skew) from the spring simulation. Used for the hero, inner-page heroes, vision/mission banners and academic strand banners.

### Grommets, Ties and Pipe
Grommets are 18px steel rings (inset ring shadows) whose centre shows the wall grey. Ties are 4px ink straps with a 12px head, hanging 30px above the sheet. The pipe is a 10px steel bar across the hero top.

### Split-flap Strip
An ink band with a 4px sunflower top rule. Fixed-width dark cells (18-30px wide, 30-46px tall, 3px radius, centre hairline) cycle programme names every 3.2s; each cell flips 2-7 random characters before landing. A live region announces each word; a 44px pause button sits at the end.

### Level Picker (re-deal tabs)
A three-cell ink-framed tablist: white cells with huge display labels. The selected cell fills by level (Basic = royal, SHS = sunflower, College = red). Selecting re-deals the panel: programme rows fly in from the right with a slight rotation, figures and notes pop up with a back ease. Arrow, Home and End keys move between tabs. Stacks vertically under 860px.

### Envelope and Tickets (enrollment route)
A kraft envelope (9:5) with a deep-kraft triangular flap and crease lines. On scroll the flap rotates open and three coloured documents slide out; checklist ticks pop in one by one. Beside it, white queue tickets carry a huge red step numeral, an ink-and-sunflower location label, the Paper shadow and a perforated bottom edge; they tear in from alternating sides.

### Painted Sign Strip
A white band with 4px ink rules where facts run as one giant uppercase sentence, words alternately red and royal, separated by sunflower stars. It scrubs sideways with scroll; with reduced motion it wraps instead.

### Bunting Flags
Pennants on a 3px ink line, cycling red, sunflower, royal (and a white logo flag), notched with clip-path. They drop on the line with an elastic bounce and then sway.

### Congratulations Tarp
A royal panel framed by grommets: commencement photo left, hand-lettered sunflower greeting and headline right.

### Papercut Flame
A flat layered SVG flame for the Professional Mace; each paper layer flickers with an independent yoyo scale and skew.

### Note Cards, Pins and Rubber Stamps
Paper slips (white, yellow, pink, blue) with the Paper shadow and a small authored tilt (`--r`), pinned by a 22px red, sunflower or royal push-pin. Linked cards straighten, lift 6px and scale 1.02 on hover with the Hang Large shadow. Optional meta line in red label type. Rubber stamps are a 3px current-colour border around display type, rotated -6deg, in red or royal.

### Programme Board
An ink-framed accordion of `details` rows: programme code in red display, title and sub-line in Figtree, a sunflower plus block that rotates 45deg when open. The open row inverts to ink with a sunflower code. Chips inside are 2px ink-outlined labels.

### Requirement Sheets
Kraft sheets with Hang Large shadow, selected by an ink-framed tab row (selected tab = ink with sunflower text), carrying a two-column checklist and a rubber stamp.

### Key Tags (portals)
Five hanging tags cycling red, sunflower, royal, ink and white, each with a steel key-hole at the top, a huge display system code, and a "go" link pinned to the bottom. They drop in with an elastic bounce and sway; hover deepens the shadow.

### Inputs / Fields (registration form)
The contact form is a printed registration sheet: white, 4px ink frame, Hang Large shadow, a header with the seal. Fields sit in ink-ruled cells with uppercase micro-labels; inputs are borderless with a 2px dashed underline. **Focus:** the underline turns solid red and the field fills note-yellow. Two columns, one under 680px.

### Navigation
A sticky white bar with a 4px ink bottom rule, the seal and stacked display wordmark at left, display-face links (800, 1.22rem) with a red 4px underline that wipes in on hover and stays on the current page, and a sunflower ENROLL tag. At 1100px it becomes an ink MENU button; the menu unrolls as a full-screen red sheet (clip-path drop) with huge links and sunflower underlines; Escape closes it.

### Footer
Ink ground, four columns (two at 900px, one at 540px), sunflower display headings, red square social buttons that flip to sunflower on hover, and a giant red uppercase wordmark that rises from below the fold on scroll.

### Motion Grammar
- **Unfurl:** clip-path drops a sheet from its top edge (1.3s, out-expo), then gives the spring a nudge.
- **Sway:** a damped spring per hung object (tarps stiffer and heavier than flags, keys and tags) fed by scroll velocity, pointer movement over the object and a slow breeze; clamped to plus or minus 7deg.
- **Flap:** per-character split-flap flips in 70ms steps, staggered 28ms per cell.
- **Pin-drop:** notices fall 60px onto their authored tilt with a bounce ease.
- **Stamp:** scale from 1.8-2.2 with rotation, power4-in, then a tiny 1.06 thud.
- **Re-deal:** tab panels' rows and figures fly back in on every selection.
- **Reduced motion:** GSAP and Lenis do not start, so no pre-hidden states are applied; tarps, flags and keys are forced to `transform: none`; transitions and animations collapse to 0.01ms; the flap strip shows its first word statically and pauses; the sign strip wraps. Content is fully visible without JavaScript.

## Do's and Don'ts

### Do:
- **Do** build every major surface as a flat vinyl field in tarp red, sunflower, seal royal, ink or white vinyl, with grommets and ties when it hangs.
- **Do** make the primary action a sunflower Tag Button with ink text; use the red or ink variant only on grounds where sunflower would vanish.
- **Do** give hung and pinned objects the Hang, Hang Large or Paper shadow, and give flat-lying structures a 3-4px ink rule instead.
- **Do** set every headline in Big Shoulders 900 uppercase at line-height 0.8-0.95, and keep reading text in Figtree at 17px or larger.
- **Do** move the admissions and notice world into kraft, cork and coloured paper slips with pins and rubber stamps.
- **Do** register any new hanging element with the spring sway and give it a static reduced-motion state.

### Don't:
- **Don't** use colour gradients, glows, glassmorphism or coloured shadows; gradients are allowed only to draw creases and perforations.
- **Don't** round the corners of sheets, cards, buttons or fields; only hardware is round.
- **Don't** put white text on sunflower.
- **Don't** use Kalam for headlines, body or buttons.
- **Don't** hide content behind motion: every reveal must start visible when JavaScript or motion is off.
- **Don't** introduce small uppercase kicker labels above headlines; the micro-label style is reserved for form fields and notice meta lines.
