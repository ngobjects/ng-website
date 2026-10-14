"""Articulated ginger roots: knuckles, growth rings and a cut end, added one at a time. Writes roots.html.

Run with a Python that has fonttools and brotli installed: python roots.py
"""
import importlib.util
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("t", os.path.join(HERE, "typefaces.py"))
t = importlib.util.module_from_spec(spec); spec.loader.exec_module(t)
g = t.g

GINGER, RING, CUT, CUT_RIM = "#e5bd66", "#b98a3e", "#f3e6a4", "#d9c56e"
SHOOT = "#4f8a4f"
NEXT_BOLD = next(face for face in t.FACES if face[0].startswith("Atkinson Hyperlegible Next Bold"))


def lobe(x0, y0, r0, x1, y1, r1, steps=28):
    """A tapered capsule: the hull of a circle at each end. r0 is usually the narrow joint, r1 the knobbly end."""
    d = math.hypot(x1 - x0, y1 - y0)
    th = math.atan2(y1 - y0, x1 - x0)
    phi = math.acos(max(-1, min(1, (r0 - r1) / d)))
    pts = []
    for i in range(steps + 1):  # round the far end
        a = th + phi - (2 * phi) * i / steps
        pts.append((x1 + r1 * math.cos(a), y1 + r1 * math.sin(a)))
    for i in range(steps + 1):  # and back round the near end
        a = th - phi - (2 * math.pi - 2 * phi) * i / steps
        pts.append((x0 + r0 * math.cos(a), y0 + r0 * math.sin(a)))
    return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + "Z"


def across(x0, y0, x1, y1, at, half):
    """A short, slightly curved growth ring across the segment from (x0, y0) to (x1, y1), at fraction 'at' along it.
    It covers the middle of the finger only, so the finger never looks cut in two."""
    th = math.atan2(y1 - y0, x1 - x0)
    cx, cy = x0 + (x1 - x0) * at, y0 + (y1 - y0) * at
    h = half * 0.55
    nx, ny = -math.sin(th) * h, math.cos(th) * h
    bx, by = math.cos(th) * h * 0.35, math.sin(th) * h * 0.35  # bow the ring towards the end of the finger
    return f"M{cx - nx:.2f} {cy - ny:.2f} Q{cx + bx:.2f} {cy + by:.2f} {cx + nx:.2f} {cy + ny:.2f}"


def cut_end(x0, y0, x1, y1, r, flesh, rim):
    """The pale, freshly cut face at the (x1, y1) end of a lobe."""
    th = math.degrees(math.atan2(y1 - y0, x1 - x0))
    return (f'<ellipse cx="{x1:.2f}" cy="{y1:.2f}" rx="{r * 0.42:.2f}" ry="{r * 0.92:.2f}" '
            f'transform="rotate({th:.1f} {x1:.2f} {y1:.2f})" fill="{flesh}" stroke="{rim}" stroke-width="1" />')


# The flat root's layout, as lobes: (joint x, y, r), (end x, y, r)
A3_EVEN = [((11, 46, 6.5), (49, 41.5, 6.5)), ((20, 44, 5), (15.5, 30, 5)), ((35, 42.5, 5.5), (40, 26, 5.5)), ((49, 41.5, 4.25), (53.5, 50, 4.25))]
A3_KNUCKLES = [((30, 44, 5.5), (10, 46.5, 7.5)), ((30, 44, 5.5), (49, 40.5, 7)),
               ((19, 43, 3.5), (15, 29, 5.8)), ((36, 41, 3.5), (40.5, 25, 6.3)), ((49, 42, 3.5), (54, 51.5, 4.8))]
# Nubs: (x, y, r), small bumps sitting on the outline
A3_NUBS = [(24.5, 47.5, 2.6), (43.5, 31.5, 2.3), (12.5, 34, 2.2), (6, 44, 2.4)]
# Rings: (lobe index, fraction along it, half length)
A3_RINGS = [(0, 0.45, 7), (1, 0.5, 6.5), (2, 0.55, 4.6), (3, 0.5, 5)]

# A layout traced from the photo: a cut end top left, a finger reaching right above the body,
# the body sprawling right to a big knob, a foot hanging down at the left, small knobs up and down
SPRAWL = [((12, 25, 6), (7, 14.5, 6.5)),       # the cut end, top left
          ((12, 25, 6), (15.5, 54, 5.5)),      # the foot hanging down at the left
          ((15, 20, 4.2), (36, 12, 6)),        # finger reaching right, above the body
          ((15, 31, 5.5), (54, 40, 8.5)),      # the body, big knob at the right
          ((40, 34, 3.4), (44, 25, 4.6)),      # knob growing up from the body
          ((31, 39, 3.4), (29.5, 47.5, 4.2))]  # knob growing down
SPRAWL_RINGS = [(1, 0.5, 5.5), (2, 0.55, 5), (3, 0.35, 6), (3, 0.65, 7)]


def root(lobes, rings=(), cut=None, shoot=None, nubs=(), color=GINGER, mask_id="m"):
    shapes = "".join(f'<path d="{lobe(*a, *b)}" />' for a, b in lobes)
    shapes += "".join(f'<circle cx="{x}" cy="{y}" r="{r}" />' for x, y, r in nubs)
    out = f'<g fill="{color}">{shapes}</g>'
    if rings:
        lines = "".join(f'<path d="{across(*lobes[i][0][:2], *lobes[i][1][:2], at, half)}" />' for i, at, half in rings)
        out += f'<g fill="none" stroke="{RING}" stroke-width="1.4" stroke-linecap="round">{lines}</g>'
    if cut is not None:
        (x0, y0, _), (x1, y1, r) = lobes[cut]
        out += cut_end(x0, y0, x1, y1, r, CUT, CUT_RIM)
    if shoot:
        out += shoot
    return out


A3_SHOOT = ('<path d="M40.5 21 C40 16.5 41.5 13 44 10.5" fill="none" stroke="#4f8a4f" stroke-width="3.4" stroke-linecap="round" />'
            + g.leaf(43.5, 11, 13, 7, 48, SHOOT))
SPRAWL_SHOOT = ('<path d="M45 21.5 C44.8 17.5 46.3 14.5 49 12.5" fill="none" stroke="#4f8a4f" stroke-width="3.2" stroke-linecap="round" />'
                + g.leaf(48.5, 13, 11, 6.5, 50, SHOOT))

VARIANTS = [
    ("A3, as on the site", "Even strokes, for reference.", dict(lobes=A3_EVEN, shoot=A3_SHOOT)),
    ("1 · Knuckles", "Fingers pinch at the joints and swell at the ends.", dict(lobes=A3_KNUCKLES, shoot=A3_SHOOT)),
    ("2 · Knuckles and nubs", "Small bumps on the outline make the silhouette knobbly, without any inner detail.", dict(lobes=A3_KNUCKLES, nubs=A3_NUBS, shoot=A3_SHOOT)),
    ("3 · Knuckles and rings", "Short growth rings in a darker ginger.", dict(lobes=A3_KNUCKLES, rings=A3_RINGS, shoot=A3_SHOOT)),
    ("4 · Knuckles and a cut end", "The pale, fresh cut on the left end, as in the photo.", dict(lobes=A3_KNUCKLES, cut=0, shoot=A3_SHOOT)),
    ("5 · All of it", "Knuckles, nubs, rings and the cut end.", dict(lobes=A3_KNUCKLES, nubs=A3_NUBS, rings=A3_RINGS, cut=0, shoot=A3_SHOOT)),
    ("6 · Sprawl", "A layout traced from the photo: the cut end top left, a finger reaching right, the body sprawling to a big knob.", dict(lobes=SPRAWL, rings=SPRAWL_RINGS, cut=0)),
    ("7 · Sprawl with a shoot", "The same, with the green shoot for colour.", dict(lobes=SPRAWL, rings=SPRAWL_RINGS, cut=0, shoot=SPRAWL_SHOOT)),
]


def mark(n, svg_id, **kw):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{root(mask_id=f"m{n}-{svg_id}", **kw)}</svg>'


def lockup(n, svg_id, text, ng, **kw):
    _, path, axes, tracking = NEXT_BOLD
    size, end, words = t.wordmark_svg(path, axes, tracking, text, ng)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {end + 20:.0f} {size:.0f}">'
            f'<g transform="scale({size / 64:.4f})">{root(mask_id=f"m{n}-{svg_id}", **kw)}</g>{words}</svg>')


rows = []
for n, (name, about, kw) in enumerate(VARIANTS):
    sizes = "".join(f'<div style="width:{s}px;height:{s}px">{mark(n, f"s{s}", **kw)}</div>' for s in (128, 32, 16))
    rows.append(
        f'<section><div class="about"><h2>{name}</h2><p>{about}</p></div>'
        f'<div class="sizes">{sizes}</div>'
        f'<div class="lockup">{lockup(n, "l", g.INK, g.TORCH, **kw)}</div>'
        f'<div class="lockup dark">{lockup(n, "d", g.MINT, g.TURMERIC, **kw)}</div></section>')

page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>engifer roots</title><style>
body { margin: 0; padding: 2rem 1rem 4rem; background: #f5f8f6; color: #121a17; font: 15px/1.5 system-ui, sans-serif; }
main { max-width: 1300px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin: 0 0 .25rem; } h2 { font-size: 1rem; margin: 0; }
.intro { color: #56635c; margin: 0 0 2rem; max-width: 70ch; }
section { display: grid; grid-template-columns: 13rem 15rem 1fr 1fr; gap: 1px; background: #dde6e1; border: 1px solid #dde6e1; border-radius: 10px; overflow: hidden; margin-bottom: 1rem; }
section > div { background: #fff; padding: 1.25rem; }
.about p { color: #56635c; font-size: .85rem; margin: .35rem 0 0; }
.sizes { display: flex; align-items: end; gap: 1rem; }
.lockup { display: flex; align-items: center; justify-content: center; }
.lockup svg { height: 60px; width: auto; }
.dark { background: #074b3c !important; }
svg { display: block; width: 100%; height: 100%; }
</style></head><body><main>
<h1>engifer roots</h1>
<p class="intro">Articulation borrowed from a real hand of ginger, added one step at a time: knuckles, nubs, growth rings, the cut end, and a layout taken from the photo. Marks at 128, 32 and 16 pixels; wordmark in Atkinson Hyperlegible Next Bold.</p>
""" + "".join(rows) + "</main></body></html>\n"

if __name__ == "__main__":
    open(os.path.join(HERE, "roots.html"), "w").write(page)
