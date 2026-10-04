"""Page-type renderers: service (consumer + B2B), hub, city, tool, article, plain."""
from common import *

def service_page(b, p):
    """p: dict with path, crumbs, h1, title, meta, eyebrow, answer, cta_points, sections[(h2,html)],
    options[(name, desc, pro, con)], amounts, qualify[], faqs[(q,a)], related[(name,path)], role, project/need, service_name"""
    path = p["path"]; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    cta_points = "".join(f"<li>{x}</li>" for x in p.get("cta_points", []))
    sections = []
    for h2, body in p.get("sections", []):
        sid = re.sub(r"[^a-z0-9]+", "-", h2.lower()).strip("-")
        sections.append(f"<h2 id='{sid}'>{esc(h2)}</h2>{body}")
    options = ""
    if p.get("options"):
        options = "<h2 id='options'>" + esc(p.get("options_h2", "How people pay for it: the options compared")) + "</h2><div class='compare'>" + "".join(
            f"<div class='opt'><h3>{esc(n)}</h3><p>{desc}</p><p class='pro'>{pro}</p><p class='con'>{con}</p></div>" for n, desc, pro, con in p["options"]) + "</div>"
    pay = ""
    if p.get("amounts"):
        pay = f"<h2 id='payments'>{esc(p.get('pay_h2','What the monthly payment might look like'))}</h2><p>{p.get('pay_intro','The table shows arithmetic, not offers. Lenders in the network quote their own APR and term after reviewing your application.')}</p>" + payment_table(p["amounts"], aprs=p.get("aprs", (7.99, 11.99, 17.99)), terms=p.get("terms", (36, 60, 84, 120)))
    qualify = ""
    if p.get("qualify"):
        qualify = f"<h2 id='qualify'>{esc(p.get('qualify_h2','Who qualifies'))}</h2><p>{p.get('qualify_intro','Every lender sets its own criteria. The things that come up most often:')}</p><ul>" + "".join(f"<li>{x}</li>" for x in p["qualify"]) + "</ul>"
    faqs = p.get("faqs", [])
    faq_block = f"<h2 id='faq'>Frequently asked questions</h2>{faq_html(faqs)}" if faqs else ""
    related = "".join(f"<li><a href='{L(rp)}'>{esc(rn)}</a></li>" for rn, rp in p.get("related", []))
    side_extra = p.get("side_extra", "")
    toc_items = [("How it works", "#how"), *[(h, "#" + re.sub(r"[^a-z0-9]+", "-", h.lower()).strip("-")) for h, _ in p.get("sections", [])]]
    if options: toc_items.append(("Options compared", "#options"))
    if pay: toc_items.append(("Monthly payments", "#payments"))
    if qualify: toc_items.append(("Who qualifies", "#qualify"))
    if faqs: toc_items.append(("FAQ", "#faq"))
    toc = "<div class='toc'><h2>On this page</h2><ol>" + "".join(f"<li><a href='{a}'>{esc(t)}</a></li>" for t, a in toc_items) + "</ol></div>"
    how = p.get("how") or f"""<h2 id='how'>How AL Elite works for {p.get('how_noun','this')}</h2><ol>
<li><strong>Tell us about it.</strong> {p.get('how_1','The project, rough cost and your state. Two minutes, no credit pull.')}</li>
<li><strong>We match you.</strong> {p.get('how_2','Your request goes only to lenders in our network who fund this kind of project in your state. We show you up front whether each one starts with a soft or hard credit inquiry.')}</li>
<li><strong>You choose and apply with the lender.</strong> {p.get('how_3','Rates, fees, terms and the approval decision come from the lender. Compare the disclosures, pick one or walk away. AL Elite never charges you.')}</li></ol>"""
    verify = f"<div class='verify'><strong>Before publishing:</strong> {p['verify']}</div>" if p.get("verify") else ""
    body = f"""{crumbs_html(b, d, p['crumbs'])}
<section class="page-hero"><div class="wrap">
<div class="stack"><p class="eyebrow">{esc(p['eyebrow'])}</p><h1>{p['h1']}</h1><p class="answer-first" id="speakable-summary">{p['answer']}</p>{byline()}</div>
<div class="cta-box"><h2>{esc(p.get('cta_h','Check your options'))}</h2><p>{p.get('cta_p','Free to compare. Not a loan application. Nothing is shared with a lender until you say so.')}</p><ul>{cta_points}</ul><a class="btn btn-light" href="#contact">{esc(p.get('cta_btn','Get matched'))}</a></div>
</div></section>
<section><div class="wrap layout">
<article class="prose">{toc}{verify}{p.get('intro','')}{how}{''.join(sections)}{options}{pay}{qualify}{faq_block}</article>
<aside class="side">
<div class="box"><h3>Related pages</h3><ul>{related}</ul></div>
{side_extra}
<div class="box"><h3>Good to know</h3><p style="font-size:.92rem;color:var(--ink-2)">AL Elite is paid by lenders and partner contractors, never by you. Read <a href="{L('/how-we-make-money/')}">how we make money</a>.</p></div>
</aside></div></section>
{contact_section(b, d, role=p.get('role','homeowner'), project=p.get('project'), need=p.get('need'))}"""
    schema = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["meta"], "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": "2026-10-04", "inLanguage": "en-US", "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#speakable-summary"]}},
        {"@type": "Service", "@id": url + "#service", "name": p.get("service_name", strip_tags(p["h1"])), "serviceType": p.get("service_type", "Financing matching"), "provider": {"@id": ORG_ID}, "areaServed": {"@type": "Country", "name": "United States"}, "description": strip_tags(p["answer"]), "url": url, "audience": {"@type": "Audience", "audienceType": p.get("audience", "Homeowners")}},
        breadcrumb_schema(p["crumbs"]),
    ]
    if faqs: schema.append(faq_schema(faqs, url))
    return page(b, path, p["title"], p["meta"], body, schema)


def hub_page(b, p):
    """Hub: intro answer + card grid of children + prose + FAQ."""
    path = p["path"]; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    cards = "".join(f"<a class='card' href='{L(cp)}'><span class='tag'>{esc(tag)}</span><h3>{esc(n)}</h3><p>{desc}</p></a>" for tag, n, desc, cp in p["cards"])
    faqs = p.get("faqs", [])
    body = f"""{crumbs_html(b, d, p['crumbs'])}
<section class="page-hero"><div class="wrap">
<div class="stack"><p class="eyebrow">{esc(p['eyebrow'])}</p><h1>{p['h1']}</h1><p class="answer-first" id="speakable-summary">{p['answer']}</p>{byline()}</div>
<div class="cta-box"><h2>{esc(p.get('cta_h','Check your options'))}</h2><p>{p.get('cta_p','Free to compare. Not a loan application.')}</p><ul>{''.join(f'<li>{x}</li>' for x in p.get('cta_points',[]))}</ul><a class="btn btn-light" href="#contact">{esc(p.get('cta_btn','Get matched'))}</a></div>
</div></section>
<section><div class="wrap"><div class="sec-head"><p class="eyebrow">{esc(p.get('cards_eyebrow','Pages in this section'))}</p><h2>{esc(p['cards_h2'])}</h2></div><div class="grid-cards">{cards}</div></div></section>
<section><div class="wrap layout"><article class="prose">{p.get('prose','')}{('<h2 id=faq>Frequently asked questions</h2>' + faq_html(faqs)) if faqs else ''}</article>
<aside class="side"><div class="box"><h3>Related pages</h3><ul>{''.join(f"<li><a href='{L(rp)}'>{esc(rn)}</a></li>" for rn, rp in p.get('related', []))}</ul></div></aside></div></section>
{contact_section(b, d, role=p.get('role','homeowner'), project=p.get('project'), need=p.get('need'))}"""
    schema = [
        {"@type": "CollectionPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["meta"], "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": "2026-10-04", "inLanguage": "en-US", "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#speakable-summary"]}},
        {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "url": DOMAIN + cp} for i, (tag, n, desc, cp) in enumerate(p["cards"])]},
        breadcrumb_schema(p["crumbs"]),
    ]
    if faqs: schema.append(faq_schema(faqs, url))
    return page(b, path, p["title"], p["meta"], body, schema)


def plain_page(b, p):
    path = p["path"]; d = depth_of(path); url = DOMAIN + path
    body = f"""{crumbs_html(b, d, p['crumbs'])}
<section class="page-hero"><div class="wrap" style="grid-template-columns:1fr"><div class="stack article-head"><p class="eyebrow">{esc(p['eyebrow'])}</p><h1>{p['h1']}</h1><p class="answer-first" id="speakable-summary">{p['answer']}</p>{byline() if p.get('byline', True) else ''}</div></div></section>
<section><div class="wrap layout"><article class="prose">{p['prose']}{('<h2 id=faq>Frequently asked questions</h2>' + faq_html(p['faqs'])) if p.get('faqs') else ''}</article>
<aside class="side"><div class="box"><h3>Related pages</h3><ul>{''.join(f"<li><a href='{link(b, rp, d)}'>{esc(rn)}</a></li>" for rn, rp in p.get('related', []))}</ul></div></aside></div></section>
{contact_section(b, d, role=p.get('role','homeowner')) if p.get('form', True) else ''}"""
    schema = [{"@type": p.get("type", "WebPage"), "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["meta"], "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": "2026-10-04", "inLanguage": "en-US"}, breadcrumb_schema(p["crumbs"])]
    if p.get("faqs"): schema.append(faq_schema(p["faqs"], url))
    schema += p.get("extra_schema", [])
    return page(b, path, p["title"], p["meta"], body, schema, noindex=p.get("noindex", False))


def article_page(b, p):
    """Blog article with Article schema. p: path, title, h1, meta, answer, sections[(h2, html)], faqs, money_page(name,path), related, date"""
    path = p["path"]; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    secs = "".join(f"<h2 id='{re.sub(r'[^a-z0-9]+','-',h.lower()).strip('-')}'>{esc(h)}</h2>{body}" for h, body in p["sections"])
    toc = "<div class='toc'><h2>In this article</h2><ol>" + "".join(f"<li><a href='#{re.sub(r'[^a-z0-9]+','-',h.lower()).strip('-')}'>{esc(h)}</a></li>" for h, _ in p["sections"]) + "</ol></div>"
    mn, mp = p["money_page"]
    body = f"""{crumbs_html(b, d, p['crumbs'])}
<section class="page-hero"><div class="wrap" style="grid-template-columns:1fr"><div class="stack article-head"><p class="eyebrow">{esc(p['eyebrow'])}</p><h1>{p['h1']}</h1><p class="answer-first" id="speakable-summary">{p['answer']}</p>{byline()}</div></div></section>
<section><div class="wrap layout"><article class="prose">{toc}{secs}{('<h2 id=faq>Frequently asked questions</h2>' + faq_html(p['faqs'])) if p.get('faqs') else ''}
<div class="callout"><strong>Ready to compare options?</strong> Our <a href="{L(mp)}">{esc(mn)}</a> page explains what lenders look for and shows example payments. Or <a href="#contact">tell us about your situation</a> and we'll match you.</div></article>
<aside class="side"><div class="box"><h3>Related</h3><ul>{''.join(f"<li><a href='{L(rp)}'>{esc(rn)}</a></li>" for rn, rp in p.get('related', []))}</ul></div></aside></div></section>
{contact_section(b, d, role=p.get('role','homeowner'), project=p.get('project'), need=p.get('need'))}"""
    schema = [
        {"@type": "Article", "@id": url + "#article", "headline": strip_tags(p["h1"]), "description": p["meta"], "url": url, "mainEntityOfPage": url, "datePublished": p.get("date", "2026-10-04"), "dateModified": "2026-10-04", "inLanguage": "en-US",
         "author": {"@type": "Person", "name": "[Author name]", "url": DOMAIN + "/about/"}, "publisher": {"@id": ORG_ID}, "about": p.get("about", strip_tags(p["h1"])),
         "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#speakable-summary"]}},
        breadcrumb_schema(p["crumbs"]),
    ]
    if p.get("faqs"): schema.append(faq_schema(p["faqs"], url))
    return page(b, path, p["title"], p["meta"], body, schema)
