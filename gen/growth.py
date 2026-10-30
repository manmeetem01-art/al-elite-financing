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
.qm{position:fixed;inset:0;background:rgba(7,26,51,.62);display:none;align-items:center;justify-content:center;z-index:100000;padding:16px}.qm.open{display:flex}
.qm .qm-box{background:#fff;border-radius:14px;max-width:440px;width:100%;padding:26px 24px 20px;position:relative;box-shadow:0 24px 60px rgba(0,0,0,.3)}
.qm .qm-close{position:absolute;top:10px;right:12px;background:none;border:0;font-size:26px;line-height:1;cursor:pointer;color:var(--muted)}
.qm .eyebrow{color:var(--gold);font-size:.74rem;font-weight:700;letter-spacing:.08em;margin:0 0 6px}
.qm h3{font-family:var(--serif,Georgia,serif);color:var(--navy);margin:0 0 6px;font-size:1.3rem}
.qm p{color:#3c4756;margin:0 0 14px;font-size:.95rem}
.qm .qm-roles{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:10px}
.qm .qm-roles label{border:1.5px solid var(--line);border-radius:10px;padding:10px;display:flex;gap:8px;align-items:center;cursor:pointer;font-weight:600;color:var(--navy)}
.qm .qm-roles input:checked+span{color:var(--navy)}.qm .qm-roles label.on{border-color:var(--navy);background:var(--surface)}
.qm select{width:100%;padding:11px 12px;border:1px solid var(--line);border-radius:8px;font:inherit;font-size:1rem;margin-bottom:10px}
.qm .btn-next{width:100%;background:var(--navy);color:#fff;border:0;border-radius:8px;padding:13px;font:inherit;font-weight:700;cursor:pointer;font-size:1rem}
.qm .fine{font-size:.78rem;color:var(--muted);margin:10px 0 0;text-align:center}
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
  // ---- quick-start modal (trigger-based, never on load)
  var form=document.getElementById('leadForm');
  if(form){
    var projSel=form.querySelector('#fproject'),needSel=form.querySelector('#fneed'),stSel=form.querySelector('#fstate');
    var qm=document.createElement('div');qm.className='qm';qm.id='quickStart';qm.setAttribute('role','dialog');qm.setAttribute('aria-modal','true');
    qm.innerHTML='<div class="qm-box"><button type="button" class="qm-close" aria-label="Close">&times;</button><p class="eyebrow">Free to compare · no credit pull</p><h3>See financing options for your project</h3><p>Three quick questions. Nothing is shared with a lender until you say so.</p>'
      +'<div class="qm-roles"><label class="on"><input type="radio" name="qrole" value="homeowner" checked hidden><span>Homeowner</span></label><label><input type="radio" name="qrole" value="contractor" hidden><span>Contractor</span></label></div>'
      +'<select id="qproj" aria-label="Project type">'+(projSel?projSel.innerHTML:'')+'</select><select id="qneed" aria-label="What do you need" hidden>'+(needSel?needSel.innerHTML:'')+'</select><select id="qstate" aria-label="State">'+(stSel?stSel.innerHTML:'')+'</select>'
      +'<button type="button" class="btn-next" id="qgo">Continue &rarr;</button><p class="fine">Not a loan application. AL Elite is a matching service, not a lender.</p></div>';
    document.body.appendChild(qm);
    var roleLabels=qm.querySelectorAll('.qm-roles label');roleLabels.forEach(function(l){l.addEventListener('click',function(){roleLabels.forEach(function(x){x.classList.remove('on');});l.classList.add('on');var con=l.querySelector('input').value==='contractor';qm.querySelector('#qproj').hidden=con;qm.querySelector('#qneed').hidden=!con;});});
    var shown=false;function openQ(src){if(shown&&src!=='cta')return;shown=true;try{sessionStorage.setItem('ale_qm','1');}catch(e){}qm.classList.add('open');document.body.style.overflow='hidden';ALE.track('quickstart_open',{source:src});}
    function closeQ(){qm.classList.remove('open');document.body.style.overflow='';}
    qm.querySelector('.qm-close').addEventListener('click',closeQ);qm.addEventListener('click',function(e){if(e.target===qm)closeQ();});document.addEventListener('keydown',function(e){if(e.key==='Escape')closeQ();});
    qm.querySelector('#qgo').addEventListener('click',function(){var con=qm.querySelector('input[name=qrole]:checked').value==='contractor';var st=qm.querySelector('#qstate').value;
      if(!st){qm.querySelector('#qstate').focus();qm.querySelector('#qstate').style.borderColor='#b3261e';return;}
      var r=form.querySelector(con?'#role-con':'#role-home');if(r){r.checked=true;r.dispatchEvent(new Event('change',{bubbles:true}));}
      if(con&&needSel)needSel.value=qm.querySelector('#qneed').value;if(!con&&projSel)projSel.value=qm.querySelector('#qproj').value;if(stSel)stSel.value=st;
      closeQ();ALE.track('quickstart_continue',{role:con?'contractor':'homeowner'});
      var c=document.getElementById('contact');if(c){c.scrollIntoView({behavior:'smooth',block:'start'});}
      setTimeout(function(){if(window.ALE_goStep)ALE_goStep(1);},500);});
    // triggers: CTA clicks, 50% scroll, 45s dwell, desktop exit intent, after calculator use; once per session
    var already=false;try{already=sessionStorage.getItem('ale_qm')==='1';}catch(e){}
    document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href$="#contact"],.sticky-cta .go,.calc-handoff a');if(a&&!a.closest('#contact')){e.preventDefault();openQ('cta');}},true);
    if(!already){
      var fired=false;function once(src){if(fired)return;fired=true;openQ(src);}
      setTimeout(function(){once('time');},45000);
      window.addEventListener('scroll',function(){var h=document.documentElement;if((h.scrollTop+window.innerHeight)/h.scrollHeight>0.5)once('scroll');},{passive:true});
      if(window.matchMedia('(hover:hover)').matches)document.addEventListener('mouseout',function(e){if(!e.relatedTarget&&e.clientY<=0)once('exit');});
      document.querySelectorAll('.tool-card input,.tool-card select').forEach(function(el){el.addEventListener('change',function(){setTimeout(function(){once('calculator');},8000);});});
    }
  }
  // ---- multi-step form
  if(!form)return;
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
  var cur=0;window.ALE_goStep=function(i){go(i);};
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
