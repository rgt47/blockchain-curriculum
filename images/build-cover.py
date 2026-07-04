#!/usr/bin/env python3
"""
Build a cover image for The Statistics of Blockchain for
Public Health, in the visual idiom of the rgtlab Curriculum
Project series: two-zone composition with a watercolour-
painted top zone and a solid bottom zone, clean sans-serif
typography.

Differs from the sister covers only in palette: anchored on
a scholarly indigo (#33356b) moving through blue-violet into
gold and cream, visibly distinct from the SCAI
(navy-indigo-amber), applied-methods (slate), applied-genai
(umber-bronze-ochre), and r-bootcamp (moss-forest) covers.

Usage:
    python3 build-cover.py
Output:
    cover.png     (1200 x 1800, the book cover)
    favicon.png   (128 x 128, the tab icon)
"""

import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# --- canvas ---------------------------------------------------------------

W, H        = 1200, 1800
SPLIT_Y     = int(H * 0.36)

# --- colours --------------------------------------------------------------

# brand indigo anchors the bottom zone
INDIGO      = (51, 53, 107)          # #33356b brand indigo
INDIGO_DEEP = (32, 34, 74)           # darker indigo
CREAM       = (248, 244, 233)
GOLD        = (201, 180, 95)
INK         = (30, 32, 60)
WHITE       = (255, 255, 255)

# top-zone watercolour palette: deep indigo through the
# brand indigo into blue-violet, warm gold, and pale cream.
WATERCOLOUR = [
    (28,  30,  66),    # deep indigo
    (51,  53,  107),   # indigo (brand)
    (110, 118, 178),   # blue-violet / periwinkle
    (201, 180, 95),    # warm gold
    (233, 231, 222),   # pale cream
]

# --- helpers --------------------------------------------------------------

def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def palette_at(t, palette=WATERCOLOUR):
    n = len(palette) - 1
    pos = t * n
    i   = int(pos)
    if i >= n:
        return palette[-1]
    return lerp(palette[i], palette[i + 1], pos - i)


def watercolour_zone(width, height, seed=71):
    rng  = random.Random(seed)
    base = Image.new('RGB', (width, height), (240, 240, 240))
    px   = base.load()

    for y in range(height):
        for x in range(width):
            t = (x / width * 0.55 + y / height * 0.45)
            t = max(0.0, min(1.0, t))
            px[x, y] = palette_at(t)

    overlay = Image.new('RGB', (width, height), (0, 0, 0))
    odraw   = ImageDraw.Draw(overlay)
    mask    = Image.new('L', (width, height), 0)
    mdraw   = ImageDraw.Draw(mask)

    for _ in range(28):
        cx = rng.randint(-100, width + 100)
        cy = rng.randint(-50, height + 50)
        r  = rng.randint(180, 480)
        col = palette_at(rng.uniform(0, 1))
        odraw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
        mdraw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=70)

    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=120))
    mask    = mask.filter(ImageFilter.GaussianBlur(radius=80))
    base    = Image.composite(overlay, base, mask)

    base    = base.filter(ImageFilter.GaussianBlur(radius=2))
    return base


def add_paper_grain(img, strength=8, seed=11):
    rng    = random.Random(seed)
    grain  = Image.new('L', img.size, 128)
    gpx    = grain.load()
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            gpx[x, y] = max(
                0, min(255, 128 + rng.randint(-strength, strength))
            )
    grain = grain.filter(ImageFilter.GaussianBlur(radius=0.5))
    img.paste(Image.blend(
        img.convert('RGB'),
        Image.merge('RGB', (grain, grain, grain)),
        0.05,
    ))
    return img


def font(name, size):
    candidates = {
        'avenir-medium':   ('/System/Library/Fonts/Avenir.ttc', 2),
        'avenir-heavy':    ('/System/Library/Fonts/Avenir.ttc', 6),
        'avenir-black':    ('/System/Library/Fonts/Avenir.ttc', 7),
        'avenir-book':     ('/System/Library/Fonts/Avenir.ttc', 1),
        'avenir-light':    ('/System/Library/Fonts/Avenir.ttc', 0),
        'helvetica-bold':  ('/System/Library/Fonts/Helvetica.ttc', 1),
        'helvetica':       ('/System/Library/Fonts/Helvetica.ttc', 0),
    }
    path, idx = candidates[name]
    return ImageFont.truetype(path, size, index=idx)


def draw_text(draw, xy, text, fnt, fill, anchor='lt'):
    draw.text(xy, text, font=fnt, fill=fill, anchor=anchor)


# --- chain motif for the top zone and favicon ----------------------------

def draw_chain(draw, nodes, node_r, colour, link_w):
    for a, b in zip(nodes, nodes[1:]):
        draw.line([a, b], fill=colour, width=link_w)
    for (cx, cy) in nodes:
        draw.ellipse((cx - node_r, cy - node_r, cx + node_r, cy + node_r),
                     fill=colour)


# --- build ---------------------------------------------------------------

def build():
    canvas = Image.new('RGB', (W, H), INDIGO)

    top = watercolour_zone(W, SPLIT_Y, seed=71)
    canvas.paste(top, (0, 0))

    draw = ImageDraw.Draw(canvas)

    # cream hairline divider
    draw.rectangle((0, SPLIT_Y, W, SPLIT_Y + 3), fill=CREAM)

    # left-edge spine accent
    draw.rectangle((0, 0, 14, SPLIT_Y), fill=INDIGO_DEEP)
    draw.rectangle((14, 0, 17, SPLIT_Y), fill=CREAM)

    # --- top-zone typography ---------------------------------------------
    series_fnt = font('avenir-heavy', 36)
    draw_text(draw, (60, 90),
              'GRADUATE BIOSTATISTICS SERIES',
              series_fnt, WHITE)

    author_fnt = font('avenir-medium', 64)
    for line in ['rgtlab Curriculum Project']:
        draw_text(draw, (60, 240), line, author_fnt, WHITE)

    # faint block-chain motif in the lower-right of the top zone
    ny = SPLIT_Y - 120
    chain_nodes = [(W - 470, ny + 40), (W - 360, ny - 10),
                   (W - 250, ny + 30), (W - 140, ny - 15)]
    draw_chain(draw, chain_nodes, node_r=13, colour=GOLD, link_w=5)

    # --- bottom-zone typography ------------------------------------------
    title_fnt   = font('avenir-black', 100)
    title_lines = ['The Statistics',
                   'of Blockchain',
                   'for Public Health']
    y = SPLIT_Y + 90
    for line in title_lines:
        draw_text(draw, (60, y), line, title_fnt, WHITE)
        y += 122

    sub_fnt = font('avenir-medium', 46)
    y += 26
    for line in ['A graduate textbook']:
        draw_text(draw, (62, y), line, sub_fnt, CREAM)
        y += 60

    edition_fnt  = font('avenir-light', 42)
    draw_text(draw, (60, H - 180), 'First Edition  ·  2026',
              edition_fnt, CREAM)

    mark_fnt = font('avenir-heavy', 44)
    draw_text(draw, (W - 60, H - 80), 'rgtlab', mark_fnt, WHITE,
              anchor='rs')
    draw.rectangle((W - 240, H - 64, W - 60, H - 60), fill=GOLD)

    canvas = add_paper_grain(canvas)
    return canvas


def build_favicon():
    size = 128
    img  = Image.new('RGB', (size, size), INDIGO)
    draw = ImageDraw.Draw(img)
    nodes = [(24, 82), (54, 44), (84, 78), (110, 46)]
    draw_chain(draw, nodes, node_r=9, colour=GOLD, link_w=5)
    return img


if __name__ == '__main__':
    img = build()
    img.save('cover.png', optimize=True)
    print(f'wrote cover.png ({img.size[0]} x {img.size[1]})')
    fav = build_favicon()
    fav.save('favicon.png', optimize=True)
    print(f'wrote favicon.png ({fav.size[0]} x {fav.size[1]})')
