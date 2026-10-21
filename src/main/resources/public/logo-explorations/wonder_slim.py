"""Logo ideas for wonder-slim, the slimmed down Project Wonder. Writes two sheets:

wonder-slim.html  the first round: marks about the word "slim" (a slimmed W, pruned, carved, a sparkle, folded, a belt, a wordmark)
lemongrass.html   the second round: lemongrass, ginger's partner in the pot, with states for errors like the ginger's

Needs nothing beyond Python itself: python wonder_slim.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

NAV = ('<nav class="sheets"><a href="index.html">1 · Directions</a> <a href="typefaces.html">2 · Typefaces</a> '
       '<a href="roots.html">3 · Roots</a> <a href="errors.html">4 · Errors</a> '
       '<a href="wonder-slim.html">5 · wonder-slim</a> <a href="lemongrass.html">6 · Lemongrass</a></nav>')

INK, PAPER, MUTED = "#16200f", "#f7f6ee", "#55604a"
INDIGO, AMBER = "#3a3fd1", "#e8930c"
LEMON, LEAF, CHILI = "#c9d84a", "#4f7a35", "#b3261e"


def svg(body, view="0 0 100 100"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" aria-hidden="true">{body}</svg>'


# ---------- Round 1: marks about the word ----------

W = "M14 24 L32 78 L50 38 L68 78 L86 24"


def slimmed(thin=4, ghost=0.16):
    return svg(f'<path d="{W}" fill="none" stroke="currentColor" stroke-opacity="{ghost}" stroke-width="20" />'
               f'<path d="{W}" fill="none" stroke="currentColor" stroke-width="{thin}" stroke-linejoin="round" stroke-linecap="round" />')


def slimmed_tiny():
    return svg(f'<path d="{W}" fill="none" stroke="currentColor" stroke-width="13" stroke-linejoin="round" stroke-linecap="round" />')


PRUNED_W = "M22 24 L34 80 L50 42 L66 80 L78 24"
GINGER_LEAF = "M0 0 C5.2 -3.2 3.8 -9.7 0 -13.0 C-3.8 -9.7 -5.2 -3.2 0 0Z"


def pruned(wood="#9a7349", leaf="#4f8a4f", detail=True):
    cut = 'fill="#efdcae" stroke="#c9ad74" stroke-width="0.8"'
    extra = (f'<path d="M24 87 H76" stroke="#c9ad74" stroke-width="2" stroke-linecap="round" />'
             f'<path d="M28 52 L21 46" stroke="{wood}" stroke-width="4.5" />'
             f'<ellipse cx="21" cy="46" rx="2.3" ry="1" transform="rotate(130.6 21 46)" {cut} />') if detail else ""
    return svg(extra
               + f'<path d="M50 42 L50 31" stroke="{wood}" stroke-width="7" />'
               f'<ellipse cx="50" cy="31" rx="3.6" ry="1.5" {cut} />'
               f'<path d="{PRUNED_W}" fill="none" stroke="{wood}" stroke-width="9" stroke-linejoin="round" />'
               f'<ellipse cx="22" cy="24" rx="4.6" ry="1.8" transform="rotate(-12.1 22 24)" {cut} />'
               f'<ellipse cx="78" cy="24" rx="4.6" ry="1.8" transform="rotate(12.1 78 24)" {cut} />'
               f'<path d="{GINGER_LEAF}" transform="translate(75 53) rotate(52) scale(0.95)" fill="{leaf}" />')


def pruned_tiny(wood="#9a7349"):
    return svg(f'<path d="{PRUNED_W}" fill="none" stroke="{wood}" stroke-width="16" stroke-linejoin="round" />')


BLOCK = "M12 20 Q12 14 18 14 H68 L73 19 L70 23 L80 27 L84 25 L88 31 V82 Q88 88 82 88 H18 Q12 88 12 82 Z"


def carved(chips=True):
    w = "M24 32 H33 L40 60 L46 40 H54 L60 60 L67 32 H76 L65 74 H56 L50 54 L44 74 H35 Z"
    c = '<path d="M80 11 L86 8 L84 16 Z M90 17 L95 16 L92 22 Z M76 5 L80 4 L78 8 Z" fill="currentColor" />' if chips else ""
    return svg(f'<path d="{BLOCK} {w}" fill="currentColor" fill-rule="evenodd" />' + c)


def carved_tiny():
    return svg('<path d="M12 20 Q12 14 18 14 H82 Q88 14 88 20 V82 Q88 88 82 88 H18 Q12 88 12 82 Z '
               'M20 28 H35 L40 52 L44 36 H56 L60 52 L65 28 H80 L67 78 H54 L50 62 L46 78 H33 Z" fill="currentColor" fill-rule="evenodd" />')


def sparkle(spark=AMBER):
    return svg('<path d="M50 4 C51.5 36 54 46 64 50 C54 54 51.5 64 50 96 C48.5 64 46 54 36 50 C46 46 48.5 36 50 4 Z" fill="currentColor" />'
               f'<path d="M74 12 C74.6 21 75.5 23 79 24 C75.5 25 74.6 27 74 36 C73.4 27 72.5 25 69 24 C72.5 23 73.4 21 74 12 Z" fill="{spark}" />')


def sparkle_tiny():
    return svg('<path d="M50 2 C53 32 58 44 74 50 C58 56 53 68 50 98 C47 68 42 56 26 50 C42 44 47 32 50 2 Z" fill="currentColor" />')


def folded(shade=0.5):
    def panel(points, opacity=1):
        return f'<polygon points="{points}" fill="currentColor" fill-opacity="{opacity}" />'
    return svg(panel("26,78 38,78 56,22 44,22", shade) + panel("62,78 74,78 92,22 80,22", shade)
               + panel("8,22 20,22 38,78 26,78") + panel("44,22 56,22 74,78 62,78"))


def belt(buckle=AMBER):
    holes = "".join(f" M{x - 1.8} 50 a1.8 1.8 0 1 0 3.6 0 a1.8 1.8 0 1 0 -3.6 0 Z" for x in (48, 58, 68))
    return svg(f'<path d="M8 44 Q8 42 10 42 H84 L93 50 L84 58 H10 Q8 58 8 56 Z{holes} M75 50 a3.4 2 0 1 0 6.8 0 a3.4 2 0 1 0 -6.8 0 Z" fill="currentColor" fill-rule="evenodd" />'
               f'<rect x="13" y="35" width="18" height="30" rx="4" fill="none" stroke="{buckle}" stroke-width="4" />'
               f'<path d="M15 50 H39" stroke="{buckle}" stroke-width="3.5" stroke-linecap="round" />')


def belt_tiny(buckle=AMBER):
    return svg(f'<path d="M4 36 H82 L97 50 L82 64 H4 Z" fill="currentColor" />'
               f'<rect x="12" y="28" width="22" height="44" rx="6" fill="none" stroke="{buckle}" stroke-width="10" />')


def wordmark(slim_color=INDIGO):
    return f'<span class="wm"><b>wonder</b><i style="color:{slim_color}">slim</i></span>'


# (name, the idea, big mark, small marks at 64/32/16, mark on dark)
IDEAS = [
    ("1 · Slimmed", "The same W, minus the weight: the old Wonder as a ghost, the slim one drawn through it.",
     slimmed(), (slimmed(6), slimmed(9), slimmed_tiny()), slimmed(7, 0.2)),
    ("2 · Pruned", "Cut back, and growing better for it. A W of branches with fresh cuts, and one new leaf in engifer's green.",
     pruned(), (pruned(detail=False), pruned_tiny(), pruned_tiny()), pruned("#c49a68", "#6fae6a", False)),
    ("3 · Carved", "Made by taking away: a block with the W cut out of it, chips flying off.",
     carved(), (carved(), carved(False), carved_tiny()), carved()),
    ("4 · Slim sparkle", "Still a wonder, just narrower. Works best of all as a favicon.",
     sparkle(), (sparkle(), sparkle_tiny(), sparkle_tiny()), sparkle("#ffb320")),
    ("5 · Folded", "Everything it needs, packed small: the W as a folded strip.",
     folded(), (folded(), folded(), folded(0.55)), folded(0.45)),
    ("6 · Belt", "Three notches tighter. The silly one.",
     belt(), (belt(), belt_tiny(), belt_tiny()), belt("#ffb320")),
]


# ---------- Round 2: lemongrass ----------

# The stalk is drawn upright, its cut end at the origin, then leaned into the square like the ginger
LEAN = "translate(16 58) rotate(28) scale(0.68)"
LEAF_UP = '<path d="M-3.5 -46 C-3 -60 -1.5 -72 0.5 -84 C1.5 -72 2.5 -60 3.5 -46 Z" fill="{c}" />'
LEAF_ARCH = '<path d="M-0.5 -46 C3.5 -58 10 -66 18 -70 C11 -64 6.5 -56 3.8 -46 Z" fill="{c}" />'
LEAF_LEFT = '<path d="M-3.8 -44 C-6.5 -51 -8.5 -56 -11 -62 L-8.8 -63 C-6.6 -57.5 -4.6 -53 -1.4 -46 Z" fill="{c}" />'
BULB = '<path d="M-5 0 C-6.6 -4 -6.6 -10 -5 -16 L5 -16 C6.6 -10 6.6 -4 5 0 Z" fill="{c}" stroke="{s}" stroke-width="0.6" />'
TINGE = '<path d="M-6 -3 C-6.3 -5 -6.3 -7 -6 -9 L6 -9 C6.3 -7 6.3 -5 6 -3 Z" fill="#c98fa6" fill-opacity="0.45" />'
CUT_END = '<ellipse cx="0" cy="0" rx="5" ry="1.5" fill="{c}" />'
PEEL = ('<path d="M-5 -14 C-6 -22 -7.6 -28 -11 -33 C-12.2 -34.2 -11.8 -31.5 -10.8 -30.2 C-8.4 -26 -6.6 -21 -4.7 -18.5 Z" '
        'fill="{c}" stroke="{s}" stroke-width="0.5" />')
SHEATHS = '<path d="M-2 -16 L-1.6 -46 M2.2 -16 L1.8 -46" fill="none" stroke="{c}" stroke-width="0.6" />'
STALK = '<path d="M-5 -16 L-4 -46 L4 -46 L5 -16 Z" fill="{c}" stroke="{s}" stroke-width="0.6" stroke-linejoin="round" />'

LEAVES = LEAF_UP.format(c="#8fb05e") + LEAF_ARCH.format(c="#6f9647") + LEAF_LEFT.format(c="#9bb86a")
BASE = BULB.format(c="#efe7c8", s="#c9bb84") + TINGE + CUT_END.format(c="#e3d4a2")
FRESH_PEEL = PEEL.format(c="#e6dfae", s="#c2b574")


def lean(body):
    return svg(f'<g transform="{LEAN}">{body}</g>', "0 0 64 64")


def fresh():
    return lean(LEAVES + STALK.format(c="#cfd68f", s="#a9b866") + SHEATHS.format(c="#aebb68") + BASE
                + '<ellipse cx="0" cy="0" rx="2.8" ry="0.8" fill="none" stroke="#c4ad70" stroke-width="0.5" />' + FRESH_PEEL)


def peeled():
    """Success: the tough outer layers are off and lie beside it, the core paler and slimmer"""
    core = ('<path d="M-4.4 -16 L-3.6 -46 L3.6 -46 L4.4 -16 Z" fill="#dfe3a6" stroke="#b3c06e" stroke-width="0.6" stroke-linejoin="round" />'
            '<path d="M-1.6 -16 L-1.3 -46 M1.8 -16 L1.5 -46" fill="none" stroke="#c3cc84" stroke-width="0.5" />'
            '<path d="M-4.6 0 C-6 -4 -6 -10 -4.4 -16 L4.4 -16 C6 -10 6 -4 4.6 0 Z" fill="#f5f0d8" stroke="#cfc390" stroke-width="0.6" />'
            '<path d="M-5.6 -3 C-5.9 -5 -5.9 -7 -5.6 -9 L5.6 -9 C5.9 -7 5.9 -5 5.6 -3 Z" fill="#c98fa6" fill-opacity="0.4" />'
            '<ellipse cx="0" cy="0" rx="4.6" ry="1.4" fill="#e9dcae" />')
    strips = ('<path d="M33 59 C39 56.5 47 57.5 54 54.5 C51 58.5 42 60.5 33 60.5 Z" fill="#e6dfae" stroke="#c2b574" stroke-width="0.5" />'
              '<path d="M39 62.5 C45 61 50.5 61.5 57 59 C53.5 62.5 46 63.5 39 63.5 Z" fill="#dcd49c" stroke="#c2b574" stroke-width="0.5" />')
    return svg(f'<g transform="{LEAN}">{LEAVES}{core}</g>{strips}', "0 0 64 64")


def bruised():
    """A warning: knocked about, the aroma escaping"""
    marks = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#8a6a32" fill-opacity="{o}" />'
                    for x, y, rx, ry, o in ((-1, -25, 1.6, 3.2, 0.45), (2, -37, 1.2, 2.5, 0.4), (-2.4, -41, 0.8, 1.6, 0.35)))
    aroma = "".join(f'<path d="{d}" fill="none" stroke="{AMBER}" stroke-width="1.6" stroke-linecap="round" />'
                    for d in ("M42 47 q2.5 -2.5 0 -5 q-2.5 -2.5 0 -5 q2.5 -2.5 0 -5", "M49 51 q2.5 -2.5 0 -5 q-2.5 -2.5 0 -5"))
    body = LEAVES + STALK.format(c="#cfd68f", s="#a9b866") + SHEATHS.format(c="#aebb68") + marks + BASE + FRESH_PEEL
    return svg(f'<g transform="{LEAN}">{body}</g>{aroma}', "0 0 64 64")


# The break runs across the stalk a little above the middle, jagged; the top folds over, held by its fibres
JAG_LOW = "L-3 -29.8 L-1.5 -31.4 L0 -29.9 L1.5 -31.3 L3 -29.8 L4.5 -31"
JAG_HIGH = "L-3 -32.3 L-1.5 -30.7 L0 -32.1 L1.5 -30.8 L3 -32.3 L4.5 -31"
BREAK_FACE = 'fill="none" stroke="#f4f0cf" stroke-width="1.1" stroke-linejoin="round" stroke-linecap="round"'


def snapped():
    """An error: folded over at a jagged break"""
    top = (LEAVES
           + f'<path d="M-4.5 -31 {JAG_HIGH} L4 -46 L-4 -46 Z" fill="#cfd68f" stroke="#a9b866" stroke-width="0.6" stroke-linejoin="round" />'
           '<path d="M-1.8 -31.8 L-1.6 -46 M2 -31.8 L1.8 -46" fill="none" stroke="#aebb68" stroke-width="0.6" />'
           f'<path d="M-4.5 -31 {JAG_HIGH}" {BREAK_FACE} />')
    bottom = (f'<path d="M-5 -16 L-4.5 -31 {JAG_LOW} L5 -16 Z" fill="#cfd68f" stroke="#a9b866" stroke-width="0.6" stroke-linejoin="round" />'
              '<path d="M-2 -16 L-1.8 -30.4 M2.2 -16 L2 -30.4" fill="none" stroke="#aebb68" stroke-width="0.6" />'
              f'<path d="M-4.5 -31 {JAG_LOW}" {BREAK_FACE} />'
              '<path d="M3 -30 l0.4 -3.6 M1.5 -31.2 l-0.2 -3 M4.3 -30.8 l0.9 -2.8 M0 -30 l-0.6 -2.2" fill="none" stroke="#d6cc8e" stroke-width="0.5" stroke-linecap="round" />')
    return lean(f'<g transform="rotate(-65 -4.5 -31)">{top}</g>' + bottom + BASE + FRESH_PEEL)


def dried():
    """Expired: straw-coloured, the leaves drooping"""
    leaves = ('<path d="M-3.5 -46 C-3 -58 -2 -66 0 -70 C3 -72.5 6.5 -71.5 8.5 -68 C5.5 -69.5 3.2 -68.5 2.2 -64 C2.6 -58 3 -52 3.5 -46 Z" fill="#c9a865" />'
              '<path d="M-0.5 -46 C4 -54 9 -55.5 13 -49 C9.5 -51.5 6.2 -50.5 3.8 -44 Z" fill="#b8934f" />'
              + LEAF_LEFT.format(c="#d4b878"))
    return lean(leaves + STALK.format(c="#dcc890", s="#b9a468")
                + '<path d="M-2 -16 L-1.6 -46 M2.2 -16 L1.8 -46 M0 -20 L0.2 -42" fill="none" stroke="#c2ad72" stroke-width="0.5" />'
                + BULB.format(c="#ebdfb8", s="#c9b98a") + CUT_END.format(c="#dccb98") + PEEL.format(c="#d4be86", s="#b9a468"))


def rings():
    """The cut end, for sizes where the stalk is too thin to read"""
    layers = [(32, 32, 29, "#6f9647", 0), (32.4, 31.8, 24.5, "#a9c06c", 0.35), (32.8, 31.5, 19.5, "#cfd68f", 0.3),
              (33, 31.4, 14.5, "#e2e2a6", 0.25), (33.2, 31.3, 9.5, "#ece8bf", 0.22), (33.3, 31.2, 5, "#f5f1d9", 0.2)]
    body = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"' + (f' stroke="#5f8540" stroke-opacity="{o}" stroke-width="0.6"' if o else "") + " />"
                   for x, y, r, c, o in layers)
    return svg(body + '<circle cx="33.3" cy="31.2" r="1.8" fill="#e5d8a4" />', "0 0 64 64")


# engifer's ginger (variant 5), for the family picture
GINGER = svg(
    '<g fill="#e5bd66"><path d="M9.8 39.0 L7.1 39.5 L4.7 41.1 L3.1 43.3 L2.5 46.0 L2.8 48.7 L4.1 51.2 L6.2 53.0 L8.9 53.9 L11.6 53.8 L31.2 49.3 L32.8 48.6 L34.2 47.5 L35.1 45.9 L35.5 44.2 L35.2 42.4 L34.4 40.8 L33.2 39.5 L31.6 38.7 L29.8 38.5Z" />'
    '<path d="M20.7 28.3 L20.0 26.2 L18.6 24.5 L16.7 23.4 L14.5 23.2 L12.3 23.8 L10.6 25.1 L9.5 27.1 L9.2 29.3 L9.7 31.4 L15.8 44.4 L16.4 45.3 L17.3 46.0 L18.3 46.4 L19.4 46.4 L20.4 46.1 L21.3 45.5 L22.0 44.7 L22.4 43.6 L22.4 42.5Z" />'
    '<circle cx="24.5" cy="47.5" r="2.6" /><circle cx="12.5" cy="34" r="2.2" /><circle cx="6" cy="44" r="2.4" /></g>'
    '<g fill="none" stroke="#b98a3e" stroke-width="1.4" stroke-linecap="round"><path d="M21.4 48.9 Q19.6 45.2 20.5 41.3" /><path d="M14.3 36.0 Q16.5 34.4 19.2 34.6" /></g>'
    '<ellipse cx="10.0" cy="46.5" rx="3.1" ry="6.9" transform="rotate(172.9 10.0 46.5)" fill="#f3e6a4" stroke="#d9c56e" stroke-width="1" />'
    '<g fill="#e5bd66"><path d="M49.7 47.4 L52.1 46.7 L54.2 45.1 L55.5 43.0 L56.0 40.5 L55.5 38.0 L54.2 35.8 L52.1 34.2 L49.7 33.5 L47.2 33.7 L28.5 38.6 L26.9 39.4 L25.6 40.6 L24.7 42.2 L24.5 44.0 L24.8 45.8 L25.7 47.4 L27.0 48.6 L28.7 49.3 L30.5 49.4Z" />'
    '<path d="M46.1 27.7 L46.7 25.3 L46.4 22.9 L45.2 20.8 L43.3 19.3 L41.0 18.7 L38.6 18.9 L36.4 20.1 L34.9 22.0 L34.2 24.3 L32.5 40.6 L32.5 41.7 L32.9 42.7 L33.6 43.5 L34.5 44.1 L35.5 44.4 L36.6 44.4 L37.6 44.0 L38.5 43.4 L39.1 42.5Z" />'
    '<path d="M49.5 53.2 L50.4 54.7 L51.8 55.8 L53.6 56.2 L55.4 56.0 L56.9 55.2 L58.1 53.8 L58.7 52.2 L58.6 50.4 L57.9 48.7 L51.8 40.0 L51.1 39.2 L50.1 38.6 L49.0 38.5 L47.8 38.6 L46.8 39.2 L46.1 40.0 L45.6 41.0 L45.5 42.1 L45.7 43.2Z" />'
    '<circle cx="43.5" cy="31.5" r="2.3" /></g>'
    '<g fill="none" stroke="#b98a3e" stroke-width="1.4" stroke-linecap="round"><path d="M38.8 38.7 Q40.7 42.0 40.1 45.7" /><path d="M35.6 32.2 Q38.5 32.0 40.9 33.7" /></g>'
    '<path d="M40.5 21 C40 16.5 41.5 13 44 10.5" fill="none" stroke="#4f8a4f" stroke-width="3.4" stroke-linecap="round" />'
    f'<path d="{GINGER_LEAF}" fill="#4f8a4f" transform="translate(43.5 11) rotate(48)" />', "2 2 60 60")

STATES = [
    ("Fresh", "The mark. One outer layer already lifting off.", fresh(), ""),
    ("Peeled", "Success, all clean. The tough layers lie beside it.", peeled(), ""),
    ("Bruised", "A warning. Still works, but something got knocked.", bruised(), "warn"),
    ("Snapped", "An error. Folded over, held by its fibres.", snapped(), "err"),
    ("Dried out", "Expired: the session timed out, the page is gone.", dried(), "dry"),
]


# ---------- The pages ----------

CSS = """
@font-face { font-family: Inter; font-weight: 400 700; src: url("../../webserver-resources/fonts/inter/inter-400-normal-latin.woff2"); }
@font-face { font-family: "DM Sans"; font-weight: 100 1000; src: url("fonts/DMSans.ttf"); }
body { margin: 0; padding: 2rem 1rem 4rem; background: %(paper)s; color: %(ink)s; font: 15px/1.5 Inter, system-ui, sans-serif; }
main { max-width: 1100px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin: 0 0 .25rem; } h2 { font-size: 1.1rem; margin: 2.5rem 0 .25rem; } h3 { font-size: .95rem; margin: 0; }
.intro, .note { color: %(muted)s; max-width: 70ch; margin: 0 0 1.25rem; } .intro a { color: #0b7a5c; }
.sheets { display: flex; flex-wrap: wrap; gap: .25rem 1.25rem; margin: 0 0 1.25rem; font-size: .9rem; } .sheets a { color: #0b7a5c; }
svg { display: block; width: 100%%; height: 100%%; }
code { font-family: "JetBrains Mono", ui-monospace, Menlo, monospace; }

.wm { font-family: "DM Sans", sans-serif; line-height: 1; white-space: nowrap; letter-spacing: -.01em; }
.wm b { font-weight: 900; } .wm i { font-style: normal; font-weight: 200; }

.ideas { display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 1rem; }
.idea { background: #fff; border: 1px solid #e3e1d2; border-radius: 10px; padding: 1.25rem; color: %(indigo)s; }
.idea h3, .idea p { color: %(ink)s; } .idea p { color: %(muted)s; font-size: .85rem; margin: .25rem 0 1rem; }
.idea .big { width: 180px; height: 180px; margin: 0 auto 1rem; }
.sizes { display: flex; align-items: end; gap: 1rem; margin-bottom: 1rem; }
.tile { display: flex; align-items: center; gap: .75rem; padding: .8rem 1rem; border-radius: 8px; background: %(ink)s; color: %(paper)s; }
.tile .m { width: 40px; height: 40px; flex: none; } .tile .wm { font-size: 26px; }
.wordmarks { display: grid; gap: 1.5rem; background: #fff; border: 1px solid #e3e1d2; border-radius: 10px; padding: 1.5rem 1.75rem; }
.wordmarks .wm { font-size: clamp(40px, 9vw, 88px); display: block; }
.ramp b { font-weight: 900; }

.mark { display: grid; grid-template-columns: minmax(0, 320px) 1fr; gap: 2rem; align-items: center; background: #fff; border: 1px solid #e3e1d2; border-radius: 10px; padding: 1.5rem; }
.mark .side { display: grid; gap: 1rem; }
.lockup { display: flex; align-items: center; gap: .75rem; padding: .9rem 1.1rem; border-radius: 10px; border: 1px solid #e3e1d2; }
.lockup .m { width: 60px; height: 60px; flex: none; } .lockup .wm { font-size: 34px; }
.lockup.dark { background: %(ink)s; color: %(paper)s; border-color: %(ink)s; }
.label { font-size: .75rem; text-transform: uppercase; letter-spacing: .06em; color: %(muted)s; margin: 0 0 .4rem; }
@media (max-width: 44rem) { .mark { grid-template-columns: 1fr; } }

.states { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 1rem; }
.state { background: #fff; border: 1px solid #e3e1d2; border-radius: 10px; padding: 1.25rem; text-align: center; }
.state.warn { background: #fff8e8; border-color: #f0d9a0; } .state.err { background: #fdecea; border-color: #efb7ae; } .state.dry { background: #f3efe2; border-color: #ddd3b5; }
.state .big { width: 150px; height: 150px; margin: 0 auto .75rem; }
.state p { color: %(muted)s; font-size: .85rem; margin: .25rem 0 0; }

.demo { background: #fff; border: 1px solid #e3e1d2; border-radius: 10px; padding: 1.5rem 1.75rem; margin-bottom: 1rem; }
.fake { font: 17px/1.5 Georgia, serif; color: #3a4232; } .fake h3 { font: 800 1.4rem/1.2 "DM Sans", sans-serif; color: %(ink)s; margin: 0 0 .4rem; }

/* The inline message, loud like ng's: it must not pass for part of the page */
.slimerr { all: initial; position: relative; display: inline-flex; align-items: stretch; max-width: 34rem; margin: 22px 18px 6px 4px; vertical-align: middle;
	box-sizing: border-box; border-radius: 6px; background: %(chili)s; border: 2px solid %(ink)s; box-shadow: 4px 4px 0 %(ink)s;
	font: 400 13px/1.45 -apple-system, "Segoe UI", Helvetica, Arial, sans-serif; color: #fff; text-align: left; }
.slimerr .stripe { flex: none; width: 10px; border-radius: 4px 0 0 4px; background: repeating-linear-gradient(-45deg, %(lemon)s 0 6px, %(ink)s 6px 12px); }
.slimerr .m { position: absolute; top: -30px; right: -18px; width: 48px; height: 48px; transform: rotate(8deg); filter: drop-shadow(2px 2px 0 %(ink)s); }
.slimerr .text { padding: 7px 36px 8px 12px; } .slimerr b { font-weight: 700; }
.slimerr code { font: 700 12px/1.45 ui-monospace, Menlo, monospace; color: #f6e27a; } .slimerr .msg { display: block; }

.chips { display: flex; flex-wrap: wrap; gap: .75rem; align-items: center; }
.chip { display: inline-flex; align-items: center; gap: .5rem; padding: .3rem .9rem .3rem .4rem; border-radius: 999px; font-size: .9rem; }
.chip .m { width: 28px; height: 28px; } .chip.warn { background: #fff3d6; border: 1px solid #e8b44a; } .chip.ok { background: #eef3dc; border: 1px solid #b7c97a; }
.bar { display: inline-flex; align-items: center; gap: .6rem; padding: .5rem .9rem; border-radius: 8px; background: %(ink)s; color: %(paper)s; font-size: .9rem; }
.bar .m { width: 26px; height: 26px; } .bar a { color: %(lemon)s; }

.expired { display: grid; grid-template-columns: 150px 1fr; gap: 2rem; align-items: center; }
.expired .big { width: 150px; height: 150px; }
.expired h3 { font: 800 1.5rem/1.2 "DM Sans", sans-serif; margin: 0 0 .4rem; } .expired p { color: %(muted)s; margin: 0 0 1rem; max-width: 46ch; }
.expired a { display: inline-block; background: %(ink)s; color: %(paper)s; font-weight: 600; text-decoration: none; padding: .55rem 1.1rem; border-radius: 6px; }
@media (max-width: 40rem) { .expired { grid-template-columns: 1fr; } }

.family { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; }
.family > div { display: flex; justify-content: center; align-items: end; gap: 2.5rem; padding: 1.75rem 1rem; border-radius: 10px; background: #fff; border: 1px solid #e3e1d2; }
.family .dark { background: %(ink)s; border-color: %(ink)s; color: #c9cfb8; }
.family figure { margin: 0; display: grid; justify-items: center; gap: .6rem; } .family .m { width: 130px; height: 130px; }
.family .wm { font-size: 28px; } .family figcaption { font-size: .85rem; }
.family .engifer { font: 800 28px/1 "DM Sans", sans-serif; color: %(ink)s; } .family .engifer span { color: #c41e4a; }
""" % dict(paper=PAPER, ink=INK, muted=MUTED, indigo=INDIGO, chili=CHILI, lemon=LEMON)


def page(title, body):
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{title}</title><style>{CSS}</style></head><body><main>\n{body}\n</main></body></html>\n')


def sized(mark, px):
    return f'<div style="width:{px}px;height:{px}px">{mark}</div>'


def idea(name, text, big, small, dark):
    return (f'<div class="idea"><h3>{name}</h3><p>{text}</p><div class="big">{big}</div>'
            f'<div class="sizes">{"".join(sized(m, px) for m, px in zip(small, (64, 32, 16)))}</div>'
            f'<div class="tile"><div class="m">{dark}</div>{wordmark("#f7f6ee")}</div></div>')


RAMP = "".join(f'<span style="font-weight:{w}{";color:" + INDIGO if i > 5 else ""}">{c}</span>'
               for i, (c, w) in enumerate(zip("wonderslim", (900, 800, 700, 600, 500, 400, 300, 250, 200, 200))))

ROUND_1 = f"""<h1>wonder-slim, first ideas</h1>
{NAV}
<p class="intro">wonder-slim has no logo. Its README says it improves Project Wonder "not by adding stuff but by <em>removing</em> stuff", so this first round is about the word: slim, cut back, carved, folded, tightened. Each at 180, 64, 32 and 16 pixels, and on dark with the wordmark. The verdict: nice, but generic, without the character the ginger gives engifer. That led to <a href="lemongrass.html">lemongrass</a>.</p>

<h2>Marks</h2>
<div class="ideas">{"".join(idea(*i) for i in IDEAS)}</div>

<h2>7 · Wordmark</h2>
<p class="note">Let the type lose the weight: heavy "wonder", hairline "slim". Or slimming as you read. Any of the marks can sit beside either.</p>
<div class="wordmarks"><div><p class="label">Heavy and hairline</p>{wordmark()}</div>
<div><p class="label">Slimming as you read</p><span class="wm">{RAMP}</span></div></div>
"""

LOCKUP_LIGHT = f'<div class="lockup"><div class="m">{fresh()}</div>{wordmark(LEAF)}</div>'
LOCKUP_DARK = f'<div class="lockup dark"><div class="m">{fresh()}</div>{wordmark(LEMON)}</div>'

ROUND_2 = f"""<h1>wonder-slim, lemongrass</h1>
{NAV}
<p class="intro">Lemongrass is ginger's partner in the pot, in Thai and Vietnamese cooking, curry pastes and tea, the way wonder-slim and engifer go together. And preparing it is slim's story: strip the tough outer layers and cut off the dry top to get to the tender core. Like the ginger, a stalk can be in trouble in ways that fit kinds of problems. A concept only.</p>

<h2>The stalk</h2>
<p class="note">Leaning like the ginger: a pale bulb with a purple band, layered sheaths, three leaves, one outer layer peeling away. At 16 pixels the stalk is a thin line, so the cut end, its rings, takes over at favicon sizes.</p>
<div class="mark"><div>{fresh()}</div><div class="side">{LOCKUP_DARK}{LOCKUP_LIGHT}
<div><p class="label">The stalk, shrinking</p><div class="sizes">{"".join(sized(fresh(), px) for px in (64, 32, 16))}</div></div>
<div><p class="label">Cut end, for favicons</p><div class="sizes">{"".join(sized(rings(), px) for px in (64, 32, 16))}</div></div></div></div>

<h2>Everything that can happen to a stalk</h2>
<div class="states">{"".join(f'<div class="state {cls}"><div class="big">{s}</div><h3>{n}</h3><p>{a}</p></div>' for n, a, s, cls in STATES)}</div>

<h2>In use</h2>
<p class="note">Mockups: the messages are made up. The inline error is as loud as ng's, so it can't pass for part of the page, in chili red, the third thing in the pot.</p>
<div class="demo"><div class="fake"><h3>Members</h3>Signed in as
<span class="slimerr"><span class="stripe"></span><span class="m">{snapped()}</span><span class="text"><b>Unknown key</b> <code>&lt;wo:WOString&gt;</code><span class="msg">Couldn't resolve 'nmae' on Person. Did you mean 'name'?</span></span></span>
and last seen on Tuesday.</div></div>
<div class="demo"><div class="chips">
<span class="chip warn"><span class="m">{bruised()}</span><span><b>Slow page:</b> Main took 2.4 s to render</span></span>
<span class="chip ok"><span class="m">{peeled()}</span><span><b>All clean:</b> no problems on this page</span></span>
<span class="bar"><span class="m">{snapped()}</span><span>3 problems on this page, <a href="#">show them</a></span></span></div></div>
<div class="demo"><div class="expired"><div class="big">{dried()}</div><div>
<h3>This page has dried out</h3><p>You were away for a while, and the page you were on has expired.</p><a href="#">Start again</a></div></div></div>

<h2>With the ginger</h2>
<p class="note">Two things that go in the same pot.</p>
<div class="family"><div><figure><div class="m">{GINGER}</div><figcaption class="engifer">e<span>ng</span>ifer</figcaption></figure>
<figure><div class="m">{fresh()}</div><figcaption>{wordmark(LEAF)}</figcaption></figure></div>
<div class="dark"><figure><div class="m">{snapped()}</div><figcaption>wonder-slim, broken</figcaption></figure>
<figure><div class="m">{dried()}</div><figcaption>wonder-slim, expired</figcaption></figure></div></div>
"""

for name, title, body in (("wonder-slim.html", "wonder-slim, first ideas", ROUND_1), ("lemongrass.html", "wonder-slim, lemongrass", ROUND_2)):
    open(os.path.join(HERE, name), "w").write(page(title, body))
    print(name)
