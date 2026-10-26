"""October 2026 batch C: homeowner posts for the services other than roofing (kitchen, bathroom, fence,
foundation, generator, water heater, siding). Topics picked from Ahrefs: 'how much does a kitchen remodel
cost' 1.9k, 'bathroom remodel cost' 11k, 'how much does a fence cost' 2.9k, 'does homeowners insurance
cover foundation repair' 1k, 'whole house generator cost' 5.1k, 'water heater replacement cost' 16k,
'siding replacement cost' 1.9k. Cost ranges are typical national ranges from cost guides and contractor
quotes, stated as ranges; the posts tell readers to get local quotes. Payments are computed."""
from common import *

HOME = ("Home", "/")
BLOG = ("Blog", "/blog/")
DATE = "2026-10-26"

def pm(P, apr, n):
    return money(payment(P, apr, n), False)

def ti(P, apr, n):
    return money(payment(P, apr, n) * n - P, False)

def ptable(amounts, apr=10.99, terms=(36, 60, 84, 120)):
    head = "".join(f"<th class='num'>{t} mo</th>" for t in terms)
    rows = "".join(f"<tr><td><strong>{money(P, False)}</strong></td>" + "".join(f"<td class='num'>{pm(P, apr, t)}</td>" for t in terms) + "</tr>" for P in amounts)
    return f"<div class='tbl'><table><thead><tr><th>Project cost</th>{head}</tr></thead><tbody>{rows}</tbody></table></div><p class='cap'>Illustrative monthly payments at {apr}% APR, standard amortization, no fees. Lenders set real rates after reviewing an application. Not an offer of credit.</p>"

LENDER_QS = """<ol><li>What is the APR including fees, and is the rate fixed?</li><li>Is there an origination fee, and is it deducted from the loan amount?</li><li>Is any promotional period deferred interest or waived interest?</li><li>Is there a prepayment penalty?</li><li>When is the contractor paid, and when does my first payment start?</li><li>Does checking my options use a soft or hard credit inquiry?</li></ol>"""

def vet(trade):
    return ("Choosing the contractor", f"""<p>The quote is only as good as the company behind it. Get two or three itemized quotes from licensed, insured {trade} on the same scope, confirm permits are included, and check reviews that go back more than a season. Read any financing documents separately from the work contract: the loan is with the lender, not the contractor. The Federal Trade Commission's guide to hiring a contractor, linked in the sources below, lists the warning signs, including pressure to pay the whole job up front and steering you to a lender before you've seen a written price.</p>""")


# ------------------------------------------------------------------ 1. kitchen
KITCHEN = dict(
    path="/blog/how-much-does-a-kitchen-remodel-cost/", date=DATE,
    crumbs=[HOME, BLOG, ("Kitchen remodel cost", "/blog/how-much-does-a-kitchen-remodel-cost/")],
    eyebrow="Homeowner guide", h1="How much does a kitchen remodel cost? Prices by scope and what it means per month",
    title="How Much Does a Kitchen Remodel Cost? Prices by Scope (2026)",
    meta="Kitchen remodel costs by scope, from a refresh to a full gut, where the money goes, ways to trim the number, and what each budget looks like as a monthly payment.",
    answer="A kitchen remodel commonly runs from about $15,000 to $30,000 for a refresh (paint, counters, hardware, appliances), $30,000 to $75,000 for a mid-range remodel with new cabinets and layout tweaks, and $75,000 or more for a full gut with moved plumbing and walls. Cabinets, labor and countertops take the largest shares. Financed at an illustrative 10.99% APR, a $40,000 remodel is about $869 a month over five years or $551 over ten.",
    money_page=("kitchen remodel financing", "/remodel-financing/kitchen/"), project="Kitchen or bathroom remodel",
    sections=[
        ("Kitchen remodel cost by scope", """<p>National cost guides and contractor quotes put most kitchen projects into three bands. Your local labor rates, the size of the kitchen and the finishes you choose move you within them.</p>
<ul><li><strong>Refresh, roughly $15,000 to $30,000.</strong> Keep the layout and most cabinets. New counters, sink and faucet, paint or refaced cabinet fronts, lighting, backsplash, and appliances. Often two to four weeks of work.</li>
<li><strong>Mid-range remodel, roughly $30,000 to $75,000.</strong> New semi-custom cabinets, stone or quartz counters, new flooring, updated electrical and plumbing in place, and sometimes a removed wall or an island. Six to ten weeks is typical.</li>
<li><strong>Major or custom remodel, $75,000 and up.</strong> Moved plumbing and gas lines, structural changes, custom cabinetry, high-end appliances and finishes. Three months or more, with permits and inspections.</li></ul>
<p>Small kitchens in lower-cost regions sit under these bands; large kitchens in expensive metros sit above them. Two or three local quotes on the same scope tell you where you really are.</p>"""),
        ("Where the money goes", """<p>Industry breakdowns and contractor estimates tend to land in similar proportions:</p>
<ul><li><strong>Cabinets and hardware:</strong> often the largest single line, roughly a quarter to a third of a mid-range budget.</li>
<li><strong>Labor and installation:</strong> around a fifth to a quarter, more where trades are expensive.</li>
<li><strong>Appliances:</strong> a wide range, from a few thousand dollars to well into five figures for pro-style ranges and built-in refrigeration.</li>
<li><strong>Countertops:</strong> quartz and granite by the square foot plus fabrication; laminate is a fraction of the price.</li>
<li><strong>Plumbing, electrical and lighting:</strong> modest if nothing moves, significant if you relocate the sink or add circuits.</li>
<li><strong>Flooring, backsplash, paint, demo and disposal, permits, design fees:</strong> the rest.</li></ul>
<p>Knowing the proportions helps you cut intelligently. Trading custom for semi-custom cabinets saves more than choosing cheaper hardware.</p>"""),
        ("Ways to bring the number down", """<ul><li><strong>Keep plumbing where it is.</strong> Moving the sink or dishwasher adds plumbing, electrical and often flooring work.</li>
<li><strong>Reface or repaint cabinets</strong> if the boxes are sound.</li>
<li><strong>Mix finishes:</strong> quartz on the island, laminate or butcher block on the perimeter.</li>
<li><strong>Buy appliances during sale seasons</strong> and resist the pro-style range unless you cook like a pro.</li>
<li><strong>Phase the work:</strong> counters and backsplash now, cabinets next year, if that suits your cash flow better than financing everything at once.</li>
<li><strong>Get an itemized quote</strong> so you can see which lines are driving the price.</li></ul>"""),
        ("What a kitchen remodel costs per month", f"""<p>Most kitchens are financed. Here's how the three cost bands look as monthly payments at an illustrative rate.</p>{ptable((20000, 40000, 60000, 90000), terms=(60, 84, 120, 144))}
<p>Longer terms lower the payment but add interest: $40,000 over 60 months costs about {ti(40000, 10.99, 60)} in interest at 10.99%, and about {ti(40000, 10.99, 144)} over 144 months. Choose the shortest term with a comfortable payment and confirm there's no prepayment penalty.</p>"""),
        ("How to pay for it", """<p>Four routes cover nearly every kitchen:</p>
<ul><li><strong>Unsecured personal loan.</strong> Funds in days, no lien on the home, fixed rate. Suits refreshes and mid-range remodels up to the lender's cap.</li>
<li><strong>Home equity loan or HELOC.</strong> Usually the lowest rate per dollar for large remodels if you have equity and a few weeks. Closing costs apply; a HELOC's rate is usually variable.</li>
<li><strong>Contractor financing.</strong> A monthly figure next to the quote, sometimes promotional. Ask whether the price is the same for cash.</li>
<li><strong>FHA 203(k) or cash-out refinance.</strong> Folds the remodel into a mortgage; sensible for very large projects or when buying a fixer-upper, rarely sensible if your current mortgage rate is low.</li></ul>
<p>Our <a href="/remodel-financing/kitchen/">kitchen remodel financing</a> page compares these with example payments, and our guide to <a href="/blog/heloc-vs-roof-loan/">home equity loans vs HELOCs vs unsecured loans</a> covers the trade-offs in detail.</p>"""),
        ("Questions to ask every lender", LENDER_QS),
        vet("remodelers or kitchen design-build firms"),
    ],
    faqs=[
        ("What is a realistic budget for a kitchen remodel?", "For most homes, $15,000 to $30,000 for a refresh, $30,000 to $75,000 for a mid-range remodel with new cabinets, and $75,000 or more for a full gut. Local quotes decide where you land."),
        ("Does a kitchen remodel add value to a home?", "Usually some, but rarely the full cost. Mid-range remodels tend to recoup a larger share than high-end ones. Remodel for how you'll live in the kitchen, not only for resale."),
        ("How long does a kitchen remodel take?", "A refresh takes a few weeks; a mid-range remodel six to ten; a full gut three months or more, depending on permits, cabinet lead times and inspections."),
        ("Can I finance a kitchen remodel with fair credit?", "Yes, though at higher APRs and sometimes smaller amounts. A co-applicant, a smaller scope or a home equity option can improve terms."),
    ],
    related=[("Kitchen remodel financing", "/remodel-financing/kitchen/"), ("Bathroom remodel cost", "/blog/how-much-does-a-bathroom-remodel-cost/"), ("Home improvement financing", "/home-improvement-financing/"), ("HELOC vs home equity loan vs unsecured loan", "/blog/heloc-vs-roof-loan/")],
)

# ------------------------------------------------------------------ 2. bathroom
BATHROOM = dict(
    path="/blog/how-much-does-a-bathroom-remodel-cost/", date=DATE,
    crumbs=[HOME, BLOG, ("Bathroom remodel cost", "/blog/how-much-does-a-bathroom-remodel-cost/")],
    eyebrow="Homeowner guide", h1="Bathroom remodel cost: what a small, mid-range and master bath remodel runs",
    title="Bathroom Remodel Cost: Small, Mid-Range & Master Bath Prices (2026)",
    meta="Bathroom remodel costs by scope, tub-to-shower conversions, accessibility remodels, where the money goes, and what each budget looks like as a monthly payment.",
    answer="A bathroom remodel commonly runs about $8,000 to $15,000 for a small hall bath with fixtures in place, $15,000 to $35,000 for a mid-range remodel with new tile, vanity and a tub-to-shower conversion, and $35,000 to $75,000 or more for a master bath with moved plumbing. Tile labor, plumbing and the shower or tub are the big lines. Financed at an illustrative 10.99% APR, a $20,000 bathroom is about $435 a month over five years.",
    money_page=("bathroom remodel financing", "/remodel-financing/bathroom/"), project="Kitchen or bathroom remodel",
    sections=[
        ("Bathroom remodel cost by scope", """<ul><li><strong>Small or hall bath refresh, roughly $8,000 to $15,000.</strong> New vanity, toilet, faucet, lighting, paint, maybe new flooring. Plumbing stays put.</li>
<li><strong>Mid-range remodel, roughly $15,000 to $35,000.</strong> New tile on floor and walls, a tub-to-shower conversion or new tub, new vanity and counter, exhaust fan and lighting updates.</li>
<li><strong>Master bath or full gut, $35,000 to $75,000+.</strong> Moved plumbing, a double vanity, a walk-in tiled shower with a custom pan, freestanding tub, heated floors, and often a new layout.</li></ul>
<p>Bathrooms cost more per square foot than almost any other room because everything is plumbed, waterproofed and tiled. A one-day acrylic shower conversion from a specialty company sits at the low end of the mid-range band; a custom tiled shower sits at the top.</p>"""),
        ("Where the money goes", """<ul><li><strong>Labor:</strong> often the largest share. Tile setters, plumbers and electricians are skilled trades.</li>
<li><strong>Shower or tub:</strong> from a prefabricated unit to a tiled shower with glass enclosure, the single biggest swing in the budget.</li>
<li><strong>Tile and waterproofing:</strong> material by the square foot plus installation; waterproofing done properly is not where to save.</li>
<li><strong>Vanity, counter, sink, faucet, toilet, lighting and exhaust fan.</strong></li>
<li><strong>Plumbing and electrical</strong> if anything moves or needs updating to code.</li>
<li><strong>Permits, demolition and disposal.</strong></li></ul>"""),
        ("Accessibility and aging-in-place remodels", """<p>Curbless showers, grab bars, comfort-height toilets, wider doors and non-slip flooring are increasingly common remodels, and they're often needed on a timeline set by a fall or a diagnosis rather than a budget cycle. Some states, local programs and the VA offer grants or low-interest loans for accessibility work; ask before you finance the whole job. Timing matters: lining up financing before the need becomes urgent gives you time to compare offers.</p>"""),
        ("Bathroom remodel cost per month", f"""{ptable((10000, 20000, 35000, 55000), terms=(36, 60, 84, 120))}
<p>A $20,000 bathroom over 60 months costs about {ti(20000, 10.99, 60)} in interest at 10.99%; over 120 months about {ti(20000, 10.99, 120)}. A shorter term usually makes sense on a bathroom because the amounts are moderate and the room will last decades.</p>"""),
        ("How to pay for a bathroom remodel", """<p>Unsecured personal loans and contractor plans cover most bathrooms and fund quickly; one-day shower companies in particular lean on promotional financing, so check whether the 0% offer is deferred interest and whether the price is the same for cash. For a master bath or a full gut with moved plumbing, a home equity loan or HELOC may be cheaper if you have equity and time. Our <a href="/remodel-financing/bathroom/">bathroom remodel financing</a> page compares the options with example payments. If you're also planning a kitchen, see <a href="/blog/how-much-does-a-kitchen-remodel-cost/">how much a kitchen remodel costs</a>.</p>"""),
        ("Questions to ask every lender", LENDER_QS),
        vet("bathroom remodelers"),
    ],
    faqs=[
        ("How much should I budget for a bathroom remodel?", "Roughly $8,000 to $15,000 for a small bath refresh, $15,000 to $35,000 for a mid-range remodel, and $35,000 or more for a master bath with moved plumbing. Local quotes decide the exact number."),
        ("What is the most expensive part of a bathroom remodel?", "Usually labor, followed by the shower or tub. A custom tiled shower with glass can cost more than everything else in a small bathroom combined."),
        ("How long does a bathroom remodel take?", "A refresh takes a week or two; a mid-range remodel three to five weeks; a full master bath six to ten weeks, depending on tile work, custom orders and inspections."),
        ("Can I finance a bathroom remodel?", "Yes. Unsecured loans, contractor plans and home equity products all cover bathroom remodels. Smaller jobs suit short unsecured terms; large remodels may be cheaper through home equity."),
    ],
    related=[("Bathroom remodel financing", "/remodel-financing/bathroom/"), ("Kitchen remodel cost", "/blog/how-much-does-a-kitchen-remodel-cost/"), ("Home improvement financing", "/home-improvement-financing/"), ("Plumbing financing", "/plumbing-financing/")],
)

# ------------------------------------------------------------------ 3. fence
FENCE = dict(
    path="/blog/how-much-does-a-fence-cost/", date=DATE,
    crumbs=[HOME, BLOG, ("Fence cost", "/blog/how-much-does-a-fence-cost/")],
    eyebrow="Homeowner guide", h1="How much does a fence cost? Price per foot by material, and how to pay for it",
    title="How Much Does a Fence Cost? Price Per Foot by Material (2026)",
    meta="Fence cost per linear foot for wood, vinyl, chain link, aluminum and composite, what drives the price, typical yard totals, and how to pay for a new fence monthly.",
    answer="Installed fence prices commonly run about $10 to $25 per linear foot for chain link, $15 to $35 for pressure-treated wood privacy fence, $20 to $45 for vinyl, $25 to $60 for aluminum, and $30 to $60 or more for composite. A typical suburban backyard of 150 to 200 linear feet therefore lands roughly between $3,000 and $10,000, with gates, slopes, removal of an old fence and permits adding to it.",
    money_page=("fence financing", "/fence-financing/"), project="Fence or deck",
    sections=[
        ("Fence cost per linear foot by material", """<p>Prices below are typical installed ranges from national cost guides and contractor quotes. Material prices, local labor and how hard your yard is to work in move you within them.</p>
<div class='tbl'><table><thead><tr><th>Material</th><th class='num'>Installed, per linear foot</th><th>Notes</th></tr></thead><tbody>
<tr><td>Chain link</td><td class='num'>$10 to $25</td><td>Cheapest; taller and vinyl-coated cost more</td></tr>
<tr><td>Pressure-treated wood privacy (6 ft)</td><td class='num'>$15 to $35</td><td>Cedar and redwood higher; needs staining</td></tr>
<tr><td>Vinyl privacy</td><td class='num'>$20 to $45</td><td>Low maintenance; wide price spread by thickness</td></tr>
<tr><td>Aluminum ornamental</td><td class='num'>$25 to $60</td><td>Pool code compliant styles available</td></tr>
<tr><td>Composite</td><td class='num'>$30 to $60+</td><td>Longest life; highest up-front cost</td></tr>
<tr><td>Wrought iron</td><td class='num'>$40 to $100+</td><td>Custom; often repair rather than replace</td></tr>
</tbody></table></div><p class='cap'>Typical ranges; your quotes will vary by region, height, style and site conditions.</p>"""),
        ("What a whole yard costs", """<p>Multiply the per-foot price by the perimeter you're fencing, then add the extras. A few typical scenarios:</p>
<ul><li><strong>Small backyard, 120 linear feet of chain link:</strong> roughly $1,500 to $3,000.</li>
<li><strong>Suburban backyard, 180 feet of 6-foot wood privacy fence with two gates:</strong> roughly $3,500 to $7,500.</li>
<li><strong>Same yard in vinyl:</strong> roughly $4,500 to $9,000.</li>
<li><strong>Corner lot, 300 feet of aluminum with a double driveway gate:</strong> roughly $9,000 to $20,000.</li></ul>
<p>Gates add a few hundred dollars each for walk gates and more for driveway or automated gates. Removing and hauling an old fence, rocky or sloped ground, long post-hole digs in clay, and HOA-required styles all add cost. Permits are usually modest but required in many cities.</p>"""),
        ("Ways to lower the price", """<ul><li><strong>Fence only the sides you need</strong>; share a line with a neighbour where both parties agree in writing.</li>
<li><strong>Choose standard heights and styles.</strong> Custom lattice tops and decorative posts add up.</li>
<li><strong>Buy material in a slow season</strong> if your installer passes on supplier pricing.</li>
<li><strong>Get three quotes on the same footage and spec</strong>; fence pricing varies more between companies than most trades.</li>
<li><strong>Check HOA and setback rules first</strong> so you don't pay for a fence you have to move.</li></ul>"""),
        ("Fence cost per month", f"""<p>Fences are a mid-size purchase, so short terms keep interest small.</p>{ptable((4000, 7000, 12000, 20000), terms=(24, 36, 60, 84))}
<p>A $7,000 fence over 36 months costs about {ti(7000, 10.99, 36)} in interest at 10.99%; stretched to 84 months it costs about {ti(7000, 10.99, 84)}. Unless cash is very tight, a two- or three-year term is the sensible range.</p>"""),
        ("How to pay for a new fence", """<p>Three common routes. Many fence companies offer financing through a lender partner, presented at the quote; ask whether a promotional rate carries a dealer fee in the price. An unsecured personal loan funds in days and pays any installer like cash, which often gets you the cash price. A 0% APR credit card can work for a small fence you'll pay off inside the promotional window. Home equity products rarely make sense for a fence-sized purchase because of closing costs and timing. Our <a href="/fence-financing/">fence financing</a> page compares these with example payments.</p>"""),
        ("Questions to ask every lender", LENDER_QS),
        vet("fence installers"),
    ],
    faqs=[
        ("How much does a 6-foot privacy fence cost?", "Installed, commonly $15 to $35 per linear foot in pressure-treated wood and $20 to $45 in vinyl. For 150 to 200 feet that's roughly $2,500 to $9,000 before gates and extras."),
        ("Is it cheaper to build a fence yourself?", "Materials are typically a third to a half of the installed price, so DIY saves money if you have the tools, time and a level yard. Post setting and gate hanging are where DIY fences most often go wrong."),
        ("Do I need a permit for a fence?", "Many cities require one, especially for fences over a certain height or near property lines. Your installer usually handles it; ask whether it's in the quote."),
        ("Can you finance a fence?", "Yes. Fence installers often offer financing, and unsecured personal loans cover fences from a few thousand dollars up, usually over two to seven years."),
    ],
    related=[("Fence financing", "/fence-financing/"), ("Deck financing", "/deck-financing/"), ("Home improvement financing", "/home-improvement-financing/"), ("Siding replacement cost", "/blog/siding-replacement-cost/")],
)

# ------------------------------------------------------------------ 4. foundation
FOUNDATION = dict(
    path="/blog/does-insurance-cover-foundation-repair/", date=DATE,
    crumbs=[HOME, BLOG, ("Insurance and foundation repair", "/blog/does-insurance-cover-foundation-repair/")],
    eyebrow="Homeowner guide", h1="Does homeowners insurance cover foundation repair? What's covered, what isn't, and what it costs",
    title="Does Homeowners Insurance Cover Foundation Repair? (2026 Guide)",
    meta="When homeowners insurance covers foundation repair and when it doesn't, typical foundation repair costs for cracks, piers and waterproofing, and how to pay for the rest.",
    answer="Usually not. Standard homeowners policies exclude foundation damage from settling, soil movement, poor drainage, tree roots and wear, which cause most foundation problems. They typically do cover foundation damage from a sudden, covered event such as a burst pipe, a fire, a vehicle impact or, with the right endorsement, an earthquake or sinkhole. Repair costs commonly range from a few hundred dollars for crack injection to $10,000 to $30,000 or more for piering, so most homeowners finance the work.",
    money_page=("foundation repair financing", "/foundation-repair-financing/"), project="Foundation repair",
    sections=[
        ("What homeowners insurance usually excludes", """<p>Policies are written around sudden, accidental events. Foundation problems are usually slow, so the common causes are excluded by name:</p>
<ul><li><strong>Settling, shifting and cracking</strong> over time.</li>
<li><strong>Expansive or shrinking soil</strong>, the main cause of foundation movement in clay-soil regions such as Texas, Oklahoma and Colorado.</li>
<li><strong>Poor drainage, hydrostatic pressure and groundwater</strong> seeping through basement walls.</li>
<li><strong>Tree roots</strong> drying out soil under the slab.</li>
<li><strong>Faulty construction or workmanship.</strong></li>
<li><strong>Flooding</strong> (separate flood insurance) and, without an endorsement, <strong>earthquakes and sinkholes</strong>.</li></ul>
<p>Read the "exclusions" and "earth movement" sections of your policy; the wording decides your claim.</p>"""),
        ("When foundation damage is covered", """<p>Coverage is more likely when a covered peril caused the damage:</p>
<ul><li>A <strong>burst or leaking pipe under the slab</strong> that washes out soil (the water damage itself is often covered; the resulting foundation repair sometimes is, depending on policy language).</li>
<li><strong>Fire, explosion, lightning or a vehicle hitting the house.</strong></li>
<li><strong>Earthquake or sinkhole</strong> if you bought that endorsement (sinkhole coverage is a specific add-on in states like Florida).</li>
<li><strong>Collapse</strong> from hidden decay or insect damage, in some policies.</li></ul>
<p>If you believe a covered event caused the damage, document it before repairs: photos, a plumber's leak report, and an independent structural engineer's assessment of cause. Insurers deny foundation claims routinely, so the cause evidence matters more than in most claims.</p>"""),
        ("What foundation repair costs", """<div class='tbl'><table><thead><tr><th>Repair</th><th class='num'>Typical range</th><th>When it's used</th></tr></thead><tbody>
<tr><td>Crack injection (epoxy or polyurethane)</td><td class='num'>$500 to $3,000</td><td>Non-structural cracks, leaks</td></tr>
<tr><td>Carbon fibre or steel wall bracing</td><td class='num'>$3,000 to $15,000</td><td>Bowing basement walls</td></tr>
<tr><td>Slab jacking / polyurethane lifting</td><td class='num'>$2,000 to $10,000</td><td>Sunken slabs, uneven floors</td></tr>
<tr><td>Steel push or helical piers</td><td class='num'>$1,000 to $3,000 per pier; $10,000 to $30,000+ for a typical job</td><td>Settlement; number of piers drives the total</td></tr>
<tr><td>Basement waterproofing and drainage</td><td class='num'>$5,000 to $15,000</td><td>Interior drain tile, sump, exterior membranes</td></tr>
<tr><td>Full foundation replacement</td><td class='num'>$40,000 to $100,000+</td><td>Rare; severe failure</td></tr>
</tbody></table></div><p class='cap'>Typical ranges from cost guides and contractor quotes. Get an independent engineer's report and two or three quotes on the same scope.</p>"""),
        ("How to pay for foundation repair", f"""<p>Because insurance rarely helps, most homeowners finance the whole repair. Options:</p>
<ul><li><strong>Unsecured personal loan</strong> for repairs up to the lender's cap; funds in days, no lien.</li>
<li><strong>Contractor financing</strong> offered by many foundation companies through lender partners.</li>
<li><strong>Home equity loan or HELOC</strong> for large pier jobs, if the home has equity; note that an appraiser will see the foundation issue, so get the engineer's report and a repair plan first.</li>
<li><strong>Government-backed programs:</strong> FHA Title I property improvement loans cover structural repairs through HUD-approved lenders, and USDA Section 504 offers repair loans and grants to eligible rural homeowners.</li></ul>
{ptable((5000, 12000, 25000, 40000), terms=(36, 60, 84, 120))}
<p>Our <a href="/foundation-repair-financing/">foundation repair financing</a> page compares these options with example payments. Because structural work can't wait long, compare offers quickly with soft-pull pre-qualification rather than applying everywhere at once.</p>"""),
        ("Questions to ask every lender", LENDER_QS),
        vet("foundation contractors, and insist on an independent structural engineer's report before signing with any of them"),
    ],
    faqs=[
        ("Does insurance cover foundation cracks?", "Not when the cracks come from settling, soil movement or drainage. Cracks caused by a covered event such as a burst pipe or a vehicle impact may be covered. The cause, documented by an engineer or plumber, decides it."),
        ("Does insurance cover foundation repair from a plumbing leak?", "Often partly. The water damage from a sudden leak is usually covered; whether the resulting foundation repair is covered depends on the policy's wording about earth movement and the leak being sudden rather than long-term."),
        ("How much does foundation repair cost on average?", "Minor crack repairs run a few hundred to a few thousand dollars; piering typically $10,000 to $30,000 or more depending on the number of piers; waterproofing $5,000 to $15,000."),
        ("Can I finance foundation repair with bad credit?", "Options exist at higher APRs, and government-backed programs may help eligible homeowners. A smaller scope, a co-applicant and a soft-pull pre-qualification improve your chances."),
    ],
    related=[("Foundation repair financing", "/foundation-repair-financing/"), ("Does insurance cover roof replacement?", "/blog/does-insurance-cover-roof-replacement/"), ("Home improvement financing", "/home-improvement-financing/"), ("Plumbing financing", "/plumbing-financing/")],
)

# ------------------------------------------------------------------ 5. generator
GENERATOR = dict(
    path="/blog/whole-house-generator-cost/", date=DATE,
    crumbs=[HOME, BLOG, ("Whole house generator cost", "/blog/whole-house-generator-cost/")],
    eyebrow="Homeowner guide", h1="Whole house generator cost: unit, installation, fuel and what it looks like per month",
    title="Whole House Generator Cost: Installed Prices & Monthly Payments (2026)",
    meta="What a whole house standby generator costs installed, by size, plus transfer switch, gas line, permits and running costs, and what each budget means as a monthly payment.",
    answer="A whole house standby generator typically costs $7,000 to $15,000 installed for a home-sized unit (roughly 14 to 24 kW), and $15,000 to $25,000 or more for larger homes or difficult installs. The unit itself is often $3,000 to $7,000; the automatic transfer switch, electrical work, gas or propane connection, concrete pad and permits make up the rest. Financed at an illustrative 10.99% APR, a $12,000 system is about $261 a month over five years.",
    money_page=("generator financing", "/generator-financing/"), project="Generator",
    sections=[
        ("Whole house generator cost by size", """<p>Standby generators are sized by kilowatts. The right size depends on which circuits you want running during an outage: essentials only (fridge, furnace blower, some lights and outlets) needs far less than whole-house with central AC.</p>
<div class='tbl'><table><thead><tr><th>Size</th><th>Covers</th><th class='num'>Unit price (typical)</th><th class='num'>Installed total (typical)</th></tr></thead><tbody>
<tr><td>10 to 14 kW</td><td>Essentials, small home</td><td class='num'>$3,000 to $5,000</td><td class='num'>$7,000 to $11,000</td></tr>
<tr><td>18 to 24 kW</td><td>Most of an average home incl. one AC</td><td class='num'>$5,000 to $7,500</td><td class='num'>$10,000 to $16,000</td></tr>
<tr><td>26 to 38 kW</td><td>Large home, multiple AC units</td><td class='num'>$7,500 to $15,000</td><td class='num'>$15,000 to $25,000+</td></tr>
</tbody></table></div><p class='cap'>Typical ranges for air-cooled and small liquid-cooled units from cost guides and installer quotes. Brand, region and site conditions change the numbers.</p>"""),
        ("What's in the installation price", """<ul><li><strong>Automatic transfer switch (ATS)</strong> and panel work: the switch that moves the house to generator power without you doing anything.</li>
<li><strong>Gas or propane connection:</strong> a new natural gas line or a propane tank and regulator. Long runs from the meter add cost.</li>
<li><strong>Concrete or composite pad</strong>, placement clearances from windows and doors, and sometimes trenching.</li>
<li><strong>Permits and inspections</strong> for electrical and gas work.</li>
<li><strong>Startup, load testing and the first service.</strong></li></ul>
<p>Installation is often as much as the unit. Quotes that look cheap sometimes exclude the gas line or the transfer switch, so compare itemized quotes.</p>"""),
        ("Running and maintenance costs", """<p>A standby generator runs a self-test weekly and needs an annual service (oil, filters, spark plugs), commonly a couple of hundred dollars a year or a service plan. Fuel during an outage depends on load: a mid-size unit on natural gas can consume several dollars an hour at full load, and propane customers need tank capacity for multi-day outages. Battery backups for the controller need replacing every few years. Budget a few hundred dollars a year on top of any loan payment.</p>"""),
        ("Is a whole house generator worth it?", """<p>It depends on how often and how long your power goes out, what's at stake when it does, and whether a smaller option would do. For homes with a sump pump, medical equipment, a home office, well water or freezers full of food, in areas with ice storms, hurricanes or an unreliable grid, the answer is often yes. For short, rare outages a portable generator with a manual transfer switch, or a battery backup for a few circuits, costs a fraction. Standby generators can also matter for insurance of basements against sump failure, and some buyers value them at resale in storm states. Our <a href="/locations/">location guides</a> cover the storm markets where they're most common.</p>"""),
        ("Generator cost per month", f"""{ptable((8000, 12000, 16000, 22000), terms=(36, 60, 84, 120))}
<p>Financing before storm season, when installers have capacity, is usually faster and cheaper than after an outage. Our <a href="/generator-financing/">generator financing</a> page compares unsecured loans, installer plans and home equity options with example payments.</p>"""),
        ("Questions to ask every lender", LENDER_QS),
        vet("licensed electricians or certified generator dealers (gas work must be done by a licensed plumber or gas fitter in most states)"),
    ],
    faqs=[
        ("How much does a Generac whole house generator cost installed?", "Brand-name home standby units commonly land in the $7,000 to $16,000 installed range for home-sized models, more for larger liquid-cooled units. The installation often costs as much as the unit."),
        ("How big a generator do I need for my house?", "Most average homes run on 18 to 24 kW if you want central AC covered, and 10 to 14 kW for essentials only. A dealer load calculation is the reliable way to size it."),
        ("Does a whole house generator increase home value?", "Often somewhat, especially in storm-prone areas, but rarely the full cost. Buy it for the outages, not the resale."),
        ("Can I finance a whole house generator?", "Yes. Unsecured loans, installer financing plans and home equity products all cover standby generators; the lender pays the installer when the system is commissioned."),
    ],
    related=[("Generator financing", "/generator-financing/"), ("Roof financing after hail damage", "/blog/roof-financing-after-hail-damage/"), ("HVAC financing", "/hvac-financing/"), ("Storm-market locations", "/locations/")],
)

# ------------------------------------------------------------------ 6. water heater
WATER = dict(
    path="/blog/water-heater-replacement-cost/", date=DATE,
    crumbs=[HOME, BLOG, ("Water heater replacement cost", "/blog/water-heater-replacement-cost/")],
    eyebrow="Homeowner guide", h1="Water heater replacement cost: tank, tankless and heat pump prices, and how to pay today",
    title="Water Heater Replacement Cost: Tank, Tankless & Heat Pump (2026)",
    meta="Water heater replacement costs for tank, tankless and heat pump units, what drives the price, when to repair instead, and how to finance an emergency replacement.",
    answer="Replacing a standard tank water heater commonly costs $1,200 to $2,500 installed; a tankless unit $3,000 to $6,000 installed; a heat pump (hybrid) water heater $2,500 to $5,000 installed, often with utility rebates. Prices rise with venting changes, gas line or electrical upgrades, code items like expansion tanks and pans, and emergency same-day service. Most replacements are financed on the spot through the plumber's plan or a short unsecured loan.",
    money_page=("water heater financing", "/water-heater-financing/"), project="Plumbing or water heater",
    sections=[
        ("Water heater replacement cost by type", """<div class='tbl'><table><thead><tr><th>Type</th><th class='num'>Installed (typical)</th><th>Pros</th><th>Cons</th></tr></thead><tbody>
<tr><td>Conventional tank, gas or electric (40 to 50 gal)</td><td class='num'>$1,200 to $2,500</td><td>Cheapest, fastest swap</td><td>Lowest efficiency, 8 to 12 year life</td></tr>
<tr><td>High-efficiency or power-vent tank</td><td class='num'>$2,000 to $3,500</td><td>Better efficiency, flexible venting</td><td>Higher price</td></tr>
<tr><td>Tankless, gas</td><td class='num'>$3,000 to $6,000</td><td>Endless hot water, 20+ year life, space saving</td><td>Venting and gas line upgrades; higher install</td></tr>
<tr><td>Heat pump (hybrid) electric</td><td class='num'>$2,500 to $5,000</td><td>Very low running cost, rebates common</td><td>Needs space and warm air; slower recovery</td></tr>
</tbody></table></div><p class='cap'>Typical installed ranges from cost guides and plumber quotes. Removal, permits, pans, expansion tanks and venting changes can add several hundred dollars.</p>"""),
        ("What pushes the price up", """<ul><li><strong>Code upgrades:</strong> expansion tank, drain pan, seismic strapping, new shut-offs and a pressure-reducing valve may be required when the unit is replaced.</li>
<li><strong>Venting and gas:</strong> switching to tankless or power-vent often needs new venting and a larger gas line.</li>
<li><strong>Electrical:</strong> heat pump and electric tankless units may need new circuits.</li>
<li><strong>Access:</strong> attic or crawlspace units cost more to swap.</li>
<li><strong>Emergency service:</strong> same-day or weekend replacement carries a premium. If you can live without hot water for a day, you can often save it.</li></ul>"""),
        ("Repair or replace?", """<p>Replace if the tank is leaking from the body (not a fitting), if the unit is past about 10 to 12 years for a tank, or if repairs are approaching half the cost of a new unit. Repair if it's a failed heating element, thermostat, thermocouple, pilot assembly or pressure-relief valve on a younger unit; those are typically a few hundred dollars. Rusty water, rumbling and slow recovery on an older tank usually mean replacement is close either way.</p>"""),
        ("How to pay for a water heater today", f"""<p>Because water heaters fail without warning, most are replaced the same day. Plumbers and HVAC companies commonly offer financing through a lender partner at the quote; a fast unsecured loan is the alternative and pays any plumber like cash. Amounts are modest, so short terms make sense.</p>{ptable((1500, 2500, 4000, 6000), terms=(12, 24, 36, 60))}
<p>A $2,500 tank over 24 months costs about {ti(2500, 10.99, 24)} in interest at 10.99%; over 60 months about {ti(2500, 10.99, 60)}. If a tankless upgrade qualifies for a utility rebate, apply it before financing. Our <a href="/water-heater-financing/">water heater financing</a> page covers the options, and <a href="/plumbing-financing/">plumbing financing</a> covers repipes and sewer lines if the problem is bigger than the heater.</p>"""),
        ("Questions to ask every lender", LENDER_QS),
        vet("plumbers"),
    ],
    faqs=[
        ("How much does it cost to replace a 50 gallon water heater?", "Commonly $1,200 to $2,500 installed for a standard gas or electric tank, more if venting, gas line or code items need updating."),
        ("Is a tankless water heater worth the extra cost?", "For households that run out of hot water, want to save space, or plan to stay 10+ years, often yes: tankless units last longer and use less energy. For a small household with a working venting setup, a high-efficiency tank is usually the better value."),
        ("Can I finance a water heater?", "Yes. Plumbers commonly offer financing through lender partners, and unsecured personal loans cover replacements from about $1,000 up. Short terms keep total interest low."),
        ("Does homeowners insurance cover a water heater?", "Usually not the heater itself when it fails from age, but sudden water damage it causes may be covered. Check your policy and photograph any damage."),
    ],
    related=[("Water heater financing", "/water-heater-financing/"), ("Plumbing financing", "/plumbing-financing/"), ("Furnace and AC replacement financing", "/blog/furnace-and-ac-replacement-financing/"), ("HVAC financing with bad credit", "/blog/how-to-get-hvac-financing-with-bad-credit/")],
)

# ------------------------------------------------------------------ 7. siding
SIDING = dict(
    path="/blog/siding-replacement-cost/", date=DATE,
    crumbs=[HOME, BLOG, ("Siding replacement cost", "/blog/siding-replacement-cost/")],
    eyebrow="Homeowner guide", h1="Siding replacement cost: vinyl, fiber cement, wood and metal, per square foot and per house",
    title="Siding Replacement Cost: Vinyl, Fiber Cement, Wood & Metal (2026)",
    meta="Siding replacement cost per square foot by material, typical whole-house totals, what adds to the price, storm damage and insurance, and what it looks like per month.",
    answer="Installed siding commonly runs about $4 to $8 per square foot for vinyl, $8 to $15 for fiber cement, $6 to $12 for engineered wood, $8 to $20 for natural wood and $10 to $20 for steel or aluminum. For a typical home with 1,800 to 2,500 square feet of exterior wall, that's roughly $8,000 to $20,000 in vinyl and $15,000 to $40,000 in fiber cement, before removal of old siding, trim, house wrap and repairs to the sheathing underneath.",
    money_page=("siding financing", "/siding-financing/"), project="Siding, gutters or windows",
    sections=[
        ("Siding cost per square foot by material", """<div class='tbl'><table><thead><tr><th>Material</th><th class='num'>Installed, per sq ft</th><th>Life</th><th>Notes</th></tr></thead><tbody>
<tr><td>Vinyl</td><td class='num'>$4 to $8</td><td>20 to 40 yrs</td><td>Cheapest; insulated vinyl costs more</td></tr>
<tr><td>Engineered wood</td><td class='num'>$6 to $12</td><td>30+ yrs</td><td>Wood look, lower maintenance</td></tr>
<tr><td>Fiber cement</td><td class='num'>$8 to $15</td><td>50 yrs</td><td>Fire and hail resistant; heavy, needs skilled crew</td></tr>
<tr><td>Natural wood (cedar, redwood)</td><td class='num'>$8 to $20</td><td>20 to 40 yrs with upkeep</td><td>Needs staining or painting</td></tr>
<tr><td>Steel or aluminum</td><td class='num'>$10 to $20</td><td>40+ yrs</td><td>Hail resistant; dents can show</td></tr>
<tr><td>Brick or stone veneer</td><td class='num'>$15 to $40+</td><td>50+ yrs</td><td>Usually accents, not whole house</td></tr>
</tbody></table></div><p class='cap'>Typical installed ranges from cost guides and contractor quotes, including labor. Removal of old siding, house wrap, trim and sheathing repairs are extra.</p>"""),
        ("Whole-house totals and what adds to them", """<p>Measure the exterior wall area (perimeter times height, minus windows and doors, plus gables) and multiply by the per-foot price, then add:</p>
<ul><li><strong>Removal and disposal</strong> of old siding, more for asbestos-containing siding on older homes.</li>
<li><strong>House wrap, flashing and trim</strong>, which should always be replaced.</li>
<li><strong>Sheathing repairs</strong> where water got behind the old siding; budget a contingency.</li>
<li><strong>Two-story or complex homes</strong> with many gables, corners and windows cost more per square foot.</li>
<li><strong>Insulation upgrades</strong> (foam board under new siding) if you want them.</li></ul>
<p>Two or three quotes on the same material and scope will show you the real local range quickly.</p>"""),
        ("Storm damage, insurance and matching", """<p>Hail and wind are the most common reasons for sudden siding replacement in the Plains, Midwest and Gulf states. Insurance often pays for damaged elevations, and whether it pays to replace undamaged sides so the house matches depends on your policy and your state's matching rules; discontinued vinyl colours are a frequent source of dispute. If a claim is involved, finance only the gap between the insurer's payment and the contractor's price, not the whole job. Our guide to <a href="/blog/roof-financing-after-hail-damage/">roof financing after hail damage</a> explains the claim process, which is the same for siding.</p>"""),
        ("Siding cost per month", f"""{ptable((9000, 15000, 25000, 40000), terms=(60, 84, 120, 144))}
<p>Siding lasts decades, so a longer term is more defensible than for a fence or a water heater, but total interest still climbs: $15,000 over 60 months costs about {ti(15000, 10.99, 60)} in interest at 10.99%, and about {ti(15000, 10.99, 144)} over 144 months.</p>"""),
        ("How to pay for siding", """<p>Siding companies lean heavily on promotional financing; ask whether the 0% offer is deferred or waived interest and whether the price is the same for cash. Unsecured personal loans cover most vinyl and engineered wood jobs and fund in days. Fiber cement or whole-house jobs in high-cost metros may justify a home equity loan or HELOC if you have equity and time. Some utilities offer rebates for insulated siding or added exterior insulation. Our <a href="/siding-financing/">siding financing</a> page compares the options with example payments.</p>"""),
        ("Questions to ask every lender", LENDER_QS),
        vet("siding contractors"),
    ],
    faqs=[
        ("How much does it cost to side a 2,000 square foot house?", "Roughly $8,000 to $20,000 in vinyl and $15,000 to $40,000 in fiber cement for a home with about 1,800 to 2,500 square feet of wall area, before old-siding removal and repairs. Local quotes decide the exact number."),
        ("What is the cheapest siding to install?", "Vinyl, at roughly $4 to $8 per square foot installed. Engineered wood and fiber cement cost more but last longer and resist hail and fire better."),
        ("Does insurance cover siding replacement?", "For storm damage from hail or wind, often yes for the damaged areas. Whether undamaged sides are replaced to match depends on your policy and state rules. Wear and age are not covered."),
        ("Can I finance new siding?", "Yes. Siding contractors commonly offer financing, and unsecured loans or home equity products cover whole-house jobs. Compare APR after any promotional period and the cash price."),
    ],
    related=[("Siding financing", "/siding-financing/"), ("Window replacement financing", "/window-financing/"), ("Fence cost", "/blog/how-much-does-a-fence-cost/"), ("Roof financing after hail damage", "/blog/roof-financing-after-hail-damage/")],
)

ARTICLES_C = [KITCHEN, BATHROOM, FENCE, FOUNDATION, GENERATOR, WATER, SIDING]


# ------------------------------------------------------------------ depth pass: three more sections per post, inserted before the lender questions
_MORE = {
 "/blog/how-much-does-a-kitchen-remodel-cost/": [
  ("A worked example: the $42,000 mid-range kitchen", f"""<p>A 180-square-foot kitchen in a suburban home, layout unchanged, island added. Semi-custom cabinets $13,500, quartz counters $5,200, appliances $7,800, flooring $3,100, backsplash and tile $1,900, plumbing and electrical in place $3,600, lighting $1,400, demo and disposal $1,200, paint and finishing $1,300, permits and design $1,000, contractor overhead and profit $2,000: about $42,000. The homeowners cut $4,000 by choosing a standard range instead of a pro-style one and refacing the pantry cabinets rather than replacing them, and financed the rest at an illustrative 10.99% over 84 months, about {pm(38000, 10.99, 84)} a month. The point of the exercise is that every line is a decision, not a given.</p>"""),
  ("Regional differences and timing", """<p>The same remodel can cost 30% to 50% more in coastal metros than in the Midwest or South, almost entirely from labor. Cabinet lead times (six to twelve weeks for semi-custom, longer for custom) set the schedule, so order before demolition. Late winter and early spring are often easier to book than summer and the run-up to the holidays. If you're financing, line up the loan before you sign the contract so a deposit is ready when cabinets are ordered.</p>"""),
  ("Mistakes that blow the budget", """<ul><li><strong>No contingency.</strong> Hidden water damage, old wiring and uneven floors show up after demo; keep 10% to 15% aside.</li><li><strong>Changing the plan mid-build.</strong> Change orders are priced at a premium and delay everything.</li><li><strong>Buying appliances last.</strong> Cabinet and counter dimensions depend on them.</li><li><strong>Financing the whole job on a promotional card</strong> you can't clear in time; deferred interest on $40,000 is painful.</li><li><strong>Skipping the itemized quote.</strong> A single number hides where the money goes and makes comparing bids impossible.</li></ul>"""),
 ],
 "/blog/how-much-does-a-bathroom-remodel-cost/": [
  ("A worked example: the $19,000 hall bath", f"""<p>A 5-by-8-foot hall bath, fixtures in place. Tub-to-shower conversion with a tiled shower and glass door $7,800, floor tile $1,600, vanity, counter and faucet $2,200, toilet $450, lighting and exhaust fan $900, plumbing updates $1,500, electrical $700, demo and disposal $800, paint and accessories $600, permit $250, contractor overhead and profit $2,200: about $19,000. Choosing a prefabricated shower unit instead of tile would have cut roughly $3,000. Financed at an illustrative 10.99% over 60 months, the job is about {pm(19000, 10.99, 60)} a month.</p>"""),
  ("Regional differences and timing", """<p>Tile and plumbing labor drive the regional spread: expensive metros can run 40% above national ranges. Specialty one-day shower companies price nationally and install fast, which is why they dominate the mid-range; their quotes are worth getting even if you end up choosing a tiled shower, because they set a useful floor for the comparison. Vanity and tile lead times are short compared with kitchens, so a bathroom can usually start within weeks of signing. If the remodel is accessibility-driven, ask about local or state grant programs before you finance; several exist for seniors and veterans.</p>"""),
  ("Mistakes that blow the budget", """<ul><li><strong>Moving the toilet</strong> when it doesn't need to move; drain relocation is expensive.</li><li><strong>Underspending on waterproofing</strong> behind the tile, where failures cost thousands later.</li><li><strong>No exhaust fan upgrade</strong>, leading to mould in a freshly tiled room.</li><li><strong>Signing a promotional financing plan without checking whether it's deferred interest</strong> and whether the price is the same for cash.</li><li><strong>Buying fixtures online without checking rough-in dimensions</strong> with the plumber first.</li></ul>"""),
 ],
 "/blog/how-much-does-a-fence-cost/": [
  ("A worked example: the $6,400 backyard fence", f"""<p>A 170-linear-foot backyard, 6-foot pressure-treated wood privacy fence at $28 per foot installed: $4,760. Two walk gates at $350 each: $700. Removal and disposal of the old chain link: $600. Permit: $120. Rocky soil surcharge for post holes: $220. Total about $6,400. The homeowners got a $350 cash discount by paying through their own loan rather than the installer's promotional plan, which carried a fee in the price. Financed at an illustrative 10.99% over 36 months, the fence is about {pm(6050, 10.99, 36)} a month.</p>"""),
  ("Regional differences and timing", """<p>Fence pricing swings with lumber and vinyl prices, local labor and soil. Clay and rock add to post-hole costs; sandy soil in the Southeast is quick to dig but may need deeper posts. Vinyl is relatively more popular in hot, humid states where wood rots faster; cedar is common in the Northwest. Spring is the busy season; late fall and winter quotes are often lower where the ground isn't frozen. Lead times are short, so a fence can usually go in within a couple of weeks of signing.</p>"""),
  ("Mistakes that cost money", """<ul><li><strong>Not confirming the property line.</strong> A survey or pins cost less than moving a fence.</li><li><strong>Ignoring HOA rules</strong> on height, style and colour.</li><li><strong>Choosing the cheapest vinyl</strong>, which can warp or crack; ask for panel thickness and warranty.</li><li><strong>Skipping gate hardware quality</strong>; gates are what fail first.</li><li><strong>Stretching a $6,000 purchase over seven years</strong> when a three-year term adds far less interest.</li></ul>"""),
 ],
 "/blog/does-insurance-cover-foundation-repair/": [
  ("How to file a foundation claim that has a chance", """<ol><li><strong>Stop the cause</strong> if it's a leak, and keep the plumber's invoice and report.</li><li><strong>Document everything</strong>: dated photos of cracks, doors that stick, sloping floors, water intrusion.</li><li><strong>Get an independent structural engineer's report</strong> on cause and scope before the adjuster visits. Insurers lean on "earth movement"; an engineer who attributes the damage to a sudden covered event is your strongest evidence.</li><li><strong>File promptly</strong> and give the adjuster the engineer's report.</li><li><strong>If denied</strong>, ask for the denial in writing citing the policy language, consider a second engineer, and know that your state's insurance department takes complaints. Public adjusters and attorneys sometimes take large claims on contingency.</li></ol>"""),
  ("Regional soils and why Texas, Oklahoma and Colorado see so many claims", """<p>Expansive clay soils swell when wet and shrink when dry, lifting and dropping slabs and footings through each cycle. Much of Texas, Oklahoma, Colorado's Front Range and parts of the Midwest sit on these soils, which is why foundation companies are so common there and why insurers write earth-movement exclusions so carefully. In those regions, drainage and consistent moisture around the foundation prevent more damage than any repair. Coastal and river areas face different problems: high water tables and hydrostatic pressure against basement walls.</p>"""),
  ("Mistakes to avoid", """<ul><li><strong>Taking the foundation company's word on cause.</strong> Get an independent engineer; they don't sell piers.</li><li><strong>Repairing before documenting</strong> if you intend to claim.</li><li><strong>Ignoring drainage</strong> after an expensive repair; gutters, grading and a French drain protect the investment.</li><li><strong>Financing without a warranty review.</strong> Transferable lifetime warranties on piers matter at resale.</li><li><strong>Applying to many lenders at once in a panic</strong>; use soft-pull pre-qualification first.</li></ul>"""),
 ],
 "/blog/whole-house-generator-cost/": [
  ("A worked example: the $13,800 standby generator", f"""<p>A 22 kW air-cooled standby generator for a 2,400-square-foot home with one central AC. Unit and 200-amp automatic transfer switch $6,900, electrical installation $2,400, natural gas line from the meter (40 feet) $1,600, composite pad and placement $600, permits and inspections $450, startup and first service $350, contractor overhead and profit $1,500: about $13,800. The homeowners financed it in March, before hurricane season, at an illustrative 10.99% over 84 months, about {pm(13800, 10.99, 84)} a month, and applied a $500 utility rebate for load management to the first payments.</p>"""),
  ("Natural gas vs propane, and sizing honestly", """<p>Natural gas needs no refuelling but depends on the utility line staying pressurised; propane needs a tank (often 250 to 500 gallons for multi-day outages, a separate cost if you don't have one) but is independent of the grid. On sizing, dealers sometimes upsell: a load calculation that includes a managed-load module for the AC can let a smaller unit cover more than you'd expect. Ask for the calculation in writing. Oversizing adds thousands up front and burns more fuel every test cycle.</p>"""),
  ("Mistakes to avoid", """<ul><li><strong>Quotes that exclude the gas line or transfer switch</strong>, which can double the price after signing.</li><li><strong>Placing the unit too close to windows</strong>; code clearances may force a costly relocation.</li><li><strong>Skipping the service plan</strong>; a generator that hasn't been serviced often fails in the first real outage.</li><li><strong>Buying in the week after a storm</strong> when prices and lead times peak.</li><li><strong>Financing on a promotional plan</strong> without checking for deferred interest and dealer fees in the price.</li></ul>"""),
 ],
 "/blog/water-heater-replacement-cost/": [
  ("A worked example: the Saturday-morning replacement", f"""<p>A 12-year-old 50-gallon gas tank starts leaking from the base on a Saturday. The plumber quotes $2,150 for a like-for-like tank, plus $380 for a required expansion tank and pan, plus a $150 weekend premium: $2,680. The homeowner asks whether Monday would be cheaper and saves the premium; Monday's price is $2,530, financed through the plumber's standard plan at an illustrative 10.99% over 24 months, about {pm(2530, 10.99, 24)} a month. A tankless upgrade was quoted at $4,900 with a $300 utility rebate; the homeowner passed because the venting change would have added another $700.</p>"""),
  ("Signs your water heater is about to fail", """<ul><li><strong>Age past 10 years</strong> on a tank unit (check the serial number for the manufacture date).</li><li><strong>Rust-coloured hot water</strong> or rust at fittings.</li><li><strong>Rumbling or popping</strong>, which is sediment boiling at the bottom of the tank.</li><li><strong>Moisture or small puddles</strong> around the base.</li><li><strong>Hot water running out faster</strong> than it used to.</li></ul><p>Replacing a failing unit on your schedule, rather than after a flooded utility room, saves the emergency premium and lets you compare quotes and financing calmly. It also lets you consider a tankless or heat pump unit properly, with rebates applied, instead of taking whatever the truck has on it that morning.</p>"""),
  ("Mistakes to avoid", """<ul><li><strong>Replacing with the wrong size.</strong> Household size and peak use decide gallons or flow rate.</li><li><strong>Skipping required code items</strong> to save a few hundred dollars; they're required for a reason and an inspector will catch them.</li><li><strong>Buying a tankless unit without checking gas line capacity</strong>.</li><li><strong>Letting the plumber take the old unit without checking the warranty</strong>; some tanks fail inside the warranty period.</li><li><strong>Financing a $2,500 heater over five years</strong> when 24 months adds far less interest.</li></ul>"""),
 ],
 "/blog/siding-replacement-cost/": [
  ("A worked example: the $17,600 vinyl re-side", f"""<p>A two-story colonial with about 2,200 square feet of wall area. Insulated vinyl siding at $6.50 per square foot installed: $14,300. Removal and disposal of the old aluminum siding: $1,400. House wrap and flashing: $700. Sheathing repair on one water-damaged corner: $600. Trim, soffit and fascia touch-ups: $400. Permit: $200. Total about $17,600. The homeowners financed it at an illustrative 10.99% over 84 months, about {pm(17600, 10.99, 84)} a month, after confirming the contractor's price was the same for cash and declining a promotional plan with a dealer fee built in.</p>"""),
  ("Regional differences and storm markets", """<p>Fiber cement is popular in fire-prone and hail-prone regions for its resistance; vinyl dominates where budgets and mild weather favour it; steel is common in the upper Midwest. In hail states, insulated vinyl and fiber cement both perform better than hollow vinyl, and some insurers price that into premiums. Lead times are short for vinyl and longer for fiber cement and custom colours. Spring and fall are the busy seasons; winter quotes can be lower in mild climates.</p>"""),
  ("Mistakes to avoid", """<ul><li><strong>Siding over rotten sheathing</strong> to save on repairs; the problem gets worse and hidden.</li><li><strong>Skipping house wrap and flashing</strong> because the old siding "didn't have it".</li><li><strong>Choosing thin vinyl</strong> that waves and fades; ask for thickness and warranty.</li><li><strong>Ignoring matching rules on an insurance claim</strong> and accepting a two-tone house.</li><li><strong>Signing a promotional plan without checking for deferred interest</strong> and whether the price differs for cash.</li></ul>"""),
 ],
}
_METAS = {
 "/blog/how-much-does-a-kitchen-remodel-cost/": "Kitchen remodel costs by scope, from a refresh to a full gut, where the money goes, how to trim it, and what each budget means per month.",
 "/blog/how-much-does-a-bathroom-remodel-cost/": "Bathroom remodel costs for small, mid-range and master baths, tub-to-shower conversions, where the money goes, and monthly payments.",
 "/blog/how-much-does-a-fence-cost/": "Fence cost per foot for wood, vinyl, chain link, aluminum and composite, typical yard totals, what adds to the price, and how to pay monthly.",
 "/blog/does-insurance-cover-foundation-repair/": "When homeowners insurance covers foundation repair and when it doesn't, typical repair costs for cracks, piers and waterproofing, and how to pay.",
 "/blog/whole-house-generator-cost/": "Whole house standby generator cost installed by size, plus transfer switch, gas line, permits and running costs, and what it means per month.",
 "/blog/water-heater-replacement-cost/": "Water heater replacement costs for tank, tankless and heat pump units, what drives the price, repair vs replace, and financing an emergency swap.",
 "/blog/siding-replacement-cost/": "Siding replacement cost per square foot by material, whole-house totals, what adds to the price, storm claims and matching, and monthly payments.",
}
for _a in ARTICLES_C:
    _a["meta"] = _METAS[_a["path"]]
    _secs = list(_a["sections"]); _i = next(i for i, s in enumerate(_secs) if s[0] == "Questions to ask every lender")
    _a["sections"] = _secs[:_i] + _MORE[_a["path"]] + _secs[_i:]


# ------------------------------------------------------------------ depth pass 2: contractor questions + upgrade-as-monthly, plus FAQs
def _upgrade(label, low, high, apr=10.99, n=84):
    d = money(payment(high, apr, n) - payment(low, apr, n), False)
    return f"""<p>Financing changes how upgrades feel. The difference between a {money(low, False)} {label} and a {money(high, False)} one is {money(high - low, False)} as a lump sum, but about {d} a month over {n} months at an illustrative {apr}% APR. That is why the better option often gets chosen once the monthly figure is on the table. Just make sure the upgrade pays you back in comfort, durability or running cost, and not only in looks, because you'll be paying for it long after the novelty fades.</p>"""

_MORE2 = {
 "/blog/how-much-does-a-kitchen-remodel-cost/": [
  ("Questions to ask the remodeler", """<ol><li>Is the quote itemized by line, with allowances for cabinets, counters and appliances stated?</li><li>What is the change-order process and pricing?</li><li>Who pulls permits and schedules inspections?</li><li>What is the lead time on the cabinets I've chosen, and when is the deposit due?</li><li>Is there a written schedule with milestones, and what happens if it slips?</li><li>Are your subcontractors licensed and insured, and will you provide certificates?</li><li>What warranty covers workmanship, and for how long?</li><li>If I finance through your plan, is the price the same as for cash?</li></ol>"""),
  ("Upgrade or standard? Think in monthly terms", _upgrade("kitchen", 35000, 45000)),
 ],
 "/blog/how-much-does-a-bathroom-remodel-cost/": [
  ("Questions to ask the remodeler", """<ol><li>What waterproofing system goes behind the tile, and is it warrantied?</li><li>Is the shower pan prefabricated or site-built, and by whom?</li><li>Will the exhaust fan be upgraded and vented outside?</li><li>Are plumbing and electrical updates to current code included?</li><li>What is the schedule, and will we have a working toilet during the job?</li><li>Who handles permits and inspections?</li><li>What is the workmanship warranty?</li><li>If I use your financing plan, is the price the same as for cash?</li></ol>"""),
  ("Upgrade or standard? Think in monthly terms", _upgrade("bathroom", 16000, 22000, n=60)),
 ],
 "/blog/how-much-does-a-fence-cost/": [
  ("Questions to ask the fence installer", """<ol><li>What post depth and concrete footing do you use, and how does it handle frost or clay?</li><li>What is the panel thickness and warranty on vinyl, or the grade and treatment on wood?</li><li>Are gates and hardware itemized, and what grade are the hinges and latches?</li><li>Do you locate utilities before digging, and who handles the permit?</li><li>Is old-fence removal and disposal included?</li><li>What is the workmanship warranty?</li><li>Is the price the same for cash as for your financing plan?</li></ol>"""),
  ("Upgrade or standard? Think in monthly terms", _upgrade("fence", 5500, 8000, n=36)),
 ],
 "/blog/does-insurance-cover-foundation-repair/": [
  ("Questions to ask the foundation contractor", """<ol><li>Will you work from an independent structural engineer's report, or only your own inspection?</li><li>What repair method do you recommend and why, and what are the alternatives?</li><li>How many piers, to what depth, and what is the price per pier if more are needed?</li><li>Is the warranty transferable, and what exactly does it cover?</li><li>What happens to flooring, plumbing and finishes during the lift, and who repairs them?</li><li>Are permits and an engineer's final inspection included?</li><li>Is the price the same for cash as for your financing plan?</li></ol>"""),
  ("Repair now or wait? Think in monthly terms", """<p>Foundation problems rarely get cheaper. A crack that costs $1,500 to inject this year can become a $15,000 pier job after two more wet-dry cycles. Financing a modest repair early is often the cheaper path: $8,000 at an illustrative 10.99% over 60 months is about """ + pm(8000, 10.99, 60) + """ a month, against a much larger job later. The exception is cosmetic cracking that an engineer confirms is stable, which can be monitored rather than repaired.</p>"""),
 ],
 "/blog/whole-house-generator-cost/": [
  ("Questions to ask the generator dealer", """<ol><li>What load calculation sizes this unit, and can I see it?</li><li>Does the quote include the transfer switch, gas line, pad, permits and startup?</li><li>What is the clearance plan for placement, and will it pass code?</li><li>What does the service plan cost, and how often does the unit self-test?</li><li>What is the warranty on the unit and on your installation?</li><li>Can I monitor the generator from my phone, and is there a subscription?</li><li>Is the price the same for cash as for your financing plan?</li></ol>"""),
  ("Essentials or whole house? Think in monthly terms", _upgrade("generator", 9500, 14000)),
 ],
 "/blog/water-heater-replacement-cost/": [
  ("Questions to ask the plumber", """<ol><li>What size or flow rate do you recommend for my household, and why?</li><li>Which code items are required (expansion tank, pan, strapping, valves) and are they in the price?</li><li>Does the venting or gas line need changes for the unit you're quoting?</li><li>Is removal and disposal of the old unit included?</li><li>What is the manufacturer warranty, and who registers it?</li><li>If I wait until a weekday, does the price change?</li><li>Is the price the same for cash as for your financing plan?</li></ol>"""),
  ("Tank or tankless? Think in monthly terms", _upgrade("water heater", 2500, 4800, n=36)),
 ],
 "/blog/siding-replacement-cost/": [
  ("Questions to ask the siding contractor", """<ol><li>Is removal of the old siding, house wrap, flashing and trim included?</li><li>How do you price sheathing repairs found during removal?</li><li>What thickness and warranty does the vinyl carry, or what brand and finish of fiber cement?</li><li>Are you certified by the manufacturer, and does that extend the warranty?</li><li>Who handles permits, and will soffit and fascia be replaced or wrapped?</li><li>What is the workmanship warranty?</li><li>Is the price the same for cash as for your financing plan?</li></ol>"""),
  ("Vinyl or fiber cement? Think in monthly terms", _upgrade("siding job", 16000, 28000, n=120)),
 ],
}
_FAQ2 = {
 "/blog/how-much-does-a-kitchen-remodel-cost/": [("How much should I keep aside for surprises?", "Ten to fifteen percent of the contract. Water damage behind cabinets, outdated wiring and uneven subfloors are the common ones."), ("Should I finance a kitchen with a HELOC?", "For a large remodel with enough equity and time, a HELOC or home equity loan usually has the lowest rate. Lock a fixed rate on the drawn amount if the lender offers it, and plan for the end of the draw period.")],
 "/blog/how-much-does-a-bathroom-remodel-cost/": [("Is a one-day shower conversion worth it?", "For a tub-to-shower swap with fixtures in place, often yes: fast, predictable and mid-range in price. Compare the total against a tiled shower quote and check the financing plan's terms."), ("Do I need a permit for a bathroom remodel?", "Usually yes when plumbing or electrical work is involved. Your contractor should pull it; ask whether it's in the price.")],
 "/blog/how-much-does-a-fence-cost/": [("How long does a fence last?", "Chain link 20 years or more, treated wood 15 to 20 with upkeep, vinyl 20 to 30, aluminum and composite 30 or more. Match the loan term to a fraction of the fence's life."), ("Can my neighbour share the cost of a fence?", "Often, by agreement. Put it in writing, including who maintains it, and confirm the property line first.")],
 "/blog/does-insurance-cover-foundation-repair/": [("Should I get a second foundation opinion?", "Yes. Foundation companies sell repairs; an independent structural engineer's report, usually a few hundred dollars, tells you the cause and the minimum fix."), ("Can I sell a house with foundation problems?", "Yes, with disclosure, usually at a discount. A completed repair with a transferable warranty is worth far more at sale than an unrepaired problem.")],
 "/blog/whole-house-generator-cost/": [("How long does a standby generator last?", "Commonly 15 to 25 years with annual service, though heavy use in long outages shortens it. Engine hours, not age, are the better measure."), ("Natural gas or propane generator?", "Natural gas if you have a line with enough capacity: no refuelling. Propane if you don't, with tank size matched to the outage length you're planning for.")],
 "/blog/water-heater-replacement-cost/": [("How long does a water heater last?", "Tank units commonly 8 to 12 years, tankless 20 or more with annual descaling, heat pump units 10 to 15. Hard water shortens all of them."), ("Should I replace a water heater before it fails?", "If it's past 10 years and showing rust or sediment noise, planning the replacement avoids an emergency premium and a flooded room, and gives you time to compare quotes and financing.")],
 "/blog/siding-replacement-cost/": [("How long does siding last?", "Vinyl 20 to 40 years, engineered wood 30 or more, fiber cement around 50, steel 40 or more. Wood depends on upkeep."), ("Can I put new siding over old siding?", "Sometimes over flat, sound wood or vinyl, but not over damaged sheathing or wavy surfaces, and never without new house wrap and flashing. Most contractors recommend removal.")],
}
for _a in ARTICLES_C:
    _secs = list(_a["sections"]); _i = next(i for i, s in enumerate(_secs) if s[0] == "Questions to ask every lender")
    _a["sections"] = _secs[:_i] + _MORE2[_a["path"]] + _secs[_i:]
    _a["faqs"] = list(_a["faqs"]) + _FAQ2[_a["path"]]


# ------------------------------------------------------------------ depth pass 3: a 'what lenders look at' section, shared wording tailored per project
def _lenders(project, amount):
    return ("What lenders look at when you finance a " + project, f"""<p>Unsecured home improvement loans are approved on the same five things whatever the project: your credit score and recent payment history, your income and how much of it already goes to debt, the amount you're asking for, how long you've had credit, and whether the application is complete. Lenders that fund {project}s usually see requests in the {money(amount[0], False)} to {money(amount[1], False)} range, and a request near the low end of that is approved more often and at a better rate than one near the top.</p>
<p>Four moves improve offers everywhere: reduce the amount (rebates, a smaller scope, a down payment), pay a card balance below about 30% of its limit before the next statement, have pay stubs or bank statements ready so the application is complete, and check options with a soft-pull pre-qualification before any hard application. If your score is on the lower side, a co-applicant with stronger credit can open better terms; they share full responsibility for the loan. Home equity products add two more checks: an appraisal or valuation and a cushion of equity the lender wants left after the loan, commonly 15% to 20% of the home's value.</p>""")

_LEND = {
 "/blog/how-much-does-a-bathroom-remodel-cost/": ("bathroom remodel", (8000, 40000)),
 "/blog/how-much-does-a-fence-cost/": ("fence", (3000, 15000)),
 "/blog/does-insurance-cover-foundation-repair/": ("foundation repair", (5000, 40000)),
 "/blog/whole-house-generator-cost/": ("standby generator", (7000, 25000)),
 "/blog/water-heater-replacement-cost/": ("water heater", (1200, 6000)),
 "/blog/siding-replacement-cost/": ("siding job", (8000, 40000)),
}
for _a in ARTICLES_C:
    if _a["path"] in _LEND:
        _secs = list(_a["sections"]); _i = next(i for i, s in enumerate(_secs) if s[0] == "Questions to ask every lender")
        _a["sections"] = _secs[:_i] + [_lenders(*_LEND[_a["path"]])] + _secs[_i:]
