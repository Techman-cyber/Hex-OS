#!/usr/bin/env python3
"""Draws the HEX cursor theme (yellow with a dark outline) and writes real Xcursor files.
Run from the project root:  python3 tools/make-cursors.py   (needs Pillow)"""
import os, struct
from PIL import Image, ImageDraw, ImageFilter

YELLOW = (250, 218, 69, 255)
INK = (32, 32, 44, 255)
OUT = "config/includes.chroot/usr/share/icons/HEX-Cursor"
SIZES = [24, 32, 48, 64]
B = 1024  # drawing canvas

def rr(d, box, r): d.rounded_rectangle(box, radius=r, fill=255)

def shape_arrow():
    m = Image.new("L", (B, B), 0); d = ImageDraw.Draw(m)
    d.polygon([(80, 40), (800, 600), (320, 660), (60, 950)], fill=255)
    return m, None, (80, 40)

def shape_point():
    m = Image.new("L", (B, B), 0); d = ImageDraw.Draw(m)
    rr(d, (330, 60, 470, 620), 70)          # index finger
    rr(d, (455, 330, 575, 700), 55)         # finger 2
    rr(d, (560, 370, 670, 720), 52)         # finger 3
    rr(d, (655, 410, 770, 740), 55)         # finger 4
    rr(d, (330, 520, 770, 930), 130)        # palm
    d.polygon([(90, 470), (330, 600), (380, 900), (250, 880), (110, 640)], fill=255)  # thumb
    m = m.filter(ImageFilter.GaussianBlur(10)).point(lambda v: 255 if v > 128 else 0)
    lines = [((455, 450), (455, 640)), ((560, 480), (560, 650)), ((655, 500), (655, 660))]
    return m, lines, (400, 60)

def shape_grab():
    m = Image.new("L", (B, B), 0); d = ImageDraw.Draw(m)
    rr(d, (190, 360, 830, 900), 190)        # palm
    for i in range(4): rr(d, (260 + i * 130, 150, 370 + i * 130, 560), 55)   # fingers
    d.ellipse((120, 430, 330, 700), fill=255)  # thumb
    m = m.filter(ImageFilter.GaussianBlur(10)).point(lambda v: 255 if v > 128 else 0)
    lines = [((385 + i * 130, 330), (385 + i * 130, 520)) for i in range(3)]
    return m, lines, (510, 520)

def shape_ibeam():
    m = Image.new("L", (B, B), 0); d = ImageDraw.Draw(m)
    d.rectangle((470, 120, 560, 900), fill=255); d.rectangle((330, 120, 700, 200), fill=255); d.rectangle((330, 820, 700, 900), fill=255)
    return m, None, (515, 510)

def render(shape, size):
    mask, lines, hot = shape()
    k = max(10, B // 34)
    outline = mask.filter(ImageFilter.MaxFilter(2 * (k // 2) + 1))
    img = Image.new("RGBA", (B, B), (0, 0, 0, 0))
    img.paste(Image.new("RGBA", (B, B), INK), (0, 0), outline)
    img.paste(Image.new("RGBA", (B, B), YELLOW), (0, 0), mask)
    if lines:
        d = ImageDraw.Draw(img)
        for a, b in lines: d.line([a, b], fill=INK, width=k, joint="curve")
    bb = outline.getbbox()
    crop = img.crop(bb)
    margin = 1
    s = (size - 2 * margin) / max(crop.size)
    w, h = max(1, round(crop.size[0] * s)), max(1, round(crop.size[1] * s))
    small = crop.resize((w, h), Image.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    if shape is shape_arrow or shape is shape_point:
        ox, oy = (margin, margin) if shape is shape_arrow else ((size - w) // 2, margin)
    else:
        ox, oy = (size - w) // 2, (size - h) // 2
    canvas.paste(small, (ox, oy), small)
    hx = int(max(0, min(size - 1, ox + (hot[0] - bb[0]) * s)))
    hy = int(max(0, min(size - 1, oy + (hot[1] - bb[1]) * s)))
    return canvas, hx, hy

def pack(canvas):
    out = bytearray()
    for r, g, b, a in canvas.getdata():
        out += struct.pack("<BBBB", r * a // 255, g * a // 255, b * a // 255, a)  # B,G,R order below
    # Xcursor wants ARGB32 little endian = bytes B,G,R,A
    out = bytearray()
    for r, g, b, a in canvas.getdata():
        out += bytes((b * a // 255, g * a // 255, r * a // 255, a))
    return bytes(out)

def write_cursor(path, shape):
    imgs = []
    for sz in SIZES:
        c, hx, hy = render(shape, sz)
        imgs.append((sz, c.size[0], c.size[1], hx, hy, 50, pack(c)))
    toc, chunks, off = b"", b"", 16 + 12 * len(imgs)
    for sz, w, h, xh, yh, delay, pix in imgs:
        toc += struct.pack("<III", 0xFFFD0002, sz, off + len(chunks))
        chunks += struct.pack("<IIIIIIIII", 36, 0xFFFD0002, sz, 1, w, h, xh, yh, delay) + pix
    with open(path, "wb") as f:
        f.write(struct.pack("<4sIII", b"Xcur", 16, 0x10000, len(imgs)) + toc + chunks)

GROUPS = {
    shape_arrow: ["left_ptr", "default", "arrow", "top_left_arrow", "right_ptr", "center_ptr", "X_cursor"],
    shape_point: ["hand2", "hand1", "pointer", "pointing_hand", "9d800788f1b08800ae810202380a0822", "e29285e634086352946a0e7090d73106"],
    shape_grab: ["grab", "grabbing", "openhand", "closedhand", "fleur", "move", "all-scroll", "size_all", "dnd-move",
                 "4498f0e0c1937ffe01fd06f973665830", "9081237383d90e509aa00f00170e968f", "fcf21c00b30f7e3f83fe0dfd12e71cff"],
    shape_ibeam: ["xterm", "text", "ibeam"],
}

if __name__ == "__main__":
    os.makedirs(OUT + "/cursors", exist_ok=True)
    for shape, names in GROUPS.items():
        for n in names: write_cursor(f"{OUT}/cursors/{n}", shape)
    open(OUT + "/index.theme", "w").write("[Icon Theme]\nName=HEX Cursor\nComment=Yellow cursors for HEX OS\nInherits=Adwaita\n")
    os.makedirs("config/includes.chroot/usr/share/icons/default", exist_ok=True)
    open("config/includes.chroot/usr/share/icons/default/index.theme", "w").write("[Icon Theme]\nInherits=HEX-Cursor\n")
    print("cursors written:", sum(len(v) for v in GROUPS.values()))
