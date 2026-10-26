"""Targeting pass from the first GSC export (Oct 16-24, 2026) cross-checked with Ahrefs volumes.

Striking-distance cluster: 'roofing companies that finance' (1,800/mo, KD0), 'roofing companies near me that
finance' (700, KD2), 'roofing companies that offer financing' (500, KD0), 'roofing contractors financing
available' (450, KD8), 'do roofers offer financing' (100, KD3) -> the roofer-financing post ranks 14-20.
KD0 money terms where thin pages sit at 60-90: fence (500), foundation repair (600), dump truck (600),
generator (250), water heater (350), kitchen remodel (700), construction equipment (1,100), hvac bad credit
(1,200 KD2), contractor financing for customers (300), equipment financing calculator (400)."""
from common import money, payment, esc

def pm(P, apr, n):
    return money(payment(P, apr, n), False)

CITY_LINKS = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in [("Houston", "/locations/texas/houston/"), ("Dallas", "/locations/texas/dallas/"), ("San Antonio", "/locations/texas/san-antonio/"), ("Oklahoma City", "/locations/oklahoma/oklahoma-city/"), ("Denver", "/locations/colorado/denver/"), ("Kansas City", "/locations/missouri/kansas-city/"), ("Minneapolis", "/locations/minnesota/minneapolis/"), ("Salt Lake City", "/locations/utah/salt-lake-city/"), ("Tampa", "/locations/florida/tampa/"), ("Nashville", "/locations/tennessee/nashville/")])


def apply(P):
    def page(path):
        return P.get(path)

    # ------------------------------------------------------------------ 1. roofer financing post -> "roofing companies that finance"
    p = page("/blog/roofing-companies-that-offer-financing/")
    if p:
        p["title"] = "Roofing Companies That Finance: How It Works & What to Ask"
        p["h1"] = "Roofing companies that finance: how it works, what it costs and what to ask"
        p["meta"] = "Most roofing companies that finance use a lender partner. How the plans work, what they really cost, how to find roofers near you that finance, and 8 questions to ask."
        p["answer"] = "Yes, most established roofing companies offer financing, usually through one or more lender partners rather than their own money. You apply at the estimate, the lender pays the roofer when the job is done, and you repay monthly. Plans range from standard fixed-rate loans to promotional 0% offers that can carry a dealer fee in the price. The eight questions below tell you which kind you're being offered, and whether your own loan at the cash price would be cheaper."
        p["sections"] = [
            ("Do roofers offer financing?", """<p>Most do. Roofing is a five-figure purchase that often arrives unplanned, so the majority of established roofing companies have at least one financing program, and many advertise "financing available" on their trucks and estimates. What differs is how it's set up. A few large companies carry their own paper; nearly everyone else enrolls with consumer lenders that specialize in home improvement. The roofer presents the plan, the lender makes the credit decision and pays the roofer on completion.</p>
<p>So the useful question isn't "do roofers offer financing" but "which plan is this roofer offering, who is the lender, and what does it cost compared with a loan I arrange myself?"</p>"""),
            ("How to find roofing companies near you that finance", f"""<p>Three reliable ways:</p>
<ul><li><strong>Ask at the estimate.</strong> Any roofer with a program will say so. Ask which lender, which plans and whether a cash discount exists.</li>
<li><strong>Check manufacturer networks.</strong> GAF and Owens Corning certified contractors often have access to manufacturer-backed financing with extended warranties.</li>
<li><strong>Bring your own financing.</strong> If a good local roofer doesn't offer a plan, that's not a reason to pick a worse roofer. An unsecured loan arranged through a marketplace such as AL Elite pays any roofer like cash, and often gets you the cash price.</li></ul>
<p>If you're in a storm market, our local guides cover roofer licensing rules, deductible laws and financing for each metro:</p><ul class="inline-links">{CITY_LINKS}</ul>"""),
        ] + list(p["sections"])
        p["faqs"] = [
            ("Do roofing companies offer financing?", "Most established roofing companies do, through one or more lender partners. The roofer presents the plan at the estimate; the lender approves the loan and pays the roofer when the roof is complete."),
            ("Do roofing companies that finance accept bad credit?", "Some programs include second-look lenders for lower credit scores, usually at higher APRs. If the roofer's plan declines you, you can still arrange financing independently, add a co-applicant, or reduce the amount by financing only the gap after an insurance claim."),
            ("Is roofing financing available with no money down?", "Many contractor plans and unsecured loans require no down payment; the lender pays the roofer on completion. A deposit may still be needed on some jobs, so ask the roofer what's required before work starts."),
        ] + list(p["faqs"])

    # ------------------------------------------------------------------ 2. HVAC bad credit money page
    p = page("/hvac-financing/bad-credit-hvac-financing/")
    if p:
        p["title"] = "HVAC Financing Bad Credit | AC & Furnace Loans for Low Scores"
        p["h1"] = "HVAC financing with bad credit: AC, furnace and heat pump loans for lower scores"
        p["sections"] = list(p.get("sections", [])) + [
            ("Is there \"guaranteed approval\" HVAC financing for bad credit?", """<p>No legitimate lender guarantees approval, and we won't either. Offers that advertise "guaranteed approval" or "no credit check" HVAC financing are usually rent-to-own plans or very high-cost loans where the total of payments can be far above the price of the system. What does exist is a wider range of lenders: some in our network consider scores below 600, look at income and recent payment history rather than the score alone, and offer a second look after a first decline. Expect a higher APR and a smaller amount than a prime borrower would see, and compare the total cost before signing.</p>"""),
            ("AC financing with bad credit: making the number smaller", """<p>Air conditioning failures are the most common emergency HVAC purchase, and lower credit makes a large request harder to approve. Three moves help: get two or three quotes on a standard-efficiency, correctly sized unit rather than the top model; apply utility rebates to reduce the amount; and put a few hundred dollars down if you can. A $7,500 request is approved far more often than an $11,500 one, and at an illustrative 19.99% APR over 60 months the payment difference is about """ + money(payment(11500, 19.99, 60) - payment(7500, 19.99, 60), False) + """ a month. Our guide to <a href="/blog/how-to-get-hvac-financing-with-bad-credit/">getting HVAC financing with bad credit</a> works through a full example.</p>"""),
            ("How HVAC lenders underwrite lower credit", """<p>Underwriting for unsecured HVAC loans looks at five things: credit score and recent history, income and the share already going to debt, the amount requested, length of credit history, and sometimes the contractor's standing. Lenders that serve lower scores weight recent behaviour more heavily: twelve months of on-time payments can outweigh an older collection. That's why a soft-pull pre-qualification is worth doing before any hard application: it shows which lenders are likely to say yes without the inquiry costing you points.</p>"""),
        ]
        p["faqs"] = list(p.get("faqs", [])) + [
            ("Can I get HVAC financing with a 550 credit score?", "Possibly, with a smaller amount, a higher APR and sometimes a co-applicant. Lenders that serve lower scores weigh income and recent payment history, so steady income and no recent missed payments help."),
            ("Is \"guaranteed approval\" HVAC financing real?", "No lender can guarantee approval. Ads using those words usually point to rent-to-own or very high-cost products. Compare the total of payments with the system's price before signing anything."),
        ]

    p = page("/roof-financing/bad-credit-roof-financing/")
    if p:
        p["sections"] = list(p.get("sections", [])) + [
            ("Roof financing with no credit check: what those offers really are", """<p>No legitimate lender offers roof financing with no credit check; every real loan involves some review of your credit or ability to repay. Offers using that phrase are usually rent-to-own arrangements or very high-cost loans. The useful alternative is a soft-pull pre-qualification, which shows what you're likely to be offered without touching your score. Many roofers and lenders in our network start there, and we tell you which ones do before you proceed. If the first lender declines, ask about a second-look lender, add a co-applicant, or finance only the gap after an insurance claim rather than the whole roof.</p>"""),
        ]
        p["faqs"] = list(p.get("faqs", [])) + [("Is there roof financing with no credit check?", "Not from legitimate lenders. A soft-pull pre-qualification is the real option: it shows likely offers without affecting your score, and only a formal application triggers a hard inquiry.")]

    # ------------------------------------------------------------------ 3. for-contractors -> "contractor financing for customers"
    p = page("/for-contractors/")
    if p:
        p["sections"] = list(p.get("sections", [])) + [
            ("Contractor financing for customers: how the money flows", """<p>In a customer financing program the homeowner is the borrower, not you. They apply (usually with a soft pull first), the lender approves and sets the rate, you do the work, and the lender pays you when the customer signs off, typically by ACH within a few business days. You never carry the receivable. Your costs are the dealer fee on any promotional plan you choose to offer and the time to train your team. Standard-rate plans usually cost you nothing, which is why we recommend leading with one and offering promotional plans only when they genuinely help the customer.</p>"""),
        ]
        p["faqs"] = list(p.get("faqs", [])) + [
            ("How can I offer financing to my customers as a contractor?", "Enroll in a program through a marketplace or lender partner, get each rep a pre-qualification link, present a monthly option next to the total on every estimate, and track close rate and ticket size for 90 days. Setup usually takes days to a few weeks."),
            ("What is contractor financing for homeowners?", "It's financing a contractor arranges for the homeowner through a lender partner, so the homeowner pays monthly instead of the full price up front. The lender, not the contractor, approves and funds the loan."),
        ]

    # ------------------------------------------------------------------ 4. calculator -> "equipment financing calculator"
    p = page("/tools/equipment-loan-calculator/")
    if p:
        p["title"] = "Equipment Financing Calculator | Construction Equipment Loan Payments"
        p["h1"] = "Equipment financing calculator: monthly payments for construction equipment loans"
    p = page("/contractor-business-loans/equipment-financing/")
    if p:
        p["sections"] = list(p.get("sections", [])) + [
            ("Construction equipment financing near you, and where to find it", """<p>Equipment lenders fund nationally, so "near me" matters less than it does for a roofer, but local still helps in two ways: regional dealers run captive financing on the brands they sell, and local banks and credit unions often offer competitive rates to businesses with a deposit relationship. A sensible search is three quotes: the dealer's captive program, a local bank or credit union, and a marketplace that reaches specialist equipment lenders in your state. Compare them on APR, down payment, term and the age limit on the machine at the end of the loan.</p>"""),
        ]

    # ------------------------------------------------------------------ 5. contractor business loans hub -> "roof coating business loans"
    p = page("/contractor-business-loans/")
    if p:
        p["prose"] = p.get("prose", "") + """<h2 id='roofing-business-loans'>Roofing and roof coating business loans</h2><p>Roofing companies have a specific cash cycle: storm seasons bring a surge of jobs that each need materials and crews up front, with insurance payments arriving weeks later. Commercial roof coating contractors add long project timelines and equipment such as sprayers and lifts. The usual fits are a <a href="/contractor-business-loans/line-of-credit/">line of credit</a> for materials and payroll during the surge, <a href="/contractor-business-loans/equipment-financing/">equipment financing</a> for coating rigs and lifts, and <a href="/contractor-business-loans/invoice-factoring/">factoring</a> for commercial jobs with slow-paying owners. See our page for <a href="/for-contractors/roofing/">roofing companies</a> for customer financing on the residential side.</p>"""

    # ------------------------------------------------------------------ 6. homepage-style internal links: money pages get a sibling link row via related lists
    for path, links in {
        "/fence-financing/": [("Deck financing", "/deck-financing/"), ("Home improvement financing", "/home-improvement-financing/")],
        "/foundation-repair-financing/": [("Home improvement financing", "/home-improvement-financing/"), ("Roof repair financing", "/roof-financing/roof-repair-financing/")],
        "/generator-financing/": [("HVAC financing", "/hvac-financing/"), ("Storm-market locations", "/locations/")],
        "/water-heater-financing/": [("HVAC financing", "/hvac-financing/"), ("Plumbing financing", "/plumbing-financing/")],
    }.items():
        p = page(path)
        if p:
            rel = list(p.get("related", []))
            for l in links:
                if l[1] not in [r[1] for r in rel]:
                    rel.append(l)
            p["related"] = rel
