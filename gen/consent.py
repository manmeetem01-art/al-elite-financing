"""Consent / 'Do Not Sell or Share' modal (Oct 30, 2026). Shows once on first visit (consent banners are
exempt from Google's interstitial guidance), stores the choice in localStorage for 12 months, honours Global
Privacy Control, gates GA4 behind consent via Consent Mode, and can be reopened from the footer link."""

CONSENT_CSS = """
.cm{position:fixed;inset:0;background:rgba(7,26,51,.55);display:none;align-items:center;justify-content:center;z-index:100001;padding:16px}.cm.open{display:flex}
.cm .cm-box{background:#fff;border-radius:14px;max-width:640px;width:100%;box-shadow:0 24px 60px rgba(0,0,0,.3);max-height:92vh;overflow:auto;position:relative}
.cm .cm-head{display:flex;align-items:center;justify-content:space-between;padding:16px 20px;border-bottom:1px solid var(--line)}
.cm .cm-head img{height:44px;width:auto}
.cm .cm-close{background:none;border:1.5px solid var(--line);border-radius:8px;width:40px;height:40px;font-size:24px;line-height:1;cursor:pointer;color:var(--navy)}
.cm .cm-body{padding:20px 24px}
.cm h2{font-family:var(--serif,Georgia,serif);color:var(--navy);font-size:1.35rem;margin:0 0 10px}
.cm p{color:#3c4756;font-size:.95rem;line-height:1.55;margin:0 0 14px}
.cm h3{font-size:1.05rem;color:var(--navy);margin:18px 0 10px}
.cm .cm-row{border:1px solid var(--line);border-radius:10px;padding:12px 14px;display:flex;align-items:center;justify-content:space-between;gap:12px;margin-bottom:8px}
.cm .cm-row strong{color:var(--navy);display:block}.cm .cm-row small{color:var(--muted);display:block;font-size:.82rem;margin-top:2px}
.cm .always{color:var(--navy);font-weight:700;font-size:.9rem;white-space:nowrap}
.cm .sw{position:relative;display:inline-flex;align-items:center;gap:8px;font-size:.9rem;color:var(--navy);white-space:nowrap}
.cm .sw input{appearance:none;width:46px;height:26px;border-radius:13px;background:#c9d3e3;position:relative;cursor:pointer;transition:background .15s;margin:0}
.cm .sw input::after{content:"";position:absolute;top:3px;left:3px;width:20px;height:20px;border-radius:50%;background:#fff;transition:left .15s;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.cm .sw input:checked{background:var(--gold)}.cm .sw input:checked::after{left:23px}
.cm .cm-foot{display:flex;gap:10px;justify-content:flex-end;padding:14px 24px 18px;border-top:1px solid var(--line);flex-wrap:wrap}
.cm .btn-c{border:0;border-radius:8px;padding:12px 18px;font:inherit;font-weight:700;cursor:pointer}
.cm .btn-confirm{background:var(--gold);color:#071a33}.cm .btn-all{background:var(--navy);color:#fff}.cm .btn-reject{background:none;border:1.5px solid var(--line);color:var(--navy)}
.cm .cm-links{font-size:.82rem;color:var(--muted);padding:0 24px 16px}
@media (max-width:640px){.cm{align-items:flex-end;padding:0}.cm .cm-box{border-radius:14px 14px 0 0;max-height:85vh}.cm .cm-foot{justify-content:stretch}.cm .btn-c{flex:1}}
"""

CONSENT_JS = r"""
(function(){
  var KEY='ale_consent_v1';var saved=null;try{saved=JSON.parse(localStorage.getItem(KEY)||'null');}catch(e){}
  var gpc=!!navigator.globalPrivacyControl;
  function apply(c){try{if(window.gtag){gtag('consent','update',{analytics_storage:c.analytics?'granted':'denied',ad_storage:c.share?'granted':'denied',ad_user_data:c.share?'granted':'denied',ad_personalization:c.share?'granted':'denied'});}}catch(e){}}
  function save(c){c.ts=Date.now();c.gpc=gpc;try{localStorage.setItem(KEY,JSON.stringify(c));}catch(e){}apply(c);if(window.ALE&&ALE.track)ALE.track('consent_update',{analytics:c.analytics?1:0,share:c.share?1:0});}
  if(saved&&Date.now()-(saved.ts||0)<365*864e5)apply(saved);
  var cm=document.createElement('div');cm.className='cm';cm.id='consentModal';cm.setAttribute('role','dialog');cm.setAttribute('aria-modal','true');cm.setAttribute('aria-labelledby','cm-h');
  cm.innerHTML='<div class="cm-box"><div class="cm-head"><img src="/logo.png" alt="AL Elite Financing" width="60" height="44"><button type="button" class="cm-close" aria-label="Close">&times;</button></div>'
   +'<div class="cm-body"><h2 id="cm-h">Your privacy choices</h2>'
   +'<p>When you use this site we store or read small amounts of information in your browser, mostly cookies. Strictly necessary cookies keep the site and forms working. Analytics cookies help us understand which pages and tools are useful. If you submit a request, we share the details you give us with lenders who pay us for introductions, which some state laws treat as a &ldquo;sale&rdquo; or &ldquo;sharing&rdquo; of personal information. You can opt out below; it will not affect requests you choose to submit.'+(gpc?' <strong>We detected a Global Privacy Control signal from your browser, so sharing is set to off.</strong>':'')+'</p>'
   +'<h3>Manage consent preferences</h3>'
   +'<div class="cm-row"><div><strong>Strictly necessary</strong><small>Site security, forms, your saved choices here.</small></div><span class="always">Always active</span></div>'
   +'<div class="cm-row"><div><strong>Analytics</strong><small>Google Analytics, anonymised IP, no ads.</small></div><label class="sw"><span id="cm-a-l">Active</span><input type="checkbox" id="cm-analytics" checked aria-label="Analytics cookies"></label></div>'
   +'<div class="cm-row"><div><strong>Share or sale of personal data</strong><small>Sharing your submitted details with lender and partner programs that compensate us.</small></div><label class="sw"><span id="cm-s-l">Active</span><input type="checkbox" id="cm-share" checked aria-label="Share or sale of personal data"></label></div>'
   +'</div><div class="cm-foot"><button type="button" class="btn-c btn-reject" id="cm-reject">Reject non-essential</button><button type="button" class="btn-c btn-confirm" id="cm-confirm">Confirm my choices</button><button type="button" class="btn-c btn-all" id="cm-all">Accept all</button></div>'
   +'<p class="cm-links"><a href="/privacy/">Privacy policy</a> &middot; <a href="/do-not-sell/">Do not sell or share my information</a> &middot; <a href="/terms/">Terms</a></p></div>';
  document.body.appendChild(cm);
  var A=cm.querySelector('#cm-analytics'),S=cm.querySelector('#cm-share');
  function labels(){cm.querySelector('#cm-a-l').textContent=A.checked?'Active':'Off';cm.querySelector('#cm-s-l').textContent=S.checked?'Active':'Off';}
  A.addEventListener('change',labels);S.addEventListener('change',labels);
  function open(){if(saved){A.checked=!!saved.analytics;S.checked=!!saved.share;}else if(gpc){S.checked=false;}labels();cm.classList.add('open');document.body.style.overflow='hidden';}
  function close(){cm.classList.remove('open');document.body.style.overflow='';}
  cm.querySelector('.cm-close').addEventListener('click',function(){if(!saved){saved={analytics:true,share:!gpc};save(saved);}close();});
  cm.querySelector('#cm-confirm').addEventListener('click',function(){saved={analytics:A.checked,share:S.checked};save(saved);close();});
  cm.querySelector('#cm-all').addEventListener('click',function(){saved={analytics:true,share:true};save(saved);close();});
  cm.querySelector('#cm-reject').addEventListener('click',function(){saved={analytics:false,share:false};save(saved);close();});
  document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('a[href="#privacy-choices"]');if(a){e.preventDefault();open();}},true);
  if(!saved||Date.now()-(saved.ts||0)>=365*864e5){setTimeout(open,1200);}
})();
"""
