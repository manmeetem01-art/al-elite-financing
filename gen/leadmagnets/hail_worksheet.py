"""Builds the 'Hail Damage Roof Claim & Financing Worksheet' PDF (fillable) in AL Elite brand colours.
Run: python3 gen/leadmagnets/hail_worksheet.py  -> gen/static/resources/hail-roof-claim-worksheet.pdf"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

NAVY, DEEP, GOLD, GOLDSOFT, INK, MUTED, LINE, SURFACE = [HexColor(c) for c in ("#0b2545", "#071a33", "#b48c2c", "#f3ead3", "#121b2b", "#6b7585", "#dde3ec", "#f5f7fb")]
F = "/usr/share/fonts/truetype/liberation/"
pdfmetrics.registerFont(TTFont("Serif", F + "LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("SerifR", F + "LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Sans", F + "LiberationSans-Regular.ttf"))
pdfmetrics.registerFont(TTFont("SansB", F + "LiberationSans-Bold.ttf"))

OUT = os.path.join(os.path.dirname(__file__), "..", "static", "resources", "hail-roof-claim-worksheet.pdf")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
W, H = letter
M = 54  # margin
TITLE = "Hail Damage Roof Claim & Financing Worksheet"

c = canvas.Canvas(OUT, pagesize=letter)
c.setTitle(TITLE); c.setAuthor("AL Elite Financing"); c.setSubject("Worksheet for homeowners after hail damage")
form = c.acroForm
_n = [0]
def uid(prefix):
    _n[0] += 1
    return f"{prefix}_{_n[0]}"

def wrap(text, font, size, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def para(x, y, text, width, font="Sans", size=10, color=INK, leading=None):
    leading = leading or size * 1.4
    c.setFont(font, size); c.setFillColor(color)
    for ln in wrap(text, font, size, width):
        c.drawString(x, y, ln); y -= leading
    return y

def header(page_title, step=None):
    c.setFillColor(NAVY); c.rect(0, H - 58, W, 58, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(0, H - 62, W, 4, fill=1, stroke=0)
    c.setFont("SansB", 9); c.setFillColor(GOLD); c.drawString(M, H - 24, "AL ELITE FINANCING  ·  HAIL DAMAGE WORKSHEET")
    c.setFont("Serif", 16); c.setFillColor(white); c.drawString(M, H - 45, page_title)
    if step:
        c.setFont("SansB", 11); c.setFillColor(GOLD); c.drawRightString(W - M, H - 45, step)

def footer(n):
    c.setStrokeColor(LINE); c.line(M, 40, W - M, 40)
    c.setFont("Sans", 8); c.setFillColor(MUTED)
    c.drawString(M, 28, "alelitefinancing.com  ·  AL Elite is a matching service, not a lender. Not legal, tax or insurance advice.")
    c.drawRightString(W - M, 28, f"Page {n}")

def h2(x, y, text):
    c.setFont("Serif", 13); c.setFillColor(NAVY); c.drawString(x, y, text)
    c.setStrokeColor(GOLD); c.setLineWidth(1.5); c.line(x, y - 5, x + 28, y - 5); c.setLineWidth(1)
    return y - 20

def field(x, y, label, w, h=20, multiline=False, hint=None):
    c.setFont("SansB", 8); c.setFillColor(MUTED); c.drawString(x, y + h + 4, label.upper())
    form.textfield(name=uid("f"), x=x, y=y, width=w, height=h, borderColor=LINE, fillColor=white, textColor=INK,
                   fontName="Helvetica", fontSize=9, borderWidth=1, fieldFlags="multiline" if multiline else "", tooltip=label)
    if hint:
        c.setFont("Sans", 7.5); c.setFillColor(MUTED); c.drawString(x, y - 9, hint)

def check(x, y, text, width=W - 2 * M - 24):
    form.checkbox(name=uid("c"), x=x, y=y - 2, size=12, borderColor=NAVY, fillColor=white, textColor=NAVY, borderWidth=1, buttonStyle="check")
    return para(x + 20, y + 1, text, width - 20, size=9.5, leading=12.5) - 4

def callout(x, y, text, width, title=None):
    lines = wrap(text, "Sans", 9.5, width - 24)
    hgt = len(lines) * 13 + 20 + (14 if title else 0)
    c.setFillColor(GOLDSOFT); c.roundRect(x, y - hgt, width, hgt, 6, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(x, y - hgt, 4, hgt, fill=1, stroke=0)
    yy = y - 16
    if title:
        c.setFont("SansB", 9.5); c.setFillColor(NAVY); c.drawString(x + 14, yy, title); yy -= 14
    c.setFont("Sans", 9.5); c.setFillColor(INK)
    for ln in lines:
        c.drawString(x + 14, yy, ln); yy -= 13
    return y - hgt - 10

# ------------------------------------------------------------------ 1. Cover
c.setFillColor(NAVY); c.rect(0, 0, W, H, fill=1, stroke=0)
c.setFillColor(DEEP); c.rect(0, 0, W, 150, fill=1, stroke=0)
c.setFillColor(GOLD); c.rect(0, 150, W, 5, fill=1, stroke=0)
# logo card
logo = os.path.join(os.path.dirname(__file__), "..", "static", "logo.png")
c.setFillColor(white); c.roundRect(M, H - 150, 150, 110, 8, fill=1, stroke=0)
c.drawImage(logo, M + 2, H - 148, width=146, height=106, mask="auto")
c.setFont("SansB", 11); c.setFillColor(GOLD); c.drawString(M, H - 215, "FREE WORKSHEET  ·  FOR HOMEOWNERS AFTER A STORM")
c.setFont("Serif", 38); c.setFillColor(white)
c.drawString(M, H - 270, "Hail Damage Roof Claim")
c.drawString(M, H - 316, "& Financing Worksheet")
c.setFont("SerifR", 15); c.setFillColor(HexColor("#c9d3e3"))
y = H - 360
for ln in wrap("Document the damage, read your policy, compare the adjuster's estimate with your roofer's quote, and work out exactly how much you need to finance. Fill it in on screen or print it.", "SerifR", 15, W - 2 * M - 40):
    c.drawString(M, y, ln); y -= 22
c.setFont("SansB", 10); c.setFillColor(GOLD); c.drawString(M, H - 470, "INSIDE")
items = ["48-hour checklist", "Storm and claim record", "Policy decoder", "Estimate comparison table", "Financing gap calculator", "Contractor vetting checklist", "Financing options compared", "Timeline and notes"]
c.setFont("Sans", 11); c.setFillColor(white)
for i, it in enumerate(items):
    col, row = i % 2, i // 2
    c.setFillColor(GOLD); c.circle(M + 4 + col * 240, H - 494 - row * 20, 2.5, fill=1, stroke=0)
    c.setFillColor(white); c.drawString(M + 14 + col * 240, H - 497 - row * 20, it)
c.setFont("Sans", 10); c.setFillColor(HexColor("#c9d3e3"))
c.drawString(M, 60, "alelitefinancing.com  ·  (888) 968-0079")
c.setFont("Sans", 8.5); c.drawString(M, 44, "AL Elite Financing is a matching service, not a lender. This worksheet is general information, not legal, tax or insurance advice.")
c.showPage()

# ------------------------------------------------------------------ 2. How to use + 48 hour checklist
header("How to use this worksheet", "Step 1 of 7"); y = H - 95
y = para(M, y, "Hail claims go wrong in two places: the record you keep in the first 48 hours, and the gap between what the insurer pays and what the roof costs. This worksheet fixes both. Work through the steps in order; each one feeds the next. Fields are fillable on screen, or print and write.", W - 2 * M, size=10.5)
y -= 8
y = h2(M, y, "The first 48 hours")
y = check(M, y, "Photographed the roof from the ground and every soft metal: gutters, downspouts, window screens, AC fins, mailbox, patio furniture, cars. Hail leaves dents on metal long after shingles dry.")
y = check(M, y, "Noted the date and time of the storm and roughly how long it lasted. The insurer will check it against weather reports.")
y = check(M, y, "Made temporary repairs to stop active leaks (tarp or patch) and kept the receipts. Most policies expect you to prevent further damage and reimburse reasonable costs.")
y = check(M, y, "Did NOT climb a wet or damaged roof. Left the close inspection to a roofer with fall protection.")
y = check(M, y, "Took the card of any door-knocking roofer and signed nothing. A reputable roofer will still be there next week.")
y = check(M, y, "Found the policy declarations page (paper or online portal).")
y = check(M, y, "Filed the claim and wrote down the claim number (next page).")
y -= 6
y = callout(M, y, "Do not sign a contract that commits you to a roofer at 'whatever the insurance approves' before the adjuster has visited. Some storm contracts carry cancellation fees if you change your mind.", W - 2 * M, "Watch out")
y = h2(M, y, "Who to call, in order")
c.setFont("Sans", 10); c.setFillColor(INK)
for i, t in enumerate(["Your insurer or agent: file the claim, get the claim number.", "A licensed local roofer: inspect, document, meet the adjuster.", "Your mortgage servicer (if any): insurance checks are often made out to both of you.", "A lender or marketplace: only once you know the gap you need to finance."]):
    c.setFillColor(GOLD); c.circle(M + 6, y + 3, 7, fill=1, stroke=0); c.setFillColor(white); c.setFont("SansB", 9); c.drawCentredString(M + 6, y, str(i + 1))
    c.setFillColor(INK); c.setFont("Sans", 10); c.drawString(M + 22, y, t); y -= 20
footer(2); c.showPage()

# ------------------------------------------------------------------ 3. Storm and claim record
header("Storm and claim record", "Step 2 of 7"); y = H - 95
y = para(M, y, "Keep everything about the claim in one place. Adjusters, roofers and lenders will all ask for these details.", W - 2 * M)
y -= 20; cw = (W - 2 * M - 16) / 2
field(M, y - 20, "Date of storm", cw); field(M + cw + 16, y - 20, "Time / duration", cw); y -= 50
field(M, y - 20, "Property address", W - 2 * M); y -= 50
field(M, y - 20, "Insurance company", cw); field(M + cw + 16, y - 20, "Policy number", cw); y -= 50
field(M, y - 20, "Claim number", cw); field(M + cw + 16, y - 20, "Date claim filed", cw); y -= 50
field(M, y - 20, "Adjuster name", cw); field(M + cw + 16, y - 20, "Adjuster phone / email", cw); y -= 50
field(M, y - 20, "Adjuster visit date", cw); field(M + cw + 16, y - 20, "Roofer present at inspection? (Y/N, name)", cw); y -= 50
field(M, y - 20, "Mortgage servicer (if any) and claims dept. phone", W - 2 * M); y -= 56
y = h2(M, y, "Damage observed")
c.setFont("Sans", 9.5); c.setFillColor(INK)
cols = ["Shingles / bruising", "Gutters & downspouts", "Vents, flashing, pipe boots", "Siding", "Windows & screens", "AC unit fins", "Skylights", "Fence / deck / other"]
for i, t in enumerate(cols):
    col, row = i % 2, i // 2
    form.checkbox(name=uid("c"), x=M + col * (cw + 16), y=y - 14 - row * 20, size=12, borderColor=NAVY, fillColor=white, textColor=NAVY, borderWidth=1, buttonStyle="check")
    c.setFillColor(INK); c.setFont("Sans", 9.5); c.drawString(M + 18 + col * (cw + 16), y - 11 - row * 20, t)
y -= 100
field(M, y - 64, "Temporary repairs made and receipts (what, who, cost)", W - 2 * M, h=64, multiline=True)
footer(3); c.showPage()

# ------------------------------------------------------------------ 4. Policy decoder
header("Policy decoder", "Step 3 of 7"); y = H - 95
y = para(M, y, "Three things on the declarations page decide how much you'll pay yourself. Find each one and write it down before the adjuster visits.", W - 2 * M)
y -= 20
y = h2(M, y, "1. Your deductible")
y = para(M, y, "Many policies in hail states carry a separate wind and hail deductible set as a percentage of the dwelling coverage (often 1% or 2%). On a home insured for $350,000, a 2% deductible is $7,000, not $1,000.", W - 2 * M, size=9.5)
y -= 24
field(M, y - 20, "Dwelling coverage amount ($)", cw, hint="Coverage A on the declarations page"); field(M + cw + 16, y - 20, "Wind/hail deductible (% or $)", cw, hint="If a %, multiply by Coverage A"); y -= 58
field(M, y - 20, "Deductible in dollars ($)", cw); field(M + cw + 16, y - 20, "Other (all-perils) deductible ($)", cw); y -= 58
y = h2(M, y, "2. Replacement cost or actual cash value?")
y = para(M, y, "Replacement-cost (RCV) policies pay in two parts: a first check at depreciated value, then the held-back depreciation once the roof is finished and invoiced, usually within a deadline. Actual-cash-value (ACV) policies pay only the depreciated value, so an older roof can leave a large permanent gap.", W - 2 * M, size=9.5)
y -= 6
form.checkbox(name=uid("c"), x=M, y=y - 14, size=12, borderColor=NAVY, fillColor=white, textColor=NAVY, borderWidth=1, buttonStyle="check"); c.setFont("Sans", 9.5); c.setFillColor(INK); c.drawString(M + 18, y - 11, "Replacement cost (RCV)")
form.checkbox(name=uid("c"), x=M + 200, y=y - 14, size=12, borderColor=NAVY, fillColor=white, textColor=NAVY, borderWidth=1, buttonStyle="check"); c.drawString(M + 218, y - 11, "Actual cash value (ACV)")
form.checkbox(name=uid("c"), x=M + 380, y=y - 14, size=12, borderColor=NAVY, fillColor=white, textColor=NAVY, borderWidth=1, buttonStyle="check"); c.drawString(M + 398, y - 11, "Not sure, ask agent")
y -= 44
field(M, y - 20, "Deadline to complete work and claim depreciation", cw, hint="Often 6 to 24 months from the loss date; check the policy"); field(M + cw + 16, y - 20, "Roof age (years) and install date", cw); y -= 58
y = h2(M, y, "3. Roof schedules and exclusions")
y = para(M, y, "Newer policies may pay roofs on an age schedule (a falling percentage as the roof ages), apply ACV to the roof only, or exclude cosmetic damage to metal. Ask your agent which of these apply.", W - 2 * M, size=9.5)
y -= 24
field(M, y - 52, "Notes from the agent (schedule, exclusions, matching rules)", W - 2 * M, h=52, multiline=True)
footer(4); c.showPage()

# ------------------------------------------------------------------ 5. Estimate comparison
header("Estimate comparison", "Step 4 of 7"); y = H - 95
y = para(M, y, "Put the adjuster's estimate and your roofer's itemized quote side by side. Differences are normal; your roofer can submit a supplement with photos for anything the adjuster missed.", W - 2 * M)
y -= 14
rows = ["Tear-off and disposal", "Shingles (squares)", "Underlayment", "Ice & water shield", "Drip edge and flashing", "Ridge, vents, pipe boots", "Decking replacement (per sheet)", "Gutters and downspouts", "Code upgrades / permits", "Siding, screens, other", "Labor / overhead & profit", "TOTAL"]
x0 = M; colw = [190, 100, 100, 114]
c.setFillColor(NAVY); c.rect(x0, y - 18, sum(colw), 20, fill=1, stroke=0)
c.setFont("SansB", 9); c.setFillColor(white)
for i, t in enumerate(["Line item", "Adjuster ($)", "Roofer ($)", "Difference / note"]):
    c.drawString(x0 + sum(colw[:i]) + 6, y - 12, t)
y -= 20
for i, r in enumerate(rows):
    if i % 2 == 0:
        c.setFillColor(SURFACE); c.rect(x0, y - 24, sum(colw), 24, fill=1, stroke=0)
    c.setFont("SansB" if r == "TOTAL" else "Sans", 9); c.setFillColor(INK); c.drawString(x0 + 6, y - 15, r)
    for j in range(1, 4):
        form.textfield(name=uid("t"), x=x0 + sum(colw[:j]) + 3, y=y - 21, width=colw[j] - 6, height=18, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=9, borderWidth=0.5)
    y -= 24
c.setStrokeColor(LINE); c.rect(x0, y, sum(colw), 20 + 24 * len(rows), fill=0, stroke=1)
y -= 16
y = callout(M, y, "Ask for the full estimate, not the summary. Check that replacement cost value (RCV), depreciation, actual cash value (ACV) and the deductible are all shown. If the adjuster missed decking, drip edge or a second shingle layer, ask the roofer to file a supplement.", W - 2 * M, "How to read the adjuster's estimate")
footer(5); c.showPage()

# ------------------------------------------------------------------ 6. Gap calculator
header("Financing gap calculator", "Step 5 of 7"); y = H - 95
y = para(M, y, "Most homeowners don't need to finance the roof. They need to cover two gaps: a short-term one until depreciation is released, and a permanent one made of the deductible and items the policy doesn't pay for. Fill in the boxes from your estimate.", W - 2 * M)
y -= 16
def calc_row(y, letter_, label, hint=None, bold=False):
    c.setFillColor(GOLD if bold else NAVY); c.roundRect(M, y - 20, 22, 22, 4, fill=1, stroke=0)
    c.setFont("SansB", 10); c.setFillColor(white); c.drawCentredString(M + 11, y - 13, letter_)
    c.setFont("SansB" if bold else "Sans", 10); c.setFillColor(INK); c.drawString(M + 32, y - 13, label)
    form.textfield(name=uid("g"), x=W - M - 150, y=y - 21, width=150, height=22, borderColor=GOLD if bold else LINE, fillColor=GOLDSOFT if bold else white, textColor=INK, fontName="Helvetica-Bold" if bold else "Helvetica", fontSize=10, borderWidth=1)
    if hint:
        c.setFont("Sans", 8); c.setFillColor(MUTED); c.drawString(M + 32, y - 25, hint)
    return y - (40 if hint else 32)
y = calc_row(y, "A", "Roofer's contract price", "From the itemized quote (including any extras you chose)")
y = calc_row(y, "B", "Insurer's replacement cost value (RCV)", "From the adjuster's estimate, after any approved supplements")
y = calc_row(y, "C", "Depreciation held back until completion", "Shown on the estimate; $0 on an ACV-only policy")
y = calc_row(y, "D", "Your deductible in dollars", "From the policy decoder page")
y = calc_row(y, "E", "First insurance check  =  B − C − D", bold=True)
y = calc_row(y, "F", "Owed to roofer before depreciation arrives  =  A − E", "Short-term gap. Ask the roofer whether they will wait for the second check.", bold=True)
y = calc_row(y, "G", "Permanent gap  =  A − B + D", "The deductible plus anything the policy doesn't cover. This is what you actually finance.", bold=True)
y -= 4
y = callout(M, y, "Worked example: contract $18,500 (A), RCV $17,200 (B), depreciation $4,100 (C), deductible $3,000 (D). First check = 17,200 − 4,100 − 3,000 = $10,100 (E). Owed before depreciation = 18,500 − 10,100 = $8,400 (F). Permanent gap = 18,500 − 17,200 + 3,000 = $4,300 (G). Financing $4,300 at an illustrative 11.99% APR over 36 months is about $143 a month.", W - 2 * M, "Example")
y = para(M, y, "Illustrative only. Rates and approval come from lenders. Use the roof financing calculator at alelitefinancing.com/tools/roof-financing-calculator/ to try your own numbers.", W - 2 * M, size=8.5, color=MUTED)
footer(6); c.showPage()

# ------------------------------------------------------------------ 7. Contractor vetting
header("Contractor vetting checklist", "Step 6 of 7"); y = H - 95
y = para(M, y, "Financing problems usually start as contractor problems. Run every roofer through this list before you sign either the roofing contract or a loan application.", W - 2 * M)
y -= 12
y = h2(M, y, "Must-haves")
for t in ["State license or registration verified (where your state requires one)", "Certificate of liability insurance and workers' compensation, dated and in the company's name", "Local physical address and a phone number that was in service before the storm", "Reviews that predate the storm, not only the last two weeks", "Written, itemized quote on the same scope as the adjuster's estimate", "Permits included and pulled by the contractor", "Written warranty for workmanship (separate from the manufacturer's)"]:
    y = check(M, y, t)
y -= 6
y = h2(M, y, "Walk away if")
for t in ["They offer to waive, absorb or 'cover' your deductible. Illegal in several states, including Texas and Colorado, and a sign the job will be priced around the insurance payout.", "They want the whole job paid up front, or cash only.", "They push you to sign the loan application before the roofing contract, or ask you to sign a partly blank form.", "The contract binds you to them at 'whatever insurance approves' with a cancellation fee.", "They steer you to one lender and won't let you compare."]:
    y = check(M, y, t)
y -= 6
field(M, y - 44, "Roofer 1: company, license #, quote $, notes", W - 2 * M, h=44, multiline=True); y -= 70
field(M, y - 44, "Roofer 2: company, license #, quote $, notes", W - 2 * M, h=44, multiline=True)
footer(7); c.showPage()

# ------------------------------------------------------------------ 8. Financing options + timeline + notes
header("Financing options and timeline", "Step 7 of 7"); y = H - 95
y = para(M, y, "Borrow against the gap (G), not the roof price (A). Compare each option on APR including fees, total cost, speed and whether it puts a lien on your home.", W - 2 * M)
y -= 12
opts = [("Unsecured personal loan", "Days to fund; no lien; APR depends on credit. Fits most deductible-sized gaps."),
        ("Roofer-arranged plan", "Convenient at the kitchen table; ask if 0% is deferred interest and whether a dealer fee is in the price."),
        ("HELOC or home equity loan", "Lower rate, weeks to close, secured by the home. Better for large gaps on ACV policies."),
        ("Savings plus a small loan", "Often cheapest: pay the deductible from savings, finance only uncovered items.")]
for t, d in opts:
    c.setFillColor(SURFACE); c.roundRect(M, y - 36, W - 2 * M, 36, 5, fill=1, stroke=0)
    c.setFont("SansB", 10); c.setFillColor(NAVY); c.drawString(M + 10, y - 14, t)
    c.setFont("Sans", 9); c.setFillColor(INK); c.drawString(M + 10, y - 28, d)
    y -= 42
y -= 4
y = h2(M, y, "Questions to ask every lender")
for t in ["What is the APR including fees, and is the rate fixed?", "Is there an origination fee, and is it deducted from the loan?", "Is any promotional period deferred interest or waived interest?", "Is there a prepayment penalty?", "Does checking my options use a soft or hard credit inquiry?"]:
    y = check(M, y, t)
y -= 6
y = h2(M, y, "Timeline")
tl = [("Day 0-2", "Photos, temporary repairs, claim filed"), ("Week 1-3", "Roofer inspection, adjuster visit, estimates compared"), ("Week 2-4", "Gap calculated, financing compared, contract signed"), ("Install", "Keep the final invoice, permits and photos"), ("After", "Submit for depreciation, pay down any bridge loan")]
for i, (a, b) in enumerate(tl):
    c.setFont("SansB", 9); c.setFillColor(GOLD); c.drawString(M, y, a)
    c.setFont("Sans", 9.5); c.setFillColor(INK); c.drawString(M + 70, y, b)
    form.textfield(name=uid("d"), x=W - M - 110, y=y - 5, width=110, height=16, borderColor=LINE, fillColor=white, textColor=INK, fontName="Helvetica", fontSize=8, borderWidth=0.5, tooltip="Date done")
    y -= 22
y -= 2
field(M, y - 56, "Notes", W - 2 * M, h=56, multiline=True)
y -= 72
c.setFillColor(NAVY); c.roundRect(M, y - 54, W - 2 * M, 54, 6, fill=1, stroke=0)
c.setFont("Serif", 13); c.setFillColor(white); c.drawString(M + 16, y - 22, "Ready to compare financing for the gap?")
c.setFont("Sans", 9.5); c.setFillColor(HexColor("#c9d3e3")); c.drawString(M + 16, y - 40, "alelitefinancing.com/roof-financing/ reaches lenders who fund roofs in your state. Or call (888) 968-0079.")
footer(8); c.showPage()
c.save()
print("wrote", OUT)
