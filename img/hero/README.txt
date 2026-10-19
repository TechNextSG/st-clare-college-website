Home page hero slideshow images (St. Clare College website).

- Put the photos here as PNG, named hero-NN-description.png. Each becomes a slide, in number order (01, 02, 03...).
  JPG also works.
- The build makes light web copies in the "web" subfolder automatically (do not edit those by hand).
- Captions are in hero.json ("file" = name without .png). A photo with no entry uses its file name as the caption.
- Recommended size: 1800 x 1000 px or larger, landscape. The photo shows inside an arched window, so keep the subject centred.
- After changing photos, run: python build.py
