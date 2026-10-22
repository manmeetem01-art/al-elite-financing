"""'Where we work' band with a Google Maps view of the US, injected above the footer on every page."""
from cities import CITIES

# Official Google Maps embed format (the "Share > Embed a map" URL). The older
# maps.google.com/maps?...&output=embed URL redirects to mobile Maps on phones, which refuses to be
# framed, so it showed blank on mobile. Centre: geographic centre of the contiguous US; 1d = view span (m).
MAP_SRC = ("https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d6000000!2d-98.5795!3d39.8283"
           "!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sus!4v1761100000000!5m2!1sen!2sus")
MAP_LINK = "https://www.google.com/maps/place/United+States/@39.8283,-98.5795,4z"

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
.usmap .mapcol{display:flex;flex-direction:column}
.usmap .mapcol .frame{flex:1}
.usmap .maplink{margin:10px 0 0;font-size:.86rem;text-align:right}
.usmap .maplink a{color:var(--navy)}
@media (max-width:900px){.usmap .wrap{grid-template-columns:1fr;gap:24px}.usmap .mapcol{order:-1}.usmap .frame{min-height:0;aspect-ratio:4/3}.usmap{padding-block:48px}}
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
<div class="mapcol">
<div class="frame">
<iframe src="{MAP_SRC}" title="Map of the United States, where AL Elite Financing matches borrowers with lenders" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
</div>
<p class="maplink"><a href="{MAP_LINK}" target="_blank" rel="noopener">Open in Google Maps</a></p>
</div>
</div>
</section>
"""
