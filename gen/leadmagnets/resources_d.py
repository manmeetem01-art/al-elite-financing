"""Batch E lead magnet: furnace emergency checklist (the platform comparison reuses the provider scorecard)."""
RESOURCES = []

def body_furnace(d):
    d.section("First hour: safety, then warmth", "Step 1 of 5")
    d.check(["Thermostat batteries and settings checked", "Breaker, fuse and furnace power switch checked", "Air filter checked (a clogged filter trips the limit switch)", "Gas valve open (gas units); if you smell gas, leave and call the utility from outside", "Carbon monoxide alarm has power", "Space heaters only in occupied rooms, never on extension cords", "Faucets dripping if pipes run through unheated spaces and it's below freezing", "Asked the HVAC company about a temporary heater for a day or two"])
    d.fields([("Date and time furnace failed", None), ("Furnace age (years) and model", None), ("Outdoor temperature / forecast", None), ("HVAC company and technician", None)])

    d.section("Repair or replace?", "Step 2 of 5")
    d.fields([("Diagnosis (in writing)", None), ("Failed part (ask to see it)", None), ("Repair quote ($)", None), ("Replacement quote ($)", None)])
    d.tick_grid(["Cracked heat exchanger (replace)", "Furnace over 15 years", "Repair near half of replacement cost", "Failed repeatedly in last two winters", "Under 12 years, single failed part (repair)", "Second opinion requested"])
    d.callout("Rule of thumb", "Repair a younger furnace with one failed part. Replace for a cracked heat exchanger at any age, or an old furnace needing a major repair.")

    d.section("Quote comparison", "Step 3 of 5")
    d.table(["Line", "Quote 1", "Quote 2", "Quote 3"], ["Company and licence #", "Furnace model and AFUE", "Sized from load calculation? (Y/N)", "Venting / gas line / electrical changes", "Thermostat and haul-away included?", "Permits included?", "Parts / labor warranty (years)", "Weekday vs after-hours price", "Cash price", "Financed price (if different)", "TOTAL"])
    d.callout("Ask", "What is the price if I pay cash or use my own lender? If I wait until a weekday, does the price change?")

    d.section("Financing comparison and bad-credit steps", "Step 4 of 5")
    d.calc([("A", "Chosen quote", None, False), ("B", "Utility rebate / assistance", None, False), ("C", "Down payment from savings", None, False), ("D", "Amount to finance  =  A − B − C", None, True)])
    d.table(["Offer", "APR incl. fees", "Term", "Monthly", "Total repaid", "Soft pull?"], ["Company standard plan", "Company promo plan", "Independent lender 1", "Independent lender 2"])
    d.h2("If your credit is on the lower side")
    d.check(["Reduced the amount (standard-efficiency, rebates, down payment)", "Checked options with a soft-pull pre-qualification first", "Co-applicant with stronger credit (if available)", "Income documents ready (pay stubs / bank statements)", "Asked about a second-look lender if declined", "Avoided 'no credit check' / 'guaranteed approval' offers (rent-to-own or very high cost)"])

    d.section("Questions and decision", "Step 5 of 5")
    d.check(["What is the APR including fees, and is the rate fixed?", "Is there an origination fee, and is it deducted from the loan?", "Is any promotional period deferred interest or waived interest?", "Is there a prepayment penalty?", "When is the company paid, and when does my first payment start?", "Who registers the warranty?"])
    d.tick_grid(["Repair now", "Replace: standard efficiency", "Replace: high efficiency", "Replace with heat pump / dual fuel"])
    d.multi("Decision, dates and notes", 70)
    d.cta("Ready to compare HVAC financing?", "alelitefinancing.com/hvac-financing/bad-credit-hvac-financing/ reaches lenders who fund furnaces and HVAC work in your state, soft-inquiry options first. Or call (888) 968-0079.")

RESOURCES.append(dict(
    slug="furnace-emergency-checklist", blog="/blog/emergency-furnace-replacement/", pages=6,
    spec=dict(title="Furnace Emergency Checklist & Financing Planner", tag="Furnace emergency checklist", kicker="Free checklist · when the furnace fails in winter",
              title_lines=["Furnace Emergency", "Checklist & Planner"],
              subtitle="Stay safe and warm tonight, decide repair or replace, compare quotes on the same lines and finance the furnace without overpaying, including steps for lower credit.",
              inside=["First-hour safety checklist", "Repair-or-replace test", "Quote comparison table", "Amount-to-finance calculator", "Bad-credit approval steps", "Lender questions and decision"], body=body_furnace),
    headline="Keep the house warm tonight and <em>finance the furnace</em> without overpaying",
    pitch="A free fillable checklist for a furnace failure: safety steps, repair-or-replace test, quote comparison, bad-credit approval steps and a financing comparison table.",
    bullets=["First-hour safety and warmth checklist", "Repair-or-replace test", "Quote comparison on 11 lines", "Bad-credit approval steps and offers to avoid"],
))


def body_heatpump(d):
    d.section("Installed in 2025? Claim the credit now", "Step 1 of 5")
    d.p("The federal 25C credit ended for property placed in service after December 31, 2025. If your heat pump, furnace or AC went in during 2025, claim it on your 2025 return.")
    d.check(["System placed in service on or before December 31, 2025 (installer's invoice shows the date)", "Equipment model numbers and manufacturer certification kept", "Form 5695, Part II completed with the 2025 return", "Amount: 30% of eligible cost, up to $2,000 (heat pump) or $600 (furnace / AC), within the $3,200 annual cap"])
    d.fields([("Install date", None), ("Equipment and model numbers", None), ("Eligible cost ($)", None), ("Credit claimed ($)", None)])

    d.section("2026 rebate finder", "Step 2 of 5")
    d.p("For a 2026 installation there is no federal credit. Work through each source and write down what you qualify for; every dollar reduces the amount you finance.")
    d.table(["Program", "Amount", "Who files", "Status / notes"], ["Electric utility rebate", "Gas utility rebate", "State or city program", "HEAR rebate (income-eligible, where launched)", "HOMES rebate (where launched)", "Manufacturer promotion", "Utility on-bill financing", "TOTAL REBATES"])
    d.callout("Where to look", "Your utility's website (search 'rebates'), your state energy office for HEAR/HOMES status, and the contractor, who usually files instant rebates on the invoice.")

    d.section("Heat pump vs furnace: quote comparison", "Step 3 of 5")
    d.table(["Line", "Heat pump quote", "Furnace (+AC) quote", "Dual-fuel quote"], ["Company and licence #", "Equipment model numbers", "Capacity at design temperature", "Efficiency (HSPF2 / SEER2 / AFUE)", "Load calculation done? (Y/N)", "Electrical / ductwork changes", "Rebates applied on invoice", "Estimated annual energy cost", "Parts / labor warranty", "Cash price", "Financed price (if different)", "TOTAL"])

    d.section("Amount to finance and monthly payment", "Step 4 of 5")
    d.calc([("A", "Chosen quote", None, False), ("B", "Total rebates (Step 2)", None, False), ("C", "Down payment from savings", None, False), ("D", "Amount to finance  =  A − B − C", None, True), ("E", "Estimated monthly energy saving vs old system", "From the contractor's estimate", False)])
    d.table(["Term", "Monthly payment", "Total interest", "Net of energy saving (payment − E)"], ["36 months", "60 months", "84 months", "120 months"])
    d.callout("Rule of thumb", "Use the HVAC financing calculator at alelitefinancing.com/tools/hvac-financing-calculator/ with amount D and a lender's quoted APR. Match the term to a fraction of the system's 15–20 year life.")

    d.section("Financing comparison and decision", "Step 5 of 5")
    d.table(["Offer", "APR incl. fees", "Term", "Monthly", "Total repaid", "Soft pull?"], ["Contractor standard plan", "Contractor promo plan", "Utility on-bill financing", "Independent lender 1", "Independent lender 2"])
    d.check(["What is the APR including fees, and is the rate fixed?", "Is there an origination fee, and is it deducted from the loan?", "Is any promotional period deferred interest or waived interest?", "Is there a prepayment penalty?", "When is the contractor paid, and when does my first payment start?", "Does checking my options use a soft or hard credit inquiry?"])
    d.tick_grid(["Heat pump", "Furnace + AC", "Dual fuel", "Repair and wait"])
    d.multi("Decision, dates and notes", 56)
    d.cta("Ready to compare HVAC financing?", "alelitefinancing.com/hvac-financing/ reaches lenders who fund heat pumps, furnaces and AC in your state, soft-inquiry options first. Or call (888) 968-0079.")

RESOURCES.append(dict(
    slug="heat-pump-incentive-financing-checklist", blog="/blog/heat-pump-tax-credit-2026/", pages=6,
    spec=dict(title="2026 Heat Pump & HVAC Incentive and Financing Checklist", tag="Heat pump incentive checklist", kicker="Free checklist · after the federal credit ended",
              title_lines=["2026 Heat Pump & HVAC", "Incentive & Financing Checklist"],
              subtitle="Claim a 2025 install correctly, find every utility, state and HEAR/HOMES rebate you still qualify for in 2026, compare heat pump and furnace quotes, and finance only what's left.",
              inside=["2025 install credit claim steps", "2026 rebate finder", "Heat pump vs furnace quote comparison", "Amount-to-finance calculator", "Financing comparison table", "Lender questions and decision"], body=body_heatpump),
    headline="Find every 2026 rebate you still qualify for, then <em>finance only what's left</em>",
    pitch="A free fillable checklist: 2025-install credit claim steps, a rebate finder for utility, state and HEAR/HOMES programs, quote comparison, amount-to-finance calculator and lender questions.",
    bullets=["Still-eligible 2025 install: Form 5695 steps", "Rebate finder: utility, state, HEAR and HOMES", "Heat pump vs furnace quote comparison", "Amount-to-finance and monthly payment worksheet"],
))


def body_pipes(d):
    d.section("First hour: thaw or shut off", "Step 1 of 5")
    d.h2("If frozen (no water, no leak)")
    d.check(["Faucet opened (hot and cold)", "Frozen section located (exterior wall, crawlspace, garage, under sink)", "Warmed gently from the faucet end: hair dryer, heating pad, warm towels; no flame", "Cabinet doors opened; other cold faucets dripping", "Heat turned up and kept on", "Plumber called if the section is in a wall or can't be found"])
    d.h2("If burst (water where it shouldn't be)")
    d.check(["Main water valve shut off (location: ____________________)", "Water heater turned off", "Electricity off near water", "Faucets opened to drain lines", "Photos taken before moving anything", "Water removal and drying started; receipts kept", "Plumber called, then insurer notified"])

    d.section("Damage and claim log", "Step 2 of 5")
    d.fields([("Date and time discovered", None), ("Outdoor temperature / thermostat setting", "Insurers ask whether heat was maintained"), ("Location of the pipe", None), ("Cause stated by plumber", "Ask for it on the invoice"), ("Insurer and policy number", None), ("Claim number and date filed", None), ("Deductible ($)", None), ("Adjuster name and phone", None)])
    d.table(["Damaged item / area", "Photos taken? (Y/N)", "Estimated cost", "Covered? (per adjuster)"], ["", "", "", "", "", ""])
    d.callout("Keep", "Plumber's invoice with cause, remediation invoices, receipts for fans/dehumidifiers, photos of the pipe before repair and of every damaged area.")

    d.section("Plumber quote comparison", "Step 3 of 5")
    d.table(["Line", "Plumber 1", "Plumber 2", "Plumber 3"], ["Company and licence #", "Call-out / emergency fee", "Thaw or repair price", "Opening and closing walls", "Other sections to insulate / reroute", "Pipe material (copper, PEX, galvanized, PB)", "Repipe recommended? Price", "Permit and warranty", "Weekday vs after-hours price", "Cash price", "Financed price (if different)", "TOTAL"])

    d.section("What insurance pays, what you finance", "Step 4 of 5")
    d.calc([("A", "Plumber + remediation + repairs total", None, False), ("B", "Insurer's approved payment", "After the deductible", False), ("C", "Savings you'll put in", None, False), ("D", "Amount to finance  =  A − B − C", None, True)])
    d.table(["Offer", "APR incl. fees", "Term", "Monthly", "Total repaid", "Soft pull?"], ["Plumber's plan", "Independent lender 1", "Independent lender 2", "0% card (if clearable in time)"])
    d.callout("Rule of thumb", "Small amounts, short terms. A $3,000 repair over 24 months costs far less in interest than over 60.")

    d.section("Prevent the next one, and decide", "Step 5 of 5")
    d.check(["Exposed pipes insulated (foam sleeves / heat tape)", "Exterior hoses disconnected; spigots drained", "Thermostat minimum 55°F, low-temperature alert set", "Gaps near pipes sealed", "Leak sensor or smart shut-off installed", "Shut-off valve labelled and the household knows where it is"])
    d.h2("Questions for every lender")
    d.check(["What is the APR including fees, and is the rate fixed?", "Is there an origination fee, and is it deducted from the loan?", "Is any promotional period deferred interest or waived interest?", "Is there a prepayment penalty?", "Does checking my options use a soft or hard credit inquiry?"])
    d.multi("Decision, dates and notes", 60)
    d.cta("Ready to compare plumbing financing?", "alelitefinancing.com/plumbing-financing/ reaches lenders who fund plumbing repairs and repipes in your state, soft-inquiry options first. Or call (888) 968-0079.")

RESOURCES.append(dict(
    slug="frozen-pipe-emergency-checklist", blog="/blog/what-to-do-if-pipes-freeze/", pages=6,
    spec=dict(title="Frozen Pipe Emergency, Claim & Repair Checklist", tag="Frozen pipe checklist", kicker="Free checklist · frozen and burst pipes",
              title_lines=["Frozen Pipe Emergency,", "Claim & Repair Checklist"],
              subtitle="Thaw safely or shut off fast, log the damage for the insurer, compare plumber quotes on the same lines and finance only what insurance doesn't pay.",
              inside=["First-hour thaw and shut-off steps", "Damage and claim log", "Plumber quote comparison", "Insurance vs financing worksheet", "Prevention checklist", "Lender questions"], body=body_pipes),
    headline="Thaw it, stop the damage, and <em>get the claim and the repair right</em>",
    pitch="A free fillable checklist for frozen and burst pipes: the first-hour steps, shut-off and damage log, insurance claim record, plumber quote comparison and a financing worksheet for what insurance doesn't pay.",
    bullets=["First-hour thaw and shut-off checklist", "Damage photo and claim log", "Plumber quote comparison", "Amount-to-finance and lender questions"],
))


def body_icedam(d):
    d.section("First hour: safe steps", "Step 1 of 5")
    d.check(["Snow raked from the bottom 3 to 4 feet of the roof from the ground (roof rake, no ladder)", "Fan pointed at the underside of the roof in the attic; bath fans and lights venting into the attic closed off", "Calcium chloride tube (not rock salt) laid across the dam to melt a channel", "Buckets under drips; belongings moved; ceiling bulge drained into a bucket", "Photos taken of the ice, the roof edge, the ceilings and every damaged item", "Steam removal booked with a professional"])
    d.callout("Never do this", "Do not chip or pry ice with a hammer, pick or shovel. Do not use a torch, heat gun or boiling water. Do not climb an icy roof or ladder. Do not pour rock salt on shingles.")
    d.fields([("Date and time first noticed", None), ("Outdoor temperature / snowfall", None), ("Where water is entering inside", None), ("Roof age (years) and type", None)])

    d.section("Damage and claim log", "Step 2 of 5")
    d.fields([("Insurer and policy number", None), ("Deductible ($)", None), ("Claim number and date filed", None), ("Adjuster name and phone", None)])
    d.table(["Damaged item / area", "Photos taken? (Y/N)", "Estimated cost", "Covered? (per adjuster)"], ["Ceiling / drywall", "Insulation", "Flooring", "Belongings", "Gutters / fascia", "Roof / decking / flashing"])
    d.callout("Keep", "Receipts for steam removal, fans and drying; the contractor's written cause of damage; photos before cleanup. Ask the adjuster in writing what is covered and whether emergency measures are reimbursed.")

    d.section("Quote comparison", "Step 3 of 5")
    d.table(["Line", "Quote 1", "Quote 2", "Quote 3"], ["Company and licence #", "Ice removal price (per hour / minimum)", "Roof repair: shingles / flashing / valley", "Decking replacement (per sheet)", "Ice-and-water shield at eaves", "Attic air sealing", "Insulation R-value and price", "Soffit / ridge ventilation, baffles", "Rebates applied", "Warranty", "Cash price", "TOTAL"])

    d.section("Insurance vs financing", "Step 4 of 5")
    d.calc([("A", "Removal + repairs + insulation total", None, False), ("B", "Insurer's approved payment", "After the deductible", False), ("C", "Utility or state rebates", None, False), ("D", "Savings you'll put in", None, False), ("E", "Amount to finance  =  A − B − C − D", None, True)])
    d.table(["Offer", "APR incl. fees", "Term", "Monthly", "Total repaid", "Soft pull?"], ["Contractor plan", "Independent lender 1", "Independent lender 2", "Home equity (if re-roofing too)"])
    d.callout("Order of work", "Air seal first, then insulate, then ventilate. Insulating over unsealed gaps does not stop the heat leak that melts the snow.")

    d.section("Prevention and decision", "Step 5 of 5")
    d.check(["Attic floor air sealed (lights, hatch, chimney, plumbing)", "Insulation at the recommended level for the climate zone", "Soffit intake and ridge exhaust clear; baffles keep insulation off soffit vents", "Bath fans and dryer vented outdoors", "Gutters cleared in autumn", "Roof rake stored where it can be reached", "Heat cables considered only as a backup, not the fix"])
    d.h2("Questions for every lender")
    d.check(["What is the APR including fees, and is the rate fixed?", "Is there an origination fee, and is it deducted from the loan?", "Is any promotional period deferred interest or waived interest?", "Is there a prepayment penalty?", "Does checking my options use a soft or hard credit inquiry?"])
    d.multi("Decision, dates and notes", 56)
    d.cta("Ready to compare financing?", "alelitefinancing.com/roof-financing/roof-repair-financing/ reaches lenders who fund roof repairs, insulation and re-roofing in your state, soft-inquiry options first. Or call (888) 968-0079.")

RESOURCES.append(dict(
    slug="ice-dam-winter-leak-checklist", blog="/blog/ice-dams-removal-cost-insurance-prevention/", pages=6,
    spec=dict(title="Ice Dam & Winter Roof Leak Checklist and Claim Log", tag="Ice dam checklist", kicker="Free checklist · ice dams and winter roof leaks",
              title_lines=["Ice Dam & Winter Roof", "Leak Checklist and Claim Log"],
              subtitle="Remove an ice dam safely, log the damage for your insurer, compare removal, repair and insulation quotes on the same lines, and finance only what isn't covered.",
              inside=["Safe first-hour steps", "Damage and claim log", "Quote comparison table", "Insurance vs financing worksheet", "Prevention checklist", "Lender questions and decision"], body=body_icedam),
    headline="Remove it safely, log the damage for the claim, and <em>fix the cause once</em>",
    pitch="A free fillable checklist for ice dams and winter roof leaks: safe first steps, damage and claim log, removal and insulation quote comparison, what insurance pays versus what to finance, and a prevention list.",
    bullets=["Safe first-hour steps and what never to do", "Damage photo and claim log", "Removal, insulation and roof repair quote comparison", "Insurance vs financing worksheet"],
))
