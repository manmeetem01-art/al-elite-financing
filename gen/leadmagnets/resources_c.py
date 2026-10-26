"""Shared lead magnet for the cost-guide posts (batch C): one planner that works for any home project."""
RESOURCES = []

def body_planner(d):
    d.section("Scope the project", "Step 1 of 5")
    d.p("Write down what you actually want done before you ask for a price. Vague scopes get vague quotes, and vague quotes become change orders.")
    d.fields([("Project (kitchen, fence, generator, siding, water heater, foundation, bathroom...)", None), ("Must-haves", None), ("Nice-to-haves (could be cut if the price is high)", None), ("Deadline or season", None)])
    d.multi("Scope in one paragraph (materials, size, what stays, what goes)", 60)
    d.tick_grid(["Permit likely needed", "HOA approval needed", "Insurance claim involved", "Rebates may apply", "Engineer or inspection report needed", "Can be phased"])

    d.section("Quote comparison", "Step 2 of 5")
    d.p("Fill in each quote on the same lines. If a line is missing from a quote, ask; missing items become change orders.")
    d.table(["Line", "Quote 1", "Quote 2", "Quote 3"], ["Company and licence #", "Materials / brand / grade", "Labor", "Removal and disposal", "Permits and inspections", "Code items / extras", "Contingency or allowances", "Warranty (workmanship / product)", "Start date and duration", "Cash price", "Financed price (if different)", "TOTAL"])
    d.callout("Same scope, same lines", "Three quotes are only comparable if they describe the same job. Send each contractor the same scope paragraph from Step 1.")

    d.section("Budget and monthly payment", "Step 3 of 5")
    d.calc([("A", "Chosen quote", None, False), ("B", "Rebates, credits or insurance payment", None, False), ("C", "Cash or savings you'll put in", None, False), ("D", "Amount to finance  =  A − B − C", None, True), ("E", "Monthly take-home income", None, False), ("F", "Essentials + existing debt payments", None, False), ("G", "Room each month  =  E − F", None, True)])
    d.p("Use the calculators at alelitefinancing.com/tools/ with amount D and a lender's quoted APR, then record the payment for each term.")
    d.table(["Term", "Monthly payment", "Total interest", "Fits inside G?"], ["24 months", "36 months", "60 months", "84 months", "120 months"])
    d.callout("Rule of thumb", "Take the shortest term with a payment you can carry comfortably, confirm there's no prepayment penalty, and match the term to a fraction of the project's life (a fence shouldn't carry a ten-year loan).")

    d.section("Financing options", "Step 4 of 5")
    d.cards([("Unsecured personal loan", "Days to fund, no lien, fixed rate. Fits most projects up to the lender's cap."), ("Contractor financing", "Monthly figure next to the quote; ask whether a promo rate is deferred interest and whether the price is the same for cash."), ("Home equity loan or HELOC", "Lower rate per dollar for large projects; weeks to close; lien on the home."), ("0% APR credit card", "Only for small amounts you can clear inside the promotional window."), ("Government-backed (FHA Title I, 203(k), USDA 504)", "Insured or subsidized; slower; suits planned projects and structural repairs."), ("Insurance claim", "For storm or sudden damage: finance only the gap between the payout and the price.")])
    d.table(["Offer", "APR incl. fees", "Term", "Monthly", "Total repaid", "Secured?"], ["Offer 1", "Offer 2", "Offer 3"])
    d.h2("Questions for every lender")
    d.check(["What is the APR including fees, and is the rate fixed?", "Is there an origination fee, and is it deducted from the loan?", "Is any promotional period deferred interest or waived interest?", "Is there a prepayment penalty?", "When is the contractor paid, and when does my first payment start?", "Does checking my options use a soft or hard credit inquiry?"])

    d.section("Contractor check and decision", "Step 5 of 5")
    d.check(["Licence or registration verified (where required)", "Insurance certificates seen (liability, workers' comp)", "Local address, reviews older than one season", "Itemized written quote on my scope", "Permits included and pulled by the contractor", "Financing documents read separately from the work contract", "No blank or partly blank forms signed", "Change-order pricing in the contract"])
    d.tick_grid(["Go ahead: Quote 1", "Go ahead: Quote 2", "Go ahead: Quote 3", "Reduce scope first", "Wait and save", "Phase the work"])
    d.multi("Decision, dates and notes", 70)
    d.cta("Ready to compare financing?", "alelitefinancing.com/home-improvement-financing/ reaches lenders who fund roofs, HVAC, kitchens, fences, generators and other home projects in your state. Or call (888) 968-0079.")

PLANNER = dict(
    slug="home-project-budget-financing-planner", pages=6,
    spec=dict(title="Home Project Budget & Financing Planner", tag="Home project planner", kicker="Free planner · any home project",
              title_lines=["Home Project Budget", "& Financing Planner"],
              subtitle="Scope the job, compare quotes on the same lines, work out the amount to finance and the monthly payment that fits, and vet the contractor before you sign.",
              inside=["Scope worksheet", "Quote comparison table", "Amount-to-finance calculator", "Payment-by-term table", "Financing options compared", "Contractor checklist"], body=body_planner),
    headline="Plan the project and the payment <em>before you sign</em>",
    pitch="A free fillable planner for any home project: scope it, compare quotes line by line, calculate what to finance and what it costs per month, and check the contractor.",
    bullets=["Scope worksheet and quote comparison", "Amount-to-finance and monthly budget calculator", "Six financing options compared", "Lender questions and contractor checklist"],
)
for _blog in ["/blog/how-much-does-a-kitchen-remodel-cost/", "/blog/how-much-does-a-bathroom-remodel-cost/", "/blog/how-much-does-a-fence-cost/", "/blog/does-insurance-cover-foundation-repair/", "/blog/whole-house-generator-cost/", "/blog/water-heater-replacement-cost/", "/blog/siding-replacement-cost/"]:
    RESOURCES.append(dict(PLANNER, blog=_blog))
