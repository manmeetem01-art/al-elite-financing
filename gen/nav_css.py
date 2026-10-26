DD_CSS = """
nav.primary li.has-dd{position:relative}
nav.primary .dd{display:none;position:absolute;top:100%;left:50%;transform:translateX(-50%);background:#fff;border:1px solid var(--line);border-radius:12px;box-shadow:0 18px 40px rgba(11,37,69,.14);padding:14px 10px;z-index:50;gap:18px;margin-top:8px;text-align:left}
nav.primary li.has-dd:hover .dd,nav.primary li.has-dd:focus-within .dd{display:flex}
nav.primary li.has-dd::after{content:"";position:absolute;left:0;right:0;top:100%;height:12px}
nav.primary .dd-col{min-width:240px}
nav.primary .dd ul{display:block;padding:0;margin:0}
nav.primary .dd li{list-style:none;margin:0}
nav.primary .dd .dd-h{font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--gold);padding:4px 10px 6px;margin:0}
nav.primary .dd a{display:block;padding:7px 10px;border-radius:8px;font-size:.92rem;color:var(--ink);white-space:nowrap}
nav.primary .dd a:hover{background:var(--surface);color:var(--navy)}
nav.primary .dd .dd-all{border-top:1px solid var(--line);margin:8px 0 0;padding-top:6px}
nav.primary .dd .dd-all a{font-weight:600;color:var(--navy)}
@media (max-width:900px){nav.primary .dd{display:block;position:static;transform:none;box-shadow:none;border:0;padding:0 0 0 14px;margin:0}nav.primary .dd-col{min-width:0}nav.primary .dd a{padding:6px 4px;font-size:.98rem;white-space:normal}nav.primary li.has-dd::after{display:none}}
footer .cols{grid-template-columns:1.4fr repeat(4,1fr)}
@media (max-width:900px){footer .cols{grid-template-columns:1fr 1fr}}
"""
