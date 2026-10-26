"""Brand snapshot cards (1200x675 PNG) for each city and state page: name, primary risk, the rule that matters,
projects most financed, suburbs count. Data from cities.CITIES and local_content; no stock photos."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from PIL import Image, ImageDraw, ImageFont
from cities import CITIES, by_state
from local_content import CITY, STATE, STATE_SLUG

OUT = os.path.join(os.path.dirname(__file__), "..", "static", "locations", "cards"); os.makedirs(OUT, exist_ok=True)
F = "/usr/share/fonts/truetype/liberation/"
serif = ImageFont.truetype(F + "LiberationSerif-Bold.ttf", 60); serif_s = ImageFont.truetype(F + "LiberationSerif-Bold.ttf", 30)
sans = ImageFont.truetype(F + "LiberationSans-Regular.ttf", 22); sansb = ImageFont.truetype(F + "LiberationSans-Bold.ttf", 18); tiny = ImageFont.truetype(F + "LiberationSans-Regular.ttf", 17)

RULE = {"Texas": "Deductible waivers illegal (Ins. Code ch. 707)", "Colorado": "Deductible rebates illegal (C.R.S. 10-4-110.8)", "Oklahoma": "Roofers must register; no deductible rebates", "Kansas": "Roofer registration; no deductible rebates", "Minnesota": "Licensed contractors; storm-contract cancel rights", "Florida": "State-licensed roofers; AOB reformed 2023", "Missouri": "Local licensing; roof age schedules common", "Nebraska": "Depreciation held until completion", "Indiana": "Local licensing; RCV vs ACV matters", "Tennessee": "State licence above threshold", "Utah": "DOPL-licensed trades", "Arizona": "ROC licence required for most work", "Georgia": "State licence for larger projects", "North Carolina": "GC licence above state threshold", "Illinois": "Licensed roofers; written contracts over $1,000", "Ohio": "State-licensed HVAC, plumbing, electrical", "Pennsylvania": "HIC registration with Attorney General"}
EXPOSURE = {"Texas": "Led U.S. hail payouts in 2025", "Missouri": "Top 3 hail payouts in 2025", "Colorado": "Front Range hail corridor", "Oklahoma": "Hail and tornado belt", "Kansas": "Hail and tornado belt", "Nebraska": "Spring to summer hail", "Indiana": "Hail + winter ice", "Minnesota": "Summer hail + ice dams", "Florida": "Hurricane; roof age drives insurance", "Tennessee": "Spring storms and tornadoes", "Utah": "Sun and snow load; age-driven", "Arizona": "Extreme heat and monsoon", "Georgia": "Humid summers and severe storms", "North Carolina": "Storms, humidity, hurricane remnants", "Illinois": "Top 3 hail payouts in 2025; hard winters", "Ohio": "Spring hail and winter cold", "Pennsylvania": "Old housing; nor'easters"}

def wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= width: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def tile(d, x, y, w, h, label, value, font=serif_s):
    d.rounded_rectangle([x, y, x + w, y + h], 12, fill="#ffffff", outline="#dde3ec")
    d.text((x + 18, y + 14), label.upper(), font=sansb, fill="#b48c2c")
    yy = y + 44
    for ln in wrap(d, value, font, w - 36)[:3]:
        d.text((x + 18, yy), ln, font=font, fill="#0b2545"); yy += font.size + 6

def card(name, sub, exposure, rule, projects, footer, path):
    im = Image.new("RGB", (1200, 675), "#f5f7fb"); d = ImageDraw.Draw(im)
    d.rectangle([0, 0, 1200, 120], fill="#0b2545"); d.rectangle([0, 120, 1200, 126], fill="#b48c2c")
    d.text((60, 28), "AL ELITE FINANCING  ·  LOCAL SNAPSHOT", font=sansb, fill="#b48c2c")
    d.text((60, 56), name, font=serif, fill="white")
    d.text((1140 - d.textlength(sub, font=sans), 66), sub, font=sans, fill="#c9d3e3")
    tile(d, 60, 160, 340, 150, "Primary exposure", exposure)
    tile(d, 430, 160, 340, 150, "Rule that matters", rule, font=ImageFont.truetype(F + "LiberationSerif-Bold.ttf", 26))
    tile(d, 800, 160, 340, 150, "Most financed", projects)
    d.rounded_rectangle([60, 340, 1140, 560], 12, fill="#ffffff", outline="#dde3ec")
    d.text((78, 356), "HOW FINANCING WORKS HERE", font=sansb, fill="#b48c2c")
    steps = ["1. Itemized quotes from licensed local contractors (and the adjuster's estimate if a claim is involved)", "2. Tell us the project, amount and timeline; no credit pull", "3. We match you with lenders who fund this work in your state; soft-inquiry options shown first", "4. You choose and apply with the lender; rates and decisions are theirs"]
    yy = 390
    for st in steps:
        for ln in wrap(d, st, sans, 1030): d.text((78, yy), ln, font=sans, fill="#121b2b"); yy += 30
        yy += 6
    d.text((60, 600), footer, font=tiny, fill="#6b7585")
    d.text((1140 - d.textlength("alelitefinancing.com  ·  A matching service, not a lender", font=tiny), 600), "alelitefinancing.com  ·  A matching service, not a lender", font=tiny, fill="#6b7585")
    im.save(path, optimize=True)

if __name__ == "__main__":
    for c in CITIES:
        city, state, ab, p = c[0], c[1], c[2], c[3]
        lc = CITY[city]
        proj = lc["services"].split(".")[0]
        proj = proj.replace(" lead", "").replace(" leads", "")
        card(f"{city}, {ab}", f"{state}  ·  {len(lc['suburbs'])} suburbs covered", EXPOSURE[state], RULE[state], proj, f"Serving {', '.join(lc['suburbs'][:6])} and more", os.path.join(OUT, p.strip('/').split('/')[-1] + ".png"))
    for st, sh in STATE.items():
        metros = ", ".join(c[0] for c in by_state()[st])
        card(st, f"{len(by_state()[st])} local guide(s)", EXPOSURE[st], RULE[st], "Roofs, HVAC, kitchens, fences, generators, foundations", f"Local guides: {metros}", os.path.join(OUT, STATE_SLUG[st] + ".png"))
    print("cards:", len(os.listdir(OUT)))
