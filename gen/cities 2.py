"""20 city pages + locations hub. Local context comes from the strategy's Target Locations tab and two cited sources.
Anything that needs local verification (cost ranges, licensing, rebates) is a clearly marked verify block, never invented."""
from common import *

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
    risk_label = "Hurricane and wind" if risk == "hurricane" else "Hail and severe storms"
    storm_para = {
        "hurricane": f"<p>Roofs in {city} are replaced for two reasons that don't apply in most of the country: hurricane and wind damage, and insurer pressure. Florida carriers increasingly decline to renew policies on roofs past a certain age, which means many {city} homeowners replace a roof that hasn't failed yet, on a deadline, to keep coverage. That's a financing event. Wind-rated installation, secondary water barriers and in some zones high-velocity hurricane code compliance raise the cost beyond what a shingle roof costs elsewhere.</p>",
        "hail": f"<p>Roofs in {city} are replaced early because of hail and wind. {why} In 2025 State Farm alone paid out $5.6 billion in hail claims nationally, with Texas the largest state at $1.4 billion, followed by Missouri and Illinois (<a href='{CLAIMS}' rel='noopener'>Claims Journal</a>, April 2026). After a major event, every roofer in the metro is booked for months, prices rise and insurers slow down. The homeowners who get their roof done first are the ones who can fund the deductible and the gap without waiting on the check.</p>",
    }[risk]
    answer = f"Roof financing in {city}, {state} lets homeowners pay for a replacement or repair monthly rather than up front, which matters in a {risk_label.lower()} market where roofs are replaced early and on short notice. AL Elite matches {city} homeowners with lenders who fund roofing and HVAC projects, matches local contractors with business lenders, and sets {city} roofers and HVAC companies up to offer customer financing. We are a matching service, not a lender."
    return dict(
        path=path, crumbs=[HOME, LOC, (state, path), (city, path)],
        eyebrow=f"Roof and HVAC financing in {city}, {ab}", h1=f"Roof financing in {city}, {state}",
        title=f"Roof Financing in {city}, {ab} | HVAC & Home Improvement Financing | AL Elite",
        meta=f"Roof financing in {city}, {state}: storm-market replacement, insurance deductibles and gaps, HVAC and home improvement financing, and customer financing for {city} roofers and contractors. AL Elite matches you with lenders. Not a lender.",
        answer=answer, why=why, risk_label=risk_label, storm_para=storm_para, demand=demand, angle=angle, city=city, state=state, ab=ab, siblings=sib_html,
    )

def city_page(b, c):
    p = city_page_dict(c); path = p["path"]; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    city, state, ab = p["city"], p["state"], p["ab"]
    faqs = [
        (f"Can I get roof financing in {city}?", f"Yes. {city} homeowners finance roofs through unsecured personal loans, contractor-arranged payment plans and home equity products. AL Elite matches you with lenders who fund roofing in {state}. Submitting a request does not pull your credit."),
        (f"Can I finance my insurance deductible for a roof in {city}?", "Yes, through legitimate third-party financing. What a contractor cannot do is waive, absorb or rebate the deductible; that's illegal in many states and prohibited for AL Elite partner contractors. Financing covers the deductible and any upgrades or non-covered work; the claim covers the rest."),
        (f"How much does a new roof cost in {city}?", f"It depends on size, pitch, material, tear-off and local demand, which spikes after storms. Get at least two itemized quotes from licensed {city} roofers. Our <a href='/roof-financing/'>roof financing</a> page explains the cost drivers and the <a href='/tools/roof-financing-calculator/'>calculator</a> turns a quote into a monthly figure."),
        (f"Does AL Elite have an office in {city}?", f"AL Elite matches {city} homeowners and contractors with lenders online and by phone. <span class='placeholder'>[State whether there is a staffed local office; if not, leave this answer as is and do not create a local Google Business Profile.]</span>"),
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
<h2 id="why-roofs-here">Why roofs in {esc(city)} get replaced early</h2>{p['storm_para']}<p>{esc(p['angle'])} {esc(p['demand'])}</p>
<h2 id="costs">Local costs and rules</h2>
<div class="verify"><strong>Before publishing this page, add verified local content here</strong> (this is what keeps a city page from being thin doorway content): typical roof replacement and HVAC replacement cost ranges for the {esc(city)} metro with a cited source; {esc(state)} contractor licensing and registration rules; the {esc(state)} statutory deadline for filing a storm claim; any utility rebates for heat pumps or efficient HVAC in {esc(city)}; and a monthly payment example at local prices. Do not publish estimates without a source.</div>
<h2 id="how-it-works">How roof financing works in {esc(city)}</h2>
<ol><li><strong>Get itemized quotes</strong> from licensed {esc(city)} roofers. If there's a claim, get the adjuster's estimate too, so you know the gap.</li>
<li><strong>Tell us about the roof.</strong> Amount, timeline, whether insurance is involved, your state. No credit pull.</li>
<li><strong>We match you</strong> with lenders in our network who fund roofing in {esc(state)}, and show you which start with a soft inquiry.</li>
<li><strong>You choose and apply with the lender.</strong> Rates, terms and the decision are theirs. Compare the offers and keep your roofer on schedule.</li></ol>
<h2 id="hvac">HVAC and other projects in {esc(city)}</h2>
<p>The same lenders fund <a href="{L('/hvac-financing/')}">HVAC replacement</a>, <a href="{L('/siding-financing/')}">siding</a> and <a href="{L('/gutter-financing/')}">gutters</a> (often damaged in the same storm as the roof), <a href="{L('/generator-financing/')}">standby generators</a> and <a href="{L('/home-improvement-financing/')}">other home improvements</a>. If a storm took the roof and the AC condenser together, tell us both; one loan is simpler than two.</p>
<h2 id="contractors">For {esc(city)} roofers and contractors</h2>
<p>Storm season is when {esc(city)} contractors win or lose the year. Partner contractors offer customer financing at the kitchen table (paid at completion, deductibles handled legally) and get matched with business lenders for <a href="{L('/contractor-business-loans/working-capital/')}">working capital</a>, <a href="{L('/contractor-business-loans/dump-truck-financing/')}">dump trucks</a> and <a href="{L('/contractor-business-loans/equipment-financing/')}">equipment</a>. See <a href="{L('/for-contractors/')}">offering financing to customers</a>.</p>
<div class="callout"><strong>Partner contractors in {esc(city)}:</strong> <span class="placeholder">[List partner roofers and HVAC companies here with links to their profiles once signed. Leave this block out until there is at least one.]</span></div>
<h2 id="faq">Frequently asked questions</h2>{faq_html(faqs)}
</article>
<aside class="side">
<div class="box"><h3>Financing in {esc(city)}</h3><ul><li><a href="{L('/roof-financing/')}">Roof financing</a></li><li><a href="{L('/roof-financing/bad-credit-roof-financing/')}">Roof financing with bad credit</a></li><li><a href="{L('/hvac-financing/')}">HVAC financing</a></li><li><a href="{L('/tools/roof-financing-calculator/')}">Roof financing calculator</a></li><li><a href="{L('/blog/does-insurance-cover-roof-replacement/')}">Does insurance cover roof replacement?</a></li></ul></div>
<div class="box"><h3>For contractors</h3><ul><li><a href="{L('/for-contractors/roofing/')}">Financing for roofing companies</a></li><li><a href="{L('/for-contractors/hvac/')}">HVAC financing for contractors</a></li><li><a href="{L('/contractor-business-loans/roofing/')}">Roofing business loans</a></li></ul></div>
<div class="box"><h3>All locations</h3><ul><li><a href="{L('/locations/')}">See all 20 metros</a></li></ul></div>
</aside></div></section>
{contact_section(b, d, role='homeowner', project='Roof replacement or repair', state=state, heading=f'Tell us about your {city} roof or project')}"""
    schema = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["meta"], "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": "2026-10-04", "inLanguage": "en-US", "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#speakable-summary"]}},
        {"@type": "Service", "@id": url + "#service", "name": f"Roof and HVAC financing matching in {city}, {state}", "serviceType": "Financing matching", "provider": {"@id": ORG_ID}, "areaServed": {"@type": "City", "name": city, "containedInPlace": {"@type": "State", "name": state}}, "description": strip_tags(p["answer"]), "url": url},
        breadcrumb_schema(p["crumbs"]), faq_schema(faqs, url),
    ]
    return page(b, path, p["title"], p["meta"], body, schema)

def locations_hub(b):
    path = "/locations/"; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    groups = ""
    for state, cs in by_state().items():
        groups += f"<div><h3>{esc(state)}</h3><ul>" + "".join(f"<li><a href='{L(c[3])}'>{esc(c[0])}</a></li>" for c in cs) + "</ul></div>"
    faqs = [
        ("Does AL Elite only work in these cities?", "No. We match nationwide in the United States. These are the metros where we've written local pages because storm exposure makes roof financing a frequent, urgent need. Lender availability varies by state."),
        ("Why these cities?", f"They were chosen from the states with the highest hail claim payouts (per State Farm's 2025 figures reported by <a href='{CLAIMS}' rel='noopener'>Claims Journal</a>) plus hurricane-exposed Florida, then by local roofing demand. Chicago, Atlanta, Phoenix, Charlotte and Louisville are next."),
        ("Does AL Elite have offices in these cities?", "AL Elite matches homeowners and contractors online and by phone. <span class='placeholder'>[State which, if any, cities have a staffed office.]</span>"),
    ]
    body = f"""{crumbs_html(b, d, [HOME, LOC])}
<section class="page-hero"><div class="wrap" style="grid-template-columns:1fr"><div class="stack article-head"><p class="eyebrow">Locations</p><h1>Roof and HVAC financing by city</h1><p class="answer-first" id="speakable-summary">AL Elite matches homeowners and contractors with lenders across the United States, with local pages for 20 metros where hail, hurricanes and insurer roof-age rules make roof financing a frequent, urgent need: Texas, Oklahoma, Colorado, Missouri, Kansas, Nebraska, Indiana, Minnesota, Florida, Tennessee and Utah.</p></div></div></section>
<section><div class="wrap"><div class="sitemap-cols">{groups}</div></div></section>
<section><div class="wrap layout"><article class="prose"><h2>What a city page gives you</h2><p>Each local page covers why roofs in that market are replaced early, how insurance deductibles and gaps are financed legally, local cost and rule notes, and which partner contractors in that metro offer financing through AL Elite. Every page links to the same lender-matching request; the difference is the local context.</p><h2 id="faq">Frequently asked questions</h2>{faq_html(faqs)}</article>
<aside class="side"><div class="box"><h3>Start here</h3><ul><li><a href="{L('/roof-financing/')}">Roof financing</a></li><li><a href="{L('/hvac-financing/')}">HVAC financing</a></li><li><a href="{L('/for-contractors/')}">For contractors</a></li></ul></div></aside></div></section>
{contact_section(b, d, role='homeowner', project='Roof replacement or repair')}"""
    schema = [
        {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": "Roof and HVAC Financing by City | Locations | AL Elite", "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": "2026-10-04", "inLanguage": "en-US"},
        {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": f"{c[0]}, {c[2]}", "url": DOMAIN + c[3]} for i, c in enumerate(CITIES)]},
        breadcrumb_schema([HOME, LOC]), faq_schema(faqs, url),
    ]
    return page(b, path, "Roof & HVAC Financing by City | 20 Storm-Market Metros | AL Elite", "Roof financing, HVAC financing and contractor financing by city: Houston, Dallas, Denver, Kansas City, Tampa, Orlando, Miami, Indianapolis and 12 more storm-prone metros. AL Elite matches you with lenders nationwide.", body, schema)
