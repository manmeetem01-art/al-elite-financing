"""Calculator pages: roof financing calculator and equipment loan calculator, with amortization schedule."""
from common import *

HOME = ("Home", "/")

CALC_JS = """
(function(){
  var amt=document.getElementById('c-amt'),term=document.getElementById('c-term'),apr=document.getElementById('c-apr'),down=document.getElementById('c-down');
  if(!amt)return;
  var usd=new Intl.NumberFormat('en-US',{style:'currency',currency:'USD',minimumFractionDigits:2});
  var usd0=new Intl.NumberFormat('en-US',{style:'currency',currency:'USD',maximumFractionDigits:0});
  function calc(){
    var P=Math.max(0,(+amt.value||0)-(down?(+down.value||0):0)),n=+term.value,a=+apr.value;
    if(n<1||P<=0){return;}
    var m=ALE.payment(P,a,n);
    document.getElementById('c-pay').innerHTML=usd.format(m)+'<small>per month</small>';
    document.getElementById('c-int').textContent=usd.format(m*n-P);
    document.getElementById('c-tot').textContent=usd.format(m*n);
    document.getElementById('c-fin').textContent=usd0.format(P);
    var cmp=document.getElementById('c-cmp');if(cmp){var rows='';[36,60,84,120,144].forEach(function(t){var mm=ALE.payment(P,a,t);rows+='<tr'+(t===n?' style="background:var(--surface)"':'')+'><td>'+t+' months</td><td class="num">'+usd.format(mm)+'</td><td class="num">'+usd.format(mm*t-P)+'</td><td class="num">'+usd.format(mm*t)+'</td></tr>';});cmp.innerHTML=rows;}
    var sch=document.getElementById('c-sched');if(sch){var bal=P,r=a/100/12,rows2='';for(var i=1;i<=n;i++){var it=bal*r,pr=m-it;bal=Math.max(0,bal-pr);rows2+='<tr><td>'+i+'</td><td class="num">'+usd.format(pr)+'</td><td class="num">'+usd.format(it)+'</td><td class="num">'+usd.format(bal)+'</td></tr>';}sch.innerHTML=rows2;}
  }
  [amt,term,apr,down].forEach(function(el){if(el)el.addEventListener('input',calc);});calc();
})();
"""

def calc_widget(default_amt, min_amt, max_amt, step, terms, default_term, default_apr, with_down=False, amount_label="Project cost"):
    topt = "".join(f"<option value='{t}'{' selected' if t==default_term else ''}>{t} months ({t//12} yr{'s' if t//12!=1 else ''}{'' if t%12==0 else ' ' + str(t%12) + ' mo'})</option>" for t in terms)
    down = f"<label for='c-down'><span class='row'><span>Down payment or trade-in</span></span><input type='number' id='c-down' min='0' step='500' value='0'></label>" if with_down else ""
    return f"""<div class="tool-card">
<div class="calc-inputs">
<label for="c-amt"><span class="row"><span>{amount_label}</span></span><input type="number" id="c-amt" min="{min_amt}" max="{max_amt}" step="{step}" value="{default_amt}"></label>
{down}
<label for="c-term"><span class="row"><span>Term</span></span><select id="c-term">{topt}</select></label>
<label for="c-apr"><span class="row"><span>Example APR (%)</span></span><input type="number" id="c-apr" min="0" max="40" step="0.01" value="{default_apr}"></label>
</div>
<div class="calc-out" aria-live="polite">
<div><p class="eyebrow" style="color:var(--gold)">Estimated monthly payment</p><p class="big" id="c-pay">$0.00<small>per month</small></p></div>
<dl><div><dt>Amount financed</dt><dd id="c-fin">$0</dd></div><div><dt>Total interest</dt><dd id="c-int">$0.00</dd></div><div><dt>Total repaid</dt><dd id="c-tot">$0.00</dd></div></dl>
<p class="note">Example only. Standard amortization, no fees. Your APR, fees and term are set by the lender and disclosed before you sign. Subject to credit approval.</p>
</div></div>
<h2 id="compare-terms">Same amount, different terms</h2>
<div class="tbl"><table><thead><tr><th>Term</th><th class="num">Monthly payment</th><th class="num">Total interest</th><th class="num">Total repaid</th></tr></thead><tbody id="c-cmp"></tbody></table></div>
<p class="cap">The highlighted row is the term selected above. A longer term lowers the payment and raises the total interest.</p>
<h2 id="schedule">Amortization schedule</h2>
<div class="tbl sched"><table><thead><tr><th>Month</th><th class="num">Principal</th><th class="num">Interest</th><th class="num">Balance</th></tr></thead><tbody id="c-sched"></tbody></table></div>"""

def tool_page(b, p):
    path = p["path"]; d = depth_of(path); L = lambda x: link(b, x, d); url = DOMAIN + path
    faqs = p["faqs"]
    body = f"""{crumbs_html(b, d, p['crumbs'])}
<section class="page-hero"><div class="wrap" style="grid-template-columns:1fr"><div class="stack article-head"><p class="eyebrow">{esc(p['eyebrow'])}</p><h1>{p['h1']}</h1><p class="answer-first" id="speakable-summary">{p['answer']}</p>{byline()}</div></div></section>
<section><div class="wrap layout"><article class="prose">{p['widget']}{p['prose']}<h2 id="faq">Frequently asked questions</h2>{faq_html(faqs)}</article>
<aside class="side"><div class="box"><h3>Related pages</h3><ul>{''.join(f"<li><a href='{L(rp)}'>{esc(rn)}</a></li>" for rn, rp in p['related'])}</ul></div>
<div class="cta-box"><h3>{esc(p['cta_h'])}</h3><p>{p['cta_p']}</p><a class="btn btn-light" href="#contact">Get matched</a></div></aside></div></section>
{contact_section(b, d, role=p['role'], project=p.get('project'), need=p.get('need'))}"""
    schema = [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": p["title"], "description": p["meta"], "isPartOf": {"@id": DOMAIN + "/#website"}, "dateModified": "2026-10-04", "inLanguage": "en-US", "speakable": {"@type": "SpeakableSpecification", "cssSelector": ["#speakable-summary"]}},
        {"@type": "WebApplication", "@id": url + "#app", "name": strip_tags(p["h1"]), "url": url, "applicationCategory": "FinanceApplication", "operatingSystem": "Any", "browserRequirements": "Requires JavaScript", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "provider": {"@id": ORG_ID}, "description": strip_tags(p["answer"])},
        breadcrumb_schema(p["crumbs"]), faq_schema(faqs, url),
    ]
    return page(b, path, p["title"], p["meta"], body, schema, extra_script=CALC_JS)

ROOF_CALC = dict(
    path="/tools/roof-financing-calculator/", crumbs=[HOME, ("Tools", "/tools/roof-financing-calculator/"), ("Roof financing calculator", "/tools/roof-financing-calculator/")],
    eyebrow="Roof financing calculator", h1="Roof financing calculator: what a new roof costs per month",
    title="Roof Financing Calculator | Roof Loan Payment Calculator | AL Elite",
    meta="Free roof financing calculator: enter the roof cost, term and an example APR to see the monthly payment, total interest and a full amortization schedule. Compare 3, 5, 7, 10 and 12-year terms. Not an offer; AL Elite is a matching service.",
    answer="This roof loan calculator estimates the monthly payment on a roof financed over a fixed term using standard amortization. Enter the quote amount, pick a term and an example APR, and it shows the payment, total interest, a term-by-term comparison and the month-by-month schedule. It's arithmetic, not an offer; lenders set real rates after reviewing your application.",
    widget=calc_widget(15000, 1000, 100000, 500, (36, 60, 84, 120, 144), 60, "9.99", amount_label="Roof quote (USD)"),
    prose="""<h2 id="how-to-use">How to use the roof financing calculator</h2>
<ol><li><strong>Enter the roof quote.</strong> Use the itemized contractor estimate, including tear-off, decking allowance and gutters if they're in the job. If insurance is paying part, enter only the gap you'll finance.</li>
<li><strong>Pick a term.</strong> Unsecured roof loans commonly run three to seven years; home equity products can run longer. The comparison table shows what each term does to the payment and the total interest.</li>
<li><strong>Enter an example APR.</strong> We don't know your rate; the lender will quote it. Try a few values. Lower credit scores generally mean higher APRs.</li></ol>
<h2 id="reading-the-results">Reading the results</h2>
<p>The monthly payment is what most people look at. The total interest line is what they should also look at. Stretching a roof loan from five years to twelve can cut the payment by a third and roughly double the interest. For a roof expected to last 20 to 25 years, a term in the five-to-ten-year range usually balances the two. For a <a href="/roof-financing/metal-roof-financing/">metal roof</a> expected to last far longer, a longer term is easier to justify.</p>
<p>The amortization schedule shows how each payment splits between principal and interest. Early payments are interest-heavy; if you expect to pay the loan off early (for example when an insurance check arrives), check whether the lender charges a prepayment penalty.</p>
<h2 id="what-the-calculator-leaves-out">What the calculator leaves out</h2>
<ul><li><strong>Fees.</strong> Some lenders charge an origination fee, deducted from the loan or added to it. Ask.</li><li><strong>Promotional plans.</strong> Contractor "no interest if paid in full" offers don't amortize like this and carry deferred interest if you miss the deadline.</li><li><strong>Variable rates.</strong> HELOCs usually have variable rates; this calculator assumes fixed.</li><li><strong>Insurance and rebates.</strong> A claim payout or utility rebate reduces what you need to finance; enter the net amount.</li></ul>
<p>When you're ready, the <a href="/roof-financing/">roof financing</a> page explains the options and what lenders look for, or <a href="#contact">tell us about the roof</a> and we'll match you with lenders.</p>""",
    faqs=[
        ("How much is a $15,000 roof per month?", "At 9.99% APR with no fees, about $319 a month over 60 months, $249 over 84 months, or $198 over 120 months. Total interest rises from roughly $4,100 to roughly $8,800 across those terms. These are illustrations; your lender sets the real rate."),
        ("How much is a $20,000 roof per month?", "At 9.99% APR with no fees, about $425 a month over 60 months or $264 over 120 months. Enter your own quote and rate above for exact figures at any APR."),
        ("What APR should I use in the calculator?", "Use a range. Lenders set APRs on credit profile, income, amount and term. Try a lower value for strong credit and a higher one for fair credit, and look at how much the total interest changes."),
        ("Is this calculator an offer of credit?", "No. It performs standard loan arithmetic. AL Elite is a matching service, not a lender; actual offers come from lenders after an application."),
        ("Does the calculator work for other projects?", "Yes. The math is the same for HVAC, siding, windows or any fixed-term instalment loan. Enter that project's cost instead."),
    ],
    related=[("Roof financing", "/roof-financing/"), ("Roof financing with bad credit", "/roof-financing/bad-credit-roof-financing/"), ("Metal roof financing", "/roof-financing/metal-roof-financing/"), ("How to finance a new roof: 6 options", "/blog/how-to-finance-a-new-roof/"), ("Equipment loan calculator (for contractors)", "/tools/equipment-loan-calculator/")],
    cta_h="Ready for real numbers?", cta_p="Tell us about the roof and we'll match you with lenders who fund roofing. Free, and no credit pull to start.",
    role="homeowner", project="Roof replacement or repair",
)

EQUIP_CALC = dict(
    path="/tools/equipment-loan-calculator/", crumbs=[HOME, ("Tools", "/tools/roof-financing-calculator/"), ("Equipment loan calculator", "/tools/equipment-loan-calculator/")],
    eyebrow="Equipment loan calculator", h1="Equipment loan calculator: payments on excavators, trucks and tools",
    title="Equipment Loan Calculator | Equipment Financing Payment Calculator | AL Elite",
    meta="Free equipment loan calculator for contractors: enter the equipment price, down payment, term and an example APR to see the monthly payment, total interest and a full amortization schedule. Compare 3 to 7-year terms. Not an offer.",
    answer="This equipment financing calculator estimates the monthly payment on an equipment or truck loan after any down payment, over a fixed term, using standard amortization. Enter the price, down payment, term and an example APR to see the payment, total interest, a term comparison and the month-by-month schedule. It's arithmetic, not an offer; equipment lenders quote real rates after reviewing the business and the asset.",
    widget=calc_widget(90000, 2000, 1000000, 1000, (24, 36, 48, 60, 72, 84), 60, "9.5", with_down=True, amount_label="Equipment price (USD)"),
    prose="""<h2 id="how-to-use">How to use the equipment loan calculator</h2>
<ol><li><strong>Enter the equipment price,</strong> including delivery and any attachments financed with it.</li>
<li><strong>Enter a down payment or trade-in.</strong> Many equipment lenders ask for a down payment on used machines or for newer businesses. The calculator finances the difference.</li>
<li><strong>Pick a term.</strong> Equipment terms usually track the asset's useful life: shorter for used machines and light equipment, longer for new heavy equipment and trucks.</li>
<li><strong>Enter an example APR.</strong> Equipment loans are secured, so rates are often lower than unsecured business credit. Try a range.</li></ol>
<h2 id="loan-vs-lease">Loan payment vs lease payment</h2>
<p>This calculator models a loan (or a $1-buyout lease, which is economically the same). A fair-market-value lease has a lower payment because you're not paying the machine down to zero; you return it or buy it at market value at the end. If a dealer quotes a lease payment that's much lower than the loan figure here, that's why, and the question becomes whether you want to own the equipment. Our <a href="/contractor-business-loans/equipment-financing/">equipment financing</a> page compares the structures.</p>
<h2 id="what-the-calculator-leaves-out">What the calculator leaves out</h2>
<ul><li><strong>Documentation and origination fees,</strong> which vary by lender.</li><li><strong>Sales tax,</strong> which may be financed or paid up front depending on the state and lender.</li><li><strong>Insurance,</strong> which lenders require on financed equipment.</li><li><strong>Tax treatment.</strong> Depreciation and expensing elections affect the real cost of ownership; ask your accountant.</li><li><strong>Factor-rate products.</strong> Some short-term lenders quote a factor rate, not an APR. This calculator assumes APR; ask any lender for the APR equivalent.</li></ul>
<p>When you've got a number you like, <a href="#contact">tell us what you're buying</a> and we'll match you with equipment lenders, or read about <a href="/contractor-business-loans/dump-truck-financing/">dump truck financing</a> if it's a vehicle.</p>""",
    faqs=[
        ("How much is a $90,000 excavator per month?", "With no down payment at 9.5% APR, about $1,890 a month over 60 months or $1,470 over 84 months. With $15,000 down, about $1,575 and $1,225 respectively. Illustrative only; equipment lenders set real rates."),
        ("What term should I finance equipment over?", "Match it to the useful life and how long you'll keep the machine. Financing a used skid steer over seven years means paying for it after it's worn out; financing a new excavator over three years means a heavy payment for an asset that will work for a decade."),
        ("Do I need a down payment for equipment financing?", "Often, especially for used equipment or businesses under two years old. Requirements vary by lender; some finance 100% for established businesses on new equipment."),
        ("Is this calculator an offer of credit?", "No. It performs standard loan arithmetic. AL Elite is a matching service, not a lender; actual offers come from lenders after an application."),
        ("Does it work for trucks and vans?", "Yes. Commercial vehicle loans amortize the same way. Enter the vehicle price and any trade-in as the down payment."),
    ],
    related=[("Construction equipment financing", "/contractor-business-loans/equipment-financing/"), ("Dump truck financing", "/contractor-business-loans/dump-truck-financing/"), ("Working capital for contractors", "/contractor-business-loans/working-capital/"), ("Contractor business loans", "/contractor-business-loans/"), ("Roof financing calculator (for homeowners)", "/tools/roof-financing-calculator/")],
    cta_h="Ready to get matched?", cta_p="Tell us what you're buying and we'll route you to equipment lenders who fund it. No credit pull to compare.",
    role="contractor", need="Equipment financing",
)

TOOL_PAGES = [ROOF_CALC, EQUIP_CALC]
