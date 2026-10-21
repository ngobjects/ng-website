# Logo explorations

Work towards a calmer engifer logo. It lives in the site's public folder so it can be shared: the site serves it at `/logo-explorations/index.html`. The logo the site uses is in `webserver-resources/`, and the published logo set is in `logo/` at the root of the repository.

| File | What it is |
| --- | --- |
| `index.html` | The mark directions (A to F), on light and on the hero's emerald, plus ways of marking the "ng". The original logo is kept here as `original-*.svg`. |
| `typefaces.html` | Wordmark typefaces side by side with the A3 mark. |
| `roots.html` | The articulated root: knuckles, nubs, growth rings and a cut end, added one at a time. |
| `generate.py` | Draws the marks and writes the SVGs that `index.html` shows. |
| `typefaces.py` | Writes `typefaces.html`. |
| `roots.py` | Writes `roots.html`. `python roots.py site 5` writes variant 5 into the site's logo files. |
| `errors.html` | Ginger in trouble: snapped, wilted, curled and shrivelled roots, and inline error messages built on them. Written by `errors.py`. |
| `wonder-slim.html` | First logo ideas for wonder-slim: marks about the word "slim". Written by `wonder_slim.py`. |
| `lemongrass.html` | wonder-slim as lemongrass, ginger's partner in the pot, with states for errors and the error box, warnings and expired page built on them. Written by `wonder_slim.py`, which needs nothing beyond Python. |
| `site_logo.py` | Writes the A3 mark with one of the typefaces into the site's `webserver-resources/` folder. Prints the image heights for the sidebar and hero templates. |
| `fonts/` | The typefaces compared in `typefaces.html`, each with its SIL Open Font License. The original Atkinson Hyperlegible and Inter are taken from the site's own fonts. |

The direction we're taking is the articulated root from `roots.html` (variant 4 or 5), with an Atkinson Hyperlegible Next Bold wordmark and the "ng" coloured. To put a variant on the site, then refresh the project in Eclipse:

    python roots.py site 5

`site_logo.py` does the same for the earlier flat root (A3) with any of the typefaces in `typefaces.py`.

The scripts need a Python with `fonttools` and `brotli` installed (`pip install fonttools brotli`). Run them from anywhere; paths are relative to the scripts.
