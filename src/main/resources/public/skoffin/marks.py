"""Skoffín marks: the head (a fox's ears, ruff and brush on a cat's face, in the dark, with glowing eyes and a fanged grin)
in five moods, and the tail S."""

FUR, SMOKE, RIM = "#2b2530", "#463c4a", "#c8552b"
FOX, EMBER, CREAM, INK = "#c8552b", "#8f3517", "#f6ead8", "#120d14"
GLOW, STARE, MOUTH = "#ffbe3b", "#ff5a2e", "#5e1620"

RIM_STYLE = f'stroke="{RIM}" stroke-width="1.3" stroke-linejoin="round"'


def ear_left(angle):
    return (f'<g transform="rotate({angle} 20 25)">'
            f'<path d="M12 31 C10.5 22 9.5 12 8 3 C16 7 24 13 30 19 Z" fill="{FUR}" {RIM_STYLE} />'
            f'<path d="M14.6 25 C13.8 19 13.2 13.5 12.6 9.5 C17 12.4 21 15.4 24.4 18.6 Z" fill="{EMBER}" />'
            '</g>')


def ear_right(angle):
    # A bite out of the right ear: it's been in fights
    return (f'<g transform="translate(64 0) scale(-1 1)"><g transform="rotate({angle} 20 25)">'
            f'<path d="M12 31 C10.5 22 9.5 12 8 3 C10.5 4.6 13 6.3 15 7.9 L14.2 11.6 L18.6 10.6 C22.6 13.4 26.6 16.2 30 19 Z" fill="{FUR}" {RIM_STYLE} />'
            f'<path d="M14.6 25 C13.8 19 13.4 15 13.2 13 L16.4 12.4 C19 14.2 21.8 16.4 24.4 18.6 Z" fill="{EMBER}" />'
            '</g></g>')


def ears(angle=0):
    return ear_left(angle) + ear_right(angle)


HEAD = (f'<path d="M32 16 C42 16 50 22 52 30 L59 31 L54 35.5 L60.5 40.5 L53 42.5 C51 50 44 55.5 37 57 L32 62 L27 57 '
        f'C20 55.5 13 50 11 42.5 L3.5 40.5 L10 35.5 L5 31 L12 30 C14 22 22 16 32 16 Z" fill="{FUR}" {RIM_STYLE} />')
# The fox in it: a rust cheek ruff, like a fox's
RUFF = (f'<path d="M12.2 30 L5 31 L10 35.5 L3.5 40.5 L11 42.5 C12.6 47.4 15.6 51.4 19.6 54.4 C18.4 46 16 37.6 12.2 30 Z" fill="{FOX}" />'
        f'<path d="M51.8 30 L59 31 L54 35.5 L60.5 40.5 L53 42.5 C51.4 47.4 48.4 51.4 44.4 54.4 C45.6 46 48 37.6 51.8 30 Z" fill="{FOX}" />')
HEAD = HEAD + RUFF + f'<path d="M32 16 C42 16 50 22 52 30 L59 31 L54 35.5 L60.5 40.5 L53 42.5 C51 50 44 55.5 37 57 L32 62 L27 57 C20 55.5 13 50 11 42.5 L3.5 40.5 L10 35.5 L5 31 L12 30 C14 22 22 16 32 16 Z" fill="none" {RIM_STYLE} />'
TUFT = f'<path d="M26 18 L28.5 11 L31 16.4 L34 9.5 L36 16.6 L38.5 12.5 L39 18.4 Z" fill="{FUR}" {RIM_STYLE} />'
HACKLES = f'<path d="M22 20 L23 8 L28 16 L31 5 L34.5 15.5 L39.5 7 L41.5 19.5 Z" fill="{FUR}" {RIM_STYLE} />'
MUZZLE = f'<path d="M23.5 44 C26 41 38 41 40.5 44 C39.6 50.4 35.4 53.6 32 53.6 C28.6 53.6 24.4 50.4 23.5 44 Z" fill="{SMOKE}" />'
NOSE = f'<path d="M30.2 42.4 C31.2 42 32.8 42 33.8 42.4 C33.4 43.6 32.7 44.4 32 44.8 C31.3 44.4 30.6 43.6 30.2 42.4 Z" fill="{INK}" />'
WHISKERS = (f'<g fill="none" stroke="{CREAM}" stroke-width=".7" stroke-linecap="round" stroke-opacity=".55">'
            '<path d="M24 45.5 C18 44.4 11 45 3 48.6" /><path d="M24.4 47.6 C19 48.4 13 50.6 7 55" />'
            '<path d="M40 45.5 C46 44.4 53 45 61 48.6" /><path d="M39.6 47.6 C45 48.4 51 50.6 57 55" /></g>')


def brows(kind="sly"):
    d = {"sly": ("M16.5 29.5 L27.5 33", "M47.5 29.5 L36.5 33"),
         "raised": ("M17 31.5 L27 28.6", "M47 31.5 L37 28.6"),
         "fury": ("M16 28 L28 33.6", "M48 28 L36 33.6")}[kind]
    return f'<g fill="none" stroke="{FOX}" stroke-width="2.4" stroke-linecap="round"><path d="{d[0]}" /><path d="{d[1]}" /></g>'


def eye_shape(side):
    # A heavy, slanted lid: big glowing eyes, but sly
    if side < 0:
        return "M18.4 34.4 L29 36.4 C28.6 40 25.8 41.4 23.4 41.2 C20.4 40.9 18.5 38.2 18.4 34.4 Z"
    return "M45.6 34.4 L35 36.4 C35.4 40 38.2 41.4 40.6 41.2 C43.6 40.9 45.5 38.2 45.6 34.4 Z"


def eyes(kind="slit"):
    out = ""
    for side, cx in ((-1, 24), (1, 40)):
        cy = 38.2
        if kind in ("slit", "round", "stare"):
            color = STARE if kind == "stare" else GLOW
            glow_r, glow_o = (8.5, .38) if kind == "stare" else (6, .18)
            out += f'<circle cx="{cx}" cy="{cy}" r="{glow_r}" fill="{color}" fill-opacity="{glow_o}" />'
            if kind == "round":
                out += f'<ellipse cx="{cx}" cy="{cy - .4}" rx="5.2" ry="4.6" fill="{color}" />'
                out += f'<circle cx="{cx}" cy="{cy - .2}" r="2.5" fill="{INK}" /><circle cx="{cx + 1}" cy="{cy - 1.2}" r=".8" fill="#fff" />'
            else:
                out += f'<path d="{eye_shape(side)}" fill="{color}" />'
                rx = .5 if kind == "stare" else .9
                out += f'<ellipse cx="{cx}" cy="{cy + .2}" rx="{rx}" ry="2.5" fill="{INK}" />'
        elif kind == "happy":
            out += f'<path d="M{cx - 4.6} {cy + 1.6} L{cx} {cy - 2.4} L{cx + 4.6} {cy + 1.6}" fill="none" stroke="{GLOW}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />'
        elif kind == "closed":
            out += f'<path d="M{cx - 4.6} {cy} C{cx - 2.6} {cy + 2.6} {cx + 2.6} {cy + 2.6} {cx + 4.6} {cy}" fill="none" stroke="{CREAM}" stroke-width="1.5" stroke-linecap="round" stroke-opacity=".8" />'
    return out


def fang(x, y, h=2.8):
    return f'<path d="M{x - 1.1} {y} L{x} {y + h} L{x + 1.1} {y} Z" fill="{CREAM}" />'


SLY_GRIN = (f'<path d="M23.5 46 C27 49.6 37 49.6 40.5 46" fill="none" stroke="{INK}" stroke-width="1.2" stroke-linecap="round" />'
            + fang(28.4, 48.2) + fang(35.6, 48.2))


def open_grin(depth=6):
    # A wide mouth with a row of small sharp teeth and two fangs
    bottom = 46 + depth
    mouth = f'<path d="M23 45.6 C27 {bottom + 1.4} 37 {bottom + 1.4} 41 45.6 C37 47.8 27 47.8 23 45.6 Z" fill="{MOUTH}" stroke="{INK}" stroke-width=".8" />'
    teeth = "M24.6 46.4 " + " ".join(f"L{25.6 + i * 1.6} {48.4 if i % 2 == 0 else 47.2}" for i in range(9)) + " C35 47.6 29 47.6 24.6 46.4 Z"
    return mouth + f'<path d="{teeth}" fill="{CREAM}" />' + fang(28, 47, 3.4) + fang(36, 47, 3.4)


def head(mood="content"):
    if mood == "content":
        return ears() + HEAD + TUFT + MUZZLE + brows("sly") + eyes("slit") + NOSE + SLY_GRIN + WHISKERS
    if mood == "delighted":
        return ears(-4) + HEAD + TUFT + MUZZLE + brows("raised") + eyes("happy") + NOSE + open_grin(6) + WHISKERS
    if mood == "wary":
        return (ears(-18) + HACKLES + HEAD + MUZZLE + brows("raised") + eyes("round") + NOSE
                + f'<path d="M26 48.4 C29 46.8 35 46.8 38 48.4" fill="none" stroke="{INK}" stroke-width="1.2" stroke-linecap="round" />'
                + fang(29.6, 47.6, 2.4) + WHISKERS)
    if mood == "stare":
        return (ears(-32) + HACKLES + HEAD + MUZZLE + brows("fury") + eyes("stare") + NOSE + open_grin(4) + WHISKERS
                + f'<g fill="none" stroke="{STARE}" stroke-width="1.4" stroke-linecap="round"><path d="M10 26 L3.5 22" /><path d="M13 21 L9 15.5" /><path d="M54 26 L60.5 22" /><path d="M51 21 L55 15.5" /></g>')
    if mood == "asleep":
        return (f'<g transform="rotate(8 32 40)">{ears(-16)}{HEAD}{TUFT}{MUZZLE}{eyes("closed")}{NOSE}'
                f'<path d="M27 47.6 C30 49 34 49 37 47.6" fill="none" stroke="{INK}" stroke-width="1.2" stroke-linecap="round" />'
                f'{fang(34.6, 48.4, 2.6)}{WHISKERS}</g>'
                f'<g fill="none" stroke="#7d8aa0" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M50 8 h5 l-5 5 h5" /><path d="M57 2 h3.4 l-3.4 3.4 h3.4" /></g>')
    raise ValueError(mood)


TAIL_PATH = "M45 11 C31 3 13 13 23 25 C31 34 47 33 43 47"
TAIL_TIP = "M43 47 C40 57.5 25 58 19 52"


def tail(body=FUR, stripe=FOX, tip=CREAM, rim=RIM):
    return (f'<path d="{TAIL_PATH}" fill="none" stroke="{rim}" stroke-width="12.6" stroke-linecap="round" />'
            f'<path d="{TAIL_PATH}" fill="none" stroke="{body}" stroke-width="10" stroke-linecap="round" />'
            f'<path d="{TAIL_PATH}" fill="none" stroke="{stripe}" stroke-width="10" stroke-dasharray="2.2 7.8" stroke-dashoffset="-6" />'
            f'<path d="{TAIL_TIP}" fill="none" stroke="{rim}" stroke-width="12.6" stroke-linecap="round" />'
            f'<path d="{TAIL_TIP}" fill="none" stroke="{tip}" stroke-width="10" stroke-linecap="round" />')


def svg(body, vb="0 0 64 64"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}">{body}</svg>'
