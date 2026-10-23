"""Builds every lead magnet: PDF (gen/static/resources/<slug>.pdf), mockup and banner images.
Run: python3 gen/leadmagnets/build_all.py"""
import os, sys, subprocess, tempfile
sys.path.insert(0, os.path.dirname(__file__)); sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from builder import build
from resources_a import RESOURCES as RA
from resources_b import RESOURCES as RB
from PIL import Image, ImageDraw, ImageFont, ImageFilter

OUT = os.path.join(os.path.dirname(__file__), "..", "static", "resources")
os.makedirs(OUT, exist_ok=True)
F = "/usr/share/fonts/truetype/liberation/"

def render_pages(pdf, pages, dpi=110):
    tmp = tempfile.mkdtemp()
    imgs = []
    for p in pages:
        subprocess.run(["pdftoppm", "-r", str(dpi), "-f", str(p), "-l", str(p), "-png", pdf, os.path.join(tmp, f"p{p}")], check=True, capture_output=True)
        f = [x for x in os.listdir(tmp) if x.startswith(f"p{p}-") or x == f"p{p}.png"][0]
        imgs.append(Image.open(os.path.join(tmp, f)).convert("RGBA"))
    return imgs

def shadowed(im, ang):
    im = im.rotate(ang, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", (im.width + 60, im.height + 60), (0, 0, 0, 0)); sh.paste((0, 0, 0, 110), (30, 38), im.split()[3])
    return sh.filter(ImageFilter.GaussianBlur(16)), im

def fit(im, w):
    return im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)

def mockup(front, back, path):
    bg = Image.new("RGBA", (720, 560), "#eef1f6")
    bs, b = shadowed(fit(back, 300), -9); fs, f = shadowed(fit(front, 320), 6)
    bg.alpha_composite(bs, (250, 20)); bg.alpha_composite(b, (280, 42)); bg.alpha_composite(fs, (110, 70)); bg.alpha_composite(f, (140, 92))
    bg.convert("RGB").save(path, quality=86, optimize=True)

def banner(r, front, back, path):
    W, H = 1200, 630
    bg = Image.new("RGBA", (W, H), "#f5f7fb"); d = ImageDraw.Draw(bg)
    d.rectangle([0, H - 8, W, H], fill="#b48c2c")
    serif = ImageFont.truetype(F + "LiberationSerif-Bold.ttf", 46); sans = ImageFont.truetype(F + "LiberationSans-Regular.ttf", 20)
    small = ImageFont.truetype(F + "LiberationSans-Bold.ttf", 15); btn = ImageFont.truetype(F + "LiberationSans-Bold.ttf", 19)
    d.rounded_rectangle([70, 70, 300, 104], 17, fill="#f3ead3"); d.text((88, 78), f"FREE PDF  ·  {r['pages']} PAGES", font=small, fill="#8a6a1c")
    # headline: strip <em> tags; colour the em phrase gold
    hl = r["headline"]
    pre, rest = hl.split("<em>"); em, post = rest.split("</em>")
    y = 130; x = 70; maxw = 560
    words = [(w, "navy") for w in pre.split()] + [(w, "gold") for w in em.split()] + [(w, "navy") for w in post.split()]
    line_x = x
    for w, col in words:
        tw = d.textlength(w + " ", font=serif)
        if line_x + tw > x + maxw: y += 54; line_x = x
        d.text((line_x, y), w, font=serif, fill="#b48c2c" if col == "gold" else "#0b2545"); line_x += tw
    y += 74
    for ln in wrap(d, r["pitch"], sans, 560): d.text((70, y), ln, font=sans, fill="#3c4756"); y += 27
    y += 14
    for t in r["bullets"]:
        d.ellipse([72, y + 7, 84, y + 19], fill="#b48c2c"); d.text((96, y), t, font=sans, fill="#121b2b"); y += 32
    y = max(y + 14, 500)
    d.rounded_rectangle([70, y, 392, y + 50], 8, fill="#0b2545"); d.text((96, y + 13), "Email me the free worksheet", font=btn, fill="white")
    bs, b = shadowed(fit(back, 300), -9); fs, f = shadowed(fit(front, 320), 6)
    bg.alpha_composite(bs, (800, 60)); bg.alpha_composite(b, (830, 82)); bg.alpha_composite(fs, (690, 110)); bg.alpha_composite(f, (720, 132))
    bg.convert("RGB").save(path, quality=88, optimize=True)

def wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

if __name__ == "__main__":
    for r in RA + RB:
        pdf = os.path.join(OUT, r["slug"] + ".pdf")
        build(r["spec"], pdf)
        from pypdf import PdfReader
        n = len(PdfReader(pdf).pages)
        r["pages"] = n
        front, back = render_pages(pdf, [1, min(3, n)])
        mockup(front, back, os.path.join(OUT, r["slug"] + "-mockup.jpg"))
        banner(r, front, back, os.path.join(OUT, r["slug"] + "-cover.jpg"))
        print(f"{r['slug']}: {n} pages")
