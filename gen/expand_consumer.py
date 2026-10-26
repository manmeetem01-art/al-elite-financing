"""Length + query-match pass for thin consumer service pages (GSC Oct 2026: fence, foundation, generator,
water heater, kitchen, bathroom, deck, garage door, window pages at position 60-90 on KD0 terms)."""
from common import money, payment

def pm(P, apr, n):
    return money(payment(P, apr, n), False)

def ti(P, apr, n):
    return money(payment(P, apr, n) * n - P, False)

def pay_para(label, amounts, apr=10.99, terms=(36, 60, 84)):
    rows = "".join(f"<tr><td><strong>{money(P, False)}</strong></td>" + "".join(f"<td class='num'>{pm(P, apr, t)}</td>" for t in terms) + f"<td class='num'>{ti(P, apr, 60)}</td></tr>" for P in amounts)
    head = "".join(f"<th class='num'>{t} mo</th>" for t in terms)
    return f"<p>Illustrative payments for typical {label} amounts at {apr}% APR, standard amortization, no fees. Lenders set real rates after reviewing your application.</p><div class='tbl'><table><thead><tr><th>Amount</th>{head}<th class='num'>Interest (60 mo)</th></tr></thead><tbody>{rows}</tbody></table></div>"

QUALIFY = ("What lenders look at", """<p>Unsecured home improvement loans are approved on five things: your credit score and recent payment history, your income and how much of it already goes to debt, the amount requested, how long you've had credit, and a complete application. You can't change history overnight, but you can reduce the amount (rebates, a smaller scope, a down payment), pay a card balance down before applying, have pay stubs or bank statements ready, and check options with a soft pull before any hard inquiry. Those four steps improve offers at every lender.</p>""")

def vet(trade):
    return ("Check the contractor before the loan", f"""<p>Get two or three itemized quotes on the same scope from licensed, insured {trade}. Confirm permits are included, read the financing documents separately from the work contract (the loan is with the lender, not the contractor), and never sign a blank or partly blank application. The Federal Trade Commission's guide to hiring a contractor, linked in the sources below, lists the warning signs.</p>""")

X = {}

X["/fence-financing/"] = dict(
    title="Fence Financing | Finance a Fence with Monthly Payments | AL Elite",
    sections=[
        ("How to finance a fence", """<p>Most fences are financed with an unsecured personal loan or a contractor's plan over two to seven years. Fence companies that offer financing usually work with a lender partner; you apply at the quote and the lender pays the installer on completion. If your installer doesn't offer a plan, a loan you arrange yourself pays them like cash. For a large perimeter fence on a rural lot, a home equity product can be cheaper per dollar if you have equity and time.</p>""" + pay_para("fence", (3500, 6000, 10000, 15000))),
        QUALIFY,
        vet("fence installers"),
    ],
    faqs=[("Can you finance a fence?", "Yes. Fence installers often offer financing through lender partners, and unsecured personal loans cover fences from a few thousand dollars up. Terms commonly run two to seven years."), ("Is fence financing available with bad credit?", "Some lenders consider lower scores at higher APRs, often for smaller amounts. Reducing the amount and adding a co-applicant help.")],
)

X["/foundation-repair-financing/"] = dict(
    sections=[
        ("Financing for foundation repair: why it's different", """<p>Foundation work is rarely optional and rarely cheap, and most homeowners insurance excludes settlement and soil movement. That makes financing the whole job, rather than a gap, the common situation. Unsecured loans suit repairs up to the lender's cap and fund in days; home equity products suit larger pier or slab jobs if the home has equity (an appraiser will note the foundation, so get the engineer's report first). Many foundation companies offer financing through lender partners, and some government-backed programs (FHA Title I, USDA 504 in rural areas) cover structural repairs for eligible homeowners.</p>""" + pay_para("foundation repair", (5000, 12000, 25000, 40000))),
        QUALIFY,
        vet("foundation contractors (ask for an independent structural engineer's report first)"),
    ],
    faqs=[("Does insurance cover foundation repair?", "Usually not for settlement, soil movement or drainage problems. Sudden events such as a burst pipe or a covered peril may be covered. Check your policy and get the cause documented by an engineer."), ("Can I finance foundation repair with bad credit?", "Options exist at higher APRs, and government-backed programs may help eligible homeowners. A smaller scope, a co-applicant and a soft-pull pre-qualification improve your chances.")],
)

X["/generator-financing/"] = dict(
    title="Generator Financing | Whole House Standby Generator Loans | AL Elite",
    sections=[
        ("Whole house generator financing: what you're paying for", """<p>A whole-home standby generator is three purchases in one: the unit (sized to the loads you want covered), the automatic transfer switch and electrical work, and the gas or propane connection, pad and permits. Installed prices for a home standby system commonly run well into five figures, which is why most are financed. Lenders treat it as a home improvement loan: unsecured over three to ten years, or through the installer's plan, with the lender paying the installer on completion. Portable and inverter generators are small enough that a card or short loan usually makes more sense.</p>""" + pay_para("home generator", (6000, 10000, 15000, 20000))),
        ("Generator financing in storm-prone states", """<p>Demand spikes after hurricanes, ice storms and grid failures, and so do install lead times. Financing before a storm season, when installers have capacity, is usually cheaper and faster than after. Some utilities and states offer rebates or low-interest programs for backup power, and a standby generator can matter for insurance of sump pumps and freezers in some areas. Our <a href="/locations/">location guides</a> cover the storm markets where backup power is most common.</p>"""),
        QUALIFY,
    ],
    faqs=[("How do you finance a whole house generator?", "Through an unsecured personal loan, the installer's financing plan, or a home equity product for larger systems. The lender pays the installer when the system is commissioned."), ("Can I finance a Generac or other brand generator?", "Yes. Financing is for the installed system regardless of brand; some manufacturers and dealers also run their own promotional programs through bank partners.")],
)

X["/water-heater-financing/"] = dict(
    title="Water Heater Financing | Hot Water Heater Replacement Loans | AL Elite",
    sections=[
        ("How to finance a hot water heater replacement", """<p>Water heaters fail without warning, so most replacements are financed the same day through the plumber's plan or a fast unsecured loan. Tank units are the cheaper, quicker swap; tankless and heat-pump water heaters cost more up front and may qualify for utility rebates that reduce the amount financed. Because amounts are modest, short terms make sense: paying a few hundred dollars less in interest matters more than a slightly lower monthly figure.</p>""" + pay_para("water heater", (1500, 2500, 4000, 6500), terms=(12, 24, 36))),
        QUALIFY,
        vet("plumbers"),
    ],
    faqs=[("Can you finance a water heater?", "Yes. Plumbers and HVAC companies commonly offer financing through lender partners, and unsecured personal loans cover replacements from about $1,000 up. Short terms keep total interest low."), ("Is financing available for a tankless water heater?", "Yes. Tankless units cost more up front, and some utilities offer rebates that reduce what you finance.")],
)

X["/remodel-financing/kitchen/"] = dict(
    title="Kitchen Remodel Financing | Kitchen Renovation Loans & Options | AL Elite",
    sections=[
        ("How to finance a kitchen renovation", """<p>Kitchens are the largest planned home project most people take on, so the full menu of options applies. Unsecured personal loans cover refreshes and mid-range remodels and fund quickly. Home equity loans and HELOCs usually offer lower rates for full gut renovations if you have equity and a few weeks. FHA 203(k) folds a remodel into a refinance. Contractor plans put a monthly figure next to the quote. Many homeowners combine two: a HELOC for the bulk and savings or a short loan for the appliances.</p>""" + pay_para("kitchen remodel", (15000, 30000, 50000, 75000), terms=(60, 84, 120))),
        ("Kitchen remodel loan or home equity?", """<p>Two tests. Timing: if you're starting next month, an unsecured kitchen remodel loan funds in days; equity products take weeks. Size: above roughly $30,000 the lower rate on a home equity product usually outweighs its closing costs, below that the gap shrinks. Our guide to <a href="/blog/heloc-vs-roof-loan/">home equity loans vs HELOCs vs unsecured loans</a> is written for roofs but the trade-offs are identical.</p>"""),
        QUALIFY,
    ],
    faqs=[("What is the best way to finance a kitchen remodel?", "For a planned, large remodel with equity, a home equity loan or HELOC is usually cheapest. For a faster start or less equity, an unsecured kitchen remodel loan or a contractor plan. Compare APR including fees and total cost."), ("Can I get a kitchen remodel loan with fair credit?", "Yes, though at higher APRs and sometimes lower amounts. A co-applicant, a smaller scope or a home equity option can improve terms.")],
)

X["/remodel-financing/bathroom/"] = dict(
    sections=[
        ("Bathroom remodel loans: matching the loan to the job", """<p>A tub-to-shower conversion or an accessibility remodel is a mid-four-figure to low-five-figure job that fits an unsecured bathroom remodel loan over three to seven years. A full master bath with moved plumbing can run much higher and may justify a home equity product. Contractor plans are common in this trade, especially for one-day shower conversions; ask whether a promotional rate carries a dealer fee in the price.</p>""" + pay_para("bathroom remodel", (8000, 15000, 25000, 40000))),
        QUALIFY,
        vet("bathroom remodelers"),
    ],
    faqs=[("Can you finance a bathroom remodel?", "Yes. Unsecured loans, contractor plans and home equity products all cover bathroom remodels. Smaller jobs suit short unsecured terms; large remodels may be cheaper through home equity.")],
)

X["/deck-financing/"] = dict(
    sections=[
        ("How deck financing works", """<p>Deck builders often offer financing through lender partners, and unsecured loans cover most decks and patio covers. Composite decks cost more up front but need less maintenance, so a slightly longer term can make sense; a pressure-treated deck with a 10- to 15-year life should carry a shorter loan. For screened porches and covered outdoor rooms, which can approach remodel pricing, compare an unsecured loan with a home equity product.</p>""" + pay_para("deck", (6000, 12000, 20000, 30000))),
        QUALIFY,
        vet("deck builders"),
    ],
    faqs=[("Can I finance a composite deck?", "Yes. Composite decks are financed like any home improvement; the higher up-front cost is often offset by lower maintenance over the deck's life.")],
)

X["/garage-door-financing/"] = dict(
    sections=[
        ("Garage door replacement loans: small amounts, short terms", """<p>A single garage door with opener is a modest purchase; a double insulated door with a smart opener and new tracks is a larger one. Either way the amounts suit short unsecured terms or a dealer plan. Many garage door companies offer same-week install with financing; check the APR after any promotional period and whether the price changes for cash. Impact-rated doors in hurricane zones may qualify for insurance discounts that partly offset the cost.</p>""" + pay_para("garage door", (1800, 3500, 6000, 9000), terms=(12, 24, 36))),
        QUALIFY,
    ],
    faqs=[("Can you finance a garage door?", "Yes. Garage door dealers commonly offer financing, and unsecured personal loans cover door and opener replacements. Short terms keep interest low on these smaller amounts.")],
)

X["/window-financing/"] = dict(
    sections=[
        ("Window replacement financing: whole house or a few at a time", """<p>Whole-house window replacement is a five-figure project that is usually financed; replacing the worst four or five windows first is a common way to keep the amount manageable. Window companies are among the heaviest users of promotional financing, so read whether the 0% offer is deferred or waived interest and whether a dealer fee sits in the price. Energy-efficient windows may qualify for utility rebates, which reduce what you finance.</p>""" + pay_para("window replacement", (8000, 15000, 25000, 40000), terms=(60, 84, 120))),
        QUALIFY,
        vet("window installers"),
    ],
    faqs=[("How do you finance window replacement?", "Through the window company's plan, an unsecured personal loan, or a home equity product for whole-house projects. Compare the APR after any promotional period and the cash price.")],
)


def apply(pages_by_path):
    for path, x in X.items():
        p = pages_by_path.get(path)
        if not p:
            continue
        for k in ("title", "h1", "meta"):
            if k in x:
                p[k] = x[k]
        p["sections"] = list(p.get("sections", [])) + x.get("sections", [])
        p["faqs"] = list(p.get("faqs", [])) + x.get("faqs", [])
