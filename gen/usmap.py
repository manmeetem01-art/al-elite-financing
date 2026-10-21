"""'Where we work' band with a Google Maps view of the US, injected above the footer on every page."""
from cities import CITIES

MAP_SRC = "https://maps.google.com/maps?q=United+States&t=m&z=4&ie=UTF8&iwloc=&output=embed"

US_MAP_CSS = """
.usmap{background:var(--surface);border-top:1px solid var(--line);padding-block:64px}
.usmap .wrap{display:grid;grid-template-columns:minmax(0,5fr) minmax(0,7fr);gap:48px;align-items:stretch}
.usmap h2{margin:.35em 0 .4em}
.usmap p.lede{color:var(--muted);max-width:46ch;margin:0 0 22px}
.usmap ul{list-style:none;margin:0 0 22px;padding:0;display:flex;flex-wrap:wrap;gap:8px}
.usmap li a{display:inline-block;padding:6px 12px;border:1px solid var(--line);border-radius:999px;background:#fff;color:var(--navy);font-size:.86rem;text-decoration:none;line-height:1.3}
.usmap li a:hover,.usmap li a:focus-visible{border-color:var(--gold);color:var(--navy-deep)}
.usmap .more{font-weight:600;color:var(--navy)}
.usmap .frame{position:relative;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:#e9edf3;min-height:440px;box-shadow:0 10px 30px rgba(11,37,69,.08)}
.usmap iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
@media (max-width:900px){.usmap .wrap{grid-template-columns:1fr;gap:28px}.usmap .frame{min-height:0;aspect-ratio:4/3}}
"""

def us_map_section():
    chips = "".join(f'<li><a href="{c[3]}">{c[0]}, {c[2]}</a></li>' for c in CITIES)
    return f"""<section class="usmap" aria-labelledby="usmap-h">
<div class="wrap">
<div>
<p class="eyebrow">Where we work</p>
<h2 id="usmap-h">Financing across the United States</h2>
<p class="lede">We match homeowners and contractors with lenders nationwide, with local guides for the storm-prone metros where a roof or AC becomes urgent. Lender availability varies by state.</p>
<ul>{chips}</ul>
<a class="more" href="/locations/">See all locations</a>
</div>
<div class="frame">
<iframe src="{MAP_SRC}" title="Map of the United States, where AL Elite Financing matches borrowers with lenders" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
</div>
</div>
</section>
"""
