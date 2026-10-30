"""Conversion layer added Oct 30, 2026: multi-step lead form (built at runtime over the existing form so both
templates get it), sticky mobile CTA, calculator-to-form handoff, and GA4 event tracking.
GA4: set GA_ID in common.py (G-XXXXXXX). Events: form_step, generate_lead, lead_magnet, calculator_use,
phone_click, cta_click."""

GROWTH_CSS = """
.lead .step{display:none;border:0;padding:0;background:none}.lead .step.on{display:block}.lead .step::before{content:none}
.lead .progress{display:flex;gap:6px;margin:0 0 16px}.lead .progress span{flex:1;height:4px;border-radius:2px;background:var(--line)}.lead .progress span.done{background:var(--gold)}
.lead .step-title{font-family:var(--serif,Georgia,serif);color:var(--navy);font-size:1.15rem;margin:0 0 12px}
.lead .step-nav{display:flex;gap:10px;align-items:center;margin-top:14px;flex-wrap:wrap}
.lead .btn-back{background:none;border:1.5px solid var(--line);border-radius:var(--radius,8px);padding:10px 14px;color:var(--navy);font:inherit;font-weight:600;cursor:pointer}
.lead .btn-next{background:var(--navy);color:#fff;border:0;border-radius:var(--radius,8px);padding:12px 20px;font:inherit;font-weight:700;cursor:pointer}
.lead .btn-next:hover{background:var(--navy-deep)}
.lead .step-note{font-size:.82rem;color:var(--muted);margin:8px 0 0}
.sticky-cta{position:fixed;left:0;right:0;bottom:0;z-index:900;display:none;background:#fff;border-top:1px solid var(--line);box-shadow:0 -8px 24px rgba(11,37,69,.12);padding:10px 12px calc(10px + env(safe-area-inset-bottom,0px))}
.sticky-cta .in{display:flex;gap:10px;align-items:center;max-width:720px;margin:auto}
.sticky-cta a{flex:1;text-align:center;text-decoration:none;font-weight:700;padding:12px 10px;border-radius:10px;font-size:.95rem}
.sticky-cta .go{background:var(--navy);color:#fff}.sticky-cta .call{border:1.5px solid var(--line);color:var(--navy);flex:0 0 auto;padding:12px 14px}
@media (max-width:760px){.sticky-cta{display:block}.sticky-cta.hide{display:none}body{padding-bottom:70px}}
.calc-handoff{margin-top:14px}.calc-handoff a{display:inline-block;background:var(--gold);color:#071a33;font-weight:700;padding:11px 18px;border-radius:8px;text-decoration:none}
"""

def sticky_cta(L):
    return f"""<div class="sticky-cta" id="stickyCta"><div class="in"><a class="go" href="{L('/#contact')}" data-cta="sticky">Check your options · no credit pull</a><a class="call" href="tel:+1-888-968-0079">Call</a></div></div>"""

GROWTH_JS = r"""
(function(){
  // ---- analytics helper
  window.ALE=window.ALE||{};
  ALE.track=function(name,params){try{if(window.gtag){gtag('event',name,params||{});}}catch(e){}};
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a');if(!a)return;
    if(/^tel:/.test(a.getAttribute('href')||''))ALE.track('phone_click',{location:a.closest('header')?'header':a.closest('footer')?'footer':a.closest('.sticky-cta')?'sticky':'body'});
    else if(a.matches('.btn-primary,.btn-lm,.sticky-cta a,.calc-handoff a,[data-cta]'))ALE.track('cta_click',{label:(a.textContent||'').trim().slice(0,60),cta:a.getAttribute('data-cta')||''});
  },true);
  var calcTracked=false;document.querySelectorAll('.tool-card input,.tool-card select').forEach(function(el){el.addEventListener('input',function(){if(!calcTracked){calcTracked=true;ALE.track('calculator_use',{tool:location.pathname});}});});
  // ---- calculator -> form handoff
  var out=document.querySelector('.tool-card .calc-out');if(out){var h=document.createElement('div');h.className='calc-handoff';h.innerHTML='<a href="#contact" data-cta="calc">Get real offers for this project &rarr;</a>';out.appendChild(h);}
  // ---- sticky CTA hides when the form is on screen
  var sc=document.getElementById('stickyCta'),contact=document.getElementById('contact');
  if(sc&&contact&&'IntersectionObserver' in window){new IntersectionObserver(function(en){en.forEach(function(x){sc.classList.toggle('hide',x.isIntersecting);});},{threshold:0.1}).observe(contact);}
  // ---- multi-step form
  var form=document.getElementById('leadForm');if(!form)return;
  function pick(sel){return Array.prototype.slice.call(form.querySelectorAll(sel));}
  function fieldOf(id){var el=form.querySelector('#'+id);return el?(el.closest('.field')||el.closest('fieldset')||el):null;}
  var s1=[form.querySelector('fieldset'),fieldOf('fproject'),fieldOf('fneed'),fieldOf('fstate')].filter(Boolean);
  var s2=[fieldOf('famount'),fieldOf('fmsg'),fieldOf('fcontact')].filter(Boolean);
  var s3=[fieldOf('fname'),fieldOf('femail'),fieldOf('fphone'),fieldOf('consent')].filter(Boolean);
  var foot=form.querySelector('.form-foot'),hints=pick('p.hint'),hp=form.querySelector('.hp'),err=form.querySelector('#formError');
  if(!s1.length||!s3.length)return;
  var steps=[{t:'Step 1 of 3: What do you need?',els:s1},{t:'Step 2 of 3: A little detail (optional)',els:s2},{t:'Step 3 of 3: Where should we send options?',els:s3}];
  var prog=document.createElement('div');prog.className='progress';prog.innerHTML='<span class="done"></span><span></span><span></span>';
  form.insertBefore(prog,form.firstChild);
  var wraps=steps.map(function(st,i){var w=document.createElement('div');w.className='step'+(i===0?' on':'');var tt=document.createElement('p');tt.className='step-title';tt.textContent=st.t;w.appendChild(tt);st.els.forEach(function(el){var p=el.parentElement;if(p&&p.classList.contains('f2')&&p.children.length===1){w.appendChild(p);}else{w.appendChild(el);}});return w;});
  wraps.forEach(function(w){form.insertBefore(w,foot||null);});
  // move leftover empty .f2 wrappers
  pick('.f2').forEach(function(f){if(!f.children.length)f.remove();});
  if(hp)wraps[2].appendChild(hp);
  if(foot)wraps[2].appendChild(foot);hints.forEach(function(h){wraps[2].appendChild(h);});if(err)wraps[2].appendChild(err);
  function nav(i){var d=document.createElement('div');d.className='step-nav';if(i>0){var b=document.createElement('button');b.type='button';b.className='btn-back';b.textContent='Back';b.addEventListener('click',function(){go(i-1);});d.appendChild(b);}
    if(i<2){var n=document.createElement('button');n.type='button';n.className='btn-next';n.textContent=i===0?'Continue':'Continue to contact details';n.addEventListener('click',function(){if(valid(i))go(i+1);});d.appendChild(n);
      var note=document.createElement('p');note.className='step-note';note.textContent=i===0?'No credit pull. Nothing is shared with a lender until you say so.':'You can skip this step.';d.appendChild(note);}
    return d;}
  wraps.forEach(function(w,i){if(i<2)w.appendChild(nav(i));else{var back=document.createElement('button');back.type='button';back.className='btn-back';back.textContent='Back';back.style.marginRight='10px';back.addEventListener('click',function(){go(1);});if(foot)foot.insertBefore(back,foot.firstChild);}});
  var cur=0;
  function go(i){wraps[cur].classList.remove('on');cur=i;wraps[cur].classList.add('on');prog.querySelectorAll('span').forEach(function(s,k){s.classList.toggle('done',k<=cur);});ALE.track('form_step',{step:cur+1});var f=wraps[cur].querySelector('input:not([type=hidden]):not([type=radio]),select,textarea');if(f&&cur>0)f.focus();}
  function valid(i){var ok=true;wraps[i].querySelectorAll('[required]').forEach(function(el){var bad=el.type==='checkbox'?!el.checked:!el.value;var fld=el.closest('.field');if(fld)fld.classList.toggle('invalid',bad);if(bad)ok=false;});return ok;}
  form.addEventListener('submit',function(){if(!valid(2)){return;}});
  // success tracking: observe the success block
  var suc=document.getElementById('formSuccess');if(suc&&'MutationObserver' in window){new MutationObserver(function(){if(!suc.hidden){ALE.track('generate_lead',{role:(form.querySelector('input[name=role]:checked')||{}).value||'',page:location.pathname});}}).observe(suc,{attributes:true,attributeFilter:['hidden']});}
})();
"""

def ga_snippet(ga_id):
    if not ga_id:
        return ""
    return f"""<script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{ga_id}',{{anonymize_ip:true}});</script>"""
