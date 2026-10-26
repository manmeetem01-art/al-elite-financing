"""On-page pass for generic (non-local) money pages, from Ahrefs US volumes (Oct 2026).
Sets the primary keyword per page, fixes titles where the easier/bigger term wasn't primary, makes sure the
primary appears in H1, meta and the answer paragraph, adds a variant H2 where a big variant exists,
and adds contextual sibling links in the body."""
from common import esc

# path -> (primary, volume, [variants with volume worth an H2])
PRIMARY = {
    "/roof-financing/": ("roof financing", 3600, ["new roof financing", "roof replacement financing", "roof loans"]),
    "/roof-financing/bad-credit-roof-financing/": ("roof financing with bad credit", 80, []),
    "/roof-financing/metal-roof-financing/": ("metal roof financing", 150, []),
    "/roof-financing/roof-repair-financing/": ("roof repair financing", 200, []),
    "/roof-financing/commercial-roof-financing/": ("commercial roof financing", 150, []),
    "/hvac-financing/": ("HVAC financing", 3700, ["AC financing", "furnace financing", "heat pump financing"]),
    "/hvac-financing/bad-credit-hvac-financing/": ("HVAC financing with bad credit", 1200, ["AC financing bad credit"]),
    "/plumbing-financing/": ("plumbing financing", 900, []),
    "/water-heater-financing/": ("water heater financing", 350, []),
    "/solar-financing/": ("solar financing", 2700, ["solar panel financing", "solar loans"]),
    "/siding-financing/": ("siding financing", 200, []),
    "/gutter-financing/": ("gutter financing", 200, []),
    "/window-financing/": ("window financing", 700, ["window replacement financing"]),
    "/foundation-repair-financing/": ("foundation repair financing", 600, []),
    "/flooring-financing/": ("flooring financing", 1000, []),
    "/pool-financing/": ("pool financing", 1600, ["pool loans"]),
    "/remodel-financing/kitchen/": ("kitchen remodel financing", 700, ["kitchen remodel loan"]),
    "/remodel-financing/bathroom/": ("bathroom remodel financing", 700, []),
    "/fence-financing/": ("fence financing", 500, []),
    "/deck-financing/": ("deck financing", 350, []),
    "/generator-financing/": ("generator financing", 250, []),
    "/garage-door-financing/": ("garage door financing", 150, []),
    "/landscaping-financing/": ("landscaping financing", 150, []),
    "/home-improvement-financing/": ("home improvement financing", 1500, ["home improvement loans"]),
    "/for-contractors/": ("contractor financing", 700, ["customer financing for contractors"]),
    "/for-contractors/roofing/": ("financing for roofing companies", 150, []),
    "/for-contractors/hvac/": ("HVAC financing for contractors", 150, []),
    "/contractor-business-loans/": ("construction business loans", 600, ["contractor business loans"]),
    "/contractor-business-loans/working-capital/": ("working capital for contractors", 70, []),
    "/contractor-business-loans/equipment-financing/": ("construction equipment financing", 1100, []),
    "/contractor-business-loans/dump-truck-financing/": ("dump truck financing", 600, []),
    "/contractor-business-loans/invoice-factoring/": ("construction invoice factoring", 300, []),
    "/contractor-business-loans/line-of-credit/": ("construction line of credit", 300, []),
    "/contractor-business-loans/hvac/": ("HVAC business loans", 300, []),
    "/contractor-business-loans/plumbing/": ("plumbing business loans", 150, []),
    "/contractor-business-loans/landscaping/": ("landscaping business loans", 150, []),
    "/tools/roof-financing-calculator/": ("roof financing calculator", 100, []),
    "/tools/equipment-loan-calculator/": ("equipment loan calculator", 1500, ["equipment financing calculator"]),
}

METAS = {
    "/hvac-financing/bad-credit-hvac-financing/": "HVAC financing with bad credit: AC, furnace and heat pump loans for lower scores, lenders that look beyond the score, and the offers to avoid.",
    "/solar-financing/": "Solar financing explained: solar loans vs leases vs PPAs, what each costs over 20 years, PACE risks, and how to compare offers before you sign.",
    "/window-financing/": "Window financing for whole-house or partial window replacement: unsecured loans, dealer plans and home equity compared, with example payments.",
    "/tools/roof-financing-calculator/": "Roof financing calculator: enter your quote, APR and term to see the monthly payment, total interest and amortization schedule for a new roof.",
    "/tools/equipment-loan-calculator/": "Equipment loan calculator: monthly payments, total interest and amortization for excavators, skid steers, trucks and other construction equipment.",
}
ANSWERS = {
    "/window-financing/": "Window financing lets you replace all or some of your windows and pay monthly, through an unsecured loan, the window company's plan or a home equity product. ",
    "/tools/roof-financing-calculator/": "This roof financing calculator turns a roofing quote, an APR and a term into a monthly payment and total interest. ",
    "/tools/equipment-loan-calculator/": "This equipment loan calculator turns an equipment price, down payment, APR and term into a monthly payment and total interest. ",
}
TITLES = {
    "/solar-financing/": ("Solar Financing | Solar Panel Loans, Leases & PPAs Compared", "Solar financing: solar panel loans, leases and PPAs, and which one actually pays"),
    "/window-financing/": ("Window Financing | Window Replacement Loans & Payment Options", "Window financing: whole-house and partial window replacement, paid monthly"),
    "/tools/equipment-loan-calculator/": ("Equipment Loan Calculator | Equipment Financing Payment Calculator", "Equipment loan calculator: monthly payments on excavators, trucks and tools"),
    "/home-improvement-financing/": ("Home Improvement Loans & Financing by Project Type | AL Elite", "Home improvement financing and loans: every project, matched to the right lender"),
    "/roof-financing/": ("Roof Financing | New Roof & Roof Replacement Financing Options", "Roof financing: new roof and roof replacement financing, paid monthly instead of all at once"),
    "/hvac-financing/": ("HVAC Financing | AC, Furnace & Heat Pump Financing Options", "HVAC financing: AC, furnace and heat pump replacement, paid monthly"),
    "/pool-financing/": ("Pool Financing | Pool Loans for In-Ground & Above-Ground Pools", "Pool financing: pool loans for in-ground and above-ground pools, and the term that fits"),
    "/contractor-business-loans/": ("Construction Business Loans | Contractor Business Loans & Capital", "Construction business loans: capital for contractors between the job and the payment"),
}

VARIANT_SECTIONS = {
    "/roof-financing/": ("New roof financing vs roof replacement financing: is there a difference?", """<p>Lenders don't distinguish between "new roof financing" and "roof replacement financing"; both are loans for a roofing job, and the same products apply. The difference is in your situation. A replacement after storm damage usually involves an insurance claim, so you finance the gap (deductible, held-back depreciation, uncovered items) rather than the whole roof. A new roof on an older home without a claim means financing the full price, which is where comparing an unsecured roof loan against a home equity product matters most. Either way, the amount, the APR and the term decide the payment, and our <a href="/tools/roof-financing-calculator/">roof financing calculator</a> shows all three.</p>"""),
    "/hvac-financing/": ("AC financing, furnace financing and heat pump financing", """<p>Most HVAC financing requests are for one of three jobs. <strong>AC financing</strong> is the summer emergency: a failed condenser or compressor replaced within days, often through the contractor's plan. <strong>Furnace financing</strong> is the winter equivalent, and in the Midwest and Northeast the furnace is often older than the AC. <strong>Heat pump financing</strong> covers systems that heat and cool with one outdoor unit, increasingly chosen in mild and even cold climates because of efficiency and utility rebates. The loan products are the same; what changes is the amount (a furnace alone is cheaper than a full split system), the rebates available, and how urgent the timeline is. Our guide to <a href="/blog/furnace-and-ac-replacement-financing/">furnace and AC replacement financing</a> compares the three with example payments.</p>"""),
    "/solar-financing/": ("Solar panel financing: loan, lease or PPA?", """<p>"Solar panel financing" and "solar loans" usually mean the same thing: a loan that lets you own the system and claim any incentives yourself. Leases and power purchase agreements (PPAs) are the alternative, where a third party owns the panels and you pay for the equipment or the power each month with little or nothing down. Ownership through a loan generally produces the best long-term value if you'll stay in the home; leases and PPAs trade that value for zero upfront cost and no maintenance. PACE financing, repaid through property taxes, is a third option in some states and is now subject to federal consumer-protection rules; compare it carefully.</p>"""),
    "/window-financing/": ("Window replacement financing: whole house or a few windows at a time", """<p>Whole-house window replacement is a five-figure project and is almost always financed; replacing the worst four or five windows first is a common way to keep the amount manageable and the loan short. Window companies lean heavily on promotional plans, so check whether a "0% for 18 months" offer is deferred interest and whether the price is the same for cash. Energy-efficient windows may qualify for utility rebates, which reduce what you finance.</p>"""),
    "/pool-financing/": ("Pool loans: what lenders offer and how long the terms run", """<p>"Pool loans" are usually unsecured personal loans sized for pool construction, often with longer terms than a typical home improvement loan because the amounts are larger. Some lenders specialize in pool financing and work directly with builders, paying in stages as the dig, shell and finish are completed. Home equity products are the main alternative for large in-ground projects if you have equity and time. Match the term to the pool's life and your plans: a 15-year loan on a pool you'll enjoy for 30 is reasonable; a 15-year loan on an above-ground pool is not.</p>"""),
    "/home-improvement-financing/": ("Home improvement loans: the main types in plain English", """<p>"Home improvement loans" covers several products. <strong>Unsecured personal loans</strong> are the most common: fixed rate, no lien, funded in days, sized from a few thousand dollars up to the lender's cap. <strong>Home equity loans</strong> and <strong>HELOCs</strong> borrow against the house at lower rates, with closing costs and weeks to close. <strong>Contractor financing</strong> is a lender's loan presented at the quote, sometimes promotional. <strong>Government-backed programs</strong> such as FHA Title I, FHA 203(k) and USDA Section 504 cover eligible repairs and remodels through participating lenders. Each project page on this site explains which of these fit that kind of job and shows example payments.</p>"""),
    "/for-contractors/": ("Customer financing for contractors: what it costs and what it returns", """<p>Customer financing for contractors is a program where a lender partner funds the homeowner's project and pays you on completion. Standard-rate plans usually cost you nothing; promotional plans carry a dealer fee of several percent of the job. In return, contractors typically see higher close rates and larger average tickets, because the homeowner is deciding on a monthly figure rather than a lump sum. Our <a href="/blog/why-contractors-lose-jobs-without-financing/">guide to why contractors lose jobs without financing</a> puts numbers on it.</p>"""),
    "/contractor-business-loans/": ("Contractor business loans vs construction business loans: same thing, different lenders", """<p>Lenders use "contractor business loans" and "construction business loans" interchangeably for working capital, equipment, truck and line-of-credit products aimed at trades businesses. The useful distinction is the lender's experience with construction cash flow: lenders who understand progress billing, retainage and seasonal revenue approve more contractors and structure terms that fit. That's the filter we apply when matching.</p>"""),
    "/tools/equipment-loan-calculator/": ("Equipment financing calculator: loan or lease?", """<p>This equipment financing calculator models a standard loan. For a lease, enter the monthly lease payment and compare the total of payments (plus any buyout) against the loan's total of payments minus the equipment's resale value at the end. Our guide to <a href="/blog/equipment-financing-vs-leasing/">equipment financing vs leasing</a> walks through that comparison with a worked example.</p>"""),
    "/remodel-financing/kitchen/": ("Kitchen remodel loan vs home equity: which is cheaper for your kitchen?", """<p>A kitchen remodel loan (unsecured) funds in days and suits refreshes and mid-range remodels; a home equity loan or HELOC usually costs less per dollar for a full gut if you have equity and a few weeks. Above roughly $30,000 the rate advantage of home equity tends to outweigh its closing costs; below that the gap narrows. Our guide to <a href="/blog/how-much-does-a-kitchen-remodel-cost/">how much a kitchen remodel costs</a> shows what each budget looks like per month.</p>"""),
}

# sibling links: path -> [(anchor, url)]
SIBLINGS = {
    "/roof-financing/": [("roof financing with bad credit", "/roof-financing/bad-credit-roof-financing/"), ("metal roof financing", "/roof-financing/metal-roof-financing/"), ("roof repair financing", "/roof-financing/roof-repair-financing/"), ("gutter financing", "/gutter-financing/"), ("siding financing", "/siding-financing/")],
    "/hvac-financing/": [("HVAC financing with bad credit", "/hvac-financing/bad-credit-hvac-financing/"), ("water heater financing", "/water-heater-financing/"), ("generator financing", "/generator-financing/"), ("plumbing financing", "/plumbing-financing/")],
    "/plumbing-financing/": [("water heater financing", "/water-heater-financing/"), ("bathroom remodel financing", "/remodel-financing/bathroom/"), ("foundation repair financing", "/foundation-repair-financing/")],
    "/water-heater-financing/": [("plumbing financing", "/plumbing-financing/"), ("HVAC financing", "/hvac-financing/")],
    "/solar-financing/": [("roof financing", "/roof-financing/"), ("generator financing", "/generator-financing/"), ("home improvement financing", "/home-improvement-financing/")],
    "/siding-financing/": [("window financing", "/window-financing/"), ("gutter financing", "/gutter-financing/"), ("roof financing", "/roof-financing/")],
    "/gutter-financing/": [("roof financing", "/roof-financing/"), ("siding financing", "/siding-financing/"), ("landscaping financing", "/landscaping-financing/")],
    "/window-financing/": [("siding financing", "/siding-financing/"), ("garage door financing", "/garage-door-financing/"), ("home improvement financing", "/home-improvement-financing/")],
    "/foundation-repair-financing/": [("plumbing financing", "/plumbing-financing/"), ("landscaping financing", "/landscaping-financing/"), ("roof repair financing", "/roof-financing/roof-repair-financing/")],
    "/flooring-financing/": [("kitchen remodel financing", "/remodel-financing/kitchen/"), ("bathroom remodel financing", "/remodel-financing/bathroom/")],
    "/pool-financing/": [("deck financing", "/deck-financing/"), ("fence financing", "/fence-financing/"), ("landscaping financing", "/landscaping-financing/")],
    "/remodel-financing/kitchen/": [("bathroom remodel financing", "/remodel-financing/bathroom/"), ("flooring financing", "/flooring-financing/")],
    "/remodel-financing/bathroom/": [("kitchen remodel financing", "/remodel-financing/kitchen/"), ("plumbing financing", "/plumbing-financing/"), ("flooring financing", "/flooring-financing/")],
    "/fence-financing/": [("deck financing", "/deck-financing/"), ("landscaping financing", "/landscaping-financing/"), ("pool financing", "/pool-financing/")],
    "/deck-financing/": [("fence financing", "/fence-financing/"), ("pool financing", "/pool-financing/"), ("landscaping financing", "/landscaping-financing/")],
    "/generator-financing/": [("HVAC financing", "/hvac-financing/"), ("solar financing", "/solar-financing/"), ("roof financing", "/roof-financing/")],
    "/garage-door-financing/": [("window financing", "/window-financing/"), ("siding financing", "/siding-financing/")],
    "/landscaping-financing/": [("fence financing", "/fence-financing/"), ("deck financing", "/deck-financing/"), ("pool financing", "/pool-financing/")],
    "/roof-financing/metal-roof-financing/": [("roof financing", "/roof-financing/"), ("commercial roof financing", "/roof-financing/commercial-roof-financing/")],
    "/roof-financing/roof-repair-financing/": [("roof financing", "/roof-financing/"), ("gutter financing", "/gutter-financing/")],
    "/roof-financing/commercial-roof-financing/": [("roof financing", "/roof-financing/"), ("construction business loans", "/contractor-business-loans/")],
    "/for-contractors/roofing/": [("HVAC financing for contractors", "/for-contractors/hvac/"), ("roofing business loans", "/contractor-business-loans/roofing/")],
    "/for-contractors/hvac/": [("financing for roofing companies", "/for-contractors/roofing/"), ("HVAC business loans", "/contractor-business-loans/hvac/")],
    "/contractor-business-loans/equipment-financing/": [("dump truck financing", "/contractor-business-loans/dump-truck-financing/"), ("construction line of credit", "/contractor-business-loans/line-of-credit/")],
    "/contractor-business-loans/dump-truck-financing/": [("construction equipment financing", "/contractor-business-loans/equipment-financing/"), ("working capital for contractors", "/contractor-business-loans/working-capital/")],
    "/contractor-business-loans/invoice-factoring/": [("construction line of credit", "/contractor-business-loans/line-of-credit/"), ("working capital for contractors", "/contractor-business-loans/working-capital/")],
    "/contractor-business-loans/line-of-credit/": [("construction invoice factoring", "/contractor-business-loans/invoice-factoring/"), ("construction equipment financing", "/contractor-business-loans/equipment-financing/")],
    "/contractor-business-loans/hvac/": [("plumbing business loans", "/contractor-business-loans/plumbing/"), ("HVAC financing for contractors", "/for-contractors/hvac/")],
    "/contractor-business-loans/plumbing/": [("HVAC business loans", "/contractor-business-loans/hvac/"), ("construction equipment financing", "/contractor-business-loans/equipment-financing/")],
    "/contractor-business-loans/landscaping/": [("construction equipment financing", "/contractor-business-loans/equipment-financing/"), ("dump truck financing", "/contractor-business-loans/dump-truck-financing/")],
    "/contractor-business-loans/roofing/": [("financing for roofing companies", "/for-contractors/roofing/"), ("working capital for contractors", "/contractor-business-loans/working-capital/")],
    "/contractor-business-loans/working-capital/": [("construction line of credit", "/contractor-business-loans/line-of-credit/"), ("construction invoice factoring", "/contractor-business-loans/invoice-factoring/")],
}

def _contains(text, kw):
    return kw.lower() in (text or "").lower()

REPORT = []

def apply(P):
    for path, (kw, vol, variants) in PRIMARY.items():
        p = P.get(path)
        if not p:
            continue
        if path in TITLES:
            p["title"], p["h1"] = TITLES[path]
        if not _contains(p.get("h1", ""), kw):
            REPORT.append(("h1 missing primary", path, kw))
        if path in METAS:
            p["meta"] = METAS[path]
        if path in ANSWERS and "answer" in p:
            p["answer"] = ANSWERS[path] + p["answer"]
        if not _contains(p.get("meta", ""), kw):
            REPORT.append(("meta missing primary", path, kw))
        if "answer" in p and not _contains(p["answer"], kw):
            REPORT.append(("answer missing primary", path, kw))
        if path in VARIANT_SECTIONS and "sections" in p:
            h, body = VARIANT_SECTIONS[path]
            if h not in [s[0] for s in p["sections"]]:
                p["sections"] = [p["sections"][0], (h, body)] + list(p["sections"][1:]) if p["sections"] else [(h, body)]
        elif path in VARIANT_SECTIONS and "prose" in p:
            h, body = VARIANT_SECTIONS[path]
            p["prose"] = p["prose"] + f"<h2 id='variant'>{esc(h)}</h2>{body}"
        if path in SIBLINGS and "sections" in p and p["sections"]:
            links = ", ".join(f'<a href="{u}">{esc(a)}</a>' for a, u in SIBLINGS[path][:-1]) + f' and <a href="{SIBLINGS[path][-1][1]}">{esc(SIBLINGS[path][-1][0])}</a>'
            h, body = p["sections"][0]
            if "See also" not in body:
                p["sections"][0] = (h, body + f"<p class='see-also'><strong>See also:</strong> {links}.</p>")
