# AL Elite Financing — website

Static site for alelitefinancing.com. 79 pages built from the SEO Page Map: homepage, trade financing pages, contractor pages, calculators, 20 city pages, blog and trust pages.

## Layout
- `public/` — the built site Vercel serves (one `index.html` per URL folder, plus `sitemap.xml` and `robots.txt`).
- `gen/` — the Python generator. Page copy lives in `consumer.py`, `contractors.py`, `cities.py`, `articles.py`, `trust.py`, `tools.py`. Shared template, CSS and the lead form are in `common.py`; page-type renderers in `render.py`. `home-index.html` is the hand-built homepage source.

## Rebuild after editing copy
```
python3 gen/build.py
rm -rf public && cp -r dist-prod public
```
(`build.py` expects `index.html` one level above `gen/`; copy `gen/home-index.html` there first, or adjust `HOME_SRC`.)

## Before launch (marked in gold blocks on the pages)
- Replace `alelitefinancing.com` in `gen/common.py` (`DOMAIN`) if the production domain differs.
- Add phone, email, hours; real author and reviewer names.
- City pages: verified local cost ranges, state licensing rules, claim deadlines, rebates.
- Legal pages are outlines for counsel; they are `noindex`.
- Lead form: posts to FormSubmit (`https://formsubmit.co/ajax/<inbox>`), set in `gen/common.py` (`SCRIPT`) and `gen/home-index.html`. Change the inbox there and rebuild. The first submission to a new inbox triggers a one-time activation email.
