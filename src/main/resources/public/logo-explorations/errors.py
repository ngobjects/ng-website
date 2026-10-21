"""Ginger in trouble: the articulated root (variant 5) when something has gone wrong, and inline error messages built on it.
Writes errors.html.

Run with a Python that has fonttools and brotli installed: python errors.py
"""
import importlib.util
import os

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("roots", os.path.join(HERE, "roots.py"))
r = importlib.util.module_from_spec(spec); spec.loader.exec_module(r)
g = r.g

LOBES, NUBS, RINGS = r.A3_KNUCKLES, r.A3_NUBS, r.A3_RINGS
DRY, DRY_RING, DRY_LEAF = "#c79a52", "#96692e", "#9a7a45"
OLIVE = "#7f8a45"
TORCH, TURMERIC, INK, MUTED = "#c41e4a", "#ffb320", "#121a17", "#56635c"


def svg(body, view="2 2 60 60"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}">{body}</svg>'


def stem(d, color=r.SHOOT, width=3.4):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" />'


# ---------- Healthy, for reference ----------

def healthy():
    return svg(r.root(LOBES, RINGS, 0, r.A3_SHOOT, NUBS))


# ---------- Snapped: an error. The root breaks at its middle joint and the halves sag apart, showing fresh fibrous flesh ----------

# The break runs through the joint at (30, 44), a little jagged
BREAK = "30.6 33, 29.2 36.5, 30.8 39.5, 29.4 42.5, 30.9 45.5, 29.5 48.5, 30.5 52, 30 57"


def snapped(sid):
    left_lobes = [LOBES[0], LOBES[2]]
    right_lobes = [LOBES[1], LOBES[3], LOBES[4]]
    left_nubs = [n for n in NUBS if n[0] < 29]
    right_nubs = [n for n in NUBS if n[0] >= 29]

    def half(lobes, nubs, rings, cut, shoot):
        body = r.root(lobes, rings, cut, shoot, nubs)
        return body

    left = half(left_lobes, left_nubs, [(0, 0.45, 7), (1, 0.55, 4.6)], 0, None)
    right = half(right_lobes, right_nubs, [(0, 0.5, 6.5), (1, 0.5, 5)], None, r.A3_SHOOT)
    pts = BREAK.split(", ")
    clip_left = "M0 0 L30.6 0 L" + pts[0] + " L" + " L".join(pts[1:]) + " L0 64Z"
    clip_right = "M64 0 L30.6 0 L" + pts[0] + " L" + " L".join(pts[1:]) + " L64 64Z"
    # The broken faces: pale flesh along the break, with a few fibres sticking out
    face = (f'<path d="M30.6 37.5 L29.6 40 L30.8 42.5 L29.8 45 L30.9 47.5 L30.2 50.5" fill="none" stroke="{r.CUT}" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" />')
    fibres_left = (f'<g stroke="{r.CUT_RIM}" stroke-width="0.8" stroke-linecap="round">'
                   '<path d="M30.4 40.5 l1.8 -0.4" /><path d="M30.6 44.2 l2.2 0.3" /><path d="M30.4 48 l1.6 0.5" /></g>')
    fibres_right = (f'<g stroke="{r.CUT_RIM}" stroke-width="0.8" stroke-linecap="round">'
                    '<path d="M30 42 l-1.8 -0.5" /><path d="M30.2 46.2 l-2 0.4" /></g>')
    return svg(
        f'<defs><clipPath id="l{sid}"><path d="{clip_left}" /></clipPath><clipPath id="r{sid}"><path d="{clip_right}" /></clipPath></defs>'
        f'<g transform="translate(-1.6 0.5) rotate(-9 30 44)"><g clip-path="url(#l{sid})">{left}{face}</g>{fibres_left}</g>'
        f'<g transform="translate(4 0.5) rotate(7 30 44)"><g clip-path="url(#r{sid})">{right}{face}</g>{fibres_right}</g>')


# ---------- Wilted: a warning. The root is fine, the shoot has gone limp and olive ----------

def wilted():
    shoot = (stem("M40.5 21 C40.2 15.5 43.5 12 47 13 C49.5 13.8 50.2 16.5 49.6 19.5", OLIVE)
             + g.leaf(49.4, 19.2, 11, 6, 168, OLIVE))
    return svg(r.root(LOBES, RINGS, 0, shoot, NUBS))


# ---------- Curled: an unknown key. The shoot curls into a question mark ----------

def curled():
    shoot = (stem("M40.5 21 C40.5 18 40.6 16.5 42.2 14.6 C44.6 12 46.8 10.4 46.6 7.4 C46.4 4.2 43.4 3 40.8 3.6 C38.6 4.1 37.4 5.6 37.2 7.4")
             + g.leaf(37.3, 7.2, 7.5, 4.6, 205, r.SHOOT))
    return svg(r.root(LOBES, RINGS, 0, shoot, NUBS), view="2 0 60 62")


# ---------- Shrivelled: expired. Dried out, wrinkled, the leaf gone brown and curled ----------

def shrivelled():
    thin = [((a[0], a[1], a[2] * 0.82), (b[0], b[1], b[2] * 0.8)) for a, b in LOBES]
    wrinkles = [(i, f, h * 0.8) for i in range(len(thin)) for f, h in ((0.3, 5.5), (0.55, 6.5), (0.8, 5))]
    body = r.root(thin, (), 0, None, [(x, y, rr * 0.8) for x, y, rr in NUBS], color=DRY)
    lines = "".join(f'<path d="{r.across(*thin[i][0][:2], *thin[i][1][:2], at, half)}" />' for i, at, half in wrinkles)
    body += f'<g fill="none" stroke="{DRY_RING}" stroke-width="1.1" stroke-linecap="round">{lines}</g>'
    body += stem("M40.5 21.5 C40.3 18.5 41.5 16.5 43.5 16.2", DRY_LEAF, 2.4)
    body += f'<path d="M43.3 16.4 C46.5 14 48.5 15.5 47.4 17.6 C46.6 19 44.8 18.4 45.4 17.2" fill="none" stroke="{DRY_LEAF}" stroke-width="2.2" stroke-linecap="round" />'
    return svg(body)


STATES = [
    ("Healthy", "For reference: variant 5, all of it.", healthy()),
    ("Snapped", "An error. Broken at the middle joint, the halves sag apart, fresh pale flesh and a few fibres at the break.", snapped("s")),
    ("Curled", "Unknown key. The shoot curls into a question mark: it grew, but not where you asked.", curled()),
    ("Wilted", "A warning. The root is fine; the shoot has gone limp and olive. Worth a look, not broken.", wilted()),
    ("Shrivelled", "Expired. A session or page that sat too long: dried, wrinkled, the leaf curled brown.", shrivelled()),
]


# ---------- Inline messages ----------

def box(kind, mark, label, element, message, accent, tint):
    return (f'<span class="ngerr" style="--accent:{accent};--tint:{tint}">'
            f'<span class="ngerr-mark">{mark}</span>'
            f'<span class="ngerr-text"><span class="ngerr-kind">{label}</span> <code class="ngerr-el">{element}</code>'
            f'<span class="ngerr-msg">{message}</span></span></span>')


def chip(mark, element, accent, tint):
    return (f'<span class="ngchip" style="--accent:{accent};--tint:{tint}"><span class="ngchip-mark">{mark}</span>'
            f'<code>{element}</code></span>')


UNKNOWN_KEY = box("unknown", curled(), "Unknown key", "&lt;wo:str&gt;",
                  "While resolving keypath 'user.nmae': Unable to resolve key 'nmae' against class 'app.User'. Did you mean '<b>name</b>'?",
                  TORCH, "#fff1f4")
BINDING = box("error", snapped("b"), "Binding configuration error", "&lt;wo:repetition&gt;",
              "You must bind either [list] or [count]", TORCH, "#fff1f4")
WARNING = box("warning", wilted(), "Deprecated binding", "&lt;wo:link&gt;",
              "[string] is deprecated. Put the link text between the tags instead.", "#a26a00", "#fff8e6")

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>engifer errors</title><style>
@font-face {{ font-family: Inter; font-weight: 400 700; src: url("../../webserver-resources/fonts/inter/inter-400-normal-latin.woff2"); }}
body {{ margin: 0; padding: 2rem 1rem 4rem; background: #f5f8f6; color: {INK}; font: 15px/1.5 Inter, system-ui, sans-serif; }}
main {{ max-width: 1100px; margin: 0 auto; }}
h1 {{ font-size: 1.5rem; margin: 0 0 .25rem; }} h2 {{ font-size: 1.1rem; margin: 2.5rem 0 .25rem; }} h3 {{ font-size: .95rem; margin: 0; }}
.intro, .note {{ color: {MUTED}; max-width: 70ch; margin: 0 0 1.25rem; }}
.sheets {{ display: flex; gap: 1.25rem; margin: 0 0 1.25rem; font-size: .9rem; }} .sheets a {{ color: #0b7a5c; }}
svg {{ display: block; width: 100%; height: 100%; }}
code {{ font-family: "JetBrains Mono", ui-monospace, Menlo, monospace; }}

.states {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap: 1px; background: #dde6e1; border: 1px solid #dde6e1; border-radius: 10px; overflow: hidden; }}
.state {{ background: #fff; padding: 1.25rem; }}
.state .big {{ width: 128px; height: 128px; margin: 0 auto .75rem; }}
.state .small {{ display: flex; gap: .75rem; align-items: end; justify-content: center; margin-bottom: .9rem; }}
.state p {{ color: {MUTED}; font-size: .85rem; margin: .25rem 0 0; }}
.dark .state {{ background: #074b3c; color: #f0f7f3; }} .dark .state p {{ color: #a8d5c0; }}

.demo {{ background: #fff; border: 1px solid #dde6e1; border-radius: 10px; padding: 1.5rem 1.75rem; margin-bottom: 1rem; }}
.demo .label {{ font-size: .75rem; text-transform: uppercase; letter-spacing: .06em; color: {MUTED}; margin: 0 0 .75rem; }}
.fake h2 {{ margin: 0 0 .5rem; font-size: 1.4rem; }}
.fake ul {{ margin: .25rem 0 0; }}

/* The inline message. In a real app it lands in pages with unknown CSS, so it would carry its styles inline and reset what it inherits */
.ngerr {{ display: inline-flex; align-items: flex-start; gap: .65rem; max-width: 36rem; vertical-align: middle; margin: .2rem 0;
	padding: .55rem .8rem .6rem .6rem; border-radius: 8px; background: var(--tint); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent);
	box-shadow: inset 3px 0 0 var(--accent); font: 400 13px/1.45 Inter, system-ui, sans-serif; color: {INK}; text-align: left; letter-spacing: 0; }}
.ngerr-mark {{ flex: none; width: 30px; height: 30px; }}
.ngerr-kind {{ font-weight: 700; color: var(--accent); }}
.ngerr-el {{ font-size: 12px; font-weight: 600; }}
.ngerr-msg {{ display: block; color: #3a4640; }}
.ngerr-msg b {{ font-family: "JetBrains Mono", ui-monospace, Menlo, monospace; font-size: 12px; }}

.ngchip {{ display: inline-flex; align-items: center; gap: .3rem; padding: .05rem .45rem .05rem .2rem; border-radius: 999px; vertical-align: middle;
	background: var(--tint); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent); font: 600 11px/1.6 Inter, sans-serif; color: var(--accent); }}
.ngchip-mark {{ width: 18px; height: 18px; }} .ngchip code {{ font-size: 11px; }}

.expired {{ display: grid; grid-template-columns: 180px 1fr; gap: 2rem; align-items: center; }}
.expired .big {{ width: 180px; height: 180px; }}
.expired h3 {{ font-size: 1.4rem; margin: 0 0 .4rem; }} .expired p {{ color: {MUTED}; margin: 0 0 1rem; max-width: 46ch; }}
.expired a {{ display: inline-block; background: {TURMERIC}; color: {INK}; font-weight: 600; text-decoration: none; padding: .55rem 1.1rem; border-radius: 6px; }}
@media (max-width: 40rem) {{ .expired {{ grid-template-columns: 1fr; }} }}
</style></head><body><main>
<h1>engifer errors</h1>
<nav class="sheets"><a href="index.html">1 · Directions</a> <a href="typefaces.html">2 · Typefaces</a> <a href="roots.html">3 · Roots</a> <a href="errors.html">4 · Errors</a> <a href="wonder-slim.html">5 · wonder-slim</a> <a href="lemongrass.html">6 · Lemongrass</a></nav>
<p class="intro">What does erroneous ginger look like? Four ways a root can be unwell, each matched to a kind of problem, then inline messages built on them, to replace the dog face that ng shows today. A concept only: nothing here is in the framework.</p>

<h2>Ginger in trouble</h2>
<p class="note">At 128, 32 and 20 pixels. The inline messages use them at about 30.</p>
<div class="states">{"".join(f'<div class="state"><div class="big">{s}</div><div class="small"><div style="width:32px;height:32px">{s}</div><div style="width:20px;height:20px">{s}</div></div><h3>{n}</h3><p>{a}</p></div>' for n, a, s in STATES)}</div>
<div class="states dark" style="margin-top:1rem">{"".join(f'<div class="state"><div class="big" style="width:72px;height:72px">{s}</div><h3>{n}</h3></div>' for n, a, s in STATES)}</div>

<h2>Inline, where the error happened</h2>
<p class="note">The message renders in place of the element that failed, so you see it where you'd see the content. Same parts as today: what went wrong, which element, the message.</p>
<div class="demo"><p class="label">Inbox, with <code>$user.nmae</code></p>
<div class="fake"><h2>Hello {UNKNOWN_KEY}</h2></div></div>
<div class="demo"><p class="label">A repetition missing its list</p>
<div class="fake"><p>Your messages:</p>{BINDING}</div></div>
<div class="demo"><p class="label">A warning (made up: ng has no warnings yet). The page still renders</p>
<div class="fake"><p>{WARNING}</p><p><a href="#" style="color:{TORCH}">Lunch on Friday?</a></p></div></div>

<h2>Compact, for tight spots</h2>
<p class="note">Inside a table cell, a button or a line of text, a full message breaks the layout. A chip says where; hovering it, or <code>/ng/dev/problems</code>, says what.</p>
<div class="demo"><div class="fake">
<p>Signed in as {chip(curled(), "user.nmae", TORCH, "#fff1f4")} · <a href="#" style="color:{TORCH}">Sign out</a></p>
<table style="border-collapse:collapse;font-size:14px"><tr><th style="text-align:left;padding:.3rem 1.5rem .3rem 0">Subject</th><th style="text-align:left">Received</th></tr>
<tr><td style="padding:.3rem 1.5rem .3rem 0">Lunch on Friday?</td><td>{chip(snapped("c"), "&lt;wo:str&gt;", TORCH, "#fff1f4")}</td></tr>
<tr><td style="padding:.3rem 1.5rem .3rem 0">Build #412 passed</td><td>{chip(wilted(), "&lt;wo:str&gt;", "#a26a00", "#fff8e6")}</td></tr></table>
</div></div>

<h2>Expired</h2>
<p class="note">Not a programming error, so not dev-only: the page a visitor gets when the page cache or session has let go of what they clicked.</p>
<div class="demo"><div class="expired"><div class="big">{shrivelled()}</div><div>
<h3>This page has dried up</h3><p>It sat too long, and the app let go of it. Start again from the front page.</p><a href="#">Back to the start</a></div></div></div>
</main></body></html>
"""

open(os.path.join(HERE, "errors.html"), "w").write(page)
print("errors.html")
