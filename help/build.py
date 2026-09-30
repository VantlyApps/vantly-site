#!/usr/bin/env python3
"""Builds the Vantly help center (help/*.html) from the articles below.

Edit an article here, then run:  python3 help/build.py
Each article is served at vantlyapps.com/help/<slug>; the app links to them.
"""
import html
from pathlib import Path

HERE = Path(__file__).parent

ARTICLES = [
    {
        "slug": "getting-started",
        "title": "Getting started",
        "summary": "Install Vantly, add the return portal to your store, and run a test return.",
        "body": """
<p>Vantly Returns adds a self-serve return portal to your store and handles each return from request to refund, store credit, or exchange. Setup takes about 15 minutes.</p>
<h2>1. Install and open the app</h2>
<p>After you install Vantly Returns, open it from <strong>Apps</strong> in your Shopify admin. The <strong>Returns</strong> page shows a short setup checklist until you finish it.</p>
<h2>2. Review your default settings</h2>
<p>Go to <strong>Settings</strong>. These are your default terms for every product: the return window, which options customers get (refund, store credit, exchange), fees, and return reasons. Products that need different terms get their own <a href="/help/rules">rules</a> later.</p>
<h2>3. Add the return portal to your store</h2>
<p>Your portal already works at <code>yourstore.com/apps/returns</code>. To link to it from your theme:</p>
<ol>
<li>In Shopify, go to <strong>Online Store › Themes › Customize</strong>.</li>
<li>Open the page where the link should go (for example a Returns page or the footer), click <strong>Add block</strong>, and choose <strong>Start a return</strong>.</li>
<li>Click <strong>Save</strong>.</li>
</ol>
<p>You can also add the portal link to your navigation menu or your order emails.</p>
<h2>4. Make a test return</h2>
<p>Place a test order, mark it fulfilled, then open your portal and start a return with the order number and email. The return appears in Vantly under <strong>Returns</strong>, where you can approve it and try the rest of the flow.</p>
<h2>Next steps</h2>
<ul>
<li><a href="/help/return-portal">Brand your return portal</a></li>
<li><a href="/help/exchanges">Offer exchanges before refunds</a></li>
<li><a href="/help/labels">Connect return labels</a></li>
</ul>
""",
    },
    {
        "slug": "return-portal",
        "title": "The return portal",
        "summary": "Templates, colors, logo, text, and your return policy.",
        "body": """
<p>The return portal is where customers start a return: they find their order, choose items and reasons, then pick how they'd like to be paid back.</p>
<h2>Choose a template</h2>
<p>Go to <strong>Return portal</strong> in Vantly. Pick a template:</p>
<ul>
<li><strong>Stella</strong>: one focused column that works well everywhere.</li>
<li><strong>Terra</strong>: a wide layout with a large photo gallery and a summary beside it.</li>
</ul>
<p>The order lookup page and progress bar look the same in both.</p>
<h2>Match your brand</h2>
<p>Upload your logo and set your colors, corner style, and font. Every piece of text in the portal can be changed, including headings, buttons, and the confirmation messages. The preview updates as you type, and <strong>Open return portal</strong> lets you walk through it like a customer.</p>
<h2>Show your return policy</h2>
<p>Paste your policy into <strong>Return policy</strong> and it appears on the first page of the portal.</p>
<h2>Where customers find it</h2>
<p>The portal lives at <code>yourstore.com/apps/returns</code>. Add the <strong>Start a return</strong> block to your theme (see <a href="/help/getting-started">Getting started</a>) or link it from your menu.</p>
""",
    },
    {
        "slug": "rules",
        "title": "Return rules",
        "summary": "Give products their own window, options, fees, and return reasons.",
        "body": """
<p>Your <strong>default settings</strong> cover every product. <strong>Rules</strong> change the terms for the products they match, like a longer window for machines or final sale for clearance items.</p>
<h2>How rules are checked</h2>
<p>Rules are checked from the top of the list, and each item follows the <strong>first rule that matches it</strong>. Anything no rule matches uses your default settings, which are always the last row. Use the arrows to change the order, and put narrow rules (like final sale) above broad ones.</p>
<h2>Create a rule</h2>
<p>Go to <strong>Rules › Create rule</strong>.</p>
<ul>
<li><strong>Applies to</strong>: product tag, type, vendor, collection, SKU, price, order details, the customer (tags, past returns), or the return itself (reason, chosen option). Match any or all of them.</li>
<li><strong>Returns</strong>: returnable or final sale, and the return window.</li>
<li><strong>Return options</strong>: which of refund, store credit, exchange, and replacement customers can choose.</li>
<li><strong>Fees and bonus</strong>: restocking fee, return shipping fee, and bonus credit. Leave a field blank to use your default.</li>
<li><strong>When opened</strong>: different terms for opened items, like store credit or exchange only. The portal then asks customers whether each item was opened.</li>
<li><strong>Return reasons</strong>: a reason list just for these products (for example, masks: Air leaks, Uncomfortable, Doesn't fit). End a reason with <code>*</code> to require a photo.</li>
<li><strong>Extras</strong>: require a photo, approve automatically, let the customer keep the item (always, or only the first time), show a message, waive fees, ask the customer to agree to a statement, or send items to another return address.</li>
<li><strong>Review and order</strong>: flag returns for review, use the rule only once per customer, or let rules below also apply.</li>
</ul>
<h2>Test before going live</h2>
<p><strong>Test on an order</strong> shows exactly which rules apply to a real order and why.</p>
""",
    },
    {
        "slug": "exchanges",
        "title": "Exchanges and store credit",
        "summary": "Keep more sales with exchanges, similar products, and bonus credit.",
        "body": """
<p>Every exchange or store credit is a sale you keep. Vantly helps customers choose them over a refund, without making refunds hard to find.</p>
<h2>What customers can exchange for</h2>
<p>When a customer chooses an exchange, they see <strong>other sizes and colors</strong> of the same product first, then <strong>similar products</strong>. In <strong>Settings › Exchanges</strong>, choose where similar products come from: the same product type, collection, vendor, or tag.</p>
<h2>Encourage exchanges and store credit</h2>
<p>In <strong>Settings › Return options</strong>, choose how the portal presents the options:</p>
<ul>
<li><strong>Gently</strong> (recommended): exchange and credit first, with a short perk line; refunds show their timing.</li>
<li><strong>Exchange first</strong>: the exchange up front, with other options one tap away.</li>
<li><strong>Neutral</strong>: every option shown the same way.</li>
</ul>
<p>You can also add a <strong>bonus</strong> (for example 10% extra) to store credit or exchanges.</p>
<h2>Price differences</h2>
<p>Choose how exchanges are priced:</p>
<ul>
<li><strong>Free swap</strong>: exchanges are always free. Only items that cost the same or less are offered.</li>
<li><strong>Customer pays the difference</strong>: the customer keeps their original discount. If the new item costs more, they get a Shopify invoice for the difference, and the exchange ships once it's paid. The return page shows whether it's paid, and you can resend the invoice or copy the payment link. Vantly sends one reminder after 2 days.</li>
</ul>
<p>If the new item costs less, choose whether the rest becomes store credit, a refund, or nothing.</p>
""",
    },
    {
        "slug": "reviewing-returns",
        "title": "Reviewing returns",
        "summary": "Approve, reject single items, adjust values, and complete returns.",
        "body": """
<p>New returns appear on the <strong>Returns</strong> page. Open one to review it.</p>
<h2>Approve or reject</h2>
<p><strong>Approve return</strong> accepts it in Shopify and emails the customer the next steps. <strong>Reject</strong> closes it and tells the customer why.</p>
<p>To accept only some items, switch those items to <strong>Reject</strong> in the Items list and give a reason. The button then reads, for example, <strong>Approve 1 of 2 items</strong>.</p>
<h2>Adjust an item's value</h2>
<p>Click the pencil next to an item's price to deduct or add an amount (for example, a missing part or a goodwill credit). The reason is saved in the return's history; the customer doesn't see it.</p>
<h2>Receive and complete</h2>
<p>When the package arrives, mark it <strong>received</strong>, choose whether to restock each item, then complete the return to issue the refund, store credit, or exchange order.</p>
<h2>Green returns</h2>
<p>When a rule lets the customer keep the item, there's nothing to ship back. The customer gets a "You can keep it" email and the return goes straight to payout.</p>
<h2>Bundles</h2>
<p>Bundles sold as one product can be returned by their individual items. Set them up in <strong>Settings › Bundles</strong>.</p>
""",
    },
    {
        "slug": "labels",
        "title": "Return labels",
        "summary": "Buy return labels with ShipStation or EasyPost, automatically or by hand.",
        "body": """
<p>Vantly can buy return labels with your own carrier accounts and rates, then email them to the customer.</p>
<h2>Connect an account</h2>
<p>Go to <strong>Integrations</strong> and open <strong>ShipStation</strong> or <strong>EasyPost</strong>. Paste your API key. Vantly lists the carriers connected to that account.</p>
<h2>Label rules</h2>
<ul>
<li><strong>When buying a label, choose</strong>: cheapest, fastest, or best value.</li>
<li><strong>Maximum label price</strong>: never pay more than this.</li>
<li><strong>Only use some carriers and services</strong>: tick the carriers or single services you want.</li>
<li><strong>Buy a label automatically when a return is approved</strong>.</li>
<li><strong>Package size and weight</strong>: used for rates when products don't have their own.</li>
</ul>
<h2>Buy or add a label by hand</h2>
<p>On a return, you can compare rates and buy a label, or add a label you already have (tracking number and link). Unused labels can be voided for a refund from the carrier.</p>
""",
    },
    {
        "slug": "package-protection",
        "title": "Package protection",
        "summary": "Offer protection in the cart and keep 100% of the fee.",
        "body": """
<p>Package protection lets customers add coverage for lost, stolen, or damaged orders. You set the price, you keep the whole fee, and you handle claims your way.</p>
<h2>Turn it on</h2>
<ol>
<li>In Vantly, go to <strong>Protection</strong>, turn on <strong>Offer package protection</strong>, set your pricing, and click <strong>Save</strong>. Vantly creates a hidden Package Protection product with a price for each step.</li>
<li>In Shopify, go to <strong>Online Store › Themes › Customize › App embeds</strong>, turn on <strong>Package protection</strong>, and save.</li>
</ol>
<h2>Pricing</h2>
<p>Protection is a percentage of the cart, kept between a minimum and maximum and rounded to your price steps (for example $0.50).</p>
<h2>The widget</h2>
<p>Choose a <strong>toggle card</strong> or a <strong>Checkout+ button</strong> with a "checkout without" link. Change the text, color, and icon, and fill the info popup with your own features and links. The preview shows it on a sample cart, on desktop and on a phone.</p>
<h2>In checkout (Shopify Plus)</h2>
<p>Stores on Shopify Plus can also show the switch in checkout: go to <strong>Settings › Checkout › Customize</strong>, click <strong>Add app block</strong>, and choose Vantly's protection block.</p>
""",
    },
    {
        "slug": "emails",
        "title": "Emails",
        "summary": "Customize every customer email and send from your own domain.",
        "body": """
<p>Vantly emails your customer at each step: request received, approved, label, reminder, received, refund or credit, exchange sent, declined, and "You can keep it" for green returns.</p>
<h2>Change the text and design</h2>
<p>Go to <strong>Emails</strong>. Turn each email on or off, and open one to edit its subject and text. <strong>Design</strong> sets your logo, colors, button style, and footer for all of them. Previews show desktop and phone.</p>
<h2>Send from your own domain</h2>
<p>In <strong>Emails › Sender and domain</strong>, add your domain (for example <code>returns@yourstore.com</code>). Vantly shows the DNS records to add at your domain provider and checks them for you, including DMARC.</p>
<h2>Use Klaviyo instead</h2>
<p>If you connect <a href="/help/integrations">Klaviyo</a>, you can let your Klaviyo flows send these emails. Vantly then sends the events and stays quiet.</p>
""",
    },
    {
        "slug": "integrations",
        "title": "Integrations",
        "summary": "ShipStation, EasyPost, Katana, and Klaviyo.",
        "body": """
<p>Go to <strong>Integrations</strong> to connect the tools you already use. Each one has its own page, and keys are stored encrypted.</p>
<h2>ShipStation and EasyPost</h2>
<p>Buy return labels with your carrier accounts. See <a href="/help/labels">Return labels</a>.</p>
<h2>Katana</h2>
<p>If Katana manages your stock, Vantly restocks returned items in Katana (matched by SKU) so its numbers stay right. Choose the Katana location, and whether to restock in Katana only, Shopify only, or both. If Katana syncs stock to Shopify, choose Katana only.</p>
<h2>Klaviyo</h2>
<p>Paste a Klaviyo private API key with Accounts: Read, Events: Write, and Profiles: Write. Vantly sends an event for each return moment (for example <em>Vantly Return Requested</em> or <em>Vantly Return Refunded</em>) with the order, items, reasons, amount, and tracking. Build flows and segments on them. Add the flow filter <strong>NotifyCustomer is true</strong> so staff choices not to email the customer are respected.</p>
""",
    },
    {
        "slug": "plans-and-billing",
        "title": "Plans and billing",
        "summary": "Plans, return limits, trials, and changing plans.",
        "body": """
<p>Every plan includes every feature and unlimited staff. Plans differ only by returns per month.</p>
<table class="table">
<tr><th>Plan</th><th>Price</th><th>Returns a month</th></tr>
<tr><td>Free</td><td>$0</td><td>20</td></tr>
<tr><td>Starter</td><td>$29/month or $290/year</td><td>150</td></tr>
<tr><td>Growth</td><td>$79/month or $790/year</td><td>500</td></tr>
<tr><td>Pro</td><td>$199/month or $1,990/year</td><td>Unlimited</td></tr>
</table>
<p>Paid plans start with a 14-day free trial. Billing goes through your Shopify invoice. You always keep 100% of package protection fees.</p>
<h2>If you go over</h2>
<p>Returns never stop. You'll see a notice in the app and a suggested plan that fits.</p>
<h2>Change your plan</h2>
<p>Go to <strong>Settings › Plan and billing</strong> and click <strong>Change plan</strong>.</p>
""",
    },
]

FAQ = [
    ("Does it create real Shopify returns?", "Yes. Each return is created in Shopify, so refunds, restocking, and reports stay in your Shopify admin."),
    ("Do customers need an account?", "No. They find their order with the order number and email."),
    ("Does it work with my theme?", "Yes. The portal and the protection widget are built to fit any theme. The widget's colors and text are yours."),
    ("What happens if I go over my plan's returns?", "Nothing stops. You'll see a notice with the plan that fits."),
    ("Who keeps the package protection fee?", "You do, all of it. Vantly doesn't take a share."),
    ("What happens to my data if I uninstall?", "All of your store's data is deleted after Shopify's deletion request. See the privacy policy."),
]

CSS = """
:root { --bg:#FFFFFF; --soft:#FAFAFA; --line:#E5E5E7; --ink:#111113; --muted:#62626B; --teal:#0F6E56; --mint:#5DCAA5; color-scheme: light; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#0B0B0C; --soft:#141416; --line:#2A2A2E; --ink:#F4F4F5; --muted:#A1A1AA; --teal:#3CC39A; color-scheme: dark; } }
:root[data-theme="dark"] { --bg:#0B0B0C; --soft:#141416; --line:#2A2A2E; --ink:#F4F4F5; --muted:#A1A1AA; --teal:#3CC39A; color-scheme: dark; }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--ink); font:16px/1.65 "Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif; -webkit-font-smoothing:antialiased; }
a { color:var(--teal); }
.wrap { max-width:960px; margin:0 auto; padding:0 16px; }
.nav { border-bottom:1px solid var(--line); }
.nav .wrap { display:flex; align-items:center; gap:18px; min-height:64px; }
.brand { display:flex; align-items:center; gap:10px; text-decoration:none; color:var(--ink); font:700 22px "Inter Tight","Inter",sans-serif; letter-spacing:-0.03em; }
.brand svg { width:28px; height:28px; }
.nav .crumb { color:var(--muted); text-decoration:none; font-weight:600; }
main { padding:44px 0 72px; }
h1 { font:700 clamp(2rem,5vw,2.8rem)/1.08 "Inter Tight","Inter",sans-serif; letter-spacing:-0.03em; margin:0 0 10px; }
h2 { font:700 1.2rem/1.3 "Inter Tight","Inter",sans-serif; letter-spacing:-0.015em; margin:34px 0 8px; }
.lede { color:var(--muted); font-size:1.1rem; margin:0 0 30px; max-width:40em; }
.grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:12px; }
.card { display:grid; gap:6px; padding:18px; border:1px solid var(--line); border-radius:14px; text-decoration:none; color:var(--ink); background:var(--bg); transition:border-color .2s, transform .2s, box-shadow .2s; }
.card:hover { border-color:color-mix(in srgb, var(--teal) 45%, var(--line)); transform:translateY(-2px); box-shadow:0 12px 28px -20px rgba(0,0,0,.35); }
.card strong { font-size:1.02rem; }
.card span { color:var(--muted); font-size:.94rem; line-height:1.45; }
.article { max-width:720px; }
.article li { margin:6px 0; }
code { background:var(--soft); border:1px solid var(--line); border-radius:6px; padding:1px 6px; font-size:.9em; }
.table { width:100%; border:1px solid var(--line); border-radius:12px; border-collapse:separate; border-spacing:0; overflow:hidden; margin:12px 0; }
.table th, .table td { text-align:left; padding:10px 14px; border-bottom:1px solid var(--line); font-size:15px; }
.table th { background:var(--soft); }
.table tr:last-child td { border-bottom:0; }
details { border:1px solid var(--line); border-radius:12px; padding:14px 16px; margin:8px 0; }
summary { cursor:pointer; font-weight:600; }
details p { margin:10px 0 0; color:var(--muted); }
.more { margin-top:44px; padding-top:22px; border-top:1px solid var(--line); color:var(--muted); }
footer { border-top:1px solid var(--line); padding:28px 0 40px; color:var(--muted); font-size:14px; }
"""

MARK = '<svg viewBox="12 9 40 48" aria-hidden="true"><g transform="translate(1.5 6)"><path d="M16 20 L30 46 L41 25 C45 17 42 11 35 11 L31 11" fill="none" stroke="#0F6E56" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M25 11 L32 6 L32 16 Z" fill="#5DCAA5" stroke="#5DCAA5" stroke-width="2" stroke-linejoin="round"/></g></svg>'
CONTACT = "support@vantlyapps.com"


def page(title: str, description: str, body: str, crumb: bool) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} · Vantly Returns Help</title>
<meta name="description" content="{html.escape(description)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@600;700&family=Inter:wght@400;500;600&display=swap">
<style>{CSS}</style>
</head>
<body>
<nav class="nav" aria-label="Main"><div class="wrap">
  <a class="brand" href="/" aria-label="Vantly home">{MARK} vantly</a>
  {'<a class="crumb" href="/help">Help center</a>' if crumb else ''}
</div></nav>
<main class="wrap">{body}</main>
<footer><div class="wrap">© 2026 Vantly · <a href="/">vantlyapps.com</a> · <a href="/privacy">Privacy</a></div></footer>
</body>
</html>
"""


def build():
    out = HERE
    cards = "".join(
        f'<a class="card" href="/help/{a["slug"]}"><strong>{html.escape(a["title"])}</strong><span>{html.escape(a["summary"])}</span></a>'
        for a in ARTICLES
    )
    faq = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in FAQ)
    index = f"""
<h1>Help center</h1>
<p class="lede">Everything you need to set up and run Vantly Returns.</p>
<div class="grid">{cards}</div>
<h2 id="faq">Frequently asked questions</h2>
{faq}
<p class="more">Can't find an answer? Email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
"""
    (out / "index.html").write_text(page("Help center", "Guides and answers for Vantly Returns.", index, False))
    for i, a in enumerate(ARTICLES):
        nxt = ARTICLES[(i + 1) % len(ARTICLES)]
        body = f"""
<article class="article">
<h1>{html.escape(a["title"])}</h1>
<p class="lede">{html.escape(a["summary"])}</p>
{a["body"]}
<p class="more">Next: <a href="/help/{nxt["slug"]}">{html.escape(nxt["title"])}</a> · Questions? <a href="mailto:{CONTACT}">{CONTACT}</a></p>
</article>
"""
        (out / f'{a["slug"]}.html').write_text(page(a["title"], a["summary"], body, True))
    print(f"Built {len(ARTICLES)} articles + index")


if __name__ == "__main__":
    build()
