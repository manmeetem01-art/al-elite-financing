"""Contractor-side lead magnets (7)."""

CTA_FC = ("Ready to offer financing to your customers?", "alelitefinancing.com/for-contractors/ matches you with programs built for your trade. Or call (888) 968-0079.")
CTA_BL = ("Ready to compare contractor business loans?", "alelitefinancing.com/contractor-business-loans/ reaches lenders who work with contractors in your state. Or call (888) 968-0079.")

RESOURCES = []

# ------------------------------------------------------------- 4. Factoring cost calculator & due diligence
def body_factoring(d):
    d.section("Is factoring the right tool?", "Step 1 of 4")
    d.tick_grid(["Subcontractor with creditworthy GCs", "GCs pay reliably but in 45–90 days", "Growing faster than cash allows", "Can't yet qualify for a bank line", "Margins can absorb a few percent", "Most billing is retainage-heavy (caution)", "Customers often dispute invoices (caution)", "Would need to factor everything forever (caution)"])
    d.cards([("Fits when", "The top five boxes are ticked and the bottom three aren't."), ("Think twice when", "Thin margins, frequent disputes or retainage-heavy billing. Factoring speeds up cash; it doesn't fix pricing.")])

    d.section("Cost calculator", "Step 2 of 4")
    d.p("Fill in one real invoice and the factor's quoted schedule. Fees are usually per 30 days, sometimes in 10- or 15-day increments after the first period.")
    d.calc([("A", "Invoice amount", None, False), ("B", "Retainage withheld (usually excluded)", None, False), ("C", "Factorable amount  =  A − B", None, True), ("D", "Advance rate (%)", "Often 70–90%", False), ("E", "Cash up front  =  C × D", None, True), ("F", "Fee for first 30 days (%)", None, False), ("G", "Fee per extra increment (%) and increment (days)", None, False), ("H", "Days until the customer pays", None, False), ("I", "Total fee (%)  =  F + G × extra increments", None, True), ("J", "Total fee ($)  =  C × I", None, True), ("K", "You receive in total  =  C − J", None, True)])
    d.callout("Example", "$60,000 invoice, 85% advance, 2.5% for 30 days + 1% per 10 days: $51,000 up front; fee $1,500 at 30 days, $3,300 at 60, $5,100 at 90.")

    d.section("Due diligence questions", "Step 3 of 4")
    d.check(["What's the advance rate, and is it calculated before or after retainage?", "How are fees calculated, and in what time increments?", "What other fees apply: setup, per-invoice, wire, monthly minimum, termination?", "Recourse or non-recourse, and what exactly does non-recourse cover? (Usually not disputes.)", "Do I have to factor all invoices, or can I choose (spot factoring)?", "How long is the contract, and how do I end it?", "How do you handle lien waivers, joint checks and pay applications?", "How quickly do you fund after verification?", "How do you notify my GC (notice of assignment)?"])
    d.table(["Factor", "Advance %", "30-day fee", "Other fees", "Recourse?", "Contract term"], ["Factor 1", "Factor 2", "Factor 3"])

    d.section("Compare with the alternatives", "Step 4 of 4")
    d.table(["Option", "Cost for this job", "Speed", "Depends on", "Notes"], ["Factoring", "Line of credit", "Working capital loan", "Supplier terms / mobilization payment"])
    d.callout("Rule of thumb", "Recurring short gaps: a line of credit is usually cheapest if you qualify. Occasional large invoices: factoring scales with billing. Never factor to cover a business that isn't profitable.")
    d.multi("Decision and notes", 70)
    d.cta(*CTA_BL)

RESOURCES.append(dict(
    slug="construction-factoring-calculator-checklist", blog="/blog/how-construction-invoice-factoring-works/", pages=5,
    spec=dict(title="Construction Factoring Cost Calculator & Due Diligence Checklist", tag="Factoring calculator", kicker="Free worksheet · for subcontractors",
              title_lines=["Factoring Cost Calculator", "& Due Diligence Checklist"],
              subtitle="Work out what factoring really costs on one of your invoices, ask the nine questions that expose hidden fees, and compare it with a line of credit or loan.",
              inside=["Fit test", "Cost calculator (A to K)", "Nine due-diligence questions", "Factor comparison table", "Alternatives comparison", "Decision page"], body=body_factoring),
    headline="What factoring <em>really costs</em> on your invoice",
    pitch="A free fillable calculator and checklist: run one real invoice through the fee schedule, ask the nine questions that expose hidden fees, and compare with a line of credit.",
    bullets=["Fit test for your business", "A-to-K cost calculator", "Nine due-diligence questions", "Factor and alternatives comparison tables"],
))

# ------------------------------------------------------------- 5. Dump truck purchase & financing checklist
def body_dump(d):
    d.section("Start with the work", "Step 1 of 5")
    d.calc([("A", "Billable hours or loads per week (realistic)", None, False), ("B", "Rate per hour or load", None, False), ("C", "Monthly revenue  =  A × B × 4.3", None, True), ("D", "Weeks per year the truck will actually work", None, False)])
    d.tick_grid(["Hauling for my own jobs", "Subcontract hauling by the hour", "Owner-operator with own customers", "Mix"])
    d.multi("Work lined up (contracts, LOIs, regular customers)", 44)

    d.section("New vs used: the truck", "Step 2 of 5")
    d.table(["Line", "Truck 1", "Truck 2", "Truck 3"], ["Year / make / model", "New or used", "Mileage or engine hours", "Body type and capacity", "Price", "Warranty remaining", "Maintenance records? (Y/N)", "Emissions equipment condition", "Title clean, no liens? (Y/N)", "Pre-purchase inspection done? (Y/N)"])
    d.h2("Used-truck inspection")
    d.tick_grid(["Engine and transmission", "DPF / EGR emissions system", "Frame and suspension", "Brakes and tires", "Hydraulics and hoist", "Body, tailgate, cab", "ECM / engine report pulled", "Accident history checked"])

    d.section("Financing comparison", "Step 3 of 5")
    d.table(["Lender", "Down payment", "APR", "Term", "Monthly", "Total interest", "Age / mileage cap"], ["Lender 1", "Lender 2", "Lender 3", "Dealer / captive"], colw=[90, 70, 55, 55, 70, 80, 84])
    d.callout("Example", "A $185,000 new tri-axle with 10% down at 9.99% over 60 months is about $3,537/month. A $110,000 used truck with 15% down at 11.99% over 60 months is about $2,079. A $62,000 older truck with 20% down at 15.99% over 48 months is about $1,406, and shorter terms on older trucks keep the payment higher than the price suggests.")

    d.section("True monthly cost", "Step 4 of 5")
    d.calc([("E", "Loan payment", None, False), ("F", "Commercial insurance (monthly)", None, False), ("G", "Fuel", None, False), ("H", "Tires, brakes, maintenance reserve", None, False), ("I", "Registration, permits, heavy vehicle use tax", None, False), ("J", "Driver wages (if not you)", None, False), ("K", "Parking / yard", None, False), ("L", "Total monthly cost  =  E + F + G + H + I + J + K", None, True), ("M", "Cost per hour or load  =  L ÷ (A × 4.3)", "Compare with B", True)])

    d.section("Application checklist", "Step 5 of 5")
    d.tick_grid(["Business registration / EIN", "Business bank statements (3–6 months)", "Personal ID and credit check consent", "CDL and driving record", "Insurance quote", "Truck details, VIN, invoice or bill of sale", "Contracts or LOIs", "Down payment proof"])
    d.check(["Separated business and personal accounts", "Paid down card balances before applying", "Chose a common make with strong resale and full records", "Compared at least three lenders on total cost"])
    d.multi("Notes", 60)
    d.cta(*CTA_BL)

RESOURCES.append(dict(
    slug="dump-truck-purchase-financing-checklist", blog="/blog/used-vs-new-dump-truck-financing/", pages=6,
    spec=dict(title="Dump Truck Purchase & Financing Checklist", tag="Dump truck checklist", kicker="Free checklist · new or used dump trucks",
              title_lines=["Dump Truck Purchase", "& Financing Checklist"],
              subtitle="Size the work, compare trucks and lenders on the same lines, calculate the true monthly cost per load, and walk into the application with everything ready.",
              inside=["Revenue sizing", "Truck comparison and inspection", "Lender comparison table", "True monthly cost calculator", "Application document list", "Notes"], body=body_dump),
    headline="Know the <em>true cost per load</em> before you finance a dump truck",
    pitch="A free fillable checklist: size the work, compare new and used trucks, line up lenders and calculate what the truck really costs each month.",
    bullets=["Revenue sizing and work-lined-up record", "Truck comparison and used-truck inspection", "Lender comparison with age/mileage caps", "True monthly cost and cost-per-load calculator"],
))

# ------------------------------------------------------------- 6. Financing ROI calculator & 90-day tracker
def body_roi(d):
    d.section("Your numbers today", "Step 1 of 4")
    d.calc([("A", "Estimates per month", None, False), ("B", "Close rate (%)", None, False), ("C", "Average ticket ($)", None, False), ("D", "Monthly booked revenue  =  A × B × C", None, True)])
    d.p("Be honest about B. Count signed contracts, not verbal yeses.")

    d.section("What financing could change", "Step 2 of 4")
    d.p("Use conservative assumptions. Many contractors see close rate and ticket both rise when a monthly option is presented at every estimate.")
    d.calc([("E", "Close rate with financing (%)", "Try B + 5 points", False), ("F", "Average ticket with financing ($)", "Try C × 1.05", False), ("G", "Monthly revenue with financing  =  A × E × F", None, True), ("H", "Share of jobs financed (%)", "Often 25–40%", False), ("I", "Average dealer fee on financed jobs (%)", "0% on standard plans; 5–12% on promo", False), ("J", "Monthly dealer fees  =  G × H × I", None, True), ("K", "Net gain per month  =  G − D − J", None, True)])
    d.callout("Example", "40 estimates, 30% close, $15,000 ticket = $180,000/month. With 35% close and a 5% larger ticket: $220,500. Minus fees on the financed share, the gain is usually well above $30,000/month. Your numbers will differ, which is why you measure.")

    d.section("90-day tracker", "Step 3 of 4")
    d.p("Track the same five numbers before and after. Fill one row per month.")
    d.table(["Month", "Estimates", "Financing presented (%)", "Close rate (%)", "Avg ticket", "Jobs financed", "Dealer fees ($)", "Days to sign"], ["Baseline (before)", "Month 1", "Month 2", "Month 3"], colw=[88, 56, 72, 60, 60, 56, 62, 50])
    d.h2("Per-rep view")
    d.table(["Rep", "Estimates", "Presented financing (%)", "Close rate (%)", "Avg ticket"], ["", "", "", "", ""])

    d.section("Where the sale breaks, and the fix", "Step 4 of 4")
    d.cards([("'We need to think about it'", "Often means 'we can't pay that today'. Show the monthly figure next to the total at the first visit."), ("The downgrade", "Show upgrade options as a payment difference, not a lump sum."), ("The competitor with a payment", "Two quotes at $16,000; one says 'about $340 a month'. Be that one."), ("The silent no", "Follow up with a pre-qualification link that uses a soft pull.")])
    d.check(["Financing mentioned early as one of three ways to pay", "Total price and APR always shown next to the monthly figure", "Soft-pull pre-qualification offered", "Never promised approval or quoted a rate not in writing", "Decline path decided (second-look lender, co-applicant, smaller scope)"])
    d.multi("Notes", 50)
    d.cta(*CTA_FC)

RESOURCES.append(dict(
    slug="contractor-financing-roi-tracker", blog="/blog/why-contractors-lose-jobs-without-financing/", pages=5,
    spec=dict(title="Customer Financing ROI Calculator & 90-Day Tracker", tag="Financing ROI tracker", kicker="Free worksheet · for contractors",
              title_lines=["Customer Financing", "ROI Calculator & Tracker"],
              subtitle="Put a number on the jobs you're losing to the payment question, model what a financing program changes, and track five numbers for 90 days to prove it.",
              inside=["Your numbers today", "Financing uplift model", "Dealer-fee cost line", "90-day tracker", "Per-rep view", "Kitchen-table fixes"], body=body_roi),
    headline="How many jobs are you losing to the <em>payment question</em>?",
    pitch="A free fillable calculator and 90-day tracker: model what offering financing does to your close rate and ticket size, net of dealer fees, then prove it with five numbers.",
    bullets=["Today's revenue baseline", "Uplift model net of dealer fees", "90-day and per-rep trackers", "Fixes for the four ways a sale slips"],
))

# ------------------------------------------------------------- 7. Buy vs lease decision worksheet
def body_lease(d):
    d.section("The machine and the work", "Step 1 of 4")
    d.fields([("Equipment (make / model / new or used)", None), ("Price", None), ("Hours per year it will work", "Under ~300: consider renting; 1,200+: usually own"), ("Years you'll keep it", None), ("Expected resale value at the end", "Dealer or auction comps")])
    d.tick_grid(["Heavy use, will modify or add attachments", "Need regular upgrades / emissions rules", "Cash is tight this year", "Project-based need (fixed term)", "Want to own it at the end", "Want predictable bundled maintenance"])

    d.section("Three structures, side by side", "Step 2 of 4")
    d.p("Get a quote for each structure and fill in the same lines. The decision turns on total cost minus what you own at the end.")
    d.table(["Line", "Equipment loan", "$1 buyout lease", "FMV lease"], ["Lender / lessor", "Upfront (down payment / first & last)", "Rate or money factor", "Term (months)", "Monthly payment", "Total of payments", "End-of-term cost (buyout / return)", "Hour limits / excess-use charges", "Who pays maintenance and insurance", "Early payoff / termination terms", "Value you own at the end"])
    d.calc([("A", "Loan: total paid − resale value you keep", None, True), ("B", "$1 buyout: total paid + $1 − resale value you keep", None, True), ("C", "FMV lease: total paid (+ buyout if you keep it)", None, True)])
    d.callout("Example", "$150,000 excavator over 60 months: loan with 10% down about $2,868/month ($187,100 total, you own it); $1 buyout lease about $3,298/month ($197,900 total, you own it); FMV lease about $2,469/month ($148,100 total, own nothing; buying it out at a $52,000 residual takes it to about $200,100).")

    d.section("Cost per operating hour", "Step 3 of 4")
    d.calc([("D", "Annual payments", None, False), ("E", "Annual insurance, maintenance, storage, transport", None, False), ("F", "Annual resale value credit (resale ÷ years kept)", "Owning only", False), ("G", "Annual cost  =  D + E − F", None, True), ("H", "Hours per year", None, False), ("I", "Cost per hour  =  G ÷ H", "Compare with your rental rate per hour", True)])
    d.h2("Tax questions for your CPA")
    d.check(["Does Section 179 or bonus depreciation apply this year, and at what limits?", "Operating lease payments vs depreciation: which suits our tax position?", "Any state differences?"])

    d.section("Decision", "Step 4 of 4")
    d.check(["Compared total cost minus what we own at the end, not just payments", "Checked hour limits and return conditions on any lease", "Noted the end-of-term notice window (many leases auto-renew)", "Confirmed the work exists before financing the machine", "Photographed the machine at delivery and kept maintenance records"])
    d.tick_grid(["Equipment loan", "$1 buyout lease", "FMV lease", "Rent for now"])
    d.multi("Why, and what would change it", 60)
    d.cta(*CTA_BL)

RESOURCES.append(dict(
    slug="equipment-buy-vs-lease-worksheet", blog="/blog/equipment-financing-vs-leasing/", pages=5,
    spec=dict(title="Equipment Buy vs Lease Decision Worksheet", tag="Buy vs lease worksheet", kicker="Free worksheet · construction equipment",
              title_lines=["Equipment Buy vs Lease", "Decision Worksheet"],
              subtitle="Compare a loan, a $1 buyout lease and an FMV lease on the same lines, work out cost per operating hour, and make the call with your CPA's questions answered.",
              inside=["Machine and usage profile", "Three structures side by side", "Total-cost-minus-ownership math", "Cost per operating hour", "CPA tax questions", "Decision checklist"], body=body_lease),
    headline="Buy or lease? <em>Decide on cost per hour</em>, not the payment",
    pitch="A free fillable worksheet that compares a loan, a $1 buyout lease and an FMV lease on the same lines and turns the result into cost per operating hour.",
    bullets=["Usage profile and ownership horizon", "Loan vs $1 buyout vs FMV comparison", "Cost per operating hour calculator", "CPA tax questions and decision checklist"],
))

# ------------------------------------------------------------- 10. Provider scorecard
def body_scorecard(d):
    d.section("How to score", "Step 1 of 3")
    d.p("Put each provider you're considering in a column and score 1 (poor) to 5 (excellent) on each row. Then weight the rows that matter most to your trade: a storm-market roofer weights speed and credit coverage; a remodeler weights promo plans and limits.")
    d.h2("The models")
    d.cards([("Marketplace / multi-lender", "Comparison and coverage; usually no single bank's promo rate."), ("Single-lender dealer program", "One credit decision, often promotional rates, narrower approvals."), ("Manufacturer program", "Promo rates tied to a brand's equipment through its bank partner."), ("Capital platform", "Working capital and customer financing combined.")])

    d.section("Scorecard", "Step 2 of 3")
    d.table(["Criterion (score 1–5)", "Provider 1", "Provider 2", "Provider 3", "Weight"], ["No-fee standard plan available", "Promotional plan dealer fees", "Approval rate for our typical customer", "Second-look / waterfall for declines", "Maximum loan size vs our tickets", "Terms available", "Funding speed and staged draws", "Soft-pull pre-qualification", "Mobile application and tools", "Trade-specific experience", "Training and support", "Contract: exclusivity, minimums, exit", "Homeowner experience (reviews of the lender)", "WEIGHTED TOTAL"], colw=[200, 70, 70, 70, 94])

    d.section("Fees and decline path", "Step 3 of 3")
    d.table(["Plan", "Provider 1 fee", "Provider 2 fee", "Provider 3 fee"], ["Standard rate", "0% 6 months", "0% 12 months", "0% 18 months", "Reduced rate 10 yr", "Reduced rate 15 yr"])
    d.check(["Ran two or three real customer profiles through each pre-qualification", "Got each fee schedule in writing", "Confirmed what happens when the first lender declines", "Checked exclusivity and termination terms", "Kept a second provider warm in case the first exits the market"])
    d.multi("Decision and notes", 60)
    d.cta(*CTA_FC)

RESOURCES.append(dict(
    slug="contractor-financing-provider-scorecard", blog="/blog/best-contractor-financing-companies/", pages=4,
    spec=dict(title="Contractor Financing Provider Scorecard", tag="Provider scorecard", kicker="Free scorecard · compare financing programs",
              title_lines=["Contractor Financing", "Provider Scorecard"],
              subtitle="Score up to three providers on the 13 criteria that decide whether a program pays for itself, plus a fee schedule and decline-path checklist.",
              inside=["Four provider models", "13-criterion weighted scorecard", "Fee schedule comparison", "Decline-path checklist", "Contract red flags", "Decision page"], body=body_scorecard),
    headline="Score financing providers on what <em>actually matters</em>",
    pitch="A free fillable scorecard: 13 weighted criteria, a plan-by-plan fee comparison and a decline-path checklist so you choose a program that pays for itself.",
    bullets=["13-criterion weighted scorecard for 3 providers", "Fee schedule by plan", "Decline-path and contract checks", "Four provider models explained"],
))

# ------------------------------------------------------------- 11. Construction bid worksheet
def body_bid(d):
    d.section("Direct costs", "Step 1 of 4")
    d.fields([("Job / customer", None), ("Scope summary", None)])
    d.calc([("A", "Materials from takeoff", None, False), ("B", "Waste allowance (%)", "Often 5–10%", False), ("C", "Materials incl. waste  =  A × (1 + B)", None, True), ("D", "Crew hours", None, False), ("E", "Average base wage", None, False), ("F", "Labor  =  D × E", None, True), ("G", "Labor burden (%)", "Payroll tax, workers' comp, insurance, PTO; often 25–40%", False), ("H", "Burdened labor  =  F × (1 + G)", None, True), ("I", "Equipment, dumpster, permits, subs", None, False), ("J", "DIRECT COST  =  C + H + I", None, True)])

    d.section("Overhead, cash-flow cost, contingency", "Step 2 of 4")
    d.calc([("K", "Overhead recovery (%)", "Annual overhead ÷ annual direct costs", False), ("L", "Overhead  =  J × K", None, True), ("M", "Days until you're paid", None, False), ("N", "Annual cost of capital (%)", "Line of credit or loan rate", False), ("O", "Cash-flow cost  =  J × N × M ÷ 365", None, True), ("P", "Contingency (%)", "Decking surprises, weather; often 3–6%", False), ("Q", "Contingency  =  J × P", None, True), ("R", "BREAK-EVEN  =  J + L + O + Q", None, True)])

    d.section("Margin and price", "Step 3 of 4")
    d.calc([("S", "Target gross margin on price (%)", "Many residential trades: 20–35%", False), ("T", "Price before financing fees  =  R ÷ (1 − S)", None, True), ("U", "Dealer fee if customer uses a promo plan (%)", "Only on jobs where it's offered", False), ("V", "Financed-price option  =  T × (1 + U)", None, True)])
    d.callout("Margin vs markup", "25% margin on price equals 33% markup on cost. Bidding 'cost plus 20%' on direct cost alone is often below break-even once overhead and the cost of waiting are counted.")
    d.h2("Bid-to-win checklist")
    d.check(["Scope itemized so the price isn't compared with a vaguer, cheaper bid", "Two or three options (standard / better / best) with a monthly payment on each", "Monthly payment shown next to the price", "Validity period set (e.g. 30 days) and a materials escalation clause for delayed starts", "Change-order pricing in the contract (per sheet / per hour)"])

    d.section("After the job: bid vs actual", "Step 4 of 4")
    d.table(["Line", "Bid", "Actual", "Variance"], ["Materials", "Crew hours", "Burdened labor", "Equipment / permits / subs", "Change-order revenue", "Days to payment", "Gross margin"])
    d.multi("What to change on the next bid", 60)
    d.cta(*CTA_FC)

RESOURCES.append(dict(
    slug="construction-bid-worksheet", blog="/blog/how-to-bid-construction-jobs/", pages=5,
    spec=dict(title="Construction Bid Worksheet", tag="Bid worksheet", kicker="Free worksheet · price jobs profitably",
              title_lines=["Construction", "Bid Worksheet"],
              subtitle="Build a bid from direct cost through labor burden, overhead, the cost of waiting to be paid, contingency and margin, then compare it with what actually happened.",
              inside=["Direct cost build-up (A to J)", "Overhead and cash-flow cost", "Contingency and break-even", "Margin vs markup pricing", "Bid-to-win checklist", "Bid vs actual review"], body=body_bid),
    headline="Build bids that are <em>above break-even</em>, every time",
    pitch="A free fillable worksheet that walks a bid from takeoff to price, including labor burden, overhead recovery, the cost of waiting to be paid and margin, then reviews bid vs actual.",
    bullets=["A-to-V bid build-up with formulas", "Cash-flow cost of slow payment", "Margin vs markup pricing", "Bid vs actual review table"],
))

# ------------------------------------------------------------- 12. Customer financing launch kit
def body_launch(d):
    d.section("Setup checklist", "Step 1 of 4")
    d.check(["Chose a program (standard no-fee plan plus optional promo plans); fee schedule in writing", "Every rep who quotes has a login and a mobile pre-qualification link", "Decided the decline path: second-look lender, co-applicant, smaller scope, independent option", "Pricing policy set: cash price vs financed price, consistent with lender rules and state law", "Funding schedule understood (completion-only vs staged draws)", "Monthly payment added next to the total price on the proposal template", "'Financing available' added to website, truck wraps, yard signs and estimates"])
    d.fields([("Program / lender partner", None), ("Standard plan APR / term", None), ("Promo plans offered and dealer fee", None), ("Go-live date", None)])

    d.section("Scripts", "Step 2 of 4")
    d.cards([("Opening the topic early", "'Most of our customers pay one of three ways: cash or check, insurance if it's storm damage, or monthly financing through a lender we work with. I'll show you all three.'"), ("Presenting the price", "'The full price is $12,400. If you'd rather spread it out, with our program that's about $230 a month over five years, and you can see whether you'd qualify without affecting your credit score. Want me to show you?'"), ("When they hesitate", "'Would it help to see the payment on the standard option versus the upgraded one? The difference is usually less than people expect.'"), ("Never say", "'Everyone gets approved.' 'Your rate will be X.' 'Sign the application first, we'll sort the contract after.'")])
    d.multi("Our version of the scripts (in our words)", 70)

    d.section("Rep training in an afternoon", "Step 3 of 4")
    d.check(["Role-played the three scripts, including the decline conversation", "Every rep ran the pre-qualification on a test profile", "Agreed what reps can and can't say (no rate guesses, no approval promises, always show total price)", "One-page cheat sheet: plans, payments on five typical job sizes, who to call when an application stalls", "Weekly review of who presents financing on every estimate"])
    d.table(["Typical job size", "Standard plan monthly", "Promo plan monthly", "Term"], ["$5,000", "$10,000", "$15,000", "$25,000", "$40,000"])

    d.section("90-day numbers", "Step 4 of 4")
    d.table(["Month", "Estimates", "Presented (%)", "Close rate (%)", "Avg ticket", "Jobs financed", "Dealer fees ($)", "Days to sign"], ["Baseline", "Month 1", "Month 2", "Month 3"], colw=[70, 56, 66, 70, 66, 62, 64, 50])
    d.callout("Example", "40 estimates at 30% close and a $12,000 ticket is $144,000/month. At 35% and $12,600 it's $176,400. If the gain isn't clear within a quarter, the problem is usually presentation, not the program.")
    d.multi("Notes", 50)
    d.cta(*CTA_FC)

RESOURCES.append(dict(
    slug="customer-financing-launch-kit", blog="/blog/how-to-offer-financing-to-customers/", pages=5,
    spec=dict(title="Customer Financing Launch Kit", tag="Financing launch kit", kicker="Free kit · set up customer financing",
              title_lines=["Customer Financing", "Launch Kit"],
              subtitle="A setup checklist, three kitchen-table scripts, an afternoon training plan and a 90-day tracker so your financing program produces sales from week one.",
              inside=["Setup checklist", "Three scripts and the never-say list", "Rep training plan", "Payment cheat sheet", "90-day tracker", "Notes"], body=body_launch),
    headline="Launch customer financing that <em>reps actually present</em>",
    pitch="A free fillable kit: setup checklist, three scripts, an afternoon training plan, a payment cheat sheet and a 90-day tracker.",
    bullets=["Seven-point setup checklist", "Three kitchen-table scripts and a never-say list", "Rep training in an afternoon", "Payment cheat sheet and 90-day tracker"],
))
