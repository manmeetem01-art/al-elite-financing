"""Homeowner-side lead magnets (7). Each entry: slug, blog path, PDF spec, and the article block copy."""

LENDER_QS = ["What is the APR including fees, and is the rate fixed?", "Is there an origination fee, and is it deducted from the loan amount?", "Is any promotional period deferred interest or waived interest?", "Is there a prepayment penalty?", "When is the contractor paid, and when does my first payment start?", "Does checking my options use a soft or hard credit inquiry?"]
CTA_ROOF = ("Ready to compare roof financing?", "alelitefinancing.com/roof-financing/ reaches lenders who fund roofs in your state. Or call (888) 968-0079.")
CTA_HVAC = ("Ready to compare HVAC financing?", "alelitefinancing.com/hvac-financing/ reaches lenders who fund HVAC work in your state. Or call (888) 968-0079.")

RESOURCES = []

# ------------------------------------------------------------- 1. Roof budget & payment planner
def body_roof_budget(d):
    d.section("How to use this planner", "Step 1 of 5")
    d.p("A roof payment comes from three numbers: the price, the APR and the term. This planner helps you pin down the price with real quotes, see what each term costs, and check the payment against your monthly budget before you apply.")
    d.h2("Before you start")
    d.check(["Two or three itemized roof quotes on the same scope (material line, underlayment, ventilation, flashing, gutters, per-sheet decking price)", "Your current monthly budget (income, essentials, existing debt payments)", "If insurance is involved: the adjuster's estimate, so you finance only the gap", "A recent look at your credit report (free at AnnualCreditReport.com)"])
    d.callout("Rule of thumb", "Go for the shortest term with a payment you can carry comfortably, and confirm there is no prepayment penalty so you can pay extra when you can.")

    d.section("Quote comparison", "Step 2 of 5")
    d.p("Fill in each quote on the same lines. If a quote is missing a line, ask the roofer, since missing items become change orders later.")
    d.table(["Line item", "Quote 1", "Quote 2", "Quote 3"], ["Company name", "Shingle / material line", "Tear-off and disposal", "Underlayment and ice & water", "Flashing, drip edge, vents", "Decking (per sheet price)", "Gutters / extras", "Permits included? (Y/N)", "Warranty (workmanship, years)", "Cash price", "Financed price (if different)", "TOTAL PRICE"])
    d.multi("Notes on differences between quotes", 50)

    d.section("Payment by term", "Step 3 of 5")
    d.p("Use the roof financing calculator at alelitefinancing.com/tools/roof-financing-calculator/ with your price and an APR a lender has quoted (or an estimate), then record the results here.")
    d.fields([("Roof price (or gap after insurance)", None), ("APR used (%)", "Lender quote or estimate")])
    d.table(["Term", "Monthly payment", "Total interest", "Total repaid"], ["36 months", "60 months", "84 months", "120 months", "144 months"])
    d.callout("Example", "At an illustrative 9.99% APR, a $15,000 roof is about $484/month over 36 months, $319 over 60, $249 over 84 and $198 over 120. Total interest rises from about $2,400 at 36 months to about $8,800 at 120.")

    d.section("Budget check", "Step 4 of 5")
    d.p("A payment fits when it leaves room after essentials and existing debt, without draining your emergency fund.")
    d.calc([("A", "Monthly take-home income", "All household income after tax", False), ("B", "Essentials (housing, utilities, food, insurance, transport)", None, False), ("C", "Existing debt payments (cards, car, student loans)", None, False), ("D", "Room each month  =  A − B − C", None, True), ("E", "Proposed roof payment", "From the term you prefer", False), ("F", "Left over after the roof payment  =  D − E", "Aim to keep a cushion", True)])
    d.h2("Decide")
    d.tick_grid(["Payment fits comfortably", "Fits only on the longer term", "Need to reduce the amount", "Wait and save first"])
    d.multi("What would change the decision? (rebates, insurance, cheaper material, co-applicant)", 48)

    d.section("Before you apply", "Step 5 of 5")
    d.h2("Questions to ask every lender")
    d.check(LENDER_QS)
    d.h2("Documents to have ready")
    d.tick_grid(["Government ID", "Recent pay stubs or bank statements", "Roofer's written quote", "Insurance estimate (if any)", "Mortgage statement (for equity options)", "Co-applicant details (if any)"])
    d.multi("Notes", 60)
    d.cta(*CTA_ROOF)

RESOURCES.append(dict(
    slug="roof-budget-payment-planner", blog="/blog/how-much-does-a-new-roof-cost-per-month/", pages=6,
    spec=dict(title="Roof Budget & Payment Planner", tag="Roof budget planner", kicker="Free planner · for homeowners",
              title_lines=["Roof Budget &", "Payment Planner"],
              subtitle="Compare quotes line by line, see what each loan term costs, and check the payment against your real monthly budget before you apply.",
              inside=["Quote comparison table", "Payment-by-term worksheet", "Monthly budget check", "Lender question list", "Document checklist", "Decision page"], body=body_roof_budget),
    headline="Find the roof payment that <em>actually fits</em> your budget",
    pitch="A free fillable planner: compare your quotes, record the payment for each term, and run a simple budget check before you talk to a lender.",
    bullets=["Quote comparison on the same 12 lines", "Payment and total interest by term", "Monthly room-after-essentials calculator", "Lender questions and document checklist"],
))

# ------------------------------------------------------------- 2. HVAC approval checklist (lower credit)
def body_hvac_bad(d):
    d.section("Shrink the number first", "Step 1 of 5")
    d.p("With lower credit, the most effective move is to need less money. Smaller requests are easier to approve and cheaper to carry.")
    d.check(["Technician confirmed it's a replacement, not a repair (ask to see the failed part)", "Two or three quotes on the same tonnage and efficiency", "Load calculation (Manual J) done, so the system isn't oversized", "Compared standard vs high efficiency on total cost, not just the sticker", "Checked utility rebates for qualifying equipment", "Checked the Weatherization Assistance Program (energy.gov) if income-eligible"])
    d.calc([("A", "Lowest sensible quote", None, False), ("B", "Rebates and credits", None, False), ("C", "Down payment from savings", None, False), ("D", "Amount to finance  =  A − B − C", None, True)])

    d.section("Credit prep", "Step 2 of 5")
    d.p("Pull your free reports at AnnualCreditReport.com (the official site) and note what you see.")
    d.fields([("Current score (approx.)", None), ("Bureau(s) checked", None), ("Errors found to dispute", None), ("Card balances above 30% of limit", "Paying these down helps")])
    d.check(["Disputed any accounts that aren't mine or are reported wrong", "Paid a card balance below 30% of its limit before the next statement", "Gathered proof of all income (pay stubs, benefits, side income)", "Avoided new hard inquiries while shopping"])
    d.callout("Soft pull first", "Check options with lenders that use a soft inquiry before any formal application. Scattering hard applications in a panic lowers your score and your chances.")

    d.section("Strengthen the application", "Step 3 of 5")
    d.cards([("Co-applicant", "A spouse or family member with stronger credit and income on the application can open better offers. They share full responsibility for the loan."), ("Down payment", "Even a few hundred dollars reduces the amount and signals commitment."), ("Realistic term", "A payment that fits reduces the lender's worry about missed payments."), ("Complete documents", "ID, pay stubs or bank statements, the contractor's quote. Complete applications get faster decisions.")])
    d.fields([("Co-applicant name (if any)", None), ("Their relationship / credit standing", None)])
    d.multi("Income sources to document", 44)

    d.section("Offers to walk away from", "Step 4 of 5")
    d.check(["'Guaranteed approval' or 'no credit check' on a large amount", "No clear APR, fees or total repaid in writing before signing", "Rent-to-own or lease-to-own HVAC where total payments far exceed the price", "Any upfront fee to 'secure' a loan", "Pressure to sign today; a good contractor will hold a quote for a day"])
    d.h2("Compare the offers you do get")
    d.table(["Offer", "APR", "Term (months)", "Monthly", "Total repaid", "Fees"], ["Contractor plan", "Lender 1", "Lender 2", "Lender 3"])

    d.section("If financing doesn't come together", "Step 5 of 5")
    d.cards([("Repair to buy a season", "If a reputable technician says it's safe, a repair can buy time to improve your credit."), ("Energy and weatherization assistance", "Community action agencies and utilities run programs for eligible households; apply through your state."), ("Warranty check", "If the failed part is still under manufacturer warranty, the repair may be much cheaper."), ("Contractor payment plan", "Some HVAC companies offer in-house plans on smaller amounts.")])
    d.multi("Plan B notes", 50)
    d.cta(*CTA_HVAC)

RESOURCES.append(dict(
    slug="hvac-financing-approval-checklist", blog="/blog/how-to-get-hvac-financing-with-bad-credit/", pages=6,
    spec=dict(title="HVAC Financing Approval Checklist", tag="HVAC approval checklist", kicker="Free checklist · lower credit scores",
              title_lines=["HVAC Financing", "Approval Checklist"],
              subtitle="Shrink the amount you need, prepare your credit, strengthen the application and spot the offers to avoid, with fillable worksheets for each step.",
              inside=["Shrink-the-number calculator", "Credit prep checklist", "Co-applicant and documents", "Offers to walk away from", "Offer comparison table", "Plan B options"], body=body_hvac_bad),
    headline="Improve your odds of <em>HVAC approval</em> with lower credit",
    pitch="A free fillable checklist: reduce the amount, fix what you can on your credit report, prepare a stronger application and compare offers safely.",
    bullets=["Shrink-the-number calculator", "Credit report prep steps", "Co-applicant and document checklist", "Offer comparison table and red flags"],
))

# ------------------------------------------------------------- 3. HVAC quote comparison & financing checklist
def body_hvac_quote(d):
    d.section("What are you actually buying?", "Step 1 of 5")
    d.p("Quotes for 'a new AC' can describe very different jobs. Tick what each quote covers before comparing prices.")
    d.tick_grid(["Furnace only", "AC condenser + coil", "Full split system", "Heat pump", "Dual-fuel (heat pump + furnace)", "Ductwork repairs", "Thermostat", "Electrical / gas line work", "Permits", "Haul-away of old equipment"])
    d.callout("Match the halves", "Replacing only the outdoor unit with a mismatched indoor coil can hurt efficiency and void warranties. Ask whether the indoor and outdoor components are a matched system.")

    d.section("Quote comparison", "Step 2 of 5")
    d.p("Write the model numbers; they let you compare like for like.")
    d.table(["Line", "Quote 1", "Quote 2", "Quote 3"], ["Company", "Equipment brand / model numbers", "Size (tons or BTU)", "SEER2 / AFUE / HSPF2", "Parts warranty (years)", "Labor warranty (years)", "Load calculation done? (Y/N)", "Ducts / thermostat included?", "Permits and haul-away included?", "Utility rebates applied", "Cash price", "TOTAL PRICE"])

    d.section("Repair or replace?", "Step 3 of 5")
    d.fields([("Age of current system (years)", None), ("Repair quote ($)", None), ("Replacement quote ($)", None), ("Refrigerant type", "R-22 is phased out; repairs cost more")])
    d.check(["Repeated breakdowns in the last two years", "Cracked heat exchanger (safety issue: replace)", "Energy bills rising while comfort falls", "Repair cost is a large fraction of replacement on an old system"])
    d.p("If several boxes are ticked, replacement is usually the better long-term value. If none are, a safe repair can buy time to plan and compare financing calmly.")

    d.section("Financing comparison", "Step 4 of 5")
    d.p("Most HVAC financing is a fixed-rate installment loan paid to the contractor on completion. Compare the contractor's plan with at least one independent option.")
    d.table(["Offer", "APR", "Term", "Monthly", "Total repaid", "Dealer fee in price?"], ["Contractor plan (standard)", "Contractor promo plan", "Independent lender 1", "Independent lender 2", "Utility on-bill program"])
    d.callout("Promotional plans", "Ask whether '0% for 18 months' is deferred interest (all back interest charged if any balance remains) or waived interest. And ask what the price would be if you paid another way; a dealer fee may be built in.")
    d.h2("Questions to ask before you sign")
    d.check(LENDER_QS + ["Who registers the warranty, and what does the labor warranty cover?"])

    d.section("Decision and notes", "Step 5 of 5")
    d.tick_grid(["Repair now, replace later", "Replace: standard efficiency", "Replace: high efficiency", "Replace: heat pump"])
    d.fields([("Chosen contractor", None), ("Chosen financing", None), ("Install date", None), ("First payment date", None)])
    d.multi("Notes", 70)
    d.cta(*CTA_HVAC)

RESOURCES.append(dict(
    slug="hvac-quote-financing-checklist", blog="/blog/furnace-and-ac-replacement-financing/", pages=6,
    spec=dict(title="HVAC Quote Comparison & Financing Checklist", tag="HVAC quote checklist", kicker="Free checklist · furnace, AC and heat pump replacement",
              title_lines=["HVAC Quote Comparison", "& Financing Checklist"],
              subtitle="Compare replacement quotes model for model, decide repair vs replace, and line up financing offers side by side before you sign anything.",
              inside=["Scope checklist", "Quote comparison table", "Repair-or-replace test", "Financing offer comparison", "Promo plan questions", "Decision page"], body=body_hvac_quote),
    headline="Compare HVAC quotes and financing <em>like for like</em>",
    pitch="A free fillable checklist that puts model numbers, efficiency, warranties and financing offers side by side so the cheapest quote doesn't become the most expensive job.",
    bullets=["Quote comparison with model numbers and SEER2", "Repair-or-replace checklist", "Financing offers side by side", "Promo plan and lender questions"],
))

# ------------------------------------------------------------- 8. Roof loan comparison worksheet (HELOC vs HE loan vs unsecured)
def body_roof_loan_compare(d):
    d.section("Which product fits your situation?", "Step 1 of 4")
    d.tick_grid(["Roof is urgent (this month)", "Planned replacement (months away)", "Little or no home equity", "Plenty of equity (20%+ after loan)", "Prefer no lien on the home", "Want the lowest rate per dollar", "Current mortgage rate is very low", "Amount is under $10,000"])
    d.cards([("Unsecured roof loan", "Days to fund, no lien, fixed rate. Wins on urgency, low equity and moderate amounts."), ("Home equity loan", "Lower fixed rate, 3 to 6 weeks to close, closing costs, lien on the home. Wins on planned, larger projects."), ("HELOC", "Variable rate, interest-only draw period then full payments. Flexible, but watch the payment jump and rate changes.")])

    d.section("Side-by-side comparison", "Step 2 of 4")
    d.p("Get a written quote or estimate for each route and fill in the same lines. The APR includes closing costs, so compare it, not the headline rate.")
    d.table(["Line", "Unsecured loan", "Home equity loan", "HELOC"], ["Lender", "Amount", "Rate (fixed / variable)", "APR incl. fees", "Term / draw period", "Closing or origination costs", "Monthly payment", "Total interest", "Time to money", "Prepayment penalty?", "Secured by home? (Y/N)"])
    d.callout("Example", "$18,000 over 10 years at 8.25% (home equity loan) is about $221/month and $8,500 interest; the same amount over 5 years at 11.99% (unsecured) is about $400/month and $6,000 interest. Lower rate doesn't always mean lower total cost once the term is longer.")

    d.section("Equity and HELOC checks", "Step 3 of 4")
    d.calc([("A", "Estimated home value", None, False), ("B", "Mortgage balance (and any other liens)", None, False), ("C", "Equity  =  A − B", None, True), ("D", "Lender's required cushion (often 15–20% of A)", None, False), ("E", "Borrowable equity  =  C − D", "Rough guide; lenders differ", True)])
    d.h2("HELOC questions")
    d.check(["When does the draw period end, and what will the payment be then?", "Can I lock a fixed rate on the amount I draw for the roof?", "Annual fee, inactivity fee, early closure fee?", "Can the lender freeze or reduce the line, and when?"])

    d.section("Decision", "Step 4 of 4")
    d.h2("Questions for every lender")
    d.check(LENDER_QS)
    d.tick_grid(["Unsecured roof loan", "Home equity loan", "HELOC", "Combination (savings + loan)"])
    d.multi("Why this choice, and what would change it", 70)
    d.cta(*CTA_ROOF)

RESOURCES.append(dict(
    slug="roof-loan-comparison-worksheet", blog="/blog/heloc-vs-roof-loan/", pages=5,
    spec=dict(title="Roof Loan Comparison Worksheet", tag="Roof loan comparison", kicker="Free worksheet · HELOC vs home equity loan vs unsecured",
              title_lines=["Roof Loan", "Comparison Worksheet"],
              subtitle="Decide between a HELOC, a home equity loan and an unsecured roof loan with a situation test, a side-by-side table and an equity calculator.",
              inside=["Situation test", "Side-by-side comparison table", "Equity calculator", "HELOC question list", "Lender questions", "Decision page"], body=body_roof_loan_compare),
    headline="HELOC, home equity loan or roof loan: <em>decide in one page</em>",
    pitch="A free fillable worksheet with a situation test, a side-by-side comparison table and an equity calculator so you pick the cheapest route for your roof.",
    bullets=["Situation test: urgent vs planned, equity vs none", "Side-by-side table on 11 lines", "Borrowable-equity calculator", "HELOC and lender questions"],
))

# ------------------------------------------------------------- 9. Roofer financing plan checklist
def body_roofer_plan(d):
    d.section("Know which plan you're being offered", "Step 1 of 4")
    d.cards([("Standard installment plan", "Fixed APR over 3 to 12 years. Often no dealer fee to the roofer, so no reason for the price to change."), ("Promotional plan", "'0% for 18 months' or 'no payments for 12 months'. The roofer pays a dealer fee, which can be built into your price."), ("Reduced-rate long-term plan", "Below-market rate for 10 to 15 years with a dealer fee attached. Lower payment, more total interest.")])
    d.tick_grid(["Standard plan", "Promotional plan", "Reduced-rate long-term plan", "Not sure yet"])
    d.callout("Deferred vs waived interest", "With deferred interest, interest accrues from day one and is charged in full if any balance remains at the end of the promotion. With waived interest, nothing accrues. Ask which one, in writing.")

    d.section("Questions for the roofer", "Step 2 of 4")
    d.check(["Who is the lender, and is this a loan or a credit line?", "What is the APR after any promotional period ends?", "Is the promotional interest deferred or waived?", "Is there a dealer fee, and would the price be lower if I paid cash or used my own lender?", "When does the lender pay you, and when does my first payment start?", "Is there a prepayment penalty?", "Does the pre-qualification use a soft inquiry?", "Can I see the loan documents before I sign the roofing contract?"])
    d.multi("Answers and anything that didn't add up", 60)

    d.section("Price comparison", "Step 3 of 4")
    d.p("Fill in the three routes. The 'cheapest' plan depends on whether you can really pay the promo balance in time.")
    d.table(["Route", "Price", "APR / terms", "Monthly", "Total paid", "Notes"], ["Roofer standard plan", "Roofer promo plan", "Own loan at cash price"])
    d.callout("Example", "$14,000 at 10.99% over 84 months is about $240/month ($20,100 total). A '0%' plan with an 8% fee in the price ($15,120) paid over 18 months is $840/month. Your own loan on a $13,500 cash price at 11.99% over 60 months is about $300/month ($18,000 total).")

    d.section("Vet the company, then decide", "Step 4 of 4")
    d.check(["State license or registration verified", "Insurance certificates (liability and workers' comp) seen", "Local address and phone in service before the storm", "Reviews that mention financing specifically", "Full price in writing before financing was discussed", "No pressure to sign the loan application before the roofing contract", "No partly blank forms"])
    d.tick_grid(["Take the roofer's standard plan", "Take the promo plan (can clear it in time)", "Use my own lender", "Get another quote"])
    d.multi("Notes", 50)
    d.cta(*CTA_ROOF)

RESOURCES.append(dict(
    slug="roofer-financing-plan-checklist", blog="/blog/roofing-companies-that-offer-financing/", pages=5,
    spec=dict(title="Roofer Financing Plan Checklist", tag="Roofer financing checklist", kicker="Free checklist · before you sign a roofer's plan",
              title_lines=["Roofer Financing", "Plan Checklist"],
              subtitle="Work out which plan you're being offered, the eight questions that expose a bad one, and whether your own loan at the cash price beats it.",
              inside=["Plan type identifier", "Deferred vs waived interest", "Eight roofer questions", "Price comparison table", "Company vetting list", "Decision page"], body=body_roofer_plan),
    headline="Eight questions before you sign a <em>roofer's financing plan</em>",
    pitch="A free fillable checklist that identifies the plan type, exposes deferred interest and dealer fees, and compares the roofer's plan with your own loan at the cash price.",
    bullets=["Plan type identifier", "Eight questions to ask the roofer", "Promo vs standard vs own loan comparison", "Company vetting checklist"],
))

# ------------------------------------------------------------- 13. Insurance claim review checklist
def body_claim_review(d):
    d.section("Your policy, decoded", "Step 1 of 5")
    d.fields([("Insurer and policy number", None), ("Dwelling coverage (Coverage A)", None), ("Wind/hail deductible (% or $)", "If %, multiply by Coverage A"), ("Deductible in dollars", None)])
    d.tick_grid(["Replacement cost (RCV) policy", "Actual cash value (ACV) policy", "ACV on roof only", "Roof age payment schedule", "Cosmetic damage exclusion", "Matching rule applies in my state"])
    d.fields([("Roof age and install date", None), ("Deadline to claim depreciation", "Check the policy; often 6–24 months")])

    d.section("Reading the adjuster's estimate", "Step 2 of 5")
    d.p("Ask for the full estimate, not the summary. Record the key lines.")
    d.calc([("A", "Replacement cost value (RCV)", None, False), ("B", "Depreciation (recoverable?)", None, False), ("C", "Actual cash value  =  A − B", None, True), ("D", "Deductible", None, False), ("E", "First payment  =  C − D", None, True)])
    d.h2("Items the estimate should include")
    d.tick_grid(["Tear-off and disposal", "Shingle squares + waste", "Underlayment / ice & water", "Drip edge and flashing", "Vents and pipe boots", "Decking allowance", "Gutters and downspouts", "Code upgrade allowance", "Second layer (if any)", "Permits"])

    d.section("Supplements, re-inspection, appraisal", "Step 3 of 5")
    d.cards([("Supplement", "Your roofer submits missed or underpriced items with photos. Routine and often approved."), ("Re-inspection", "A second adjuster visit, useful after a rushed first inspection."), ("Appraisal clause", "For disputes about amount (not coverage): you and the insurer each hire an appraiser; an umpire resolves differences."), ("State insurance department", "Takes complaints about coverage disputes; a public adjuster or attorney may be worth it on a large claim.")])
    d.table(["Missed / underpriced item", "Roofer's price", "Insurer's price", "Status"], ["", "", "", "", ""])

    d.section("The gap you need to finance", "Step 4 of 5")
    d.calc([("F", "Roofer's contract price", None, False), ("G", "Owed to roofer before depreciation arrives  =  F − E", "Short-term gap", True), ("H", "Permanent gap  =  F − A + D", "Deductible + uncovered items; this is what you finance", True)])
    d.callout("Never finance the whole roof when insurance pays most of it", "Borrow against H, not F. A $4,000 gap at an illustrative 11.99% over 36 months is about $133/month.")

    d.section("Before the next storm, and notes", "Step 5 of 5")
    d.check(["'Before' photos of the roof and soft metals, dated", "Roof install date and warranty paperwork filed", "Deductible calculated in dollars and a plan for it", "Agent asked about roof schedules, ACV and cosmetic exclusions"])
    d.multi("Claim notes, dates, who said what", 110)
    d.cta(*CTA_ROOF)

RESOURCES.append(dict(
    slug="roof-insurance-claim-review-checklist", blog="/blog/does-insurance-cover-roof-replacement/", pages=6,
    spec=dict(title="Roof Insurance Claim Review Checklist", tag="Roof claim review", kicker="Free checklist · roof insurance claims",
              title_lines=["Roof Insurance Claim", "Review Checklist"],
              subtitle="Decode your policy, read the adjuster's estimate line by line, know when to supplement or appeal, and calculate the gap insurance leaves.",
              inside=["Policy decoder", "Adjuster estimate reader", "Supplement and appraisal guide", "Missed-items tracker", "Financing gap calculator", "Before-the-storm checklist"], body=body_claim_review),
    headline="Make sure your <em>roof claim</em> pays what it should",
    pitch="A free fillable checklist that decodes your policy, walks through the adjuster's estimate, tracks supplements and calculates the gap you may need to finance.",
    bullets=["Policy decoder (deductible, RCV vs ACV, schedules)", "Adjuster estimate reader", "Supplement, re-inspection and appraisal guide", "Financing gap calculator"],
))

# ------------------------------------------------------------- 14. Roof financing option picker
def body_option_picker(d):
    d.section("Your situation", "Step 1 of 4")
    d.tick_grid(["Storm damage, insurance paying most", "Planned replacement, no rush", "Urgent, little equity", "Lower credit score", "Large project ($25,000+)", "Prefer no lien on the home", "Very low current mortgage rate", "Can clear a promo balance in 12–18 months"])
    d.fields([("Roof quote or gap to finance ($)", None), ("Approximate credit score", None), ("Home equity (value minus mortgage)", None), ("When the roof must happen", None)])

    d.section("The options, side by side", "Step 2 of 4")
    d.cards([("Unsecured personal loan", "Fast, no lien, fixed rate. Fits urgent roofs, modest amounts, low equity."), ("Contractor financing", "At the quote, sometimes promotional. Ask about deferred interest and dealer fees."), ("Home equity loan", "Lower fixed rate, weeks to close, lien on home. Fits planned, large projects."), ("HELOC", "Variable, flexible draw; watch the end of the draw period."), ("0% APR credit card", "Only for small amounts you can clear before the promo ends."), ("Insurance claim", "Covers most of a storm roof; finance the deductible and uncovered items only."), ("Government-backed (FHA Title I, 203(k), USDA 504)", "Insured or subsidized; slower, fewer lenders, suits planned projects and lower credit.")])

    d.section("Offer comparison", "Step 3 of 4")
    d.table(["Offer", "APR incl. fees", "Term", "Monthly", "Total repaid", "Secured?"], ["Personal loan 1", "Personal loan 2", "Contractor plan", "Home equity / HELOC", "Other"])
    d.h2("Questions for every lender")
    d.check(LENDER_QS)
    d.callout("Four steps that improve offers everywhere", "Finance the gap, not the roof. Pay a card balance down before applying. Have income documents ready. Check options with a soft pull before any hard inquiry.")

    d.section("Decision", "Step 4 of 4")
    d.tick_grid(["Personal loan", "Contractor plan", "Home equity loan", "HELOC", "Government-backed program", "Savings + small loan"])
    d.fields([("Chosen lender / program", None), ("Monthly payment", None), ("Term", None), ("Total cost", None)])
    d.multi("Notes and next steps", 80)
    d.cta(*CTA_ROOF)

RESOURCES.append(dict(
    slug="roof-financing-option-picker", blog="/blog/how-to-finance-a-new-roof/", pages=5,
    spec=dict(title="Roof Financing Option Picker", tag="Roof financing picker", kicker="Free worksheet · seven ways to pay for a roof",
              title_lines=["Roof Financing", "Option Picker"],
              subtitle="Match your situation to the right way to pay for a roof, compare the offers you get on the same lines, and record the decision.",
              inside=["Situation checklist", "Seven options explained", "Offer comparison table", "Lender question list", "Four approval boosters", "Decision page"], body=body_option_picker),
    headline="Seven ways to pay for a roof: <em>pick yours</em>",
    pitch="A free fillable worksheet that matches your situation to the right financing option and compares the offers you receive on the same lines.",
    bullets=["Situation checklist", "Personal loan to government programs, explained", "Offer comparison on six columns", "Lender questions and approval boosters"],
))
