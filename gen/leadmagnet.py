"""Downloadable-resource lead magnet for blog posts.

Add to an article dict:
    lead_magnet=dict(slug="hail-roof-claim-worksheet", title="...", pitch="...", bullets=[...],
                     pages=8, file="/resources/hail-roof-claim-worksheet.pdf",
                     cover="/resources/hail-roof-claim-worksheet-cover.jpg")
Renders two CTA blocks (mid-article and before the FAQ) and one modal form (name, phone, email).
On submit the form posts to FormSubmit (same endpoint as the contact form): the team gets the lead
by email, the reader gets an automatic thank-you email with the download link, and the page shows
the download button straight away."""
from common import esc, DOMAIN, LEAD_EMAIL

LM_CSS = """
.lm{margin:36px 0;border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--surface);display:grid;grid-template-columns:1.1fr .9fr}
.lm .lm-body{padding:26px 28px}
.lm .pill{display:inline-block;background:var(--gold-soft);color:#8a6a1c;font-weight:700;font-size:.74rem;letter-spacing:.06em;padding:5px 11px;border-radius:999px;margin-bottom:10px}
.lm h3{font-family:var(--serif,Georgia,serif);font-size:1.45rem;line-height:1.2;margin:0 0 8px;color:var(--navy)}
.lm h3 em{font-style:normal;color:var(--gold)}
.lm p{margin:0 0 12px;color:#3c4756}
.lm ul{margin:0 0 16px;padding-left:1.1em;font-size:.95rem}
.lm .lm-cover{background:#e9edf3;min-height:220px}
.lm .lm-cover img{width:100%;height:100%;object-fit:cover;display:block}
.btn-lm{display:inline-block;background:var(--navy);color:#fff;font-weight:700;padding:12px 20px;border-radius:8px;border:0;cursor:pointer;font-size:1rem;text-decoration:none}
.btn-lm:hover{background:var(--navy-deep)}
.lm.lm-compact{grid-template-columns:1fr;margin:24px 0}
.lm.lm-compact .lm-cover{display:none}
@media (max-width:760px){.lm{grid-template-columns:1fr}.lm .lm-cover{order:-1;min-height:0;aspect-ratio:720/400}}
.lm-modal{position:fixed;inset:0;background:rgba(7,26,51,.62);display:none;align-items:center;justify-content:center;z-index:100000;padding:16px}
.lm-modal.open{display:flex}
.lm-dialog{background:#fff;border-radius:14px;max-width:460px;width:100%;padding:26px 26px 22px;position:relative;box-shadow:0 24px 60px rgba(0,0,0,.3);max-height:92vh;overflow:auto}
.lm-dialog h3{font-family:var(--serif,Georgia,serif);color:var(--navy);margin:0 0 6px;font-size:1.3rem}
.lm-dialog p{color:#3c4756;margin:0 0 14px;font-size:.95rem}
.lm-dialog label{display:block;font-weight:600;font-size:.88rem;margin:10px 0 4px;color:var(--navy)}
.lm-dialog input{width:100%;padding:11px 12px;border:1px solid var(--line);border-radius:8px;font-size:1rem;font-family:inherit}
.lm-dialog input:focus{outline:2px solid var(--gold);border-color:var(--gold)}
.lm-dialog .close{position:absolute;top:10px;right:12px;background:none;border:0;font-size:26px;line-height:1;cursor:pointer;color:var(--muted)}
.lm-dialog .btn-lm{width:100%;margin-top:14px;text-align:center}
.lm-dialog .fine{font-size:.76rem;color:var(--muted);margin:10px 0 0}
.lm-dialog .err{color:#b3261e;font-size:.88rem;margin:8px 0 0;display:none}
.lm-done{text-align:center}
.lm-done .tick{width:54px;height:54px;border-radius:50%;background:var(--gold-soft);color:var(--gold);font-size:30px;line-height:54px;margin:0 auto 10px}
"""

def block(lm, compact=False):
    bullets = "".join(f"<li>{esc(b)}</li>" for b in lm.get("bullets", []))
    img = lm.get("mockup") or lm.get("cover")
    cover = f'<div class="lm-cover"><img src="{img}" alt="{esc(lm["title"])} preview" loading="lazy" width="720" height="560"></div>' if img else ""
    return f"""<aside class="lm{' lm-compact' if compact else ''}" aria-label="Free download">
<div class="lm-body"><span class="pill">FREE PDF · {lm.get('pages', '')} PAGES</span>
<h3>{lm['headline']}</h3><p>{esc(lm['pitch'])}</p><ul>{bullets}</ul>
<button type="button" class="btn-lm" data-lm-open>Email me the free worksheet</button></div>{cover}</aside>"""

def modal(lm, page_url):
    thank_you = (f"Thank you for visiting AL Elite Financing.\\n\\nHere is your copy of the {lm['title']}:\\n{DOMAIN}{lm['file']}\\n\\n"
                 "It is fillable on screen (open it in Adobe Reader, Preview or your browser) or you can print it.\\n\\n"
                 "When you know the gap you need to finance, one request at " + DOMAIN + "/roof-financing/ reaches lenders who fund roofs in your state, "
                 "or call (888) 968-0079.\\n\\nAL Elite Financing\\nA matching service, not a lender.")
    return f"""<div class="lm-modal" id="lmModal" role="dialog" aria-modal="true" aria-labelledby="lmTitle">
<div class="lm-dialog">
<button type="button" class="close" aria-label="Close" data-lm-close>&times;</button>
<form id="lmForm" novalidate>
<h3 id="lmTitle">Where should we send the worksheet?</h3>
<p>We'll email you the PDF right away and show the download link here too.</p>
<label for="lmName">Full name</label><input id="lmName" name="name" type="text" autocomplete="name" required>
<label for="lmEmail">Email address</label><input id="lmEmail" name="email" type="email" autocomplete="email" required>
<label for="lmPhone">Phone number</label><input id="lmPhone" name="phone" type="tel" autocomplete="tel" required>
<input type="text" name="website" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
<p class="err" id="lmErr">Please check your name, email and phone, then try again.</p>
<button type="submit" class="btn-lm" id="lmSubmit">Send me the worksheet</button>
<p class="fine">By submitting, you agree AL Elite Financing may contact you about this resource and financing options by email, phone or text. AL Elite is a matching service, not a lender. <a href="/privacy/">Privacy policy</a>.</p>
</form>
<div class="lm-done" id="lmDone" hidden>
<div class="tick">&#10003;</div><h3>Check your inbox</h3>
<p>Thank you for visiting AL Elite Financing. We've emailed the worksheet to <strong id="lmSentTo"></strong>. You can also download it now:</p>
<a class="btn-lm" href="{lm['file']}" download>Download the PDF</a>
<p class="fine">Didn't get the email? Check spam, or use the download button above.</p>
</div></div></div>
<script>(function(){{
var modal=document.getElementById('lmModal'),form=document.getElementById('lmForm'),done=document.getElementById('lmDone');
function open(){{modal.classList.add('open');document.body.style.overflow='hidden';setTimeout(function(){{var f=document.getElementById('lmName');if(f)f.focus();}},50);}}
function close(){{modal.classList.remove('open');document.body.style.overflow='';}}
document.querySelectorAll('[data-lm-open]').forEach(function(b){{b.addEventListener('click',open);}});
document.querySelectorAll('[data-lm-close]').forEach(function(b){{b.addEventListener('click',close);}});
modal.addEventListener('click',function(e){{if(e.target===modal)close();}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape')close();}});
form.addEventListener('submit',function(e){{
  e.preventDefault();
  var name=form.name.value.trim(),email=form.email.value.trim(),phone=form.phone.value.trim(),err=document.getElementById('lmErr');
  if(name.length<2||!/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(email)||phone.replace(/\\D/g,'').length<7){{err.style.display='block';return;}}
  if(form.website.value){{return;}}
  err.style.display='none';var sb=document.getElementById('lmSubmit');sb.disabled=true;sb.textContent='Sending...';
  var lead={{name:name,email:email,phone:phone,resource:'{esc(lm['title'])}',file:'{lm['file']}',page:'{page_url}'}};
  function finish(sent){{document.getElementById('lmSentTo').textContent=email;form.hidden=true;done.hidden=false;
    if(!sent){{done.querySelector('p').innerHTML='Thank you for visiting AL Elite Financing. Your download is ready below. (We could not confirm the email send, so please use the button.)';}}
    sb.disabled=false;sb.textContent='Send me the worksheet';}}
  function viaFormSubmit(){{
    var data={{name:name,email:email,phone:phone,resource:lead.resource,download_link:'{DOMAIN}{lm['file']}',page:lead.page,submitted_at:new Date().toISOString(),
      _subject:'Worksheet download: {esc(lm['title'])} - '+name,_template:'table',_captcha:'false',_replyto:email,_autoresponse:'{thank_you}'}};
    return fetch('https://formsubmit.co/ajax/{LEAD_EMAIL}',{{method:'POST',headers:{{'Content-Type':'application/json','Accept':'application/json'}},body:JSON.stringify(data)}})
      .then(function(r){{return r.json().then(function(j){{return r.ok&&String(j.success)!=='false';}});}}).catch(function(){{return false;}});
  }}
  // Preferred: our own endpoint emails the PDF as an attachment (Resend). Falls back to FormSubmit if not configured.
  fetch('/api/download',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(lead)}})
    .then(function(r){{return r.json().then(function(j){{return {{status:r.status,ok:r.ok&&j.ok}};}});}})
    .catch(function(){{return {{status:0,ok:false}};}})
    .then(function(res){{if(res.ok)return finish(true);return viaFormSubmit().then(finish);}});
}});
}})();</script>"""
