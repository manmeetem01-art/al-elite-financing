"""Consumer (homeowner) trade pages. Each entry is unique copy; shared scaffolding is parametrised by trade."""
from common import *

HOME = ("Home", "/")
HUB = ("Home improvement financing", "/home-improvement-financing/")

def std_options(trade, insurance=False, equity=True, extra=None):
    opts = [
        ("Personal loan for the project", f"An unsecured instalment loan, usually funded in days, repaid over a fixed term. The most common way homeowners finance {trade} when they want to keep their home out of it.", "Fixed payments, fast funding, no lien on the house.", "APR rises quickly with lower credit scores; some lenders charge an origination fee."),
        ("Contractor-arranged financing", f"Your contractor offers a payment plan at the kitchen table, usually through a lender partner. AL Elite partner contractors use our network for exactly this.", "Convenience, promotional rates on some plans, one conversation instead of two.", "Promotional 'same as cash' plans can carry deferred interest if not paid in full by the deadline. Read the terms."),
    ]
    if equity:
        opts.append(("Home equity loan or HELOC", f"Borrow against the equity in your home. Rates are typically lower because the loan is secured by the property.", "Larger projects, lower rates, long terms.", "Takes weeks, involves closing costs and an appraisal, and your home is collateral."))
    opts.append(("Credit card with a promotional rate", "A 0% introductory purchase APR card can cover smaller jobs if you can clear the balance before the promo ends.", "Small repairs you can repay inside 12 to 21 months.", "The standard APR after the promo period is usually the highest of any option here."))
    if insurance:
        opts.insert(0, ("Insurance claim plus financing for the gap", f"After storm, hail or wind damage, your homeowners policy may cover part of the {trade}. Financing then covers the deductible, upgrades or anything the adjuster didn't approve.", "Storm damage with a documented claim.", "Claims take time, and policies with roof-age depreciation schedules pay less than you expect. Our guide on insurance and roof replacement explains the process."))
    if extra:
        opts += extra
    return opts

def std_qualify(extra=None):
    q = [
        "<strong>Credit score.</strong> Most unsecured lenders look for scores in the mid-600s or higher for their better rates. Some lenders in our network consider lower scores, at a higher APR or with a co-applicant.",
        "<strong>Income and debt-to-income ratio.</strong> Lenders want to see that the new payment fits alongside your mortgage, car payment and other obligations.",
        "<strong>Loan amount and term.</strong> Unsecured loans typically cap out at a level that varies by lender; larger projects may point you toward a home equity product.",
        "<strong>State.</strong> Not every lender operates in every state, and some products have state-specific limits. We only match you with lenders who can serve your location.",
        "<strong>Identity and residency.</strong> Expect to verify who you are and that you own or occupy the home. You never give that information to AL Elite; the lender collects it securely.",
    ]
    return q + (extra or [])

def common_faqs(trade, page_noun):
    return [
        (f"Is AL Elite a lender for {trade}?", f"No. AL Elite is a matching service. We route your request to lenders in our network who fund {trade}, and they make the offer and the decision. We are paid by lenders and partner contractors, so comparing options through us is free."),
        (f"Does requesting {trade} options affect my credit?", "Submitting a request to AL Elite does not pull your credit. Many lenders in the network show initial options with a soft inquiry, which does not affect your score. A hard inquiry usually happens only when you formally apply with the lender you choose. We label each lender's approach before you proceed."),
        (f"How fast can {trade} be funded?", "That depends on the lender and the product. Unsecured personal loans and contractor-arranged plans are typically the fastest, often within days of approval. Home equity products take longer because of appraisals and closing. We tell you what to expect from each lender before you apply."),
    ]

# ------------------------------------------------------------------ ROOF (pillar)
ROOF = dict(
    path="/roof-financing/", crumbs=[HOME, HUB, ("Roof financing", "/roof-financing/")],
    eyebrow="Roof financing", h1="Roof financing: pay for a new roof monthly instead of all at once",
    title="Roof Financing | Compare New Roof & Roof Replacement Loans | AL Elite",
    meta="Roof financing explained: new roof loans, roof replacement financing options, bad credit choices, example monthly payments and what lenders look for. AL Elite matches you with lenders. Not a lender.",
    answer="Roof financing lets you pay for a roof replacement or repair over a fixed term rather than up front. The common routes are an unsecured personal loan, a payment plan arranged through your roofing contractor, or a home equity product. AL Elite matches homeowners with lenders who fund roofing projects, and tells you up front which lenders start with a soft credit check.",
    cta_points=["Roof replacement, repair and storm damage", "Options for a range of credit profiles", "Lenders that fund roofing specifically"],
    project="Roof replacement or repair", how_noun="a roof",
    intro="""<p>A roof rarely fails on a convenient schedule. It leaks after a hail storm, it fails inspection when you're selling, or the insurance company gives you a deadline. The quote arrives, and it's more than you have sitting in a checking account. That's the situation this page is written for.</p>""",
    sections=[
        ("What drives the cost of a new roof", """<p>Two roofs on the same street can differ by thousands of dollars. The factors that move the number most:</p><ul>
<li><strong>Size and pitch.</strong> Roofers price by the "square" (100 sq ft). Steeper roofs cost more per square because they're slower and riskier to work on.</li>
<li><strong>Material.</strong> Architectural asphalt shingles are the baseline in most of the country. Metal, tile and slate cost more up front but last longer, which matters for how long you'd want to finance.</li>
<li><strong>Tear-off and decking.</strong> Removing old layers and replacing rotten decking adds labor and disposal. It's also where surprise costs appear mid-job, so leave room in your financing.</li>
<li><strong>Storm season and local demand.</strong> After a major hail event, crews in that metro are booked for months and prices rise. Our <a href="/locations/">city pages</a> cover storm-market timing.</li>
<li><strong>Code upgrades.</strong> Ice-and-water shield, ventilation and ridge requirements vary by state and county.</li></ul>
<p>Get at least two written quotes that itemize these elements. A lender will typically ask for the quote, and an itemized one makes it easier to finance the right amount rather than a round guess.</p>"""),
        ("Roof financing after storm or hail damage", """<p>In hail-belt states, a large share of roof replacements start with an insurance claim. Financing still matters in three places: the <strong>deductible</strong> (which on newer policies can be a percentage of the dwelling value, not a flat amount), <strong>upgrades</strong> the policy won't cover such as impact-resistant shingles, and the <strong>gap</strong> when a claim is depreciated for roof age. Our guide <a href="/blog/does-insurance-cover-roof-replacement/">Does insurance cover roof replacement?</a> walks through the claims process.</p><p>Be careful with any contractor who offers to "waive" or "absorb" your deductible. In many states that is insurance fraud, and it's a reason we vet partner contractors.</p>"""),
        ("Metal, repair and commercial roofs", """<p>Some roof projects need their own treatment. <a href="/roof-financing/metal-roof-financing/">Metal roof financing</a> covers the higher up-front cost and longer lifespan trade-off. <a href="/roof-financing/roof-repair-financing/">Roof repair financing</a> is for smaller jobs where a full loan may be overkill. <a href="/roof-financing/commercial-roof-financing/">Commercial roof financing</a> is for business owners and landlords, where the lender and the paperwork are different.</p>"""),
    ],
    options=std_options("a new roof", insurance=True),
    amounts=[8000, 15000, 25000],
    qualify=std_qualify(["<strong>A written quote.</strong> Most lenders funding a specific project want to see the contractor's estimate, and contractor-arranged plans pay the roofer directly."]),
    faqs=[
        ("Can you finance a roof?", "Yes. Roof replacement is one of the most commonly financed home projects. The main routes are an unsecured personal loan, a payment plan arranged through the roofing contractor, or a home equity loan or line of credit. Which one fits depends on the cost, how urgently the work is needed and whether you want to use your home as collateral."),
        ("What credit score do you need for roof financing?", "There's no single number. Unsecured lenders generally offer their better rates to scores in the mid-600s and above, and some lenders in our network consider lower scores at a higher APR or with a co-applicant. Contractor-arranged plans sometimes have their own thresholds. See our page on <a href='/roof-financing/bad-credit-roof-financing/'>roof financing with bad credit</a> for realistic expectations."),
        ("How much is a $15,000 roof per month?", "As an example, $15,000 over 60 months at 9.99% APR with no fees is about $319 per month and roughly $4,100 in total interest. Over 120 months it's about $198 a month, with roughly double the interest. Try your own numbers in the <a href='/tools/roof-financing-calculator/'>roof financing calculator</a>. These are illustrations, not offers."),
        ("Can I finance a roof if insurance is paying part of it?", "Yes. Financing commonly covers the deductible, upgrades the adjuster didn't approve, or the depreciation holdback on an older roof. Lenders will usually want to know the insurance amount so the loan covers only the gap."),
        ("Should I finance through my roofer or get my own loan?", "Compare both. Contractor-arranged financing is convenient and sometimes carries promotional rates, but promotional plans can include deferred interest. A personal loan you arrange yourself gives you a fixed rate and payment with no surprises. AL Elite shows you both kinds of lender so you can put the offers side by side."),
    ] + common_faqs("roof financing", "roof"),
    related=[("Roof financing with bad credit", "/roof-financing/bad-credit-roof-financing/"), ("Metal roof financing", "/roof-financing/metal-roof-financing/"), ("Roof repair financing", "/roof-financing/roof-repair-financing/"), ("Roof financing calculator", "/tools/roof-financing-calculator/"), ("Siding financing", "/siding-financing/"), ("Gutter financing", "/gutter-financing/"), ("How to finance a new roof: 6 options", "/blog/how-to-finance-a-new-roof/"), ("Roofing companies that offer financing", "/blog/roofing-companies-that-offer-financing/"), ("Are you a roofer? Offer financing to customers", "/for-contractors/roofing/")],
    service_name="Roof financing matching", audience="Homeowners replacing or repairing a roof",
)

ROOF_BAD_CREDIT = dict(
    path="/roof-financing/bad-credit-roof-financing/", crumbs=[HOME, HUB, ("Roof financing", "/roof-financing/"), ("Bad credit", "/roof-financing/bad-credit-roof-financing/")],
    eyebrow="Roof financing with bad credit", h1="Roof financing with bad credit: what's realistic, and what to avoid",
    title="Roof Financing with Bad Credit | Realistic Options | AL Elite",
    meta="Roof financing with bad credit or a low score: which lenders consider it, what APRs to expect, co-applicants, secured options and the 'no credit check' offers to avoid. AL Elite is a matching service, not a lender.",
    answer="Roof financing with bad credit is possible but narrower. Some lenders consider scores below the mid-600s, usually at a higher APR, a smaller amount or with a co-applicant. Options that don't rely on your score include a home equity product (secured by the house) or an insurance claim for storm damage. Be wary of any site promising 'guaranteed approval' or 'no credit check' roof loans; AL Elite doesn't make those claims and won't match you with lenders who do.",
    cta_points=["Lenders that consider lower scores", "Honest about approval odds", "No 'guaranteed approval' claims"],
    project="Roof replacement or repair", how_noun="a roof with a lower credit score",
    verify="Confirm with each lender partner which minimum score (if any) they publish before quoting ranges on this page. The copy below deliberately avoids numbers lenders haven't confirmed.",
    sections=[
        ("What 'bad credit' means to a roof lender", """<p>Lenders look at your score, but also at <em>why</em> it's low. A score dragged down by high card utilization reads differently from one with a recent bankruptcy or collections. Thin credit (few accounts, short history) is different again. When you tell us about the project, it helps to say which of these applies, because it changes which lenders are worth your time.</p>"""),
        ("Five routes that can work with a lower score", """<ol>
<li><strong>Lenders who specialise in fair or near-prime credit.</strong> Higher APRs, often an origination fee, but a real fixed-term loan. Read the APR, not just the monthly payment.</li>
<li><strong>A co-applicant or co-signer.</strong> A spouse or family member with stronger credit can bring the rate down substantially. They are legally responsible for the loan.</li>
<li><strong>Home equity, if you have it.</strong> Because the loan is secured, score thresholds are often more forgiving. The trade-off is that the house is collateral and the process takes weeks.</li>
<li><strong>Contractor-arranged plans.</strong> Some contractor financing programs have second-look lenders built in. Ask the roofer whether their program has one.</li>
<li><strong>Insurance first, financing second.</strong> If the roof was storm-damaged, a claim can cover most of the cost and leave a much smaller amount to finance.</li></ol>"""),
        ("Offers to avoid", """<p>Searches for "no credit check roof financing" bring up lenders you should treat with caution. A legitimate lender will check your credit; the question is whether it's a soft or hard inquiry and when. "Guaranteed approval" and "no credit check" loans tend to carry very high costs or turn out to be lead-capture pages. If a lender won't show you an APR before you commit, walk away.</p><div class="callout"><strong>Our commitment:</strong> we won't tell you approval is guaranteed, because it isn't. We will tell you honestly if your profile is unlikely to get offers, and what would change that.</div>"""),
    ],
    options=None, amounts=[8000, 12000], aprs=(14.99, 22.99, 29.99),
    pay_h2="What higher-APR financing actually costs per month", pay_intro="With a lower score, APRs tend to sit in a higher band. The table shows what that means for the payment and, more importantly, the total interest. Illustrative only; lenders set actual rates.",
    qualify=std_qualify(["<strong>Recent history matters more than old history.</strong> Twelve months of on-time payments can open doors a two-year-old default closed."]),
    faqs=[
        ("Can I get roof financing with a 550 credit score?", "Some lenders consider scores in that range, typically at a high APR, a smaller loan amount or with a co-applicant. Approval is not guaranteed. A secured option such as a home equity product, or an insurance claim for storm damage, may be more realistic. Tell us your situation and we'll be honest about what's likely."),
        ("Is there roof financing with no credit check?", "Legitimate lenders check credit. What varies is whether the initial check is a soft inquiry (no effect on your score) or a hard one. Offers advertising 'no credit check' usually carry very high costs or aren't real lenders. AL Elite doesn't match with lenders making those claims."),
        ("Will applying hurt my credit further?", "Submitting to AL Elite doesn't pull your credit. Lenders that pre-qualify with a soft inquiry won't affect your score. A hard inquiry at formal application typically has a small, temporary effect. Multiple hard inquiries for the same purpose in a short window are often treated as one by scoring models, but limit them anyway."),
        ("Does a co-signer really help?", "Usually, yes. A co-applicant with stronger credit and income can turn a decline into an approval or lower the APR substantially. They take on full legal responsibility for the loan, so it's a serious ask."),
    ],
    related=[("Roof financing (main page)", "/roof-financing/"), ("HVAC financing with bad credit", "/hvac-financing/bad-credit-hvac-financing/"), ("Does insurance cover roof replacement?", "/blog/does-insurance-cover-roof-replacement/"), ("HELOC vs roof loan vs contractor financing", "/blog/heloc-vs-roof-loan/"), ("Roof financing calculator", "/tools/roof-financing-calculator/")],
    service_name="Roof financing matching for lower credit scores", audience="Homeowners with fair or poor credit",
)

ROOF_METAL = dict(
    path="/roof-financing/metal-roof-financing/", crumbs=[HOME, HUB, ("Roof financing", "/roof-financing/"), ("Metal roof financing", "/roof-financing/metal-roof-financing/")],
    eyebrow="Metal roof financing", h1="Metal roof financing: paying for a roof that outlasts the loan",
    title="Metal Roof Financing Options | Standing Seam & Metal Shingle Loans | AL Elite",
    meta="Metal roof financing options: how to finance standing seam or metal shingle roofs, longer terms to match a longer-lasting roof, insurance discounts, example payments. AL Elite matches you with lenders.",
    answer="Metal roof financing works like any roof loan, with one difference: the higher up-front cost usually justifies a longer term, because a metal roof is expected to last several decades. The common routes are a personal loan, contractor-arranged financing or a home equity product. AL Elite matches you with lenders who fund roofing, including larger metal roof projects.",
    cta_points=["Standing seam, metal shingle and stone-coated steel", "Longer terms for larger amounts", "Lenders who fund premium roofing"],
    project="Roof replacement or repair", how_noun="a metal roof",
    sections=[
        ("Why metal roofs are financed differently", """<p>An asphalt roof and a metal roof solve the same problem on very different timelines. The metal roof costs more on day one, but its expected service life is far longer, it often qualifies for homeowners-insurance discounts in hail and wind markets, and it can reduce cooling costs. That changes the financing math in two ways:</p><ul>
<li><strong>A longer term is defensible.</strong> Financing a 50-year roof over 10 or 12 years is not unreasonable, where financing a 20-year shingle roof over 12 years leaves you paying for a roof near the end of its life.</li>
<li><strong>Home equity becomes more attractive.</strong> For larger amounts, a secured product with a lower rate may cost less overall than an unsecured loan, despite closing costs.</li></ul>"""),
        ("Questions to ask before you finance a metal roof", """<ul>
<li>Is the quote for standing seam, exposed-fastener panels, metal shingles or stone-coated steel? The price and lifespan differ a lot.</li>
<li>Does the metal roof qualify for an impact-resistance (Class 4) insurance discount in your state? Ask your insurer in writing; the discount can offset part of the payment.</li>
<li>Is the warranty transferable if you sell? A transferable warranty supports resale value, which matters if you're financing over a long term.</li>
<li>Does the contractor install metal regularly? Metal is a different trade from shingles. We ask partner contractors this directly.</li></ul>"""),
    ],
    options=std_options("a metal roof", insurance=True),
    amounts=[20000, 30000, 45000], terms=(60, 84, 120, 144),
    qualify=std_qualify(),
    faqs=[
        ("Can you finance a metal roof?", "Yes. Metal roofs are financed through the same channels as other roofs: personal loans, contractor-arranged plans and home equity products. Because the amount is usually larger, longer terms and secured options are more common than with a shingle roof."),
        ("Is a metal roof worth financing over 10 years?", "It can be, because the roof is expected to last well beyond the loan. Compare total interest at different terms using the <a href='/tools/roof-financing-calculator/'>calculator</a> and weigh it against any insurance discount or energy savings the roof brings. Whether it's worth it depends on your rate and how long you'll stay in the home."),
        ("Do metal roofs lower insurance premiums?", "In many hail and wind markets, insurers offer discounts for roofs rated Class 4 for impact resistance, which many metal products are. Discounts vary by insurer and state, so get confirmation in writing before counting on it."),
    ] + common_faqs("metal roof financing", "metal roof"),
    related=[("Roof financing (main page)", "/roof-financing/"), ("Roof financing calculator", "/tools/roof-financing-calculator/"), ("HELOC vs roof loan", "/blog/heloc-vs-roof-loan/"), ("Solar panel financing", "/solar-financing/")],
    service_name="Metal roof financing matching", audience="Homeowners installing a metal roof",
)

ROOF_REPAIR = dict(
    path="/roof-financing/roof-repair-financing/", crumbs=[HOME, HUB, ("Roof financing", "/roof-financing/"), ("Roof repair financing", "/roof-financing/roof-repair-financing/")],
    eyebrow="Roof repair financing", h1="Roof repair financing: smaller jobs, faster money",
    title="Roof Repair Financing | Finance Leaks, Flashing & Storm Repairs | AL Elite",
    meta="Roof repair financing for leaks, flashing, missing shingles and storm repairs. When a small loan, a promo-rate card or contractor financing makes sense, and when repair vs replace changes the answer. AL Elite matches you with lenders.",
    answer="Roof repair financing covers smaller jobs, from a leak or flashing repair to a partial re-shingle after wind damage. For amounts under a few thousand dollars, a short-term personal loan, a contractor payment plan or a promotional-rate credit card is usually simpler than a larger loan. AL Elite matches you with lenders who fund smaller roofing jobs, and flags when a repair quote is high enough that replacement financing makes more sense.",
    cta_points=["Leaks, flashing, missing shingles, storm patches", "Smaller amounts and shorter terms", "Repair vs replace guidance"],
    project="Roof replacement or repair", how_noun="a roof repair",
    sections=[
        ("Repair or replace: the financing question underneath", """<p>Roofers have a rule of thumb: when a repair quote approaches a meaningful fraction of a replacement, and the roof is in the back half of its life, replacement usually wins. The financing consequence is real. Financing a repair on a roof that will need replacing in three years means paying for the same roof twice. Ask the contractor for the roof's remaining expected life in writing alongside the repair quote.</p>"""),
        ("Fast options for smaller roof repairs", """<ul>
<li><strong>Short-term personal loan.</strong> Many lenders fund small amounts over 12 to 36 months. Short terms keep total interest low.</li>
<li><strong>Contractor payment plan.</strong> Partner roofers offer plans sized for repairs. Ask whether a promotional period applies and what happens if it's not paid in full by the end.</li>
<li><strong>Promotional-rate credit card.</strong> Workable if you can clear the balance inside the promo window. Not workable if you can't.</li>
<li><strong>Insurance.</strong> Storm-related repairs may be claimable. Weigh the deductible and any premium effect against the repair cost; for small repairs, a claim often isn't worth filing.</li></ul>"""),
    ],
    options=None, amounts=[2500, 5000, 8000], terms=(12, 24, 36, 60),
    qualify=std_qualify(),
    faqs=[
        ("Can I finance a roof repair?", "Yes. Smaller roofing jobs are financed through short-term personal loans, contractor payment plans and promotional-rate credit cards. For larger repairs, the same options as a full roof replacement apply."),
        ("Is it worth financing a small roof repair?", "If the alternative is leaving a leak, yes; water damage compounds fast. Keep the term short to limit interest, and confirm the roof has enough life left that the repair is a real fix rather than a delay."),
        ("Will my insurance cover a roof repair?", "Sudden storm damage is often covered, subject to your deductible. Wear and tear and neglect usually aren't. For a small repair, compare the deductible with the repair cost before filing. Our <a href='/blog/does-insurance-cover-roof-replacement/'>insurance guide</a> covers the process."),
    ] + common_faqs("roof repair financing", "roof repair"),
    related=[("Roof financing (main page)", "/roof-financing/"), ("Gutter financing", "/gutter-financing/"), ("Siding financing", "/siding-financing/"), ("Does insurance cover roof replacement?", "/blog/does-insurance-cover-roof-replacement/"), ("Roof financing calculator", "/tools/roof-financing-calculator/")],
    service_name="Roof repair financing matching", audience="Homeowners repairing a roof",
)

ROOF_COMMERCIAL = dict(
    path="/roof-financing/commercial-roof-financing/", crumbs=[HOME, HUB, ("Roof financing", "/roof-financing/"), ("Commercial roof financing", "/roof-financing/commercial-roof-financing/")],
    eyebrow="Commercial roof financing", h1="Commercial roof financing for business owners and landlords",
    title="Commercial Roof Financing | Flat, TPO, Metal & Membrane Roofs | AL Elite",
    meta="Commercial roof financing for business owners, landlords and property managers: equipment-style loans, SBA-backed options, lines of credit and lender requirements for TPO, EPDM, metal and modified bitumen roofs. AL Elite matches you with business lenders.",
    answer="Commercial roof financing uses business lenders rather than consumer ones. Depending on the property and the business, that can mean a term loan, an SBA-backed loan, a commercial line of credit or financing arranged by the roofing contractor. AL Elite matches business owners and landlords with lenders who fund commercial roofing, and matches commercial roofers who want to offer financing to their customers.",
    cta_points=["Term loans, lines of credit and SBA-backed options", "Owner-occupied and investment property", "Lenders who understand commercial roofing"],
    role="contractor", need="Not sure yet", how_noun="a commercial roof",
    how_1="The property type, roof system (TPO, EPDM, metal, modified bitumen), the quote and how long you've owned or operated. No credit pull.",
    how_2="Your request goes to business lenders in our network who fund commercial property improvements in your state.",
    how_3="Rates, terms and the decision come from the lender. Compare the offers and choose, or don't. AL Elite never charges you.",
    sections=[
        ("How commercial roof financing differs from residential", """<ul>
<li><strong>The borrower is the business or the property owner,</strong> so lenders look at business revenue, time in operation, the property's income and sometimes a personal guarantee.</li>
<li><strong>Amounts are larger and terms longer.</strong> Low-slope commercial roofs are priced by the square foot across large areas; a term loan over 5 to 10 years is common.</li>
<li><strong>Tax treatment is different.</strong> Some roof work on commercial property may qualify for accelerated depreciation or expensing under current tax rules. That's a question for your accountant, not this page.</li>
<li><strong>Tenants and leases matter.</strong> On investment property, lenders may ask about lease terms and whether tenants contribute to capital improvements.</li></ul>"""),
        ("Common ways businesses pay for a commercial roof", """<ul>
<li><strong>Business term loan.</strong> Fixed amount, fixed term, predictable payment. The default for a single defined project.</li>
<li><strong>SBA-backed loan.</strong> Longer terms and competitive rates for qualifying small businesses, with more paperwork and a longer timeline.</li>
<li><strong>Commercial line of credit.</strong> Useful when the roof is one of several capital projects, or when the final scope isn't fixed.</li>
<li><strong>Contractor-arranged commercial financing.</strong> Some commercial roofers partner with lenders to offer financing at proposal stage. AL Elite partner contractors can do this through our network.</li></ul>"""),
    ],
    options=None, amounts=[50000, 120000, 250000], aprs=(8.5, 11.5, 15.5), terms=(36, 60, 84, 120),
    pay_h2="Example payments on a commercial roof loan",
    qualify=["<strong>Time in business and revenue.</strong> Most business lenders want a track record; requirements vary widely.", "<strong>Property ownership or long-term lease.</strong> Lenders want to know the business will benefit from the roof for the life of the loan.", "<strong>Business and sometimes personal credit.</strong> Smaller businesses are often underwritten partly on the owner's credit.", "<strong>A detailed proposal.</strong> Roof system, square footage, warranty and contractor credentials."],
    qualify_intro="Business lenders each set their own criteria. The things they ask about most:",
    faqs=[
        ("Can a business finance a new roof?", "Yes. Business term loans, SBA-backed loans, commercial lines of credit and contractor-arranged financing are all used for commercial roofing. AL Elite matches business owners and landlords with lenders who fund this kind of project."),
        ("Can I finance a roof on a rental property?", "Usually, yes, through a business or investment-property lender rather than a consumer lender. Expect questions about the property's income and your other obligations."),
        ("I'm a commercial roofer. Can I offer financing to my customers?", "Yes. Our <a href='/for-contractors/roofing/'>financing for roofing companies</a> page explains how partner contractors present financing at proposal stage, for both residential and commercial customers."),
    ],
    related=[("Contractor business loans", "/contractor-business-loans/"), ("Financing for roofing companies", "/for-contractors/roofing/"), ("Construction line of credit", "/contractor-business-loans/line-of-credit/"), ("Residential roof financing", "/roof-financing/")],
    service_name="Commercial roof financing matching", service_type="Business financing matching", audience="Business owners, landlords and property managers",
)

# ------------------------------------------------------------------ HVAC
HVAC = dict(
    path="/hvac-financing/", crumbs=[HOME, HUB, ("HVAC financing", "/hvac-financing/")],
    eyebrow="HVAC financing", h1="HVAC financing: replace the AC or furnace now, pay monthly",
    title="HVAC Financing | AC, Furnace & Heat Pump Loans | AL Elite",
    meta="HVAC financing for AC, furnace and heat pump replacement: options when the system dies in a heatwave, bad credit choices, rebates, example monthly payments and what lenders look for. AL Elite matches you with lenders.",
    answer="HVAC financing lets you replace a failed air conditioner, furnace or heat pump and pay over a fixed term. Because HVAC failures are urgent, the fastest routes are a personal loan or a payment plan arranged through the HVAC contractor; home equity products are cheaper but slower. AL Elite matches homeowners with lenders who fund HVAC replacement and tells you which ones start with a soft credit check.",
    cta_points=["Central AC, furnaces, heat pumps, mini-splits", "Fast options for emergency replacement", "Lower-credit options available"],
    project="HVAC (AC, furnace, heat pump)", how_noun="an HVAC system",
    intro="""<p>Air conditioners fail in July and furnaces fail in January. Nobody plans the timing, and the quote tends to land in the middle of the worst week to be without heating or cooling. This page is about getting a system installed quickly on terms you can live with afterward.</p>""",
    sections=[
        ("What drives the cost of HVAC replacement", """<ul>
<li><strong>System type.</strong> A straight AC swap, a furnace, a full split system, a heat pump or ductless mini-splits all sit at different price points.</li>
<li><strong>Capacity and efficiency.</strong> Higher SEER2 and HSPF2 ratings cost more up front and less to run. Efficiency can also qualify for rebates.</li>
<li><strong>Ductwork.</strong> If the ducts are leaky, undersized or absent, that's a second project inside the first.</li>
<li><strong>Electrical and code work.</strong> Heat pumps and larger systems sometimes need panel upgrades or new disconnects.</li>
<li><strong>Season.</strong> Emergency replacements in peak season cost more and offer less room to compare quotes.</li></ul>"""),
        ("Rebates and incentives can reduce what you finance", """<p>Many utilities and some state programs offer rebates for high-efficiency equipment and heat pumps, and federal tax credits have applied to certain qualifying equipment. The rules change, so confirm current programs with your utility and a tax professional before relying on them. The practical point for financing: a rebate paid after installation doesn't reduce the up-front cost, so you may finance the full amount and apply the rebate to the balance later.</p>"""),
        ("HVAC financing with lower credit", """<p>HVAC is one of the trades where lenders are most used to urgent, lower-credit requests, because nobody waits to fix their credit before replacing a dead furnace. We have a dedicated page on <a href="/hvac-financing/bad-credit-hvac-financing/">HVAC financing with bad credit</a> that sets realistic expectations.</p>"""),
    ],
    options=std_options("an HVAC replacement"),
    amounts=[6000, 10000, 16000],
    qualify=std_qualify(),
    faqs=[
        ("Can you finance an HVAC system?", "Yes. Air conditioners, furnaces, heat pumps and mini-split systems are routinely financed through personal loans, contractor-arranged payment plans and home equity products. The urgent nature of most HVAC failures means fast-funding options are the most common."),
        ("What's the fastest way to finance an AC replacement?", "A contractor-arranged plan or an online personal loan is usually fastest, often funded within days of approval. Home equity products take weeks. AL Elite tells you each lender's typical timeline before you apply."),
        ("Can I get HVAC financing with bad credit?", "Some lenders in our network consider lower scores, usually at a higher APR or with a co-applicant. Approval is never guaranteed. See <a href='/hvac-financing/bad-credit-hvac-financing/'>HVAC financing with bad credit</a> for what's realistic."),
        ("Is it better to repair or replace before financing?", "If the system is old, uses a phased-out refrigerant or the repair quote is a large fraction of replacement, replacement financing is usually the better use of money. Ask the contractor for the system's age and the repair's expected life in writing."),
    ] + common_faqs("HVAC financing", "HVAC"),
    related=[("HVAC financing with bad credit", "/hvac-financing/bad-credit-hvac-financing/"), ("Water heater financing", "/water-heater-financing/"), ("Plumbing financing", "/plumbing-financing/"), ("Generator financing", "/generator-financing/"), ("Are you an HVAC contractor? Offer financing", "/for-contractors/hvac/")],
    service_name="HVAC financing matching", audience="Homeowners replacing heating or cooling equipment",
)

HVAC_BAD_CREDIT = dict(
    path="/hvac-financing/bad-credit-hvac-financing/", crumbs=[HOME, HUB, ("HVAC financing", "/hvac-financing/"), ("Bad credit", "/hvac-financing/bad-credit-hvac-financing/")],
    eyebrow="HVAC financing with bad credit", h1="HVAC financing with bad credit: getting the heat or AC back on",
    title="HVAC Financing with Bad Credit | Realistic AC & Furnace Options | AL Elite",
    meta="HVAC financing with bad credit: lenders that consider lower scores, co-applicants, contractor second-look programs, secured options and the offers to avoid. Honest about odds. AL Elite is a matching service, not a lender.",
    answer="HVAC financing with bad credit is possible, with trade-offs. Some lenders in AL Elite's network consider scores below the mid-600s, usually at a higher APR, a smaller amount or with a co-applicant. Contractor financing programs sometimes include a second-look lender for declined applications. No legitimate lender guarantees approval, and we won't either.",
    cta_points=["Lenders that consider lower scores", "Contractor second-look programs", "No 'guaranteed approval' claims"],
    project="HVAC (AC, furnace, heat pump)", how_noun="HVAC with a lower credit score",
    verify="Confirm with lender partners which publish a minimum score before adding ranges. Copy avoids unconfirmed numbers.",
    sections=[
        ("Why HVAC lenders are used to lower-credit requests", """<p>An HVAC failure is an emergency, and lenders who work with HVAC contractors know that. Many contractor financing programs are built with a primary lender for stronger credit and a second-look lender for applications the first one declines. Ask the contractor whether their program has one. It's the single most useful question when your score is low.</p>"""),
        ("Options that depend less on your score", """<ul>
<li><strong>Co-applicant.</strong> A household member with stronger credit can change the outcome. They become fully responsible for the loan.</li>
<li><strong>Home equity.</strong> Secured lending is more forgiving on score, but takes weeks, which is hard with a dead furnace. Some homeowners use a short-term option now and refinance into equity later.</li>
<li><strong>Utility and assistance programs.</strong> Some utilities offer on-bill financing or repair assistance for heating equipment, and some states have energy assistance programs. Check with your utility before borrowing.</li>
<li><strong>Repair now, replace later.</strong> If a repair buys a season, it may be worth taking a smaller loan now and improving your credit before the full replacement.</li></ul>"""),
        ("Offers to avoid", """<p>"No credit check" and "guaranteed approval" HVAC financing is advertised aggressively. Legitimate lenders check credit. If an offer won't show an APR before you commit, or asks for an up-front fee, treat it as a warning sign.</p>"""),
    ],
    options=None, amounts=[6000, 10000], aprs=(14.99, 22.99, 29.99),
    pay_h2="What higher-APR HVAC financing costs per month", pay_intro="Lower scores usually mean APRs in a higher band. Look at the total interest column as closely as the payment. Illustrative only.",
    qualify=std_qualify(["<strong>Stability signals.</strong> Steady income and time at your address help when the score doesn't."]),
    faqs=[
        ("Can I finance an AC unit with bad credit?", "Possibly. Some lenders consider lower scores at a higher APR or smaller amount, and many contractor programs include a second-look lender. A co-applicant improves the odds. Approval is never guaranteed."),
        ("What credit score is needed for HVAC financing?", "There's no universal threshold. Better rates typically start in the mid-600s, and some lenders consider scores below that. Lender partners set their own criteria, and we show you only lenders whose criteria you may fit."),
        ("Does a contractor's financing accept bad credit?", "It depends on the program. Many have a primary and a second-look lender. AL Elite partner contractors use our network, which includes lenders for a range of credit profiles."),
    ],
    related=[("HVAC financing (main page)", "/hvac-financing/"), ("Roof financing with bad credit", "/roof-financing/bad-credit-roof-financing/"), ("Water heater financing", "/water-heater-financing/")],
    service_name="HVAC financing matching for lower credit scores", audience="Homeowners with fair or poor credit",
)

# ------------------------------------------------------------------ other trades (compact unique entries)
def trade(slug, name, h1, title, meta, answer, project, drivers, extra_sections, faqs, related, amounts, cta_points, insurance=False, equity=True, terms=(36, 60, 84, 120), tag_noun=None):
    return dict(
        path=f"/{slug}/", crumbs=[HOME, HUB, (name, f"/{slug}/")], eyebrow=name, h1=h1, title=title, meta=meta, answer=answer,
        cta_points=cta_points, project=project, how_noun=tag_noun or name.lower().replace(" financing", ""),
        sections=[(f"What drives the cost of {tag_noun or name.lower().replace(' financing','')}", "<ul>" + "".join(f"<li>{x}</li>" for x in drivers) + "</ul>")] + extra_sections,
        options=std_options(tag_noun or name.lower().replace(" financing", ""), insurance=insurance, equity=equity), amounts=amounts, terms=terms,
        qualify=std_qualify(), faqs=faqs + common_faqs(name.lower(), name), related=related,
        service_name=f"{name} matching", audience="Homeowners",
    )

PLUMBING = trade("plumbing-financing", "Plumbing financing",
    "Plumbing financing: repipes, sewer lines and emergency repairs", "Plumbing Financing | Repipe, Sewer Line & Emergency Plumbing Loans | AL Elite",
    "Plumbing financing for repipes, sewer line replacement, slab leaks and emergency repairs: fast options, what drives the cost, example monthly payments and what lenders look for. AL Elite matches you with lenders.",
    "Plumbing financing covers the jobs that can't wait: a burst pipe, a failed sewer line, a slab leak or a whole-house repipe. Because most plumbing emergencies need same-week action, the practical options are a personal loan or a contractor-arranged plan; larger repipes may suit a home equity product. AL Elite matches homeowners with lenders who fund plumbing work.",
    "Plumbing or water heater",
    ["<strong>Access.</strong> Pipes under a slab, behind tile or inside finished walls cost more to reach than exposed lines.", "<strong>Scope.</strong> A single repair, a partial repipe or a whole-house repipe are different jobs with different price points.", "<strong>Sewer line method.</strong> Trenchless lining or bursting avoids digging up the yard but isn't always possible.", "<strong>Material.</strong> PEX, copper and CPVC have different material and labor costs.", "<strong>Permits and inspection.</strong> Required for most repipes and sewer work; cost varies by city."],
    [("Plumbing emergencies and the speed of money", """<p>A sewer backup or a burst pipe doesn't allow time to shop for a home equity line. Online personal loans and contractor payment plans typically fund fastest. If the long-term fix is expensive, some homeowners use a fast option for the emergency repair and a cheaper, slower option for the full repipe later.</p><p>Check your homeowners policy too. Sudden pipe bursts are often covered; gradual leaks and wear usually aren't.</p>""")],
    [("Can you finance plumbing repairs?", "Yes. Personal loans, contractor-arranged plans and promotional-rate cards are used for repairs; home equity products suit larger repipes and sewer replacements. AL Elite matches you with lenders who fund plumbing work."),
     ("Does insurance cover a sewer line replacement?", "Standard policies often exclude sewer lines unless you have a service-line endorsement. Sudden, accidental water damage inside the home is more commonly covered than the line itself. Check your policy and ask your insurer in writing."),
     ("Can I finance a whole-house repipe?", "Yes. Repipes are among the larger plumbing projects and are financed through personal loans or home equity products. A written scope with material and permit costs helps the lender size the loan.")],
    [("Water heater financing", "/water-heater-financing/"), ("HVAC financing", "/hvac-financing/"), ("Foundation repair financing", "/foundation-repair-financing/"), ("Plumbing business loans (for plumbers)", "/contractor-business-loans/plumbing/")],
    [3000, 8000, 15000], ["Burst pipes, slab leaks, sewer lines, repipes", "Fast options for emergencies", "Larger amounts for whole-house work"], tag_noun="plumbing work")

WATER_HEATER = trade("water-heater-financing", "Water heater financing",
    "Water heater financing: tank and tankless replacement without the up-front hit", "Water Heater Financing | Tank & Tankless Replacement Loans | AL Elite",
    "Water heater financing for tank, tankless and heat pump water heaters: fast options for a failed unit, rebates, example payments and what lenders look for. AL Elite matches you with lenders.",
    "Water heater financing is usually a smaller, faster loan: a failed tank needs replacing within days, and the amounts suit short-term personal loans, contractor payment plans or promotional-rate cards. Tankless and heat pump water heaters cost more up front and may qualify for rebates. AL Elite matches homeowners with lenders who fund water heater replacement.",
    "Plumbing or water heater",
    ["<strong>Type.</strong> Standard tank, tankless (on-demand), heat pump (hybrid) and solar water heaters span a wide price range.", "<strong>Fuel and venting.</strong> Switching from gas to electric, or installing tankless, can require new venting, gas lines or electrical work.", "<strong>Capacity.</strong> Larger households need larger tanks or higher-flow tankless units.", "<strong>Code requirements.</strong> Expansion tanks, pans, seismic straps and permits vary by jurisdiction.", "<strong>Removal and disposal.</strong> Usually included, but confirm."],
    [("Rebates for efficient water heaters", """<p>Heat pump water heaters in particular often qualify for utility rebates and, in some years, federal tax credits. Programs change; check with your utility and a tax professional. Rebates typically arrive after installation, so plan to finance the full amount and apply the rebate afterward.</p>""")],
    [("Can I finance a water heater?", "Yes. Water heaters are commonly financed with short-term personal loans, contractor payment plans or promotional-rate credit cards. Higher-cost tankless and heat pump units are sometimes bundled into larger plumbing or HVAC financing."),
     ("Is a tankless water heater worth financing?", "It depends on your hot water use, energy prices and how long you'll stay. Tankless units cost more up front and may last longer and run cheaper. Compare the monthly payment against expected savings, and check for rebates."),
     ("How fast can a water heater loan fund?", "Short-term personal loans and contractor plans often fund within days of approval. We show you each lender's typical timeline before you apply.")],
    [("Plumbing financing", "/plumbing-financing/"), ("HVAC financing", "/hvac-financing/"), ("HVAC financing with bad credit", "/hvac-financing/bad-credit-hvac-financing/")],
    [1800, 3500, 6000], ["Tank, tankless and heat pump units", "Small, fast loans", "Rebate-aware guidance"], terms=(12, 24, 36, 60), tag_noun="a water heater")

SOLAR = trade("solar-financing", "Solar financing",
    "Solar panel financing: loans, leases and PPAs, and which one you actually own", "Solar Panel Financing | Solar Loans vs Leases vs PPAs | AL Elite",
    "Solar panel financing explained: solar loans, leases and power purchase agreements compared, dealer fees, tax credits, example monthly payments and lender requirements. AL Elite matches you with lenders.",
    "Solar financing comes in three forms: a solar loan (you own the system), a lease (the installer owns it and you pay a monthly fee) and a power purchase agreement (you buy the electricity). Only a loan builds equity in the system and lets you claim any available tax credit yourself. AL Elite matches homeowners with lenders who fund solar installations and explains the dealer-fee question before you sign.",
    "Solar",
    ["<strong>System size.</strong> Priced per watt installed; larger systems cost more but often less per watt.", "<strong>Battery storage.</strong> Adding a battery can add substantially to the cost, and may qualify for separate incentives.", "<strong>Roof condition.</strong> If the roof needs replacing within the system's life, do it first. Many homeowners finance <a href='/roof-financing/'>roof</a> and solar together.", "<strong>Electrical upgrades.</strong> Panel upgrades or service changes are common on older homes.", "<strong>Dealer fees.</strong> Low-APR solar loans often carry a dealer fee built into the price. Ask for the cash price and the financed price side by side."],
    [("Solar loans vs leases vs PPAs", """<div class='compare'>
<div class='opt'><h3>Solar loan</h3><p>You borrow, you own the system, you claim any tax credit for which you qualify.</p><p class='pro'>Homeowners who plan to stay and want the long-term savings.</p><p class='con'>Dealer fees on low-APR loans can inflate the price. Compare the cash price.</p></div>
<div class='opt'><h3>Solar lease</h3><p>The installer owns the system; you pay a fixed monthly amount, often with an annual escalator.</p><p class='pro'>No up-front cost and no maintenance responsibility.</p><p class='con'>You don't own it, don't get the credit, and the lease complicates a home sale.</p></div>
<div class='opt'><h3>Power purchase agreement</h3><p>You buy the power the panels produce at a set rate per kWh.</p><p class='pro'>Lowest commitment; pay only for production.</p><p class='con'>Same ownership and resale issues as a lease; rates may escalate.</p></div></div>
<p>Tax credit rules for residential solar have changed and may change again. Confirm current eligibility with a tax professional before counting on a credit in your financing math.</p>""")],
    [("Can you finance solar panels?", "Yes. Solar loans, leases and power purchase agreements are the three main structures. A loan is the only one where you own the system. AL Elite matches you with lenders who fund solar installations."),
     ("What is a dealer fee on a solar loan?", "A fee the installer pays the lender to offer a low APR, usually passed into the system price. It's why the financed price is often higher than the cash price. Always ask for both prices and compare the total cost, not just the rate."),
     ("Does solar financing require good credit?", "Solar loans tend to have stricter credit requirements than some other home improvement loans because of the amounts and terms involved. Leases and PPAs have their own criteria. We'll tell you which lenders fit your profile.")],
    [("Roof financing", "/roof-financing/"), ("Generator financing", "/generator-financing/"), ("Solar financing for installers", "/for-contractors/solar/")],
    [15000, 25000, 40000], ["Loans, leases and PPAs explained", "Dealer-fee transparency", "Roof + solar together"], terms=(60, 120, 180, 240), tag_noun="a solar installation")

SIDING = trade("siding-financing", "Siding financing",
    "Siding financing: vinyl, fiber cement and storm-damage replacement", "Siding Financing | Vinyl, Fiber Cement & Storm Damage Siding Loans | AL Elite",
    "Siding financing for vinyl, fiber cement, wood and engineered siding, including hail and wind damage replacement alongside a roof. Options, example payments and lender requirements. AL Elite matches you with lenders.",
    "Siding financing covers full or partial siding replacement, which often happens alongside roof work after hail or wind damage. The common routes are a personal loan, contractor-arranged financing or, for larger whole-house jobs, a home equity product. AL Elite matches homeowners with lenders who fund exterior projects and can combine roof and siding into one request.",
    "Siding, gutters or windows",
    ["<strong>Material.</strong> Vinyl is the baseline; fiber cement, engineered wood, cedar and stone veneer cost more.", "<strong>Square footage and stories.</strong> Two-story homes cost more per square foot for labor and access.", "<strong>Removal and sheathing repair.</strong> Rot behind old siding is common and only visible after tear-off.", "<strong>Insulation and house wrap.</strong> Often added during replacement and worth it for energy performance.", "<strong>Trim, soffit and fascia.</strong> Frequently replaced at the same time."],
    [("Siding and roof together after a storm", """<p>Hail that damages a roof usually damages siding on the windward side too. Insurers often handle both in one claim, and contractors often quote both together. If you're financing the gap between the claim payout and the full job, one loan for roof plus siding is simpler than two. Tell us both in your request. See our <a href="/blog/does-insurance-cover-roof-replacement/">guide to insurance claims</a> for the process.</p>""")],
    [("Can you finance siding?", "Yes. Siding replacement is financed through personal loans, contractor-arranged plans and home equity products. It's often combined with roof financing after storm damage."),
     ("Will insurance pay for siding damage?", "Sudden hail or wind damage is often covered, subject to the deductible and policy terms. Matching issues arise when only one side is damaged and the old siding is discontinued; some states have matching rules, some don't. Ask your adjuster in writing."),
     ("Is fiber cement worth financing over vinyl?", "Fiber cement costs more up front and is more durable and fire-resistant. Whether the extra cost is worth financing depends on how long you'll stay and local resale expectations.")],
    [("Roof financing", "/roof-financing/"), ("Gutter financing", "/gutter-financing/"), ("Window replacement financing", "/window-financing/"), ("Does insurance cover roof replacement?", "/blog/does-insurance-cover-roof-replacement/")],
    [8000, 15000, 25000], ["Vinyl, fiber cement, wood, stone veneer", "Storm-damage replacement", "Roof and siding in one request"], insurance=True, tag_noun="siding")

GUTTER = trade("gutter-financing", "Gutter financing",
    "Gutter financing: seamless gutters, guards and drainage fixes", "Gutter Financing | Seamless Gutters & Gutter Guard Loans | AL Elite",
    "Gutter financing for seamless gutter replacement, gutter guards, downspouts and drainage work, often alongside a new roof. Small-loan options, example payments and what lenders look for. AL Elite matches you with lenders.",
    "Gutter financing is typically a small, short loan for seamless gutter replacement, gutter guards or drainage work, frequently done at the same time as a new roof. Short-term personal loans, contractor plans and promotional-rate cards fit most gutter jobs; larger packages are bundled into roof financing. AL Elite matches homeowners with lenders who fund exterior work.",
    "Siding, gutters or windows",
    ["<strong>Linear feet and stories.</strong> Priced per foot; second-story work costs more.", "<strong>Material.</strong> Aluminum is standard; copper and steel cost more.", "<strong>Gutter guards.</strong> A meaningful add-on; quality and price vary widely.", "<strong>Fascia repair.</strong> Rotten fascia behind old gutters is a common surprise.", "<strong>Drainage.</strong> Extensions, drains and grading fixes if water is reaching the foundation."],
    [("Why gutters belong in the roof conversation", """<p>Gutters are removed and reinstalled during a roof replacement, so it's the cheapest moment to replace them. Many homeowners add gutters to the roof quote and finance the two together. Failing gutters are also one of the leading causes of <a href="/foundation-repair-financing/">foundation</a> and basement water problems, which cost far more to fix than the gutters themselves.</p>""")],
    [("Can you finance gutters?", "Yes. Gutter replacement and gutter guards are financed through short-term personal loans, contractor payment plans and promotional-rate cards, or bundled into roof financing."),
     ("Is it cheaper to replace gutters with a roof?", "Usually. The gutters come off during a roof job anyway, so labor overlaps. Ask the roofer to quote both."),
     ("Are gutter guards worth financing?", "If you have heavy tree cover or a steep, hard-to-reach roof, guards can reduce maintenance and ladder risk. Quality varies a lot; get the product name and warranty in writing.")],
    [("Roof financing", "/roof-financing/"), ("Siding financing", "/siding-financing/"), ("Foundation repair financing", "/foundation-repair-financing/"), ("Roof repair financing", "/roof-financing/roof-repair-financing/")],
    [2000, 4000, 7000], ["Seamless gutters, guards, downspouts", "Small, short loans", "Bundle with a roof"], terms=(12, 24, 36, 60), tag_noun="gutters")

WINDOWS = trade("window-financing", "Window replacement financing",
    "Window replacement financing: whole-house and partial replacement", "Window Replacement Financing | Energy-Efficient Window Loans | AL Elite",
    "Window replacement financing for whole-house and partial replacements: what drives the cost, dealer financing vs your own loan, energy rebates, example payments and lender requirements. AL Elite matches you with lenders.",
    "Window replacement financing covers full-house or partial window replacement, a project that's usually planned rather than urgent, which gives you time to compare a personal loan, dealer financing and a home equity product. AL Elite matches homeowners with lenders who fund window projects and explains the promotional plans window dealers commonly offer.",
    "Siding, gutters or windows",
    ["<strong>Number and size of windows.</strong> The biggest factor; whole-house jobs scale quickly.", "<strong>Frame material.</strong> Vinyl, fiberglass, composite, wood-clad and aluminum span a wide range.", "<strong>Glass package.</strong> Double vs triple pane, low-E coatings and gas fills affect price and efficiency.", "<strong>Installation type.</strong> Insert (pocket) replacement is cheaper than full-frame replacement.", "<strong>Custom shapes and egress requirements.</strong> Bay, bow and arched windows, plus code-required egress sizes in bedrooms."],
    [("Dealer financing vs your own loan", """<p>Window companies are among the most aggressive users of in-home financing, and the plans vary from fair to expensive. The common trap is deferred interest: a "no interest if paid in full in 18 months" plan that charges all the back interest if you're a month late. A fixed-rate personal loan has no such clause. AL Elite shows you both so you can compare the total cost, not just the pitch.</p>""")],
    [("Can you finance window replacement?", "Yes. Window replacement is financed through personal loans, dealer or contractor-arranged plans and home equity products for larger whole-house jobs."),
     ("Should I use the window company's financing?", "Compare it with an independent loan. Dealer plans can be good, but deferred-interest promotions carry a sting if not paid in full on time. Ask for the APR after the promo period and whether interest is deferred or waived."),
     ("Do new windows qualify for rebates or credits?", "Energy-efficient windows have qualified for utility rebates and federal tax credits in some years. Rules change; check with your utility and a tax professional before relying on them.")],
    [("Siding financing", "/siding-financing/"), ("Roof financing", "/roof-financing/"), ("Home improvement financing", "/home-improvement-financing/")],
    [8000, 15000, 25000], ["Whole-house and partial replacement", "Dealer plan vs independent loan", "Rebate-aware"], tag_noun="window replacement")

FOUNDATION = trade("foundation-repair-financing", "Foundation repair financing",
    "Foundation repair financing: piers, slab repair and basement waterproofing", "Foundation Repair Financing | Piers, Slab & Basement Waterproofing Loans | AL Elite",
    "Foundation repair financing for piering, slab repair, crawl space work and basement waterproofing: why it can't wait, what drives the cost, example payments and lender requirements. AL Elite matches you with lenders.",
    "Foundation repair financing covers structural work such as piering, slab lifting, wall anchors, crawl space encapsulation and basement waterproofing. These are larger, non-optional projects, so personal loans and home equity products are the usual routes, with contractor financing available from many foundation specialists. AL Elite matches homeowners with lenders who fund structural repairs.",
    "Foundation repair",
    ["<strong>Repair method.</strong> Push piers, helical piers, slab jacking, carbon fiber straps and wall anchors are priced very differently.", "<strong>Number of piers.</strong> Pier-based repairs are priced per pier; the engineer's plan sets the count.", "<strong>Soil and access.</strong> Expansive clay soils (common in Texas, Oklahoma and Colorado) and tight access raise cost.", "<strong>Water management.</strong> Drainage, sump systems and waterproofing are often needed to stop the cause, not just the symptom.", "<strong>Engineering and permits.</strong> A structural engineer's report is often required and worth paying for independently."],
    [("Why foundation work is hard to postpone", """<p>Foundation movement doesn't stabilise on its own, and the longer it continues the more it costs to correct and the more it affects everything above it: doors, floors, plumbing, roof lines. Lenders understand this; a foundation repair is treated as a necessary repair rather than a discretionary improvement. If you're selling, unrepaired foundation issues usually surface in inspection and reduce offers by more than the repair costs.</p><p>Get an independent structural engineer's report before signing a repair contract. It protects you from both under- and over-scoped repairs, and lenders view it favourably.</p>""")],
    [("Can you finance foundation repair?", "Yes. Foundation repair is financed through personal loans, home equity products and contractor-arranged plans from foundation specialists. Because it's a necessary structural repair, lenders are used to funding it."),
     ("Does homeowners insurance cover foundation repair?", "Usually not for settling, soil movement or poor drainage. Sudden events such as a burst pipe undermining the slab are sometimes covered. Check your policy and ask your insurer in writing."),
     ("Can I finance basement waterproofing?", "Yes. Interior drainage systems, sump pumps, exterior membranes and crawl space encapsulation are financed through the same channels as foundation repair, and often bundled with it.")],
    [("Plumbing financing", "/plumbing-financing/"), ("Gutter financing", "/gutter-financing/"), ("Home improvement financing", "/home-improvement-financing/")],
    [8000, 15000, 30000], ["Piers, slab repair, wall anchors, waterproofing", "Larger amounts and longer terms", "Engineer-report guidance"], tag_noun="foundation repair")

FLOORING = trade("flooring-financing", "Flooring financing",
    "Flooring financing: hardwood, tile, LVP and carpet", "Flooring Financing | Hardwood, Tile, LVP & Carpet Loans | AL Elite",
    "Flooring financing for hardwood, engineered wood, tile, luxury vinyl plank and carpet: what drives the cost, retailer plans vs your own loan, example payments and lender requirements. AL Elite matches you with lenders.",
    "Flooring financing covers new floors across one room or the whole house. It's a planned project, so you can compare a personal loan, a flooring retailer's promotional plan and, for large jobs, a home equity product. AL Elite matches homeowners with lenders who fund interior projects and explains how retailer promotions work.",
    "Flooring",
    ["<strong>Material.</strong> Carpet and laminate at the low end, luxury vinyl plank in the middle, tile and solid hardwood at the top, with wide ranges inside each.", "<strong>Square footage.</strong> Priced per square foot installed.", "<strong>Subfloor condition.</strong> Levelling, moisture issues and rotten subfloor add labor.", "<strong>Removal and disposal.</strong> Tearing out old tile is particularly labor-intensive.", "<strong>Stairs, transitions and trim.</strong> Often quoted separately and easy to overlook."],
    [("Retailer promotions and the deferred-interest clause", """<p>Big flooring retailers lean heavily on "no interest for X months" plans. These work if you pay the balance in full before the deadline. If you don't, many charge all the interest from day one. A fixed-rate personal loan removes that risk. Compare both before deciding. If you're financing floors as part of a larger remodel, see our <a href="/remodel-financing/kitchen/">kitchen</a> and <a href="/remodel-financing/bathroom/">bathroom</a> remodel pages.</p>""")],
    [("Can you finance flooring?", "Yes. Flooring is financed through personal loans, retailer or contractor promotional plans and, for whole-house jobs, home equity products."),
     ("Is flooring store financing a good deal?", "It can be, if you pay in full inside the promotional window. Deferred-interest plans charge back-interest if you don't. Ask whether interest is deferred or waived and what the standard APR is."),
     ("How long should I finance floors for?", "Match the term to the floor's life and your budget. Carpet has a shorter life than hardwood or tile; a shorter term keeps you from paying for floors you've already replaced.")],
    [("Kitchen remodel financing", "/remodel-financing/kitchen/"), ("Bathroom remodel financing", "/remodel-financing/bathroom/"), ("Home improvement financing", "/home-improvement-financing/")],
    [4000, 8000, 15000], ["Hardwood, tile, LVP, carpet", "Retailer plan vs independent loan", "Whole-house options"], terms=(24, 36, 60, 84), tag_noun="new flooring")

POOL = trade("pool-financing", "Pool financing",
    "Pool financing: in-ground and above-ground pools, and the term that fits", "Pool Financing | In-Ground & Above-Ground Pool Loans | AL Elite",
    "Pool financing for in-ground and above-ground pools: pool loans vs home equity, what drives the cost, builder financing, example monthly payments and lender requirements. AL Elite matches you with lenders.",
    "Pool financing is one of the larger home improvement loans, and in-ground pools are often financed over long terms through a dedicated pool loan (an unsecured personal loan sized for pools) or a home equity product. Above-ground pools suit smaller, shorter loans. AL Elite matches homeowners with lenders who fund pool construction and explains how pool builders' financing partners work.",
    "Pool",
    ["<strong>Type.</strong> Above-ground, vinyl liner, fiberglass and gunite (concrete) in-ground pools occupy very different price bands.", "<strong>Size and features.</strong> Spas, water features, heaters, automation and lighting add up fast.", "<strong>Site work.</strong> Excavation, soil conditions, drainage and access for equipment.", "<strong>Decking and fencing.</strong> Code-required barriers and the surrounding hardscape are often quoted separately.", "<strong>Permits and inspections.</strong> Required everywhere; cost varies."],
    [("Pool loans vs home equity", """<p>Because pools are expensive and long-lived, both unsecured pool loans and home equity products are common. Unsecured loans fund faster and keep the house out of it, at a higher rate. Home equity products take longer and cost more to set up, at a lower rate over a long term. Many pool builders offer financing through lender partners; compare their offer against an independent one before signing. Add in ongoing costs (chemicals, electricity, maintenance, insurance) when deciding what payment is comfortable.</p>""")],
    [("Can you finance a pool?", "Yes. In-ground pools are financed through dedicated pool loans, home equity products and builder-arranged financing. Above-ground pools suit smaller personal loans or retailer plans."),
     ("How long can you finance a pool?", "Unsecured pool loans commonly run several years; home equity products can run considerably longer. A longer term lowers the payment and raises total interest. Use the payment table on this page to compare."),
     ("Does a pool add value to a home?", "It depends on your market and climate. In warm-weather regions pools are often expected; elsewhere they can be neutral or negative for some buyers. Finance a pool because you'll use it, not as an investment.")],
    [("Deck financing", "/deck-financing/"), ("Landscaping financing", "/landscaping-financing/"), ("Fence financing", "/fence-financing/"), ("Home improvement financing", "/home-improvement-financing/")],
    [25000, 45000, 75000], ["In-ground and above-ground", "Pool loans vs home equity", "Builder financing compared"], terms=(60, 84, 120, 180), tag_noun="a pool")

KITCHEN = dict(trade("remodel-financing/kitchen", "Kitchen remodel financing",
    "Kitchen remodel financing: from a refresh to a full gut", "Kitchen Remodel Financing | Kitchen Renovation Loans | AL Elite",
    "Kitchen remodel financing for refreshes, mid-range and full renovations: personal loans vs home equity vs cash-out refinance, what drives the cost, example payments and lender requirements. AL Elite matches you with lenders.",
    "Kitchen remodel financing depends on scope. A refresh (counters, paint, hardware) fits a personal loan; a mid-range remodel can go either way; a full gut with layout changes usually points to a home equity product because of the amount. AL Elite matches homeowners with lenders who fund renovations and helps you decide which structure fits the size of the job.",
    "Kitchen or bathroom remodel",
    ["<strong>Layout changes.</strong> Moving plumbing, gas or load-bearing walls is where budgets double.", "<strong>Cabinets.</strong> Typically the largest line item; stock, semi-custom and custom span a wide range.", "<strong>Countertops and appliances.</strong> Material choices swing the number significantly.", "<strong>Electrical and code upgrades.</strong> Older kitchens often need new circuits and GFCI work.", "<strong>Contingency.</strong> Remodels uncover surprises. Lenders prefer a budget with 10 to 15 percent held back."],
    [("Which financing fits which kitchen", """<div class='compare'>
<div class='opt'><h3>Refresh</h3><p>Counters, backsplash, paint, hardware, maybe appliances. No layout change.</p><p class='pro'>Personal loan or promotional-rate card.</p><p class='con'>Keep the term short; cosmetic work doesn't justify a decade of payments.</p></div>
<div class='opt'><h3>Mid-range remodel</h3><p>New cabinets, counters, flooring, lighting. Layout mostly unchanged.</p><p class='pro'>Personal loan or HELOC, depending on amount and how fast you need funds.</p><p class='con'>Compare total interest; HELOC rates are usually lower but variable.</p></div>
<div class='opt'><h3>Full renovation</h3><p>Layout changes, structural work, everything new.</p><p class='pro'>Home equity loan, HELOC or cash-out refinance.</p><p class='con'>Weeks to close, closing costs, and your home is collateral.</p></div></div>""")],
    [("Can you finance a kitchen remodel?", "Yes. Kitchen remodels are financed through personal loans for smaller jobs and home equity products or cash-out refinances for larger ones. Contractor-arranged plans are also common."),
     ("Is a HELOC better than a personal loan for a kitchen?", "A HELOC usually has a lower, variable rate and a longer draw period, which suits a project paid in stages. A personal loan is faster, fixed and unsecured. For a mid-range remodel either can work; the right answer depends on how much equity you have, how fast you need funds and your comfort with a variable rate."),
     ("How much should I budget for surprises?", "Remodelers commonly recommend holding 10 to 15 percent of the budget in reserve. A lender is more comfortable with a request that includes contingency than one that will need a second loan halfway through.")],
    [("Bathroom remodel financing", "/remodel-financing/bathroom/"), ("Flooring financing", "/flooring-financing/"), ("Plumbing financing", "/plumbing-financing/"), ("Home improvement financing", "/home-improvement-financing/"), ("Are you a remodeler? Offer financing", "/for-contractors/remodeling/")],
    [15000, 30000, 60000], ["Refresh to full renovation", "Personal loan vs home equity", "Contingency-aware budgeting"], terms=(60, 84, 120, 180), tag_noun="a kitchen remodel"),
    crumbs=[HOME, HUB, ("Kitchen remodel financing", "/remodel-financing/kitchen/")])

BATHROOM = dict(trade("remodel-financing/bathroom", "Bathroom remodel financing",
    "Bathroom remodel financing: tub-to-shower conversions to full renovations", "Bathroom Remodel Financing | Bathroom Renovation Loans | AL Elite",
    "Bathroom remodel financing for tub-to-shower conversions, accessibility upgrades and full renovations: options by scope, what drives the cost, example payments and lender requirements. AL Elite matches you with lenders.",
    "Bathroom remodel financing ranges from a short personal loan for a tub-to-shower conversion to a home equity product for a full primary-bath renovation. Accessibility upgrades such as walk-in showers and grab bars are a common, often urgent reason to remodel. AL Elite matches homeowners with lenders who fund renovations and explains the one-day-bath promotional plans.",
    "Kitchen or bathroom remodel",
    ["<strong>Scope.</strong> A fixture swap, a tub-to-shower conversion and a full gut are very different jobs.", "<strong>Tile and fixtures.</strong> Material choices drive a large share of the cost.", "<strong>Plumbing changes.</strong> Moving the toilet or shower drain adds significant labor.", "<strong>Waterproofing and ventilation.</strong> Non-negotiable and sometimes overlooked in cheap quotes.", "<strong>Accessibility features.</strong> Curbless showers, wider doors and grab bars; some may qualify for assistance programs."],
    [("Accessibility remodels and timing", """<p>Many bathroom remodels are driven by a change in mobility: a parent moving in, an injury, aging in place. These projects can't always wait for a slow financing process. Personal loans and contractor plans fund fastest. Some states and non-profits offer grants or low-cost loans for accessibility modifications; check before borrowing. The "one-day bath" companies advertise heavily and usually offer in-home financing; compare their total price and plan terms with an independent quote and loan.</p>""")],
    [("Can you finance a bathroom remodel?", "Yes. Smaller bathroom jobs are financed through personal loans and contractor plans; full renovations may suit a home equity product."),
     ("How much can I borrow for a bathroom?", "That depends on the lender, your credit and income. Unsecured personal loans cap out at amounts that vary by lender; home equity products depend on your available equity. Tell us the scope and we'll match you with lenders whose limits fit."),
     ("Are accessibility bathroom upgrades covered by insurance or grants?", "Health insurance generally doesn't cover home modifications. Some state programs, veterans' programs and non-profits do offer help. Check those first; then finance any remainder.")],
    [("Kitchen remodel financing", "/remodel-financing/kitchen/"), ("Plumbing financing", "/plumbing-financing/"), ("Flooring financing", "/flooring-financing/"), ("Home improvement financing", "/home-improvement-financing/")],
    [8000, 15000, 30000], ["Conversions, accessibility, full remodels", "Fast options when mobility changes", "One-day-bath plans compared"], tag_noun="a bathroom remodel"),
    crumbs=[HOME, HUB, ("Bathroom remodel financing", "/remodel-financing/bathroom/")])

FENCE = trade("fence-financing", "Fence financing",
    "Fence financing: wood, vinyl, chain link and privacy fences", "Fence Financing | Wood, Vinyl & Privacy Fence Loans | AL Elite",
    "Fence financing for wood, vinyl, aluminum and chain link fences: small-loan options, contractor plans, what drives the cost, example payments and lender requirements. AL Elite matches you with lenders.",
    "Fence financing is usually a small to mid-size loan for a new or replacement fence. Short-term personal loans, contractor payment plans and promotional-rate cards fit most fence projects; long runs of vinyl or ornamental fencing can push into larger-loan territory. AL Elite matches homeowners with lenders who fund outdoor projects.",
    "Fence, deck or landscaping",
    ["<strong>Linear feet.</strong> Fencing is priced per foot; corner lots and large yards add up.", "<strong>Material.</strong> Chain link at the low end, wood in the middle, vinyl, composite and aluminum above.", "<strong>Height and style.</strong> Privacy fences cost more than picket; decorative tops add cost.", "<strong>Gates.</strong> Each gate, especially driveway gates, adds materially.", "<strong>Site conditions.</strong> Slopes, rock, tree roots and old-fence removal."],
    [("Fences, HOAs and permits", """<p>Before financing a fence, confirm HOA rules (height, material, color) and local permit requirements. Replacing a fence a neighbor shares can also involve cost-sharing agreements. A fence built to the wrong spec is one of the few projects you can be made to tear down, which is a bad outcome when you're still paying for it.</p>""")],
    [("Can you finance a fence?", "Yes. Fences are financed through short-term personal loans, contractor payment plans and promotional-rate credit cards, or bundled with other outdoor work."),
     ("Is it worth financing a fence?", "For safety (children, pets, pools) or privacy, often yes. Keep the term short so the loan ends well before the fence needs replacing."),
     ("Can I include a fence in a pool loan?", "Usually. Pool barriers are code-required, and pool builders often include fencing in the quote. Tell us if you want them financed together.")],
    [("Pool financing", "/pool-financing/"), ("Deck financing", "/deck-financing/"), ("Landscaping financing", "/landscaping-financing/")],
    [3000, 6000, 12000], ["Wood, vinyl, aluminum, chain link", "Small, short loans", "Bundle with pool or deck"], terms=(12, 24, 36, 60), tag_noun="a fence")

DECK = trade("deck-financing", "Deck financing",
    "Deck financing: wood and composite decks, patios and covers", "Deck Financing | Composite & Wood Deck Loans | AL Elite",
    "Deck financing for wood and composite decks, patio covers and outdoor living spaces: options, what drives the cost, example payments and lender requirements. AL Elite matches you with lenders.",
    "Deck financing covers new decks, deck replacement and outdoor living additions such as patio covers and screened porches. Personal loans and contractor plans fit most decks; large composite builds with roofs or kitchens may suit a home equity product. AL Elite matches homeowners with lenders who fund outdoor projects.",
    "Fence, deck or landscaping",
    ["<strong>Square footage and height.</strong> Elevated decks need more structure, stairs and railings.", "<strong>Material.</strong> Pressure-treated wood is the baseline; cedar, composite and PVC cost more and last longer.", "<strong>Railings and stairs.</strong> Often a surprising share of the total.", "<strong>Covers, screens and lighting.</strong> Turn a deck into an outdoor room, and a bigger loan.", "<strong>Permits and inspections.</strong> Required for most decks; ledger attachment and footings are inspected."],
    [("Matching the term to the material", """<p>A pressure-treated deck and a composite deck have very different lifespans, which should shape how long you finance. Composite costs more and lasts longer, so a longer term is more defensible. Whichever you choose, get the structural details (footings, ledger flashing, joist spacing) in the quote. Deck failures are a safety issue, and a cheap quote that skips them isn't cheap.</p>""")],
    [("Can you finance a deck?", "Yes. Decks are financed through personal loans, contractor-arranged plans and, for large outdoor living builds, home equity products."),
     ("Is composite decking worth financing over wood?", "Composite costs more up front and needs less maintenance over a longer life. If you'll stay in the home long enough to benefit, it's often worth the larger loan. If not, wood with a shorter loan may be the better choice."),
     ("Do I need a permit for a deck?", "Almost always, for anything attached to the house or above a certain height. Your contractor should pull it. Unpermitted decks cause problems at sale and with insurance.")],
    [("Pool financing", "/pool-financing/"), ("Fence financing", "/fence-financing/"), ("Landscaping financing", "/landscaping-financing/")],
    [6000, 12000, 25000], ["Wood, composite, covers, screens", "Term matched to material life", "Outdoor living builds"], tag_noun="a deck")

GENERATOR = trade("generator-financing", "Generator financing",
    "Generator financing: standby generators for storm-prone homes", "Generator Financing | Whole-House Standby Generator Loans | AL Elite",
    "Generator financing for whole-house standby generators and transfer switches: why storm-market homeowners finance them, what drives the cost, example payments and lender requirements. AL Elite matches you with lenders.",
    "Generator financing covers standby (whole-house) generators, transfer switches and the gas or propane work that goes with them. It's a popular project in hurricane and winter-storm markets where multi-day outages are a real risk. Personal loans and dealer-arranged plans fit most installations; AL Elite matches homeowners with lenders who fund generator projects.",
    "Generator or garage door",
    ["<strong>Generator size (kW).</strong> Partial-house vs whole-house capacity is the main price driver.", "<strong>Fuel.</strong> Natural gas, propane or diesel, and whether a gas line or propane tank must be installed.", "<strong>Transfer switch and electrical work.</strong> Automatic transfer switches and panel work are a large share of the cost.", "<strong>Pad, placement and permits.</strong> Code setbacks from windows and property lines affect placement.", "<strong>Maintenance plan.</strong> Often offered with installation; worth comparing."],
    [("Generators and storm markets", """<p>In the Gulf Coast, Florida and the winter-storm belt, a generator is less a luxury than a backup for the refrigerator, the sump pump, medical equipment and the furnace. Demand spikes after each major event, which is when dealer lead times and prices rise. Financing before the season rather than after the outage usually gets a better install slot and a better price. Many homeowners pair a generator with a <a href="/roof-financing/">roof</a> or <a href="/hvac-financing/">HVAC</a> replacement in the same loan.</p>""")],
    [("Can you finance a standby generator?", "Yes. Standby generators are financed through personal loans, dealer-arranged plans and promotional-rate programs from manufacturers' dealer networks."),
     ("Is a whole-house generator worth financing?", "If your area has frequent multi-day outages, or someone in the home depends on powered medical equipment or climate control, often yes. If outages are rare and short, a portable unit may be enough."),
     ("Does a generator add home value?", "In outage-prone markets it's a selling point; elsewhere it's neutral. Finance it for the resilience, not the resale.")],
    [("HVAC financing", "/hvac-financing/"), ("Roof financing", "/roof-financing/"), ("Solar financing", "/solar-financing/")],
    [8000, 12000, 18000], ["Standby generators and transfer switches", "Storm-season timing", "Pair with roof or HVAC"], tag_noun="a standby generator")

GARAGE = trade("garage-door-financing", "Garage door financing",
    "Garage door financing: replacement doors and openers", "Garage Door Financing | Garage Door Replacement Loans | AL Elite",
    "Garage door financing for replacement doors, openers and storm-rated doors: small-loan options, what drives the cost, example payments and lender requirements. AL Elite matches you with lenders.",
    "Garage door financing is a small, short loan for a replacement door and opener, sometimes with a wind-rated door required in hurricane zones. Short-term personal loans, dealer payment plans and promotional-rate cards fit nearly all garage door projects. AL Elite matches homeowners with lenders who fund smaller home improvements.",
    "Generator or garage door",
    ["<strong>Door size and count.</strong> Single vs double, one door vs two or three.", "<strong>Material and insulation.</strong> Steel, aluminum, wood and composite; insulated doors cost more and are quieter and warmer.", "<strong>Wind rating.</strong> Required in many coastal counties; adds cost.", "<strong>Opener.</strong> Belt-drive, smart openers and battery backup add to the price.", "<strong>Framing repair.</strong> Rotten jambs or headers discovered at removal."],
    [("Garage doors and insurance in hurricane zones", """<p>A garage door is often the largest opening in a house and a common failure point in high winds. In coastal counties a wind-rated door may be required by code and may qualify for insurance mitigation credits. Ask your insurer before choosing a door; the credit can offset part of the payment.</p>""")],
    [("Can you finance a garage door?", "Yes. Garage doors are financed through short-term personal loans, dealer plans and promotional-rate cards. Amounts are small enough that terms of one to three years are typical."),
     ("Is an insulated garage door worth it?", "If the garage is attached, used as a workspace or below living space, yes; it reduces noise and heat transfer. For a detached, unused garage, less so."),
     ("Do wind-rated doors lower insurance?", "In many hurricane-zone states, opening-protection credits apply. Confirm with your insurer in writing.")],
    [("Generator financing", "/generator-financing/"), ("Window replacement financing", "/window-financing/"), ("Home improvement financing", "/home-improvement-financing/")],
    [1800, 3500, 6000], ["Doors, openers, wind-rated doors", "Small, short loans", "Insurance-credit aware"], terms=(12, 24, 36, 60), tag_noun="a garage door")

LANDSCAPING = trade("landscaping-financing", "Landscaping financing",
    "Landscaping financing: hardscape, drainage, irrigation and planting", "Landscaping Financing | Hardscape, Drainage & Yard Project Loans | AL Elite",
    "Landscaping financing for hardscape, retaining walls, drainage, irrigation and planting: options by project size, what drives the cost, example payments and lender requirements. AL Elite matches you with lenders.",
    "Landscaping financing covers everything from a drainage fix to a full backyard build with patios, retaining walls and irrigation. Smaller projects fit personal loans and contractor plans; large hardscape builds can run into home equity territory. AL Elite matches homeowners with lenders who fund outdoor projects.",
    "Fence, deck or landscaping",
    ["<strong>Hardscape.</strong> Patios, walkways, retaining walls and outdoor kitchens are the expensive part.", "<strong>Drainage and grading.</strong> Unglamorous and often necessary; protects the foundation.", "<strong>Irrigation.</strong> Zones, controllers and water-source work.", "<strong>Plants and sod.</strong> Mature trees and large plantings cost far more than starter stock.", "<strong>Access and site conditions.</strong> Slopes, rock and tight access raise labor."],
    [("Finance the drainage before the patio", """<p>Water problems don't respect new hardscape. If the yard sends water toward the house, the drainage and grading should be done first, and they're the part most worth financing because they protect the <a href="/foundation-repair-financing/">foundation</a>. Lenders are also more comfortable with a project that has a defined scope and a licensed contractor than with an open-ended "backyard makeover."</p>""")],
    [("Can you finance landscaping?", "Yes. Landscaping and hardscape are financed through personal loans, contractor-arranged plans and, for large builds, home equity products."),
     ("What landscaping projects are worth financing?", "Drainage and grading that protect the home, retaining walls that address a safety issue, and hardscape you'll use for years. Seasonal plantings and lawn work are better paid from cash."),
     ("How long should I finance a landscaping project?", "Match the term to the life of the work. Hardscape lasts decades; plantings and irrigation components less. Keep terms short for the shorter-lived parts.")],
    [("Deck financing", "/deck-financing/"), ("Fence financing", "/fence-financing/"), ("Pool financing", "/pool-financing/"), ("Landscaping business loans (for landscapers)", "/contractor-business-loans/landscaping/")],
    [5000, 12000, 30000], ["Hardscape, drainage, irrigation", "Scope-matched terms", "Protect the foundation first"], tag_noun="a landscaping project")

# ------------------------------------------------------------------ HUB
HOME_IMPROVEMENT_HUB = dict(
    path="/home-improvement-financing/", crumbs=[HOME, HUB],
    eyebrow="Home improvement financing", h1="Home improvement financing: every project, matched to the right lender",
    title="Home Improvement Financing | Loans by Project Type | AL Elite",
    meta="Home improvement financing by project: roof, HVAC, plumbing, solar, siding, windows, remodels, pools and more. How home improvement loans, home equity and contractor financing compare. AL Elite matches you with lenders.",
    answer="Home improvement financing is any loan or payment plan used to pay for work on your home over time rather than up front. The main types are unsecured home improvement loans (personal loans), contractor-arranged financing, home equity loans and HELOCs, and cash-out refinancing. AL Elite matches homeowners with lenders by project type, because a lender that funds roofs isn't always the right one for a pool.",
    cta_points=["Every trade we cover, one request", "Lenders matched by project type", "Free, no credit pull to start"],
    cards_h2="Financing by project", cards_eyebrow="Pick your project",
    cards=[
        ("Most requested", "Roof financing", "Replacement, repair, metal and storm damage.", "/roof-financing/"),
        ("Urgent", "HVAC financing", "AC, furnace and heat pump replacement.", "/hvac-financing/"),
        ("Repairs", "Plumbing financing", "Repipes, sewer lines, emergencies.", "/plumbing-financing/"),
        ("Repairs", "Water heater financing", "Tank, tankless and heat pump units.", "/water-heater-financing/"),
        ("Energy", "Solar financing", "Loans vs leases vs PPAs.", "/solar-financing/"),
        ("Exterior", "Siding financing", "Vinyl, fiber cement, storm replacement.", "/siding-financing/"),
        ("Exterior", "Gutter financing", "Seamless gutters and guards.", "/gutter-financing/"),
        ("Exterior", "Window replacement financing", "Whole-house and partial.", "/window-financing/"),
        ("Structural", "Foundation repair financing", "Piers, slab, waterproofing.", "/foundation-repair-financing/"),
        ("Interior", "Flooring financing", "Hardwood, tile, LVP, carpet.", "/flooring-financing/"),
        ("Remodel", "Kitchen remodel financing", "Refresh to full renovation.", "/remodel-financing/kitchen/"),
        ("Remodel", "Bathroom remodel financing", "Conversions to full remodels.", "/remodel-financing/bathroom/"),
        ("Outdoor", "Pool financing", "In-ground and above-ground.", "/pool-financing/"),
        ("Outdoor", "Deck financing", "Wood, composite, covers.", "/deck-financing/"),
        ("Outdoor", "Fence financing", "Wood, vinyl, chain link.", "/fence-financing/"),
        ("Outdoor", "Landscaping financing", "Hardscape, drainage, irrigation.", "/landscaping-financing/"),
        ("Resilience", "Generator financing", "Whole-house standby units.", "/generator-financing/"),
        ("Small jobs", "Garage door financing", "Doors and openers.", "/garage-door-financing/"),
    ],
    prose="""<h2>The four ways homeowners finance improvements</h2>
<div class='compare'>
<div class='opt'><h3>Home improvement loan (unsecured personal loan)</h3><p>Fixed amount, fixed rate, fixed term. Funded in days. No lien on your home.</p><p class='pro'>Most projects under the lender's cap, especially urgent ones.</p><p class='con'>Rate depends heavily on credit score.</p></div>
<div class='opt'><h3>Contractor-arranged financing</h3><p>Offered by the contractor through a lender partner, often at proposal stage.</p><p class='pro'>Convenience and promotional offers.</p><p class='con'>Deferred-interest promotions; always compare with an independent loan.</p></div>
<div class='opt'><h3>Home equity loan or HELOC</h3><p>Secured by your home; lower rates and longer terms.</p><p class='pro'>Large projects when you have equity and time.</p><p class='con'>Weeks to close, closing costs, home is collateral.</p></div>
<div class='opt'><h3>Cash-out refinance</h3><p>Replace your mortgage with a larger one and take the difference.</p><p class='pro'>Very large projects when current mortgage rates are favourable.</p><p class='con'>Resets your mortgage; rarely sensible if your existing rate is low.</p></div></div>
<h2>Home improvement loans vs home renovation loans</h2>
<p>People use both phrases to mean the same thing: an unsecured personal loan used for work on the home. Some lenders market "home improvement loans" with slightly different terms or amounts than their general personal loans, but the underwriting is the same. What matters is the APR, the fee, the term and whether the lender funds your kind of project. That last point is why we match by trade.</p>
<h2>How to choose</h2>
<ol><li><strong>Size the project honestly,</strong> with a written quote and a contingency.</li><li><strong>Decide whether your home should be collateral.</strong> If not, you're choosing between a personal loan and contractor financing.</li><li><strong>Decide how fast you need funds.</strong> Emergencies rule out equity products.</li><li><strong>Compare total cost,</strong> not the monthly payment alone. A longer term means a lower payment and more interest.</li><li><strong>Check the credit-inquiry policy</strong> of each lender before you apply. We label this for every lender we match you with.</li></ol>""",
    faqs=[
        ("What is the best way to finance home improvements?", "There's no single best way. Unsecured home improvement loans suit most mid-size and urgent projects; home equity products suit large planned ones; contractor financing suits convenience and sometimes promotional pricing. Compare total cost, speed and whether you want your home as collateral."),
        ("What credit score do you need for a home improvement loan?", "Better rates on unsecured loans typically begin in the mid-600s. Some lenders consider lower scores at higher APRs. Secured products are more forgiving on score but slower."),
        ("Can I get home improvement financing through my contractor?", "Often, yes. Many contractors offer financing through lender partners. AL Elite partner contractors use our network. Compare the contractor's offer with an independent loan before deciding."),
        ("Does AL Elite charge homeowners?", "No. We're paid by lenders and partner contractors. Comparing options through AL Elite is free, and submitting a request does not pull your credit."),
    ],
    related=[("For contractors: offer financing", "/for-contractors/"), ("Roof financing calculator", "/tools/roof-financing-calculator/"), ("How to finance a new roof: 6 options", "/blog/how-to-finance-a-new-roof/"), ("HELOC vs roof loan vs contractor financing", "/blog/heloc-vs-roof-loan/"), ("Locations", "/locations/")],
    project="Other home improvement",
)

CONSUMER_SERVICE_PAGES = [ROOF, ROOF_BAD_CREDIT, ROOF_METAL, ROOF_REPAIR, ROOF_COMMERCIAL, HVAC, HVAC_BAD_CREDIT, PLUMBING, WATER_HEATER, SOLAR, SIDING, GUTTER, WINDOWS, FOUNDATION, FLOORING, POOL, KITCHEN, BATHROOM, FENCE, DECK, GENERATOR, GARAGE, LANDSCAPING]
CONSUMER_HUBS = [HOME_IMPROVEMENT_HUB]
