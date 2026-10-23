// Emails a blog lead magnet (PDF attached) to the reader and forwards the lead to the team.
// Runs on Vercel as a Node serverless function. Requires env vars:
//   RESEND_API_KEY  - from resend.com (free tier is enough)
//   FROM_EMAIL      - a sender on a domain verified in Resend, e.g. "AL Elite Financing <hello@alelitefinancing.com>"
//   LEAD_EMAIL      - where lead notifications go (defaults to the contact-form inbox)
// The page falls back to FormSubmit if this endpoint is not configured.
const SITE = "https://www.alelitefinancing.com";
const ALLOWED = new Set([SITE, "https://alelitefinancing.com"]);

module.exports = async (req, res) => {
  const origin = req.headers.origin || "";
  if (ALLOWED.has(origin)) res.setHeader("Access-Control-Allow-Origin", origin);
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  if (req.method === "OPTIONS") return res.status(204).end();
  // Accept the canonical names and the variants that were set in Vercel.
  const env = (...names) => { for (const n of names) { const v = process.env[n]; if (v && String(v).trim()) return String(v).trim(); } return ""; };
  const key = env("RESEND_API_KEY", "resend_api", "RESEND_API", "resend_api_key");
  const from = env("FROM_EMAIL", "FromEmail", "from_email", "FROMEMAIL");
  const leadTo = env("LEAD_EMAIL", "lead_email", "LeadEmail") || "manmeetsingh0177@gmail.com";

  // Health check: GET /api/download?check=1 reports configuration without exposing secrets.
  if (req.method === "GET") {
    const url = new URL(req.url, SITE);
    if (url.searchParams.get("check") !== "1") return res.status(405).json({ ok: false, error: "POST only" });
    const out = { key_set: !!key, from_set: !!from, from_domain: from ? (from.match(/@([^>\s]+)/) || [])[1] || null : null, lead_email_set: !!env("LEAD_EMAIL", "lead_email", "LeadEmail") };
    if (key) {
      try {
        const r = await fetch("https://api.resend.com/domains", { headers: { Authorization: `Bearer ${key}` } });
        const j = await r.json();
        out.resend_status = r.status;
        out.domains = Array.isArray(j.data) ? j.data.map((d) => ({ name: d.name, status: d.status })) : (j.message || j.name || "unexpected");
      } catch (e) { out.resend_error = String(e.message || e); }
    }
    return res.status(200).json(out);
  }
  if (req.method !== "POST") return res.status(405).json({ ok: false, error: "POST only" });
  if (!key || !from) return res.status(503).json({ ok: false, error: "email not configured" });

  let body = req.body;
  if (typeof body === "string") { try { body = JSON.parse(body); } catch { body = {}; } }
  const name = String(body.name || "").trim().slice(0, 120);
  const email = String(body.email || "").trim().slice(0, 200);
  const phone = String(body.phone || "").trim().slice(0, 40);
  const resource = String(body.resource || "Worksheet").trim().slice(0, 160);
  const file = String(body.file || "").trim();
  const page = String(body.page || "").trim().slice(0, 300);
  if (body.website) return res.status(200).json({ ok: true }); // honeypot
  if (name.length < 2 || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || phone.replace(/\D/g, "").length < 7)
    return res.status(400).json({ ok: false, error: "invalid input" });
  if (!file.startsWith("/resources/") || !file.endsWith(".pdf"))
    return res.status(400).json({ ok: false, error: "invalid file" });

  const link = SITE + file;
  const first = name.split(" ")[0];
  const send = (payload) => fetch("https://api.resend.com/emails", {
    method: "POST", headers: { Authorization: `Bearer ${key}`, "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const reader = await send({
    from, to: [email], reply_to: leadTo,
    subject: `Your ${resource} from AL Elite Financing`,
    html: `<div style="font-family:Arial,sans-serif;max-width:560px;margin:auto;color:#121b2b">
<div style="background:#0b2545;padding:22px 26px;border-bottom:4px solid #b48c2c"><span style="color:#b48c2c;font-weight:700;font-size:13px;letter-spacing:.06em">AL ELITE FINANCING</span></div>
<div style="padding:26px">
<h2 style="font-family:Georgia,serif;color:#0b2545;margin:0 0 10px">Thank you for visiting AL Elite Financing, ${escapeHtml(first)}.</h2>
<p>Your copy of the <strong>${escapeHtml(resource)}</strong> is attached. It's fillable on screen (Adobe Reader, Preview or most browsers) or you can print it.</p>
<p><a href="${link}" style="display:inline-block;background:#0b2545;color:#fff;text-decoration:none;padding:12px 20px;border-radius:8px;font-weight:700">Download the PDF</a></p>
<p>When you know the gap you need to finance, one request at <a href="${SITE}/roof-financing/">${SITE.replace("https://", "")}/roof-financing/</a> reaches lenders who fund roofs in your state, or call (888) 968-0079.</p>
<p style="color:#6b7585;font-size:12px;margin-top:26px">AL Elite Financing is a matching service, not a lender. Lenders set rates and make decisions. This worksheet is general information, not legal, tax or insurance advice.</p>
</div></div>`,
    attachments: [{ path: link, filename: file.split("/").pop() }],
  });
  if (!reader.ok) {
    const t = await reader.text();
    return res.status(502).json({ ok: false, error: "send failed", detail: t.slice(0, 300) });
  }

  await send({
    from, to: [leadTo], reply_to: email,
    subject: `Worksheet download: ${resource} - ${name}`,
    text: `New lead magnet download\n\nName: ${name}\nEmail: ${email}\nPhone: ${phone}\nResource: ${resource}\nPage: ${page}\nTime: ${new Date().toISOString()}`,
  }).catch(() => {});

  return res.status(200).json({ ok: true });
};

function escapeHtml(s) { return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c])); }
