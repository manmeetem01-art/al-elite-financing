"""20 city pages + locations hub. Local context comes from the strategy's Target Locations tab and two cited sources.
Anything that needs local verification (cost ranges, licensing, rebates) is a clearly marked verify block, never invented."""
from common import *
from expand_cities import local_section
from local_content import CITY, STATE as STATE_HUB, STATE_SLUG
from expand_cities import STATE as STATE_RULES

HOME = ("Home", "/")
LOC = ("Locations", "/locations/")
CLAIMS = "https://www.claimsjournal.com/news/national/2026/04/23/337102.htm"

# city, state name, abbr, slug path, risk type, why (from sheet), local-financing-search note, extra local angle
CITIES = [
    ("Houston", "Texas", "TX", "/locations/texas/houston/", "hurricane", "Hurricane and hail exposure; Texas led the country in hail claim payouts in 2025.", "Houston homeowners search specifically for roof financing, which tells us the need is real and local.", "Gulf Coast humidity shortens shingle life, and wind-rated installation matters for insurance."),
    ("Dallas", "Texas", "TX", "/locations/texas/dallas/", "hail", "The North Texas hail corridor; Texas led the country in hail claim payouts in 2025.", "Dallas roofers and homeowners deal with a spring hail season nearly every year.", "Impact-resistant (Class 4) shingles often earn insurance discounts here; ask your insurer in writing."),
    ("San Antonio", "Texas", "TX", "/locations/texas/san-antonio/", "hail", "Hail and severe-storm exposure in South Texas; Texas led hail payouts in 2025.", "San Antonio has the largest local roof-financing search demand we found in any launch city, with homeowners specifically looking for affordable roof financing.", "Growth on the north side means a lot of roofs of the same age reaching replacement together."),
    ("Fort Worth", "Texas", "TX", "/locations/texas/fort-worth/", "hail", "The western end of the DFW hail corridor; Texas led hail payouts in 2025.", "Fort Worth shares Dallas's spring hail season and its roofer capacity crunch after big events.", "Tarrant County's mix of older housing stock and new subdivisions means both repair and full replacement demand."),
    ("Austin", "Texas", "TX", "/locations/texas/austin/", "hail", "Hail and severe-storm exposure in Central Texas, with fast housing growth.", "Austin's rapid build-out over the last fifteen years means a wave of first-time roof replacements is arriving.", "Energy-efficient and metal roofing are popular here; both change the financing term that makes sense."),
    ("Oklahoma City", "Oklahoma", "OK", "/locations/oklahoma/oklahoma-city/", "hail", "Oklahoma was among the top states for hail claim payouts in 2025.", "Oklahoma City homeowners search for roof financing by name, a signal of real local need.", "Tornado and straight-line wind damage add to hail as reasons roofs get replaced early."),
    ("Tulsa", "Oklahoma", "OK", "/locations/oklahoma/tulsa/", "hail", "Oklahoma was among the top states for hail claim payouts in 2025.", "Tulsa has existing local search demand for roof financing.", "Spring hail and summer wind events drive clustered replacement demand across the metro."),
    ("Denver", "Colorado", "CO", "/locations/colorado/denver/", "hail", "Colorado was among the top states for hail claim payouts in 2025, and the Front Range sees frequent large hail events.", "Denver's late-spring and summer hail season regularly produces large claim events.", "Many Front Range insurers now use roof-age schedules or separate wind/hail deductibles, which increases what homeowners finance."),
    ("Colorado Springs", "Colorado", "CO", "/locations/colorado/colorado-springs/", "hail", "Front Range hail exposure with a high roof-replacement frequency.", "Colorado Springs sees repeat hail events, so many roofs are replaced more than once in a decade.", "Percentage-based wind/hail deductibles are common here and are often the amount homeowners need to finance."),
    ("Kansas City", "Missouri", "MO", "/locations/missouri/kansas-city/", "hail", "Missouri was the second-highest state for hail claim payouts in 2025.", "Kansas City homeowners search for roof financing by name.", "The metro straddles Missouri and Kansas; contractor licensing and insurance rules differ by side."),
    ("St. Louis", "Missouri", "MO", "/locations/missouri/st-louis/", "hail", "Missouri was the second-highest state for hail claim payouts in 2025.", "St. Louis combines a large, older housing stock with regular severe-storm seasons.", "Older roofs and brick homes mean more decking and flashing work in replacement quotes."),
    ("Wichita", "Kansas", "KS", "/locations/kansas/wichita/", "hail", "Kansas was among the top states for hail claim payouts in 2025.", "Wichita homeowners search specifically for roof financing options.", "Wind-driven hail from the southwest is the typical damage pattern, often hitting one side of the roof and siding together."),
    ("Omaha", "Nebraska", "NE", "/locations/nebraska/omaha/", "hail", "Eastern Nebraska has high hail and severe-storm exposure.", "Omaha has strong local roofing demand with little competition for financing information.", "Hail damage to siding and gutters alongside the roof is common, and often financed as one job."),
    ("Indianapolis", "Indiana", "IN", "/locations/indiana/indianapolis/", "hail", "Indiana entered the top ten states for hail claim payouts in 2025.", "Indianapolis has the highest local roofing demand of any city we researched.", "A large stock of homes built in the same post-war and 1990s waves means replacement demand arrives in clusters."),
    ("Minneapolis", "Minnesota", "MN", "/locations/minnesota/minneapolis/", "hail", "Hail in summer and ice-dam and winter damage the rest of the year.", "Minneapolis has high roofing demand driven by both hail and winter.", "Ice dams and freeze-thaw damage mean roofs here are replaced for reasons insurers treat differently from storm damage."),
    ("Tampa", "Florida", "FL", "/locations/florida/tampa/", "hurricane", "Hurricane exposure, plus Florida's roof-age insurance pressure.", "Tampa homeowners search for roof financing by name.", "Many Florida insurers won't renew policies on roofs past a certain age, forcing replacement before the roof has failed."),
    ("Orlando", "Florida", "FL", "/locations/florida/orlando/", "hurricane", "Hurricane and severe-storm exposure, plus Florida's roof-age insurance pressure.", "Orlando has existing local search demand for roofing financing.", "Insurance-driven replacement (to keep or get a policy) is a major reason Orlando homeowners finance roofs."),
    ("Miami", "Florida", "FL", "/locations/florida/miami/", "hurricane", "The highest hurricane exposure in the country, plus Florida's roof-age insurance pressure.", "Miami has high-value local search demand for roof financing.", "High-velocity hurricane zone code requirements raise roofing costs and make wind-rated installation non-negotiable."),
    ("Nashville", "Tennessee", "TN", "/locations/tennessee/nashville/", "hail", "Severe storms, tornadoes and hail in a fast-growing metro.", "Nashville's growth has produced a large stock of similar-age roofs.", "Spring severe-weather season and summer storms drive both repair and replacement."),
    ("Salt Lake City", "Utah", "UT", "/locations/utah/salt-lake-city/", "hail", "Wind, hail and heavy snow loads along the Wasatch Front.", "Salt Lake City and Utah more broadly show existing local search demand for roof financing.", "Snow load and ice damage are the common winter causes of roof replacement here."),
    ("Phoenix", "Arizona", "AZ", "/locations/arizona/phoenix/", "heat", "Extreme heat and monsoon storms; AC failures in July are same-day emergencies.", "Phoenix homeowners search for AC and HVAC financing in summer more than any other project.", "Intense sun and heat shorten the life of AC systems, roofs and exterior finishes."),
    ("Atlanta", "Georgia", "GA", "/locations/georgia/atlanta/", "mixed", "Humid summers, severe spring storms, tornadoes and ice storms.", "Atlanta homeowners search for HVAC and roof financing year-round.", "Red clay and heavy rain make drainage and crawlspace moisture recurring issues."),
    ("Charlotte", "North Carolina", "NC", "/locations/north-carolina/charlotte/", "mixed", "Severe spring storms, occasional hail and tornadoes, hurricane remnants and ice.", "Charlotte homeowners search for HVAC and roof financing as 1990s-era homes reach first replacements.", "Rapid growth means a large wave of first roof and HVAC replacements."),
    ("Raleigh", "North Carolina", "NC", "/locations/north-carolina/raleigh/", "mixed", "Summer storms, hurricane remnants and winter ice across the Triangle.", "Triangle homeowners finance HVAC, roofing and crawlspace work steadily.", "Newer suburban housing is reaching its first replacements."),
    ("Chicago", "Illinois", "IL", "/locations/illinois/chicago/", "hail", "Illinois ranked among the top three states for hail claim payouts in 2025; winters add freeze-thaw damage.", "Chicago homeowners search for roof, furnace and home improvement financing across a century-old housing stock.", "Flat roofs, old masonry and basements make repair a constant."),
    ("Columbus", "Ohio", "OH", "/locations/ohio/columbus/", "hail", "Spring hail and wind, with hot summers and cold winters.", "Columbus homeowners finance roofs, furnaces and basement work.", "Mid-century housing plus fast suburban growth."),
    ("Philadelphia", "Pennsylvania", "PA", "/locations/pennsylvania/philadelphia/", "mixed", "Nor'easters, summer storms and tropical remnants on one of the oldest housing stocks in the country.", "Philadelphia homeowners finance flat roofs, boiler conversions and renovations.", "Rowhouse roofs, old plumbing and basements drive the work."),
]

def by_state():
    out = {}
    for c in CITIES:
        out.setdefault(c[1], []).append(c)
    return out

def city_page_dict(c):
    city, state, ab, path, risk, why, demand, angle = c
    siblings = [s for s in by_state()[state] if s[0] != city]
    sib_html = ", ".join(f"<a href='{s[3]}'>{s[0]}</a>" for s in siblings) if siblings else "none yet"
    risk_label = {"hurricane": "Hurricane and wind", "hail": "Hail and severe storms", "heat": "Heat, sun and monsoon", "mixed": "Storms, heat and age"}[risk]
    storm_para_extra = {
        "heat": f"<p>Roofs and AC systems in {city} wear out from heat and sun rather than storms. {why} Tile roofs need underlayment replacement on a cycle, foam roofs need recoating, and an air conditioner that fails in July is replaced within days, which is why most {city} HVAC replacements are financed at the quote.</p>",
        "mixed": f"<p>{city} roofs and HVAC systems face a mix of exposures rather than one dominant storm type. {why} Insurance claims follow severe storms, but most financed projects here are age-driven replacements and renovations, so homeowners usually have time to compare quotes and financing rather than deciding under storm pressure.</p>",
    }
    storm_para = {
        "hurricane": f"<p>Roofs in {city} are replaced for two reasons that don't apply in most of the country: hurricane and wind damage, and insurer pressure. Florida carriers increasingly decline to renew policies on roofs past a certain age, which means many {city} homeowners replace a roof that hasn't failed yet, on a deadline, to keep coverage. That's a financing event. Wind-rated installation, secondary water barriers and in some zones high-velocity hurricane code compliance raise the cost beyond what a shingle roof costs elsewhere.</p>",
        "hail": f"<p>Roofs in {city} are replaced early because of hail and wind. {why} In 2025 State Farm alone paid out $5.6 billion in hail claims nationally, with Texas the largest state at $1.4 billion, followed by Missouri and Illinois (<a href='{CLAIMS}' rel='noopener'>Claims Journal</a>, April 2026). After a major event, every roofer in the metro is booked for months, prices rise and insurers slow down. The homeowners who get their roof done first are the ones who can fund the deductible and the gap without waiting on the check.</p>",
    } | storm_para_extra
    storm_para = storm_para[risk]
    answer = f"Roof financing in {city}, {state} lets homeowners pay for a replacement or repair monthly rather than up front, which matters in a {risk_label.lower()} market where roofs are replaced early and on short notice. AL Elite matches {city} homeowners with lenders who fund roofing and HVAC projects, matches local contractors with business lenders, and sets {city} roofers and HVAC companies up to offer customer financing. We are a matching service, not a lender."
    return dict(
        path=path, crumbs=[HOME, LOC, (state, f"/locations/{STATE_SLUG[state]}/"), (city, path)],
        eyebrow=f"Home improvement financing in {city}, {ab}", h1=f"Home improvement financing in {city}, {state}: roofs, HVAC, kitchens, generators and contractor programs",
        title=f"{city} Home Improvement Financing: Roof, HVAC, Kitchen & More",
        meta=f"Home improvement financing in {city}, {state}: roof and HVAC financing, kitchen and bathroom remodel loans, fence, generator and foundation financing, local rules and rebates, and customer financing for {city} contractors.",
        answer=answer, why=why, risk_label=risk_label, storm_para=storm_para, demand=demand, angle=angle, city=city, state=state, ab=ab, siblings=sib_html,
    )

def city_page(b, c):
    p = city_page_dict(c); path = p["path"]; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    city, state, ab = p["city"], p["state"], p["ab"]
    lc = CITY[city]
    subs = lc["suburbs"]
    sub_text = ", ".join(subs[:-1]) + " and " + subs[-1]
    svc = [("Kitchen remodel financing", "/remodel-financing/kitchen/"), ("Bathroom remodel financing", "/remodel-financing/bathroom/"), ("Fence financing", "/fence-financing/"), ("Generator financing", "/generator-financing/"), ("Foundation repair financing", "/foundation-repair-financing/"), ("Siding financing", "/siding-financing/"), ("Window replacement financing", "/window-financing/"), ("Water heater financing", "/water-heater-financing/"), ("Plumbing financing", "/plumbing-financing/"), ("Solar financing", "/solar-financing/"), ("Deck financing", "/deck-financing/"), ("Pool financing", "/pool-financing/")]
    svc_grid = "".join(f"<a href='{L(u)}'>{esc(n)}</a>" for n, u in svc)
    faqs = [
        (f"Can I get roof financing in {city}?", f"Yes. {city} homeowners finance roofs through unsecured personal loans, contractor-arranged payment plans and home equity products. AL Elite matches you with lenders who fund roofing in {state}. Submitting a request does not pull your credit."),
        (f"Can I finance my insurance deductible for a roof in {city}?", "Yes, through legitimate third-party financing. What a contractor cannot do is waive, absorb or rebate the deductible; that's illegal in many states and prohibited for AL Elite partner contractors. Financing covers the deductible and any upgrades or non-covered work; the claim covers the rest."),
        (f"How much does a new roof cost in {city}?", f"It depends on size, pitch, material, tear-off and local demand, which spikes after storms. Get at least two itemized quotes from licensed {city} roofers. Our <a href='/roof-financing/'>roof financing</a> page explains the cost drivers and the <a href='/tools/roof-financing-calculator/'>calculator</a> turns a quote into a monthly figure."),
        (f"Can I get HVAC financing in {city} with bad credit?", f"Often, yes. Lenders in our network that fund HVAC work in {state} include some that consider lower scores; start with a soft-pull pre-qualification, reduce the amount with rebates or a standard-efficiency system, and consider a co-applicant. Avoid 'no credit check' offers."),
        (f"How do {city} contractors offer financing to customers?", f"By joining a program such as AL Elite's partner program: the homeowner applies at the estimate, the lender approves and pays the contractor on completion, and standard-rate plans usually cost the contractor nothing. Setup takes days to a few weeks."),
        (f"Can I get home improvement financing in {city} for a kitchen, fence or generator?", f"Yes. The same lenders that fund roofs in {state} fund kitchens, bathrooms, fences, generators, foundation repair, siding, windows, water heaters, solar and pools. Tell us the project and the amount and we match you with lenders who fund that type of work in {state}."),
        (f"Do you serve the suburbs around {city}?", f"Yes. {sub_text} and the rest of the {city} metro are covered; lender availability is set by state, not by city limits."),
        (f"Does AL Elite have an office in {city}?", f"AL Elite matches {city} homeowners and contractors with lenders online and by phone."),
        (f"I'm a roofer in {city}. Can I offer financing to customers?", f"Yes. Licensed, insured {city} roofers and HVAC contractors can join AL Elite's partner program to offer customer financing and be listed on this page. See <a href='/for-contractors/roofing/'>financing for roofing companies</a>."),
    ]
    body = f"""{crumbs_html(b, d, p['crumbs'])}
<section class="page-hero"><div class="wrap">
<div class="stack"><p class="eyebrow">{esc(p['eyebrow'])}</p><h1>{p['h1']}</h1><p class="answer-first" id="speakable-summary">{p['answer']}</p>{byline()}</div>
<div class="cta-box"><h2>Check your options in {esc(city)}</h2><p>Free to compare. Not a loan application. Nothing is shared with a lender until you say so.</p><ul><li>Roof, HVAC and home improvement financing</li><li>Lenders who serve {esc(state)}</li><li>Deductible and insurance-gap financing done legally</li></ul><a class="btn btn-light" href="#contact">Get matched in {esc(city)}</a></div>
</div></section>
<section><div class="wrap layout"><article class="prose">
<div class="city-stats">
<div class="s"><span class="k">Market</span><span class="v">{esc(city)}, {ab}</span><small>{esc(state)}</small></div>
<div class="s"><span class="k">Primary roof risk</span><span class="v">{esc(p['risk_label'])}</span><small>{esc(p['why'] if 'why' in p else '')}</small></div>
<div class="s"><span class="k">Also serving</span><span class="v" style="font-size:1rem">{p['siblings']}</span><small>Other {esc(state)} metros</small></div>
</div>
<figure class="local-card"><img src="{L('/locations/cards/' + path.strip('/').split('/')[-1] + '.png')}" alt="{esc(city)}, {ab} home financing snapshot: primary risk, deductible rules and projects financed" width="1200" height="675" loading="lazy"></figure>
<h2 id="about">Financing home projects in {esc(city)}</h2><p>{esc(lc['intro'])}</p><p>This guide covers the {esc(city)} metro. For statewide rules, rebates and the other metros we serve, see <a href="{L('/locations/' + STATE_SLUG[state] + '/')}">roof, HVAC and home improvement financing in {esc(state)}</a>.</p><p>{esc(lc['housing'])}</p>
<h2 id="suburbs">Suburbs and communities we serve around {esc(city)}</h2><p>Lenders in our network fund projects across the {esc(city)} metro, not only inside the city limits. Homeowners and contractors in {sub_text} get the same matching, the same disclosures and the same {esc(state)} lender coverage. If your community isn't listed, it's still covered; the list is the places we hear from most.</p>
<h2 id="roofers-that-finance">Roof financing in {esc(city)}: roofing companies that finance and how to compare them</h2>
<p>Most established {esc(city)} roofers offer financing or monthly payment plans, almost always through a lender partner rather than their own money. Ask three things when you call for quotes: do you offer financing, through which lender, and does the pre-qualification use a soft credit pull. Get the full price in writing before the plan is discussed so you can see whether it changes, and ask what the price is for cash. If a good local roofer doesn't offer a plan, an unsecured loan arranged through AL Elite pays any roofer like cash. In {esc(state)}, never accept an offer to waive or absorb your insurance deductible; finance it instead. Our guide to <a href="{L('/blog/roofing-companies-that-offer-financing/')}">roofing companies that finance</a> has the eight questions to ask, and <a href="{L('/blog/hvac-companies-that-offer-financing/')}">HVAC companies that offer financing</a> covers the same for AC and furnace work in {esc(city)}.</p>
<h2 id="why-roofs-here">Why roofs in {esc(city)} get replaced early</h2>{p['storm_para']}<p>{esc(p['angle'])} {esc(p['demand'])}</p>
<h2 id="costs">Financing a roof, HVAC or home project in {esc(state)}: local costs and rules</h2>
{local_section(state, city)}
<h2 id="how-it-works">How home improvement financing works in {esc(city)}</h2>
<ol><li><strong>Get itemized quotes</strong> from licensed {esc(city)} roofers. If there's a claim, get the adjuster's estimate too, so you know the gap.</li>
<li><strong>Tell us about the roof.</strong> Amount, timeline, whether insurance is involved, your state. No credit pull.</li>
<li><strong>We match you</strong> with lenders in our network who fund roofing in {esc(state)}, and show you which start with a soft inquiry.</li>
<li><strong>You choose and apply with the lender.</strong> Rates, terms and the decision are theirs. Compare the offers and keep your roofer on schedule.</li></ol>
<h2 id="hvac">HVAC financing in {esc(city)}: AC, furnace and heat pump replacement</h2><p>{esc(lc['services'])}</p><p>HVAC replacements in {esc(city)} are usually decided in a day, when a system fails in the worst weather, so most are financed at the quote through the contractor's plan or an unsecured loan. Ask for two system options with the monthly payment on each, check utility rebates for high-efficiency equipment before you finance, and ask whether a promotional rate is deferred interest. If your credit is on the lower side, start with a soft-pull pre-qualification; see <a href="{L('/hvac-financing/bad-credit-hvac-financing/')}">HVAC financing with bad credit</a>. Our <a href="{L('/hvac-financing/')}">HVAC financing</a> page compares the options, and the <a href="{L('/tools/hvac-financing-calculator/')}">HVAC financing calculator</a> runs your quote.</p>
<h2 id="home-improvement-loans">Home improvement loans in {esc(city)}: kitchens, bathrooms, fences, decks and windows</h2><p>Planned projects in {esc(city)} follow the housing stock described above: renovations in the older neighborhoods, first replacements in the newer suburbs. The same four routes cover nearly every job: an unsecured home improvement loan (days to fund, no lien), the contractor's financing plan, a home equity loan or HELOC for large remodels if you have equity and a few weeks, and government-backed programs such as FHA Title I for eligible repairs. Start from the project page that matches yours: <a href="{L('/remodel-financing/kitchen/')}">kitchen remodel financing</a>, <a href="{L('/remodel-financing/bathroom/')}">bathroom remodel financing</a>, <a href="{L('/fence-financing/')}">fence financing</a>, <a href="{L('/deck-financing/')}">deck financing</a>, <a href="{L('/window-financing/')}">window financing</a>, <a href="{L('/siding-financing/')}">siding financing</a> or <a href="{L('/flooring-financing/')}">flooring financing</a>. Each has example payments and the questions to ask a lender.</p>
<h2 id="generator-foundation">Generator, foundation, plumbing and water heater financing in {esc(city)}</h2><p>These are the projects that arrive without warning. Standby generators are financed before and after outages (<a href="{L('/generator-financing/')}">generator financing</a>, and our <a href="{L('/tools/generator-sizing-calculator/')}">generator sizing calculator</a> estimates the size and cost). Foundation repair is rarely covered by insurance and is usually financed in full (<a href="{L('/foundation-repair-financing/')}">foundation repair financing</a>). Water heater and sewer line failures are same-day decisions where short terms keep interest low (<a href="{L('/water-heater-financing/')}">water heater financing</a>, <a href="{L('/plumbing-financing/')}">plumbing financing</a>). For {esc(city)} homeowners considering solar or a pool, see <a href="{L('/solar-financing/')}">solar financing</a> and <a href="{L('/pool-financing/')}">pool financing</a>.</p>
<div class="svc-grid">{svc_grid}</div>
<p>The same lenders fund <a href="{L('/hvac-financing/')}">HVAC replacement</a>, <a href="{L('/siding-financing/')}">siding</a> and <a href="{L('/gutter-financing/')}">gutters</a> (often damaged in the same storm as the roof), <a href="{L('/generator-financing/')}">standby generators</a> and <a href="{L('/home-improvement-financing/')}">other home improvements</a>. If a storm took the roof and the AC condenser together, tell us both; one loan is simpler than two.</p>
<h2 id="contractors">Contractor financing in {esc(city)}: customer financing and business loans for local trades</h2><p>{esc(lc['contractors'])}</p><p>Roofers, HVAC companies, remodelers, fence, foundation and plumbing contractors in {esc(city)} can offer customer financing at the estimate through our partner program (the lender pays you on completion; standard-rate plans usually cost you nothing) and get matched with business lenders for <a href="{L('/contractor-business-loans/equipment-financing/')}">equipment</a>, <a href="{L('/contractor-business-loans/working-capital/')}">working capital</a> and <a href="{L('/contractor-business-loans/invoice-factoring/')}">invoice factoring</a>. See <a href="{L('/for-contractors/')}">contractor financing programs</a> and our <a href="{L('/blog/why-contractors-lose-jobs-without-financing/')}">guide to why contractors lose jobs without financing</a>.</p>
<p>Storm season is when {esc(city)} contractors win or lose the year. Partner contractors offer customer financing at the kitchen table (paid at completion, deductibles handled legally) and get matched with business lenders for <a href="{L('/contractor-business-loans/working-capital/')}">working capital</a>, <a href="{L('/contractor-business-loans/dump-truck-financing/')}">dump trucks</a> and <a href="{L('/contractor-business-loans/equipment-financing/')}">equipment</a>. See <a href="{L('/for-contractors/')}">offering financing to customers</a>.</p>
<!-- Partner contractors in {esc(city)}: add a callout listing signed partner roofers/HVAC companies with profile links once there is at least one. -->
<h2 id="faq">Frequently asked questions</h2>{faq_html(faqs)}
</article>
<aside class="side">
<div class="box"><h3>Financing in {esc(city)}</h3><ul><li><a href="{L('/roof-financing/')}">Roof financing</a></li><li><a href="{L('/roof-financing/bad-credit-roof-financing/')}">Roof financing with bad credit</a></li><li><a href="{L('/hvac-financing/')}">HVAC financing</a></li><li><a href="{L('/tools/roof-financing-calculator/')}">Roof financing calculator</a></li><li><a href="{L('/blog/does-insurance-cover-roof-replacement/')}">Does insurance cover roof replacement?</a></li></ul></div>
<div class="box"><h3>For contractors</h3><ul><li><a href="{L('/for-contractors/roofing/')}">Financing for roofing companies</a></li><li><a href="{L('/for-contractors/hvac/')}">HVAC financing for contractors</a></li><li><a href="{L('/contractor-business-loans/roofing/')}">Roofing business loans</a></li></ul></div>
<div class="box"><h3>All locations</h3><ul><li><a href="{L('/locations/')}">See all states and metros</a></li></ul></div>
</aside></div></section>
{contact_section(b, d, role='homeowner', project='Roof replacement or repair', state=state, heading=f'Tell us about your {city} roof or project')}"""
    schema = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["meta"], "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": MODIFIED, "inLanguage": "en-US", "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#speakable-summary"]}},
        {"@type": "Service", "@id": url + "#service", "name": f"Roof and HVAC financing matching in {city}, {state}", "serviceType": "Financing matching", "provider": {"@id": ORG_ID}, "areaServed": {"@type": "City", "name": city, "containedInPlace": {"@type": "State", "name": state}}, "description": strip_tags(p["answer"]), "url": url},
        breadcrumb_schema(p["crumbs"]), faq_schema(faqs, url),
    ]
    return page(b, path, p["title"], p["meta"], body, schema)

def locations_hub(b):
    path = "/locations/"; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    groups = ""
    for state, cs in by_state().items():
        groups += f"<div><h3><a href='{L('/locations/' + STATE_SLUG[state] + '/')}'>{esc(state)}</a></h3><ul>" + "".join(f"<li><a href='{L(c[3])}'>{esc(c[0])}</a></li>" for c in cs) + "</ul></div>"
    faqs = [
        ("Does AL Elite only work in these cities?", "No. We match nationwide in the United States. These are the metros where we've written local pages because storm exposure makes roof financing a frequent, urgent need. Lender availability varies by state."),
        ("Why these cities?", f"They were chosen from the states with the highest hail claim payouts (per State Farm's 2025 figures reported by <a href='{CLAIMS}' rel='noopener'>Claims Journal</a>) plus hurricane-exposed Florida, then by local roofing demand. Chicago, Atlanta, Phoenix, Charlotte and Louisville are next."),
        ("Does AL Elite have offices in these cities?", "AL Elite matches homeowners and contractors online and by phone."),
    ]
    body = f"""{crumbs_html(b, d, [HOME, LOC])}
<section class="page-hero"><div class="wrap" style="grid-template-columns:1fr"><div class="stack article-head"><p class="eyebrow">Locations</p><h1>Roof, HVAC and home improvement financing near me: find your state and city</h1><p class="answer-first" id="speakable-summary">Searching for roof financing near me, roofing companies near me that finance, or HVAC financing near me? Lender availability is set by state, so start with your state below, then your metro for local rules, rebates and contractor checks. AL Elite matches homeowners and contractors with lenders across the United States, with local guides for 27 metros in 17 states.</p></div></div></section>
<section><div class="wrap"><article class="prose">
<h2 id="near-me">"Near me" financing: what local actually changes</h2><p>The lenders are national or state-licensed, so a lender that funds roofs in your state funds them in every suburb. What "near me" really decides is the contractor side: licensing rules, permit requirements, insurance deductible laws, utility rebates and which roofing and HVAC companies have a real address and a track record in your area. Each metro guide below covers those, plus how to find roofing companies that finance and HVAC companies that offer financing locally. If your town isn't listed, your state hub applies; the matching is the same.</p>
</article></div></section>
<section><div class="wrap"><div class="sitemap-cols">{groups}</div></div></section>
<section><div class="wrap layout"><article class="prose"><h2>What a city page gives you</h2><p>Each local page covers why roofs in that market are replaced early, how insurance deductibles and gaps are financed legally, local cost and rule notes, and which partner contractors in that metro offer financing through AL Elite. Every page links to the same lender-matching request; the difference is the local context.</p><h2 id="faq">Frequently asked questions</h2>{faq_html(faqs)}</article>
<aside class="side"><div class="box"><h3>Start here</h3><ul><li><a href="{L('/roof-financing/')}">Roof financing</a></li><li><a href="{L('/hvac-financing/')}">HVAC financing</a></li><li><a href="{L('/for-contractors/')}">For contractors</a></li></ul></div></aside></div></section>
{contact_section(b, d, role='homeowner', project='Roof replacement or repair')}"""
    schema = [
        {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": "Roof and HVAC Financing by City | Locations | AL Elite", "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": MODIFIED, "inLanguage": "en-US"},
        {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": f"{c[0]}, {c[2]}", "url": DOMAIN + c[3]} for i, c in enumerate(CITIES)]},
        breadcrumb_schema([HOME, LOC]), faq_schema(faqs, url),
    ]
    return page(b, path, "Roof & Home Improvement Financing Near Me | Find Your City | AL Elite", "Roof financing, HVAC financing and contractor financing by city: Local guides for 27 metros in 17 states, from Houston, Dallas and Phoenix to Chicago, Atlanta, Charlotte and Miami. AL Elite matches you with lenders nationwide.", body, schema)


# ------------------------------------------------------------------ state hub pages (Oct 2026 local pass)
def state_page(b, state):
    sh = STATE_HUB[state]; slug = STATE_SLUG[state]
    path = f"/locations/{slug}/"; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    metros = by_state()[state]
    metro_cards = "".join(f"<a class='card' href='{L(c[3])}'><h3>{esc(c[0])}, {esc(c[2])}</h3><p>{esc(CITY[c[0]]['intro'].split('. ')[0])}.</p></a>" for c in metros)
    metro_names = ", ".join(c[0] for c in metros)
    svc = [("Roof financing", "/roof-financing/"), ("HVAC financing", "/hvac-financing/"), ("Kitchen remodel financing", "/remodel-financing/kitchen/"), ("Bathroom remodel financing", "/remodel-financing/bathroom/"), ("Fence financing", "/fence-financing/"), ("Generator financing", "/generator-financing/"), ("Foundation repair financing", "/foundation-repair-financing/"), ("Siding financing", "/siding-financing/"), ("Window replacement financing", "/window-financing/"), ("Water heater financing", "/water-heater-financing/"), ("Plumbing financing", "/plumbing-financing/"), ("Solar financing", "/solar-financing/")]
    svc_grid = "".join(f"<a href='{L(u)}'>{esc(n)}</a>" for n, u in svc)
    faqs = [
        (f"Can I get roof financing anywhere in {state}?", f"Yes. Lender availability is set by state, so homeowners anywhere in {state} get the same matching, whether they're in {metro_names} or a smaller town. Our local pages cover the metros we hear from most."),
        (f"Which home projects can be financed in {state}?", f"Roofs, HVAC, kitchens, bathrooms, fences, generators, foundation repair, siding, windows, water heaters, plumbing, solar, decks and pools. Tell us the project and amount and we match you with lenders who fund that work in {state}."),
        (f"Can {state} contractors offer financing to customers?", f"Yes. Licensed, insured {state} roofers, HVAC companies, remodelers and other trades can join our partner program to offer customer financing and get matched with business lenders. See <a href='/for-contractors/'>for contractors</a>."),
        (f"Does AL Elite have offices in {state}?", "AL Elite matches homeowners and contractors online and by phone across the United States."),
    ]
    body = f"""{crumbs_html(b, d, [HOME, LOC, (state, path)])}
<section class="page-hero"><div class="wrap">
<div class="stack"><p class="eyebrow">Home improvement financing in {esc(state)}</p><h1>{esc(sh['h1'])}</h1><p class="answer-first" id="speakable-summary">AL Elite matches {esc(state)} homeowners with lenders for roofs, HVAC, kitchens, fences, generators and every other home project, and {esc(state)} contractors with customer financing programs and business lenders. We're a matching service, not a lender; lenders set rates and make decisions.</p>{byline()}</div>
<div class="cta-box"><h2>Check your options in {esc(state)}</h2><p>Free to compare. Not a loan application. Nothing is shared with a lender until you say so.</p><ul><li>Every home project type</li><li>Lenders who serve {esc(state)}</li><li>Soft-inquiry options shown first</li></ul><a class="btn-primary" href="{L('/#contact')}">Check your options</a></div>
</div></section>
<section><div class="wrap layout"><article class="prose">
<figure class="local-card"><img src="{L('/locations/cards/' + slug + '.png')}" alt="{esc(state)} home financing snapshot: storm exposure, deductible rules and programs" width="1200" height="675" loading="lazy"></figure>
<h2 id="overview">Home projects in {esc(state)}: what gets financed and why</h2><p>{esc(sh['intro'])}</p>
<h2 id="roof">Roof financing, roof replacement financing and roof repair financing in {esc(state)}</h2><p>Whether the search is for roof financing, roof replacement financing or roof repair financing in {esc(state)}, the loan products are the same: unsecured roof loans, contractor plans and home equity products. What changes is the amount: a repair is a short loan, a replacement after a claim is usually the deductible and uncovered items, and an age-driven replacement without a claim is the full job. The same lenders also fund HVAC, kitchens, fences, generators and the rest of the house across {esc(state)}; lender availability is set at the state level, so every town in {esc(state)} gets the same matching as the metros below.</p>
<h2 id="metros">Local guides for {esc(state)}</h2><div class="grid-cards">{metro_cards}</div>
<h2 id="rules">{esc(state)} rules that affect your project and your financing</h2><p>{esc(sh['rules'])}</p>
<h2 id="programs">Rebates, assistance and government-backed programs in {esc(state)}</h2><p>{esc(sh['programs'])} Links to the federal programs are in the sources at the end of this page.</p>
<h2 id="claims">Insurance claims in {esc(state)}: how the gap gets financed</h2>{STATE_RULES.get(state, "")}<p>When a claim pays most of a roof, siding or fence, the financing question is the gap: the deductible, depreciation held back until completion, and items the adjuster didn't allow. That is usually a smaller, shorter loan than the whole project. Our guide to <a href="{L('/blog/roof-financing-after-hail-damage/')}">roof financing after hail damage</a> walks through the arithmetic, and the <a href="{L('/blog/does-insurance-cover-roof-replacement/')}">insurance and roof replacement</a> guide covers policy language.</p>
<h2 id="options">Financing options {esc(state)} homeowners use</h2>
<ul><li><strong>Unsecured personal loans.</strong> Days to fund, no lien, fixed rate. The most common route for roofs, HVAC, fences and generators.</li>
<li><strong>Contractor financing plans.</strong> A monthly figure next to the quote through the contractor's lender partner; ask whether promotional rates are deferred interest and whether the price is the same for cash.</li>
<li><strong>Home equity loans and HELOCs.</strong> Lower rates for large planned projects such as kitchens or whole-house siding, with weeks to close and a lien on the home.</li>
<li><strong>Government-backed programs.</strong> FHA Title I property improvement loans through HUD-approved lenders, FHA 203(k) for remodels folded into a mortgage, and USDA Section 504 repair loans and grants in eligible rural parts of {esc(state)}.</li>
<li><strong>Rebates and assistance.</strong> Utility rebates reduce what you finance on HVAC and insulation; weatherization assistance covers eligible households.</li></ul>
<h2 id="services">Financing by project type in {esc(state)}</h2><div class="svc-grid">{svc_grid}</div>
<h2 id="timing">Timing projects in {esc(state)}</h2><p>Storm-driven work (roofs, siding, fences, gutters) peaks right after severe weather, when the best local contractors are booked for weeks and out-of-town crews arrive. Planned work (kitchens, bathrooms, windows, generators, water heater upgrades) is easiest to schedule in the shoulder seasons when crews have capacity and quotes are more competitive. Either way, arranging financing before you sign keeps the project on schedule: a pre-qualification that uses a soft credit inquiry costs nothing and tells you what you're likely to be offered before the deposit is due.</p>
<h2 id="qualify">What lenders look at for {esc(state)} homeowners</h2><p>Unsecured home improvement loans are approved on five things: your credit score and recent payment history, your income and how much of it already goes to debt, the amount requested, how long you've had credit, and a complete application. Reducing the amount (rebates, a smaller scope, a down payment), paying a card balance down before applying, having pay stubs or bank statements ready, and checking options with a soft pull before any hard inquiry improve offers at every lender. Home equity products add an appraisal and a required equity cushion, commonly 15% to 20% of the home's value.</p>
<h2 id="how-it-works">How it works</h2>
<ol><li><strong>Get itemized quotes</strong> from licensed {esc(state)} contractors. If insurance is involved, get the adjuster's estimate so you know the gap.</li><li><strong>Tell us about the project.</strong> Amount, timeline, whether insurance is involved, your state. No credit pull.</li><li><strong>We match you</strong> with lenders who fund that type of work in {esc(state)}, and show which start with a soft inquiry.</li><li><strong>You choose and apply with the lender.</strong> Rates, terms and the decision are theirs.</li></ol>
<h2 id="contractors">For {esc(state)} contractors</h2><p>Roofers, HVAC companies, remodelers, fence and foundation contractors across {esc(state)} can offer customer financing at the estimate (paid at completion, deductibles handled legally where claims are involved) and get matched with business lenders for <a href="{L('/contractor-business-loans/equipment-financing/')}">equipment</a>, <a href="{L('/contractor-business-loans/working-capital/')}">working capital</a> and <a href="{L('/contractor-business-loans/invoice-factoring/')}">factoring</a>. See <a href="{L('/for-contractors/')}">for contractors</a>.</p>
<h2 id="faq">Frequently asked questions</h2>{faq_html(faqs)}
</article>
<aside class="side">
<div class="box"><h3>{esc(state)} metros</h3><ul>{''.join(f"<li><a href='{L(c[3])}'>{esc(c[0])}</a></li>" for c in metros)}</ul></div>
<div class="box"><h3>Start here</h3><ul><li><a href="{L('/home-improvement-financing/')}">Home improvement financing</a></li><li><a href="{L('/roof-financing/')}">Roof financing</a></li><li><a href="{L('/hvac-financing/')}">HVAC financing</a></li><li><a href="{L('/for-contractors/')}">For contractors</a></li></ul></div>
<div class="box"><h3>All locations</h3><ul><li><a href="{L('/locations/')}">See all states and metros</a></li></ul></div>
</aside></div></section>
{contact_section(b, d, role='homeowner', project='Home improvement', state=state, heading=f'Tell us about your {state} project')}"""
    schema = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": sh["title"], "description": sh["meta"], "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": MODIFIED, "inLanguage": "en-US"},
        {"@type": "Service", "@id": url + "#service", "name": f"Home improvement and contractor financing matching in {state}", "serviceType": "Financing matching", "provider": {"@id": ORG_ID}, "areaServed": {"@type": "State", "name": state}},
        breadcrumb_schema([HOME, LOC, (state, path)]), faq_schema(faqs, url),
    ]
    return page(b, path, sh["title"], sh["meta"], body, schema)

STATE_PATHS = [f"/locations/{STATE_SLUG[s]}/" for s in STATE_HUB]
