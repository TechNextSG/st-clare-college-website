Home page hero slideshow images (St. Clare College website).

- Every file named hero-NN-description.webp in this folder becomes a slide, in number order (01, 02, 03...).
- Add a matching hero-NN-description-800.webp (800 px wide) for phones; optional.
- Captions are in hero.json ("file" = name without .webp). A photo with no entry uses its file name as the caption.
- Recommended size: 1800 x 1000 px or larger, landscape, subject away from the left third (the headline sits there).
- After changing photos, run: python build.py
