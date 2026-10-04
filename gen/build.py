"""Build the AL Elite site twice: prod (root-relative URLs, real folders) and artifact (relative paths)."""
import os, re, sys, json, shutil
sys.path.insert(0, os.path.dirname(__file__))
from common import *
from render import service_page, hub_page, plain_page, article_page
from consumer import CONSUMER_SERVICE_PAGES, CONSUMER_HUBS
from contractors import CONTRACTOR_SERVICE_PAGES, CONTRACTOR_HUBS
from tools import TOOL_PAGES, tool_page
from cities import CITIES, city_page, locations_hub
from articles import ARTICLES, blog_hub
from trust import TRUST_PAGES

ROOT = os.path.dirname(os.path.dirname(__file__))
HOME_SRC = open(os.path.join(ROOT, "index.html") if os.path.exists(os.path.join(ROOT, "index.html")) else os.path.join(os.path.dirname(__file__), "home-index.html")).read()

def rewrite_links(html_text, depth):
    """Artifact mode: turn root-relative hrefs into relative file paths."""
    prefix = "../" * depth
    def sub(m):
        attr, path, anchor = m.group(1), m.group(2), m.group(3) or ""
        if path == "/":
            return f'{attr}="{prefix}index.html{anchor}"'
        return f'{attr}="{prefix}{path.strip("/")}/index.html{anchor}"'
    return re.sub(r'(href)="(/[^"#:]*)(#[^"]*)?"', sub, html_text)

def build(mode, outdir):
    b = Build(mode)
    if os.path.exists(outdir): shutil.rmtree(outdir)
    os.makedirs(outdir)
    pages = {}
    # Homepage: use the hand-built index.html; in artifact mode strip to body-only and rewrite links.
    pages["/"] = HOME_SRC
    for p in CONSUMER_SERVICE_PAGES + CONTRACTOR_SERVICE_PAGES: pages[p["path"]] = service_page(b, p)
    for p in CONSUMER_HUBS + CONTRACTOR_HUBS: pages[p["path"]] = hub_page(b, p)
    for p in TOOL_PAGES: pages[p["path"]] = tool_page(b, p)
    for c in CITIES: pages[c[3]] = city_page(b, c)
    pages["/locations/"] = locations_hub(b)
    for a in ARTICLES: pages[a["path"]] = article_page(b, a)
    pages["/blog/"] = blog_hub(b)
    for p in TRUST_PAGES: pages[p["path"]] = plain_page(b, p)
    # tools hub alias: /tools/ -> redirect-ish page listing both calculators
    pages["/tools/"] = plain_page(b, dict(path="/tools/", crumbs=[("Home", "/"), ("Tools", "/tools/")], eyebrow="Tools", h1="Financing calculators", title="Financing Calculators | Roof & Equipment Loan Calculators | AL Elite", meta="Free calculators: roof financing payment calculator for homeowners and equipment loan calculator for contractors. Illustrative only.", answer="Two free calculators: the roof financing calculator turns a roof quote into a monthly payment, and the equipment loan calculator does the same for excavators, trucks and tools. Both show total interest and a full amortization schedule. Arithmetic only; lenders set real rates.", prose="<div class='grid-cards'><a class='card' href='/tools/roof-financing-calculator/'><span class='tag'>Homeowners</span><h3>Roof financing calculator</h3><p>Monthly payment, total interest and schedule for a roof loan.</p></a><a class='card' href='/tools/equipment-loan-calculator/'><span class='tag'>Contractors</span><h3>Equipment loan calculator</h3><p>Payments on equipment and trucks after a down payment.</p></a></div>", related=[("Roof financing", "/roof-financing/"), ("Construction equipment financing", "/contractor-business-loans/equipment-financing/")], byline=False))

    for path, html_text in pages.items():
        d = depth_of(path)
        if mode == "artifact":
            html_text = rewrite_links(html_text, d)
            if path == "/":
                # body-only for the artifact page itself
                head = re.search(r"<head>(.*?)</head>", html_text, re.S).group(1)
                title = re.search(r"<title>.*?</title>", head).group(0)
                fonts = re.search(r'<link rel="stylesheet"[^>]*>', head).group(0)
                style = re.search(r"<style>.*?</style>", head, re.S).group(0)
                body = re.search(r"<body>(.*?)</body>", html_text, re.S).group(1)
                html_text = title + "\n" + fonts + "\n" + style + "\n" + body
        fp = os.path.join(outdir, out_path(path))
        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w").write(html_text)
    # sitemap + robots for prod
    if mode == "prod":
        urls = "".join(f"<url><loc>{DOMAIN}{p}</loc><lastmod>2026-10-04</lastmod></url>" for p in pages if p not in ("/privacy/", "/terms/", "/accessibility/", "/do-not-sell/"))
        open(os.path.join(outdir, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
        open(os.path.join(outdir, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    return pages

if __name__ == "__main__":
    prod = build("prod", os.path.join(ROOT, "dist-prod"))
    art = build("artifact", os.path.join(ROOT, "dist-artifact"))
    print(len(prod), "pages")
    # ---- validation
    banned = ["guaranteed approval", "delve", "tapestry", "vibrant", "crucial", "comprehensive", "robust", "seamless", "groundbreaking", "leverage", "synergy", "transformative", "paramount", "reimagine", "empower", "supercharge", "game-changing", "revolutioni", "unlock"]
    problems = []
    for path, h in prod.items():
        for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try: json.loads(m.group(1))
            except Exception as e: problems.append((path, "bad json-ld", str(e)))
        low = h.lower()
        for w in banned:
            # allow the phrase inside "no 'guaranteed approval'" style warnings only when preceded by quote/negation context
            for mm in re.finditer(re.escape(w), low):
                ctx = low[max(0, mm.start()-60):mm.end()+30]
                if w == "guaranteed approval" and any(k in ctx for k in ["never", "no '", "no \"", "not", "avoid", "won't", "don't", "promis", "claims", "language", "or '", "prohibit", "offers advertising"]):
                    continue
                problems.append((path, "banned word", w, ctx.strip()))
        for m in re.finditer(r'href="(/[^"#]*)', h):
            t = m.group(1)
            if t not in prod: problems.append((path, "broken link", t))
        if h.count("<h1") != 1: problems.append((path, "h1 count", h.count("<h1")))
        if len(re.search(r'<meta name="description" content="([^"]*)"', h).group(1)) > 175: problems.append((path, "meta too long"))
    for p in problems: print(p)
    print("problems:", len(problems))
