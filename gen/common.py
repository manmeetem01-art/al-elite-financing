"""Shared template, components and helpers for the AL Elite site generator."""
import json, re, html, math, os

DOMAIN = "https://www.alelitefinancing.com"
REVIEWED = "October 2026"
BASE_CSS = open(os.path.join(os.path.dirname(__file__), "base.css")).read()
LOGO_IMG = '<img class="brand-logo" src="' + open(os.path.join(os.path.dirname(__file__), "logo_data.txt")).read() + '" alt="AL Elite Financing" width="146" height="106">'

EXTRA_CSS = """
/* Inner-page additions */
[hidden]{display:none!important}
.crumbs{font-size:.85rem;color:var(--muted);padding-block:14px}
.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.crumbs li+li::before{content:"/";margin-right:6px;color:var(--line)}
.crumbs a{color:var(--muted);text-decoration:none}
.crumbs a:hover{color:var(--navy)}
.page-hero{padding-block:clamp(28px,4vw,56px) clamp(40px,5vw,64px);background:linear-gradient(180deg,#fff 0%,var(--surface) 100%);border-bottom:1px solid var(--line)}
.page-hero .wrap{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:40px;align-items:start}
@media (max-width:900px){.page-hero .wrap{grid-template-columns:1fr}}
.page-hero .stack{gap:18px}
.answer-first{border-left:3px solid var(--gold);padding-left:20px;font-size:1.12rem;color:var(--ink-2);max-width:62ch}
.byline{font-size:.85rem;color:var(--muted);display:flex;flex-wrap:wrap;gap:6px 18px}
.cta-box{display:grid;gap:14px;padding:26px;border-radius:var(--radius);background:var(--navy);color:var(--on-navy)}
.cta-box h2,.cta-box h3{color:#fff;font-size:1.3rem}
.cta-box p{color:var(--on-navy-muted);font-size:.95rem}
.cta-box ul{margin:0;padding:0;list-style:none;display:grid;gap:8px;font-size:.92rem}
.cta-box li{display:flex;gap:10px;align-items:flex-start}
.cta-box li::before{content:"";width:7px;height:7px;border-radius:50%;background:var(--gold);flex:none;margin-top:9px}
.cta-box .btn{justify-self:start}
.prose{max-width:72ch;display:grid;gap:16px}
.prose h2{font-size:clamp(1.5rem,2.4vw,2rem);margin-top:18px}
.prose h3{font-size:1.2rem;margin-top:6px}
.prose p,.prose li{color:var(--ink-2)}
.prose ul,.prose ol{margin:0;padding-left:22px;display:grid;gap:8px}
.prose strong{color:var(--ink)}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 340px;gap:56px;align-items:start}
@media (max-width:1000px){.layout{grid-template-columns:1fr}}
.side{display:grid;gap:24px;position:sticky;top:calc(env(safe-area-inset-top,0px) + 90px)}
@media (max-width:1000px){.side{position:static}}
.side .box{border:1px solid var(--line);border-radius:var(--radius);padding:20px;display:grid;gap:10px;background:#fff}
.side .box h3{font-family:var(--body);font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold)}
.side .box ul{list-style:none;margin:0;padding:0;display:grid;gap:8px;font-size:.95rem}
.side .box a{text-decoration:none;font-weight:500}
.side .box a:hover{text-decoration:underline}
.tbl{overflow-x:auto;border:1px solid var(--line);border-radius:var(--radius)}
table{border-collapse:collapse;width:100%;font-size:.95rem;font-variant-numeric:tabular-nums}
th,td{padding:12px 14px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--surface);font-size:.78rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted);font-weight:700}
tr:last-child td{border-bottom:0}
td.num,th.num{text-align:right}
.cap{font-size:.82rem;color:var(--muted)}
.callout{padding:18px 20px;border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:var(--radius);background:var(--surface);color:var(--ink-2);font-size:.95rem}
.callout strong{color:var(--ink)}
.verify{padding:14px 16px;border:1px dashed var(--gold);border-radius:var(--radius);background:var(--gold-soft);color:var(--ink-2);font-size:.9rem}
.verify strong{color:var(--ink)}
.compare{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px}
.compare .opt{border:1px solid var(--line);border-radius:var(--radius);padding:18px;display:grid;gap:8px;background:#fff}
.compare .opt h3{font-family:var(--body);font-size:1.02rem;color:var(--navy)}
.compare .opt p{font-size:.9rem;color:var(--ink-2)}
.compare .opt .pro,.compare .opt .con{font-size:.88rem}
.compare .opt .pro::before{content:"Best for: ";font-weight:700;color:var(--ok)}
.compare .opt .con::before{content:"Watch out: ";font-weight:700;color:var(--err)}
.article-head{max-width:760px}
.article-head h1{font-size:clamp(1.9rem,3.8vw,2.9rem)}
.toc{border:1px solid var(--line);border-radius:var(--radius);padding:18px 20px;background:var(--surface)}
.toc h2{font-family:var(--body);font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
.toc ol{margin:0;padding-left:20px;display:grid;gap:6px;font-size:.95rem}
.city-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px}
.city-stats .s{border:1px solid var(--line);border-radius:var(--radius);padding:16px;display:grid;gap:4px;background:#fff}
.city-stats .k{font-size:.74rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:700}
.city-stats .v{font-family:var(--display);font-size:1.3rem;color:var(--navy);font-weight:600}
.city-stats small{color:var(--muted);font-size:.8rem}
.tool-card{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:#fff}
.sched{max-height:420px;overflow:auto}
.post-list{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}
.post{display:grid;gap:8px;padding:22px;border:1px solid var(--line);border-radius:var(--radius);text-decoration:none;color:var(--ink);align-content:start}
.post:hover{border-color:var(--navy)}
.post h3{font-size:1.15rem}
.post p{color:var(--ink-2);font-size:.92rem}
.post .meta{font-size:.78rem;color:var(--muted);letter-spacing:.06em;text-transform:uppercase;font-weight:700}
.sitemap-cols{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:28px}
.sitemap-cols ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.sitemap-cols h3{font-family:var(--body);font-size:.8rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gold)}
"""


REVIEW_CSS = """
.reviews{background:var(--surface)}
.review-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}
.review{display:grid;gap:12px;padding:24px;border:1px solid var(--line);border-radius:var(--radius);background:#fff;align-content:start;position:relative}
.review .stars{display:flex;gap:3px;color:var(--gold)}
.review .stars svg{width:18px;height:18px}
.review blockquote{margin:0;font-size:1.02rem;color:var(--ink);line-height:1.55}
.review .who{display:flex;gap:12px;align-items:center;font-size:.9rem;color:var(--ink-2)}
.review .avatar{width:40px;height:40px;border-radius:50%;background:var(--navy);color:#fff;display:grid;place-items:center;font-weight:700;font-family:var(--display);flex:none}
.review .who strong{display:block;color:var(--ink)}
.review .sample{justify-self:start;font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--err);border:1px solid var(--err);border-radius:3px;padding:2px 6px;background:#fff}
.review-summary{display:flex;flex-wrap:wrap;gap:18px 32px;align-items:center;margin-bottom:28px}
.review-summary .big{font-family:var(--display);font-size:2.4rem;color:var(--navy);font-weight:600;line-height:1}
.review-summary .meta{font-size:.9rem;color:var(--muted)}
.review-sources{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;font-size:.88rem;color:var(--muted)}
.review-sources a{color:var(--navy)}
"""

def stars(n=5):
    s = "<svg viewBox='0 0 24 24' fill='currentColor' aria-hidden='true'><path d='M12 2.5l2.9 6.1 6.7.8-4.9 4.6 1.3 6.6L12 17.3l-6 3.3 1.3-6.6L2.4 9.4l6.7-.8z'/></svg>"
    return "<span class='stars' aria-label='" + str(n) + " out of 5 stars'>" + s * n + "</span>"

# SAMPLE cards: visibly labelled, generic placeholders. Replace with real, permissioned reviews before launch.
SAMPLE_REVIEWS = [
    ("homeowner", "Roof replacement, Texas", "[Replace with a real homeowner review: what the project was, how fast the match came back, what they'd tell a neighbour.]", "A.B.", "Homeowner"),
    ("homeowner", "HVAC replacement, Florida", "[Replace with a real homeowner review. Keep it in the customer's own words; do not edit for marketing.]", "C.D.", "Homeowner"),
    ("contractor", "Roofing company, Colorado", "[Replace with a real partner-contractor review: close rate, how customers reacted to a monthly figure, funding timing.]", "E.F.", "Partner contractor"),
]

def reviews_section(b, d, audience="homeowner"):
    L = lambda p: link(b, p, d)
    cards = ""
    for aud, ctx, text, initials, role in SAMPLE_REVIEWS:
        cards += f"""<figure class="review"><span class="sample">Sample, replace before launch</span>{stars(5)}<blockquote>{text}</blockquote><figcaption class="who"><span class="avatar" aria-hidden="true">{initials[0]}</span><span><strong>{initials}, {role}</strong>{esc(ctx)}</span></figcaption></figure>"""
    return f"""<section class="reviews" aria-labelledby="reviews-h">
<div class="wrap">
<div class="sec-head"><p class="eyebrow">What customers say</p><h2 id="reviews-h">Reviews from homeowners and contractors</h2><p class="lede">Every review here is from a real customer, published with their permission and in their own words. We don't edit them and we don't pay for them.</p></div>
<div class="review-summary"><span class="big"><span class="placeholder">[4.x]</span><span style="font-size:1.2rem;color:var(--muted)"> / 5</span></span><span class="meta">from <span class="placeholder">[n]</span> verified reviews on <span class="placeholder">[Google / Trustpilot / BBB]</span></span></div>
<div class="review-grid">{cards}</div>
<p class="review-sources">Read all reviews on <a href="#" rel="noopener">Google</a>, <a href="#" rel="noopener">Trustpilot</a> and the <a href="#" rel="noopener">Better Business Bureau</a>. <span class="placeholder">[Link each to the real profile; remove any you don't have.]</span></p>
<div class="verify" style="margin-top:22px"><strong>Before publishing this section:</strong> replace the three sample cards with real reviews (name or initials, city or state, trade, exact text, star rating, date, source and written permission). Then add AggregateRating and Review schema in <code>gen/common.py</code> using only the real figures. Do not publish fabricated or paraphrased reviews; the FTC's endorsement rules and Google's review policies both apply.</div>
</div></section>"""

# ---------------------------------------------------------------- link rewriting
class Build:
    def __init__(self, mode):
        self.mode = mode  # "prod" or "artifact"

def link(build, path, depth=0):
    """Rewrite a site path (/roof-financing/, /#contact, https://...) for the build mode."""
    if path.startswith("http") or path.startswith("mailto:") or path.startswith("tel:"):
        return path
    if build.mode == "prod":
        return path
    prefix = "../" * depth
    anchor = ""
    if "#" in path:
        path, anchor = path.split("#", 1)
        anchor = "#" + anchor
    if path == "" :
        return anchor or "#"
    if path == "/":
        return prefix + "index.html" + anchor
    p = path.strip("/")
    return prefix + p + "/index.html" + anchor

def out_path(path):
    """Where a page lands on disk relative to the site root."""
    if path == "/":
        return "index.html"
    return path.strip("/") + "/index.html"

def depth_of(path):
    if path == "/":
        return 0
    return path.strip("/").count("/") + 1

# ---------------------------------------------------------------- helpers
def esc(s):
    return html.escape(s, quote=True)

def payment(P, apr, n):
    r = apr / 100 / 12
    if r == 0:
        return P / n
    f = (1 + r) ** n
    return P * r * f / (f - 1)

def money(x, cents=True):
    return "${:,.2f}".format(x) if cents else "${:,.0f}".format(x)

def payment_table(amounts, aprs=(7.99, 11.99, 17.99), terms=(36, 60, 84, 120), caption=None):
    """Illustrative payment table. Example APRs are arithmetic, not offers."""
    rows = []
    head = "<tr><th>Amount</th><th>Example APR</th>" + "".join(f"<th class='num'>{t} mo</th>" for t in terms) + "</tr>"
    for P in amounts:
        for i, a in enumerate(aprs):
            cells = "".join(f"<td class='num'>{money(payment(P, a, t))}</td>" for t in terms)
            first = f"<td rowspan='{len(aprs)}'><strong>{money(P, False)}</strong></td>" if i == 0 else ""
            rows.append(f"<tr>{first}<td>{a:.2f}%</td>{cells}</tr>")
    cap = caption or "Example monthly payments using standard amortization with no fees. The APRs shown are illustrative tiers, not offers. Your rate, fees and term are set by the lender and depend on your credit profile, income and state."
    return f"<div class='tbl'><table><thead>{head}</thead><tbody>{''.join(rows)}</tbody></table></div><p class='cap'>{cap}</p>"

def faq_html(faqs):
    out = ["<div class='faq-list'>"]
    for q, a in faqs:
        out.append(f"<details><summary>{esc(q)}<svg class='plus' viewBox='0 0 24 24' fill='none' stroke='currentColor' stroke-width='2' aria-hidden='true'><path d='M12 5v14M5 12h14'/></svg></summary><div class='a'><p>{a}</p></div></details>")
    out.append("</div>")
    return "".join(out)

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)

def faq_schema(faqs, url):
    return {
        "@type": "FAQPage", "@id": url + "#faq",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}} for q, a in faqs],
    }

def breadcrumb_schema(crumbs):
    return {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + p} for i, (n, p) in enumerate(crumbs)]}

ORG_ID = DOMAIN + "/#organization"

# ---------------------------------------------------------------- components
def brand_svg(fill="#0b2545"):
    return f"""<svg class="brand-mark" viewBox="0 0 40 40" aria-hidden="true"><rect x="1" y="1" width="38" height="38" rx="4" fill="{fill}"/><path d="M8 24 L20 11 L32 24" fill="none" stroke="#b48c2c" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><path d="M12 24 V30 H28 V24" fill="none" stroke="#ffffff" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/></svg>"""

def header(b, d):
    L = lambda p: link(b, p, d)
    return f"""<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><span><strong>AL Elite is a matching service, not a lender.</strong> We connect you with lenders. Rates and approval decisions come from them.</span><span>Call <a href="tel:+1-888-968-0079">(888) 968-0079</a></span></div></div>
<header class="site"><div class="wrap">
<a class="brand" href="{L('/')}" aria-label="AL Elite Financing home">{LOGO_IMG}<span><span class="brand-name">AL Elite</span><span class="brand-sub">Financing</span></span></a>
<button class="menu-btn" id="menuBtn" aria-expanded="false" aria-controls="primaryNav">Menu <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
<nav class="primary" id="primaryNav" aria-label="Primary"><ul>
<li><a href="{L('/home-improvement-financing/')}">Homeowners</a></li>
<li><a href="{L('/for-contractors/')}">Contractors</a></li>
<li><a href="{L('/contractor-business-loans/')}">Business loans</a></li>
<li><a href="{L('/tools/roof-financing-calculator/')}">Calculators</a></li>
<li><a href="{L('/locations/')}">Locations</a></li>
<li><a href="{L('/about/')}">About</a></li>
<li><a class="btn btn-primary" href="#contact">Check your options</a></li>
</ul></nav></div></header>"""

def footer(b, d):
    L = lambda p: link(b, p, d)
    return f"""<footer><div class="wrap">
<div class="cols">
<div><a class="brand" href="{L('/')}" aria-label="AL Elite Financing home">{LOGO_IMG}<span><span class="brand-name">AL Elite</span><span class="brand-sub">Financing</span></span></a>
<p class="about">A financing marketplace for home improvement. We match homeowners with consumer lenders and contractors with business lenders across the United States.</p><p class="about" style="margin-top:10px"><a href="tel:+1-888-968-0079">(888) 968-0079</a></p></div>
<div><h4>Homeowners</h4><ul>
<li><a href="{L('/roof-financing/')}">Roof financing</a></li><li><a href="{L('/hvac-financing/')}">HVAC financing</a></li><li><a href="{L('/plumbing-financing/')}">Plumbing financing</a></li><li><a href="{L('/solar-financing/')}">Solar financing</a></li><li><a href="{L('/home-improvement-financing/')}">All home improvement financing</a></li><li><a href="{L('/tools/roof-financing-calculator/')}">Roof financing calculator</a></li></ul></div>
<div><h4>Contractors</h4><ul>
<li><a href="{L('/for-contractors/')}">Offer customer financing</a></li><li><a href="{L('/contractor-business-loans/')}">Contractor business loans</a></li><li><a href="{L('/contractor-business-loans/equipment-financing/')}">Equipment financing</a></li><li><a href="{L('/contractor-business-loans/invoice-factoring/')}">Invoice factoring</a></li><li><a href="{L('/tools/equipment-loan-calculator/')}">Equipment loan calculator</a></li><li><a href="{L('/blog/')}">Blog</a></li></ul></div>
<div><h4>Company</h4><ul>
<li><a href="{L('/about/')}">About AL Elite</a></li><li><a href="{L('/how-we-make-money/')}">How we make money</a></li><li><a href="{L('/lender-network/')}">Our lender network</a></li><li><a href="{L('/locations/')}">Locations</a></li><li><a href="#contact">Contact</a></li><li><a href="{L('/privacy/')}">Privacy policy</a></li></ul></div>
</div>
<div class="disclosures">
<p><strong>Important disclosures.</strong> AL Elite Financing is not a lender, bank or credit union and does not make credit decisions, set rates or fund loans. We operate a lead-matching marketplace that connects consumers and businesses with third-party lenders. Lenders may compensate us for introductions. Any loan offer, APR, fee, term or approval is determined solely by the lender and is subject to their credit approval and underwriting. Not all applicants will qualify. Loan products and lender availability vary by state.</p>
<p>Payment figures shown on this site are illustrations based on standard amortization and are not offers of credit. Your actual terms may differ. Nothing on this site is legal, tax or financial advice. <span class="placeholder">[Add any state-specific licensing or lead-generator disclosures required by counsel before launch.]</span></p>
<p>Last reviewed: {REVIEWED}. <span class="placeholder">[Reviewed by: name, title and credentials of the finance professional responsible for this page.]</span></p>
</div>
<div class="legal-row"><span>&copy; 2026 AL Elite Financing. All rights reserved.</span>
<ul><li><a href="{L('/privacy/')}">Privacy</a></li><li><a href="{L('/terms/')}">Terms</a></li><li><a href="{L('/accessibility/')}">Accessibility</a></li><li><a href="{L('/do-not-sell/')}">Do not sell or share my information</a></li></ul></div>
</div></footer>"""

STATES = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Columbia","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]

def contact_section(b, d, role="homeowner", project=None, need=None, heading=None, lede=None, state=None):
    """The lead form, reused on every page. Preselects role/project for the page's topic."""
    L = lambda p: link(b, p, d)
    projects = ["Roof replacement or repair","HVAC (AC, furnace, heat pump)","Plumbing or water heater","Solar","Siding, gutters or windows","Kitchen or bathroom remodel","Foundation repair","Pool","Flooring","Fence, deck or landscaping","Generator or garage door","Other home improvement"]
    needs = ["Offer financing to my customers","Working capital","Equipment financing","Dump truck or work truck financing","Invoice factoring","Line of credit","Not sure yet"]
    popt = "".join(f"<option{' selected' if p==project else ''}>{p}</option>" for p in projects)
    nopt = "".join(f"<option{' selected' if n==need else ''}>{n}</option>" for n in needs)
    sopt = "<option value=''>Select your state</option>" + "".join(f"<option{' selected' if s==state else ''}>{s}</option>" for s in STATES)
    con = role == "contractor"
    heading = heading or ("Tell us about the project, and we'll come back to you" if not con else "Tell us about the business, and we'll come back to you")
    lede = lede or "A real person reads every request. We'll reply by email or phone, whichever you choose, and we won't share your details with a lender until you ask us to."
    return f"""<section class="contact" id="contact" aria-labelledby="contact-h">
<div class="wrap">
<div class="contact-aside">
<div class="stack"><p class="eyebrow">Get in touch</p><h2 id="contact-h">{heading}</h2><p class="lede">{lede}</p></div>
<div class="block"><span class="k">Phone</span><span><a href="tel:+1-888-968-0079">(888) 968-0079</a></span></div>
<div class="block"><span class="k">Email</span><span class="placeholder">[Add contact email address]</span></div>
<div class="block"><span class="k">Hours</span><span class="placeholder">[Add business hours and time zone]</span></div>
<div class="block"><span class="k">What we won't ask for here</span><span>Social Security numbers, bank account numbers or card details. Lenders collect those securely at application, never through this form.</span></div>
</div>
<form class="lead" id="leadForm" novalidate>
<fieldset><legend>I am a</legend><div class="radios">
<label><input type="radio" name="role" value="homeowner" id="role-home"{'' if con else ' checked'}> Homeowner</label>
<label><input type="radio" name="role" value="contractor" id="role-con"{' checked' if con else ''}> Contractor or business owner</label></div></fieldset>
<div class="f2">
<div class="field"><label for="fname">Full name</label><input type="text" id="fname" name="name" autocomplete="name" required><span class="error">Please enter your name.</span></div>
<div class="field"><label for="femail">Email</label><input type="email" id="femail" name="email" autocomplete="email" inputmode="email" required><span class="error">Please enter a valid email address.</span></div></div>
<div class="f2">
<div class="field"><label for="fphone">Phone <span class="opt">(optional)</span></label><input type="tel" id="fphone" name="phone" autocomplete="tel" inputmode="tel" placeholder="(555) 555-0100"><span class="hint">Only if you'd like a call back.</span></div>
<div class="field"><label for="fstate">State</label><select id="fstate" name="state" autocomplete="address-level1" required>{sopt}</select><span class="error">Please select your state.</span></div></div>
<div class="f2">
<div class="field" id="projectField"{' hidden' if con else ''}><label for="fproject">Project type</label><select id="fproject" name="project">{popt}</select></div>
<div class="field" id="needField"{'' if con else ' hidden'}><label for="fneed">What do you need?</label><select id="fneed" name="need">{nopt}</select></div>
<div class="field"><label for="famount">Approximate amount <span class="opt">(optional)</span></label><select id="famount" name="amount"><option value="">Select a range</option><option>Under $5,000</option><option>$5,000 to $15,000</option><option>$15,000 to $30,000</option><option>$30,000 to $75,000</option><option>$75,000 to $250,000</option><option>Over $250,000</option></select></div></div>
<div class="field"><label for="fmsg">Anything else we should know? <span class="opt">(optional)</span></label><textarea id="fmsg" name="message" rows="4" placeholder="Timeline, insurance claim in progress, preferred contact time..."></textarea></div>
<div class="field"><label for="fcontact">Preferred contact method</label><select id="fcontact" name="contact_method"><option>Email</option><option>Phone call</option><option>Text message</option></select></div>
<div class="hp" aria-hidden="true"><label for="website">Leave this field empty</label><input type="text" id="website" name="website" tabindex="-1" autocomplete="off"></div>
<div class="field"><label class="consent"><input type="checkbox" id="consent" name="consent" required><span>I agree to be contacted by AL Elite Financing about my request at the email and phone number provided, including by phone call, text message or email, which may use automated technology. Consent is not a condition of any purchase or service. Message and data rates may apply. Reply STOP to opt out of texts. I have read the <a href="{L('/privacy/')}">Privacy Policy</a> and <a href="{L('/terms/')}">Terms of Use</a>.</span></label><span class="error">Please tick the consent box so we're allowed to reply to you.</span></div>
<div class="form-foot"><button class="btn btn-primary" type="submit" id="submitBtn">Send my request</button><span class="secure"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>Sent over an encrypted connection. We never sell your information.</span></div>
<p class="hint" style="font-size:.82rem;color:var(--muted)">Submitting this form does not pull your credit and is not a loan application. You'll choose whether to proceed with any lender.</p>
<p class="callout" id="formError" hidden tabindex="-1" style="border-left-color:var(--err)"><strong>We couldn't send that.</strong> Please try again in a moment, or call us on <a href="tel:+1-888-968-0079">(888) 968-0079</a>.</p>
</form>
<div class="success" id="formSuccess" hidden role="status"><h3>Request received</h3><p>Thanks, <span id="successName">there</span>. One of our team will reply within one business day using the contact method you chose. Nothing has been shared with a lender yet, and your credit has not been checked.</p></div>
</div></section>"""

SCRIPT = """
(function(){
  var btn=document.getElementById('menuBtn'),nav=document.getElementById('primaryNav');
  if(btn&&nav){btn.addEventListener('click',function(){var open=nav.classList.toggle('open');btn.setAttribute('aria-expanded',open?'true':'false');});
    nav.addEventListener('click',function(e){if(e.target.tagName==='A'){nav.classList.remove('open');btn.setAttribute('aria-expanded','false');}});}
  var form=document.getElementById('leadForm');
  if(form){
    var roleHome=document.getElementById('role-home'),roleCon=document.getElementById('role-con');
    var projectField=document.getElementById('projectField'),needField=document.getElementById('needField');
    function syncRole(){var con=roleCon.checked;projectField.hidden=con;needField.hidden=!con;}
    roleHome.addEventListener('change',syncRole);roleCon.addEventListener('change',syncRole);syncRole();
    function setInvalid(el,bad){var f=el.closest('.field');if(f){f.classList.toggle('invalid',bad);}el.setAttribute('aria-invalid',bad?'true':'false');}
    function validEmail(v){return /^[^\\s@]+@[^\\s@]+\\.[^\\s@]{2,}$/.test(v);}
    form.addEventListener('submit',function(e){
      e.preventDefault();
      if(document.getElementById('website').value)return;
      var name=document.getElementById('fname'),email=document.getElementById('femail'),state=document.getElementById('fstate'),consent=document.getElementById('consent');
      var bad=false,first=null;
      [[name,!name.value.trim()],[email,!validEmail(email.value.trim())],[state,!state.value],[consent,!consent.checked]].forEach(function(p){setInvalid(p[0],p[1]);if(p[1]){bad=true;first=first||p[0];}});
      if(bad){first.focus();return;}
      var data=Object.fromEntries(new FormData(form).entries());
      delete data.website;
      data.consent=consent.checked?'Yes - agreed to be contacted (TCPA consent text shown on form)':'No';
      data.submitted_at=new Date().toISOString();data.page=location.href;
      data._subject='New AL Elite lead: '+(data.role||'')+' - '+(data.project||data.need||'');
      data._template='table';data._captcha='false';data._replyto=data.email;data._honey='';
      var sb=document.getElementById('submitBtn');sb.disabled=true;sb.textContent='Sending...';
      var errBox=document.getElementById('formError');
      fetch('https://formsubmit.co/ajax/manmeetsingh0177@gmail.com',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json'},body:JSON.stringify(data)})
        .then(function(r){return r.json().then(function(j){return {ok:r.ok&&String(j.success)!=='false',j:j};});})
        .then(function(res){
          if(!res.ok)throw new Error(res.j&&res.j.message||'send failed');
          document.getElementById('successName').textContent=name.value.trim().split(' ')[0]||'there';form.hidden=true;var s=document.getElementById('formSuccess');s.hidden=false;s.setAttribute('tabindex','-1');s.focus();
        })
        .catch(function(){sb.disabled=false;sb.textContent='Send my request';if(errBox){errBox.hidden=false;errBox.focus();}});
    });
    ['fname','femail','fstate','consent'].forEach(function(id){var el=document.getElementById(id);el.addEventListener('input',function(){setInvalid(el,false);});el.addEventListener('change',function(){setInvalid(el,false);});});
  }
  window.ALE={payment:function(P,apr,n){var r=apr/100/12;if(r===0)return P/n;var f=Math.pow(1+r,n);return P*r*f/(f-1);}};
})();
"""

def trim_meta(meta, limit=160):
    if len(meta) <= limit + 5:
        return meta
    cut = meta[:limit]
    i = max(cut.rfind(". "), cut.rfind("; "))
    if i > 80:
        return meta[:i + 1]
    j = cut.rfind(", ")
    return (meta[:j] if j > 80 else cut.rstrip()) + "."

def page(b, path, title, meta, body_html, schema_nodes, og_title=None, extra_script="", noindex=False):
    meta = trim_meta(meta)
    d = depth_of(path)
    url = DOMAIN + path
    graph = [{"@type": "Organization", "@id": ORG_ID, "name": "AL Elite Financing", "url": DOMAIN + "/", "logo": DOMAIN + "/logo.png", "telephone": "+1-888-968-0079", "contactPoint": {"@type": "ContactPoint", "telephone": "+1-888-968-0079", "contactType": "customer service", "areaServed": "US", "availableLanguage": "English"}}] + schema_nodes
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    robots = "noindex, follow" if noindex else "index, follow, max-snippet:-1, max-image-preview:large"
    return f"""<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(title)}</title>
<meta name="description" content="{esc(meta)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="AL Elite Financing">
<meta property="og:title" content="{esc(og_title or title)}">
<meta property="og:description" content="{esc(meta)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{DOMAIN}/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=Public+Sans:wght@400;500;600;700&display=swap">
<style>{BASE_CSS}{EXTRA_CSS}{REVIEW_CSS}</style>
</head>
<body>
{header(b, d)}
<main id="main">
{body_html}
</main>
{footer(b, d)}
<script type="application/ld+json">
{ld}
</script>
<script>{SCRIPT}{extra_script}</script>
</body>
</html>"""

def crumbs_html(b, d, crumbs):
    L = lambda p: link(b, p, d)
    items = "".join(f"<li><a href='{L(p)}'>{esc(n)}</a></li>" if i < len(crumbs) - 1 else f"<li aria-current='page'>{esc(n)}</li>" for i, (n, p) in enumerate(crumbs))
    return f"<nav class='crumbs' aria-label='Breadcrumb'><div class='wrap'><ol>{items}</ol></div></nav>"

def byline():
    return f"<p class='byline'><span>Written by <span class='placeholder'>[author name]</span></span><span>Reviewed by <span class='placeholder'>[finance reviewer, credentials]</span></span><span>Last reviewed {REVIEWED}</span></p>"
