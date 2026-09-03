from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent
W, H = 1200, 630


def font(size, bold=False):
    names = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for name in names:
        path = Path(name)
        if path.exists():
            return ImageFont.truetype(str(path), size)
    return ImageFont.load_default()


def t(draw, xy, value, size, fill, bold=False, anchor=None):
    draw.text(xy, value, font=font(size, bold), fill=fill, anchor=anchor)


def pill(draw, xy, label, fill, fg="#07111f"):
    x, y = xy
    f = font(20, True)
    bbox = draw.textbbox((0, 0), label, font=f)
    width = bbox[2] - bbox[0] + 32
    draw.rounded_rectangle((x, y, x + width, y + 36), radius=18, fill=fill)
    draw.text((x + 16, y + 7), label, font=f, fill=fg)
    return width


def base():
    img = Image.new("RGB", (W, H), "#07111f")
    draw = ImageDraw.Draw(img)
    for y in range(H):
        mix = y / H
        draw.line((0, y, W, y), fill=(7, int(17 + 24 * mix), int(31 + 50 * mix)))
    for x in range(0, W, 90):
        draw.line((x, 0, x + 260, H), fill="#10233f", width=1)
    for y in range(35, H, 78):
        draw.line((0, y, W, y), fill="#0f294b", width=1)
    return img, draw


def save_svg(path, title, subtitle, accent, body):
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <rect width="{W}" height="{H}" fill="#07111f"/>
  <rect x="70" y="230" width="1060" height="250" rx="18" fill="#0b1f33" stroke="{accent}" stroke-width="2"/>
  <text x="72" y="150" fill="#f8fafc" font-family="Arial, sans-serif" font-size="54" font-weight="700">{title}</text>
  <text x="74" y="192" fill="#cbd5e1" font-family="Arial, sans-serif" font-size="27">{subtitle}</text>
  {body}
</svg>
"""
    path.write_text(svg)


def agent_hero():
    img, draw = base()
    pill(draw, (72, 56), "ARCKIT AGENT ARCHITECTURE", "#a7f3d0")
    pill(draw, (412, 56), "6 COMMANDS", "#facc15")
    t(draw, (72, 128), "AI Agent Architecture", 56, "#f8fafc", True)
    t(draw, (74, 195), "inventory, design, governance, integration, security, maturity", 27, "#cbd5e1")

    draw.rounded_rectangle((70, 230, 1130, 485), radius=18, fill="#0b1f33", outline="#a7f3d0", width=2)
    nodes = [
        (190, 330, "Inventory", "#a7f3d0"),
        (380, 290, "Design", "#facc15"),
        (590, 330, "Integration", "#7dd3fc"),
        (790, 290, "Governance", "#c4b5fd"),
        (1000, 330, "Security", "#fda4af"),
        (590, 430, "Maturity", "#fdba74"),
    ]
    for i in range(len(nodes) - 1):
        x1, y1, _, _ = nodes[i]
        x2, y2, _, _ = nodes[i + 1]
        draw.line((x1 + 72, y1, x2 - 72, y2), fill="#d6e4ff", width=4)
    draw.line((590, 355, 590, 405), fill="#d6e4ff", width=4)
    for cx, cy, label, fill in nodes:
        draw.rounded_rectangle((cx - 82, cy - 28, cx + 82, cy + 28), radius=16, fill=fill)
        t(draw, (cx, cy), label, 20, "#07111f", True, anchor="mm")

    t(draw, (88, 532), "AAGI  |  AAGR  |  AAOV  |  AAIN  |  AASE  |  AAMT", 25, "#f8fafc", True)
    t(draw, (88, 585), "agent-architecture recipe  |  core arckit dependency  |  MIT community overlay", 21, "#cbd5e1")

    img.save(ROOT / "2026-06-30-arckit-agent-architecture-hero.png", optimize=True)
    save_svg(
        ROOT / "2026-06-30-arckit-agent-architecture-hero.svg",
        "AI Agent Architecture",
        "inventory, design, governance, integration, security, maturity",
        "#a7f3d0",
        '<text x="88" y="532" fill="#f8fafc" font-family="Arial, sans-serif" font-size="25" font-weight="700">AAGI | AAGR | AAOV | AAIN | AASE | AAMT</text>',
    )


def togaf_hero():
    img, draw = base()
    pill(draw, (72, 56), "ARCKIT TOGAF ADM", "#7dd3fc")
    pill(draw, (326, 56), "9 COMMANDS", "#facc15")
    t(draw, (72, 128), "TOGAF ADM Workflow", 56, "#f8fafc", True)
    t(draw, (74, 195), "ADM phases as versioned ArcKit artefacts", 27, "#cbd5e1")

    draw.rounded_rectangle((70, 230, 1130, 485), radius=18, fill="#0b1f33", outline="#7dd3fc", width=2)
    phases = [
        (150, 355, "Prelim", "#7dd3fc"),
        (285, 315, "A", "#93c5fd"),
        (420, 355, "C", "#a7f3d0"),
        (555, 315, "Rationalize", "#fdba74"),
        (720, 355, "Gaps", "#facc15"),
        (865, 315, "Transition", "#c4b5fd"),
        (1025, 355, "Board", "#fda4af"),
    ]
    for i in range(len(phases) - 1):
        x1, y1, _, _ = phases[i]
        x2, y2, _, _ = phases[i + 1]
        draw.line((x1 + 58, y1, x2 - 58, y2), fill="#d6e4ff", width=4)
    for cx, cy, label, fill in phases:
        draw.ellipse((cx - 58, cy - 58, cx + 58, cy + 58), fill=fill, outline="#d6e4ff", width=2)
        t(draw, (cx, cy), label, 18 if len(label) > 7 else 24, "#07111f", True, anchor="mm")

    t(draw, (88, 532), "ADMP  |  BPCM  |  APP  |  APPR  |  GAPA  |  TRANS  |  BORD  |  ACHG  |  REPO", 22, "#f8fafc", True)
    t(draw, (88, 585), "togaf-adm-full recipe  |  architecture repository  |  MIT community overlay", 21, "#cbd5e1")

    img.save(ROOT / "2026-07-01-arckit-togaf-adm-hero.png", optimize=True)
    save_svg(
        ROOT / "2026-07-01-arckit-togaf-adm-hero.svg",
        "TOGAF ADM Workflow",
        "ADM phases as versioned ArcKit artefacts",
        "#7dd3fc",
        '<text x="88" y="532" fill="#f8fafc" font-family="Arial, sans-serif" font-size="22" font-weight="700">ADMP | BPCM | APP | APPR | GAPA | TRANS | BORD | ACHG | REPO</text>',
    )


if __name__ == "__main__":
    agent_hero()
    togaf_hero()
