"""Social and web images from the articulated root (variant 5): avatars (GitHub, Facebook), the Facebook cover,
the link-sharing image, and the site's icons (favicon.ico, touch and app icons).

Run with a Python that has fonttools and brotli installed: python make_social.py
Renders with headless Chrome into png/, and copies the site's images into its public/ folder.
"""
import importlib.util
import os
import shutil
import struct
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.join(HERE, "../..")
EXPLORATIONS = os.path.join(REPO, "src/main/resources/public/logo-explorations")
FONTS = os.path.join(REPO, "src/main/resources/webserver-resources/fonts/inter")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
OUT = os.path.join(HERE, "png")
PUBLIC = os.path.join(REPO, "src/main/resources/public")
os.makedirs(OUT, exist_ok=True)

spec = importlib.util.spec_from_file_location("roots", os.path.join(EXPLORATIONS, "roots.py"))
roots = importlib.util.module_from_spec(spec)
spec.loader.exec_module(roots)
g = roots.g

# Variant 5, "All of it": knuckles, nubs, growth rings and the cut end
N, (_, _, KW) = next((n, v) for n, v in enumerate(roots.VARIANTS) if v[0].startswith("5 "))

EMERALD, MINT, TURMERIC, PAPER = "#074b3c", "#f0f7f3", "#ffb320", "#f5f8f6"

# The site's hero band: a faint blueprint grid with one soft glow
BAND = (f"background-color:{EMERALD};"
        "background-image:radial-gradient(ellipse 60% 140% at 100% 0%, rgba(62,232,165,.16), transparent 65%),"
        "linear-gradient(rgba(168,230,200,.08) 1px, transparent 1px),linear-gradient(90deg, rgba(168,230,200,.08) 1px, transparent 1px),"
        "linear-gradient(rgba(168,230,200,.04) 1px, transparent 1px),linear-gradient(90deg, rgba(168,230,200,.04) 1px, transparent 1px);"
        "background-size:auto,{major}px {major}px,{major}px {major}px,{minor}px {minor}px,{minor}px {minor}px;")

FONT_FACE = ('<style>@font-face{font-family:Inter;font-weight:400;src:url("file://' + FONTS + '/inter-400-normal-latin.woff2")}'
             '@font-face{font-family:Inter;font-weight:500;src:url("file://' + FONTS + '/inter-500-normal-latin.woff2")}</style>')


def mark(svg_id):
    """The mark, cropped close like the favicon so it can be sized by its visible extent"""
    return roots.mark(N, svg_id, **KW).replace('viewBox="0 0 64 64"', 'viewBox="2 2 60 60"')


def lockup(svg_id):
    return roots.lockup(N, svg_id, MINT, TURMERIC, **KW)


def render(body, width, height, name, transparent=False):
    page = os.path.join(HERE, "_render.html")
    with open(page, "w") as f:
        f.write(f'<html><head>{FONT_FACE}</head><body style="margin:0">'
                f'<div style="width:{width}px;height:{height}px;position:relative;overflow:hidden">{body}</div></body></html>')
    shot = os.path.join(HERE, "_render.png")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    "--virtual-time-budget=2000", f"--window-size={width},{height}", f"--screenshot={shot}", "file://" + page]
                   + (["--default-background-color=00000000"] if transparent else []),
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    os.replace(shot, os.path.join(OUT, name))
    os.remove(page)
    print(name)


def avatar(background, svg_id):
    # Sized to sit well inside the circle Facebook and GitHub crop avatars to
    return (f'<div style="{background}width:100%;height:100%;display:flex;align-items:center;justify-content:center">'
            f'<div style="width:70%;height:70%">{mark(svg_id)}</div></div>')


SVG_FILL = "<style>svg{display:block;width:100%;height:100%}</style>"

render(SVG_FILL + avatar(BAND.format(major=128, minor=32), "av1"), 1024, 1024, "engifer-avatar-1024.png")
render(SVG_FILL + avatar(f"background:{PAPER};", "av2"), 1024, 1024, "engifer-avatar-light-1024.png")

# Facebook cover: 1640×856 upload. Desktop shows the middle 1640×624, phones a narrower centre, so everything sits in the middle
cover = (f'<div style="{BAND.format(major=120, minor=24)}width:100%;height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px">'
         f'<div style="width:620px">{lockup("cv")}</div>'
         f'<div style="font:400 34px/1.3 Inter,sans-serif;color:#a8d5c0;letter-spacing:-0.01em">A Java web framework</div>'
         f'<div style="font:500 24px/1 Inter,sans-serif;color:{MINT};opacity:.75;letter-spacing:.02em">www.engifer.com</div>'
         '</div>')
render("<style>svg{display:block;width:100%;height:auto}</style>" + cover, 1640, 856, "facebook-cover-1640x856.png")


# ---------- Link sharing: Open Graph image, 1200×630 ----------
og = cover.replace("gap:34px", "gap:30px").replace('<div style="width:620px">', '<div style="width:560px">').replace("font:400 34px", "font:400 32px")
render("<style>svg{display:block;width:100%;height:auto}</style>" + og, 1200, 630, "engifer-og-1200x630.png")

# ---------- Icons ----------
# Touch and app icons: full-bleed emerald squares (iOS and Android round the corners themselves)
for size, name in ((180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")):
	render(SVG_FILL + avatar(BAND.format(major=size // 8, minor=size // 32), f"ic{size}"), size, size, name)

# Favicon: the transparent mark, packed into one .ico with 16, 32 and 48 pixel PNGs (48 is what search results use)
favicon_sizes = (16, 32, 48)
for size in favicon_sizes:
	render(SVG_FILL + f'<div style="width:{size}px;height:{size}px">{mark(f"fav{size}")}</div>', size, size, f"favicon-{size}.png", transparent=True)


def write_ico(path, pngs):
	"""An .ico holding PNG images: header, one directory entry per image, then the PNG data"""
	data = [open(png, "rb").read() for _, png in pngs]
	offset = 6 + 16 * len(pngs)
	out = struct.pack("<HHH", 0, 1, len(pngs))
	for (size, _), blob in zip(pngs, data):
		out += struct.pack("<BBBBHHII", size % 256, size % 256, 0, 0, 1, 32, len(blob), offset)
		offset += len(blob)
	with open(path, "wb") as f:
		f.write(out + b"".join(data))
	print(os.path.basename(path))


write_ico(os.path.join(OUT, "favicon.ico"), [(size, os.path.join(OUT, f"favicon-{size}.png")) for size in favicon_sizes])

# The site serves these from its public folder
for name in ("favicon.ico", "apple-touch-icon.png", "icon-192.png", "icon-512.png", "engifer-og-1200x630.png"):
	shutil.copy(os.path.join(OUT, name), os.path.join(PUBLIC, name))
