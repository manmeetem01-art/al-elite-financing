"""Length + keyword pass for the seven original blog posts (Oct 2026 audit).
Each was 540-1,020 words of real content against a 1,500-word target. Sections below are added
before the FAQ; metas are rewritten to <=155 chars with the primary keyword; two H1s get their
primary keyword. Applied by build.py via apply()."""
from common import money, payment

def pm(P, apr, n):
    return money(payment(P, apr, n), False)

def ti(P, apr, n):
    return money(payment(P, apr, n) * n - P, False)

EXTRA = {}

# ---------------------------------------------------------------- heloc-vs-roof-loan (537 words)
EXTRA["/blog/heloc-vs-roof-loan/"] = dict(
    h1="Home equity loan for a new roof vs HELOC vs roof loan: which should pay?",
    title="Home Equity Loan for a New Roof vs HELOC vs Roof Loan (2026)",
    meta="Home equity loan for a new roof, HELOC or unsecured roof loan? Speed, cost, collateral risk and a worked $18,000 example to help you choose.",
    sections=[
        ("Can you deduct the interest?", """<p>Interest on a home equity loan or HELOC is generally deductible only when the money is used to buy, build or substantially improve the home that secures the loan, and only if you itemize. A roof replacement usually qualifies as a substantial improvement; a minor repair may not. Interest on an unsecured personal loan is not deductible for personal use. For most homeowners taking the standard deduction the difference is zero, so don't let the tax angle drive the decision. Keep the invoices either way, and ask a tax professional if the amounts are large.</p>"""),
        ("A worked example: the same $18,000 roof three ways", f"""<p>Numbers make the trade-offs concrete. Take an $18,000 asphalt replacement and three illustrative routes.</p>
<div class='tbl'><table><thead><tr><th>Route</th><th>Example rate</th><th>Term</th><th class='num'>Monthly</th><th class='num'>Total interest</th><th>Time to money</th></tr></thead><tbody>
<tr><td>Home equity loan for the new roof</td><td>8.25% fixed</td><td>10 yr</td><td class='num'>{pm(18000, 8.25, 120)}</td><td class='num'>{ti(18000, 8.25, 120)}</td><td>3 to 6 weeks</td></tr>
<tr><td>HELOC (draw $18,000)</td><td>8.75% variable</td><td>10 yr repay</td><td class='num'>{pm(18000, 8.75, 120)}</td><td class='num'>{ti(18000, 8.75, 120)} if the rate holds</td><td>2 to 6 weeks</td></tr>
<tr><td>Unsecured roof loan</td><td>11.99% fixed</td><td>7 yr</td><td class='num'>{pm(18000, 11.99, 84)}</td><td class='num'>{ti(18000, 11.99, 84)}</td><td>1 to 5 days</td></tr>
<tr><td>Unsecured roof loan, shorter</td><td>11.99% fixed</td><td>5 yr</td><td class='num'>{pm(18000, 11.99, 60)}</td><td class='num'>{ti(18000, 11.99, 60)}</td><td>1 to 5 days</td></tr>
</tbody></table></div><p class='cap'>Illustrative rates and standard amortization, no fees. Home equity products usually carry closing costs; some lenders waive them with conditions. Not offers.</p>
<p>Two things stand out. The home equity loan's lower rate is partly offset by its longer term: you pay for ten years and the total interest is not dramatically lower than a five-year unsecured loan. And the HELOC's number is only as good as its rate, which can change. If your roof is urgent, the unsecured loan's speed may be worth more than the rate difference; if the project is planned and large, equity products earn their paperwork.</p>"""),
        ("What a home equity loan for a new roof actually involves", """<p>Because the loan is secured by your home, the lender treats it like a small mortgage. Expect an application with income and asset documentation, a credit check, an appraisal or automated valuation to confirm your equity, a title check, and closing documents. Most lenders want you to keep a cushion of equity after the loan, commonly around 15% to 20% of the home's value, so a homeowner who bought recently with a small down payment may not qualify even with good credit.</p>
<p>Closing costs can include origination, appraisal, title and recording fees. Some lenders advertise no closing costs but recover them if you pay the loan off within a few years. Ask for the loan estimate and compare the APR, which includes those costs, not just the rate.</p>
<p>Timing matters too. The whole process commonly takes three to six weeks. That is fine for a roof you're planning for spring. It isn't fine for a roof that's leaking into the kitchen.</p>"""),
        ("HELOC details that catch people out", """<ul><li><strong>Draw period versus repayment period.</strong> Many HELOCs let you draw for 10 years with interest-only payments, then require full principal-and-interest payments for the next 10 to 20. The payment jump at that point surprises homeowners who only budgeted for the interest-only years.</li>
<li><strong>Variable rate.</strong> Most HELOCs float with a benchmark rate. Some let you lock a fixed rate on a portion of the balance, which is worth asking about for a one-time project like a roof.</li>
<li><strong>Annual fees and inactivity fees.</strong> Small, but they add up on a line you only used once.</li>
<li><strong>Lender can freeze or reduce the line</strong> if home values fall or your finances change. Rare, but it happened widely in 2008 and 2009.</li>
<li><strong>Convenience is a risk.</strong> A line you can draw on for years makes it easy to borrow for things that weren't the roof.</li></ul>"""),
        ("When the unsecured roof loan is the smarter choice", """<p>Unsecured loans get dismissed as the expensive option, and at the rate level that's often true. But they win in specific situations:</p>
<ul><li><strong>The roof can't wait.</strong> Days versus weeks is the whole story after a storm.</li>
<li><strong>You have little equity</strong> or bought within the last few years.</li>
<li><strong>You don't want a lien on the house.</strong> Missed payments on an unsecured loan hurt your credit; missed payments on a home equity product can, in the worst case, threaten the home.</li>
<li><strong>The amount is moderate.</strong> On a $9,000 repair the interest difference between products is small in dollars, and closing costs on an equity loan can wipe it out.</li>
<li><strong>Your mortgage rate is very low.</strong> Cash-out refinancing to pay for a roof would reset your whole mortgage at today's rate. A separate loan leaves the cheap mortgage alone.</li></ul>
<p>Our <a href="/roof-financing/">roof financing</a> page shows how unsecured and contractor-arranged options compare, and our guide to <a href="/blog/how-much-does-a-new-roof-cost-per-month/">what a new roof costs per month</a> has payment tables for other amounts and terms.</p>"""),
        ("Questions to ask before choosing", """<ol><li>How soon does the roof need to happen? If the answer is "this month," equity products are usually out.</li>
<li>How much equity do I have after the lender's cushion? Ask for an estimate before paying for an appraisal.</li>
<li>What is the APR including closing costs, not the headline rate?</li>
<li>Is there a prepayment penalty or an early-closure fee that claws back waived costs?</li>
<li>For a HELOC: when does the draw period end, and what will the payment be then?</li>
<li>Will I actually pay a 10-year loan off early? If not, compare total interest honestly.</li>
<li>Am I comfortable with the roof loan being secured by the house?</li></ol>"""),
    ],
    faqs=[
        ("Is a home equity loan a good way to pay for a new roof?", "It can be the cheapest option per dollar for a planned roof if you have enough equity, because rates are lower and terms longer. It takes weeks to close and puts a lien on the home, so it suits planned projects more than emergencies."),
        ("How much equity do I need for a roof loan secured by my home?", "Most lenders want you to keep roughly 15% to 20% equity after the new loan. On a $400,000 home with a $300,000 mortgage, that leaves limited room, so check with the lender before paying for an appraisal."),
    ],
)

# ---------------------------------------------------------------- roofing-companies-that-offer-financing (575)
EXTRA["/blog/roofing-companies-that-offer-financing/"] = dict(
    meta="How to find roofing companies that offer financing, what their plans really cost, the questions that expose a bad plan, and when to bring your own loan.",
    sections=[
        ("Questions to ask before you sign the roofer's plan", """<ol><li>Who is the lender, and is this a loan or a credit line?</li>
<li>What is the APR after any promotional period ends?</li>
<li>Is the promotional interest deferred or waived?</li>
<li>Is there a dealer fee, and would the price be lower if I paid cash or used my own lender?</li>
<li>When does the lender pay you, and when does my first payment start?</li>
<li>Is there a prepayment penalty?</li>
<li>Does the pre-qualification use a soft inquiry?</li>
<li>Can I see the loan documents before I sign the roofing contract?</li></ol>
<p>A roofer who answers these in writing is usually a roofer who runs the program well. One who deflects to "the finance company handles that" is telling you to read the documents very carefully.</p>"""),
        ("How roofer financing plans are structured", """<p>Most roofing companies that offer financing don't lend their own money. They enroll with one or more consumer lenders, and the lender pays the roofer when the job is done. Three plan types show up again and again.</p>
<ul><li><strong>Standard installment plans.</strong> A fixed APR, usually from the high single digits up, over three to twelve years. Often no dealer fee to the roofer, which means no reason for the roofer to inflate the price.</li>
<li><strong>Promotional plans.</strong> "0% for 18 months" or "no payments for 12 months." The lender charges the roofer a dealer fee for these, sometimes 5% to 15% of the job. That fee has to come from somewhere, which is why a cash price can be lower.</li>
<li><strong>Reduced-rate long-term plans.</strong> A below-market rate for 10 to 15 years with a dealer fee attached. Lower monthly figure, more total interest, and a price that may carry the fee.</li></ul>
<p>Knowing which type you're being offered tells you which questions to ask.</p>"""),
        ("Deferred interest versus waived interest", f"""<p>Promotional plans come in two flavors that look identical on the flyer. With <strong>waived interest</strong>, nothing accrues during the promotion; if you pay it off in time you paid zero. With <strong>deferred interest</strong>, interest accrues from day one at the plan's regular rate (often above 20%) and is charged in full if any balance remains at the end of the promotion.</p>
<p>On a $14,000 roof at an illustrative 24.99% deferred rate, a homeowner who still owes $500 on the last day of an 18-month promotion could be charged all the interest that accrued on the full balance over those 18 months, roughly {money(14000 * 0.2499 * 1.5 * 0.6, False)} or more depending on how the balance declined. The promotion only helps if you can clear the whole balance in time. Ask which one you're being offered, in writing.</p>"""),
        ("A quick cost comparison: roofer plan versus your own loan", f"""<p>Here is an illustrative $14,000 roof financed three ways, so you can see what the dealer fee does.</p>
<div class='tbl'><table><thead><tr><th>Route</th><th class='num'>Price</th><th>Terms</th><th class='num'>Monthly</th><th class='num'>Total paid</th></tr></thead><tbody>
<tr><td>Roofer's standard plan</td><td class='num'>$14,000</td><td>10.99%, 84 mo</td><td class='num'>{pm(14000, 10.99, 84)}</td><td class='num'>{money(payment(14000, 10.99, 84) * 84, False)}</td></tr>
<tr><td>Roofer's "0% for 18 mo", price includes 8% fee, paid in time</td><td class='num'>$15,120</td><td>0%, 18 mo</td><td class='num'>{money(15120 / 18, False)}</td><td class='num'>$15,120</td></tr>
<tr><td>Your own personal loan, cash price</td><td class='num'>$13,500</td><td>11.99%, 60 mo</td><td class='num'>{pm(13500, 11.99, 60)}</td><td class='num'>{money(payment(13500, 11.99, 60) * 60, False)}</td></tr>
</tbody></table></div><p class='cap'>Hypothetical. Assumes the roofer discounts 3.5% for cash and adds 8% for the promotional plan. Your quotes will differ.</p>
<p>The "0%" plan is the cheapest only if you can pay $840 a month for 18 months. If you can't, the standard plan or your own loan is better, and the cash-price discount matters more than most homeowners realize.</p>"""),
        ("What to do if the roofer's plan declines you", """<p>A decline at the kitchen table isn't the end. Ask whether the roofer's program has a second-look lender; many do, and the roofer may need to resubmit. If not, check options independently with a soft-pull pre-qualification, consider a co-applicant, or reduce the amount by choosing a standard-efficiency material or financing only the gap after insurance. Our guide to <a href="/roof-financing/bad-credit-roof-financing/">roof financing with bad credit</a> covers the realistic paths.</p>"""),
        ("Finding a roofer you can trust with the financing conversation", """<p>The financing plan is only as good as the company presenting it. Before you sign either agreement:</p>
<ul><li>Confirm the state license or registration, insurance certificates and a local address.</li>
<li>Read reviews that mention financing specifically. Complaints about surprise interest or price changes tell you how the company handles the plan.</li>
<li>Get the full price in writing before the financing is discussed, so you can see whether it changes.</li>
<li>Avoid contractors who push you to sign the loan application before the roof contract, or who ask you to sign a partly blank form.</li></ul>
<p>Many good roofers offer financing well; the point is to know what you're signing. If you'd rather compare lenders independently and then pay the roofer, start with our <a href="/roof-financing/">roof financing</a> page.</p>"""),
    ],
    faqs=[
        ("Is 0% roofing financing really free?", "Only if the interest is waived rather than deferred and you pay the full balance within the promotional period. The roofer usually pays the lender a dealer fee for these plans, which can be built into the price, so compare the financed price with the cash price before deciding."),
        ("Do roofing companies charge more if you finance?", "Some build the lender's dealer fee into the price, especially for promotional 0% plans, so the financed price can be higher than a cash price. Ask for both prices and compare the total cost."),
        ("Can I use my own loan to pay a roofer?", "Yes. An unsecured personal loan or home equity product pays the roofer like cash. Many roofers prefer it, and you may get a cash discount."),
    ],
)

# ---------------------------------------------------------------- best-contractor-financing-companies (597)
EXTRA["/blog/best-contractor-financing-companies/"] = dict(
    meta="The best contractor financing companies compared by model: marketplaces, dealer programs, manufacturer plans and capital platforms, and how to choose.",
    sections=[
        ("How the models look from the homeowner's side", """<p>Contractors sometimes forget that the customer is also comparing. From the homeowner's chair, a single-lender dealer program means one credit decision, one rate and no comparison; convenient, but they may wonder whether a better offer existed. A manufacturer program ties the deal to a brand of equipment, which is fine if they wanted that brand anyway. A marketplace gives them choices but can feel like one more thing to research during a stressful week. The provider that wins is often the one whose process the customer finds least stressful: a soft-pull check, a clear monthly figure, and no surprises in the documents. Ask each provider you evaluate to walk you through the homeowner's screens, not just yours, and read the customer reviews of the lender behind the program, not only the platform's own marketing.</p>
<p>Finally, remember that providers come and go, and so do their terms. Lenders exit home improvement lending when credit tightens, and platforms get acquired. Keep a second option warm so a provider change doesn't stall your sales for a month.</p>"""),
        ("The criteria that separate the best contractor financing companies", """<p>Lists of providers go stale quickly. The criteria don't. Whichever companies you compare, score them on the same things:</p>
<ul><li><strong>Dealer fees, plan by plan.</strong> The best contractor financing companies publish a fee schedule and offer at least one plan with no fee to you.</li>
<li><strong>Credit coverage.</strong> A single prime lender approves a narrow band of customers. A waterfall with second-look lenders approves more without you re-pitching the job.</li>
<li><strong>Approval amounts and terms.</strong> A $25,000 cap won't cover a full roof-and-gutters job in a high-cost metro.</li>
<li><strong>Funding speed and staging.</strong> Completion-only funding strains cash flow on large jobs; progress draws help.</li>
<li><strong>Customer experience.</strong> Soft-pull pre-qualification, a mobile application and clear disclosures. Hard pulls at the first step cost you nervous customers.</li>
<li><strong>Support and training.</strong> Does the provider train your sales team and give you a human to call when an application stalls?</li>
<li><strong>Contract terms.</strong> Exclusivity, minimum volume, early termination fees and who owns the customer relationship.</li></ul>"""),
        ("A scoring sheet you can use this week", """<p>Put each provider you're considering in a column and score 1 to 5 on each row: no-fee plan available, promotional plan fees, approval rate for your typical customer, maximum loan size, funding timing, soft-pull pre-qualification, mobile tools, trade-specific experience, support quality, and contract flexibility. Weight the rows by what matters to your business. A roofer in a storm market cares most about speed and credit coverage; a remodeler with long sales cycles cares about promotional plans and larger limits.</p>
<p>Run two or three real customer profiles through each provider's pre-qualification if they allow it. The marketing says everyone approves; the test tells you who actually does.</p>"""),
        ("Where AL Elite sits in this comparison", """<p>We're a matching marketplace, not a lender, so we belong in model 1. Our angle is trade fit: we route homeowners to lenders that fund roofs, HVAC and other home improvement work in their state, and contractors to programs built for their trade. We're paid by lenders and by partner contractors for program services, which we explain on our <a href="/how-we-make-money/">how we make money</a> page. The honest trade-off is the same as any marketplace: you get comparison and coverage, not a single bank's promotional rate on a single brand of equipment. For many contractors the right answer is a marketplace plus one manufacturer program.</p>"""),
        ("Mistakes contractors make when choosing a provider", """<ul><li><strong>Picking on the promo rate alone.</strong> The 0% plan that costs you 12% in dealer fees may lose money on thin-margin jobs.</li>
<li><strong>Signing exclusivity too early.</strong> Test a program for a quarter before locking in.</li>
<li><strong>Ignoring the decline path.</strong> Half the value of a program is what happens when the first lender says no.</li>
<li><strong>Not training the team.</strong> A program nobody presents produces no sales. See our guide to <a href="/blog/how-to-offer-financing-to-customers/">how to offer financing to customers</a> for scripts.</li>
<li><strong>Forgetting compliance.</strong> Rate quotes, pricing differences between cash and financed customers, and promises of approval all carry regulatory risk. Your provider should give you written guidance.</li></ul>"""),
    ],
    faqs=[
        ("What approval rate should I expect from a contractor financing program?", "It depends on your customers' credit profiles and whether the program includes second-look lenders. Programs with a single prime lender approve a narrower band; multi-lender waterfalls approve more. Ask providers for approval data from contractors in your trade and region, and test the pre-qualification with a few real profiles."),
        ("Do contractor financing companies charge the homeowner fees?", "The homeowner pays interest and any fees set by the lender, which are disclosed in the loan documents. Dealer fees are charged to the contractor, not the homeowner, though some contractors build them into the price."),
        ("Which contractor financing company has the lowest fees?", "Fees depend on the plan, not just the company. Most providers offer a standard-rate plan with no dealer fee and promotional plans with fees of several percent. Ask each provider for a written fee schedule and compare the plans you'd actually use."),
        ("Can I use more than one contractor financing company?", "Yes, unless you've signed an exclusive agreement. Many contractors pair a marketplace or multi-lender program with a manufacturer program for promotional rates on specific equipment."),
    ],
)

# ---------------------------------------------------------------- how-to-bid-construction-jobs (633)
EXTRA["/blog/how-to-bid-construction-jobs/"] = dict(
    meta="How to bid construction jobs profitably: takeoffs, labor burden, overhead, margin vs markup, contingency, payment terms and pricing in customer financing.",
    sections=[
        ("Change orders: where margin is won or lost", """<p>The original bid is only the start of the job's economics. Rotten decking, hidden wiring, an inspector's new requirement: every job has surprises, and whether they add margin or eat it depends on your process. Put a change-order clause in the contract with a per-sheet or per-hour price for the common surprises, so the conversation on site is "here's the price we agreed for this" rather than a negotiation while the roof is open. Document with photos, get written approval before the work, and bill promptly. Contractors who treat change orders as a favor to the customer end up financing them; contractors who price and process them cleanly turn surprises into the most profitable hours on the job.</p>
<p>Also watch the small items that aren't surprises but get forgotten: disposal, permit fees that rose this year, fuel, and the extra trip to finish the punch list. Keep a checklist of recurring omissions from past jobs and run every bid against it before it goes out.</p>"""),
        ("A worked bid: a $42,000 roofing job", f"""<p>Here's how the pieces fit on an illustrative residential re-roof, so the percentages stop being abstract.</p>
<div class='tbl'><table><thead><tr><th>Line</th><th class='num'>Amount</th><th>Note</th></tr></thead><tbody>
<tr><td>Materials (from takeoff, plus 5% waste)</td><td class='num'>$14,700</td><td>Shingles, underlayment, flashing, vents, fasteners</td></tr>
<tr><td>Labor: 160 crew-hours at $28 base</td><td class='num'>$4,480</td><td>Wages only</td></tr>
<tr><td>Labor burden at 35%</td><td class='num'>$1,568</td><td>Payroll tax, workers' comp, insurance, PTO</td></tr>
<tr><td>Equipment, dumpster, permits</td><td class='num'>$1,900</td><td>Direct job costs</td></tr>
<tr><td><strong>Direct cost</strong></td><td class='num'><strong>$22,648</strong></td><td></td></tr>
<tr><td>Overhead recovery at 18% of direct cost</td><td class='num'>$4,077</td><td>Office, trucks, insurance, sales, software</td></tr>
<tr><td>Cash-flow cost (45 days, see below)</td><td class='num'>$340</td><td>Financing the job until paid</td></tr>
<tr><td>Contingency at 4%</td><td class='num'>$1,083</td><td>Decking surprises, weather days</td></tr>
<tr><td><strong>Break-even</strong></td><td class='num'><strong>$28,148</strong></td><td></td></tr>
<tr><td>Target margin 25% (markup 33.3%)</td><td class='num'>$9,383</td><td>Margin on price, not markup on cost</td></tr>
<tr><td>Dealer fee if customer uses a 0% plan (6%)</td><td class='num'>$2,250</td><td>Only if offered; see below</td></tr>
<tr><td><strong>Bid price</strong></td><td class='num'><strong>$37,531 cash / $39,781 with promo plan</strong></td><td></td></tr>
</tbody></table></div><p class='cap'>Hypothetical figures to show structure. Your burden, overhead and margin targets will differ.</p>
<p>Notice how far the final price sits above direct cost. Contractors who bid at "cost plus 20%" on direct cost alone are often pricing below break-even once overhead and the cost of waiting to be paid are counted.</p>"""),
        ("Pricing the cost of waiting to be paid", f"""<p>If a job's direct cost is $22,648 and you're paid 45 days after you spend it, you've lent the customer that money for a month and a half. At an illustrative 18% annual cost of capital (a line of credit or short-term loan), that's roughly {money(22648 * 0.18 * 45 / 365, False)}. It belongs in the bid. On commercial work with retainage and 60- to 90-day pay cycles the number is larger, and the tools to bridge it (a <a href="/contractor-business-loans/line-of-credit/">construction line of credit</a> or <a href="/contractor-business-loans/invoice-factoring/">invoice factoring</a>) have costs of their own that the bid should recover.</p>"""),
        ("Bid-to-win, not bid-to-be-cheapest", """<p>The lowest bid wins a certain kind of customer: the one who'll leave you for the next lowest bid. A bid wins profitably when it's clear, complete and easy to say yes to:</p>
<ul><li><strong>Itemize the scope</strong> so your price isn't compared with a competitor's vaguer, cheaper one.</li>
<li><strong>Show two or three options</strong> (standard, better, best) with the monthly payment for each. Customers pick the middle option far more often than the cheapest.</li>
<li><strong>Put the payment next to the price.</strong> A $37,500 roof is also "about $700 a month over 5 years." That number closes jobs.</li>
<li><strong>Set an expiry.</strong> Material prices move; a 30-day validity protects you and creates a reason to decide.</li></ul>"""),
        ("Track your numbers after the job", """<p>A bid is a forecast. Compare it with reality on every job: actual hours against estimated, material cost against the takeoff, change-order revenue, and days to payment. After ten jobs you'll know whether your burden rate, overhead percentage and contingency are honest. Most contractors find labor hours run higher than estimated and change orders lower than hoped; adjust the next bids accordingly. If you offer customer financing, track how often it's used and what the dealer fees actually cost, so the allowance in your bid matches reality. Our <a href="/for-contractors/">contractor financing</a> page covers how to set that up.</p>"""),
    ],
    faqs=[
        ("How do I bid a job when material prices keep changing?", "Price from current supplier quotes, not last quarter's, add a short validity period to the bid, and include a materials escalation clause for jobs that won't start for weeks. Locking in a supplier price for the job's duration, where possible, removes the risk entirely."),
        ("What margin should a construction bid have?", "It varies by trade and market. Many residential contractors target a 20% to 35% gross margin on price after full direct costs; specialty and emergency work can carry more. The key is to apply margin on top of overhead and contingency, not on bare direct cost."),
        ("Should I add the cost of customer financing to my bids?", "Only for plans that charge you a dealer fee, and only on jobs where the customer chooses that plan. Many contractors quote a cash price and a financed price, or absorb the fee on larger jobs where the margin allows."),
    ],
)

# ---------------------------------------------------------------- how-to-offer-financing-to-customers (686)
EXTRA["/blog/how-to-offer-financing-to-customers/"] = dict(
    meta="How to offer financing to customers as a contractor: choose a program, set it up, present the monthly payment, handle declines and get paid.",
    sections=[
        ("Training your reps in an afternoon", """<p>Most financing programs fail at the rep level, not the program level. A short training works better than a thick manual:</p>
<ul><li><strong>Role-play the three scripts above</strong> until they sound natural, including the decline conversation.</li>
<li><strong>Have every rep run the pre-qualification tool</strong> on a test profile so they know every screen the customer will see.</li>
<li><strong>Agree on what they can and can't say:</strong> no rate guesses, no approval promises, always show the total price alongside the payment.</li>
<li><strong>Give them a one-page cheat sheet</strong> with the plans you offer, the monthly payment on five typical job sizes, and who to call when an application stalls.</li>
<li><strong>Review the numbers weekly</strong> for the first month: who's presenting financing on every estimate and who isn't.</li></ul>
<p>Reps who are comfortable with the conversation present it every time; reps who aren't quietly skip it, and the program produces nothing.</p>"""),
        ("Three scripts that work at the kitchen table", """<p>The words matter more than the brochure. Three short scripts contractors use successfully:</p>
<p><strong>Opening the topic early:</strong> "Before we get into the numbers, most of our customers pay one of three ways: cash or check, an insurance claim if it's storm damage, or monthly financing through a lender we work with. I'll show you all three so you can pick what suits you."</p>
<p><strong>Presenting the price:</strong> "The full price for the system we talked about is $12,400. If you'd rather spread it out, with the financing program that's about $230 a month over five years, and you can see whether you'd qualify without affecting your credit score. Want me to show you?"</p>
<p><strong>When they hesitate on price:</strong> "I understand. Would it help to see what the payment looks like on the standard option versus the upgraded one? The difference is usually less than people expect."</p>
<p>None of these promise approval, quote a rate you don't have in writing, or pressure. That's deliberate; it keeps you on the right side of the lender agreement and lending rules.</p>"""),
        ("The numbers to track in your first 90 days", f"""<p>Offering financing changes your business only if you measure it. Five numbers, tracked before and after:</p>
<ol><li>Close rate on estimates where financing was presented, versus where it wasn't.</li>
<li>Average ticket size.</li>
<li>Share of jobs financed, and which plans were chosen.</li>
<li>Dealer fees paid as a percentage of financed revenue.</li>
<li>Days from estimate to signed contract.</li></ol>
<p>A company running 40 estimates a month at a 30% close and a $12,000 average ticket books about {money(40 * 0.30 * 12000, False)}. If financing lifts the close rate to 35% and the ticket by 5%, that becomes about {money(40 * 0.35 * 12600, False)}. Even after dealer fees on the financed share, the gain is usually clear within one quarter. If it isn't, the problem is usually presentation, not the program.</p>"""),
        ("Common setup mistakes", """<ul><li><strong>Only enrolling the owner.</strong> Every rep who quotes needs their own login and training.</li>
<li><strong>Burying the financing on page three of the proposal.</strong> Put the monthly option next to the total price on page one.</li>
<li><strong>Offering only the promotional plan.</strong> Lead with a standard plan that costs you nothing; offer the promo when it genuinely helps the customer.</li>
<li><strong>No process for declines.</strong> Decide in advance: second-look lender, co-applicant, smaller scope, or an independent option like <a href="/home-improvement-financing/">AL Elite's homeowner matching</a>.</li>
<li><strong>Charging financed customers more without disclosure.</strong> Check your lender agreement and state rules; this is a frequent compliance problem.</li></ul>"""),
        ("Where this fits with other ways to pay", """<p>Customer financing is one of three payment paths, alongside cash and insurance. For storm trades, insurance pays most of the roof and financing covers the deductible and uncovered items, so your team should be able to explain both in the same conversation. Our guide to <a href="/blog/roof-financing-after-hail-damage/">roof financing after hail damage</a> is written for homeowners, and it's a useful read for reps who sell in storm markets. For a comparison of program providers, see <a href="/blog/best-contractor-financing-companies/">best contractor financing companies</a>.</p>"""),
    ],
    faqs=[
        ("Do I need a license to offer customer financing?", "You don't lend the money, the lender does, so you generally don't need a lending license. You do need to follow the lender's program rules and advertising and pricing laws in your state. Ask the provider for written compliance guidance and check with counsel if you're unsure."),
        ("How long does it take to set up customer financing?", "Days to a few weeks, depending on the provider's review of your business, licensing and insurance. Budget time to train your sales team before the first estimate."),
        ("What should I say if a customer asks what rate they'll get?", "Only what the lender has stated in writing. Say that the lender sets the rate based on their application, show the pre-qualification tool, and avoid guessing a number."),
    ],
)

# ---------------------------------------------------------------- does-insurance-cover-roof-replacement (724)
EXTRA["/blog/does-insurance-cover-roof-replacement/"] = dict(
    meta="Does insurance cover roof replacement? When storm damage is covered, how deductibles and depreciation work, the claim process, and financing the gap.",
    sections=[
        ("Before the storm: three things to do now", """<ul><li><strong>Photograph your roof and the soft metals</strong> (gutters, vents, AC fins) in good condition, with dates. "Before" photos make hail claims far easier.</li>
<li><strong>Find your roof's installation date and any warranty paperwork.</strong> Age drives both the payment schedule and the adjuster's view of pre-existing wear.</li>
<li><strong>Read the deductible line.</strong> If it's a percentage of dwelling coverage, calculate the dollar figure now so it isn't a surprise, and decide whether to keep an emergency fund or a financing plan ready for it.</li></ul>
<p>Ten minutes of preparation can be the difference between a claim that pays the roof and one that pays a repair.</p>"""),
        ("Roof age schedules and the newer policy forms", """<p>Insurers in storm-heavy states have been rewriting roof coverage. Three changes are now common, and they decide how much of a replacement you'll pay for yourself.</p>
<ul><li><strong>Roof payment schedules.</strong> Some policies pay a percentage of replacement cost that falls with the roof's age, for example 100% for a roof under 5 years, stepping down to 40% or less past 15 years. On an older roof that can leave a five-figure gap.</li>
<li><strong>Actual cash value for roofs only.</strong> A policy can cover the house at replacement cost but pay the roof at depreciated value. Check the roof endorsement, not just the main form.</li>
<li><strong>Cosmetic damage exclusions.</strong> Dents on a metal roof that don't cause leaks may be excluded entirely.</li></ul>
<p>Ask your agent which of these applies to you before the next storm season. It's easier to change coverage calmly than to discover it after the adjuster's visit.</p>"""),
        ("How to read the adjuster's estimate", """<p>The estimate is usually produced in a standard estimating program and runs to several pages. The lines that matter most:</p>
<ul><li><strong>Replacement cost value (RCV):</strong> what the insurer thinks the full job costs.</li>
<li><strong>Depreciation:</strong> the amount held back until the work is done, on replacement-cost policies.</li>
<li><strong>Actual cash value (ACV):</strong> RCV minus depreciation, which is what the first check is based on.</li>
<li><strong>Deductible:</strong> subtracted from what's paid to you.</li>
<li><strong>Line items:</strong> squares of shingles, underlayment, flashing, vents, gutters, and any code-upgrade allowance.</li></ul>
<p>Compare the line items with your roofer's quote. If the adjuster missed the decking, the drip edge or the second layer of shingles, your roofer can submit a supplement with photos. Supplements are routine and often approved.</p>"""),
        ("Supplements, re-inspections and appraisal", """<p>If the first estimate is short, you have options before accepting it. A <strong>supplement</strong> is a request to add missed or underpriced items, usually submitted by the roofer with documentation. A <strong>re-inspection</strong> is a second adjuster visit, useful when the first was rushed after a large storm. If you and the insurer still disagree on the amount (not whether the damage is covered), most policies include an <strong>appraisal clause</strong>: you and the insurer each hire an appraiser, and an umpire resolves differences. For disputes about coverage itself, your state's insurance department can take complaints, and a public adjuster or attorney may be worth consulting on a large claim.</p>"""),
        ("Working out the financing number", f"""<p>The amount you may need to finance is the gap between the roofer's price and what insurance pays, plus timing. On a $16,000 replacement with a $14,500 RCV, $3,200 depreciation and a $2,500 deductible, the first check is $8,800. You owe the roofer $7,200 until the depreciation is released on completion, and $4,000 permanently (the deductible plus $1,500 the estimate didn't cover). Financing $4,000 at an illustrative 11.99% over 36 months is about {pm(4000, 11.99, 36)} a month. Our guide to <a href="/blog/roof-financing-after-hail-damage/">roof financing after hail damage</a> walks through this step by step, and the <a href="/roof-financing/">roof financing</a> page compares the options for the gap.</p>"""),
    ],
    faqs=[
        ("Should I file a claim for minor roof damage?", "Not always. If the repair costs less than your deductible, or only slightly more, filing may not pay and can affect your claims history. Get a roofer's assessment first and ask your agent how a claim would affect your renewal."),
        ("Will my insurance pay for a full roof replacement or just a repair?", "It depends on the extent of damage and your policy. Insurers often repair isolated damage and replace when damage is widespread or matching materials aren't available. Some states have matching rules that affect this."),
        ("What is recoverable depreciation on a roof claim?", "On a replacement-cost policy, the insurer holds back depreciation from the first payment and releases it after the roof is completed and invoiced, usually within a deadline set by the policy. Miss the deadline and it may not be paid."),
    ],
)

# ---------------------------------------------------------------- how-to-finance-a-new-roof (1016)
EXTRA["/blog/how-to-finance-a-new-roof/"] = dict(
    meta="How to finance a new roof: personal loans, contractor plans, HELOCs, home equity loans, credit cards, insurance and government programs compared.",
    sections=[
        ("What lenders look at, whichever option you choose", """<p>Across personal loans, contractor plans and home equity products, the same five things decide approval and rate: your credit score and recent payment history, your income and how much of it already goes to debt, the amount you're asking for, how long you've had credit, and, for secured options, how much equity you have. You can't change your history overnight, but you can reduce the amount (finance the gap, not the roof), pay a card balance down before you apply, gather income documents so the application is complete, and check options with a soft pull before committing to any hard inquiry. Those four steps improve offers at every lender on this list.</p>"""),
        ("Option 7: Government-backed programs", """<p>Three federal programs fit specific situations. FHA Title I property improvement loans are made by HUD-approved lenders for improvements that protect the home, up to $25,000 on a single-family house with terms up to 20 years; amounts over $7,500 are secured by the property. FHA 203(k) folds repairs into a purchase or refinance mortgage. In eligible rural areas, USDA Section 504 offers low-rate repair loans to very-low-income owners and grants of up to $10,000 to owners 62 and older. None of these is fast, and not every lender participates, so they suit planned replacements. Details and links are on our <a href="/roof-financing/">roof financing</a> page.</p>"""),
        ("Matching the option to your situation", """<p>Four common situations and the option that usually fits:</p>
<ul><li><strong>Storm damage, insurance paying most of it.</strong> Finance only the deductible and uncovered items with a short unsecured loan or the roofer's standard plan.</li>
<li><strong>Planned replacement, good equity, no rush.</strong> Home equity loan, or a HELOC if you can lock a fixed rate on the draw.</li>
<li><strong>Urgent replacement, little equity.</strong> Unsecured personal loan or contractor financing; compare the two on APR and total cost.</li>
<li><strong>Lower credit score.</strong> Reduce the amount, check options with a soft pull, consider a co-applicant, and look at government-backed programs if timing allows.</li></ul>"""),
        ("Questions to ask every lender", """<ol><li>What is the APR including fees, and is the rate fixed?</li>
<li>Is there an origination fee, and is it deducted from the loan amount?</li>
<li>Is there a prepayment penalty?</li>
<li>Is any promotional period deferred interest or waived interest?</li>
<li>When is the roofer paid, and when does my first payment start?</li>
<li>Does checking my options use a soft or hard credit inquiry?</li></ol>
<p>Written answers to those six questions let you compare any two offers in a few minutes.</p>"""),
    ],
    faqs=[
        ("What is the cheapest way to finance a new roof?", "For a planned project with enough equity, a home equity loan usually has the lowest rate. For an urgent roof or a smaller gap, a short-term unsecured loan or a no-fee contractor plan often costs less in total once closing costs and time are counted."),
    ],
)


def apply(pages_by_path):
    for path, extra in EXTRA.items():
        p = pages_by_path.get(path)
        if not p:
            continue
        for k in ("h1", "title", "meta"):
            if k in extra:
                p[k] = extra[k]
        p["sections"] = list(p.get("sections", [])) + extra.get("sections", [])
        p["faqs"] = list(p.get("faqs", [])) + extra.get("faqs", [])
