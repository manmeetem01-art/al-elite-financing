"""Brand PDF builder for AL Elite lead magnets. A resource is a spec dict; blocks flow across pages
with automatic page breaks. Fillable fields via reportlab AcroForm."""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

NAVY, DEEP, GOLD, GOLDSOFT, INK, MUTED, LINE, SURFACE, PALE = [HexColor(c) for c in ("#0b2545", "#071a33", "#b48c2c", "#f3ead3", "#121b2b", "#6b7585", "#dde3ec", "#f5f7fb", "#c9d3e3")]
F = "/usr/share/fonts/truetype/liberation/"
for n, f in (("Serif", "LiberationSerif-Bold.ttf"), ("SerifR", "LiberationSerif-Regular.ttf"), ("Sans", "LiberationSans-Regular.ttf"), ("SansB", "LiberationSans-Bold.ttf")):
    pdfmetrics.registerFont(TTFont(n, F + f))
W, H = letter
M = 54
BOTTOM = 70
STATIC = os.path.join(os.path.dirname(__file__), "..", "static")


class Doc:
    def __init__(self, path, spec):
        self.c = canvas.Canvas(path, pagesize=letter)
        self.spec = spec
        self.c.setTitle(spec["title"]); self.c.setAuthor("AL Elite Financing"); self.c.setSubject(spec.get("subtitle", ""))
        self.form = self.c.acroForm
        self.n = 0; self.page = 0; self.y = H
        self.section_title = ""; self.step = ""

    # ---------- utilities
    def uid(self, p="f"):
        self.n += 1; return f"{p}{self.n}"

    def wrap(self, text, font, size, width):
        words, lines, cur = text.split(), [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if pdfmetrics.stringWidth(t, font, size) <= width: cur = t
            else: lines.append(cur); cur = w
        if cur: lines.append(cur)
        return lines

    def need(self, h):
        if self.y - h < BOTTOM:
            self.new_page()

    def header(self):
        c = self.c
        c.setFillColor(NAVY); c.rect(0, H - 58, W, 58, fill=1, stroke=0)
        c.setFillColor(GOLD); c.rect(0, H - 62, W, 4, fill=1, stroke=0)
        c.setFont("SansB", 9); c.setFillColor(GOLD); c.drawString(M, H - 24, "AL ELITE FINANCING  ·  " + self.spec["tag"].upper())
        c.setFont("Serif", 16); c.setFillColor(white); c.drawString(M, H - 45, self.section_title)
        if self.step:
            c.setFont("SansB", 11); c.setFillColor(GOLD); c.drawRightString(W - M, H - 45, self.step)

    def footer(self):
        c = self.c
        c.setStrokeColor(LINE); c.setLineWidth(1); c.line(M, 40, W - M, 40)
        c.setFont("Sans", 8); c.setFillColor(MUTED)
        c.drawString(M, 28, "alelitefinancing.com  ·  AL Elite is a matching service, not a lender. Not legal, tax, insurance or financial advice.")
        c.drawRightString(W - M, 28, f"Page {self.page}")

    def new_page(self):
        if self.page:
            self.footer(); self.c.showPage()
        self.page += 1
        self.header(); self.y = H - 95

    # ---------- blocks
    def section(self, title, step=None):
        self.section_title = title; self.step = step or ""
        self.new_page()

    def p(self, text, size=10, color=INK, font="Sans"):
        lines = self.wrap(text, font, size, W - 2 * M); lead = size * 1.4
        self.need(len(lines) * lead + 6)
        self.c.setFont(font, size); self.c.setFillColor(color)
        for ln in lines: self.c.drawString(M, self.y, ln); self.y -= lead
        self.y -= 6

    def h2(self, text):
        self.need(40)
        self.y -= 6
        self.c.setFont("Serif", 13); self.c.setFillColor(NAVY); self.c.drawString(M, self.y, text)
        self.c.setStrokeColor(GOLD); self.c.setLineWidth(1.5); self.c.line(M, self.y - 5, M + 28, self.y - 5); self.c.setLineWidth(1)
        self.y -= 22

    def check(self, items):
        for t in items:
            lines = self.wrap(t, "Sans", 9.5, W - 2 * M - 20)
            self.need(len(lines) * 12.5 + 6)
            self.form.checkbox(name=self.uid("c"), x=M, y=self.y - 4, size=12, borderColor=NAVY, fillColor=white, textColor=NAVY, borderWidth=1, buttonStyle="check")
            self.c.setFont("Sans", 9.5); self.c.setFillColor(INK)
            yy = self.y
            for ln in lines: self.c.drawString(M + 20, yy, ln); yy -= 12.5
            self.y = yy - 4
        self.y -= 4

    def numbered(self, items):
        for i, t in enumerate(items):
            lines = self.wrap(t, "Sans", 10, W - 2 * M - 24)
            self.need(len(lines) * 13.5 + 6)
            self.c.setFillColor(GOLD); self.c.circle(M + 6, self.y + 3, 7, fill=1, stroke=0)
            self.c.setFillColor(white); self.c.setFont("SansB", 9); self.c.drawCentredString(M + 6, self.y, str(i + 1))
            self.c.setFillColor(INK); self.c.setFont("Sans", 10)
            yy = self.y
            for ln in lines: self.c.drawString(M + 22, yy, ln); yy -= 13.5
            self.y = yy - 4
        self.y -= 4

    def fields(self, items, cols=2):
        """items: list of (label, hint) ; hint may be None. Laid out in a grid."""
        gap = 16; cw = (W - 2 * M - gap * (cols - 1)) / cols
        for i in range(0, len(items), cols):
            row = items[i:i + cols]
            has_hint = any(h for _, h in row)
            self.need(56 if has_hint else 46)
            for j, (label, hint) in enumerate(row):
                x = M + j * (cw + gap)
                self.c.setFont("SansB", 8); self.c.setFillColor(MUTED); self.c.drawString(x, self.y - 10, label.upper())
                self.form.textfield(name=self.uid(), x=x, y=self.y - 34, width=cw, height=20, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=9, borderWidth=1, tooltip=label)
                if hint:
                    self.c.setFont("Sans", 7.5); self.c.setFillColor(MUTED); self.c.drawString(x, self.y - 44, hint)
            self.y -= 56 if has_hint else 46

    def multi(self, label, h=56):
        self.need(h + 24)
        self.c.setFont("SansB", 8); self.c.setFillColor(MUTED); self.c.drawString(M, self.y - 10, label.upper())
        self.form.textfield(name=self.uid(), x=M, y=self.y - 14 - h, width=W - 2 * M, height=h, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=9, borderWidth=1, fieldFlags="multiline", tooltip=label)
        self.y -= h + 26

    def table(self, headers, rows, colw=None, label_col=True):
        """headers: list of str. rows: list of row labels (first column text). Remaining columns are fillable."""
        n = len(headers); total = W - 2 * M
        if not colw:
            first = 190 if label_col else total / n
            colw = [first] + [(total - first) / (n - 1)] * (n - 1) if label_col else [total / n] * n
        self.need(20 + 24 * min(len(rows), 3))
        x0 = M; top = self.y
        self.c.setFillColor(NAVY); self.c.rect(x0, self.y - 18, sum(colw), 20, fill=1, stroke=0)
        self.c.setFont("SansB", 9); self.c.setFillColor(white)
        for i, t in enumerate(headers): self.c.drawString(x0 + sum(colw[:i]) + 6, self.y - 12, t)
        self.y -= 20
        for i, r in enumerate(rows):
            if self.y - 24 < BOTTOM:
                self.c.setStrokeColor(LINE); self.c.rect(x0, self.y, sum(colw), top - self.y, fill=0, stroke=1)
                self.new_page(); top = self.y
                self.c.setFillColor(NAVY); self.c.rect(x0, self.y - 18, sum(colw), 20, fill=1, stroke=0)
                self.c.setFont("SansB", 9); self.c.setFillColor(white)
                for k, t in enumerate(headers): self.c.drawString(x0 + sum(colw[:k]) + 6, self.y - 12, t)
                self.y -= 20
            if i % 2 == 0:
                self.c.setFillColor(SURFACE); self.c.rect(x0, self.y - 24, sum(colw), 24, fill=1, stroke=0)
            bold = isinstance(r, str) and r.isupper()
            start = 0
            if label_col:
                self.c.setFont("SansB" if bold else "Sans", 9); self.c.setFillColor(INK); self.c.drawString(x0 + 6, self.y - 15, r); start = 1
            for j in range(start, n):
                self.form.textfield(name=self.uid("t"), x=x0 + sum(colw[:j]) + 3, y=self.y - 21, width=colw[j] - 6, height=18, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=9, borderWidth=0.5)
            self.y -= 24
        self.c.setStrokeColor(LINE); self.c.rect(x0, self.y, sum(colw), top - self.y, fill=0, stroke=1)
        self.y -= 14

    def calc(self, rows):
        """rows: (letter, label, hint, bold)"""
        for letter_, label, hint, bold in rows:
            self.need(42 if hint else 34)
            self.c.setFillColor(GOLD if bold else NAVY); self.c.roundRect(M, self.y - 20, 22, 22, 4, fill=1, stroke=0)
            self.c.setFont("SansB", 10); self.c.setFillColor(white); self.c.drawCentredString(M + 11, self.y - 13, letter_)
            self.c.setFont("SansB" if bold else "Sans", 10); self.c.setFillColor(INK); self.c.drawString(M + 32, self.y - 13, label)
            self.form.textfield(name=self.uid("g"), x=W - M - 150, y=self.y - 21, width=150, height=22, borderColor=GOLD if bold else LINE, fillColor=GOLDSOFT if bold else white, textColor=INK, fontName="Helvetica-Bold" if bold else "Helvetica", fontSize=10, borderWidth=1)
            if hint:
                self.c.setFont("Sans", 8); self.c.setFillColor(MUTED); self.c.drawString(M + 32, self.y - 25, hint)
            self.y -= 40 if hint else 32
        self.y -= 4

    def callout(self, title, text):
        lines = self.wrap(text, "Sans", 9.5, W - 2 * M - 24)
        hgt = len(lines) * 13 + 20 + (14 if title else 0)
        self.need(hgt + 10)
        self.c.setFillColor(GOLDSOFT); self.c.roundRect(M, self.y - hgt, W - 2 * M, hgt, 6, fill=1, stroke=0)
        self.c.setFillColor(GOLD); self.c.rect(M, self.y - hgt, 4, hgt, fill=1, stroke=0)
        yy = self.y - 16
        if title:
            self.c.setFont("SansB", 9.5); self.c.setFillColor(NAVY); self.c.drawString(M + 14, yy, title); yy -= 14
        self.c.setFont("Sans", 9.5); self.c.setFillColor(INK)
        for ln in lines: self.c.drawString(M + 14, yy, ln); yy -= 13
        self.y -= hgt + 10

    def cards(self, items):
        for t, d in items:
            lines = self.wrap(d, "Sans", 9, W - 2 * M - 20)
            hgt = 22 + len(lines) * 12
            self.need(hgt + 6)
            self.c.setFillColor(SURFACE); self.c.roundRect(M, self.y - hgt, W - 2 * M, hgt, 5, fill=1, stroke=0)
            self.c.setFont("SansB", 10); self.c.setFillColor(NAVY); self.c.drawString(M + 10, self.y - 14, t)
            self.c.setFont("Sans", 9); self.c.setFillColor(INK)
            yy = self.y - 28
            for ln in lines: self.c.drawString(M + 10, yy, ln); yy -= 12
            self.y -= hgt + 6
        self.y -= 4

    def tick_grid(self, items, cols=2):
        gap = 16; cw = (W - 2 * M - gap * (cols - 1)) / cols
        for i in range(0, len(items), cols):
            self.need(22)
            for j, t in enumerate(items[i:i + cols]):
                x = M + j * (cw + gap)
                self.form.checkbox(name=self.uid("c"), x=x, y=self.y - 14, size=12, borderColor=NAVY, fillColor=white, textColor=NAVY, borderWidth=1, buttonStyle="check")
                self.c.setFillColor(INK); self.c.setFont("Sans", 9.5); self.c.drawString(x + 18, self.y - 11, t)
            self.y -= 22
        self.y -= 6

    def cta(self, title, text):
        lines = self.wrap(text, "Sans", 9.5, W - 2 * M - 32)
        hgt = 36 + 13 * len(lines)
        self.need(hgt + 16)
        self.c.setFillColor(NAVY); self.c.roundRect(M, self.y - hgt, W - 2 * M, hgt, 6, fill=1, stroke=0)
        self.c.setFont("Serif", 13); self.c.setFillColor(white); self.c.drawString(M + 16, self.y - 22, title)
        self.c.setFont("Sans", 9.5); self.c.setFillColor(PALE)
        yy = self.y - 40
        for ln in lines: self.c.drawString(M + 16, yy, ln); yy -= 13
        self.y -= hgt + 10

    # ---------- cover and finish
    def cover(self):
        s = self.spec; c = self.c
        c.setFillColor(NAVY); c.rect(0, 0, W, H, fill=1, stroke=0)
        c.setFillColor(DEEP); c.rect(0, 0, W, 150, fill=1, stroke=0)
        c.setFillColor(GOLD); c.rect(0, 150, W, 5, fill=1, stroke=0)
        c.setFillColor(white); c.roundRect(M, H - 150, 150, 110, 8, fill=1, stroke=0)
        c.drawImage(os.path.join(STATIC, "logo.png"), M + 2, H - 148, width=146, height=106, mask="auto")
        c.setFont("SansB", 11); c.setFillColor(GOLD); c.drawString(M, H - 215, s["kicker"].upper())
        c.setFont("Serif", 36); c.setFillColor(white)
        y = H - 268
        for ln in s["title_lines"]: c.drawString(M, y, ln); y -= 44
        c.setFont("SerifR", 15); c.setFillColor(PALE); y -= 2
        for ln in self.wrap(s["subtitle"], "SerifR", 15, W - 2 * M - 40): c.drawString(M, y, ln); y -= 22
        y -= 26
        c.setFont("SansB", 10); c.setFillColor(GOLD); c.drawString(M, y, "INSIDE"); y -= 24
        for i, it in enumerate(s["inside"]):
            col, row = i % 2, i // 2
            c.setFillColor(GOLD); c.circle(M + 4 + col * 240, y + 3 - row * 20, 2.5, fill=1, stroke=0)
            c.setFillColor(white); c.setFont("Sans", 11); c.drawString(M + 14 + col * 240, y - row * 20, it)
        c.setFont("Sans", 10); c.setFillColor(PALE); c.drawString(M, 60, "alelitefinancing.com  ·  (888) 968-0079")
        c.setFont("Sans", 8.5); c.drawString(M, 44, "AL Elite Financing is a matching service, not a lender. This resource is general information, not legal, tax, insurance or financial advice.")
        c.showPage()

    def finish(self):
        self.footer(); self.c.showPage(); self.c.save()


def build(spec, out):
    d = Doc(out, spec)
    d.cover()
    spec["body"](d)
    d.finish()
    return out
