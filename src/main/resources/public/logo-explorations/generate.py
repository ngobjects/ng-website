"""Logo explorations: several mark directions with an Inter wordmark, plus a comparison sheet."""
import os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.varLib.instancer import instantiateVariableFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "../../webserver-resources/fonts/inter")
OUT = HERE  # Run with a Python that has fonttools and brotli installed


INK, MINT, EMERALD, TURMERIC, TORCH = "#121a17", "#f0f7f3", "#074b3c", "#ffb320", "#c41e4a"
GINGER, GINGER_DEEP, LEAF, LEAF_BRIGHT = "#eaa53c", "#b8701f", "#2f8a57", "#5cc98a"


class Font:
    def __init__(self, weight):
        # The bundled Inter files are variable fonts, so pin the weight axis
        self.f = instantiateVariableFont(TTFont(f"{FONTS}/inter-{weight}-normal-latin.woff2"), {"wght": weight})
        self.cmap = self.f.getBestCmap()
        self.glyphs = self.f.getGlyphSet()
        self.hmtx = self.f["hmtx"]

    def glyph(self, ch, x, baseline, scale=1.0):
        name = self.cmap[ord(ch)]
        pen = SVGPathPen(self.glyphs)
        self.glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
        return pen.getCommands(), self.hmtx[name][0] * scale

    def bounds(self, ch):
        pen = BoundsPen(self.glyphs)
        self.glyphs[self.cmap[ord(ch)]].draw(pen)
        return pen.bounds


R, M, B = Font(400), Font(500), Font(600)
UPM, CAP, XH = 2048, 1490, 1118


def leaf(x, y, length, width, angle, fill):
    """A pointed leaf whose base sits at (x, y), pointing up and rotated by angle degrees."""
    L, w = length, width / 2
    d = (f"M0 0 C{w * 1.5:.2f} {-L * 0.25:.2f} {w * 1.1:.2f} {-L * 0.75:.2f} 0 {-L:.2f} "
         f"C{-w * 1.1:.2f} {-L * 0.75:.2f} {-w * 1.5:.2f} {-L * 0.25:.2f} 0 0Z")
    return f'<path d="{d}" fill="{fill}" transform="translate({x} {y}) rotate({angle})" />'


# ---- Marks, each drawn in a 64x64 box. Each takes a dict of colours so it can be recoloured for dark or mono use.

def mark_root(c):
    """A: the ginger hand redrawn flat. No outline, a single fill, a leaf instead of a stalk."""
    s = c["ginger"]
    return ('<g fill="none" stroke-linecap="round">'
            f'<path d="M11 46 L49 41.5" stroke="{s}" stroke-width="13" />'
            f'<path d="M20 44 L15.5 30" stroke="{s}" stroke-width="10" />'
            f'<path d="M35 42.5 L40 26" stroke="{s}" stroke-width="11" />'
            f'<path d="M49 41.5 L53.5 50" stroke="{s}" stroke-width="8.5" />'
            f'<path d="M40.5 22 C40 17 41.5 13.5 44 11" stroke="{c["leaf"]}" stroke-width="3.4" />'
            '</g>'
            + leaf(43.5, 11.5, 13, 7, 48, c["leaf"]))


def mark_tile(c):
    """B: a rounded tile holding the e, with a leaf sprouting from it. Built to survive favicon size."""
    x0, y0, x1, y1 = B.bounds("e")
    scale = 36 / (y1 - y0)
    gw = (x1 - x0) * scale
    gx = 32 - gw / 2 - x0 * scale
    baseline = 32 + 19 - y0 * scale  # centred vertically
    d, _ = B.glyph("e", gx, baseline, scale)
    # The tile is leaf shaped: two round corners, two nearly sharp ones
    tile = "M24 0 H60 A4 4 0 0 1 64 4 V40 A24 24 0 0 1 40 64 H4 A4 4 0 0 1 0 60 V24 A24 24 0 0 1 24 0Z"
    return (f'<path d="{tile}" fill="{c["tile"]}" />'
            f'<path d="{d}" fill="{c["on_tile"]}" />')


def mark_slice(c):
    """C: a cross-section of the root: skin, flesh, and the ring of fibres inside it."""
    fibres = []
    for i in range(12):
        import math
        a = i * math.pi / 6
        fibres.append(f'<path d="M{32 + 7 * math.cos(a):.2f} {32 + 7 * math.sin(a):.2f} L{32 + 14 * math.cos(a):.2f} {32 + 14 * math.sin(a):.2f}" />')
    return (f'<circle cx="32" cy="32" r="28" fill="{c["skin"]}" />'
            f'<circle cx="32" cy="32" r="24.5" fill="{c["ginger"]}" />'
            f'<circle cx="32" cy="32" r="18" fill="none" stroke="{c["skin"]}" stroke-width="1.6" opacity=".55" />'
            f'<g stroke="{c["skin"]}" stroke-width="1.6" stroke-linecap="round" opacity=".45">' + "".join(fibres) + "</g>"
            f'<circle cx="32" cy="32" r="3" fill="{c["skin"]}" opacity=".6" />')


def mark_tag(c):
    """E: a template tag where the slash is a shoot. The framework is about templates; ginger is about roots."""
    return ('<g fill="none" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M17 19 L5 32 L17 45" stroke="{c["chevron"]}" stroke-width="5.5" />'
            f'<path d="M47 19 L59 32 L47 45" stroke="{c["chevron"]}" stroke-width="5.5" />'
            f'<path d="M26 53 C29 42 31 32 36.5 21" stroke="{c["leaf"]}" stroke-width="5" />'
            '</g>'
            + leaf(36.5, 22, 15, 9, 32, c["accent"]))


def mark_nodes(c):
    """F: the root as a little graph of nodes. A geometric take on the hand of ginger."""
    s = c["ginger"]
    return ('<g fill="none" stroke-linecap="round">'
            f'<path d="M15 44 L47 40 M15 44 L28 22 M47 40 L28 22" stroke="{s}" stroke-width="4.5" />'
            '</g>'
            f'<circle cx="15" cy="44" r="10" fill="{s}" />'
            f'<circle cx="47" cy="40" r="8.5" fill="{s}" />'
            f'<circle cx="28" cy="22" r="6.5" fill="{s}" />'
            + leaf(30, 16.5, 12, 6.5, 28, c["leaf"]))


LIGHT = dict(ginger=GINGER, skin=GINGER_DEEP, leaf=LEAF, tile=EMERALD, on_tile=MINT, accent=TURMERIC, chevron=EMERALD)
DARK = dict(ginger=TURMERIC, skin=GINGER_DEEP, leaf=LEAF_BRIGHT, tile=MINT, on_tile=EMERALD, accent=TURMERIC, chevron=MINT)


# ---- Wordmark

def wordmark(x, baseline, color, ng=None, ng_weight=None, leaf_dot=None, font=B, tracking=-0.025):
    """Returns (svg, end x). ng colours the n and g, ng_weight sets them in another weight, leaf_dot replaces the i's dot."""
    out, pos = [], x
    for i, ch in enumerate("engifer"):
        is_ng = i in (1, 2)
        f = ng_weight if (is_ng and ng_weight) else font
        glyph_ch = "ı" if (ch == "i" and leaf_dot) else ch
        d, adv = f.glyph(glyph_ch, pos, baseline)
        out.append(f'<path d="{d}" fill="{ng if (is_ng and ng) else color}" />')
        if ch == "i" and leaf_dot:
            x0, _, x1, _ = f.bounds("ı")
            cx = pos + (x0 + x1) / 2
            out.append(leaf(cx - 40, baseline - XH - 120, 560, 330, 30, leaf_dot))
        pos += adv + tracking * UPM
    return "".join(out), pos - tracking * UPM


def lockup(mark, colors, text, **kw):
    """Mark beside the wordmark, everything in font units."""
    size = CAP * 1.95
    baseline = size / 2 + CAP / 2
    gap = size * 0.24
    words, end = wordmark(size + gap, baseline, text, **kw)
    width, height = end + 20, size
    s = size / 64
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.0f} {height:.0f}">'
            f'<g transform="scale({s:.4f})">{mark(colors)}</g>{words}</svg>\n')


def word_only(text, **kw):
    top = XH + 700  # room for ascenders and the leaf
    words, end = wordmark(10, top, text, **kw)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {end + 20:.0f} {top + 460:.0f}">{words}</svg>\n'


def mark_svg(mark, colors):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{mark(colors)}</svg>\n'


VARIANTS = [
    ("a-root", "Flat root", "The current idea, cleaned up. No outline, one ginger colour, a leaf instead of a stalk.", mark_root),
    ("b-tile", "Leaf tile", "The e on an emerald tile cut in the shape of a leaf. Reads well as a favicon and app icon.", mark_tile),
    ("c-slice", "Slice", "A cross-section of the root. Calm and round, sits well next to text.", mark_slice),
    ("e-tag", "Sprouting tag", "A template tag where the slash grows a leaf. Nods to what the framework does.", mark_tag),
    ("f-nodes", "Root graph", "The hand of ginger as three connected nodes. A more technical take.", mark_nodes),
]

files = {}
for key, *_ , mark in VARIANTS:
    files[f"{key}-mark.svg"] = mark_svg(mark, LIGHT)
    files[f"{key}-mark-on-dark.svg"] = mark_svg(mark, DARK)
    files[f"{key}-logo.svg"] = lockup(mark, LIGHT, INK)
    files[f"{key}-logo-on-dark.svg"] = lockup(mark, DARK, MINT)

# A in the current logo's colours: the pale ginger flesh and the green shoot, without the outline
for key, ginger in (("a2-root-flesh", "#ecca7a"), ("a3-root-flesh-deep", "#e5bd66")):
    colors = dict(LIGHT, ginger=ginger, leaf="#4f8a4f")
    files[f"{key}-mark.svg"] = mark_svg(mark_root, colors)
    files[f"{key}-mark-on-dark.svg"] = mark_svg(mark_root, colors)
    files[f"{key}-logo.svg"] = lockup(mark_root, colors, INK)
    files[f"{key}-logo-on-dark.svg"] = lockup(mark_root, colors, MINT)

files["d-leaf-dot-logo.svg"] = word_only(INK, leaf_dot=LEAF)
files["d-leaf-dot-logo-on-dark.svg"] = word_only(MINT, leaf_dot=LEAF_BRIGHT)
# Ways of keeping the ng visible, on the plain wordmark
files["ng-none.svg"] = word_only(INK)
files["ng-colour.svg"] = word_only(INK, ng=TORCH)
files["ng-emerald.svg"] = word_only(INK, ng="#0b7a5c")
files["ng-weight.svg"] = word_only(INK, font=R, ng_weight=B)

for name, svg in files.items():
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)
print(len(files), "files")
