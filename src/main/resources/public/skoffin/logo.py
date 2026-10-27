"""Writes logo.html: the Skoffín brand concept, from the marks in marks.py. Plain Python: python logo.py"""
import os

import marks as m

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.html")

MOODS = [
    ("content", "Content", "The mark. A sly grin: it knows something you don't."),
    ("delighted", "Delighted", "Success, all clear, a new release. All teeth."),
    ("wary", "Wary", "A warning. Hackles up, eyes wide: something's off, but it still works."),
    ("stare", "The stare", "An error. In the stories its glare kills; here it only kills the render."),
    ("asleep", "Asleep", "Expired. It dozed off waiting for you, one fang showing."),
]

symbols = "".join(f'<symbol id="h-{k}" viewBox="0 0 64 64">{m.head(k)}</symbol>' for k, _, _ in MOODS)
symbols += f'<symbol id="tail" viewBox="0 0 64 64">{m.tail()}</symbol>'
symbols += f'<symbol id="tail-on-fox" viewBox="0 0 64 64">{m.tail(m.FUR, m.BONE, "#fff", m.BONE)}</symbol>'


def use(ref, cls="mark", label=None):
    a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg class="{cls}" {a}><use href="#{ref}" /></svg>'


def sized(ref, px):
    return f'<div style="width: {px}px; height: {px}px">{use(ref)}</div>'


def tile(ref, title, text, sizes=(32, 20)):
    small = "".join(sized(ref, s) for s in sizes)
    return (f'<div class="tile"><div class="big">{use(ref)}</div><div class="small">{small}</div>'
            f'<h3>{title}</h3><p>{text}</p></div>')


WORD = 'Skoff<span class="ki">í</span>n'
def tailword(ref="tail"):
    return f'<span class="tailword">{use(ref)}<span>koff<span class="ki">í</span>n</span></span>'


TAILWORD = tailword()


def box(cls, ref, label, element, message):
    return (f'<span class="ngerr {cls}"><span class="ngerr-mark">{use(ref)}</span><span class="ngerr-text">'
            f'<span class="ngerr-kind">{label}</span> <code class="ngerr-el">{element}</code>'
            f'<span class="ngerr-msg">{message}</span></span></span>')


def chip(cls, ref, text):
    return f'<span class="ngchip {cls}"><span class="ngchip-mark">{use(ref)}</span>{text}</span>'


SWATCHES = [("Night", "#0e0b12"), ("Fur", "#1a1422"), ("Bruise", "#33283f"), ("Blood", "#c81e3a"), ("Clot", "#5e0f22"),
            ("Venom", "#b8f53c"), ("Bone", "#ece6d6"), ("Ash", "#efedf2"), ("Silver", "#aab3bd"), ("The stare, errors", "#ff2a3c")]

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Skoffín</title>
<meta name="description" content="Skoffín: a brand concept for a component-based Java web framework, after the Icelandic cat-fox of folklore.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,400..800,0..100&family=Figtree:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;600&display=swap">
<style>
:root {{
	--night: #0e0b12;
	--fur: #1a1422;
	--blood: #c81e3a;
	--clot: #5e0f22;
	--bone: #ece6d6;
	--venom: #b8f53c;
	--silver: #aab3bd;
	--ash: #efedf2;
	--line: #ddd8e3;
	--muted: #5c5666;
	--stare: #c8102e;
	--warn: #6f6a00;
}}

* {{ box-sizing: border-box; }}

body {{
	margin: 0;
	padding: 2rem 1rem 4rem;
	background: var(--ash);
	color: var(--night);
	font: 16px/1.55 "Figtree", system-ui, sans-serif;
}}

main {{ max-width: 1100px; margin: 0 auto; }}

h1, h2, h3, .word {{ font-family: "Fraunces", Georgia, serif; font-variation-settings: "SOFT" 100, "opsz" 144; font-weight: 650; }}
h2 {{ font-size: 1.5rem; margin: 3rem 0 .25rem; letter-spacing: -.01em; }}
h3 {{ font-size: 1.1rem; margin: 0; }}

.intro, .note {{ color: var(--muted); max-width: 68ch; margin: 0 0 1.25rem; }}
.sheets {{ display: flex; flex-wrap: wrap; gap: .5rem 1.25rem; margin: 0 0 1.5rem; font-size: .9rem; }}
a {{ color: #a3162b; }}

svg.mark {{ display: block; width: 100%; height: 100%; overflow: visible; }}
code {{ font-family: "JetBrains Mono", ui-monospace, Menlo, monospace; }}

/* The hero: an Icelandic winter night, with the northern lights */

.hero {{
	position: relative;
	overflow: hidden;
	display: flex;
	align-items: center;
	gap: clamp(1.5rem, 4vw, 3.5rem);
	padding: clamp(2rem, 5vw, 4rem);
	border-radius: 18px;
	background:
		radial-gradient(ellipse 70% 55% at 70% 0%, rgba(184, 245, 60, .16), transparent 70%),
		radial-gradient(ellipse 50% 55% at 100% 30%, rgba(200, 30, 58, .22), transparent 70%),
		linear-gradient(#08060b, #0e0b12 60%, #160f1b);
	color: var(--bone);
}}

.hero .stars {{ position: absolute; inset: 0; pointer-events: none; }}
.hero .stars i {{ position: absolute; width: 2px; height: 2px; border-radius: 50%; background: #fff; opacity: .55; }}
.hero-head {{ flex: none; width: clamp(160px, 26vw, 300px); position: relative; }}
.hero-head::after {{ content: ""; position: absolute; inset: 22% 18% 30%; background: radial-gradient(closest-side, rgba(184, 245, 60, .2), transparent); z-index: -1; }}
.hero-text {{ position: relative; display: flex; flex-direction: column; gap: .9rem; }}
.hero .word {{ margin: 0; font-size: clamp(64px, 11vw, 136px); line-height: .9; letter-spacing: -.02em; color: var(--bone); }}
.hero .tagline {{ margin: 0; font-size: clamp(18px, 2vw, 24px); color: #ddd5e3; max-width: 28ch; text-wrap: balance; }}
.hero .lore {{ margin: 0; font-size: 14px; color: #a99fb5; font-style: italic; }}
@media (max-width: 700px) {{ .hero {{ flex-direction: column; text-align: center; }} .hero-text {{ align-items: center; }} }}

/* The acute on the í sits a little close to the f's in Fraunces; nudge it */
.ki {{ margin-left: .01em; }}

.story {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem; }}
.story div {{ background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 1.1rem 1.25rem; }}
.story p {{ margin: .3rem 0 0; color: var(--muted); font-size: .95rem; }}

/* Tiles */

.tiles {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 1px; background: var(--line); border: 1px solid var(--line); border-radius: 12px; overflow: hidden; }}
.tile {{ background: #fff; padding: 1.25rem; }}
.tile .big {{ width: 128px; height: 128px; margin: 0 auto .75rem; }}
.tile .small {{ display: flex; gap: .75rem; align-items: end; justify-content: center; margin-bottom: .9rem; }}
.tile p {{ color: var(--muted); font-size: .88rem; margin: .25rem 0 0; }}
.dark .tile {{ background: var(--night); color: var(--bone); }}
.dark .tile p {{ color: #a99fb5; }}
.dark .tile .big {{ width: 72px; height: 72px; }}

/* Lockups */

.lockups {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; }}
.lockup {{ display: flex; align-items: center; gap: .8rem; padding: 1.4rem 1.5rem; border-radius: 12px; background: #fff; border: 1px solid var(--line); }}
.lockup .m {{ flex: none; width: 64px; height: 64px; }}
.lockup .word {{ font-size: 50px; line-height: 1; letter-spacing: -.02em; }}
.lockup.on-dark {{ background: var(--night); border-color: var(--night); color: var(--bone); }}
.lockup.blood {{ background: var(--blood); border-color: var(--blood); color: #fff; }}

.tailword {{ display: inline-flex; align-items: baseline; }}
.tailword svg {{ width: .86em; height: .86em; margin-right: -.1em; transform: translateY(.1em); }}

.badge {{ display: inline-flex; align-items: center; gap: 7px; height: 36px; padding: 0 10px 0 6px; border: 1px solid var(--line); border-radius: 4px; background: var(--ash); text-decoration: none; color: var(--night); line-height: 1; }}
.badge .bm {{ width: 24px; height: 24px; }}
.badge .k {{ display: block; font: 7.5px/1 "JetBrains Mono", monospace; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); margin-bottom: 3px; }}
.badge .v {{ font-family: "Fraunces", serif; font-variation-settings: "SOFT" 100; font-weight: 650; font-size: 13px; }}

/* Demos */

.demo {{ background: #fff; border: 1px solid var(--line); border-radius: 12px; padding: 1.5rem 1.75rem; margin-bottom: 1rem; }}
.demo .label {{ font-size: .75rem; text-transform: uppercase; letter-spacing: .06em; color: var(--muted); margin: 0 0 .75rem; }}
.fake h2 {{ margin: 0 0 .5rem; font-size: 1.4rem; }}

/* The inline message. In a real app it lands in pages with unknown CSS, so it would carry its styles inline and reset what it inherits */
.ngerr {{ display: inline-flex; align-items: flex-start; gap: .65rem; max-width: 36rem; vertical-align: middle; margin: .2rem 0;
	padding: .55rem .8rem .6rem .6rem; border-radius: 8px; background: var(--tint); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent);
	box-shadow: inset 3px 0 0 var(--accent); font: 400 13px/1.45 "Figtree", system-ui, sans-serif; color: var(--night); text-align: left; letter-spacing: 0; }}
.ngerr-mark {{ flex: none; width: 34px; height: 34px; }}
.ngerr-kind {{ font-weight: 700; color: var(--accent); }}
.ngerr-el {{ font-size: 12px; font-weight: 600; }}
.ngerr-msg {{ display: block; color: #3b3640; }}
.ngerr-msg b {{ font-family: "JetBrains Mono", ui-monospace, monospace; font-size: 12px; }}

.ngchip {{ display: inline-flex; align-items: center; gap: .3rem; padding: .05rem .5rem .05rem .2rem; border-radius: 999px; vertical-align: middle;
	background: var(--tint); border: 1px solid color-mix(in srgb, var(--accent) 35%, transparent); font: 600 11px/1.6 "Figtree", sans-serif; color: var(--accent); }}
.ngchip-mark {{ width: 18px; height: 18px; }}
.ngchip code {{ font-size: 11px; }}

.error {{ --accent: var(--stare); --tint: #fde8eb; }}
.warning {{ --accent: var(--warn); --tint: #f6f7dc; }}
.fine {{ --accent: #3d6a0c; --tint: #eef8dc; }}

.expired {{ display: grid; grid-template-columns: 170px 1fr; gap: 2rem; align-items: center; background: #e6e3ec; border-color: #d2ccdc; }}
.expired .big {{ width: 170px; height: 170px; }}
.expired h3 {{ font-size: 1.5rem; margin: 0 0 .4rem; }}
.expired p {{ color: #4f4859; margin: 0 0 1rem; max-width: 46ch; }}
@media (max-width: 40rem) {{ .expired {{ grid-template-columns: 1fr; }} }}

.silver-button {{ display: inline-flex; align-items: center; gap: .5rem; padding: .6rem 1.2rem; border-radius: 999px; border: 1px solid #8d97a3;
	background: linear-gradient(#e9edf1, #b9c1ca); color: var(--night); font-weight: 700; text-decoration: none; box-shadow: inset 0 1px 0 #fff, 0 1px 2px rgba(0, 0, 0, .15); }}

/* Colour and type */

.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: .75rem; }}
.swatch div {{ height: 64px; border-radius: 10px; border: 1px solid rgba(29, 27, 34, .08); }}
.swatch strong {{ display: block; font-size: .85rem; margin-top: .4rem; }}
.swatch code {{ font-size: .78rem; color: var(--muted); }}

.type {{ display: grid; gap: .6rem; }}
.type div {{ display: flex; flex-wrap: wrap; align-items: baseline; gap: .4rem 1rem; }}
.type span:last-child {{ font-size: .85rem; color: var(--muted); }}
</style>
</head>
<body>

<svg width="0" height="0" style="position: absolute" aria-hidden="true"><defs>{symbols}</defs></svg>

<main>
<nav class="sheets"><a href="../glytta/usages.html">glytta usages</a> <a href="../logo-explorations/errors.html">engifer errors</a></nav>

<section class="hero">
	<div class="stars" aria-hidden="true">{"".join(f'<i style="left: {x}%; top: {y}%"></i>' for x, y in ((6, 12), (14, 70), (22, 30), (35, 8), (48, 82), (57, 18), (64, 60), (76, 10), (83, 44), (91, 76), (96, 22), (42, 46)))}</div>
	<div class="hero-head">{use("h-content", label="Skoffín: a dark cat-fox with glowing eyes and a fanged grin")}</div>
	<div class="hero-text">
		<h1 class="word">{WORD}</h1>
		<p class="tagline">A component-based Java web framework.</p>
		<p class="lore">Born of a cat and a fox, in Icelandic folklore.</p>
	</div>
</section>

<h2>The creature</h2>
<p class="intro">A skoffín is what you get when a fox fathers kittens on a cat: a creature of the dark, half one thing, half another, and more than either. That suits a framework that pairs an HTML template with a Java class. Monstrous, but the kind you'd still let in. A concept only: nothing here is in the framework.</p>
<div class="story">
	<div><h3>Cat mother</h3><p>The face, the slit-pupilled eyes that glow in the dark, the whiskers, the fangs.</p></div>
	<div><h3>Fox father</h3><p>The tall ears (one of them bitten), the ruff and brows, blood red where a fox is rust, the brush of a tail with its pale tip.</p></div>
	<div><h3>The glare</h3><p>In the stories, a skoffín's stare kills whatever it falls on. That's the error state.</p></div>
	<div><h3>Silver</h3><p>Only a gun loaded with silver can stop one. Silver is the colour of the fix: the button that gets you out.</p></div>
</div>

<h2>Marks</h2>
<p class="note">The head for the logo and the favicon, the tail for the S. At 128, 32 and 16 pixels.</p>
<div class="tiles">
	{tile("h-content", "The head", "A cat's face under a fox's ears, in the dark. The blood-red rim keeps it readable on night backgrounds; at 16 it's two eyes and two ears.", (32, 16))}
	{tile("tail", "The tail", "A fox's brush, dark with blood-red stripes, curled into an S. For the wordmark, and for spots where a face is too much.", (32, 16))}
</div>

<h2>Lockups</h2>
<p class="note">The wordmark is Fraunces with its soft corners turned all the way up: a storybook serif, a little wonky.</p>
<div class="lockups">
	<div class="lockup">{use("h-content", "mark m")}<span class="word">{WORD}</span></div>
	<div class="lockup on-dark"><span class="word">{TAILWORD}</span></div>
	<div class="lockup blood"><span class="word">{tailword("tail-on-fox")}</span></div>
	<div class="lockup"><a class="badge" href="#"><span class="bm">{use("h-content")}</span><span><span class="k">Powered by</span><span class="v">{WORD}</span></span></a><span class="note" style="margin: 0">The 88×31 badge.</span></div>
</div>

<h2>Moods</h2>
<p class="note">Five moods, each matched to a kind of problem. At 128, 32 and 20 pixels. The inline messages use them at about 34.</p>
<div class="tiles">
	{"".join(tile("h-" + k, t, d) for k, t, d in MOODS)}
</div>
<div class="tiles dark" style="margin-top: 1rem">
	{"".join(f'<div class="tile"><div class="big">{use("h-" + k)}</div><h3>{t}</h3></div>' for k, t, d in MOODS)}
</div>

<h2>Inline, where the error happened</h2>
<p class="note">The message renders in place of the element that failed, so you see it where you'd see the content. What went wrong, which element, the message.</p>
<div class="demo"><p class="label">Inbox, with <code>$user.nmae</code></p>
<div class="fake"><h2>Hello {box("error", "h-stare", "Unknown key", "&lt;wo:str&gt;", "While resolving keypath 'user.nmae': Unable to resolve key 'nmae' against class 'app.User'. Did you mean '<b>name</b>'?")}</h2></div></div>
<div class="demo"><p class="label">A repetition missing its list</p>
<div class="fake"><p>Your messages:</p>{box("error", "h-stare", "Binding configuration error", "&lt;wo:repetition&gt;", "You must bind either [list] or [count]")}</div></div>
<div class="demo"><p class="label">A warning (made up: there are no warnings yet). The page still renders</p>
<div class="fake"><p>{box("warning", "h-wary", "Deprecated binding", "&lt;wo:link&gt;", "[string] is deprecated. Put the link text between the tags instead.")}</p><p><a href="#">Lunch on Friday?</a></p></div></div>

<h2>Compact, for tight spots</h2>
<p class="note">Inside a table cell, a button or a line of text, a full message breaks the layout. A chip says where; hovering it, or <code>/ng/dev/problems</code>, says what.</p>
<div class="demo"><div class="fake">
<p>Signed in as {chip("error", "h-stare", "<code>user.nmae</code>")} · <a href="#">Sign out</a></p>
<table style="border-collapse: collapse; font-size: 14px">
	<tr><th style="text-align: left; padding: .3rem 1.5rem .3rem 0">Subject</th><th style="text-align: left">Received</th></tr>
	<tr><td style="padding: .3rem 1.5rem .3rem 0">Lunch on Friday?</td><td>{chip("error", "h-stare", "<code>&lt;wo:str&gt;</code>")}</td></tr>
	<tr><td style="padding: .3rem 1.5rem .3rem 0">Build #412 passed</td><td>{chip("warning", "h-wary", "<code>&lt;wo:str&gt;</code>")}</td></tr>
</table>
<p style="margin: 1rem 0 0">{chip("fine", "h-delighted", "All clear: no problems on this page")}</p>
</div></div>

<h2>Expired</h2>
<p class="note">Not a programming error, so not dev-only: the page a visitor gets when the page cache or session has let go of what they clicked. The way out is the silver button.</p>
<div class="demo expired"><div class="big">{use("h-asleep")}</div><div>
<h3>This page fell asleep</h3><p>It waited a long time for you to come back, then curled up and dozed off. Start again from the front page.</p><a class="silver-button" href="#">Wake it up</a></div></div>

<h2>Colour</h2>
<p class="note">Venom and blood: near-black fur, blood red where a fox is rust, venom-green eyes that turn red when it stares, and a cold, ashen paper around it.</p>
<div class="swatches">
	{"".join(f'<div class="swatch"><div style="background: {c}"></div><strong>{n}</strong><code>{c}</code></div>' for n, c in SWATCHES)}
</div>

<h2>Type</h2>
<div class="demo type">
	<div><span class="word" style="font-size: 34px">Fraunces, soft</span><span>wordmark and headings</span></div>
	<div><span style="font-size: 22px">Figtree</span><span>body text</span></div>
	<div><span style="font-family: 'JetBrains Mono', monospace; font-size: 19px">JetBrains Mono</span><span>code and templates</span></div>
</div>
</main>

</body>
</html>
"""

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w").write(page)
print(OUT, len(page))
