"""Generate The Admissibility Stack flowchart in spine style.

v1.4 changes:
- Remove redundant arrow before OBSERVATION LAYER divider.
- Compress vertical spacing (HEADER_H 60→54, SECTION_H 54→48, PILL_H 60→54,
  LAYER_GAP 32→22, ARROW_LEN 32→20).
- Primitive Distinctions and Resolution Effects rendered as mid-width boxed
  sub-headers in slate colour (distinct from gold headers).
"""
from PIL import Image, ImageDraw, ImageFont
import os

# --- Palette (spine style) ---
BG = (26, 29, 35)           # #1a1d23
BOX_FILL = (34, 38, 46)     # #22262e
GOLD = (201, 162, 39)       # #c9a227
CREAM = (244, 241, 232)     # #f4f1e8
GRAY_SUB = (168, 168, 168)  # #a8a8a8
SLATE = (72, 82, 96)        # #485260  — sub-header box fill
AMBER = (216, 168, 74)      # #d8a84a  — observation layer bands (softer than gold)

# --- Layout constants ---
W, H = 1200, 2200
MARGIN_X = 80
HEADER_H = 54
SECTION_H = 48
PILL_H = 54
PILL_PAD = 42
LAYER_GAP = 22
ARROW_LEN = 20
PILL_GAP = 24
PILL_RADIUS = 12
HEADER_RADIUS = 6
SUBHEADER_H = 40
SUBHEADER_W_FRAC = 0.55  # fraction of content_w
STRUCT_RADIUS = 4         # sharp corners — structural ontology
OBS_RADIUS = 18           # rounded corners — observation layer

# --- Element types ---
# "section"   = full-width gold bar, bold uppercase (STRUCTURAL ONTOLOGY, OBSERVATION LAYER)
# "subheader" = mid-width slate box (Primitive Distinctions, Resolution Effects)
# "header"    = regular gold bar with bold text
# "pills"     = row of pill boxes
# "arrow"     = downward arrow

elements = [
    ("section", "STRUCTURAL ONTOLOGY"),
    ("subheader", "Primitive Distinctions"),
    ("pills", ["Identity", "Memory", "Record"]),
    ("arrow",),
    ("header", "Relations Governing Primitives"),
    ("pills", ["Continuity", "Encoded Persistence (Memory)", "Boundary Coupling (Record)"]),
    ("arrow",),
    ("header", "Domain Invariants"),
    ("pills", ["Universal Coupling Constraint", "Resolution-Depth Constraint"]),
    ("arrow",),
    ("header", "Admissible Claim Classes"),
    ("pills", ["Continuation (Binary)", "Unitarity", "Ontic vs Epistemic Order"]),
    ("section2", "OBSERVATION LAYER", "(Resolution-Dependent Effects)"),
    ("subheader", "Resolution Effects", "(Observer-Dependent Consequences)"),
    ("pills", ["Projection / Coarse-Graining", "Epistemic Non-Uniqueness", "Apparent Irreversibility"]),
    ("arrow",),
    ("header", "Bounded Subsystems"),
    ("pills", ["Agency", "Macro Freedom"]),
    ("arrow",),
    ("header", "Cost of Remaining Defined"),
    ("pills", ["Ledger Cost", "Boundary Rent", "Constraint Affordability (CA-0)"]),
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
font_section = get_font(18, bold=True)
font_section_sub = get_font(16)
font_header = get_font(20, bold=True)
font_subheader = get_font(18, bold=True)
font_pill = get_font(22)
font_pill_sm = get_font(18)

# --- Helpers ---
def rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
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

def draw_pills(draw, cx, y, pills, content_w, radius=PILL_RADIUS, pill_fill=BOX_FILL, pill_outline=GOLD, text_fill=CREAM):
    active_font = font_pill
    active_pad = PILL_PAD
    pill_widths = []
    for p in pills:
        pw, _ = text_size(draw, p, active_font)
        pill_widths.append(pw + active_pad * 2)
    total_pill_w = sum(pill_widths) + PILL_GAP * (len(pills) - 1)

    if total_pill_w > content_w:
        active_font = font_pill_sm
        active_pad = 28
        pill_widths = []
        for p in pills:
            pw, _ = text_size(draw, p, active_font)
            pill_widths.append(pw + active_pad * 2)
        total_pill_w = sum(pill_widths) + PILL_GAP * (len(pills) - 1)

    pill_x = cx - total_pill_w // 2
    pill_y = y

    for j, p in enumerate(pills):
        pw = pill_widths[j]
        rounded_rect(draw,
                     (pill_x, pill_y, pill_x + pw, pill_y + PILL_H),
                     radius=radius, fill=pill_fill, outline=pill_outline, width=2)
        ptw, pth = text_size(draw, p, active_font)
        draw.text((pill_x + (pw - ptw) // 2, pill_y + (PILL_H - pth) // 2),
                  p, fill=text_fill, font=active_font)
        pill_x += pw + PILL_GAP

    return pill_y + PILL_H

# --- Compute layout ---
img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

content_w = W - 2 * MARGIN_X
cx = W // 2

# Title
title_text = "The Admissibility Stack"
tw, th = text_size(draw, title_text, font_title)
title_y = 50
title_box_h = th + 30
rounded_rect(draw, (MARGIN_X, title_y, W - MARGIN_X, title_y + title_box_h),
             radius=16, fill=BOX_FILL, outline=GOLD, width=2)
draw.text((cx - tw // 2, title_y + 15), title_text, fill=CREAM, font=font_title)

y = title_y + title_box_h + LAYER_GAP + 10

# Draw elements
in_observation_layer = False
for elem in elements:
    kind = elem[0]

    if kind == "section":
        # Full-width gold bar, bold uppercase
        label = elem[1]
        rounded_rect(draw, (MARGIN_X, y, W - MARGIN_X, y + SECTION_H),
                     radius=STRUCT_RADIUS, fill=GOLD, outline=GOLD, width=1)
        sw, sh = text_size(draw, label, font_section)
        draw.text((cx - sw // 2, y + (SECTION_H - sh) // 2), label, fill=BG, font=font_section)
        y += SECTION_H + 8

    elif kind == "section2":
        # Two-line section divider (title + subtitle) — amber zone
        in_observation_layer = True
        label = elem[1]
        subtitle = elem[2]
        sw, sh = text_size(draw, label, font_section)
        stw, sth = text_size(draw, subtitle, font_section_sub)
        bar_h = sh + sth + 24
        rounded_rect(draw, (MARGIN_X, y, W - MARGIN_X, y + bar_h),
                     radius=OBS_RADIUS, fill=AMBER, outline=AMBER, width=1)
        draw.text((cx - sw // 2, y + 8), label, fill=BG, font=font_section)
        draw.text((cx - stw // 2, y + 8 + sh + 4), subtitle, fill=BG, font=font_section_sub)
        y += bar_h + 8

    elif kind == "subheader":
        # Mid-width slate box, optional subtitle
        label = elem[1]
        subtitle = elem[2] if len(elem) > 2 else None
        box_w = int(content_w * SUBHEADER_W_FRAC)
        x0 = cx - box_w // 2
        sw, sh = text_size(draw, label, font_subheader)
        if subtitle:
            stw, sth = text_size(draw, subtitle, font_section_sub)
            box_h = sh + sth + 16
            rounded_rect(draw, (x0, y, x0 + box_w, y + box_h),
                         radius=HEADER_RADIUS, fill=SLATE, outline=SLATE, width=1)
            draw.text((cx - sw // 2, y + 6), label, fill=CREAM, font=font_subheader)
            draw.text((cx - stw // 2, y + 6 + sh + 2), subtitle, fill=CREAM, font=font_section_sub)
            y += box_h + 8
        else:
            rounded_rect(draw, (x0, y, x0 + box_w, y + SUBHEADER_H),
                         radius=HEADER_RADIUS, fill=SLATE, outline=SLATE, width=1)
            draw.text((cx - sw // 2, y + (SUBHEADER_H - sh) // 2), label, fill=CREAM, font=font_subheader)
            y += SUBHEADER_H + 8

    elif kind == "header":
        # Band color + radius follows zone
        band = AMBER if in_observation_layer else GOLD
        hr = OBS_RADIUS if in_observation_layer else STRUCT_RADIUS
        label = elem[1]
        rounded_rect(draw, (MARGIN_X, y, W - MARGIN_X, y + HEADER_H),
                     radius=hr, fill=band, outline=band, width=1)
        hw, hh = text_size(draw, label, font_header)
        draw.text((cx - hw // 2, y + (HEADER_H - hh) // 2), label, fill=BG, font=font_header)
        y += HEADER_H + 12

    elif kind == "pills":
        pills = elem[1]
        r = OBS_RADIUS if in_observation_layer else STRUCT_RADIUS
        y = draw_pills(draw, cx, y, pills, content_w, radius=r)
        y += LAYER_GAP

    elif kind == "arrow":
        draw_arrow(draw, cx, y, y + ARROW_LEN)
        y += ARROW_LEN + 8

# --- Posture footer ---
y += 10
footer = "Stage-0 / CRL-0 / observer-only / non-authoritative"
fw, fh = text_size(draw, footer, font_pill)
draw.text((cx - fw // 2, y), footer, fill=GRAY_SUB, font=font_pill)
y += fh + 16

# --- Non-claim invariant ---
font_nonclaim = get_font(15)
nonclaim = "Consequence map, not definition source. Primitives live in Papers / FN."
nw, nh = text_size(draw, nonclaim, font_nonclaim)
draw.text((cx - nw // 2, y), nonclaim, fill=GRAY_SUB, font=font_nonclaim)

# --- Crop to content ---
final_h = y + nh + 50
img = img.crop((0, 0, W, final_h))

out_path = os.path.join(os.path.dirname(__file__), "admissibility-stack.png")
img.save(out_path, "PNG")
print(f"Saved: {out_path} ({W}x{final_h})")
