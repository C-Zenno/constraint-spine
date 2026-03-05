"""Generate The Admissibility Stack flowchart in spine style.

v1.2 changes:
- Insert Domain Invariants layer between Relations and Claim Class Structure.
- Encoded Persistence → Encoded Persistence (Memory).
- Boundary Coupling → Boundary Coupling (Record).
- Affordability (CA-0) → Constraint Affordability (CA-0).
"""
from PIL import Image, ImageDraw, ImageFont
import os

# --- Palette (spine style) ---
BG = (26, 29, 35)           # #1a1d23
BOX_FILL = (34, 38, 46)     # #22262e
GOLD = (201, 162, 39)       # #c9a227
CREAM = (244, 241, 232)     # #f4f1e8
GRAY_SUB = (168, 168, 168)  # #a8a8a8

# --- Layout constants ---
W, H = 1200, 1800
MARGIN_X = 80
HEADER_H = 60
PILL_H = 60
PILL_PAD = 42
LAYER_GAP = 32
ARROW_LEN = 32
PILL_GAP = 24
PILL_RADIUS = 12
HEADER_RADIUS = 6

# --- Layers ---
layers = [
    ("Primitive Distinctions", ["Identity", "Memory", "Record"]),
    ("Relations Governing Primitives", ["Continuity", "Encoded Persistence (Memory)", "Boundary Coupling (Record)"]),
    ("Domain Invariants", ["Universal Coupling Constraint", "Resolution-Depth Constraint"]),
    ("Claim Class Structure", ["Continuation (Binary)", "Unitarity", "Ontic vs Epistemic Order"]),
    ("Resolution Effects", ["Projection / Coarse-Graining", "Epistemic Non-Uniqueness", "Apparent Irreversibility"]),
    ("Bounded Subsystems", ["Agency", "Macro Freedom"]),
    ("Cost of Remaining Defined", ["Ledger Cost", "Boundary Rent", "Constraint Affordability (CA-0)"]),
]

# --- Font setup ---
def get_font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/segoeui.ttf",
        "C:/Windows/Fonts/segoeuib.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/arialbd.ttf",
    ]
    if bold:
        candidates = [
            "C:/Windows/Fonts/segoeuib.ttf",
            "C:/Windows/Fonts/arialbd.ttf",
        ] + candidates
    for f in candidates:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()

font_title = get_font(36, bold=True)
font_header = get_font(20, bold=True)
font_pill = get_font(22)
font_pill_sm = get_font(18)

# --- Helpers ---
def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)

def text_size(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

def draw_arrow(draw, cx, y_start, y_end):
    mid_x = cx
    draw.line([(mid_x, y_start), (mid_x, y_end)], fill=GOLD, width=2)
    arrow_sz = 8
    draw.polygon([
        (mid_x, y_end),
        (mid_x - arrow_sz, y_end - arrow_sz * 1.5),
        (mid_x + arrow_sz, y_end - arrow_sz * 1.5),
    ], fill=GOLD)

# --- Compute layout ---
img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

content_w = W - 2 * MARGIN_X
cx = W // 2

# Title
title_text = "The Admissibility Stack"
tw, th = text_size(draw, title_text, font_title)
title_y = 50
# Title box
title_box_h = th + 30
rounded_rect(draw, (MARGIN_X, title_y, W - MARGIN_X, title_y + title_box_h),
             radius=HEADER_RADIUS, fill=BOX_FILL, outline=GOLD, width=2)
draw.text((cx - tw // 2, title_y + 15), title_text, fill=CREAM, font=font_title)

y = title_y + title_box_h + LAYER_GAP + 10

# Draw each layer
for i, (header, pills) in enumerate(layers):
    # Arrow from previous
    if i > 0:
        draw_arrow(draw, cx, y, y + ARROW_LEN)
        y += ARROW_LEN + 8

    # Header bar
    rounded_rect(draw, (MARGIN_X, y, W - MARGIN_X, y + HEADER_H),
                 radius=HEADER_RADIUS, fill=GOLD, outline=GOLD, width=1)
    hw, hh = text_size(draw, header, font_header)
    draw.text((cx - hw // 2, y + (HEADER_H - hh) // 2), header, fill=BG, font=font_header)
    y += HEADER_H

    # Pill row — use smaller font if pills overflow content width
    active_font = font_pill
    active_pad = PILL_PAD
    pill_widths = []
    for p in pills:
        pw, ph = text_size(draw, p, active_font)
        pill_widths.append(pw + active_pad * 2)
    total_pill_w = sum(pill_widths) + PILL_GAP * (len(pills) - 1)

    if total_pill_w > content_w:
        active_font = font_pill_sm
        active_pad = 28
        pill_widths = []
        for p in pills:
            pw, ph = text_size(draw, p, active_font)
            pill_widths.append(pw + active_pad * 2)
        total_pill_w = sum(pill_widths) + PILL_GAP * (len(pills) - 1)

    pill_x = cx - total_pill_w // 2
    pill_y = y + 12

    for j, p in enumerate(pills):
        pw = pill_widths[j]
        rounded_rect(draw,
                     (pill_x, pill_y, pill_x + pw, pill_y + PILL_H),
                     radius=PILL_RADIUS, fill=BOX_FILL, outline=GOLD, width=2)
        ptw, pth = text_size(draw, p, active_font)
        draw.text((pill_x + (pw - ptw) // 2, pill_y + (PILL_H - pth) // 2),
                  p, fill=CREAM, font=active_font)
        pill_x += pw + PILL_GAP

    y = pill_y + PILL_H + LAYER_GAP

# --- Posture footer ---
y += 10
footer = "Stage-0 / CRL-0 / observer-only / non-authoritative"
fw, fh = text_size(draw, footer, font_pill)
draw.text((cx - fw // 2, y), footer, fill=GRAY_SUB, font=font_pill)

# --- Crop to content ---
final_h = y + fh + 50
img = img.crop((0, 0, W, final_h))

out_path = os.path.join(os.path.dirname(__file__), "admissibility-stack.png")
img.save(out_path, "PNG")
print(f"Saved: {out_path} ({W}x{final_h})")
