"""Contractor-side pages: offer customer financing (B2B pillar + trade spokes), business capital (pillar + spokes), tools."""
from common import *

HOME = ("Home", "/")
FC = ("For contractors", "/for-contractors/")
CBL = ("Contractor business loans", "/contractor-business-loans/")

B2B_HOW = dict(
    how_1="Your trade, where you operate, roughly how many jobs a month you quote, and whether you need capital, a customer-financing program or both. No credit pull.",
    how_2="Your request goes to lenders in our network who work with contractors in your trade and state. For customer financing, we set up a program; for capital, we match you with business lenders.",
    how_3="Rates, terms and the decision come from the lender. For customer-financing programs, there's no cost to join and no obligation to use it on every job.",
)

def biz_qualify(extra=None):
    return [
        "<strong>Time in business.</strong> Many business lenders want at least one to two years of operating history; some products accept less.",
        "<strong>Revenue.</strong> Annual revenue thresholds vary by lender and product. Bank statements are the usual proof.",
        "<strong>Business and personal credit.</strong> Smaller contractors are often underwritten partly on the owner's personal credit.",
        "<strong>Licensing and insurance.</strong> A current contractor's license (where required) and general liability insurance.",
        "<strong>State.</strong> Lender availability and product rules vary by state. We match you with lenders who serve your location.",
    ] + (extra or [])

def b2b_faqs(topic):
    return [
        (f"Is AL Elite a lender for {topic}?", f"No. AL Elite is a matching service. We route your request to business lenders in our network who fund {topic}, and they set the terms and make the decision. Lenders pay us for introductions; you don't."),
        ("Does requesting options affect my business or personal credit?", "Submitting a request to AL Elite does not pull credit. Business lenders typically run a soft inquiry to pre-qualify and a hard inquiry at formal application. We tell you each lender's approach before you proceed."),
    ]

# ---------------------------------------------------------------- Offer customer financing (pillar)
FOR_CONTRACTORS = dict(
    path="/for-contractors/", crumbs=[HOME, FC],
    eyebrow="For contractors", h1="Contractor financing: offer your customers a way to pay monthly, and close the jobs you're losing",
    title="Contractor Financing | Offer Customer Financing & Close More Jobs | AL Elite",
    meta="Contractor financing for roofing, HVAC, plumbing, remodeling and solar: offer financing to your customers through AL Elite's lender network, get paid when the job is done, no cost to join. Plus business capital when you need it.",
    answer="Contractor financing, in the sense most contractors mean it, is a program that lets your customers pay for the job monthly through a lender while you get paid in full when the work is done. AL Elite sets contractors up with a customer-financing program drawn from our lender network, with lenders for a range of customer credit profiles. Separately, we match contractors who need capital for their own business with business lenders.",
    cta_points=["No cost to join, no monthly minimums", "Lenders for prime and near-prime customers", "Get paid at completion, not in instalments"],
    cta_h="Become a partner contractor", cta_btn="Apply to partner", role="contractor", need="Offer financing to my customers", how_noun="contractors", **B2B_HOW,
    intro="""<p>Every contractor has heard it: "We love the quote, we just can't do it right now." Sometimes that's true. More often it means the customer can't write a cheque for the full amount this month, and nobody offered them a way to pay $300 a month instead. The jobs that walk at that moment are the ones a financing program brings back.</p>""",
    sections=[
        ("How offering financing changes the sales conversation", """<ul>
<li><strong>You quote a monthly payment, not just a total.</strong> A $14,000 roof is a hard number. "About $280 a month" is a decision most households can make at the table.</li>
<li><strong>You stop discounting to close.</strong> Contractors without financing often cut price to get a yes. With financing, the customer can afford the full-scope job, including the upgrades.</li>
<li><strong>You get paid on completion.</strong> The lender funds the job; you're not carrying the receivable or chasing instalments.</li>
<li><strong>You win the storm season.</strong> After hail or a hurricane, every homeowner needs a roof and few have the cash. The contractor who can finance it books the job.</li></ul>
<p>Our guide <a href="/blog/how-to-offer-financing-to-customers/">how to offer financing to your customers</a> goes through the setup, the pitch and the compliance basics step by step.</p>"""),
        ("What the AL Elite partner program includes", """<ul>
<li><strong>A customer-financing link and QR code</strong> you can put on quotes, invoices and your website.</li>
<li><strong>In-home payment estimates</strong> so your reps can show a monthly figure before the customer applies.</li>
<li><strong>Multiple lenders, including second-look.</strong> A single-lender program declines too many customers. Ours routes to lenders for a range of credit profiles.</li>
<li><strong>A partner profile page and badge</strong> ("Financing available through AL Elite") that links to your business from our site, including on our <a href="/locations/">city pages</a> in your market.</li>
<li><strong>Clear rules on what you can and can't say.</strong> You never quote rates you don't have in writing from a lender, and you never offer to absorb insurance deductibles. We vet partners on this.</li></ul>
<div class="verify">Before publishing: confirm the exact partner-program terms (fees, dealer-fee options, funding timing, which lenders are second-look) with the lender partners and legal, and replace this list with the contracted terms.</div>"""),
        ("Financing programs by trade", """<p>The pitch and the ticket size differ by trade, so we've written a page for each: <a href="/for-contractors/roofing/">financing for roofing companies</a>, <a href="/for-contractors/hvac/">HVAC financing for contractors</a>, <a href="/for-contractors/remodeling/">home improvement financing for contractors</a> and <a href="/for-contractors/solar/">solar financing for installers</a>.</p>"""),
        ("Need capital for the business instead?", """<p>Customer financing solves the customer's cash-flow problem. If the problem is yours (payroll before the draw, an excavator, a dump truck, a slow-paying GC), see <a href="/contractor-business-loans/">contractor business loans</a>. Many partners use both.</p>"""),
    ],
    options=[
        ("AL Elite partner program", "Multi-lender customer financing from our network, with a partner profile and badge.", "Contractors who want more approvals and a program that costs nothing to join.", "You'll need to follow the compliance rules; we enforce them."),
        ("Single-lender dealer program", "Financing offered through one consumer lender or a manufacturer's program.", "Simplicity, one relationship.", "One credit box means more declines, and some charge the contractor a dealer fee per job."),
        ("In-house instalment plans", "You carry the receivable and the customer pays you over time.", "Very small jobs with trusted repeat customers.", "You're now a lender: licensing, collections risk and tied-up cash."),
        ("Referring customers to their own lender", "You hand the customer a list of lenders and let them sort it out.", "Nothing to set up.", "Most customers won't follow through, and you lose the job to whoever offers financing at the table."),
    ],
    options_h2="Ways contractors offer financing, compared",
    amounts=None,
    qualify=biz_qualify(["<strong>Customer reviews and complaint history.</strong> We check these before accepting partners; lenders do too."]),
    qualify_h2="Who can become a partner contractor", qualify_intro="We accept licensed, insured contractors in good standing. Lenders in the program also have their own requirements. What matters most:",
    faqs=[
        ("How do I offer financing to my customers?", "Join a financing program through a lender or a marketplace like AL Elite, put the financing option on your quotes and website, and train your reps to present a monthly payment alongside the total. The customer applies with the lender; when approved, the lender pays you at completion. Our <a href='/blog/how-to-offer-financing-to-customers/'>step-by-step guide</a> covers setup and compliance."),
        ("What does customer financing cost the contractor?", "It depends on the program. Some lenders charge a dealer fee per funded job, especially for promotional-rate offers; standard-rate loans often carry no contractor fee. AL Elite's partner program is free to join. We're paid by lenders for introductions. Confirm per-job fees with us before you present promotional offers."),
        ("What if my customer has bad credit?", "A multi-lender program routes declined applications to a second-look lender who considers lower scores at a higher APR. No program approves everyone, and you must never tell a customer approval is guaranteed."),
        ("How quickly does the lender pay the contractor?", "Typically at job completion once the customer signs off, with timing set by the lender. We tell you each lender's funding process when you join."),
        ("Can I offer financing if I'm a small, one-truck operation?", "Usually, yes, if you're licensed and insured. Some lenders have minimum revenue or time-in-business requirements; we'll match you with programs that fit."),
    ] + b2b_faqs("contractor financing programs"),
    related=[("Financing for roofing companies", "/for-contractors/roofing/"), ("HVAC financing for contractors", "/for-contractors/hvac/"), ("Home improvement financing for contractors", "/for-contractors/remodeling/"), ("Solar financing for installers", "/for-contractors/solar/"), ("Contractor business loans", "/contractor-business-loans/"), ("How to offer financing to your customers", "/blog/how-to-offer-financing-to-customers/"), ("Best contractor financing companies compared", "/blog/best-contractor-financing-companies/")],
    service_name="Customer financing programs for contractors", service_type="Business financing matching", audience="Contractors and home service businesses",
)

def trade_b2b(slug, name, h1, title, meta, answer, sections, faqs, related, cta_points):
    return dict(
        path=f"/for-contractors/{slug}/", crumbs=[HOME, FC, (name, f"/for-contractors/{slug}/")], eyebrow=name, h1=h1, title=title, meta=meta, answer=answer,
        cta_points=cta_points, cta_h="Become a partner contractor", cta_btn="Apply to partner", role="contractor", need="Offer financing to my customers", how_noun=name.lower(), **B2B_HOW,
        sections=sections, options=None, amounts=None, qualify=biz_qualify(), qualify_h2="Who can join", faqs=faqs + b2b_faqs(name.lower()), related=related,
        service_name=name, service_type="Business financing matching", audience="Contractors",
    )

FC_ROOFING = trade_b2b("roofing", "Financing for roofing companies",
    "Financing for roofing companies: win the storm season with customer financing",
    "Financing for Roofing Companies | Customer Financing for Roofers | AL Elite",
    "Financing for roofing companies: offer customer financing on every roof quote, cover deductibles and upgrades legally, get paid at completion, and get business capital for crews and equipment. AL Elite's roofing contractor financing program.",
    "Financing for roofing companies works on two levels: a customer-financing program so homeowners can pay for a roof monthly (you're paid at completion), and business capital for the roofer's own crews, trucks and materials. AL Elite sets roofers up with a multi-lender customer program and matches them with business lenders. Roofing is our most active trade.",
    [("Why roofing is the trade that needs financing most", """<p>Roofs are expensive, urgent and often unplanned. A homeowner with a hail-damaged roof has a deadline from the insurer and a deductible that may run into thousands, plus upgrades (impact-resistant shingles, new decking, gutters) the claim won't cover. The roofer who can say "the deductible and the upgrades come to about $190 a month" books the job. The roofer who can't loses it to the one who can.</p><p>Our homeowner-side <a href="/roof-financing/">roof financing</a> page ranks for the searches your customers make. Partner roofers are listed on it and on the <a href="/locations/">city pages</a> for their markets.</p>"""),
     ("Deductibles: what you can and can't do", """<p>Offering to waive, absorb or "work with" a homeowner's insurance deductible is illegal in a growing list of states and is grounds for removal from our program everywhere. What you can do is offer legitimate financing for the deductible and any non-covered upgrades, with the homeowner paying the deductible in full as the policy requires. That's a clean, lawful pitch, and it closes.</p>"""),
     ("Business capital for roofers", """<p>Roofing cash flow is brutal: materials up front, crews weekly, insurance checks whenever the adjuster gets to it. Partners use <a href="/contractor-business-loans/working-capital/">working capital</a> for storm-season ramp-up, <a href="/contractor-business-loans/dump-truck-financing/">dump truck financing</a> for debris hauling, and <a href="/contractor-business-loans/equipment-financing/">equipment financing</a> for lifts and shingle elevators. See <a href="/contractor-business-loans/roofing/">roofing business loans</a>.</p>""")],
    [("How do roofing companies offer financing?", "Through a lender program or a marketplace like AL Elite. The roofer presents a monthly payment with the quote; the homeowner applies with the lender; the lender pays the roofer at completion. Our <a href='/blog/how-to-offer-financing-to-customers/'>guide</a> covers the steps."),
     ("Can I finance a customer's insurance deductible?", "You can offer the customer legitimate third-party financing for the deductible and non-covered work. You cannot waive, absorb or rebate the deductible; that's illegal in many states and prohibited in our program."),
     ("Do roofing financing programs cost the roofer anything?", "Some lenders charge a dealer fee per funded job for promotional-rate offers; standard-rate loans often carry no fee. AL Elite's program is free to join. Confirm per-job fees before presenting promotional offers.")],
    [("Offer customer financing (main page)", "/for-contractors/"), ("Roofing business loans", "/contractor-business-loans/roofing/"), ("Dump truck financing", "/contractor-business-loans/dump-truck-financing/"), ("Homeowner roof financing page", "/roof-financing/"), ("Roofing companies that offer financing (homeowner guide)", "/blog/roofing-companies-that-offer-financing/")],
    ["Storm-season customer financing", "Deductible-compliant pitch", "Capital for crews and trucks"])

FC_HVAC = trade_b2b("hvac", "HVAC financing for contractors",
    "HVAC financing for contractors: turn 'we'll think about it' into an install date",
    "HVAC Financing for Contractors | Offer Customer Financing on HVAC Jobs | AL Elite",
    "HVAC financing for contractors: offer customer financing on AC, furnace and heat pump replacements, with second-look lenders for lower-credit customers, get paid at install, and get capital for vans, inventory and payroll. AL Elite's HVAC contractor program.",
    "HVAC financing for contractors is a customer-financing program sized for emergency replacements: the customer applies in minutes, often from the kitchen table, and the contractor is paid at install. Because HVAC customers skew urgent and credit-varied, a multi-lender program with a second-look option matters more here than in any other trade. AL Elite sets HVAC contractors up with that program and matches them with business lenders for the shop.",
    [("The HVAC sale is a same-day sale", """<p>When the AC dies in July the customer wants it fixed today, not after they shop for a HELOC. A contractor who can show "a new system for about $165 a month" and get a decision in minutes wins the job. A contractor who hands over a brochure for a bank loses it to the one who can. Our program's lenders are chosen for decision speed as much as rate.</p>"""),
     ("Second-look lenders are the whole game in HVAC", """<p>HVAC customers aren't filtered by credit the way kitchen-remodel customers are; everyone's furnace fails eventually. A single-lender program will decline a large share of your emergency customers. Our program routes a decline to a second-look lender automatically. You must never tell a customer approval is guaranteed, but you can tell them, truthfully, that there's more than one lender looking.</p>"""),
     ("Capital for the HVAC business", """<p>Partners use <a href="/contractor-business-loans/working-capital/">working capital</a> for pre-season inventory, <a href="/contractor-business-loans/equipment-financing/">equipment financing</a> for vans and recovery machines, and <a href="/contractor-business-loans/line-of-credit/">lines of credit</a> for the shoulder seasons. See <a href="/contractor-business-loans/hvac/">HVAC business loans</a>.</p>""")],
    [("How do HVAC contractors offer financing?", "Through a lender program or marketplace. Present a monthly payment with the quote, let the customer apply on their phone, and get paid at install. AL Elite's program includes multiple lenders and a second-look option."),
     ("What about customers with bad credit?", "Route them to a second-look lender rather than losing the job. Our program does that automatically. Approval is never guaranteed and you must not say it is. See our homeowner page on <a href='/hvac-financing/bad-credit-hvac-financing/'>HVAC financing with bad credit</a> for what customers are reading."),
     ("Can I offer promotional 'same as cash' plans?", "Some lenders in the program offer promotional-rate plans, which typically carry a dealer fee. Decide per job whether the fee is worth the close. Disclose the terms exactly as the lender states them.")],
    [("Offer customer financing (main page)", "/for-contractors/"), ("HVAC business loans", "/contractor-business-loans/hvac/"), ("Homeowner HVAC financing page", "/hvac-financing/"), ("HVAC financing with bad credit (homeowner page)", "/hvac-financing/bad-credit-hvac-financing/")],
    ["Same-day decisions", "Second-look lenders built in", "Capital for vans and inventory"])

FC_REMODEL = trade_b2b("remodeling", "Home improvement financing for contractors",
    "Home improvement financing for contractors: bigger scopes, fewer price cuts",
    "Home Improvement Financing for Contractors | Remodeler Customer Financing | AL Elite",
    "Home improvement financing for contractors and remodelers: offer customer financing on kitchens, bathrooms, flooring, windows and siding, present full-scope quotes, get paid on completion. AL Elite's remodeler financing program.",
    "Home improvement financing for contractors is a customer-financing program for planned projects such as kitchens, bathrooms, windows, flooring and siding. The value for a remodeler is less about rescuing a lost sale and more about selling the full scope: customers who can pay monthly choose the better cabinets and keep the upgrades in. AL Elite sets remodelers up with a multi-lender program and matches them with business lenders.",
    [("Financing sells scope, not just the job", """<p>Remodel customers rarely walk away entirely; they trim. The quartz becomes laminate, the second bathroom waits. When the quote comes with a monthly figure, the trimming stops. Contractors in our program use financing to protect margin rather than to discount. The homeowner pages your customers read, <a href="/remodel-financing/kitchen/">kitchen</a> and <a href="/remodel-financing/bathroom/">bathroom remodel financing</a>, list partner contractors by market.</p>"""),
     ("Larger amounts, longer terms, more comparison", """<p>Remodel tickets run higher than repairs, and customers have time to compare your financing with a HELOC. Be straightforward: a fixed-rate loan through your program is faster and simpler; a HELOC may be cheaper for a very large job. Customers who feel you've been honest about that come back for the next project.</p>"""),
     ("Capital for remodeling businesses", """<p>Remodelers carry materials and subs for weeks before the final draw. <a href="/contractor-business-loans/working-capital/">Working capital</a> and <a href="/contractor-business-loans/line-of-credit/">lines of credit</a> are the common tools; see <a href="/contractor-business-loans/">contractor business loans</a>.</p>""")],
    [("How do remodelers offer financing?", "Through a lender program or marketplace like AL Elite. Present a monthly payment with every quote and let the customer apply before the final walkthrough. The lender pays you per the agreed schedule."),
     ("Does financing work for large remodels?", "Yes, within the lenders' amount limits. For very large projects the customer may also consider a home equity product. Our program covers the loan amounts typical of kitchen and bath remodels."),
     ("Can I use financing for windows, siding and flooring too?", "Yes. The program covers planned home improvement across trades, including windows, siding, flooring and exterior work.")],
    [("Offer customer financing (main page)", "/for-contractors/"), ("Kitchen remodel financing (homeowner page)", "/remodel-financing/kitchen/"), ("Bathroom remodel financing (homeowner page)", "/remodel-financing/bathroom/"), ("Window replacement financing (homeowner page)", "/window-financing/"), ("Contractor business loans", "/contractor-business-loans/")],
    ["Sell the full scope", "Kitchens, baths, windows, floors, siding", "Capital between draws"])

FC_SOLAR = trade_b2b("solar", "Solar financing for installers",
    "Solar financing for installers: loans, dealer fees and the price you can defend",
    "Solar Financing for Installers | Solar Loan Programs for Contractors | AL Elite",
    "Solar financing for installers: offer solar loans to customers, understand dealer fees and the cash-vs-financed price, present leases and PPAs honestly, and get capital for inventory and crews. AL Elite's solar installer program.",
    "Solar financing for installers is a customer-financing program built around solar loans, usually with longer terms than other home improvement lending. The industry's main compliance risk is the dealer fee: a low advertised APR funded by a fee that inflates the system price. AL Elite's program requires installers to show the cash price and the financed price side by side. We also match installers with business lenders for inventory and crews.",
    [("Dealer fees and the price you can defend", """<p>Solar customers are increasingly aware that a 2.99% loan often comes with a dealer fee built into the system price. Regulators are aware too. Our program's rule is simple: show the cash price and the financed price together, and let the customer choose. Installers who do this close fewer customers on a misleading rate and keep more of them past the first bill. The homeowner page your customers read, <a href="/solar-financing/">solar financing</a>, explains dealer fees in plain language.</p>"""),
     ("Loans, leases and PPAs", """<p>Loans mean the customer owns the system and claims any available tax credit. Leases and PPAs mean the installer or a third party owns it. If you offer more than one structure, present the ownership difference clearly. Tax credit rules change; never quote a credit as certain.</p>"""),
     ("Capital for solar installers", """<p>Solar businesses carry panels, inverters and racking ahead of install, and wait on utility interconnection to get paid. <a href="/contractor-business-loans/working-capital/">Working capital</a> and <a href="/contractor-business-loans/equipment-financing/">equipment financing</a> for trucks and lifts are the common requests. See <a href="/contractor-business-loans/">contractor business loans</a>.</p>""")],
    [("How do solar installers offer financing?", "Through solar loan lenders, lease/PPA providers or a marketplace like AL Elite. Present the financed price and the cash price together, let the customer apply, and get funded per the lender's schedule."),
     ("What is a dealer fee in solar?", "A fee the installer pays the lender to offer a below-market APR, typically passed into the system price. It's legal if disclosed, and the source of many complaints when it isn't. Our program requires side-by-side pricing."),
     ("Can I offer leases and PPAs through AL Elite?", "Our program is loan-focused. Installers who offer leases or PPAs through other providers can still use our loan program and business-capital matching.")],
    [("Offer customer financing (main page)", "/for-contractors/"), ("Solar financing (homeowner page)", "/solar-financing/"), ("Equipment financing", "/contractor-business-loans/equipment-financing/"), ("Contractor business loans", "/contractor-business-loans/")],
    ["Side-by-side pricing built in", "Longer-term solar loans", "Capital for inventory and crews"])

# ---------------------------------------------------------------- Business capital (pillar)
CBL_HUB = dict(
    path="/contractor-business-loans/", crumbs=[HOME, CBL],
    eyebrow="Contractor business loans", h1="Construction business loans: capital for contractors between the job and the draw",
    title="Construction Business Loans | Contractor Loans for Working Capital, Equipment & Trucks | AL Elite",
    meta="Construction business loans and contractor loans: working capital, equipment financing, dump truck loans, invoice factoring and lines of credit for roofing, HVAC, plumbing and landscaping contractors. AL Elite matches contractors with business lenders.",
    answer="Construction business loans are financing for the contractor's own business rather than the customer's project: working capital to cover payroll and materials before a draw, equipment and truck financing, invoice factoring to get paid on slow invoices, and lines of credit for seasonal swings. AL Elite matches contractors with business lenders who understand construction cash flow, and explains which product fits which problem.",
    cta_points=["Working capital, equipment, trucks, factoring, credit lines", "Lenders who understand construction cash flow", "No credit pull to compare"],
    cta_h="Get matched with a business lender", cta_btn="Get matched", role="contractor", need="Not sure yet",
    cards_h2="Financing by what you need it for", cards_eyebrow="Pick the problem",
    cards=[
        ("Cash flow", "Working capital for contractors", "Payroll, materials and subs before the job pays.", "/contractor-business-loans/working-capital/"),
        ("Equipment", "Construction equipment financing", "Excavators, lifts, skid steers, tools.", "/contractor-business-loans/equipment-financing/"),
        ("Vehicles", "Dump truck and work truck financing", "New and used trucks for hauling and crews.", "/contractor-business-loans/dump-truck-financing/"),
        ("Receivables", "Construction invoice factoring", "Turn unpaid invoices into cash this week.", "/contractor-business-loans/invoice-factoring/"),
        ("Flexibility", "Construction line of credit", "Draw as needed through the season.", "/contractor-business-loans/line-of-credit/"),
        ("By trade", "Roofing business loans", "Storm-season capital for roofers.", "/contractor-business-loans/roofing/"),
        ("By trade", "HVAC business loans", "Vans, inventory and payroll for HVAC shops.", "/contractor-business-loans/hvac/"),
        ("By trade", "Plumbing business loans", "Trucks, equipment and growth for plumbers.", "/contractor-business-loans/plumbing/"),
        ("By trade", "Landscaping business loans", "Mowers, trucks and seasonal capital.", "/contractor-business-loans/landscaping/"),
    ],
    prose="""<h2>Which product fits which problem</h2>
<div class='tbl'><table><thead><tr><th>The problem</th><th>The usual fix</th><th>Why</th></tr></thead><tbody>
<tr><td>Payroll is Friday, the draw is in three weeks</td><td><a href='/contractor-business-loans/working-capital/'>Working capital loan</a> or <a href='/contractor-business-loans/line-of-credit/'>line of credit</a></td><td>Short-term, fast, sized to the gap</td></tr>
<tr><td>A GC pays net-60 and you can't wait</td><td><a href='/contractor-business-loans/invoice-factoring/'>Invoice factoring</a></td><td>Advances against the invoice itself; the GC's credit matters more than yours</td></tr>
<tr><td>You need a $90,000 excavator</td><td><a href='/contractor-business-loans/equipment-financing/'>Equipment financing</a></td><td>The equipment is the collateral; longer terms match its life</td></tr>
<tr><td>The dump truck died mid-season</td><td><a href='/contractor-business-loans/dump-truck-financing/'>Truck financing</a></td><td>Vehicle lending with new and used options</td></tr>
<tr><td>Every spring you need cash and every fall you don't</td><td><a href='/contractor-business-loans/line-of-credit/'>Line of credit</a></td><td>Draw and repay as the season turns</td></tr>
<tr><td>Customers can't afford the job</td><td><a href='/for-contractors/'>Customer financing program</a></td><td>That's the customer's loan, not yours; you get paid at completion</td></tr></tbody></table></div>
<h2>What business lenders look at for contractors</h2>
<ul><li><strong>Time in business and revenue,</strong> usually from bank statements and tax returns.</li><li><strong>Owner's personal credit,</strong> for smaller businesses especially.</li><li><strong>Licensing and insurance.</strong></li><li><strong>Backlog and receivables,</strong> because they show the loan will be repaid from real work.</li><li><strong>Equipment or invoices as collateral,</strong> where the product uses them.</li></ul>
<h2>The use case we hear most</h2>
<p>"I've got $80,000 of work signed and I need $30,000 to cover crews and materials until the first draw." That's a working capital or line-of-credit request, and it's the single most common thing contractors ask us for. The <a href='/contractor-business-loans/working-capital/'>working capital</a> page walks through it, including how lenders size the amount.</p>""",
    faqs=[
        ("What is a construction business loan?", "Any financing for a contractor's own business: working capital, equipment and truck loans, invoice factoring, lines of credit or SBA-backed loans. It's distinct from customer financing, which is the homeowner's loan for the project."),
        ("How much can a contractor borrow?", "That depends on revenue, time in business, credit and the product. Equipment loans are sized to the equipment; factoring to the invoices; working capital to cash flow. Tell us what you need it for and we'll match you with lenders whose limits fit."),
        ("Can a new contractor get a business loan?", "It's harder with under a year in business, but not impossible: equipment financing (where the asset is collateral) and factoring (where the customer's credit matters) are the most accessible. Working capital loans usually want more history."),
        ("Does AL Elite charge contractors?", "No. Lenders pay us for introductions. Comparing options is free and does not pull your credit."),
    ],
    related=[("Offer customer financing", "/for-contractors/"), ("Equipment loan calculator", "/tools/equipment-loan-calculator/"), ("How to bid construction jobs (and price in financing)", "/blog/how-to-bid-construction-jobs/"), ("Best contractor financing companies compared", "/blog/best-contractor-financing-companies/")],
)

def cbl_page(slug, name, h1, title, meta, answer, sections, faqs, related, cta_points, amounts, aprs=(8.5, 12.5, 18.5), terms=(12, 24, 36, 60), pay_h2=None, need="Working capital", qualify_extra=None, options=None, options_h2=None):
    return dict(
        path=f"/contractor-business-loans/{slug}/", crumbs=[HOME, CBL, (name, f"/contractor-business-loans/{slug}/")], eyebrow=name, h1=h1, title=title, meta=meta, answer=answer,
        cta_points=cta_points, cta_h="Get matched with a business lender", cta_btn="Get matched", role="contractor", need=need, how_noun=name.lower(), **B2B_HOW,
        sections=sections, options=options, options_h2=options_h2, amounts=amounts, aprs=aprs, terms=terms, pay_h2=pay_h2 or f"Example payments on {name.lower()}",
        pay_intro="Illustrative arithmetic only. Business lenders quote their own rates, fees and structures (some use factor rates rather than APR; ask for the APR equivalent).",
        qualify=biz_qualify(qualify_extra), qualify_h2="What lenders look for", faqs=faqs + b2b_faqs(name.lower()), related=related,
        service_name=f"{name} matching", service_type="Business financing matching", audience="Contractors and construction businesses",
    )

CBL_WC = cbl_page("working-capital", "Working capital for contractors",
    "Working capital for contractors: bridging the gap between the job and the draw",
    "Working Capital for Contractors | Short-Term Contractor Loans & Subcontractor Financing | AL Elite",
    "Working capital for contractors and subcontractors: short-term loans and lines to cover payroll, materials and subs before the draw. How lenders size it, what it costs, factor rates vs APR. AL Elite matches contractors with business lenders.",
    "Working capital for contractors is short-term financing that covers payroll, materials and subcontractors between starting a job and getting paid for it. It's sized to the cash-flow gap, usually repaid within a year, and comes as a term loan, a line of credit or a merchant-cash-style advance. AL Elite matches contractors with business lenders who fund construction working capital and explains the cost differences, including factor rates.",
    [("The $80,000 problem", """<p>A contractor signs $80,000 of work. The first draw is 30 days out, materials are due now and the crew is paid Friday. The gap is maybe $25,000 to $35,000 for a month or two. That's a working capital request, and lenders size it from your bank statements, backlog and the payment terms on the signed contracts. Bring those three things and the conversation is short.</p>"""),
     ("Factor rates vs APR: read this before you sign", """<p>Some short-term business lenders quote a <strong>factor rate</strong> (for example 1.2) instead of an APR. A 1.2 factor on $30,000 means you repay $36,000. Over 12 months that looks like 20%; over 4 months the APR equivalent is far higher. Always ask for the APR equivalent and the total payback, and compare on that basis. Lenders in our network must provide it.</p>"""),
     ("Subcontractor financing", """<p>Subs have the same problem one layer down, with a GC who pays when the owner pays. Options include working capital against the signed subcontract, a <a href="/contractor-business-loans/line-of-credit/">line of credit</a> for recurring gaps, or <a href="/contractor-business-loans/invoice-factoring/">factoring</a> the invoice to the GC. Factoring is often the best fit for subs because the GC's credit, not yours, drives approval.</p>""")],
    [("How is working capital for contractors calculated?", "Lenders look at monthly revenue from bank statements, signed backlog and the payment terms on current contracts, then size a loan or line to the gap you can show. A clear statement like 'I need $30,000 for 60 days until the first draw on a signed $80,000 job' is exactly what they want to hear."),
     ("What's the difference between a working capital loan and a line of credit?", "A loan is a lump sum repaid on a schedule; a line is a limit you draw against and repay as needed, paying interest only on what's outstanding. Lines suit recurring seasonal gaps; loans suit a one-off need."),
     ("Can a subcontractor get working capital?", "Yes. Subcontractors use working capital loans, lines of credit and invoice factoring. Factoring is often easiest because approval rests on the GC's credit.")],
    [("Construction line of credit", "/contractor-business-loans/line-of-credit/"), ("Construction invoice factoring", "/contractor-business-loans/invoice-factoring/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["Sized to the gap, not a round number", "Factor-rate vs APR explained", "Options for subcontractors"],
    [15000, 30000, 60000], terms=(6, 12, 18, 24), qualify_extra=["<strong>Signed contracts and backlog.</strong> The clearest evidence the loan will be repaid from real work."])

CBL_EQUIP = cbl_page("equipment-financing", "Construction equipment financing",
    "Construction equipment financing: own the excavator, keep the cash",
    "Construction Equipment Financing | Excavator, Skid Steer & Lift Loans | AL Elite",
    "Construction equipment financing for excavators, skid steers, lifts, compressors and tools: loans vs leases, new vs used, terms matched to equipment life, example payments and lender requirements. AL Elite matches contractors with equipment lenders.",
    "Construction equipment financing is a loan or lease secured by the equipment itself, which is why it's often easier to get than unsecured business credit. Terms usually match the equipment's useful life, and both new and used machines can be financed. AL Elite matches contractors with equipment lenders and explains the loan-vs-lease decision, including the tax angle to raise with your accountant.",
    [("Loan or lease?", """<div class='compare'>
<div class='opt'><h3>Equipment loan</h3><p>You own the machine at the end. Payments build equity.</p><p class='pro'>Equipment you'll run for years.</p><p class='con'>Higher payment than a lease; you carry resale risk.</p></div>
<div class='opt'><h3>Fair-market-value lease</h3><p>Lower payments; return, renew or buy at market value at the end.</p><p class='pro'>Equipment that goes obsolete or that you need only for a contract.</p><p class='con'>You don't own it; total cost can be higher if you keep it.</p></div>
<div class='opt'><h3>$1 buyout lease</h3><p>Lease structure, but you own it for a dollar at the end.</p><p class='pro'>Ownership with lease-style paperwork.</p><p class='con'>Economically a loan; compare the rate as one.</p></div></div>
<p>Equipment purchases can have tax consequences (depreciation, expensing elections). That's a conversation for your accountant before you choose a structure.</p>"""),
     ("New vs used", """<p>Used equipment is financeable, usually at shorter terms and sometimes higher rates, with lenders capping age and hours. Have the serial number, hours and an inspection or auction report ready. Dealer financing on new machines can carry promotional rates; compare against an independent lender's offer, as with any dealer program.</p>"""),
     ("Try the numbers", """<p>The <a href="/tools/equipment-loan-calculator/">equipment loan calculator</a> shows the payment at different terms and rates, plus total interest, so you can compare a 36-month loan against a 60-month one before talking to a lender.</p>""")],
    [("Can I finance used construction equipment?", "Yes. Most equipment lenders finance used machines within age and hours limits, often at shorter terms. Bring the serial number, hours and condition report."),
     ("Is it better to lease or buy construction equipment?", "Buy (loan) what you'll run for years; lease what goes obsolete or is contract-specific. Compare total cost over the period you'll keep it, and ask your accountant about tax treatment."),
     ("What credit do I need for equipment financing?", "Because the equipment is collateral, requirements are often more forgiving than for unsecured loans. Lenders still look at business history and the owner's credit; newer businesses may need a larger down payment.")],
    [("Equipment loan calculator", "/tools/equipment-loan-calculator/"), ("Dump truck financing", "/contractor-business-loans/dump-truck-financing/"), ("Construction line of credit", "/contractor-business-loans/line-of-credit/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["New and used machines", "Loan vs lease explained", "Terms matched to equipment life"],
    [40000, 90000, 180000], aprs=(7.5, 10.5, 14.5), terms=(36, 48, 60, 84), need="Equipment financing")

CBL_TRUCK = cbl_page("dump-truck-financing", "Dump truck financing",
    "Dump truck financing: new and used trucks, and the terms that make sense",
    "Dump Truck Financing | Work Truck Loans for Contractors | AL Elite",
    "Dump truck financing and work truck loans for contractors: new vs used, down payments, terms, owner-operator vs fleet, example payments and lender requirements. AL Elite matches contractors with commercial vehicle lenders.",
    "Dump truck financing is commercial vehicle lending secured by the truck, available for new and used trucks and for owner-operators as well as fleets. Lenders look at the truck's age and mileage, your business history and the owner's credit, and often ask for a down payment on used units. AL Elite matches contractors with commercial vehicle lenders and covers work trucks, service vans and trailers too.",
    [("New vs used dump trucks", """<p>A new truck finances at longer terms and lower rates; a used one costs less but lenders cap age and mileage and may want a larger down payment. For a contractor who hauls occasionally, a well-maintained used truck on a shorter loan often makes more sense than a new one on a long one. Have the VIN, mileage, engine hours and any inspection report ready; it speeds every lender's decision.</p>"""),
     ("Owner-operators and newer businesses", """<p>Vehicle lending is one of the more accessible products for contractors with limited business history, because the truck is the collateral. Expect a larger down payment and a higher rate with under two years in business, and expect the owner's personal credit to matter. A CDL where required and commercial insurance are prerequisites.</p>"""),
     ("Work trucks, vans and trailers", """<p>The same lenders finance service vans for HVAC and plumbing shops, crew-cab pickups, equipment trailers and roofing dump trailers. Tell us what you're buying and we'll match the right lender type.</p>""")],
    [("Can I finance a used dump truck?", "Yes, within lender limits on age and mileage, usually with a down payment and a shorter term than a new truck. Bring the VIN, mileage and condition details."),
     ("How much down payment do I need for a dump truck?", "It varies by lender, truck age and your business history. Newer businesses and older trucks generally mean larger down payments. We'll match you with lenders whose requirements fit."),
     ("Can an owner-operator get dump truck financing?", "Yes. Commercial vehicle lenders work with owner-operators regularly. Expect the owner's credit, a CDL where required and commercial insurance to be part of the application.")],
    [("Construction equipment financing", "/contractor-business-loans/equipment-financing/"), ("Equipment loan calculator", "/tools/equipment-loan-calculator/"), ("Roofing business loans", "/contractor-business-loans/roofing/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["New and used trucks", "Owner-operators welcome", "Vans and trailers too"],
    [45000, 90000, 160000], aprs=(7.5, 10.5, 14.5), terms=(36, 48, 60, 72), need="Dump truck or work truck financing")

CBL_FACTOR = cbl_page("invoice-factoring", "Construction invoice factoring",
    "Construction invoice factoring: get paid this week on a net-60 invoice",
    "Construction Invoice Factoring | Construction Factoring for Subcontractors | AL Elite",
    "Construction invoice factoring explained: how factoring works for subcontractors and suppliers, advance rates, fees, recourse vs non-recourse, pay-when-paid clauses and retainage. AL Elite matches contractors with construction factoring companies.",
    "Construction invoice factoring is selling an unpaid invoice to a factoring company for an immediate advance (typically a large percentage of the invoice), with the balance minus a fee paid when your customer pays. It's built for subcontractors and suppliers waiting on general contractors, because approval rests on the GC's credit rather than yours. AL Elite matches contractors with factoring companies that understand construction's pay-when-paid clauses and retainage.",
    [("How construction factoring actually works", """<ol>
<li>You complete the work and invoice the GC or owner.</li>
<li>The factor verifies the invoice (and, in construction, often the pay application and lien position).</li>
<li>The factor advances most of the invoice value, usually within days.</li>
<li>The GC pays the factor on the original terms.</li>
<li>The factor pays you the remainder, less its fee.</li></ol>
<p>The fee depends on how long the invoice takes to be paid. The slower your customer, the more factoring costs.</p>"""),
     ("Why construction factoring is its own specialty", """<p>Generic factors avoid construction because of <strong>pay-when-paid clauses</strong> (the GC pays you when the owner pays them), <strong>retainage</strong> (a percentage held back until project completion) and <strong>lien rights</strong>. Construction-specialist factors understand all three and price accordingly. Using a generalist usually means a decline or a bad rate. Our network includes construction specialists.</p>"""),
     ("Recourse vs non-recourse", """<p>With <strong>recourse</strong> factoring, you buy the invoice back if the customer doesn't pay. With <strong>non-recourse</strong>, the factor absorbs the credit loss (usually only for insolvency, not disputes), at a higher fee. Most construction factoring is recourse. Know which you're signing.</p>""")],
    [("What is construction invoice factoring?", "Selling an unpaid construction invoice to a factoring company for an immediate advance, with the balance (less a fee) paid when the GC or owner pays. Approval depends mainly on the customer's credit."),
     ("How much does construction factoring cost?", "Fees vary with invoice size, customer credit and how long the invoice takes to pay. Ask for the fee structure in writing, including what happens if the invoice goes past the expected date, and compare the effective annual cost."),
     ("Can a subcontractor factor invoices to a general contractor?", "Yes; that's the most common use. The factor will verify the pay application and may want to understand retainage and lien position on the project.")],
    [("Working capital for contractors", "/contractor-business-loans/working-capital/"), ("Construction line of credit", "/contractor-business-loans/line-of-credit/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["Approval on the GC's credit", "Construction-specialist factors", "Recourse vs non-recourse explained"],
    None, need="Invoice factoring", qualify_extra=["<strong>Creditworthy customers.</strong> The GC or owner's payment history matters more than your own credit.", "<strong>Clean invoices.</strong> Approved pay applications, no disputes, clear lien position."])

CBL_LOC = cbl_page("line-of-credit", "Construction line of credit",
    "Construction line of credit: draw in spring, repay in fall",
    "Construction Line of Credit | Contractor Line of Credit | AL Elite",
    "Construction line of credit for contractors: how revolving credit lines work for seasonal cash flow, secured vs unsecured lines, what lenders require, costs and when a line beats a loan. AL Elite matches contractors with business lenders.",
    "A construction line of credit is revolving business credit: a lender sets a limit, you draw what you need when you need it, repay as jobs pay, and pay interest only on the outstanding balance. It fits contractors with recurring, seasonal cash-flow gaps better than a lump-sum loan. AL Elite matches contractors with lenders who offer construction and contractor lines of credit, secured and unsecured.",
    [("When a line beats a loan", """<p>If your cash need is one-off (a single big job, a single machine), a loan is cleaner. If it recurs (every spring you buy materials and hire, every fall you're flush), a line of credit means you borrow only for the weeks you need to and stop paying interest the day you repay. Many contractors keep a line open permanently as a buffer for slow-paying customers and surprise costs.</p>"""),
     ("Secured vs unsecured lines", """<p>Unsecured lines are faster and simpler but smaller and more credit-sensitive. Secured lines (against equipment, receivables or real estate) are larger and cheaper but take longer. Banks and credit unions tend to offer the best-priced lines to established contractors; online lenders are faster and more flexible for newer businesses. Our network includes both.</p>"""),
     ("What lenders want to see", """<p>Beyond the basics (time in business, revenue, credit), line-of-credit lenders look for consistent deposits, a manageable debt load and a reason the line will be repaid: backlog, signed contracts, a clear seasonal pattern. A line is a relationship product; expect an annual review.</p>""")],
    [("What is a construction line of credit?", "A revolving credit limit a contractor draws against as needed and repays as jobs pay, with interest only on the outstanding balance. It suits recurring seasonal gaps."),
     ("How much can a contractor get on a line of credit?", "Limits depend on revenue, credit and whether the line is secured. Secured lines against equipment or receivables are typically larger. We'll match you with lenders whose limits fit your business."),
     ("Is a line of credit better than a working capital loan?", "For recurring needs, usually yes; for a one-off gap, a loan is simpler. Many contractors use both: a line as a buffer and a loan for a specific large need.")],
    [("Working capital for contractors", "/contractor-business-loans/working-capital/"), ("Construction invoice factoring", "/contractor-business-loans/invoice-factoring/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["Draw and repay with the season", "Secured and unsecured options", "Bank and online lenders"],
    None, need="Line of credit", qualify_extra=["<strong>Consistent deposits and a seasonal pattern.</strong> Lenders want to see the line will be repaid each cycle."])

def cbl_trade(slug, name, h1, title, meta, answer, sections, faqs, related, cta_points, amounts):
    return cbl_page(slug, name, h1, title, meta, answer, sections, faqs, related, cta_points, amounts, need="Not sure yet", terms=(12, 24, 36, 60))

CBL_ROOFING = cbl_trade("roofing", "Roofing business loans",
    "Roofing business loans: capital for the storm season and the slow season",
    "Roofing Business Loans | Working Capital & Equipment for Roofers | AL Elite",
    "Roofing business loans: working capital for storm-season ramp-up, dump truck and equipment financing, factoring slow insurance checks, lines of credit for the off-season. AL Elite matches roofing companies with business lenders.",
    "Roofing business loans cover the cash-flow swings specific to roofing: materials and crews up front, insurance checks that arrive on the adjuster's schedule, and a storm season that can triple volume overnight. The usual tools are working capital for ramp-up, equipment and truck financing, factoring for slow insurance-paid invoices and a line of credit for the off-season. AL Elite matches roofers with business lenders and sets them up to offer customer financing.",
    [("Roofing cash flow in one paragraph", """<p>A hail storm hits. Within a week you've signed forty jobs. Shingles, underlayment and crews cost money now; the insurance checks and homeowner payments come over the next three months. The roofer who can fund the ramp-up books the forty jobs. The roofer who can't books ten. That's what <a href="/contractor-business-loans/working-capital/">working capital</a> and a <a href="/contractor-business-loans/line-of-credit/">line of credit</a> are for.</p>"""),
     ("Trucks, equipment and the off-season", """<p>Dump trucks and dump trailers for tear-off debris, shingle elevators and lifts, and crew vehicles are financed against the asset; see <a href="/contractor-business-loans/dump-truck-financing/">dump truck financing</a> and <a href="/contractor-business-loans/equipment-financing/">equipment financing</a>. For the winter slowdown, a line of credit drawn in the off-season and repaid in spring keeps crews together.</p>"""),
     ("Customer financing is the other half", """<p>Business capital funds your side of the job. A customer-financing program funds the homeowner's: deductibles, upgrades and non-covered work paid monthly, with you paid at completion. See <a href="/for-contractors/roofing/">financing for roofing companies</a>.</p>""")],
    [("What loans are available for roofing companies?", "Working capital loans, lines of credit, equipment and truck financing, invoice factoring for insurance-paid jobs, and SBA-backed loans for established companies. AL Elite matches roofers with lenders offering each."),
     ("Can a roofing company factor insurance-paid invoices?", "Often, yes, with factors who understand insurance claim timing and assignment-of-benefits rules in your state. Confirm the state's rules first."),
     ("Can a new roofing company get financing?", "Equipment and truck financing are the most accessible with limited history because the asset is collateral. Working capital usually needs a year or more of statements.")],
    [("Financing for roofing companies (offer customer financing)", "/for-contractors/roofing/"), ("Working capital for contractors", "/contractor-business-loans/working-capital/"), ("Dump truck financing", "/contractor-business-loans/dump-truck-financing/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["Storm-season ramp-up capital", "Trucks and equipment", "Off-season lines of credit"], [25000, 50000, 100000])

CBL_HVAC = cbl_trade("hvac", "HVAC business loans",
    "HVAC business loans: vans, inventory and payroll through the shoulder seasons",
    "HVAC Business Loans | Working Capital & Van Financing for HVAC Companies | AL Elite",
    "HVAC business loans: financing for service vans, pre-season inventory, recovery equipment and payroll through spring and fall, plus lines of credit and SBA options. AL Elite matches HVAC companies with business lenders.",
    "HVAC business loans address the two cash-flow problems HVAC shops share: buying equipment and inventory ahead of summer and winter peaks, and surviving the spring and fall shoulder seasons when calls drop. The tools are working capital for pre-season buying, vehicle and equipment financing for vans and tools, and a line of credit for the slow months. AL Elite matches HVAC companies with business lenders and sets them up to offer customer financing.",
    [("Pre-season inventory and the equipment pipeline", """<p>Distributors want to be paid before July; your customers pay in July and August. <a href="/contractor-business-loans/working-capital/">Working capital</a> sized to the pre-season buy, repaid from peak-season revenue, is the standard structure. For shops growing past the one-van stage, <a href="/contractor-business-loans/equipment-financing/">equipment financing</a> covers vans, recovery machines, vacuum pumps and diagnostic tools.</p>"""),
     ("Shoulder seasons", """<p>April and October are when HVAC owners lie awake. A <a href="/contractor-business-loans/line-of-credit/">line of credit</a> drawn in the shoulder and repaid at peak is the cleanest fix, and it's cheaper than the merchant-cash advances that get pitched to HVAC shops every spring. Ask any short-term lender for the APR equivalent before you sign.</p>"""),
     ("Customer financing", """<p>A customer-financing program with a second-look lender turns emergency calls into installs regardless of the customer's credit. See <a href="/for-contractors/hvac/">HVAC financing for contractors</a>.</p>""")],
    [("What financing do HVAC companies use?", "Working capital for pre-season inventory, vehicle and equipment financing for vans and tools, lines of credit for shoulder seasons and SBA-backed loans for expansion. Customer-financing programs handle the homeowner's side."),
     ("Can I finance HVAC service vans?", "Yes. Commercial vehicle lenders finance new and used service vans and upfits. See dump truck and work truck financing for how vehicle lending works."),
     ("Should an HVAC shop take a merchant cash advance?", "Usually there's a cheaper option. Ask any advance provider for the APR equivalent and total payback, then compare with a line of credit or working capital loan from our network.")],
    [("HVAC financing for contractors (offer customer financing)", "/for-contractors/hvac/"), ("Working capital for contractors", "/contractor-business-loans/working-capital/"), ("Dump truck and work truck financing", "/contractor-business-loans/dump-truck-financing/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["Pre-season inventory capital", "Van and tool financing", "Shoulder-season lines"], [20000, 40000, 80000])

CBL_PLUMBING = cbl_trade("plumbing", "Plumbing business loans",
    "Plumbing business loans: trucks, equipment and growth capital for plumbers",
    "Plumbing Business Loans | Financing for Plumbing Companies | AL Elite",
    "Plumbing business loans: financing for service trucks, sewer cameras and jetters, hiring and growth, working capital on commercial jobs and lines of credit. AL Elite matches plumbing companies with business lenders.",
    "Plumbing business loans fund the trucks, specialised equipment and hiring that let a plumbing company take on more and bigger jobs. Residential service shops mostly need vehicle and equipment financing; plumbers working commercial and new-construction jobs also need working capital and factoring for slow-paying GCs. AL Elite matches plumbing companies with business lenders and sets them up to offer customer financing.",
    [("Equipment that pays for itself", """<p>A sewer camera, a hydro-jetter or a trenchless lining rig lets a plumber sell jobs that previously went to a specialist. These are classic <a href="/contractor-business-loans/equipment-financing/">equipment financing</a> candidates: the asset is collateral and the payment is covered by the new revenue. Service trucks and vans are financed the same way; see <a href="/contractor-business-loans/dump-truck-financing/">work truck financing</a>.</p>"""),
     ("Commercial and new-construction plumbing", """<p>Once you're a sub on commercial projects, you're waiting on pay applications and retainage. <a href="/contractor-business-loans/working-capital/">Working capital</a> covers the gap on a single job; <a href="/contractor-business-loans/invoice-factoring/">construction factoring</a> turns the GC's slow invoice into cash this week.</p>"""),
     ("Customer financing for residential plumbing", """<p>Repipes and sewer line replacements are large, urgent tickets. A customer-financing program lets homeowners say yes; see <a href="/for-contractors/">offering financing to customers</a>. The homeowner page they read is <a href="/plumbing-financing/">plumbing financing</a>.</p>""")],
    [("What loans are available for plumbing companies?", "Vehicle and equipment financing, working capital, lines of credit, construction invoice factoring for commercial subs, and SBA-backed loans. AL Elite matches plumbers with lenders for each."),
     ("Can I finance a hydro-jetter or sewer camera?", "Yes. Specialised plumbing equipment is financed like any construction equipment, with the equipment as collateral."),
     ("Can a plumbing sub factor invoices to a GC?", "Yes, through construction-specialist factors who understand pay applications and retainage.")],
    [("Plumbing financing (homeowner page)", "/plumbing-financing/"), ("Construction equipment financing", "/contractor-business-loans/equipment-financing/"), ("Construction invoice factoring", "/contractor-business-loans/invoice-factoring/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["Trucks and specialised equipment", "Commercial job cash flow", "Customer financing for big tickets"], [20000, 40000, 80000])

CBL_LANDSCAPING = cbl_trade("landscaping", "Landscaping business loans",
    "Landscaping business loans: mowers, trucks and surviving the winter",
    "Landscaping Business Loans | Financing for Landscapers & Hardscapers | AL Elite",
    "Landscaping business loans: financing for mowers, trucks, trailers and skid steers, spring ramp-up working capital, lines of credit for winter, and growth into hardscape. AL Elite matches landscaping companies with business lenders.",
    "Landscaping business loans cover the most seasonal cash flow in the trades: heavy spending on equipment and labor in spring, strong revenue through summer, and little or nothing in winter outside snow markets. Equipment and truck financing, spring working capital and a line of credit for the off-season are the usual tools. AL Elite matches landscaping and hardscape companies with business lenders.",
    [("Equipment season", """<p>Commercial mowers, trucks, trailers, skid steers and mini-excavators for hardscape are all financed against the asset through <a href="/contractor-business-loans/equipment-financing/">equipment financing</a> and <a href="/contractor-business-loans/dump-truck-financing/">truck financing</a>. Dealer promotions on mowers are common in late winter; compare them with an independent lender's rate before signing.</p>"""),
     ("Spring ramp-up and winter", """<p>Hiring, fuel, materials and insurance all land in March and April before the first invoices. <a href="/contractor-business-loans/working-capital/">Working capital</a> sized to the ramp-up, repaid by midsummer, is the standard structure. For winter, a <a href="/contractor-business-loans/line-of-credit/">line of credit</a> drawn in the off-season beats carrying debt all year. Snow-removal contracts, where you have them, change the picture and lenders like to see them.</p>"""),
     ("Growing into hardscape", """<p>Patios, retaining walls and outdoor kitchens are higher-ticket and less seasonal than maintenance. The equipment is more expensive and customers often need financing of their own; see <a href="/for-contractors/">offering financing to customers</a> and the homeowner page for <a href="/landscaping-financing/">landscaping financing</a>.</p>""")],
    [("What financing is available for landscaping companies?", "Equipment and truck financing, spring working capital, lines of credit for the off-season and SBA-backed loans for growth. AL Elite matches landscapers with lenders for each."),
     ("Can I finance commercial mowers?", "Yes, through equipment lenders or dealer programs. Compare dealer promotional rates with an independent offer."),
     ("How do landscapers get through winter financially?", "A line of credit drawn in the off-season and repaid in summer, snow contracts where available, and keeping fixed costs low. Lenders look favourably on a documented seasonal plan.")],
    [("Landscaping financing (homeowner page)", "/landscaping-financing/"), ("Construction equipment financing", "/contractor-business-loans/equipment-financing/"), ("Construction line of credit", "/contractor-business-loans/line-of-credit/"), ("Contractor business loans (main page)", "/contractor-business-loans/")],
    ["Mowers, trucks, skid steers", "Spring ramp-up capital", "Off-season lines of credit"], [15000, 30000, 60000])

CONTRACTOR_SERVICE_PAGES = [FOR_CONTRACTORS, FC_ROOFING, FC_HVAC, FC_REMODEL, FC_SOLAR, CBL_WC, CBL_EQUIP, CBL_TRUCK, CBL_FACTOR, CBL_LOC, CBL_ROOFING, CBL_HVAC, CBL_PLUMBING, CBL_LANDSCAPING]
CONTRACTOR_HUBS = [CBL_HUB]
