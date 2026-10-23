# AL Elite Financing — website

Static site for alelitefinancing.com. 86 pages built from the SEO Page Map: homepage, trade financing pages, contractor pages, calculators, 20 city pages, blog and trust pages.

## Layout
- `public/` — the built site Vercel serves (one `index.html` per URL folder, plus `sitemap.xml` and `robots.txt`).
- `gen/` — the Python generator. Page copy lives in `consumer.py`, `contractors.py`, `cities.py`, `articles.py`, `trust.py`, `tools.py`. Shared template, CSS and the lead form are in `common.py`; page-type renderers in `render.py`. `home-index.html` is the hand-built homepage source.

## Rebuild after editing copy
```
python3 gen/build.py
rm -rf public && cp -r dist-prod public
```
`build.py` reads the homepage from `gen/home-index.html` and copies static assets (`logo.png`, `og-image.jpg`) from `gen/static/`, so a rebuild never drops them. It prints a validation report (broken links, H1 count, JSON-LD, meta length); it should end with `problems: 0`.

## Blog
New posts live in `gen/articles_new_a.py` (homeowner) and `gen/articles_new_b.py` (contractor). Each post targets a keyword distinct from its money page, links to one money page and one related post, and is automatically listed in the "Related" box of its money page. Bump `MODIFIED` in `gen/common.py` on each release (feeds schema `dateModified` and sitemap `lastmod`).

## Draft notes
Gold "verify" boxes and `[bracketed]` placeholders are stripped from the production build. Set `SHOW_DRAFT_NOTES = True` in `gen/common.py` to see them while editing. Still outstanding: named author and reviewer, contact email and hours, state licensing/lead-generator disclosures, verified local content on city pages.

## Removed pages
`/lender-network/` was removed in October 2026 and 301-redirects to `/how-we-make-money/` (see `vercel.json`).

## Before launch (marked in gold blocks on the pages)
- Replace `alelitefinancing.com` in `gen/common.py` (`DOMAIN`) if the production domain differs.
- Add phone, email, hours; real author and reviewer names.
- City pages: verified local cost ranges, state licensing rules, claim deadlines, rebates.
- Legal pages are outlines for counsel; they are `noindex`.
- Lead form: posts to FormSubmit (`https://formsubmit.co/ajax/<inbox>`), set in `gen/common.py` (`SCRIPT`) and `gen/home-index.html`. Change the inbox there and rebuild. The first submission to a new inbox triggers a one-time activation email.

## Indexing
- `.github/workflows/indexnow.yml` submits every sitemap URL to IndexNow (Bing/Yandex/Naver/Seznam) after each push that changes `public/`. The key file lives in `gen/static/` and is served at the site root.
- Google ignores IndexNow: keep the sitemap submitted in Google Search Console and use URL Inspection > Request indexing for changed money pages.

## Blog lead magnets (downloadable PDFs)
Each resource is a PDF in `gen/static/resources/` built by a script in `gen/leadmagnets/` (brand colours, fillable fields), plus a banner (`*-cover.jpg`, for social) and a mockup (`*-mockup.jpg`, used in the article block). To attach one to a post, add a `lead_magnet=dict(...)` to the article (see the hail-damage post in `gen/articles_new_a.py`). The renderer inserts two CTA blocks and a popup form (name, email, phone). Submissions go to FormSubmit (`LEAD_EMAIL` in `gen/common.py`): the team gets the lead, the reader gets an automatic thank-you email with the download link, and the page shows the download button immediately.

### Email delivery for lead magnets
`api/download.js` (Vercel function) emails the PDF as an attachment via Resend and forwards the lead. Set in Vercel → Settings → Environment Variables: `RESEND_API_KEY`, `FROM_EMAIL` (sender on a domain verified in Resend, e.g. `AL Elite Financing <hello@alelitefinancing.com>`), optional `LEAD_EMAIL`. Until these are set the endpoint returns 503 and the page falls back to FormSubmit (lead captured, auto-reply unreliable).
