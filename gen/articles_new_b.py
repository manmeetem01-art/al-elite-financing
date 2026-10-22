"""New blog posts, October 2026 batch B (contractor side). From the Content Calendar, months 2-4.
Same rules as batch A: distinct keyword from the money page, one primary money-page link and one
related post in the body, illustrative arithmetic only."""
from common import *

HOME = ("Home", "/")
BLOG = ("Blog", "/blog/")
ACHR = "https://achrnews.com/articles/144272-more-than-25-of-surveyed-homeowners-plan-to-finance-home-improvement-projects-by-borrowing-from-contractor"
DATE = "2026-10-20"

def pm(P, apr, n):
    return money(payment(P, apr, n), False)

def ti(P, apr, n):
    return money(payment(P, apr, n) * n - P, False)


# --------------------------------------------------------------------------- 5
FACTORING = dict(
    path="/blog/how-construction-invoice-factoring-works/", date=DATE,
    crumbs=[HOME, BLOG, ("How construction factoring works", "/blog/how-construction-invoice-factoring-works/")],
    eyebrow="Contractor guide", h1="Construction invoice factoring: how it works and what it really costs",
    title="How Construction Invoice Factoring Works (and What It Costs)",
    meta="How construction factoring works step by step: advance rates, fees, recourse, retainage and lien waivers, a worked cost example, and when a loan is cheaper.",
    answer="Construction invoice factoring turns an unpaid progress invoice into cash within days. A factoring company buys the invoice, advances most of its value up front (often in the 70% to 90% range), collects from the general contractor or owner, then pays you the rest minus its fee. Fees are commonly quoted per 30 days the invoice is outstanding, so slow payers make factoring expensive. It works best for subcontractors with creditworthy customers and long payment cycles.",
    money_page=("construction invoice factoring", "/contractor-business-loans/invoice-factoring/"), role="contractor", need="Invoice factoring",
    sections=[
        ("Why contractors run short of cash on profitable jobs", """<p>Construction is one of the few industries where you can win a profitable job and still run out of money doing it. You pay crews weekly and suppliers on 30-day terms, but your own invoices go through a pay application process, approval by the general contractor, the owner's draw schedule and often a "pay-when-paid" clause. Sixty to ninety days from work performed to money in the bank is common for subcontractors, and retainage of 5% to 10% can be held until the project closes out.</p>
<p>Factoring exists to close that gap. Instead of borrowing against your business, you sell specific invoices for cash now. Approval depends mostly on the creditworthiness of the customer who owes you, not only on your own credit, which is why it's often available to younger companies that can't yet get a bank line of credit.</p>"""),
        ("How factoring works, step by step", """<ol><li><strong>You do the work and invoice.</strong> For construction, that's usually an approved progress billing or pay application.</li>
<li><strong>You submit the invoice to the factor.</strong> Along with supporting documents: the subcontract, the approved pay app, sometimes lien waivers and proof the work was accepted.</li>
<li><strong>The factor verifies.</strong> They confirm with the GC or owner that the invoice is valid and approved, and check the payer's credit.</li>
<li><strong>You get the advance.</strong> Typically a large percentage of the invoice, often within a few business days of verification.</li>
<li><strong>The customer pays the factor.</strong> A notice of assignment tells your customer to pay the factoring company directly, usually to a lockbox.</li>
<li><strong>You get the reserve, minus fees.</strong> Once paid, the factor releases the remaining balance less its fee.</li></ol>"""),
        ("What it really costs: a worked example", f"""<p>Factoring fees are usually quoted as a percentage of the invoice per period, often per 30 days, sometimes in smaller increments after the first period. Here's an illustrative $60,000 progress invoice with an 85% advance and a fee of 2.5% for the first 30 days plus 1% for each additional 10 days.</p>
<div class='tbl'><table><thead><tr><th>Customer pays in</th><th class='num'>Fee</th><th class='num'>You receive in total</th><th class='num'>Fee as % of invoice</th></tr></thead><tbody>
<tr><td>30 days</td><td class='num'>$1,500</td><td class='num'>$58,500</td><td class='num'>2.5%</td></tr>
<tr><td>45 days</td><td class='num'>$2,700</td><td class='num'>$57,300</td><td class='num'>4.5%</td></tr>
<tr><td>60 days</td><td class='num'>$3,300</td><td class='num'>$56,700</td><td class='num'>5.5%</td></tr>
<tr><td>90 days</td><td class='num'>$5,100</td><td class='num'>$54,900</td><td class='num'>8.5%</td></tr>
</tbody></table></div>
<p class='cap'>Hypothetical fee schedule. 45 days rounds up to two 10-day increments after the first 30. Real schedules vary by factor, volume and customer risk.</p>
<p>You received about $51,000 up front in each case. If the GC pays in 60 days, you paid $3,300 to use roughly $51,000 for two months. Annualized, that's far more expensive than a bank line of credit. But if that $51,000 meets payroll and lets you start the next job instead of turning it down, the comparison isn't factoring versus a cheap loan. It's factoring versus the margin you'd lose.</p>
<p>Watch for fees beyond the headline rate: application or setup fees, per-invoice processing fees, wire fees, monthly minimums, and early termination fees if you leave the contract. Ask for the total cost on a sample invoice in writing.</p>"""),
        ("Recourse vs non-recourse", """<p>In <strong>recourse factoring</strong>, if your customer doesn't pay, you have to buy the invoice back or replace it. Fees are usually lower because you keep the credit risk. In <strong>non-recourse factoring</strong>, the factor takes on the risk of the customer's insolvency, though usually not disputes over the quality of your work. Fees are higher and the definition of what's covered matters. Read the non-recourse clause closely; in construction, most non-payment is about disputes, back-charges and change orders, which non-recourse often doesn't cover.</p>"""),
        ("Construction-specific issues that trip contractors up", """<ul><li><strong>Retainage.</strong> Most factors won't advance against retainage, because it isn't due until closeout and may be reduced by punch-list disputes. Expect the advance to be calculated on the invoice net of retainage.</li>
<li><strong>Pay-when-paid and pay-if-paid clauses.</strong> If your subcontract says you only get paid when the owner pays the GC, the factor will price that delay in, and some won't take the invoice at all.</li>
<li><strong>Lien waivers.</strong> Conditional and unconditional waivers have to line up with the factor's payment flow. Signing an unconditional waiver before money arrives can weaken your position.</li>
<li><strong>Bonded and public jobs.</strong> Government and bonded projects can be attractive because payers are creditworthy, but some public contracts restrict assignment of payments. Check before you sign.</li>
<li><strong>Change orders.</strong> Unapproved change orders usually can't be factored. Get them signed.</li>
<li><strong>Customer relationships.</strong> A notice of assignment tells your GC you're factoring. Most are used to it, but ask how your key customers view it.</li></ul>"""),
        ("Factoring vs a loan or line of credit", f"""<p>Factoring isn't the only way to bridge slow pay. Compare it with the alternatives:</p>
<ul><li><strong>Business line of credit.</strong> Usually cheaper per dollar and you draw only what you need, but harder to qualify for and often requires two or more years in business, solid financials and sometimes a personal guarantee.</li>
<li><strong>Working capital loan.</strong> A fixed amount repaid over months. Predictable, but you pay interest on the whole amount even if you only needed it for a few weeks. Our guide to <a href="/contractor-business-loans/working-capital/">working capital for contractors</a> compares the main types.</li>
<li><strong>Supplier terms.</strong> Negotiating 60-day terms with your main supplier can be cheaper than any financing.</li>
<li><strong>Mobilization payments.</strong> On larger jobs, ask for a deposit or mobilization payment to fund the first weeks.</li></ul>
<p>As a rough comparison, a $50,000 working capital loan at an illustrative 18% APR over 12 months costs about {ti(50000, 18, 12)} in interest. If you only need the money for 60 days on each of a few invoices, factoring can come out similar or cheaper, and it scales with your billing. If you need cash every month indefinitely, a line of credit is usually the better long-term tool.</p>"""),
        ("When factoring makes sense, and when it doesn't", """<p><strong>It tends to fit when:</strong> you're a subcontractor with creditworthy GCs who pay reliably but slowly; you're growing faster than your cash allows; you can't yet qualify for a bank line; and your margins can absorb a few percent of the invoice.</p>
<p><strong>Think twice when:</strong> your margins are thin; your customers routinely pay late or dispute invoices; most of your billing is retainage-heavy; or you'd be factoring every invoice forever to cover a business that isn't profitable. Factoring speeds up cash; it doesn't fix pricing. Our guide on <a href="/blog/how-to-bid-construction-jobs/">how to bid construction jobs</a> covers building financing costs into your numbers.</p>"""),
        ("Questions to ask a factoring company", """<ol><li>What's the advance rate, and is it calculated before or after retainage?</li>
<li>How are fees calculated, and in what time increments?</li>
<li>What other fees apply: setup, per-invoice, wire, monthly minimum, termination?</li>
<li>Is it recourse or non-recourse, and what exactly does non-recourse cover?</li>
<li>Do I have to factor all invoices, or can I choose (spot factoring)?</li>
<li>How long is the contract, and how do I end it?</li>
<li>How do you handle lien waivers, joint checks and pay applications?</li>
<li>How quickly do you fund after verification?</li></ol>"""),
    ],
    faqs=[
        ("How much does construction factoring cost?", "Fees are commonly quoted as a percentage of the invoice per 30 days or per shorter increment, so total cost depends on how long your customer takes to pay. Ask for the total fee on a sample invoice at 30, 60 and 90 days, plus any setup or per-invoice fees."),
        ("Can subcontractors factor invoices to general contractors?", "Yes. That's one of the most common uses. The factor will verify the invoice with the GC and look at the GC's payment history and credit."),
        ("Can I factor retainage?", "Usually not. Most factors exclude retainage because it isn't due until project closeout and can be reduced by disputes. Some specialist lenders offer separate retainage financing."),
        ("Does factoring show up as debt?", "Factoring is typically structured as a sale of receivables rather than a loan, so it may not appear as debt in the same way. How it's treated in your books and for tax purposes is a question for your accountant."),
        ("How fast can I get money from factoring?", "Once your account is set up and an invoice is verified, many factors fund within a few business days. Initial setup and verification of a new customer take longer."),
        ("What's the difference between spot factoring and a factoring contract?", "Spot factoring lets you sell individual invoices when you need cash, usually at a higher fee per invoice. A contract typically covers all or most of your invoices for a set term in exchange for lower rates, often with monthly minimums. If your cash crunch is seasonal, spot factoring can be the more flexible choice."),
        ("Will my general contractor know I'm factoring?", "Usually yes. The factor sends a notice of assignment asking the GC to pay it directly. This is common in construction, but it's worth mentioning to key customers."),
    ],
    related=[("Construction invoice factoring", "/contractor-business-loans/invoice-factoring/"), ("Working capital for contractors", "/contractor-business-loans/working-capital/"), ("How to bid construction jobs", "/blog/how-to-bid-construction-jobs/"), ("Construction line of credit", "/contractor-business-loans/line-of-credit/")],
)


# --------------------------------------------------------------------------- 6
def truck_table():
    rows = []
    for label, price, down, apr, n in (("New tri-axle (example)", 185000, 0.10, 9.99, 60), ("Used, 4 years old (example)", 110000, 0.15, 11.99, 60), ("Used, 9 years old (example)", 62000, 0.20, 15.99, 48)):
        P = price * (1 - down)
        rows.append(f"<tr><td>{label}</td><td class='num'>{money(price, False)}</td><td class='num'>{int(down*100)}%</td><td class='num'>{money(P, False)}</td><td>{apr:.2f}% / {n} mo</td><td class='num'>{pm(P, apr, n)}</td><td class='num'>{ti(P, apr, n)}</td></tr>")
    return "<div class='tbl'><table><thead><tr><th>Truck</th><th class='num'>Price</th><th class='num'>Down</th><th class='num'>Financed</th><th>Example APR / term</th><th class='num'>Monthly</th><th class='num'>Total interest</th></tr></thead><tbody>" + "".join(rows) + "</tbody></table></div><p class='cap'>Hypothetical prices and illustrative APRs, standard amortization, no fees or taxes. Not offers.</p>"

DUMP = dict(
    path="/blog/used-vs-new-dump-truck-financing/", date=DATE,
    crumbs=[HOME, BLOG, ("New vs used dump truck financing", "/blog/used-vs-new-dump-truck-financing/")],
    eyebrow="Contractor guide", h1="Dump truck financing: new vs used, rates and terms",
    title="Used vs New Dump Truck Financing: Rates, Terms, Down Payments",
    meta="New or used dump truck? How lenders treat age, mileage and down payment, example monthly payments, what owner-operators need to qualify, and inspection tips.",
    answer=f"Lenders finance both new and used dump trucks, but they price them differently. New trucks usually get longer terms and lower down payments; used trucks typically need more down, shorter terms and a higher rate, and many lenders set limits on age and mileage. As an illustration, $166,500 financed on a new truck at 9.99% over 60 months is about {pm(166500, 9.99, 60)} a month, while $93,500 on a used truck at 11.99% is about {pm(93500, 11.99, 60)}.",
    money_page=("dump truck financing", "/contractor-business-loans/dump-truck-financing/"), role="contractor", need="Dump truck or work truck financing",
    sections=[
        ("Start with the work, not the truck", """<p>Dump truck financing is equipment financing with a few twists of its own: the truck is titled like a vehicle, it may need a CDL to drive, it carries heavy commercial insurance, and its resale value depends heavily on age, mileage and how hard it has worked. Those details shape what lenders offer, and they're worth understanding before you start comparing trucks.</p>
<p>A dump truck is a revenue tool, so the first question is how much work it will do. Hauling for your own excavation or site work, subcontracting to another contractor by the hour, or running an owner-operator business with your own customers all lead to different trucks and different financing.</p>
<p>Before you shop, estimate how many billable hours or loads a week you can realistically keep it busy, at what rate, and what fuel, insurance, tires, maintenance, permits and a driver will cost. The truck payment needs to sit comfortably inside that margin. Lenders will ask the same questions, especially if you're new to trucking.</p>"""),
        ("New vs used: how lenders see each", """<p><strong>New trucks</strong> come with a known history, a manufacturer warranty and predictable resale value, so lenders are comfortable with longer terms and smaller down payments. Some manufacturers and dealers offer promotional financing on new units. The trade-off is price: a new tandem or tri-axle dump truck with body is a six-figure purchase, and depreciation in the first years is steep.</p>
<p><strong>Used trucks</strong> cost less and the steepest depreciation has already happened, which makes them popular with owner-operators and growing contractors. Lenders, though, carry more risk on an older asset. Expect them to look closely at model year, engine hours or mileage, maintenance records and the body and hoist condition. Many lenders cap the age of the truck at the end of the loan, so an older truck means a shorter term and a higher payment than the price alone suggests.</p>"""),
        ("Example payments: new vs used", f"""<p>Here's how price, down payment, rate and term combine for three hypothetical trucks.</p>{truck_table()}
<p>The used options cost far less in total, but notice how the shorter term on the older truck keeps its payment higher than you might expect. Factor in maintenance too: an older truck's lower payment can be eaten by repairs and downtime, and a truck that's in the shop isn't earning.</p>"""),
        ("What lenders look for", """<ul><li><strong>Time in business.</strong> Two or more years opens the most options. Startups and new owner-operators can still find financing, typically with a larger down payment or a co-signer.</li>
<li><strong>Personal and business credit.</strong> For small businesses, personal credit usually matters a lot, and many lenders ask for a personal guarantee.</li>
<li><strong>Revenue and bank statements.</strong> Several months of statements show the cash flow that will make the payments.</li>
<li><strong>CDL and driving record.</strong> If you'll be driving, lenders and insurers will look at your CDL and history. If you'll hire drivers, they may ask how you vet them.</li>
<li><strong>Contracts or work lined up.</strong> A letter of intent or steady customer can strengthen an application, especially for newer businesses.</li>
<li><strong>The truck itself.</strong> Year, make, model, VIN, mileage or hours, and an invoice or bill of sale. For private-party purchases, expect the lender to want an inspection and clean title.</li></ul>"""),
        ("Down payments and terms", """<p>Down payments are where new and used differ most. On new trucks, well-qualified buyers may see modest down payment requirements. On used trucks, 10% to 20% or more is common, and higher for older units, newer businesses or lower credit. Terms commonly run from about three to six years on equipment loans, shorter on older trucks.</p>
<p>A larger down payment does more than lower the monthly figure. It keeps you from owing more than the truck is worth if you need to sell it in a slow season. Trucks depreciate, and being "upside down" on a loan limits your options.</p>"""),
        ("Loan, lease or TRAC lease?", """<p>Most dump trucks are bought with an equipment loan: you own the truck, the lender holds a lien and you can usually deduct depreciation, subject to tax rules. Leasing is the alternative. A <strong>TRAC lease</strong> (terminal rental adjustment clause) is common for trucks: lower payments with a set residual value at the end, with you responsible for any difference between the residual and what the truck sells for. Fair-market-value leases let you hand the truck back. We compare these trade-offs in detail in <a href="/blog/equipment-financing-vs-leasing/">equipment financing vs leasing</a>.</p>"""),
        ("Buying used without buying a problem", """<ol><li><strong>Get a pre-purchase inspection</strong> from an independent heavy-truck mechanic: engine, transmission, emissions system, frame, suspension, brakes, hydraulics, body and tailgate.</li>
<li><strong>Pull the history.</strong> Maintenance records, any accident history and an ECM or engine report where available. Fleet trucks with full records are often a safer bet.</li>
<li><strong>Check emissions equipment.</strong> Repairs to DPF and EGR systems can be expensive. Make sure the truck meets the rules where you'll operate.</li>
<li><strong>Confirm the title is clean</strong> and no existing liens remain. Your lender will insist on this.</li>
<li><strong>Price the insurance first.</strong> Commercial truck insurance can change your monthly cost significantly. Get a quote before committing.</li></ol>"""),
        ("The true monthly cost of running a dump truck", f"""<p>The loan payment is often less than half of what a dump truck costs each month. Before you commit, put rough figures against each line:</p>
<ul><li><strong>Commercial auto insurance</strong>, which for heavy trucks can be a large monthly bill, especially for newer businesses or drivers with limited history.</li>
<li><strong>Fuel</strong>, the biggest variable cost, tied directly to hours and loads.</li>
<li><strong>Tires and brakes</strong>, which wear quickly under heavy loads and on rough job sites.</li>
<li><strong>Scheduled maintenance and repairs</strong>, including hydraulics, body and tailgate.</li>
<li><strong>Registration, permits and taxes</strong>, including heavy vehicle use tax for trucks above the federal weight threshold and any state or local hauling permits.</li>
<li><strong>Driver wages</strong> if you're not driving it yourself.</li>
<li><strong>Parking or yard space.</strong></li></ul>
<p>Add those to the payment and divide by the hours or loads you expect each month. That cost per hour is the number you compare against your hauling rate. If a $93,500 used-truck loan at an illustrative 11.99% runs about {pm(93500, 11.99, 60)} a month and operating costs add the same again, you need enough billable work to cover both, with room left for profit and slow weeks.</p>"""),
        ("How to strengthen your application", """<ol><li><strong>Separate business and personal finances.</strong> A business bank account with steady deposits is easier for lenders to underwrite than mixed personal accounts.</li>
<li><strong>Bring proof of work.</strong> Contracts, letters of intent or invoices from hauling you've already done.</li>
<li><strong>Save a bigger down payment.</strong> It lowers the lender's risk and your payment at the same time.</li>
<li><strong>Choose a truck the lender likes.</strong> Common makes and well-documented trucks with strong resale values are easier to finance than unusual or heavily modified units.</li>
<li><strong>Clean up your credit</strong> before applying: pay down card balances and dispute errors on your reports.</li>
<li><strong>Apply with complete documents</strong>: ID, CDL, bank statements, business registration, and the truck's details or invoice.</li></ol>"""),
        ("Keeping the truck profitable", """<p>Financing a truck is the easy part; keeping it earning is the business. Build a maintenance reserve into your rates from day one, track cost per hour or per load, and keep the truck busy in the slow months by lining up hauling for other contractors. If the truck will sit idle for long stretches, renting or subcontracting hauling may be cheaper than owning, at least until the work justifies it.</p>"""),
    ],
    faqs=[
        ("Can I finance a used dump truck with bad credit?", "Possibly, but expect a larger down payment, a higher rate and a shorter term. A co-signer, a strong down payment, steady bank deposits and work already lined up all help."),
        ("How old of a dump truck will lenders finance?", "It varies. Many lenders set a maximum age for the truck at the end of the loan, so older trucks get shorter terms. Some specialist lenders finance older equipment with stricter conditions."),
        ("Can a new owner-operator get dump truck financing?", "Yes, through lenders that work with startups. Expect more scrutiny of your personal credit, CDL, experience and planned work, and usually a larger down payment."),
        ("Is it better to buy a new or used dump truck?", "New trucks offer warranty coverage, reliability and easier financing at a higher price. Used trucks cost less and depreciate more slowly from here, but bring more maintenance risk. Run total cost of ownership, not just the payment."),
        ("How much down do I need for a dump truck?", "It depends on the truck, your credit and time in business. Used trucks commonly require 10% to 20% or more; new trucks can require less for well-qualified buyers."),
    ],
    related=[("Dump truck financing", "/contractor-business-loans/dump-truck-financing/"), ("Equipment financing vs leasing", "/blog/equipment-financing-vs-leasing/"), ("Equipment loan calculator", "/tools/equipment-loan-calculator/"), ("Construction equipment financing", "/contractor-business-loans/equipment-financing/")],
)


# --------------------------------------------------------------------------- 7
LOSEJOBS = dict(
    path="/blog/why-contractors-lose-jobs-without-financing/", date=DATE,
    crumbs=[HOME, BLOG, ("Why contractors lose jobs without financing", "/blog/why-contractors-lose-jobs-without-financing/")],
    eyebrow="Contractor guide", h1="Why contractors lose jobs without financing (and how to fix it)",
    title="Why Contractors Lose Jobs Without Financing (and How to Fix It)",
    meta="When homeowners say they need to think about it, they often mean they can't pay today. Why that loses jobs and how offering financing fixes it.",
    answer="Contractors lose jobs without financing because many homeowners can't or won't pay a five-figure quote from savings, so they delay, shrink the scope or choose the competitor who offered a monthly payment. Surveys show about 30% of homeowners plan to finance projects and over a quarter of those prefer to arrange it through their contractor. Offering financing at the quote, presented as a monthly option alongside the total, keeps those buyers in the room.",
    money_page=("contractor financing programs", "/for-contractors/"), role="contractor", need="Offer financing to my customers",
    sections=[
        ("The objection you're actually hearing", f"""<p>"We need to think about it." "We're getting a couple more quotes." "Let us talk it over." Every contractor hears these, and many write them off as price shopping. Often they mean something simpler: the household doesn't have $14,000 sitting in checking, and nobody has offered another way to pay.</p>
<p>The demand is real. A Modernize survey of more than 3,100 homeowners found about 30% planned to use financing or a loan for their project, and more than a quarter of those wanted to arrange it through their contractor (<a href="{ACHR}" rel="noopener">ACHR News</a>). If you don't offer it, a meaningful share of your leads are walking into the estimate already hoping you will.</p>"""),
        ("Five ways the job slips away", """<ol><li><strong>The delay.</strong> The homeowner decides to "save up." The leak gets worse, the AC limps along, and by the time they're ready, they call whoever is on the yard sign down the street.</li>
<li><strong>The downgrade.</strong> They can afford the repair but not the replacement, or the standard shingle but not the upgraded line, so your ticket shrinks.</li>
<li><strong>The competitor with a payment.</strong> Two quotes at $16,000. One says $16,000. The other says "$16,000, or about $340 a month." The second one feels affordable.</li>
<li><strong>The credit card.</strong> They put part of it on a card, run out of room, and the job stops at the deposit.</li>
<li><strong>The silent no.</strong> They never call back. You never learn that a monthly option would have closed it.</li></ol>"""),
        ("What financing changes at the kitchen table", f"""<p>A monthly payment reframes the decision. The question moves from "Do we have $16,000?" to "Can we fit about {pm(16000, 9.99, 60)} a month into our budget?" For most households, the second question is easier to say yes to, and it doesn't require draining the emergency fund.</p>
<p>It also changes which options get chosen. When a better system or roof is only a few dozen dollars more a month, homeowners are more willing to pick the option that's actually right for the house. On a $16,000 job versus a $19,000 upgraded version at an illustrative 9.99% over 60 months, the difference is about {money(payment(19000, 9.99, 60) - payment(16000, 9.99, 60), False)} a month. That's an easier conversation than "it's three thousand more."</p>
<p>And it shortens the sales cycle. A homeowner who can see a pre-qualified monthly option at the first visit has fewer reasons to wait.</p>"""),
        ("What it costs you, honestly", """<p>Customer financing isn't free for the contractor, and you should know the economics before you start.</p>
<ul><li><strong>Dealer fees on promotional plans.</strong> Low-rate or "same as cash" offers are often paid for by a fee charged to the contractor, a percentage of the loan. Standard-rate plans may carry little or no dealer fee. Know which plans cost you what.</li>
<li><strong>Pricing decisions.</strong> Some contractors build dealer fees into their prices; others absorb them on certain jobs. Be consistent, and never quote a higher price to financing customers than you'd disclose, since lending rules and lender agreements restrict how this works.</li>
<li><strong>Funding timing.</strong> Most programs pay you when the job is complete and the customer signs off, sometimes with a partial draw at the start for larger jobs. Understand the funding schedule so it fits your cash flow.</li>
<li><strong>Time to learn it.</strong> Your sales team needs to present financing well, which takes a little training.</li></ul>
<p>Compare that cost with your close rate. If financing turns even a few "we'll think about it" estimates a month into signed jobs, the math usually works.</p>"""),
        ("How to present financing without sounding like a salesman", """<p>The best financing conversations feel like a normal part of the quote, not a pitch.</p>
<ul><li><strong>Mention it early.</strong> "Most of our customers use one of three ways to pay: cash, insurance, or monthly financing. We'll go over all three." Now it's normal, not a sign of weakness.</li>
<li><strong>Show the total and the monthly side by side.</strong> Always show the full price and the APR alongside the monthly figure. Hiding the total damages trust and can run afoul of lending rules.</li>
<li><strong>Offer a soft-pull check.</strong> "We can see what you'd likely qualify for without affecting your credit." That's an easy yes.</li>
<li><strong>Don't push.</strong> If they want to pay cash or use their own bank, great. Financing is an option, not a requirement.</li>
<li><strong>Never promise approval.</strong> Approval belongs to the lender. Phrases like "everyone gets approved" create problems.</li></ul>
<p>Our guide to <a href="/blog/how-to-offer-financing-to-customers/">how to offer financing to your customers</a> includes sample scripts and a setup checklist.</p>"""),
        ("Choosing a financing program", """<p>Look beyond the headline rate when you compare programs:</p>
<ul><li><strong>Credit range.</strong> Does the program cover only prime borrowers, or does it include a second-look lender for customers who are declined first?</li>
<li><strong>Loan sizes and terms</strong> that match your jobs, from small repairs to full replacements.</li>
<li><strong>Dealer fees by plan</strong>, in writing.</li>
<li><strong>Funding speed</strong> and whether partial funding is available on larger jobs.</li>
<li><strong>Tools.</strong> A mobile application link, a quick soft-pull pre-qualification and clear disclosures your team can show customers.</li>
<li><strong>Trade fit.</strong> Lenders who understand roofing, HVAC or remodeling approve more of the right customers.</li></ul>
<p>AL Elite matches contractors with programs built for their trade and gives partners a profile page and a "Financing available through AL Elite" badge. See our <a href="/for-contractors/">contractor financing</a> page for how it works.</p>"""),
        ("Which trades feel it most", """<p>The bigger and more urgent the ticket, the more financing matters.</p>
<ul><li><strong>Roofing.</strong> Replacements run well into five figures and often follow storms that nobody budgeted for. Insurance covers some of it, but deductibles and uncovered items still need paying.</li>
<li><strong>HVAC.</strong> A system that fails in July or January has to be replaced now. Homeowners in that situation rarely have time to save, so the contractor who can offer a monthly option at the first visit often wins the job.</li>
<li><strong>Plumbing and sewer lines.</strong> Repipes and sewer replacements are surprise expenses with real urgency.</li>
<li><strong>Remodeling and solar.</strong> Planned projects with long sales cycles, where a clear monthly figure helps homeowners commit and choose the scope they actually want.</li></ul>
<p>If your trade has high tickets, urgency or both, you're likely losing more jobs to the payment question than you realize. The fix doesn't require changing your prices or your crews, only adding one more way for the customer to say yes before they leave the table.</p>"""),
        ("Measure whether it's working", """<p>You don't need special software to know whether financing pays off. Track a few numbers for 90 days after you start offering it: close rate on estimates where financing was presented versus not, average ticket size, the share of customers who used financing, time from estimate to signed contract, and dealer fees paid as a percentage of revenue. Those five figures will tell you within a quarter whether the program is paying for itself, and which crews present it best.</p>"""),
        ("A quick example", f"""<p>Picture a roofing company running 40 estimates a month at an average ticket of $15,000 and a 30% close rate: 12 jobs. Suppose financing nudges the close rate to 35% and lifts the average ticket by 5% as a few customers choose better materials. That's 14 jobs at $15,750: about {money(14 * 15750 - 12 * 15000, False)} more monthly revenue. Even after dealer fees on the financed share, the improvement is usually significant. Your numbers will differ, which is why measuring matters.</p>"""),
    ],
    faqs=[
        ("Do contractors pay to offer customer financing?", "Often, depending on the plan. Promotional low-rate plans usually carry a dealer fee paid by the contractor; standard-rate plans may cost little or nothing. Get each plan's fee in writing."),
        ("Does offering financing really increase sales?", "Many contractors report higher close rates and larger average tickets when financing is presented at every estimate, because it removes the upfront-cash barrier. Track your own close rate before and after to measure it."),
        ("When does the contractor get paid on a financed job?", "Usually when the work is complete and the customer confirms it, though some programs offer partial funding up front on larger jobs. Check the funding schedule before you sign up."),
        ("What if my customer gets declined?", "Some programs include second-look lenders who review declined applications. If not, the customer may still qualify elsewhere, use a co-applicant, or choose a smaller scope."),
        ("How long does it take to set up a customer financing program?", "Many programs can be set up within days to a few weeks, depending on the lender's review of your business, licensing and insurance. Plan time to train your sales team on presenting options and disclosures."),
        ("Is it legal to charge financing customers more?", "Rules vary and lender agreements often prohibit charging financed customers a different price than cash customers without proper disclosure. Speak with your lender partner and counsel about how to handle dealer fees in your pricing."),
    ],
    related=[("For contractors: offer customer financing", "/for-contractors/"), ("How to offer financing to your customers", "/blog/how-to-offer-financing-to-customers/"), ("Financing for roofing companies", "/for-contractors/roofing/"), ("HVAC financing for contractors", "/for-contractors/hvac/")],
)


# --------------------------------------------------------------------------- 8
def lease_compare():
    price = 150000
    loan_P = price * 0.9
    loan_pm = payment(loan_P, 9.99, 60)
    rows = [
        ("Equipment loan, 10% down", "$15,000", money(loan_pm, False), money(loan_pm * 60 + 15000, False), "You own it; resale value is yours"),
        ("$1 buyout lease (example)", "First + last payment", money(payment(price, 11.49, 60), False), money(payment(price, 11.49, 60) * 60 + 1, False), "Own it for $1 at end"),
        ("Fair market value lease (example)", "First payment", money(payment(price - 52000, 9.49, 60) + 52000 * 0.0949 / 12, False), money((payment(price - 52000, 9.49, 60) + 52000 * 0.0949 / 12) * 60, False), "Return, renew or buy at market value"),
    ]
    body = "".join(f"<tr><td>{a}</td><td>{b}</td><td class='num'>{c}</td><td class='num'>{d}</td><td>{e}</td></tr>" for a, b, c, d, e in rows)
    return f"<div class='tbl'><table><thead><tr><th>Structure</th><th>Upfront</th><th class='num'>Monthly (60 mo)</th><th class='num'>Total paid</th><th>At the end</th></tr></thead><tbody>{body}</tbody></table></div><p class='cap'>Hypothetical $150,000 excavator. Illustrative rates; FMV example assumes a $52,000 residual. Excludes taxes, fees, insurance and maintenance. Not offers.</p>"

LEASE = dict(
    path="/blog/equipment-financing-vs-leasing/", date=DATE,
    crumbs=[HOME, BLOG, ("Equipment financing vs leasing", "/blog/equipment-financing-vs-leasing/")],
    eyebrow="Contractor guide", h1="Construction equipment financing vs leasing: which costs less?",
    title="Construction Equipment Financing vs Leasing: Which Costs Less?",
    meta="Should you finance or lease an excavator, loader or lift? Ownership, cash flow, taxes, total cost, the lease types explained, and a side-by-side example.",
    answer="Financing usually costs less over the life of a machine you'll keep and use heavily, because you build equity and keep the resale value. Leasing usually wins on cash flow and flexibility: lower upfront cost, sometimes lower payments, and the option to return or upgrade. The right answer depends on how many hours you'll run the machine, how long you'll keep it, your cash position and your tax situation.",
    money_page=("construction equipment financing", "/contractor-business-loans/equipment-financing/"), role="contractor", need="Equipment financing",
    sections=[
        ("The core difference", """<p>With an <strong>equipment loan</strong>, you buy the machine and the lender holds a lien until it's paid off. You own it from day one, carry it on your balance sheet, and keep whatever it's worth at the end. With an <strong>equipment lease</strong>, a leasing company owns the machine and you pay to use it for a set term. What happens at the end depends on the lease type, and that's where most of the cost difference hides.</p>
<p>Neither is universally cheaper. The question is how the machine fits your business: how often it will work, how long it will stay useful to you, and how much cash you want to tie up.</p>"""),
        ("The lease types, explained", """<ul><li><strong>$1 buyout lease</strong> (also called a capital or finance lease). You make payments for the term and then buy the machine for a nominal amount. Economically it behaves a lot like a loan, often with a little less up front.</li>
<li><strong>Fair market value (FMV) lease.</strong> Lower payments because you're only paying for the machine's expected depreciation during the term. At the end you return it, renew, or buy it at market value.</li>
<li><strong>10% purchase option lease.</strong> A middle ground: you can buy the machine for a set percentage of its original price at the end.</li>
<li><strong>TRAC lease.</strong> Common for trucks and titled vehicles. A set residual value at the end, with you responsible for the difference if the vehicle sells for less, or keeping the surplus if it sells for more.</li>
<li><strong>Rental and rent-to-own.</strong> Short-term rental for occasional jobs; some dealers credit part of rental payments toward purchase.</li></ul>"""),
        ("A side-by-side example", f"""<p>Here's a hypothetical $150,000 excavator under three structures.</p>{lease_compare()}
<p>In this example the FMV lease has the lowest monthly payment and the lowest total paid, about $148,100, but you own nothing at the end. If the machine is still worth around $52,000 and you decide to keep it, buying it out takes the total to roughly $200,100, more than either alternative. The $1 buyout lease needs the least cash up front of the ownership options but costs the most of the two, about $197,900. The loan, at about $187,100 including the down payment, is the cheapest route to owning the machine outright.</p>
<p>The real comparison is total cost minus what you own at the end. That's why the decision turns on how long you'll keep the machine.</p>"""),
        ("When financing (buying) usually wins", """<ul><li><strong>You'll run it hard and keep it long.</strong> Excavators, loaders and skid steers that work most weeks for years are classic buy-and-hold assets. Their value after the loan is yours.</li>
<li><strong>Heavy use or modification.</strong> Leases may limit hours and require return in specific condition. If you put thousands of hours on a machine or add attachments and custom work, ownership avoids penalties.</li>
<li><strong>You have the down payment.</strong> Loans commonly require some money down, although some lenders finance up to 100% for strong borrowers.</li>
<li><strong>Tax depreciation matters to you.</strong> Owners can generally depreciate equipment, and Section 179 and bonus depreciation rules can let businesses deduct much or all of a qualifying purchase in the first year. Those rules changed in 2025, so confirm current limits with your CPA.</li></ul>"""),
        ("When leasing usually wins", """<ul><li><strong>Cash is tight or better spent elsewhere.</strong> Lower upfront cost keeps money free for payroll, materials and bonding capacity.</li>
<li><strong>Technology or emissions rules change quickly.</strong> If newer models bring real productivity gains, or you need to meet changing emissions requirements, regular upgrades through FMV leases can make sense.</li>
<li><strong>Project-based need.</strong> A machine needed for a two-year contract may be better leased for that term than bought and sold afterward.</li>
<li><strong>You want predictable costs.</strong> Some leases bundle maintenance, making monthly cost easier to forecast.</li>
<li><strong>Balance sheet considerations.</strong> Lease accounting rules now put most leases on the balance sheet, so this advantage is smaller than it used to be, but structures still affect ratios lenders and sureties look at. Ask your accountant.</li></ul>"""),
        ("Use hours to decide", f"""<p>A practical test is cost per operating hour. Divide your expected total cost of owning (payments plus maintenance, insurance and storage, minus expected resale value) by the hours you'll actually run the machine. Do the same for leasing, then for renting.</p>
<p>A machine you'll run 300 hours a year is often cheaper to rent when needed. One you'll run 1,200 or more hours a year usually justifies owning. Somewhere in between, leasing can be the best fit. Your own utilization numbers are the most important input here, more than the interest rate.</p>
<p>For a quick payment estimate on a loan, a $120,000 machine with 10% down at an illustrative 9.99% over 60 months is about {pm(108000, 9.99, 60)} a month. Our <a href="/tools/equipment-loan-calculator/">equipment loan calculator</a> lets you try your own numbers.</p>"""),
        ("What lenders and lessors look for", """<p>Both lenders and leasing companies typically review time in business, personal and business credit, recent bank statements and revenue, the equipment's age and value, and sometimes your backlog of work. Newer businesses can still qualify, especially for equipment with strong resale value, but should expect larger down payments or security deposits. Used equipment is widely financed and leased; older machines may get shorter terms.</p>
<p>When you compare offers, ask for: the total of all payments, any documentation or origination fees, the end-of-term terms in writing (buyout price or return conditions), hour limits and excess-use charges, who pays for maintenance and insurance, and any prepayment or early termination costs.</p>"""),
        ("Common mistakes to avoid", """<ul><li><strong>Comparing monthly payments only.</strong> A low lease payment can hide a large end-of-term cost. Always compare total cost minus what you'd own.</li>
<li><strong>Ignoring hour limits.</strong> Exceeding the hours in an FMV lease can bring per-hour charges that wipe out the savings.</li>
<li><strong>Missing the end-of-term notice window.</strong> Many leases require written notice months before the end if you want to return the equipment. Miss it and some leases renew automatically.</li>
<li><strong>Buying before the work is there.</strong> A financed machine sitting idle still has a payment. Make sure the backlog supports it.</li>
<li><strong>Overlooking return condition.</strong> Lessors can charge for damage beyond normal wear. Photograph the machine at delivery and keep maintenance records.</li>
<li><strong>Letting tax tail wag the dog.</strong> A year-end deduction is valuable, but buying equipment you don't need to save tax still costs you money.</li></ul>"""),
        ("A simple decision checklist", """<ol><li>How many hours a year will this machine work?</li>
<li>How long will it stay useful to my business?</li>
<li>How much cash can I put down without straining payroll and materials?</li>
<li>Do I want to own it at the end, or upgrade?</li>
<li>What does my CPA say about depreciation versus lease deductions this year?</li>
<li>What is the total cost of each option minus what I'd own at the end?</li></ol>
<p>If you're also weighing trucks, our guide to <a href="/blog/used-vs-new-dump-truck-financing/">new vs used dump truck financing</a> covers TRAC leases and age limits. When you're ready, our <a href="/contractor-business-loans/equipment-financing/">construction equipment financing</a> page explains how AL Elite matches you with lenders and lessors who fund your type of machine.</p>"""),
    ],
    faqs=[
        ("Is it cheaper to lease or finance construction equipment?", "Financing is usually cheaper over the long run if you keep and use the machine for years, because you own its remaining value. Leasing is often cheaper in the short term and better for cash flow or frequent upgrades."),
        ("Can I lease used construction equipment?", "Yes. Many lessors lease used equipment, though older machines may get shorter terms and higher rates."),
        ("Can I write off leased equipment?", "Lease payments on operating leases are generally deductible as a business expense, while owned equipment is depreciated, sometimes rapidly under Section 179 or bonus depreciation. Your CPA can tell you which works better for your situation."),
        ("What credit score do I need for equipment financing?", "Requirements vary. Strong personal and business credit opens the best terms, but equipment is collateral, so many lenders work with a broader range of profiles than for unsecured loans."),
        ("Can I pay off an equipment loan or lease early?", "Loans often allow early payoff, sometimes with a fee. Leases are usually harder to end early and may require paying most of the remaining payments. Ask about early payoff terms before signing."),
        ("What is a $1 buyout lease?", "A lease where you make payments for the term and then buy the equipment for $1. It works much like a loan, and is often treated like a purchase for tax and accounting purposes."),
    ],
    related=[("Construction equipment financing", "/contractor-business-loans/equipment-financing/"), ("Used vs new dump truck financing", "/blog/used-vs-new-dump-truck-financing/"), ("Equipment loan calculator", "/tools/equipment-loan-calculator/"), ("Contractor business loans", "/contractor-business-loans/")],
)

ARTICLES_B = [FACTORING, DUMP, LOSEJOBS, LEASE]
