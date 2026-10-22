"""New blog posts, October 2026 batch A (homeowner side). From the Content Calendar, months 2-4.
Each post targets a keyword that is distinct from its money page (to avoid cannibalising it),
links to exactly one primary money page plus one related post in the body, and uses computed,
illustrative payments only."""
from common import *

HOME = ("Home", "/")
BLOG = ("Blog", "/blog/")
CLAIMS = "https://www.claimsjournal.com/news/national/2026/04/23/337102.htm"
DATE = "2026-10-20"

def pm(P, apr, n):
    return money(payment(P, apr, n), False)

def ti(P, apr, n):
    return money(payment(P, apr, n) * n - P, False)


# --------------------------------------------------------------------------- 1
HAIL = dict(
    path="/blog/roof-financing-after-hail-damage/", date=DATE,
    crumbs=[HOME, BLOG, ("Roof financing after hail damage", "/blog/roof-financing-after-hail-damage/")],
    eyebrow="Homeowner guide", h1="Roof financing after hail damage: what to do first",
    title="Roof Financing After Hail Damage: What to Do First (2026 Guide)",
    meta="Hail hit your roof? The order that protects your claim and budget: document, file, get inspected, then finance only the gap insurance leaves.",
    answer="After hail, the order matters: photograph the damage and make temporary repairs, file the insurance claim, get a roofer to meet the adjuster, and only then decide how to finance. Most homeowners don't need to finance the whole roof. They need to cover the deductible, any depreciation held back until the work is done, and items the policy doesn't pay for. That gap is usually a smaller, shorter loan.",
    money_page=("roof financing", "/roof-financing/"), project="Roof replacement or repair",
    sections=[
        ("Why hail turns into a financing question", f"""<p>Hail is the most expensive routine weather event for American roofs. State Farm alone paid about $5.6 billion in hail claims in 2025, with Texas accounting for $1.4 billion of it, followed by Missouri and Illinois (<a href="{CLAIMS}" rel="noopener">Claims Journal</a>). Behind those totals are millions of homeowners who woke up to dented gutters and granules in the downspouts and a roof that suddenly needs replacing years ahead of schedule.</p>
<p>The money problem is rarely "insurance won't pay anything." It's timing and gaps. The deductible is due up front. Many policies hold back part of the payout until the roof is finished. Code upgrades, decking and gutters may or may not be covered. A homeowner who budgeted nothing for a roof this year can easily be looking at several thousand dollars out of pocket, on a deadline set by the next storm.</p>"""),
        ("Step 1: Document and protect the roof (first 48 hours)", """<p>Before anyone talks about money, create the record your claim will rest on.</p>
<ul><li><strong>Photograph everything from the ground.</strong> Dented gutters, downspouts, window screens, AC fins, siding, cars and patio furniture. Hail size and direction show up on soft metals long after the storm.</li>
<li><strong>Note the date and time of the storm.</strong> Your insurer will check it against weather reports.</li>
<li><strong>Stop active leaks.</strong> A tarp or temporary patch is usually reimbursable and most policies expect you to prevent further damage. Keep the receipt.</li>
<li><strong>Don't climb onto a wet or damaged roof.</strong> Leave the close inspection to a roofer with fall protection.</li></ul>
<p>If a storm-chasing crew knocks on the door the next morning, take their card and don't sign anything yet. We'll come back to why.</p>"""),
        ("Step 2: File the claim and understand your policy", """<p>Call your insurer or file online and get a claim number. Then find your declarations page and look for three things, because they decide how much you may need to finance.</p>
<ul><li><strong>Your deductible, and how it's calculated.</strong> In hail-prone states many policies now carry a separate wind and hail deductible set as a percentage of the dwelling coverage, often 1% or 2%. On a home insured for $350,000, a 2% deductible is $7,000, which is a very different number from a flat $1,000.</li>
<li><strong>Replacement cost (RCV) or actual cash value (ACV).</strong> Replacement-cost policies typically pay in two parts: an initial check for the depreciated value, then the held-back depreciation once the work is complete and invoiced. Actual-cash-value policies only pay the depreciated value, so an older roof can leave a large gap that never comes back.</li>
<li><strong>Roof age schedules and exclusions.</strong> Some newer policies pay roofs on a schedule by age, or exclude cosmetic damage to metal. Read these before the adjuster visits so nothing surprises you.</li></ul>
<p>Our longer guide on <a href="/blog/does-insurance-cover-roof-replacement/">whether insurance covers roof replacement</a> walks through each of these in more detail.</p>"""),
        ("Step 3: Get the inspection right", """<p>Ask a licensed local roofer to inspect and, ideally, to be on the roof when the adjuster comes. Adjusters work quickly after big storms, and a contractor who points out the soft-metal damage, the bruised shingles and the code items gives you the best chance of an accurate first estimate.</p>
<p>When you choose that roofer, check the state license or registration where one exists, a local address, proof of insurance and reviews that predate the storm. Be cautious about anyone who offers to "cover your deductible" or "eat" it. Waiving or rebating a deductible is illegal in several states, including Texas and Colorado, and it's a sign the rest of the job may be priced around the insurance payout rather than the work. In Florida, rules on assignment-of-benefits agreements changed for policies issued or renewed from 2023, so read anything that asks you to sign over claim rights very carefully.</p>"""),
        ("Step 4: Work out the gap you actually need to finance", f"""<p>Once you have the adjuster's estimate and a roofer's itemized quote, the financing number becomes simple arithmetic. Here is an illustrative example for a replacement-cost policy.</p>
<div class='tbl'><table><thead><tr><th>Line</th><th class='num'>Amount</th></tr></thead><tbody>
<tr><td>Roofer's contract price</td><td class='num'>$18,500</td></tr>
<tr><td>Insurer's replacement cost estimate</td><td class='num'>$17,200</td></tr>
<tr><td>Less depreciation held back until completion</td><td class='num'>&minus;$4,100</td></tr>
<tr><td>Less 1% wind/hail deductible on $300,000 coverage</td><td class='num'>&minus;$3,000</td></tr>
<tr><td><strong>First insurance check</strong></td><td class='num'><strong>$10,100</strong></td></tr>
<tr><td>Owed to roofer before depreciation is released</td><td class='num'>$8,400</td></tr>
<tr><td><strong>Permanent gap after depreciation is paid</strong> (deductible + uncovered items)</td><td class='num'><strong>$4,300</strong></td></tr>
</tbody></table></div>
<p class='cap'>Hypothetical figures for illustration. Your policy terms, estimate and contract will differ.</p>
<p>Two different needs show up. There's a short-term cash need of about $8,400 until the depreciation check arrives, and a permanent gap of about $4,300. Some roofers will wait for the depreciation check; others want it before they start. Ask, because the answer changes what you borrow.</p>
<p>If you only need the permanent gap, a $4,300 loan at an illustrative 11.99% APR is about {pm(4300, 11.99, 36)} a month over 36 months, or {pm(4300, 11.99, 60)} over 60. If you also need to bridge the depreciation, borrowing $8,400 for a short term and paying most of it down when the second check lands keeps total interest low.</p>"""),
        ("Your financing options after a storm", """<p>Which option fits depends on how fast you need the money, how big the gap is and how you feel about using the house as collateral.</p>
<ul><li><strong>Unsecured personal loan.</strong> Fast, often funded within days, no lien on the home. Good for gaps from a few thousand dollars up to the lender's cap. APR depends heavily on credit.</li>
<li><strong>Roofer-arranged financing.</strong> Convenient at the kitchen table and sometimes promotional. Ask whether a "same as cash" offer is deferred interest, and whether a dealer fee is built into the price.</li>
<li><strong>HELOC or home equity loan.</strong> Usually cheaper per dollar, but slower to close. Better suited to large gaps on older roofs under ACV policies than to an urgent deductible.</li>
<li><strong>Emergency savings plus a small loan.</strong> Often the cheapest blend. Cover the deductible from savings and finance only the uncovered items.</li></ul>
<p>Whatever you choose, borrow against the itemized gap, not the full roof price. Our <a href="/roof-financing/">roof financing</a> page compares these options side by side with example payments.</p>"""),
        ("Mistakes that cost homeowners money after hail", """<ul><li><strong>Signing a contract before the adjuster visits.</strong> Some storm contracts bind you to that roofer at whatever the insurer approves, with cancellation fees if you change your mind.</li>
<li><strong>Financing the whole roof when insurance is paying most of it.</strong> You pay interest on money you didn't need.</li>
<li><strong>Missing the depreciation deadline.</strong> Replacement-cost policies usually give you a window to finish the work and submit the final invoice. Miss it and the held-back money may be lost.</li>
<li><strong>Taking a long term for a small gap.</strong> A 10-year loan on a $4,000 deductible means paying for the storm long after the roof is forgotten.</li>
<li><strong>Ignoring the rest of the house.</strong> Gutters, siding, screens and AC coils are often on the same claim. Make sure they're on the estimate before you finance anything.</li></ul>"""),
        ("A simple timeline to follow", """<ol><li><strong>Day 0 to 2:</strong> photos, temporary repairs, claim filed.</li>
<li><strong>Week 1 to 3:</strong> roofer inspection, adjuster visit, estimates compared.</li>
<li><strong>Week 2 to 4:</strong> calculate the gap, compare financing, sign the roofing contract.</li>
<li><strong>Install:</strong> keep copies of the final invoice, permits and photos.</li>
<li><strong>After install:</strong> submit for released depreciation, then pay down any bridge financing.</li></ol>"""),
    ],
    faqs=[
        ("Should I finance the roof before the insurance claim is settled?", "Usually not. Wait until you have the adjuster's estimate and a roofer's itemized quote, so you borrow only the deductible and uncovered items. The exception is urgent temporary repairs, which you can pay for and submit as part of the claim."),
        ("Can I get roof financing to cover my hail deductible?", "Yes. Personal loans and contractor financing programs commonly cover deductibles and uncovered items. Lenders treat it like any other roof loan, based on your credit, income and the amount."),
        ("What if insurance denies my hail claim?", "Ask for the denial in writing with the policy language it relies on, get your roofer's documentation, and consider requesting a re-inspection or using your policy's appraisal clause. If you still need the work, you'd finance the full cost, so compare options carefully."),
        ("Is it illegal for a roofer to pay my deductible?", "In several states, including Texas and Colorado, it is illegal for a contractor to waive, rebate or absorb an insurance deductible. Even where it isn't explicitly illegal, it can amount to insurance fraud. Pay your deductible and finance it if needed."),
        ("Will my insurance premium go up after a hail claim?", "It can. Weather claims are generally treated differently from at-fault claims, but insurers in hail-heavy states have been raising premiums and deductibles across the board. Ask your agent how a claim may affect your renewal, and weigh that against the size of the damage."),
        ("How long do I have to file a hail claim?", "It depends on your policy and your state. Some policies and states allow a year or more, others less. Check your policy and file as soon as you can; early claims are easier to document."),
    ],
    related=[("Roof financing", "/roof-financing/"), ("Does insurance cover roof replacement?", "/blog/does-insurance-cover-roof-replacement/"), ("Roof financing calculator", "/tools/roof-financing-calculator/"), ("Siding financing after storm damage", "/siding-financing/"), ("Storm-market city pages", "/locations/")],
)


# --------------------------------------------------------------------------- 2
ROOF_AMTS = (8000, 12000, 15000, 20000, 25000, 30000, 40000)
def roof_month_table():
    terms = (36, 60, 84, 120, 144)
    head = "<tr><th>Roof cost</th>" + "".join(f"<th class='num'>{t} mo</th>" for t in terms) + "</tr>"
    rows = "".join("<tr><td><strong>" + money(P, False) + "</strong></td>" + "".join(f"<td class='num'>{pm(P, 9.99, t)}</td>" for t in terms) + "</tr>" for P in ROOF_AMTS)
    return f"<div class='tbl'><table><thead>{head}</thead><tbody>{rows}</tbody></table></div><p class='cap'>Illustrative monthly payments at 9.99% APR, standard amortization, no fees. Not an offer of credit.</p>"

def apr_tier_table(P=15000, n=60):
    tiers = [("Excellent credit (example)", 7.99), ("Good credit (example)", 11.99), ("Fair credit (example)", 17.99), ("Lower credit (example)", 24.99)]
    rows = "".join(f"<tr><td>{t}</td><td>{a:.2f}%</td><td class='num'>{pm(P, a, n)}</td><td class='num'>{ti(P, a, n)}</td></tr>" for t, a in tiers)
    return f"<div class='tbl'><table><thead><tr><th>Profile</th><th>Example APR</th><th class='num'>Monthly</th><th class='num'>Total interest</th></tr></thead><tbody>{rows}</tbody></table></div><p class='cap'>{money(P, False)} over {n} months. Example APRs are illustrative tiers, not quotes; lenders set rates after reviewing your application.</p>"

MONTHLY = dict(
    path="/blog/how-much-does-a-new-roof-cost-per-month/", date=DATE,
    crumbs=[HOME, BLOG, ("New roof cost per month", "/blog/how-much-does-a-new-roof-cost-per-month/")],
    eyebrow="Homeowner guide", h1="How much does a new roof cost per month? Payment tables by price",
    title="How Much Does a New Roof Cost Per Month? Payment Tables (2026)",
    meta="Monthly payments for $8,000 to $40,000 roofs over 3 to 12 years, how APR and term change the total, and how to pick a payment that fits.",
    answer=f"A new roof financed at an illustrative 9.99% APR costs roughly {pm(15000, 9.99, 60)} a month for a $15,000 roof over five years, {pm(20000, 9.99, 84)} a month for a $20,000 roof over seven years, and {pm(30000, 9.99, 120)} a month for a $30,000 roof over ten years. Your real payment depends on the price, the APR a lender offers you and the term you choose. Longer terms lower the payment but raise total interest.",
    money_page=("roof financing calculator", "/tools/roof-financing-calculator/"), project="Roof replacement or repair",
    sections=[
        ("Start with the price, not the payment", """<p>The monthly payment is the number everyone asks about, but it's the last number you should settle. It comes from three inputs: how much you borrow, the APR and the term. Change any one and the payment moves.</p>
<p>So begin with an itemized quote. Roof prices swing widely with size, pitch, the number of layers to tear off, material, decking condition and local labor costs. A typical asphalt-shingle replacement on a single-family home often lands somewhere between about $10,000 and $25,000, metal and tile run higher, and storm markets can spike after a big hail season. Two or three quotes on the same scope will tell you more about your number than any national average.</p>
<p>Ask each roofer to quote the same scope: the same material line, underlayment, ventilation, flashing and gutter work, plus a per-sheet price for any decking that needs replacing. Without that, you're comparing different roofs, and the cheapest quote can become the most expensive once change orders arrive. A written scope also gives the lender a clean figure to work with, which speeds up approval.</p>
<p>If insurance is paying part of the job, finance only the gap. Our guide to <a href="/blog/roof-financing-after-hail-damage/">roof financing after hail damage</a> shows how to work that number out.</p>"""),
        ("Monthly payment by roof price and term", f"""<p>The table below holds the APR steady so you can see what price and term do on their own.</p>{roof_month_table()}
<p>Notice how the payment falls fast at first as the term stretches, then flattens. Going from 36 to 60 months on a $15,000 roof cuts the payment by about {money(payment(15000, 9.99, 36) - payment(15000, 9.99, 60), False)} a month. Going from 120 to 144 months saves only about {money(payment(15000, 9.99, 120) - payment(15000, 9.99, 144), False)}, while adding two more years of payments.</p>"""),
        ("How your credit changes the same roof", f"""<p>APR does more damage than most people expect. Here is the same $15,000 roof over five years at four example rates.</p>{apr_tier_table()}
<p>The gap between the best and worst example tiers is about {money(payment(15000, 24.99, 60) - payment(15000, 7.99, 60), False)} a month and roughly {money((payment(15000, 24.99, 60) - payment(15000, 7.99, 60)) * 60, False)} over the life of the loan. That's why it's worth comparing several lenders, and why a few months of credit repair can be worth more than any discount on the roof itself. If your score is on the lower side, read our <a href="/roof-financing/bad-credit-roof-financing/">roof financing with bad credit</a> page for realistic expectations.</p>"""),
        ("The real cost of a longer term", f"""<p>A 10- or 12-year term makes a roof feel affordable, and sometimes it's the right call. Just know what it costs. On a $20,000 roof at 9.99%:</p>
<div class='tbl'><table><thead><tr><th>Term</th><th class='num'>Monthly</th><th class='num'>Total interest</th><th class='num'>Total repaid</th></tr></thead><tbody>
{''.join(f"<tr><td>{n} months</td><td class='num'>{pm(20000, 9.99, n)}</td><td class='num'>{ti(20000, 9.99, n)}</td><td class='num'>{money(payment(20000, 9.99, n) * n, False)}</td></tr>" for n in (36, 60, 84, 120, 144))}
</tbody></table></div><p class='cap'>Illustrative, standard amortization, no fees.</p>
<p>A sensible middle path is to take a longer term for a lower required payment, then pay extra when you can. Before you sign, confirm the loan has no prepayment penalty. Most personal loans don't, but check.</p>"""),
        ("How to pick a payment that fits", """<p>A quick way to sanity-check a roof payment:</p>
<ol><li><strong>Look at your monthly budget after essentials.</strong> The roof payment should fit without drawing down your emergency fund.</li>
<li><strong>Match the term to the roof's life, but shorter.</strong> An asphalt roof may last 20 years or more. A loan that ends well before then means you're not still paying for this roof when the next one is due.</li>
<li><strong>Compare total cost, not just payment.</strong> Two offers with similar payments can differ by thousands in interest and fees.</li>
<li><strong>Price in fees.</strong> An origination fee taken from the loan means you either borrow more or receive less. Ask for the APR, which includes it, rather than only the interest rate.</li>
<li><strong>Read promotional offers carefully.</strong> A "no interest for 12 months" plan may charge all the back interest if the balance isn't cleared in time.</li></ol>"""),
        ("Personal loan, contractor plan or home equity?", """<p>The payment tables above assume a simple fixed-rate installment loan, which is how most unsecured personal loans and many contractor financing plans work. Home equity loans and HELOCs often carry lower rates and longer terms, so the monthly figure can be lower again, but they take longer to close, can involve closing costs and put your home up as collateral. HELOC rates are usually variable, so the payment can change.</p>
<p>For an urgent replacement, speed and simplicity often win. For a large, planned project, the lower cost of home equity can be worth the wait. We compare the trade-offs in <a href="/blog/heloc-vs-roof-loan/">HELOC vs roof loan vs contractor financing</a>.</p>"""),
        ("Three homeowners, three choices", f"""<p>The right term depends on the household, not the roof. Three illustrative examples, all at 9.99% APR:</p>
<p><strong>Maria, $14,000 roof, tight budget, expects a raise next year.</strong> She takes 84 months for a required payment of about {pm(14000, 9.99, 84)}, and plans to add $100 a month once her pay goes up. Paying {money(payment(14000, 9.99, 84) + 100, False)} a month instead clears the loan years early and saves a large share of the interest, because the extra goes straight to principal.</p>
<p><strong>Dev and Priya, $22,000 metal roof, comfortable budget.</strong> They choose 60 months at about {pm(22000, 9.99, 60)} a month. Total interest is about {ti(22000, 9.99, 60)}, against about {ti(22000, 9.99, 120)} on a 10-year term. They plan to stay in the house for decades, so finishing the loan quickly matters more to them than a lower monthly figure.</p>
<p><strong>Tom, $6,500 insurance gap after hail.</strong> A small amount doesn't need a long term. Over 36 months the payment is about {pm(6500, 9.99, 36)}, with total interest of only about {ti(6500, 9.99, 36)}. Stretching a gap that size to ten years would make little sense.</p>"""),
        ("Costs the monthly payment doesn't show", """<p>A roof loan payment isn't the only number that changes when you replace a roof. A few others are worth putting in the plan:</p>
<ul><li><strong>Origination fees.</strong> Some lenders deduct a fee from the loan amount. If you need $15,000 in hand and the fee is 5%, you'd need to borrow more to cover it. The APR includes this fee, which is why it's the better number to compare.</li>
<li><strong>Insurance.</strong> A new roof, especially an impact-resistant one, can lower your homeowners premium with some insurers. Older roofs are increasingly hard or expensive to insure in storm states. Ask your agent before choosing materials.</li>
<li><strong>Energy.</strong> Better attic ventilation and reflective materials can trim cooling costs. Don't count on savings to pay the loan, but they can soften it.</li>
<li><strong>Gutters, decking and extras.</strong> Rotten decking found during tear-off is a common surprise. Ask how your contract prices it per sheet, and keep a 10% cushion.</li>
<li><strong>Home value.</strong> A roof doesn't usually return its full cost on resale, but an old roof can stall a sale or lower offers. If you're likely to sell soon, factor that in.</li></ul>"""),
        ("Try your own numbers", """<p>Every roof and every borrower is different, so use the tables as a starting point. Our <a href="/tools/roof-financing-calculator/">roof financing calculator</a> lets you enter your own quote, APR and term, and shows the monthly payment, total interest and a full amortization schedule. When you're ready to see real offers, one request through AL Elite gets your project in front of lenders who fund roofs in your state, and we tell you up front which ones start with a soft credit check.</p>"""),
    ],
    faqs=[
        ("What is a typical monthly payment for a new roof?", f"For a $15,000 roof at an illustrative 9.99% APR, about {pm(15000, 9.99, 60)} a month over five years or {pm(15000, 9.99, 120)} over ten. Your payment depends on your price, APR and term."),
        ("What credit score do I need to finance a roof?", "There's no single cutoff. Each lender sets its own criteria, and many look at income, debts and payment history as well as score. Stronger credit generally means more offers and lower APRs."),
        ("Is it better to take a shorter or longer roof loan?", "A shorter term costs less in total interest; a longer term lowers the monthly payment. Many homeowners choose a term with a comfortable payment and pay extra when they can, provided there's no prepayment penalty."),
        ("Do roof loans have prepayment penalties?", "Most unsecured personal loans don't, but some loans and promotional plans have fees or conditions. Check the loan agreement before signing."),
        ("Can I pay off a roof loan early?", "Usually yes. Paying extra each month or making a lump-sum payment reduces principal and total interest. Confirm there's no prepayment penalty and that extra payments are applied to principal."),
        ("Does checking roof financing options hurt my credit?", "Many lenders show initial options with a soft inquiry, which doesn't affect your score. A hard inquiry usually happens only when you formally apply with a lender you've chosen."),
    ],
    related=[("Roof financing calculator", "/tools/roof-financing-calculator/"), ("How to finance a new roof: 6 options", "/blog/how-to-finance-a-new-roof/"), ("Roof financing", "/roof-financing/"), ("Metal roof financing", "/roof-financing/metal-roof-financing/")],
)


# --------------------------------------------------------------------------- 3
HVAC_BAD = dict(
    path="/blog/how-to-get-hvac-financing-with-bad-credit/", date=DATE,
    crumbs=[HOME, BLOG, ("HVAC financing with bad credit", "/blog/how-to-get-hvac-financing-with-bad-credit/")],
    eyebrow="Homeowner guide", h1="How to get HVAC financing with bad credit: a realistic plan",
    title="How to Get HVAC Financing With Bad Credit: A Realistic Plan",
    meta="AC died and your credit isn't great? A step-by-step plan: shrink the amount, shop with soft pulls, add a co-applicant, and avoid bad offers.",
    answer="You can often get HVAC financing with bad credit, but expect fewer offers and higher APRs. The best results come from shrinking the amount you need (repair if it makes sense, right-size the system, get competing quotes), checking options with lenders that use a soft credit pull first, adding a creditworthy co-applicant if you have one, and refusing any offer that promises guaranteed approval or hides the APR.",
    money_page=("HVAC financing with bad credit", "/hvac-financing/bad-credit-hvac-financing/"), project="HVAC (AC, furnace, heat pump)",
    sections=[
        ("What \"bad credit\" means to an HVAC lender", """<p>Lenders don't share one definition. Broadly, scores in the mid-600s and above tend to see the most options, scores in the high 500s to low 600s see fewer and more expensive ones, and scores lower than that get very limited choices. But the score is only part of the picture. Lenders also look at income, how much of it already goes to debt, recent late payments, collections and how long your credit history is.</p>
<p>It also helps to know what lenders are protecting against. With an unsecured HVAC loan there's no collateral the lender can easily recover, so they lean on signs that you'll keep paying: stable income, a history of paying recent bills on time and a debt load that leaves room in the budget. A score dragged down by one old medical collection reads very differently from one dragged down by several recent missed payments.</p>
<p>That's good news, because some of those factors are in your control even when the AC is out in July. A lender who sees steady income and a manageable debt load may approve a smaller amount that another lender would decline at a larger one.</p>"""),
        ("Step 1: Shrink the number before you apply", """<p>The single most effective move with lower credit is to need less money. Smaller amounts are easier to approve and cheaper to carry.</p>
<ul><li><strong>Confirm it's a replacement.</strong> A failed capacitor, contactor or blower motor is a repair measured in hundreds of dollars, not thousands. Ask the technician to show you the failed part and the reason replacement is recommended.</li>
<li><strong>Get two or three quotes on the same scope.</strong> Prices for the same tonnage and efficiency can vary a lot between companies.</li>
<li><strong>Right-size the system.</strong> Ask whether a load calculation (often called a Manual J) was done. An oversized system costs more up front and can run worse.</li>
<li><strong>Consider the efficiency step.</strong> Higher-efficiency units cost more. Sometimes that pays back on energy bills; sometimes a standard-efficiency unit is the better financial choice for you.</li>
<li><strong>Look for utility rebates.</strong> Many utilities offer rebates on qualifying equipment, which lowers the amount you finance.</li></ul>"""),
        ("Step 2: Check your credit before a lender does", """<p>Pull your credit reports from the three bureaus through the official free site, AnnualCreditReport.com, and look for errors: accounts that aren't yours, late payments reported incorrectly, paid collections still showing a balance. Disputing a clear error won't fix your score overnight, but it's worth starting now.</p>
<p>Also check your credit card balances. If you can pay a card down below 30% of its limit before applying, your utilization improves and that can help at the next reporting date.</p>"""),
        ("Step 3: Shop with soft pulls first", """<p>A soft inquiry lets a lender show you whether you're likely to qualify, and at roughly what rate, without affecting your score. A hard inquiry happens when you formally apply. With lower credit, avoid scattering hard applications across many lenders in a panic; each one can nudge your score down and make the next approval harder.</p>
<p>When you submit a request through AL Elite, we route it to lenders in our network who fund HVAC work in your state and consider a wider range of credit profiles, and we tell you before you proceed whether each one starts with a soft or hard inquiry. Nobody can promise approval, and we won't.</p>"""),
        ("Step 4: Strengthen the application", """<ul><li><strong>Add a co-applicant.</strong> A spouse or family member with stronger credit and income on the application can open better offers. They become equally responsible for the debt, so be sure they understand that.</li>
<li><strong>Show all your income.</strong> Part-time work, benefits and regular side income can count if you can document them.</li>
<li><strong>Offer a down payment.</strong> Even a few hundred dollars toward the job reduces the amount financed and signals commitment.</li>
<li><strong>Choose a realistic term.</strong> A term that keeps the payment comfortable reduces the lender's worry that you'll fall behind.</li>
<li><strong>Have documents ready.</strong> Recent pay stubs or bank statements, ID and the contractor's written quote. Complete applications get decisions faster, which matters when the house is 90 degrees.</li></ul>"""),
        ("What the payments can look like", f"""<p>Lower credit usually means a higher APR, so look at the total, not only the monthly figure. Here's an $8,000 AC replacement over 60 months at three example rates.</p>
<div class='tbl'><table><thead><tr><th>Example APR</th><th class='num'>Monthly</th><th class='num'>Total interest</th></tr></thead><tbody>
{''.join(f"<tr><td>{a:.2f}%</td><td class='num'>{pm(8000, a, 60)}</td><td class='num'>{ti(8000, a, 60)}</td></tr>" for a in (17.99, 24.99, 35.99))}
</tbody></table></div><p class='cap'>Illustrative only, standard amortization, no fees. Not offers. Many states cap consumer loan APRs; lenders must disclose the APR before you sign.</p>
<p>If the only offer you can get is at the top of that range, compare it with a repair that buys a season, a smaller system, or waiting a few months while you improve your profile, if the household can safely manage that.</p>"""),
        ("A worked example: the July breakdown", f"""<p>Imagine a homeowner with a 590 credit score whose 17-year-old AC fails in July. The first quote is $11,800 for a high-efficiency system, and the contractor's financing comes back declined.</p>
<p>She asks for a second and third quote on a standard-efficiency system sized from a load calculation. The middle quote is $8,200 with a 10-year parts warranty. A utility rebate takes off a few hundred dollars more. Her adult son, who has stronger credit, agrees to be co-applicant. She puts $500 down from savings.</p>
<p>The amount she needs drops from $11,800 to roughly $7,400. At an illustrative 19.99% APR over 60 months, that's about {pm(7400, 19.99, 60)} a month, compared with about {pm(11800, 24.99, 60)} for the original quote at a higher rate, if she had been approved at all. Nothing about her score changed. What changed was the size and strength of the request.</p>"""),
        ("Use the loan to rebuild your credit", """<p>An installment loan you pay on time every month is one of the steadier ways to improve a credit profile. A few habits make the most of it:</p>
<ul><li><strong>Set up autopay</strong> for at least the minimum, so a busy month never becomes a late payment.</li>
<li><strong>Pay a little extra when you can.</strong> It shortens the loan and cuts interest, especially at higher APRs.</li>
<li><strong>Keep card balances low</strong> while the loan is open. New card debt can undo the progress.</li>
<li><strong>Check back in 12 months.</strong> If your score has risen meaningfully, refinancing a high-APR HVAC loan into a cheaper one may be possible. Check for prepayment penalties first.</li></ul>"""),
        ("Offers to walk away from", """<ul><li><strong>"Guaranteed approval" or "no credit check" on a large amount.</strong> Responsible lenders assess ability to repay. Promises like these often come with very high costs.</li>
<li><strong>No clear APR.</strong> If you can't see the APR, fees and total repaid in writing before signing, don't sign.</li>
<li><strong>Rent-to-own or lease-to-own HVAC</strong> where the total of payments is far above the system's price. Ask for the total cost and compare.</li>
<li><strong>Upfront fees to "secure" a loan.</strong> Legitimate lenders don't ask you to pay before you're approved.</li>
<li><strong>Pressure to sign today.</strong> A good contractor will hold a quote for a day while you check options.</li></ul>"""),
        ("Other ways to cover an urgent HVAC bill", """<p>If financing doesn't come together, there are still options worth a call: local weatherization and energy assistance programs (often run through community action agencies) that help eligible households with heating and cooling, utility payment or repair programs, manufacturer warranty claims if the failed component is still covered, and payment plans offered directly by the HVAC company. For heating emergencies in winter, ask your utility what assistance is available in your area.</p>"""),
    ],
    faqs=[
        ("Can I finance an AC unit with a 550 credit score?", "Possibly, but offers will be limited and APRs high. Reducing the amount, adding a co-applicant with stronger credit and showing steady income improve your chances. No legitimate lender can guarantee approval."),
        ("Do HVAC companies offer financing for bad credit?", "Many HVAC companies work with lender partners, and some partners consider lower scores, sometimes with a second-look lender if the first declines. Compare the APR and total cost with an independent offer before signing."),
        ("Will applying for HVAC financing hurt my credit?", "Checking options with a soft inquiry doesn't affect your score. A formal application usually triggers a hard inquiry, which can lower your score slightly for a short time."),
        ("Is it better to repair or replace a failing AC with bad credit?", "If a reputable technician says a repair is safe and reasonably priced, repairing can buy time to improve your credit before a replacement. If the system is very old, uses phased-out refrigerant or keeps failing, replacement may be the better long-term value."),
        ("What is a co-applicant and should I use one?", "A co-applicant applies with you and shares full responsibility for repaying the loan. It can improve your offers if their credit and income are stronger, but missed payments affect both of you."),
    ],
    related=[("HVAC financing with bad credit", "/hvac-financing/bad-credit-hvac-financing/"), ("Furnace and AC replacement financing", "/blog/furnace-and-ac-replacement-financing/"), ("HVAC financing", "/hvac-financing/"), ("Water heater financing", "/water-heater-financing/")],
)


# --------------------------------------------------------------------------- 4
FURNACE = dict(
    path="/blog/furnace-and-ac-replacement-financing/", date=DATE,
    crumbs=[HOME, BLOG, ("Furnace and AC replacement financing", "/blog/furnace-and-ac-replacement-financing/")],
    eyebrow="Homeowner guide", h1="Furnace and AC replacement financing: what to expect",
    title="Furnace & AC Replacement Financing: Costs, Options, Payments",
    meta="Replacing a furnace, AC or heat pump? What drives the price, how furnace financing works, example payments and questions to ask first.",
    answer=f"Furnace and AC replacements are usually financed with an unsecured installment loan, either through the HVAC contractor's lender partner or an independent lender, over three to ten years. As an illustration, a $7,000 furnace at 11.99% APR is about {pm(7000, 11.99, 60)} a month over five years, and a $14,000 full system is about {pm(14000, 11.99, 84)} a month over seven. Approval and rate depend on your credit and income.",
    money_page=("HVAC financing", "/hvac-financing/"), project="HVAC (AC, furnace, heat pump)",
    sections=[
        ("What you're actually paying for", """<p>"A new furnace" or "a new AC" can mean very different jobs. Before financing, make sure you know which one you're quoting:</p>
<ul><li><strong>Furnace only.</strong> Replacing a gas or electric furnace, keeping the existing outdoor AC unit.</li>
<li><strong>AC condenser and coil.</strong> The outdoor unit and the matching indoor evaporator coil. Replacing only the outdoor unit with a mismatched coil can hurt efficiency and void warranties.</li>
<li><strong>Full split system.</strong> Furnace or air handler, coil and outdoor unit together, often the best value if both halves are old.</li>
<li><strong>Heat pump.</strong> Heats and cools with one outdoor unit, sometimes paired with a gas furnace as backup (a dual-fuel system).</li>
<li><strong>Ductwork.</strong> Leaky or undersized ducts add cost but can be the difference between a system that works and one that doesn't.</li></ul>"""),
        ("What drives the price", """<p>HVAC quotes vary with system size (tonnage or BTUs), efficiency rating, brand and warranty, whether ductwork, electrical or gas line changes are needed, permits, how hard the equipment is to reach, and local labor rates. A furnace alone is often several thousand dollars; a full system replacement is commonly well into five figures. Getting two or three quotes on the same scope is the best way to understand your local price.</p>
<p>Ask each contractor for an itemized quote that lists the model numbers, efficiency ratings, warranty terms (parts and labor, and for how long), what's included for ducts and thermostats, and whether permits and haul-away are in the price. Model numbers let you compare like for like.</p>"""),
        ("Repair or replace?", """<p>A common rule of thumb is to compare the repair cost with the age of the system: if the system is near the end of its expected life and the repair is a large fraction of a replacement, replacement often makes more sense. Other signs it's time: repeated breakdowns, an AC that uses phased-out R-22 refrigerant, a cracked heat exchanger on a furnace (a safety issue, so take it seriously), or energy bills climbing while comfort falls.</p>
<p>If a repair is reasonable and safe, it can be the cheapest way to get through a season and plan the replacement properly, with time to compare financing.</p>"""),
        ("How furnace and AC financing works", """<p>Most HVAC financing is a fixed-rate installment loan: you borrow the cost of the job, the lender pays the contractor when the work is done, and you repay in equal monthly payments. There are three common routes.</p>
<ul><li><strong>Contractor lender programs.</strong> The HVAC company offers financing at the quote, often through one or two lender partners. Convenient, sometimes promotional. Ask about deferred interest and dealer fees.</li>
<li><strong>Independent personal loans.</strong> You apply directly with a lender and pay the contractor yourself. Good for comparing against the contractor's offer.</li>
<li><strong>Home equity.</strong> A HELOC or home equity loan can be cheaper but is slower and secured by the home. Rarely the right tool for an emergency replacement.</li></ul>
<p>Some utilities also run on-bill financing programs for qualifying efficient equipment. Ask your utility whether one exists in your area.</p>"""),
        ("Example monthly payments", f"""<p>To see how amount and APR interact, here are illustrative payments for three common job sizes.</p>{payment_table((5000, 9000, 15000), aprs=(8.99, 13.99, 19.99), terms=(36, 60, 84, 120))}
<p>If your credit is on the lower side, our guide to <a href="/blog/how-to-get-hvac-financing-with-bad-credit/">getting HVAC financing with bad credit</a> covers how to shrink the amount and improve your offers.</p>"""),
        ("Efficiency ratings in plain English", """<p>Quotes are full of acronyms, and they matter because higher ratings cost more up front. The ones you'll see:</p>
<ul><li><strong>SEER2</strong> measures cooling efficiency for air conditioners and heat pumps under the testing standard that took effect in 2023. Higher is more efficient. Minimum required levels vary by region of the country.</li>
<li><strong>AFUE</strong> is the share of fuel a furnace turns into heat. An 80% AFUE furnace wastes about a fifth of its fuel up the flue; 95% and higher units are condensing furnaces that need different venting.</li>
<li><strong>HSPF2</strong> measures heat pump heating efficiency. In colder climates, ask about cold-climate heat pumps and how well the unit performs at low outdoor temperatures.</li></ul>
<p>The financing question is whether the extra cost of a higher rating pays back over the years you'll own the system. In a mild climate with modest bills, the payback on top-tier efficiency can be long. In a hot or cold climate with high usage, it can be meaningful. Ask the contractor to estimate annual operating cost for each option so you can compare total cost, not just the sticker price.</p>"""),
        ("How promotional plans and dealer fees work", f"""<p>Many HVAC companies advertise offers like "0% for 18 months" or very low payments. They can be good deals, but understand the mechanics.</p>
<p><strong>Deferred interest</strong> plans charge interest from day one in the background. If the full balance isn't paid by the end of the promotion, all of that interest is added at once. <strong>Waived interest</strong> plans genuinely charge nothing during the promotion. The wording in the agreement tells you which one you have.</p>
<p>Low-rate offers are often paid for by a <strong>dealer fee</strong>, a percentage of the loan the lender charges the contractor. Some contractors absorb it; others build it into the price. A fair question is: "What would the price be if I paid cash or used my own lender?" If the answer is several hundred dollars lower, compare that against the promotional offer. A $10,000 job at an illustrative 9.99% over 60 months costs about {pm(10000, 9.99, 60)} a month; a "0%" offer on a price inflated to $10,800 over the same term costs {money(10800 / 60, False)} a month, so the math isn't always what the advertisement suggests.</p>"""),
        ("Questions to ask before you sign", """<ol><li>What is the APR, and what will I repay in total?</li>
<li>Is any promotional rate deferred interest, and what happens if I don't pay the balance in time?</li>
<li>Is there a dealer fee, and is it built into the price I'm being quoted? Would the price be lower if I paid another way?</li>
<li>Is there a prepayment penalty?</li>
<li>When does the lender pay the contractor, and when does my first payment start?</li>
<li>Does the quote include permits, a load calculation and haul-away of the old equipment?</li>
<li>Who handles warranty registration, and what does the labor warranty cover?</li></ol>"""),
        ("Timing your replacement", """<p>Emergency replacements happen in the worst weather, when contractors are busiest. If your system is old and you can plan ahead, spring and fall are often easier for scheduling, and you have time to compare quotes and financing calmly. Planning ahead also lets you check your credit, pay down card balances and gather income documents before you apply.</p>
<p>Even in an emergency, you usually have a little room. Many contractors can install a temporary heater or make a short-term repair to keep the house safe for a few days. Use that window to get a second quote and check one independent financing option against the contractor's plan. A day or two of comparison on a five-figure purchase is time well spent, and a good contractor will understand.</p>
<p>When you're ready, our <a href="/hvac-financing/">HVAC financing</a> page explains what lenders look for and shows more example payments. One request through AL Elite reaches lenders who fund HVAC work in your state.</p>"""),
    ],
    faqs=[
        ("Can you finance a furnace replacement?", f"Yes. Furnace replacements are commonly financed with installment loans through the HVAC contractor or an independent lender. For example, $7,000 at an illustrative 11.99% APR is about {pm(7000, 11.99, 60)} a month over 60 months."),
        ("How long are furnace and AC loans?", "Terms commonly run from 3 to 10 years, and some programs go longer. A longer term lowers the payment but increases total interest."),
        ("Is it cheaper to replace the furnace and AC together?", "Often, yes. Replacing both at once can save on labor and ensure the indoor and outdoor components are matched. If one is fairly new, replacing only the failed half can make sense."),
        ("What credit score do I need for HVAC financing?", "Each lender sets its own criteria. Stronger credit generally means more choices and lower APRs; some lenders consider lower scores at higher rates or with a co-applicant."),
        ("Should I choose a heat pump instead of a furnace and AC?", "It depends on your climate, fuel costs and existing equipment. Heat pumps can heat and cool efficiently with one system, and cold-climate models work in much lower temperatures than older units. In very cold areas, a dual-fuel setup with a gas furnace backup is common. Ask for operating cost estimates for each option."),
        ("Are there rebates for new heat pumps or furnaces?", "Many utilities and some states offer rebates on qualifying efficient equipment. Federal tax incentives have changed in recent years, so check current IRS guidance or ask a tax professional."),
    ],
    related=[("HVAC financing", "/hvac-financing/"), ("HVAC financing with bad credit (guide)", "/blog/how-to-get-hvac-financing-with-bad-credit/"), ("Water heater financing", "/water-heater-financing/"), ("Generator financing", "/generator-financing/")],
)

ARTICLES_A = [HAIL, MONTHLY, HVAC_BAD, FURNACE]
