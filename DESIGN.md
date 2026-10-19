---
name: St. Clare College of Caloocan
description: Paper Campus - layered construction paper, scissor-cut edges, paper grain and soft lift shadows; a pop-up diorama of the Caloocan campus.
colors:
  scissor-red: "#d7141a"
  scissor-red-deep: "#a50f14"
  sunflower: "#ffd400"
  sunflower-soft: "#ffe880"
  seal-royal: "#0b2a8f"
  sky-sheet: "#1f4fc4"
  leaf: "#3d9a3a"
  leaf-deep: "#2b7a2e"
  leaf-soft: "#7cc46a"
  kraft: "#b98b55"
  kraft-deep: "#8e6638"
  kraft-pale: "#e8d3b0"
  wood: "#8a5232"
  ink: "#141414"
  white-sheet: "#ffffff"
  chalk-table: "#e4ecf6"
  muted-ink: "#3f4250"
  note-yellow: "#fff3a6"
  note-pink: "#ffd9d3"
  note-blue: "#d6e3ff"
  dusk-navy: "#1c2340"
typography:
  display:
    fontFamily: "Bricolage, Bricolage Fallback, system-ui, sans-serif"
    fontSize: "clamp(3rem, 8vw, 6.6rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 82"
  headline:
    fontFamily: "Bricolage, Bricolage Fallback, system-ui, sans-serif"
    fontSize: "clamp(2.4rem, 5.6vw, 4.6rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 82"
  title:
    fontFamily: "Bricolage, Bricolage Fallback, system-ui, sans-serif"
    fontSize: "clamp(1.4rem, 2.1vw, 1.9rem)"
    fontWeight: 800
    lineHeight: 1
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 82"
  numeral:
    fontFamily: "Bricolage, Bricolage Fallback, system-ui, sans-serif"
    fontSize: "clamp(3rem, 6vw, 5rem)"
    fontWeight: 800
    lineHeight: 0.8
    fontVariation: "'wdth' 78"
  lede:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(1.08rem, 1.45vw, 1.28rem)"
    fontWeight: 400
    lineHeight: 1.55
  body:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.6
  label:
    fontFamily: "Figtree, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 800
    letterSpacing: "0.06em"
  hand:
    fontFamily: "Kalam, Comic Sans MS, cursive"
    fontSize: "1.1rem"
    fontWeight: 700
    lineHeight: 1.1
rounded:
  cut: "3px"
  tab-sheet: "8px"
  tile: "10px"
  folder-tab: "12px 12px 0 0"
  pill: "999px"
spacing:
  gutter: "clamp(16px, 4vw, 44px)"
  wrap: "1260px"
  band: "clamp(80px, 10vw, 140px)"
  sheet: "clamp(24px, 4vw, 50px)"
  grid-gap: "clamp(18px, 3vw, 40px)"
  section-gap: "clamp(30px, 6vw, 90px)"
components:
  button-primary:
    backgroundColor: "{colors.sunflower}"
    textColor: "{colors.ink}"
    rounded: "{rounded.tab-sheet}"
    padding: "0 24px"
    height: "52px"
  button-red:
    backgroundColor: "{colors.scissor-red}"
    textColor: "{colors.white-sheet}"
    rounded: "{rounded.tab-sheet}"
    padding: "0 24px"
    height: "52px"
  button-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.sunflower}"
    rounded: "{rounded.tab-sheet}"
    padding: "0 24px"
    height: "52px"
  button-white:
    backgroundColor: "{colors.white-sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.tab-sheet}"
    padding: "0 24px"
    height: "52px"
  button-small:
    rounded: "{rounded.tab-sheet}"
    padding: "0 16px"
    height: "44px"
  paper-sheet:
    backgroundColor: "{colors.white-sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.cut}"
    padding: "{spacing.sheet}"
  notice-note:
    backgroundColor: "{colors.note-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.cut}"
    padding: "30px 24px 22px"
  folder-tab:
    backgroundColor: "{colors.white-sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.folder-tab}"
    padding: "16px 24px 18px"
    height: "64px"
  folder-tab-selected:
    backgroundColor: "{colors.scissor-red}"
    textColor: "{colors.white-sheet}"
  form-field:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "0"
    padding: "6px 0"
    height: "44px"
  form-field-focus:
    backgroundColor: "{colors.note-yellow}"
  chip:
    backgroundColor: "{colors.white-sheet}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "5px 12px"
---

# Design System: St. Clare College of Caloocan

## Overview

**Creative North Star: "The Paper Campus"**

The whole site is a construction-paper diorama of one Caloocan school. Every surface is a sheet of coloured paper that has been cut with scissors, laid on a pale chalk-blue table, and lifted a few millimetres off the sheet underneath it. Nothing is drawn with a stroke: shape comes from the cut edge, depth from a soft 12-16% lift shadow, and texture from a multiplied fractal-noise paper grain. The home hero is a pop-up book of the campus (sun, clouds, hills, building, trees, bunting) built from authored SVG layers that rise on load and drift at different speeds with scroll and pointer.

The register is bright, hand-made and school-proud, not childish. Sheets are cut from five saturated school colours (scissor red, sunflower, seal royal, sky, leaf) plus kraft and white, with pastel sticky notes for secondary content. Real campus photos are mounted as taped prints; people appear as Open Peeps cut-out stickers (CC0) with a white die-cut border. Type is a compressed, heavy Bricolage Grotesque that reads like letters cut from card, against a calm Figtree body and a Kalam hand for captions written on the paper.

Motion is a pop-up book grammar: layers rise from their base with a back-out overshoot, sheets slap down with a slight rotation and settle to a resting tilt, the kraft envelope opens on scroll and documents slide out, bunting drops onto its line, and the crowd bobs while in view. All content is visible without JavaScript and with reduced motion.

**Key Characteristics:**
- Every coloured surface is a cut sheet: fill on a pseudo-element, roughened by the `#rough` SVG displacement filter, grain-multiplied, lifted by a soft drop shadow.
- Sections are full-bleed paper bands whose top edge is a torn, scissor-cut SVG path in the band's own colour.
- Sheets rest at small tilts (-1.5deg to +1.2deg); hover straightens or lifts them.
- People are Open Peeps stickers, never stock photos of models.
- Paper objects carry the story: masking tape, kraft envelope, numbered tickets, bunting flags, folder tabs, key tags, stamp marks.

## Colors

Saturated construction-paper sheets on a pale chalk table, with ink for type and pastel notes for secondary content.

### Primary
- **Scissor Red** (scissor-red): the school's main sheet. Ribbon ticker, red bands, mobile menu sheet, selected College tab, course codes, ticket and timeline numerals, file-type tabs, social discs, checklist ticks, nav underline strip.
- **Scissor Red Deep** (scissor-red-deep): small red text on light paper where Scissor Red is too bright (note meta lines, required-field marks, stamp marks on notes).

### Secondary
- **Sunflower** (sunflower): the default call-to-action sheet (Enroll buttons); accent text on dark sheets (footer headings, ink-button labels, mace citation); FAQ and programme-board plus discs; the selected SHS tab; text selection.
- **Sunflower Soft** (sunflower-soft): hover fill for download rows; sun rays in the diorama.

### Tertiary
- **Seal Royal** (seal-royal): taken from the college seal. Vision sheet, royal bands, selected Basic Ed tab, the mobile hero copy card, document file tabs, big numerals on Basic Ed notes.
- **Sky Sheet** (sky-sheet): the diorama sky behind the home hero and the default inner-page hero; the browser theme colour.
- **Leaf / Leaf Deep / Leaf Soft** (leaf, leaf-deep, leaf-soft): diorama hills and trees (back hill deep, front hill leaf, foreground strip soft). Leaf Deep is the green inner-page hero.

### Neutral
- **White Sheet** (white-sheet): the default paper for cards, the deal panel, FAQ, file rows, the header bar.
- **Chalk Table** (chalk-table): the page background, the table every sheet lies on; also the punched hole in key tags.
- **Ink** (ink): body text, ink buttons, the footer sheet, bunting string, focus ring.
- **Muted Ink** (muted-ink): secondary small print (`small` lines, form footnotes).
- **Kraft / Kraft Deep** (kraft, kraft-deep): the enrollment envelope body and flap only.
- **Kraft Pale** (kraft-pale): the light kraft band.
- **Wood** (wood): tree trunks in the diorama.
- **Dusk Navy** (dusk-navy): the dark inner-page hero variant.
- **Note Yellow / Pink / Blue** (note-yellow, note-pink, note-blue): sticky-note sheets on the notice wall, envelope documents, the open programme-board row, the focused form field.

### Named Rules
**The Sheet Not Swatch Rule.** A colour enters the page as a cut sheet of paper (grain-multiplied, roughened, lifted), never as a flat fill or a gradient. Gradients are not used for colour anywhere.

**The Paired Text Rule.** Each sheet colour carries a fixed text colour: red, royal, sky, leaf and ink sheets take white text (ink buttons take sunflower); sunflower, white, kraft and the pastel notes take ink.

## Typography

**Display Font:** Bricolage Grotesque, self-hosted as "Bricolage" (weights 600-800, width 75-100%), with an Arial-based metric fallback
**Body Font:** Figtree (400-800, roman and italic), with system-ui
**Hand Font:** Kalam 700, with Comic Sans MS and cursive

**Character:** Bricolage at weight 800 and 78-85% width reads like heavy letters cut from card and stacked tight (line-height 0.8-0.92); Figtree is the calm, friendly reading voice; Kalam is the pen on the paper, kept for captions and the envelope address.

### Hierarchy
- **Display** (800, clamp(3rem, 8vw, 6.6rem), 0.92, width 82%): page h1 in the hero. The closer h2 goes larger (clamp(3.6rem, 12vw, 10rem), 0.86).
- **Headline** (800, clamp(2.4rem, 5.6vw, 4.6rem), 0.92): band h2, balanced wrap.
- **Title** (800, clamp(1.4rem, 2.1vw, 1.9rem), 1): card and sheet h3; a larger step at clamp(2rem, 4vw, 3.2rem).
- **Numeral** (800, width 78-80%, line-height 0.8-0.95): course codes, years, ticket numbers, key-tag letters, equation tiles; usually Scissor Red or Seal Royal on white.
- **Lede** (400, 600 over the diorama; clamp(1.08rem, 1.45vw, 1.28rem), 1.55, max 56ch): the paragraph under a headline.
- **Body** (400, 17px, 1.6): reading text; long answers cap at 62-68ch.
- **Label** (800, 0.8rem, 0.06em, uppercase): form field labels and event "where" lines.
- **Hand** (Kalam 700, about 1.1rem, 1.1): photo-print captions, envelope address.

### Named Rules
**The Cut Letters Rule.** Every heading, numeral, button label, tab label and brand mark uses Bricolage at 800 with a narrowed width (78-85%). Figtree never sets a heading.

**The Pen Only Writes Rule.** Kalam appears only where a person would have written on the paper: captions under taped prints and the envelope front. Never a heading, never a button.

## Layout

A single centred column, `min(1260px, 100% - 2 * gutter)` with a fluid gutter of clamp(16px, 4vw, 44px). Pages are stacks of full-bleed paper bands with generous vertical padding (clamp(80px, 10vw, 140px)); each band's top edge overlaps the previous band by 44px through its cut-edge SVG.

Inside bands, layout is asymmetric two-column grids: band heads at 1.25fr / 0.95fr (headline left, lede right, bottom-aligned), splits at 1fr / 1fr, the enrollment route at 0.9fr / 1.1fr with a sticky envelope, the collage at 1.05fr / 0.95fr with absolutely placed overlapping prints. Card groups use auto-fill or auto-fit grids (notice wall minmax(280px, 1fr), strands minmax(220px, 1fr)), five key tags across, eight bunting flags across. Notice walls are always CSS grid, never CSS columns, so tape never splits.

Responsive: the desktop menu collapses at 1120px into a full-screen red sheet that opens as a circular clip from the menu button. Two-column grids stack at 860-900px; bunting goes from 8 to 4 across at 900px; key tags from 5 to 2 at 1000px and to 1 at 520px. On phones (760px and under) the hero becomes auto-height, the hero copy moves onto its own tilted royal sheet, and the crowd trims to five peeps.

## Elevation & Depth

Depth is physical layering of paper: each sheet casts a soft, low-opacity shadow onto whatever lies below it, and the scissor filter gives the edge a slightly irregular silhouette. There are no hard offset shadows, glows or glass. Shadows use CSS `filter: drop-shadow` so they follow the rough cut silhouette, not `box-shadow`.

### Shadow Vocabulary
- **Lift** (`drop-shadow(0 6px 8px rgba(20,20,20,.14)) drop-shadow(0 1px 1px rgba(20,20,20,.12))`): every standard sheet, button, tab and row.
- **Lift Large** (`drop-shadow(0 14px 16px rgba(20,20,20,.16)) drop-shadow(0 2px 2px rgba(20,20,20,.12))`): hero-scale sheets (deal panel, ribbon, congratulations banner, mobile hero card).
- **Edge Up** (`drop-shadow(0 -5px 6px rgba(20,20,20,.12))`): torn band edges, casting upward onto the band above.
- **Diorama Layer** (`drop-shadow(0 6px 6px rgba(10,20,60,.22))`): each hero SVG layer, tinted toward the sky.
- **Sticker** (`drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff) drop-shadow(0 -2px 0 #fff) drop-shadow(0 6px 6px rgba(0,0,0,.25))`): Open Peeps cut-outs; a white die-cut border plus lift.

### Named Rules
**The Scissor Filter Rule.** Every paper silhouette goes through `url(#rough)` (feTurbulence fractalNoise, baseFrequency 0.035, 2 octaves, seed 7; feDisplacementMap scale 5), applied to the fill pseudo-element so the text on the sheet stays crisp.

**The Soft Lift Rule.** Paper shadows stay at 12-25% opacity and are blurred. A sheet rests on the table; it never floats or casts a hard offset.

## Shapes

Shapes are cut, not drawn. Sheets have nearly square corners (3px) that the rough filter makes irregular; buttons, rows and tabs are slightly rounder (8px); equation tiles and the deal panel 10px; folder tabs round only their top corners (12px 12px 0), and the deal sheet under them squares its top-left corner to join the selected tab. Silhouettes come from clip-path where paper would be cut: bunting pennants (a V notch), the envelope flap (a triangle) and the mobile menu (a circle reveal). Band tops are wavy torn paths generated per band from a seed. Full circles are kept for small discs (pause button, plus discs, social icons, tick bullets). Sheets carry small resting rotations; masking tape strips sit across top edges at -4deg / +5deg.

## Components

### Buttons
Paper tickets you can lift.
- **Shape:** gently rounded cut sheet (8px), roughened, with the Lift shadow; min-height 52px (small 44px).
- **Primary:** Sunflower sheet, Ink label in Bricolage 800 at 85% width, 1.2rem.
- **Variants:** Scissor Red with a white label; Ink with a Sunflower label; White with an Ink label.
- **Hover / Active:** hover lifts 3px and tilts -1.5deg over 0.4s on the expo-out curve; active presses to 0.98 scale. Focus is the global 3px Ink ring at 3px offset (Sunflower on dark sheets).
- **Text link:** weight 800, underlined, 2px thickness, 0.2em offset.

### Chips
- **Style:** white pill, Ink text at 0.84rem 700, 2px inset ink ring. Used only for programme specialisations on the programme board.

### Cards / Containers
- **Paper sheet:** any colour sheet, 3px corner, grain + scissor filter + Lift; padding clamp(24px, 4vw, 50px) for large sheets, 26-40px for cards.
- **Notice note:** white or pastel sheet with masking tape on top, alternating rests of -1.2deg / 0.9deg / -0.5deg; linked notes straighten and rise 6px on hover. An optional photo bleeds to the sheet edge.
- **Taped print:** white sheet with a 12px border and a 48px bottom lip holding a Kalam caption; photo at 4:3.
- **Key tag:** tall sheet with a punched hole (chalk circle with an inset shadow) at the top, a giant Bricolage letter, and the link pinned to the bottom; tilts alternate and straighten on hover.
- **Ticket:** a numbered enrollment step with a huge red numeral floated left and a small Ink tag with Sunflower text pinned at the top right naming the room.

### Inputs / Fields
- **Style:** no box; a 2px dashed ink underline at 40% on a registration-form sheet, 17px body text, min-height 44px. Labels are uppercase 0.8rem 800 with 0.06em tracking; required marks in Scissor Red Deep.
- **Focus:** the underline turns solid Scissor Red and the field fills Note Yellow, like a highlighted line on a paper form.

### Navigation
- **Desktop:** a sticky white paper bar (roughened, soft downward shadow) with the seal and wordmark on the left, Figtree 700 links, and a 4px red strip that scales in from the left on hover and for the current page.
- **Mobile (1120px and under):** a Menu sheet-button opens a full-screen Scissor Red sheet with Bricolage links at clamp(2.2rem, 10vw, 3.6rem) and Sunflower strips; focus is trapped, the page is inert, Esc closes.

### Folder-Tab Level Picker
Three paper folder tabs (College, Senior High, Basic Ed) sit 8px low and rise to 0 when selected, taking their level colour (Red, Sunflower, Royal). The panel below is a white sheet joined to the tabs. On switching, list rows deal in from the right with a 3deg rotation and the figures pop up. Full ARIA tabs with arrow, Home and End keys and hash deep links.

### Enrollment Envelope
A kraft envelope (back, front, triangular flap) that on scroll flips its flap open and slides three documents (white, yellow, blue) up and out at small angles, while the checklist beside it ticks item by item. The address is written in Kalam.

### Paper Diorama Hero
An inline SVG scene of layered paper (sun with rays, clouds, back hill, campus building, trees, bunting, front hill, foreground strip) where each layer carries a `data-depth` from 0.15 to 1. Layers rise in sequence on load and drift by depth x 14% on scroll and depth x 36px with the pointer. A row of Open Peeps stickers stands along the foreground and the college seal is slapped on at the top right. Inner pages use a shorter version (sun, clouds, two hills) on a Sky, Red, Royal, Leaf Deep or Dusk Navy sheet.

### Bunting
Eight pennant flags (clip-path V notch) on an ink string, alternating Sunflower, White, Royal and Red, fluttering 2.4deg on a 5s loop with staggered delay; they drop onto the line with an elastic ease.

## Do's and Don'ts

### Do:
- **Do** build every coloured surface as a cut sheet: fill on `::before`, `background: var(--grain), <colour>; background-blend-mode: multiply; filter: url(#rough) var(--lift)`.
- **Do** start each band with its torn edge in the band's own colour, overlapping the band above by 44px.
- **Do** give sheets a small resting tilt (within 1.5deg) through `--rest` so the reveal settles there.
- **Do** keep text crisp: the scissor filter goes on the paper layer, never on the element that holds the text.
- **Do** use Open Peeps cut-outs with the white Sticker border for people, and real campus photos as taped prints.
- **Do** pair sheet colours with their fixed text colours (white on Red, Royal, Sky, Leaf, Ink; Ink on Sunflower, White, Kraft, notes).
- **Do** keep everything readable with motion off: reveal targets start hidden only under `.js`, and reduced motion stops the ribbon, flutter and transitions.

### Don't:
- **Don't** draw outlines or strokes around paper sheets; edges come from the cut and the shadow. (The white die-cut border on sticker people is the one contour the world uses.)
- **Don't** use gradients for colour, glass, glows or hard offset shadows.
- **Don't** set a heading in Figtree or Kalam, or a caption in Bricolage.
- **Don't** lay notice cards out with CSS columns; tape must not split across columns.
- **Don't** rest a sheet at more than about 5deg (stickers, stamps and tape strips excepted).
