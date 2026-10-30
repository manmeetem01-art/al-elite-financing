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
