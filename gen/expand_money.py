"""Length pass for thin money pages (Oct 2026 audit). Contractor hub was 472 words of real content,
contractor service pages 580-720, calculators ~600. Sections are keyed to each page's primary keyword."""
from common import money, payment

def pm(P, apr, n):
    return money(payment(P, apr, n), False)

def ti(P, apr, n):
    return money(payment(P, apr, n) * n - P, False)

SECTIONS = {}
FAQS = {}
PROSE = {}

# ---------------------------------------------------------------- hub (prose page)
PROSE["/contractor-business-loans/"] = f"""<h2 id='which-loan'>Which construction business loan fits which problem</h2>
<p>Construction business loans aren't one product. The right one depends on what the money is for and how long you need it.</p>
<div class='tbl'><table><thead><tr><th>The problem</th><th>The usual fit</th><th>Why</th></tr></thead><tbody>
<tr><td>Payroll due before the GC pays</td><td><a href="/contractor-business-loans/invoice-factoring/">Invoice factoring</a> or a <a href="/contractor-business-loans/line-of-credit/">line of credit</a></td><td>Short gap, repaid when the invoice clears</td></tr>
<tr><td>Materials deposit on a job you just won</td><td><a href="/contractor-business-loans/working-capital/">Working capital loan</a> or line of credit</td><td>Weeks to months, modest amount</td></tr>
<tr><td>Excavator, skid steer, lift</td><td><a href="/contractor-business-loans/equipment-financing/">Equipment financing</a> or a lease</td><td>The machine is the collateral; terms match its life</td></tr>
<tr><td>Dump truck or work truck</td><td><a href="/contractor-business-loans/dump-truck-financing/">Dump truck financing</a></td><td>Titled vehicle, often 3 to 6 year terms</td></tr>
<tr><td>Bonding capacity, growth, a second crew</td><td>Term loan or SBA-backed loan</td><td>Longer horizon, larger amount</td></tr>
<tr><td>Customers who can't pay the quote up front</td><td><a href="/for-contractors/">Customer financing program</a></td><td>The homeowner borrows, you get paid on completion</td></tr>
</tbody></table></div>
<h2 id='what-it-costs'>What construction business loans cost: a quick comparison</h2>
<p>Lenders quote costs in different units, which makes comparison hard. Three illustrative ways to borrow $50,000 for a year:</p>
<ul><li><strong>Term loan at 14% APR over 12 months:</strong> about {pm(50000, 14, 12)} a month, roughly {ti(50000, 14, 12)} in interest.</li>
<li><strong>Short-term loan quoted as a 1.25 factor rate:</strong> you repay $62,500, which is $12,500 in cost; because the balance drops as you pay, the equivalent APR is far higher than 25%.</li>
<li><strong>Line of credit at 16% APR, drawn for 90 days twice:</strong> about {money(50000 * 0.16 * 180 / 365, False)} in interest, because you only pay for the days you use.</li></ul>
<p>Always ask for the APR and the total dollars repaid. Our <a href="/contractor-business-loans/working-capital/">working capital</a> page explains factor rates in more detail.</p>
<h2 id='qualify'>What lenders look for from contractors</h2>
<p>Time in business (two years opens the most doors, but newer companies have options), personal and business credit, recent bank statements showing deposits that cover the payment, annual revenue, and for equipment the asset itself. Lenders also like to see contracts or a backlog, current licensing and insurance, and clean lien history. Separating business and personal accounts, keeping bookkeeping current and paying existing obligations on time before you apply all improve what you're offered.</p>
<p>One request through AL Elite goes to business lenders who work with contractors in your trade and state. We're a matching service: lenders set the terms and make the decision, and we show you each one's disclosures the same way. See <a href="/how-we-make-money/">how we're paid</a>.</p>"""

# ---------------------------------------------------------------- equipment financing (755)
SECTIONS["/contractor-business-loans/equipment-financing/"] = [
    ("What construction equipment financing covers", """<p>Lenders in this space finance most of what sits on a job site: excavators, backhoes, skid steers and compact track loaders, wheel loaders, dozers, mini excavators, telehandlers and boom lifts, compactors, concrete and paving equipment, trenchers, generators and light towers, attachments, and trailers to move it all. Titled vehicles like dump trucks are usually handled by vehicle lenders; see <a href="/contractor-business-loans/dump-truck-financing/">dump truck financing</a>. Soft costs such as delivery, installation and sometimes extended warranties can often be rolled into the loan, which keeps cash in the business.</p>"""),
    ("Rates, terms and down payments", f"""<p>Equipment loans typically run from two to seven years, with the term capped by the machine's expected useful life and age. Down payments range from zero for strong borrowers on new equipment to 10% to 20% or more on used machines, older units, or newer businesses. Rates depend on credit, time in business and the equipment: a well-qualified buyer on a new machine sits at one end; a start-up buying an older used excavator sits at the other.</p>
<p>As an illustration, $120,000 financed over 60 months costs about {pm(120000, 8.99, 60)} a month at 8.99% and about {pm(120000, 14.99, 60)} at 14.99%. The difference, roughly {money((payment(120000, 14.99, 60) - payment(120000, 8.99, 60)) * 60, False)} over the life of the loan, is why it pays to compare more than one lender and to clean up credit before applying.</p>"""),
    ("Section 179, bonus depreciation and timing", """<p>Owners can usually depreciate equipment, and federal rules allow much of a qualifying purchase to be deducted in the year it's placed in service through Section 179 expensing and bonus depreciation. Those rules were expanded in 2025, so ask your CPA for the current limits before year-end buying. The tax benefit is real but it's a timing benefit, not free money: a machine you don't need doesn't become a good purchase because of a deduction. IRS Publication 946 explains the rules and is linked in the sources below.</p>"""),
    ("Common mistakes with equipment loans", """<ul><li><strong>Financing a machine for longer than you'll keep it,</strong> which leaves you owing more than it's worth when you want to upgrade.</li>
<li><strong>Skipping the inspection on used equipment.</strong> Hours, undercarriage wear and hydraulics are where the money hides.</li>
<li><strong>Ignoring total cost.</strong> Insurance, transport, maintenance and downtime belong in the cost-per-hour calculation.</li>
<li><strong>Buying before the work exists.</strong> A financed machine sitting in the yard still has a payment.</li>
<li><strong>Not reading the end-of-term terms on leases.</strong> Residuals, hour limits and return conditions decide the real cost. Our guide to <a href="/blog/equipment-financing-vs-leasing/">equipment financing vs leasing</a> covers them.</li></ul>"""),
]
FAQS["/contractor-business-loans/equipment-financing/"] = [
    ("Can I finance used construction equipment?", "Yes. Most lenders finance used equipment, often with shorter terms and larger down payments on older machines. Expect an inspection and a clean title or bill of sale."),
    ("How long does equipment financing take?", "Simple applications on well-documented equipment can fund in a few business days. Larger amounts, private-party purchases and newer businesses take longer because of inspections and documentation."),
]

# ---------------------------------------------------------------- working capital (807)
SECTIONS["/contractor-business-loans/working-capital/"] = [
    ("Working capital for contractors: the main loan types", """<p>"Working capital" covers several products, and they behave very differently.</p>
<ul><li><strong>Short-term working capital loans.</strong> A fixed amount repaid over 3 to 24 months, often with daily or weekly payments. Fast and widely available, but check the APR, not the factor rate.</li>
<li><strong>Business lines of credit.</strong> A limit you draw on as needed and repay; interest only on what's outstanding. Best for recurring gaps. See <a href="/contractor-business-loans/line-of-credit/">construction line of credit</a>.</li>
<li><strong>Invoice factoring.</strong> Sell approved invoices for cash now; the factor collects from your customer. Good for subcontractors with slow-paying GCs. See <a href="/contractor-business-loans/invoice-factoring/">construction invoice factoring</a>.</li>
<li><strong>Merchant cash advances.</strong> An advance against future card or bank receipts, repaid as a percentage of deposits. Very fast and very expensive; use with care.</li>
<li><strong>SBA-backed loans.</strong> Longer terms and lower rates, slower to close and more paperwork; best for planned growth rather than next week's payroll.</li></ul>"""),
    ("A worked example: bridging a 60-day pay cycle", f"""<p>A subcontractor wins a $150,000 job paid in two progress payments at 30 and 60 days, with 10% retainage. Direct costs of about $95,000 fall in the first five weeks. Three ways to bridge the gap:</p>
<ul><li><strong>Line of credit at an illustrative 16% APR,</strong> drawing $60,000 for about 45 days: roughly {money(60000 * 0.16 * 45 / 365, False)} in interest.</li>
<li><strong>Factoring the first $75,000 invoice</strong> at an 85% advance and 2.5% for 30 days: about $1,875 in fees, and roughly $63,750 in the bank within days of the pay app being approved.</li>
<li><strong>A 6-month working capital loan of $60,000 at 20% APR:</strong> about {pm(60000, 20, 6)} a month and roughly {ti(60000, 20, 6)} in interest, with payments continuing after the job pays.</li></ul>
<p>The line of credit is cheapest if you qualify; factoring scales with billing and doesn't depend as much on your own credit; the term loan is the simplest to get but the least flexible. Most growing contractors end up with a line of credit for routine gaps and factoring or a term loan for larger jobs.</p>"""),
    ("Reducing the need for working capital in the first place", """<p>Borrowing is one lever; terms are another. Ask for mobilization or deposit payments on larger jobs, bill progress payments on time with complete pay applications so nothing is rejected for paperwork, negotiate 45- or 60-day terms with your main suppliers, and chase retainage releases at closeout. Pricing the cost of waiting into your bids also helps; see <a href="/blog/how-to-bid-construction-jobs/">how to bid construction jobs</a>. A contractor who tightens billing and terms often needs half the working capital they thought.</p>"""),
]
FAQS["/contractor-business-loans/working-capital/"] = [
    ("Can a new contractor get a working capital loan?", "Options exist for businesses under two years old, usually smaller amounts at higher cost, and often with a personal guarantee. Steady bank deposits, signed contracts and clean personal credit help."),
]

# ---------------------------------------------------------------- invoice factoring (647)
SECTIONS["/contractor-business-loans/invoice-factoring/"] = [
    ("Construction invoice factoring, step by step", """<ol><li>You complete the work and submit a progress billing or pay application that the GC or owner approves.</li>
<li>You submit the approved invoice and backup (subcontract, pay app, lien waivers as required) to the factor.</li>
<li>The factor verifies the invoice with the payer and checks the payer's credit.</li>
<li>You receive the advance, commonly 70% to 90% of the invoice net of retainage, often within a few business days.</li>
<li>Your customer pays the factor directly, usually after a notice of assignment.</li>
<li>The factor releases the remainder, minus its fee.</li></ol>"""),
    ("What construction factoring costs", f"""<p>Fees are usually quoted per period the invoice is outstanding. On a $60,000 invoice with an 85% advance and a schedule of 2.5% for the first 30 days plus 1% per additional 10 days, the fee is $1,500 at 30 days, $3,300 at 60 days and $5,100 at 90 days. Slow payers make factoring expensive, so it suits GCs who pay reliably if slowly. Ask about setup, per-invoice, wire, monthly-minimum and termination fees, and whether the agreement is recourse (you buy back unpaid invoices) or non-recourse (the factor takes the payer's insolvency risk, usually not disputes). Our guide on <a href="/blog/how-construction-invoice-factoring-works/">how construction invoice factoring works</a> has a full worked example and a question list.</p>"""),
    ("Construction-specific terms to check", """<ul><li><strong>Retainage</strong> is usually excluded from the advance.</li>
<li><strong>Pay-when-paid and pay-if-paid clauses</strong> in your subcontract affect whether the factor will take the invoice and at what price.</li>
<li><strong>Lien waivers</strong> must line up with the factor's payment flow; don't sign unconditional waivers before funds arrive.</li>
<li><strong>Public and bonded jobs</strong> may restrict assignment of payments.</li>
<li><strong>Spot factoring versus a contract:</strong> spot lets you choose invoices at a higher fee; contracts lower the fee but add minimums and a term.</li></ul>"""),
]
FAQS["/contractor-business-loans/invoice-factoring/"] = [
    ("How fast does construction factoring fund?", "Once your account is set up and an invoice is verified, many factors advance funds within two to three business days. The first invoice takes longer because of onboarding and payer verification."),
]

# ---------------------------------------------------------------- line of credit (639)
SECTIONS["/contractor-business-loans/line-of-credit/"] = [
    ("How a construction line of credit works", f"""<p>A lender sets a limit, say $100,000. You draw what you need when you need it, pay interest only on the outstanding balance, repay as jobs pay, and draw again. Rates are usually variable, quoted as a margin over a benchmark. Some lines carry an annual fee, draw fees or a requirement to pay the balance to zero for a period each year. Secured lines (backed by receivables, equipment or a blanket lien) cost less than unsecured ones; most require a personal guarantee.</p>
<p>The appeal is cost on short gaps. Drawing $40,000 for 30 days at an illustrative 15% APR costs about {money(40000 * 0.15 * 30 / 365, False)}. A 12-month term loan for the same amount would charge interest for the whole year whether you needed it or not.</p>"""),
    ("Qualifying for a construction line of credit", """<p>Banks and credit unions typically want two or more years in business, solid financial statements or tax returns, good personal and business credit, and often a deposit relationship. Online lenders are faster and more flexible on time in business, at higher rates and smaller limits. Either way, lenders look at receivables quality (who owes you and how fast they pay), existing debt, and whether your deposits comfortably cover the payments. Clean books and separated business accounts make a visible difference.</p>"""),
    ("Line of credit versus the alternatives", """<ul><li><strong>Versus a term loan:</strong> cheaper for recurring short gaps, more expensive if you keep a large balance for a year.</li>
<li><strong>Versus factoring:</strong> usually cheaper per dollar, but depends on your own credit rather than your customer's, and takes longer to set up. See <a href="/contractor-business-loans/invoice-factoring/">invoice factoring</a>.</li>
<li><strong>Versus a business credit card:</strong> larger limits and lower rates, but less convenient for small purchases. Many contractors use both.</li></ul>
<p>Our <a href="/contractor-business-loans/working-capital/">working capital</a> page compares all of these with a worked example.</p>"""),
]

# ---------------------------------------------------------------- dump truck (723)
SECTIONS["/contractor-business-loans/dump-truck-financing/"] = [
    ("What dump truck financing lenders look for", """<ul><li><strong>Time in business and revenue.</strong> Two or more years helps; start-ups and new owner-operators can still qualify with more down.</li>
<li><strong>Personal credit and a personal guarantee,</strong> which most small-business truck loans require.</li>
<li><strong>Bank statements</strong> showing deposits that cover the payment with room for fuel, insurance and maintenance.</li>
<li><strong>The truck:</strong> year, make, model, mileage or hours, VIN and condition. Many lenders cap the truck's age at the end of the term.</li>
<li><strong>CDL and driving record</strong> if you'll drive it, and proof of commercial insurance.</li>
<li><strong>Work lined up:</strong> contracts, letters of intent or steady customers strengthen an application.</li></ul>"""),
    ("Beyond the payment: the real cost of a dump truck", f"""<p>The loan is often less than half the monthly cost. Commercial truck insurance, fuel, tires and brakes, hydraulics and body maintenance, registration, permits and heavy vehicle use tax, and a driver's wages all sit on top. A used truck financed at about {pm(93500, 11.99, 60)} a month can easily cost the same again to run. Divide the total by the loads or hours you can realistically bill, and compare that with your hauling rate before you sign. Our guide to <a href="/blog/used-vs-new-dump-truck-financing/">new vs used dump truck financing</a> works through an example.</p>"""),
]

# ---------------------------------------------------------------- for-contractors trade pages
SECTIONS["/for-contractors/roofing/"] = [
    ("Financing for roofing companies: how the program works day to day", """<p>Once enrolled, your reps present a monthly option alongside the total price at the estimate. The homeowner checks eligibility with a soft pull on their phone or yours, chooses a plan, and completes the application with the lender. You schedule the job as normal. When the roof is complete and the homeowner signs off, the lender pays you, usually by ACH within a few business days. Some programs offer a partial draw at the start for larger jobs. Declines can be routed to a second-look lender automatically, so one "no" doesn't end the sale.</p>"""),
    ("Storm season: pairing insurance claims with financing", """<p>In hail and hurricane markets most roof sales involve an insurance claim, and the financing conversation is about the deductible and the items the adjuster didn't cover. Train reps to explain the claim timeline and the financing option in the same visit: the first insurance check, the depreciation held until completion, and a short loan for the gap. Never offer to waive or absorb a deductible; it's illegal in several states and a sign of a program that will be priced around the payout. Our homeowner guide to <a href="/blog/roof-financing-after-hail-damage/">roof financing after hail damage</a> is a useful script for reps.</p>"""),
]
SECTIONS["/for-contractors/hvac/"] = [
    ("HVAC financing for contractors: the emergency sale", """<p>Most HVAC replacements are decided in a day, when the system fails in the worst weather. The contractor who can show a monthly option on the first visit wins a large share of those jobs, because the homeowner can't wait to save up. Build the financing step into your service call: the technician diagnoses, the comfort advisor or tech presents two or three systems with the payment on each, and the homeowner checks eligibility on the spot. Manufacturer programs (Trane, Carrier, Lennox and others, through their bank partners) can be layered with a multi-lender program so that promotional rates are available on specific equipment and a broader program catches everyone else.</p>"""),
    ("Selling efficiency with a payment, not a price", """<p>The difference between a standard-efficiency system and a high-efficiency one is a few thousand dollars as a price and a few dozen dollars a month as a payment. Reps who show the monthly difference, alongside estimated energy savings and any utility rebates, sell more of the better equipment. Keep the comparison honest: show both totals, don't promise savings you can't document, and let the homeowner choose. Our contractor guide to <a href="/blog/why-contractors-lose-jobs-without-financing/">why contractors lose jobs without financing</a> covers the numbers behind this.</p>"""),
]
SECTIONS["/for-contractors/remodeling/"] = [
    ("Home improvement financing for contractors with long sales cycles", """<p>Remodeling is a planned purchase. Homeowners compare bids over weeks, which gives financing a different job than in roofing or HVAC: it moves the decision from "someday" to "this spring" and it supports bigger scopes. Present a monthly figure in the first proposal, show the upgrade options as payment differences, and offer a pre-qualification early so the homeowner knows their budget before they fall in love with a kitchen they can't fund. Larger limits matter here; check that your program covers your typical ticket.</p>"""),
    ("Progress payments and funding on larger jobs", """<p>A $60,000 kitchen can't be funded only at completion without straining your cash. Look for programs that fund in stages (a draw at start, at rough-in, at completion) or combine customer financing with your own <a href="/contractor-business-loans/line-of-credit/">line of credit</a> to cover materials deposits. Document each stage with photos and sign-offs, since lenders release funds against them.</p>"""),
]
SECTIONS["/for-contractors/solar/"] = [
    ("Solar financing for installers: loans, leases and PACE", """<p>Solar has more financing structures than any other trade: solar loans (the homeowner owns the system and any incentives), leases and power purchase agreements (a third party owns it and the homeowner pays for the power), and in some states PACE assessments repaid through property taxes. Each sells differently. Loans suit homeowners who want ownership and incentives; leases suit those who want no upfront cost and no maintenance; PACE is under new federal consumer-protection rules and has drawn regulator concern over property-tax increases, so present it carefully and never as the only option.</p>"""),
    ("What solar lenders check on the installer side", """<p>Solar lenders care about installer quality because they're financing a system that must perform for 20 years. Expect to show licensing, insurance, years in business, installation volume, warranty terms and sometimes customer reviews. Some lenders require specific equipment or certified installers. Keeping documentation current speeds onboarding and keeps approvals flowing.</p>"""),
]

# ---------------------------------------------------------------- calculators (prose pages)
PROSE["/tools/roof-financing-calculator/"] = f"""<h2 id='how-to-use'>How to use the roof financing calculator</h2>
<p>Enter the roof quote (or the gap after insurance, if a claim is paying most of it), the APR a lender has quoted or an estimate, and the term in months. The calculator shows the monthly payment, total interest and a full amortization schedule. Try two or three terms side by side: the payment falls quickly from 36 to 60 months and flattens after 120, while total interest keeps climbing.</p>
<h2 id='reading-results'>Reading the results</h2>
<ul><li><strong>Monthly payment</strong> is principal plus interest with standard amortization; it excludes any origination fee, insurance or taxes.</li>
<li><strong>Total interest</strong> is what the loan costs beyond the amount borrowed. Compare this across offers, not just the payment.</li>
<li><strong>The schedule</strong> shows how much of each early payment goes to interest. Paying extra early saves the most.</li></ul>
<h2 id='examples'>Example roof financing payments</h2>
<p>A $12,000 roof at an illustrative 9.99% APR is about {pm(12000, 9.99, 60)} a month over 60 months or {pm(12000, 9.99, 120)} over 120. A $25,000 roof at the same rate is about {pm(25000, 9.99, 84)} over 84 months. If your credit puts you at 17.99% instead, the $12,000 roof over 60 months is about {pm(12000, 17.99, 60)}. Our guide to <a href="/blog/how-much-does-a-new-roof-cost-per-month/">how much a new roof costs per month</a> has full tables, and the <a href="/roof-financing/">roof financing</a> page compares the loan types behind the numbers.</p>"""

PROSE["/tools/equipment-loan-calculator/"] = f"""<h2 id='how-to-use'>How to use the equipment loan calculator</h2>
<p>Enter the equipment price, the down payment (as an amount or percentage), the APR and the term. The calculator subtracts the down payment, then shows the monthly payment, total interest and an amortization schedule on the financed amount. Soft costs like delivery or attachments can be added to the price if you plan to finance them.</p>
<h2 id='reading-results'>What to compare</h2>
<ul><li><strong>Payment against revenue.</strong> Divide the payment by the hours or loads you can bill each month to see the cost per hour the machine must earn before fuel, insurance and maintenance.</li>
<li><strong>Term against useful life.</strong> A loan that outlasts the machine leaves you upside down when you want to upgrade.</li>
<li><strong>Down payment trade-off.</strong> More down lowers the payment and total interest but ties up cash the business may need for payroll.</li></ul>
<h2 id='examples'>Example equipment loan payments</h2>
<p>A $150,000 excavator with 10% down at an illustrative 9.99% APR over 60 months is about {pm(135000, 9.99, 60)} a month, with roughly {ti(135000, 9.99, 60)} in total interest. A $45,000 used skid steer with 15% down at 12.99% over 48 months is about {pm(38250, 12.99, 48)}. For leasing comparisons and tax questions, see <a href="/blog/equipment-financing-vs-leasing/">equipment financing vs leasing</a> and the <a href="/contractor-business-loans/equipment-financing/">construction equipment financing</a> page.</p>"""


def apply(pages_by_path):
    for path, secs in SECTIONS.items():
        p = pages_by_path.get(path)
        if p is not None:
            p["sections"] = list(p.get("sections", [])) + secs
    for path, faqs in FAQS.items():
        p = pages_by_path.get(path)
        if p is not None:
            p["faqs"] = list(p.get("faqs", [])) + faqs
    for path, html in PROSE.items():
        p = pages_by_path.get(path)
        if p is not None:
            p["prose"] = p.get("prose", "") + html
