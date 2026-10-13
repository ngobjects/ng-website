# Logo explorations

Work towards a calmer engifer logo. Nothing here is final; the logo the site uses is in `src/main/resources/public/`, and the published logo set is one level up in `logo/`.

| File | What it is |
| --- | --- |
| `index.html` | The mark directions (A to F), on light and on the hero's emerald, plus ways of marking the "ng". |
| `typefaces.html` | Wordmark typefaces side by side with the A3 mark. |
| `generate.py` | Draws the marks and writes the SVGs that `index.html` shows. |
| `typefaces.py` | Writes `typefaces.html`. |
| `site_logo.py` | Writes the A3 mark with one of the typefaces into the site's `public/` folder. Prints the image heights for the sidebar and hero templates. |
| `fonts/` | The typefaces compared in `typefaces.html`, each with its SIL Open Font License. The original Atkinson Hyperlegible and Inter are taken from the site's own fonts. |

The site currently uses A3 (the flat root, a shade deeper than the old flesh colour) with an Atkinson Hyperlegible Next Bold wordmark and the "ng" coloured:

    python site_logo.py "Atkinson Hyperlegible Next Bold"

The scripts need a Python with `fonttools` and `brotli` installed (`pip install fonttools brotli`). Run them from anywhere; paths are relative to the scripts.
