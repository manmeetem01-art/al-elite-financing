"""October 2026 re-audit pass.

1. Competitor-gap content on money pages (government-backed loans, cash-out refinance, PACE risk,
   contractor vetting) - topics NerdWallet, LendEDU, BadCredit.org and Bob Vila cover and we didn't.
2. "Sources and further reading" block on every content page, citing primary sources only
   (.gov agencies and the trade press already cited on the site). Injected by build.py.
3. Internal links for weakly linked pages (tools hub, garage door, commercial roof, roof repair,
   contractor trade pages).
Facts here were checked against the linked primary sources on 2026-10-22.
"""

S = {
    "hud_title1": ("HUD: FHA Title I property improvement loans", "https://www.hud.gov/program_offices/housing/sfh/title/title-i"),
    "hud_203k": ("HUD: FHA 203(k) rehabilitation mortgage", "https://www.hud.gov/program_offices/housing/sfh/203k"),
    "usda_504": ("USDA Rural Development: Section 504 home repair loans and grants", "https://www.rd.usda.gov/programs-services/single-family-housing-programs/single-family-housing-repair-loans-grants"),
    "doe_wap": ("U.S. Department of Energy: how to apply for weatherization assistance", "https://www.energy.gov/scep/wap/how-apply-weatherization-assistance"),
    "cfpb_pace_rule": ("CFPB: residential PACE financing rule", "https://www.consumerfinance.gov/rules-policy/final-rules/residential-property-assessed-clean-energy-financing-regulation-z/"),
    "cfpb_pace_report": ("CFPB: PACE financing and consumer outcomes", "https://www.consumerfinance.gov/about-us/newsroom/cfpb-proposes-new-consumer-protections-for-homeowners-seeking-clean-energy-financing"),
    "ftc_contractor": ("FTC: hiring a contractor", "https://consumer.ftc.gov/articles/hiring-contractor"),
    "acr": ("AnnualCreditReport.com: free credit reports (official site)", "https://www.annualcreditreport.com/"),
    "irs_946": ("IRS Publication 946: how to depreciate property", "https://www.irs.gov/publications/p946"),
    "irs_2290": ("IRS Form 2290: heavy highway vehicle use tax", "https://www.irs.gov/forms-pubs/about-form-2290"),
    "sba_loans": ("U.S. Small Business Administration: loans", "https://www.sba.gov/funding-programs/loans"),
    "noaa_spc": ("NOAA Storm Prediction Center: severe weather reports", "https://www.spc.noaa.gov/"),
    "claims": ("Claims Journal: 2025 hail claim payouts by state", "https://www.claimsjournal.com/news/national/2026/04/23/337102.htm"),
    "trane_fin": ("Trane: residential financing", "https://www.trane.com/residential/en/pricing/financing/"),
    "carrier_fin": ("Carrier: HVAC financing", "https://www.carrier.com/us/en/residential/homeowner-resources/financing/"),
    "achr": ("ACHR News: homeowners planning to finance projects", "https://achrnews.com/articles/144272-more-than-25-of-surveyed-homeowners-plan-to-finance-home-improvement-projects-by-borrowing-from-contractor"),
}

def a(key, text=None):
    label, url = S[key]
    return f'<a href="{url}" rel="noopener" target="_blank">{text or label}</a>'

HOMEOWNER = ["ftc_contractor", "acr"]
GOV = ["hud_title1", "hud_203k", "usda_504"]

# path (exact) or prefix ending in "*" -> source keys. First match wins; exact paths beat prefixes.
PAGE_SOURCES = {
    "/": ["hud_title1", "ftc_contractor", "sba_loans", "claims"],
    "/roof-financing/": ["claims", "hud_title1", "usda_504", "ftc_contractor", "noaa_spc"],
    "/roof-financing/bad-credit-roof-financing/": ["acr", "hud_title1", "usda_504", "ftc_contractor"],
    "/roof-financing/roof-repair-financing/": ["hud_title1", "usda_504", "ftc_contractor"],
    "/roof-financing/commercial-roof-financing/": ["sba_loans", "irs_946"],
    "/hvac-financing/": ["doe_wap", "hud_title1", "cfpb_pace_report", "trane_fin", "carrier_fin", "ftc_contractor"],
    "/hvac-financing/bad-credit-hvac-financing/": ["acr", "doe_wap", "hud_title1", "ftc_contractor"],
    "/solar-financing/": ["cfpb_pace_rule", "cfpb_pace_report", "ftc_contractor"],
    "/home-improvement-financing/": GOV + ["doe_wap", "cfpb_pace_report", "ftc_contractor"],
    "/for-contractors/*": ["achr", "ftc_contractor"],
    "/contractor-business-loans/dump-truck-financing/": ["sba_loans", "irs_946", "irs_2290"],
    "/contractor-business-loans/*": ["sba_loans", "irs_946"],
    "/locations/*": ["claims", "noaa_spc", "hud_title1", "ftc_contractor"],
    "/tools/equipment-loan-calculator/": ["irs_946", "sba_loans"],
    "/tools/*": ["hud_title1", "acr"],
    "/blog/roof-financing-after-hail-damage/": ["claims", "noaa_spc", "ftc_contractor", "hud_title1"],
    "/blog/does-insurance-cover-roof-replacement/": ["claims", "noaa_spc", "ftc_contractor"],
    "/blog/how-much-does-a-new-roof-cost-per-month/": ["hud_title1", "usda_504", "acr"],
    "/blog/how-to-finance-a-new-roof/": GOV + ["ftc_contractor"],
    "/blog/heloc-vs-roof-loan/": ["hud_title1", "hud_203k", "ftc_contractor"],
    "/blog/roofing-companies-that-offer-financing/": ["ftc_contractor", "hud_title1"],
    "/blog/how-to-get-hvac-financing-with-bad-credit/": ["acr", "doe_wap", "hud_title1"],
    "/blog/furnace-and-ac-replacement-financing/": ["doe_wap", "cfpb_pace_report", "ftc_contractor"],
    "/blog/how-construction-invoice-factoring-works/": ["sba_loans"],
    "/blog/used-vs-new-dump-truck-financing/": ["irs_2290", "irs_946", "sba_loans"],
    "/blog/equipment-financing-vs-leasing/": ["irs_946", "sba_loans"],
    "/blog/why-contractors-lose-jobs-without-financing/": ["achr", "ftc_contractor"],
    "/blog/how-to-offer-financing-to-customers/": ["achr", "cfpb_pace_rule"],
    "/blog/best-contractor-financing-companies/": ["achr", "sba_loans"],
    "/blog/how-to-bid-construction-jobs/": ["sba_loans", "irs_946"],
    "/blog/*": ["ftc_contractor", "acr"],
    "/about/": ["ftc_contractor"],
    "/how-we-make-money/": ["ftc_contractor"],
    "*": HOMEOWNER,  # every other consumer page (plumbing, siding, pool, etc.)
}
NO_SOURCES = {"/privacy/", "/terms/", "/accessibility/", "/do-not-sell/", "/blog/", "/locations/", "/tools/"}

def sources_for(path):
    if path in NO_SOURCES:
        return []
    if path in PAGE_SOURCES:
        return PAGE_SOURCES[path]
    best = None
    for k in PAGE_SOURCES:
        if k.endswith("*") and k != "*" and path.startswith(k[:-1]):
            if best is None or len(k) > len(best):
                best = k
    return PAGE_SOURCES[best] if best else PAGE_SOURCES["*"]

def sources_block(path):
    keys = sources_for(path)
    if not keys:
        return ""
    items = "".join(f"<li>{a(k)}</li>" for k in keys)
    return ("<section class='sources' aria-labelledby='sources-h'><h2 id='sources-h'>Sources and further reading</h2>"
            "<p>Primary sources we rely on for this page. Program rules change, so check the source before you rely on a figure.</p>"
            f"<ul>{items}</ul></section>")

SOURCES_CSS = """
.sources{margin-top:40px;padding:22px 24px;border:1px solid var(--line);border-radius:10px;background:var(--surface)}
.sources h2{font-size:1.15rem;margin:0 0 6px}
.sources p{color:var(--muted);font-size:.92rem;margin:0 0 10px}
.sources ul{margin:0;padding-left:1.1em;display:grid;gap:6px;font-size:.95rem}
"""


# ---------------------------------------------------------------- competitor-gap content
GOV_OPTION = ("Government-backed home repair loans",
    f"{a('hud_title1', 'FHA Title I')} loans are made by HUD-approved lenders for improvements that protect or improve a home's livability: up to $25,000 on a single-family home, terms up to 20 years, and loans over $7,500 must be secured by the property. In eligible rural areas, {a('usda_504', 'USDA Section 504')} offers repair loans to very-low-income owners and grants of up to $10,000 to owners 62 and older.",
    "Pros: insured or subsidized programs; may suit thinner equity or lower credit.",
    "Cons: fewer participating lenders, more paperwork and slower closing than a personal loan.")

CASHOUT_OPTION = ("Cash-out refinance",
    f"Replace your mortgage with a larger one and take the difference in cash. FHA's {a('hud_203k', '203(k)')} program goes further and rolls the cost of repairs into a purchase or refinance mortgage.",
    "Pros: often the lowest rate per dollar for very large projects.",
    "Cons: closing costs, a new long mortgage term, and it rarely makes sense if your current rate is lower than today's.")

WAP_OPTION = ("Weatherization and utility programs",
    f"The Department of Energy's {a('doe_wap', 'Weatherization Assistance Program')} pays for energy upgrades, sometimes including furnace repair or replacement, for eligible lower-income homeowners and renters. You apply through your state's weatherization agency. Many utilities add rebates or on-bill financing.",
    "Pros: grant-funded work for those who qualify; rebates reduce what you borrow.",
    "Cons: income limits, waiting lists and not for emergencies.")

VET_SECTION = ("Check the contractor before you check the financing", f"""<p>Financing problems often start as contractor problems. The Federal Trade Commission's guide to {a('ftc_contractor', 'hiring a contractor')} lists the warning signs worth knowing: door-to-door solicitation after a storm, pressure to pay the whole job up front, cash-only terms, and a contractor who steers you to a lender they know before you've seen a written quote.</p>
<ul><li>Get written quotes from more than one licensed, insured company, on the same scope.</li>
<li>Confirm permits are included and who pulls them.</li>
<li>Read the financing documents separately from the work contract. They are two agreements, and the loan is with the lender, not the contractor.</li>
<li>Never sign a blank or partly blank loan application.</li></ul>""")

PACE_SECTION = ("PACE financing: read this before you sign", f"""<p>Some contractors offer Property Assessed Clean Energy (PACE) financing for HVAC, solar and other energy upgrades. Instead of a loan payment, you repay through a special assessment on your property tax bill, secured by a lien on the home. The Consumer Financial Protection Bureau studied these loans and found they {a('cfpb_pace_report', 'raised property taxes by about $2,700 a year on average and increased mortgage delinquency')}. In December 2024 the CFPB {a('cfpb_pace_rule', 'finalized rules')} that require PACE lenders to check your ability to repay.</p>
<p>PACE can still be the right tool for some homeowners, but ask how the assessment changes your tax bill and escrow payment, whether your mortgage lender allows it, and what happens if you sell. Compare it with an unsecured loan before you sign.</p>""")

GOV_SECTION = ("Government-backed options most homeowners don't hear about", f"""<p>Three federal programs are worth a look before a high-APR loan, especially with lower credit or limited equity:</p>
<ul><li><strong>{a('hud_title1', 'FHA Title I property improvement loans')}.</strong> Made by HUD-approved lenders, up to $25,000 for a single-family home with terms up to 20 years. Loans over $7,500 must be secured by the home, and the home must have been occupied for at least 90 days.</li>
<li><strong>{a('hud_203k', 'FHA 203(k) rehabilitation mortgages')}.</strong> Combine the cost of repairs with a home purchase or refinance in one FHA-insured mortgage. Best for large projects.</li>
<li><strong>{a('usda_504', 'USDA Section 504 home repair')}.</strong> For very-low-income owners in eligible rural areas: low-rate repair loans repaid over 20 years, and grants of up to $10,000 for owners 62 and older to remove health and safety hazards.</li></ul>
<p>None of these is fast, and not every lender participates. They suit planned projects better than an emergency.</p>""")


MFR_HVAC_OPTION = ("Manufacturer financing programs",
    f"Major brands run financing programs through their dealers, usually with a bank partner such as Synchrony or Wells Fargo. {a('trane_fin', 'Trane')} and {a('carrier_fin', 'Carrier')} publish theirs; Lennox, Rheem and others have similar programs. Promotional rates are often tied to specific higher-efficiency equipment.",
    "Pros: promotional APRs on new equipment; applied for at the dealer visit.",
    "Cons: only through participating dealers and only on that brand's equipment; promotional terms may be deferred interest.")

MFR_ROOF_OPTION = ("Manufacturer and direct-lender programs",
    "Shingle makers such as GAF and Owens Corning offer financing through their certified contractor networks, and some banks (LightStream, for example) make unsecured roofing loans directly. Both are worth comparing against a marketplace offer on APR, fees and term.",
    "Pros: brand-backed programs often come with upgraded warranties; direct lenders can fund within days.",
    "Cons: tied to a certified contractor or a single lender's credit criteria, so there's no comparison built in.")

PLATFORM_SECTION = ("How to compare contractor financing platforms", f"""<p>Searching for contractor financing turns up platforms such as Hearth, Acorn Finance and HFS Financial, bank programs such as Regions, and manufacturer-backed plans. They differ on things that matter to your margins. Compare them on:</p>
<ul><li><strong>Dealer fees by plan.</strong> The fee on a promotional 0% plan can be several points of the job; standard-rate plans are often free to the contractor.</li>
<li><strong>Credit coverage.</strong> One prime lender, or a waterfall with second-look lenders for declined customers?</li>
<li><strong>Funding timing.</strong> On completion only, or with a draw at the start of larger jobs?</li>
<li><strong>Closed-loop or open.</strong> Some programs restrict funds to your company; marketplaces let the homeowner take the loan anywhere.</li>
<li><strong>Tools your reps will actually use.</strong> A mobile pre-qualification link with a soft pull beats a PDF application.</li>
<li><strong>Trade fit.</strong> A program built for roofing or HVAC approves more of the right customers than a generic one.</li></ul>
<p>We've written up the main providers in <a href="/blog/best-contractor-financing-companies/">best contractor financing companies</a> and the sales side in <a href="/blog/why-contractors-lose-jobs-without-financing/">why contractors lose jobs without financing</a>.</p>""")


def apply(pages_by_path):
    """Mutate page dicts in place. pages_by_path: {path: dict} across all generated page types."""
    def P(path):
        return pages_by_path.get(path)

    roof = P("/roof-financing/")
    if roof:
        roof["options"] = list(roof["options"]) + [MFR_ROOF_OPTION, GOV_OPTION, CASHOUT_OPTION]
        roof["sections"] = list(roof["sections"]) + [GOV_SECTION, VET_SECTION]
    hvac = P("/hvac-financing/")
    if hvac:
        hvac["options"] = list(hvac["options"]) + [MFR_HVAC_OPTION, WAP_OPTION, GOV_OPTION]
        hvac["sections"] = list(hvac["sections"]) + [PACE_SECTION, VET_SECTION]
    for path in ("/roof-financing/bad-credit-roof-financing/", "/hvac-financing/bad-credit-hvac-financing/"):
        pg = P(path)
        if pg:
            extra = WAP_OPTION if "hvac" in path else GOV_OPTION
            if pg.get("options"):
                pg["options"] = list(pg["options"]) + [extra]
            pg["sections"] = list(pg.get("sections", [])) + [("Check your reports first", f"<p>Before you apply, pull your free reports from all three bureaus at {a('acr', 'AnnualCreditReport.com')}, the official site, and dispute anything that's wrong. Paying a card balance below about 30% of its limit before the next statement can also help.</p>")]
    rr = P("/roof-financing/roof-repair-financing/")
    if rr:
        rr["sections"] = list(rr["sections"]) + [("Low-cost programs for essential repairs", f"<p>If the repair is about safety or keeping the house livable, check two federal programs first: {a('hud_title1', 'FHA Title I')} property improvement loans through HUD-approved lenders, and in rural areas {a('usda_504', 'USDA Section 504')} repair loans and grants. Both move slower than a personal loan, so they suit planned repairs more than an active leak.</p>")]
    solar = P("/solar-financing/")
    if solar and solar.get("sections") is not None:
        solar["sections"] = list(solar["sections"]) + [PACE_SECTION]
    hub = P("/home-improvement-financing/")
    if hub:
        hub["prose"] = hub.get("prose", "") + f"<h2 id='{'government-backed'}'>{GOV_SECTION[0]}</h2>{GOV_SECTION[1]}<h2 id='pace'>{PACE_SECTION[0]}</h2>{PACE_SECTION[1]}<h2 id='vet-contractor'>{VET_SECTION[0]}</h2>{VET_SECTION[1]}"
    fc = P("/for-contractors/")
    if fc:
        fc["sections"] = list(fc.get("sections", [])) + [PLATFORM_SECTION]
    cbl = P("/contractor-business-loans/")
    if cbl:
        cbl["prose"] = cbl.get("prose", "") + f"""<h2 id='sba'>SBA-backed loans for contractors</h2><p>The {a('sba_loans', 'U.S. Small Business Administration')} guarantees part of loans made by participating lenders, including the 7(a) program for working capital and equipment and microloans for smaller amounts. SBA loans usually carry longer terms than online lenders but take longer to close and need more documentation. They're worth comparing for larger, planned purchases rather than next-week payroll.</p>
<p>For equipment, ask your accountant how Section 179 and bonus depreciation apply this year; {a('irs_946', 'IRS Publication 946')} sets out the rules.</p>"""

    # ---- internal links for weakly linked pages
    def add_related(path, *links):
        pg = P(path)
        if not pg:
            return
        rel = list(pg.get("related", []))
        for lk in links:
            if lk[1] != path and lk[1] not in [r[1] for r in rel]:
                rel.append(lk)
        pg["related"] = rel

    tools_hub = ("All financing calculators", "/tools/")
    add_related("/tools/roof-financing-calculator/", tools_hub, ("Equipment loan calculator", "/tools/equipment-loan-calculator/"))
    add_related("/tools/equipment-loan-calculator/", tools_hub, ("Roof financing calculator", "/tools/roof-financing-calculator/"))
    add_related("/roof-financing/", ("Commercial roof financing", "/roof-financing/commercial-roof-financing/"))
    add_related("/roof-financing/metal-roof-financing/", ("Roof repair financing", "/roof-financing/roof-repair-financing/"), ("Commercial roof financing", "/roof-financing/commercial-roof-financing/"))
    add_related("/roof-financing/bad-credit-roof-financing/", ("Roof repair financing", "/roof-financing/roof-repair-financing/"))
    add_related("/contractor-business-loans/", ("Commercial roof financing", "/roof-financing/commercial-roof-financing/"))
    add_related("/for-contractors/roofing/", ("Commercial roof financing", "/roof-financing/commercial-roof-financing/"))
    for gpath in ("/generator-financing/", "/home-improvement-financing/", "/fence-and-deck-financing/", "/window-financing/"):
        add_related(gpath, ("Garage door financing", "/garage-door-financing/"))
    trade_loans = [("HVAC business loans", "/contractor-business-loans/hvac/"), ("Plumbing business loans", "/contractor-business-loans/plumbing/"), ("Landscaping business loans", "/contractor-business-loans/landscaping/")]
    for p in ("/contractor-business-loans/working-capital/", "/contractor-business-loans/equipment-financing/", "/contractor-business-loans/line-of-credit/", "/for-contractors/hvac/", "/for-contractors/plumbing/", "/for-contractors/landscaping/"):
        add_related(p, *trade_loans)
    for p in ("/for-contractors/hvac/", "/for-contractors/roofing/", "/for-contractors/remodeling/", "/solar-financing/"):
        add_related(p, ("Solar contractor financing", "/for-contractors/solar/"))
    add_related("/about/", ("Locations we serve", "/locations/"), ("Financing guides", "/blog/"), ("Calculators", "/tools/"))
