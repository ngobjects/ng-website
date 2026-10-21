"""Compares wordmark typefaces next to the A3 mark, with the coloured ng. Writes typefaces.html.

Run with a Python that has fonttools and brotli installed: python typefaces.py
"""
import importlib.util, os, sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.varLib.instancer import instantiateVariableFont

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("g", os.path.join(HERE, "generate.py"))
g = importlib.util.module_from_spec(spec); spec.loader.exec_module(g)

FONTS = os.path.join(HERE, "fonts")
SITE_FONTS = os.path.join(HERE, "../../webserver-resources/fonts")
INTER = f"{SITE_FONTS}/inter/inter-600-normal-latin.woff2"

# (label, file, variable axis settings, tracking in em)
NAV = '<nav class="sheets"><a href="index.html">1 · Directions</a> <a href="typefaces.html">2 · Typefaces</a> <a href="roots.html">3 · Roots</a> <a href="errors.html">4 · Errors</a> <a href="wonder-slim.html">5 · wonder-slim</a> <a href="lemongrass.html">6 · Lemongrass</a></nav>'
NAV_CSS = ".sheets { display: flex; gap: 1.25rem; margin: 0 0 1.25rem; font-size: .9rem; } .sheets a { color: #0b7a5c; }"

FACES = [
    ("Atkinson Hyperlegible Bold (the original logo)", f"{SITE_FONTS}/Atkinson-Hyperlegible/Atkinson-Hyperlegible-Bold-102a.woff2", None, -0.02),
    ("Atkinson Hyperlegible Next Bold (on the site)", f"{FONTS}/AtkinsonHyperlegibleNext.ttf", {"wght": 700}, -0.02),
    ("Atkinson Hyperlegible Next SemiBold", f"{FONTS}/AtkinsonHyperlegibleNext.ttf", {"wght": 600}, -0.02),
    ("Bricolage Grotesque Bold", f"{FONTS}/BricolageGrotesque.ttf", {"wght": 700, "wdth": 100, "opsz": 48}, -0.03),
    ("Bricolage Grotesque SemiBold, condensed", f"{FONTS}/BricolageGrotesque.ttf", {"wght": 600, "wdth": 85, "opsz": 48}, -0.02),
    ("DM Sans Bold", f"{FONTS}/DMSans.ttf", {"wght": 700, "opsz": 40}, -0.03),
    ("IBM Plex Sans Bold", f"{FONTS}/IBMPlexSans-Bold.otf", None, -0.02),
    ("Figtree Bold", f"{FONTS}/Figtree.ttf", {"wght": 700}, -0.03),
    ("Inter SemiBold (committed trial)", INTER, {"wght": 600}, -0.025),
]


def wordmark_svg(path, axes, tracking, text, ng):
    f = TTFont(path)
    if axes:
        f = instantiateVariableFont(f, {k: v for k, v in axes.items() if k in [a.axisTag for a in f["fvar"].axes]})
    upm = f["head"].unitsPerEm
    s = 2048 / upm  # normalise to the same units as the mark lockups
    cap = (f["OS/2"].sCapHeight or upm * 0.7) * s
    cmap, glyphs, hmtx = f.getBestCmap(), f.getGlyphSet(), f["hmtx"]
    size = cap * 1.95
    baseline = size / 2 + cap / 2
    x = size + size * 0.24
    parts = []
    for i, ch in enumerate("engifer"):
        name = cmap[ord(ch)]
        pen = SVGPathPen(glyphs)
        glyphs[name].draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
        parts.append(f'<path d="{pen.getCommands()}" fill="{ng if i in (1, 2) else text}" />')
        x += hmtx[name][0] * s + tracking * 2048
    return size, x, "".join(parts)


colors = dict(g.LIGHT, ginger="#e5bd66", leaf="#4f8a4f")
rows = []
for label, path, axes, tracking in FACES:
    cells = []
    for text, ng, bg in ((g.INK, g.TORCH, "#fff"), (g.MINT, g.TURMERIC, g.EMERALD)):
        size, end, words = wordmark_svg(path, axes, tracking, text, ng)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {end + 20:.0f} {size:.0f}" style="height:56px;display:block">'
               f'<g transform="scale({size / 64:.4f})">{g.mark_root(colors)}</g>{words}</svg>')
        cells.append(f'<div style="background:{bg};padding:18px 26px;flex:1;display:flex;align-items:center">{svg}</div>')
    rows.append(f'<div style="display:flex;align-items:stretch;border-bottom:1px solid #dde6e1"><div style="width:230px;padding:18px;font:14px system-ui">{label}</div>{"".join(cells)}</div>')

if __name__ == "__main__":
    page = ("""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>engifer typefaces</title><style>
body { margin: 0; padding: 2rem 1rem 4rem; background: #f5f8f6; color: #121a17; font: 15px/1.5 system-ui, sans-serif; }
main { max-width: 1300px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin: 0 0 .25rem; }
.intro { color: #56635c; margin: 0 0 2rem; max-width: 70ch; }
.rows { border: 1px solid #dde6e1; border-radius: 10px; overflow: hidden; background: #fff; }
""" + NAV_CSS + """
</style></head><body><main>
<h1>engifer typefaces</h1>
""" + NAV + """
<p class="intro">Wordmark typefaces side by side with the A3 mark, the ng coloured as in the logo. The site uses Atkinson Hyperlegible Next Bold.</p>
<div class="rows">""" + "".join(rows) + "</div></main></body></html>\n")
    open(os.path.join(HERE, "typefaces.html"), "w").write(page)
