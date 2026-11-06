"""Nov 6, 2026 audit fixes (GSC + crawl): title/meta length, exact-question FAQs for queries already at pos <20,
internal links to under-linked pages, and removal of unproven homepage claims."""
import re

TITLES = {
    "/": "Home Improvement & Contractor Financing | AL Elite Financing",
    "/blog/best-contractor-financing-companies/": "Best Contractor Financing Companies Compared (2026)",
    "/blog/emergency-furnace-replacement/": "Emergency Furnace Replacement: Cost, Payment & Bad Credit",
    "/blog/hearth-vs-service-finance-vs-greensky/": "Hearth vs Service Finance vs GreenSky vs Wisetack (2026)",
    "/blog/how-much-does-a-bathroom-remodel-cost/": "Bathroom Remodel Cost: Small, Mid-Range & Master (2026)",
    "/blog/ice-dams-removal-cost-insurance-prevention/": "Ice Dams: Safe Removal, Cost, Insurance & Prevention (2026)",
    "/blog/siding-replacement-cost/": "Siding Replacement Cost: Vinyl, Fiber Cement & More (2026)",
    "/blog/whole-house-generator-cost/": "Whole House Generator Cost: Installed Prices (2026)",
    "/contractor-business-loans/equipment-financing/": "Construction Equipment Financing | Excavator & Skid Steer Loans",
    "/contractor-business-loans/landscaping/": "Landscaping Business Loans | Financing for Landscapers",
    "/for-contractors/hvac/": "HVAC Financing for Contractors | Customer Financing on Jobs",
    "/for-contractors/solar/": "Solar Financing for Installers | Loan Programs for Contractors",
    "/how-we-make-money/": "How AL Elite Makes Money | Lender & Partner Compensation",
    "/plumbing-financing/": "Plumbing Financing | Repipe, Sewer & Emergency Plumbing Loans",
    "/roof-financing/metal-roof-financing/": "Metal Roof Financing | Standing Seam & Metal Shingle Loans",
    "/siding-financing/": "Siding Financing | Vinyl, Fiber Cement & Storm Damage Loans",
    "/tools/": "Financing Calculators | Roof, HVAC, Pool, Fence & Factoring",
}

def trim_meta(m, n=158):
    if len(m) <= n:
        return m
    cut = m[:n].rsplit(" ", 1)[0].rstrip(",;:- ")
    return cut + ("" if cut.endswith(".") else ".")

FAQS = {
 "/blog/hvac-companies-that-offer-financing/": [
  ("Can an HVAC company charge more if you finance?", "Indirectly, yes. Promotional plans such as '0% for 18 months' usually cost the company a dealer fee of several percent, and some build it into the price, which is why a cash price can be lower. Lender agreements and some state rules may restrict charging financed customers more than cash customers, so ask for both prices in writing and compare the total cost."),
  ("Do most HVAC companies offer financing?", "Most established ones do, through one or more lender partners. They present a plan at the quote, usually with a soft-pull pre-qualification, and the lender pays the company when the job is complete."),
  ("How does HVAC financing work?", "You apply (often with a soft credit pull first), the lender approves and sets the rate, the HVAC company installs the system, and the lender pays the company on completion while you repay the lender monthly. Compare the APR after any promotional period and the cash price.")],
 "/for-contractors/": [
  ("Which companies let contractors offer financing to homeowners?", "Four types of provider do: dealer-sponsored lender programs (Service Finance, Synchrony and manufacturer programs), contractor-paid marketplaces (Hearth), pay-over-time built into field-service software (Wisetack), and lender-paid marketplaces such as AL Elite and Acorn Finance. Our <a href='/blog/hearth-vs-service-finance-vs-greensky/'>comparison of the platforms</a> explains how each is paid and when the contractor is funded."),
  ("Which customer financing programs are best for contractors?", "It depends on your ticket size, how much you sell on promotional offers and who should receive the funds. Under about $10,000 inside field software, embedded pay-over-time fits; for mid-to-large tickets, a dealer-sponsored program for promotions plus a no-fee marketplace for everyone else is a common pairing. Use the <a href='/blog/best-contractor-financing-companies/'>provider scorecard</a> to compare."),
  ("Which lenders specialize in contractor financing?", "For customer financing: dealer-sponsored lenders and marketplaces that fund home improvement loans. For the contractor's own business: equipment lenders, factoring companies and lenders that understand progress billing and retainage. We match both; see <a href='/contractor-business-loans/'>contractor business loans</a>.")],
 "/blog/best-contractor-financing-companies/": [
  ("Which lenders specialize in contractor financing?", "Dealer-sponsored lenders and marketplaces for customer financing, and equipment, factoring and working-capital lenders that understand construction cash flow for the contractor's own business. Our <a href='/for-contractors/'>contractor financing</a> page explains both sides.")],
 "/blog/equipment-financing-vs-leasing/": [
  ("Can contractors lease used construction equipment instead of buying it?", "Yes. Many lessors lease used machines, usually on shorter terms with hour limits and higher implicit rates. Compare total cost minus resale value with the <a href='/tools/equipment-lease-vs-buy-calculator/'>equipment lease vs buy calculator</a> before choosing.")],
 "/blog/how-to-offer-financing-to-customers/": [
  ("How do I offer financing to my HVAC customers?", "Enroll in a customer financing program, give each tech a soft-pull pre-qualification link, present a monthly figure next to the total on every estimate and track close rate and ticket size for 90 days. See <a href='/for-contractors/hvac/'>HVAC financing for contractors</a>."),
  ("How do I offer financing to my customers as a contractor?", "Join a program through a lender partner or marketplace, train reps to show a monthly payment at the estimate, and decide your decline path. Standard-rate plans usually cost the contractor nothing; promotional plans carry a dealer fee.")],
}

RELATED = {
 "/window-financing/": [("Garage door financing", "/garage-door-financing/")],
 "/siding-financing/": [("Garage door financing", "/garage-door-financing/")],
 "/deck-financing/": [("Garage door financing", "/garage-door-financing/")],
 "/gutter-financing/": [("Garage door financing", "/garage-door-financing/")],
 "/blog/how-much-does-a-fence-cost/": [("Landscaping financing", "/landscaping-financing/")],
 "/window-financing/": [("Window companies that offer financing", "/blog/window-companies-that-offer-financing/"), ("Garage door financing", "/garage-door-financing/")],
 "/plumbing-financing/": [("Plumbers that offer financing", "/blog/plumbers-that-offer-financing/"), ("What to do if pipes freeze", "/blog/what-to-do-if-pipes-freeze/")],
 "/hvac-financing/": [("Heat pump tax credit 2026", "/blog/heat-pump-tax-credit-2026/")],
 "/pool-financing/": [("Pool loan calculator", "/tools/pool-loan-calculator/")],
 "/solar-financing/": [("Solar loan calculator", "/tools/solar-loan-calculator/")],
 "/for-contractors/": [("Hearth vs Service Finance vs GreenSky vs Wisetack", "/blog/hearth-vs-service-finance-vs-greensky/")],
}

def apply(P):
    for path, t in TITLES.items():
        if path in P:
            P[path]["title"] = t
    for path, p in P.items():
        if path.startswith("/blog/") and path != "/blog/" or path.startswith(("/locations/", "/tools/", "/for-contractors", "/contractor-business-loans")) or path == "/":
            pass
        t = p.get("title", "")
        if "Roof, HVAC, Kitchen & More" in t:
            p["title"] = t.replace("Roof, HVAC, Kitchen & More", "Roof, HVAC & More")
        m = p.get("meta", "")
        if m and len(m) > 160:
            p["meta"] = trim_meta(m)
    for path, qs in FAQS.items():
        p = P.get(path)
        if not p:
            continue
        have = {q for q, _ in p.get("faqs", [])}
        p["faqs"] = list(p.get("faqs", [])) + [x for x in qs if x[0] not in have]
    for path, rel in RELATED.items():
        p = P.get(path)
        if not p:
            continue
        cur = list(p.get("related", []))
        for r in rel:
            if r[1] not in [c[1] for c in cur]:
                cur.append(r)
        p["related"] = cur
