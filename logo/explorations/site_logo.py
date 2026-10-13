"""Writes the A3 mark with one of the typefaces from typefaces.py into the site's public/ folder.

Usage: python site_logo.py "Atkinson Hyperlegible Next Bold"   (the start of a label in typefaces.FACES)
Prints the logo's size, and the image heights for the sidebar (132px wide) and hero (320px wide) templates.
"""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("f", os.path.join(HERE, "typefaces.py"))
f = importlib.util.module_from_spec(spec); spec.loader.exec_module(f)
g = f.g
label = sys.argv[1]
_, path, axes, tracking = next(face for face in f.FACES if face[0].startswith(label))
PUB = os.path.join(HERE, "../../src/main/resources/public/")
for name, text, ng in (("engifer-logo.svg", g.INK, g.TORCH), ("engifer-logo-on-dark.svg", g.MINT, g.TURMERIC)):
    size, end, words = f.wordmark_svg(path, axes, tracking, text, ng)
    open(PUB + name, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {end + 20:.0f} {size:.0f}">'
                                f'<g transform="scale({size / 64:.4f})">{g.mark_root(f.colors)}</g>{words}</svg>\n')
    print(name, f"{end + 20:.0f} x {size:.0f}", round(132 * size / (end + 20)), round(320 * size / (end + 20)))
