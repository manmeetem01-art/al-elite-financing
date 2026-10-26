"""Attach lead magnets to blog posts (built by gen/leadmagnets/build_all.py)."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "leadmagnets"))
from resources_a import RESOURCES as RA
from resources_b import RESOURCES as RB
from resources_c import RESOURCES as RC

def apply(pages_by_path):
    for r in RA + RB + RC:
        p = pages_by_path.get(r["blog"])
        if not p or p.get("lead_magnet"):
            continue
        p["lead_magnet"] = dict(audience="contractor" if r in RB else "homeowner", slug=r["slug"], title=r["spec"]["title"], pages=r["pages"], headline=r["headline"], pitch=r["pitch"], bullets=r["bullets"],
                                file=f"/resources/{r['slug']}.pdf", cover=f"/resources/{r['slug']}-cover.jpg", mockup=f"/resources/{r['slug']}-mockup.jpg")
