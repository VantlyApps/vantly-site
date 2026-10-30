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
<p>Go to <strong>Return portal</strong> in Vantly. The page has two tabs: <strong>Look</strong> for the design and <strong>Text</strong> for the wording.</p>
<h2>Choose a template</h2>
<ul>
<li><strong>Side by side</strong> (the default): built for big screens. What the customer is returning sits on the left and the next step on the right, with no scrolling. On phones it becomes one column.</li>
<li><strong>Classic</strong>: one bold, focused column with a floating bar, made for scrolling on every screen.</li>
</ul>
<p>Customers can go back a step at any time, and their picks stay filled in.</p>
<h2>Review before submitting</h2>
<p>After choosing how they're paid back, customers see a summary (what's going back, what they get, and the totals) and press <strong>Confirm</strong>. It's on by default. To create returns straight away instead, turn off <strong>Let customers review before submitting</strong> in <strong>Settings › Return options</strong>.</p>
<h2>Match your brand</h2>
<p>On the <strong>Look</strong> tab, upload your logo and choose its position (left, center, or right). Vantly warns you if the logo is too small to look sharp. Then set your colors, corner style, and font.</p>
<h2>Change the wording</h2>
<p>On the <strong>Text</strong> tab, every piece of text in the portal can be changed, grouped by step: headings, buttons, hints, and confirmation messages. The preview updates as you type, and <strong>Open return portal</strong> lets you walk through it like a customer.</p>
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
<p>Your <strong>default settings</strong> cover every product. <strong>Rules</strong> change the terms for the products they match, like a longer window for snowboards or final sale for clearance items.</p>
<h2>How rules are checked</h2>
<p>Rules are checked from the top of the list, and each item follows the <strong>first rule that matches it</strong>. Anything no rule matches uses your default settings, which are always the last row. Drag a rule by its ⋮⋮ handle to change the order, and put narrow rules (like final sale) above broad ones.</p>
<h2>Create a rule</h2>
<p>Go to <strong>Rules › Create rule</strong>.</p>
<ul>
<li><strong>Applies to</strong>: the product (tag, collection, type, vendor, SKU, price, or where it shipped from), the order (tag, discount code, total, date, shipping country, whether it has Vantly package protection, or whether it contains a SKU), the customer (tag, past returns, order count), or the return itself (item condition, reason, chosen outcome, return value). Match any or all of them.</li>
<li><strong>Returns</strong>: returnable or final sale, the return window, and whether it counts from delivery or shipment.</li>
<li><strong>Return options</strong>: which of refund, store credit, exchange, and replacement customers can choose. These replace your default options for the items the rule matches.</li>
<li><strong>Fees and bonus</strong>: restocking fee, return shipping fee, and bonus credit. Leave a field blank to use your default.</li>
<li><strong>Return reasons</strong>: a reason list just for these products (for example, boots: Too tight, Too loose, Wrong flex). Drag reasons to reorder them, and turn on <strong>Photo required</strong> for any reason that needs one.</li>
<li><strong>Extras</strong>: require a photo, approve automatically, let the customer keep the item (always, or only the first time), show a message, waive fees, ask the customer to agree to a statement, tag the customer when approved, or send the items to a <a href="/help/reviewing-returns">return destination</a>.</li>
<li><strong>Review and order</strong>: flag returns for review, use the rule only once per customer, or let rules below also apply.</li>
</ul>
<h2>Different terms for opened items</h2>
<p>Make two rules, one with the condition <strong>Item condition is Opened</strong> and one with <strong>Item condition is Unopened</strong>, and give each its own options and fees. The portal then asks customers whether each item was opened. (Older rules may still show a <strong>When opened</strong> section; it keeps working.)</p>
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
<p>When a customer chooses an exchange, they see <strong>other sizes and colors</strong> of the same product first, then <strong>similar products</strong> under "You might also like". If their reason is "too small" or "too big", the portal suggests one size up or down. In <strong>Settings › Exchanges</strong>, choose where similar products come from: the same product type, collection, vendor, or tag.</p>
<h2>When the new item ships</h2>
<p>In <strong>Settings › Exchanges</strong>, choose <strong>Send exchanges</strong>: after the returned item arrives, or as soon as the return is approved. If the new item is out of stock, Vantly gives store credit or a refund instead (your choice).</p>
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
<p>If the new item costs less, choose whether the rest becomes store credit, a refund, or nothing. Staff can also change the price of any exchange on the return page before its order is created.</p>
""",
    },
    {
        "slug": "reviewing-returns",
        "title": "Reviewing returns",
        "summary": "Approve, reject single items, adjust values, and complete returns.",
        "body": """
<p>New returns appear on the <strong>Returns</strong> page. Open one to review it.</p>
<h2>Work on many returns at once</h2>
<p>On the <strong>Returns</strong> page, tick the returns you want, then choose <strong>Approve</strong>, <strong>Mark received</strong>, or <strong>Complete</strong> (up to 50 at a time). Vantly asks you to confirm, and tells you about any return it couldn't change.</p>
<h2>Approve or reject</h2>
<p><strong>Approve return</strong> accepts it in Shopify and emails the customer the next steps. <strong>Reject</strong> closes it and tells the customer why.</p>
<p>To accept only some items, switch those items to <strong>Reject</strong> in the Items list and give a reason. The button then reads, for example, <strong>Approve 1 of 2 items</strong>.</p>
<h2>Adjust an item's value</h2>
<p>Click the pencil next to an item's price to deduct or add an amount (for example, a missing part or a goodwill credit). The reason is saved in the return's history; the customer doesn't see it.</p>
<h2>Receive and complete</h2>
<p>When the package arrives, mark it <strong>received</strong>, choose whether to restock each item, then complete the return to issue the refund, store credit, or exchange order.</p>
<h2>Green returns</h2>
<p>When a rule lets the customer keep the item, there's nothing to ship back. The customer gets a "You can keep it" email and the return goes straight to payout.</p>
<h2>Create a return for a customer</h2>
<p>Customer called or emailed? On the <strong>Returns</strong> page, create a return yourself: find the order, pick the items, reason, and outcome. It's approved right away. You can let the customer keep the items, waive fees, and make an exception for items your rules block (it's noted on the return).</p>
<h2>Restock as a different product</h2>
<p>In <strong>Settings › Restock as</strong>, map a product to another one, for example an opened board back into stock as "Used". Choose whether the mapping applies always, only to opened items, or only to unopened ones. You can upload the mappings as a spreadsheet.</p>
<h2>Return destinations</h2>
<p>In <strong>Settings › Return destinations</strong>, add other addresses, like a supplier or a second warehouse. A rule's <strong>Where these items go back to</strong> sends matching items there, and labels are made out to that address. If a return mixes items for different places, the customer gets one return per destination. Turn off <strong>Count these items back into my inventory</strong> for drop-ship suppliers.</p>
<h2>Bundles</h2>
<p>Bundles sold as one product can be returned by their individual items. Set them up in <strong>Settings › Bundles</strong>. The refund for each item is what the customer paid for the bundle, split by each item's current store price.</p>
""",
    },
    {
        "slug": "labels",
        "title": "Return labels",
        "summary": "Buy return labels with ShipStation, EasyPost, or Shippo, automatically or by hand.",
        "body": """
<p>Vantly can buy return labels with your own carrier accounts and rates, then email them to the customer.</p>
<h2>Which carriers?</h2>
<p>Vantly connects to carriers <strong>through ShipStation, EasyPost, or Shippo</strong>, not one carrier at a time. Connect one and you can use <strong>USPS, UPS, FedEx, DHL</strong>, and any other carrier in that account:</p>
<ul>
<li><strong>ShipStation</strong>: the carriers you've connected in ShipStation, at your ShipStation rates.</li>
<li><strong>EasyPost</strong>: EasyPost's discounted USPS, UPS, and FedEx rates, or your own carrier accounts added in EasyPost.</li>
<li><strong>Shippo</strong>: Shippo's discounted USPS, UPS, FedEx, and DHL rates, or your own carrier accounts added in Shippo.</li>
</ul>
<p>Don't use any of them? You can still add a label by hand on any return (paste a tracking number and label link).</p>
<h2>Connect an account</h2>
<p>Go to <strong>Integrations</strong> and open <strong>ShipStation</strong>, <strong>EasyPost</strong>, or <strong>Shippo</strong>. Paste your API key; Vantly checks it right away and stores it encrypted. It then lists the carriers connected to that account. Test keys work too, for free test labels.</p>
<h2>International returns</h2>
<p>For cross-border returns, ShipStation and EasyPost labels include returned-goods customs information automatically.</p>
<h2>Label rules</h2>
<ul>
<li><strong>When buying a label, choose</strong>: cheapest, fastest, or best value.</li>
<li><strong>Maximum label price</strong>: never pay more than this.</li>
<li><strong>Only use some carriers and services</strong>: tick the carriers or single services you want.</li>
<li><strong>Buy a label automatically when a return is approved</strong>.</li>
<li><strong>Default package</strong>: weight is used when products don't have their own. Box size is optional (some carriers price by size).</li>
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
        "summary": "Labels, ShipBob, Katana, Klaviyo, Omnisend, Brevo, Slack, and webhooks.",
        "body": """
<p>Go to <strong>Integrations</strong> to connect the tools you already use. Each one has its own page, and keys are stored encrypted.</p>
<h2>ShipStation, EasyPost, and Shippo</h2>
<p>Buy return labels with your carrier accounts. See <a href="/help/labels">Return labels</a>.</p>
<h2>ShipBob</h2>
<p>If ShipBob runs your warehouse, Vantly creates each approved return in ShipBob (with the tracking number when there's a label) and marks the return received when the warehouse gets it. Paste a ShipBob personal access token (in ShipBob: <strong>Integrations › API Tokens › Generate New Token</strong>), choose the fulfillment center that receives returns, and choose what ShipBob does with returned items: ShipBob's default, restock, quarantine, or dispose. Items the customer keeps, and items going to a <a href="/help/reviewing-returns">return destination</a>, aren't sent to ShipBob.</p>
<h2>Katana</h2>
<p>If Katana manages your stock, Vantly restocks returned items in Katana (matched by SKU) so its numbers stay right. Choose the Katana location, and whether to restock in Katana only, Shopify only, or both. If Katana syncs stock to Shopify, choose Katana only.</p>
<h2>Klaviyo</h2>
<p>Paste a Klaviyo private API key with Accounts: Read, Events: Write, and Profiles: Write. Vantly sends an event for each return moment (for example <em>Vantly Return Requested</em> or <em>Vantly Return Refunded</em>) with the order, items, reasons, amount, and tracking. Build flows and segments on them. Add the flow filter <strong>NotifyCustomer is true</strong> so staff choices not to email the customer are respected.</p>
<h2>Omnisend and Brevo</h2>
<p>Paste your API key and Vantly sends the same return events to Omnisend or Brevo. Under <strong>Who emails your customers about returns?</strong>, choose Vantly or your email platform; if you choose the platform, Vantly's own customer emails stay off. Send a test event to confirm the key works.</p>
<h2>Slack</h2>
<p>Post returns to a channel, like #returns. Create an incoming webhook in Slack, paste the link (it starts with <code>https://hooks.slack.com/</code>), and choose what to post: new returns, only flagged returns, or new returns and every update. Each message shows the order, customer, outcome, amount, and items with reasons, plus a button that opens the return in Vantly.</p>
<h2>Webhooks</h2>
<p>Send return updates to any system, like a 3PL or ERP. Add an https endpoint and Vantly POSTs JSON to it every time a return changes (for example <code>return.label_created</code>). Each request is signed with your signing secret in the <code>X-Vantly-Signature</code> header.</p>
<h2>Coming soon</h2>
<p>Gorgias (see a customer's returns next to their tickets) and Shopify Flow.</p>
""",
    },
    {
        "slug": "team",
        "title": "Team and permissions",
        "summary": "Invite your team and choose what each person can do.",
        "body": """
<p>Until you add someone, everyone on your Shopify staff who opens Vantly is an Admin. To give people different access, go to <strong>Settings › Users and roles</strong>.</p>
<h2>Roles</h2>
<table class="table">
<tr><th>Role</th><th>What they can do</th></tr>
<tr><td>Admin</td><td>Everything, including users, settings, branding, and package protection.</td></tr>
<tr><td>Manager</td><td>All return work, including refunds, exchanges, and price changes, plus rules and bundles.</td></tr>
<tr><td>Agent</td><td>Review returns: approve, reject, notes, labels, and create returns. Can't issue money or change prices.</td></tr>
<tr><td>Viewer</td><td>Can look at returns and analytics, but can't change anything.</td></tr>
</table>
<p>The store owner is always an Admin.</p>
<h2>Invite someone</h2>
<p>Add their email, an optional name, and a role. Tick <strong>Email them a link to the app</strong> to send them a way in. You can change someone's role or remove them at any time.</p>
<h2>Everyone else</h2>
<p><strong>Staff who aren't on the list</strong> sets the role for any other Shopify staff member who opens the app, or turns their access off.</p>
<h2>Who did what</h2>
<p>Every change on a return is saved in its history with the staff member's name.</p>
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
    ("Can I connect USPS, UPS, FedEx, or DHL directly?", "Vantly connects to carriers through ShipStation, EasyPost, or Shippo. Connect one and you can use USPS, UPS, FedEx, DHL, and the other carriers in that account, at your own rates (or EasyPost's and Shippo's discounted rates). No shipping account? You can still add a label by hand on any return."),
    ("Do customers need an account?", "No. They find their order with the order number and email."),
    ("Can I create a return for a customer myself?", "Yes. Click Create return on the Returns page, find the order, and pick the items and outcome. It's approved right away, and you can make exceptions to your rules."),
    ("Can I approve or complete lots of returns at once?", "Yes. Tick returns on the Returns page and choose Approve, Mark received, or Complete, up to 50 at a time."),
    ("Can I give my team limited access?", "Yes. In Settings › Users and roles, give each person a role: Admin, Manager, Agent, or Viewer. Agents can review returns but can't issue money."),
    ("Can some returns go to a supplier or another warehouse?", "Yes. Add the address in Settings › Return destinations, then use a rule to send matching items there. Labels are made out to that address."),
    ("Does it work with ShipBob?", "Yes. Approved returns are created in ShipBob, and Vantly marks them received when the warehouse gets them."),
    ("Can my email platform send the return emails?", "Yes, with Klaviyo, Omnisend, or Brevo. Vantly sends an event for each return step, and you choose whether Vantly or your platform emails the customer."),
    ("Can I get return alerts in Slack?", "Yes. Connect Slack under Integrations and choose new returns, flagged returns only, or every update."),
    ("Does it work with my theme?", "Yes. The portal and the protection widget are built to fit any theme. The widget's colors and text are yours."),
    ("What happens if I go over my plan's returns?", "Nothing stops. You'll see a notice with the plan that fits."),
    ("Who keeps the package protection fee?", "You do, all of it. Vantly doesn't take a share."),
    ("What happens to my data if I uninstall?", "All of your store's data is deleted after Shopify's deletion request. See the privacy policy."),
]


# ---------------- Vantly Cancellations (coming soon) ----------------
# Served at vantlyapps.com/help/cancellations/<slug>
CANCEL_ARTICLES = [
    {
        "slug": "how-it-works",
        "title": "How Vantly Cancellations works",
        "summary": "The cancel portal, step by step, from the customer's side and yours.",
        "body": """
<p>Vantly Cancellations gives your customers a self-serve page to cancel an order before it ships. Before they confirm, they tell you why and see an offer made for that reason. They can always still cancel.</p>
<h2>What the customer sees</h2>
<ol>
<li><strong>Find order.</strong> They enter their order number and email. No account needed.</li>
<li><strong>Items and reason.</strong> Every item is selected. They untick anything they want to keep, then pick a reason for what they're cancelling. Follow-up questions open under the reason when you've set them up.</li>
<li><strong>Review.</strong> They see the offer you set for that reason, like a product that solves the problem, a discount, or a size swap. Two buttons: <strong>Keep my order</strong> or <strong>Cancel anyway</strong>, with the refund amount shown.</li>
<li><strong>Done.</strong> A clear confirmation: what was cancelled, what still ships, and when the refund arrives.</li>
</ol>
<h2>What happens behind the scenes</h2>
<ul>
<li>As soon as a customer starts, the order is put on a <strong>fulfillment hold</strong>, so your warehouse doesn't ship it mid-decision.</li>
<li><a href="/help/cancellations/rules">Rules</a> decide if the cancel goes through right away, waits for your approval, or isn't allowed.</li>
<li>If they keep the order, the hold is released and the order ships. Anything they added from an offer goes on the same order.</li>
<li>If they cancel, the items are refunded and restocked, and the order is tagged <code>vantly-cancelled</code>.</li>
</ul>
<h2>Where customers find it</h2>
<p>The portal lives at <code>yourstore.com/apps/cancel</code>. Link it from your Shopify order confirmation, your FAQ, and your account page.</p>
""",
    },
    {
        "slug": "reasons-and-offers",
        "title": "Reasons, questions and offers",
        "summary": "Product groups, follow-up questions, and the offer each reason shows.",
        "body": """
<p>Reasons are what customers pick when they cancel. Each reason can ask follow-up questions and show one offer.</p>
<h2>Product groups</h2>
<p>Different products get cancelled for different reasons. A snowboard might be cancelled because the customer doesn't have bindings yet, boots because they're worried about the fit. Product groups let each kind of product have its own list.</p>
<ul>
<li>Go to <strong>Reasons &amp; offers</strong> and click <strong>Add product group</strong>.</li>
<li>Choose which products belong to it by collection, product, or product tag.</li>
<li>Add the reasons for that group.</li>
</ul>
<p>Groups are checked from the top. If a product fits two groups, the higher one wins. <strong>Everything else</strong> is always last and covers every product not in a group. There's no limit on how many groups you can have.</p>
<p>If an order has items from two groups, the customer answers once per group, not once per item.</p>
<h2>Shared reasons</h2>
<p>Reasons like "Found a better price" or "Wrong shipping address" apply to everything. Set them up once under <strong>Shared reasons</strong>. They show after each group's own reasons, and you can turn one off for a specific group.</p>
<h2>Follow-up questions</h2>
<p>Questions open under a reason when the customer picks it: choose one, short text, long text, or a product picker. The answers show on each cancellation and in Overview, so you can see the real cause, like "is missing bindings".</p>
<h2>Offers</h2>
<p>Each reason can show one offer:</p>
<ul>
<li><strong>Suggest products</strong>: add-ons that solve the problem. A product can show to everyone or only for certain answers.</li>
<li><strong>Discount</strong>: a code or a partial refund.</li>
<li><strong>Swap item</strong>: change the variant or product instead of cancelling.</li>
<li><strong>Shipping upgrade</strong>: a faster method at no cost.</li>
<li><strong>Fix address</strong>: edit the shipping address before it ships.</li>
<li><strong>Message only</strong>: a short note and a link.</li>
<li><strong>No offer</strong>: go straight to the cancel button.</li>
</ul>
<p>The customer can always cancel. Offers never hide the cancel button.</p>
""",
    },
    {
        "slug": "rules",
        "title": "Cancellation rules",
        "summary": "Decide which orders can be cancelled, and whether you approve them first.",
        "body": """
<p>Rules run when the customer looks up their order, before any reasons or offers. They decide what happens:</p>
<ul>
<li><strong>Auto-cancel</strong>: refunded and restocked right away.</li>
<li><strong>Needs approval</strong>: the order stays paused until you approve or decline it.</li>
<li><strong>Block</strong>: the customer sees your message instead, like "Your order is already being packed."</li>
</ul>
<h2>How rules are checked</h2>
<p>From the top of the list; the first rule that matches decides. Drag the handle to change the order. The last rule, <strong>Everything else</strong>, covers every order the rules above didn't match. Orders that already shipped can never be cancelled in the portal.</p>
<h2>Conditions</h2>
<p>Every condition is picked from your store, not typed: order total, time since the order, time of day, customer tag, order tag, collection, product, product tag, payment method, and shipping country. Match all or any of them.</p>
<h2>Common setups</h2>
<ul>
<li>Block cancels after your daily cutoff (for example after 2 p.m. for same-day shipping).</li>
<li>Approve big orders yourself.</li>
<li>Block wholesale customers or final sale items.</li>
</ul>
""",
    },
    {
        "slug": "managing-cancellations",
        "title": "Managing cancellations",
        "summary": "The cancellations list, approvals, and what you see on each one.",
        "body": """
<p><strong>Cancellations</strong> lists every request, with tabs for <strong>Needs approval</strong>, <strong>Saved</strong>, <strong>Cancelled</strong> and <strong>Blocked</strong>.</p>
<h2>Each cancellation</h2>
<p>Click a row to see:</p>
<ul>
<li><strong>Items</strong>: which were cancelled, which were kept, and anything added from an offer.</li>
<li><strong>What the customer told you</strong>: the reason and answers per product group, the offer they saw, and whether they took it.</li>
<li><strong>Summary</strong>: refund, revenue saved, and which rule applied.</li>
<li><strong>History</strong>: every step with times, from the hold to the refund.</li>
</ul>
<h2>Approvals</h2>
<p>When a rule says <strong>Needs approval</strong>, the order stays paused. Click <strong>Approve cancel</strong> to refund and restock, or <strong>Decline</strong> to keep the order and resume shipping. Vantly Cancellations doesn't send its own emails; Shopify's standard notifications (like order cancelled and refund) go out from your Shopify settings.</p>
""",
    },
    {
        "slug": "analytics",
        "title": "Overview and analytics",
        "summary": "Revenue saved, save rate, and why customers cancel.",
        "body": """
<p><strong>Overview</strong> shows how your cancel portal is doing:</p>
<ul>
<li><strong>Revenue saved</strong>: orders customers kept after seeing an offer.</li>
<li><strong>Save rate</strong>: the share of cancel requests that ended in a kept order.</li>
<li><strong>Why customers cancel</strong>: each reason, how often it was picked, and how often you saved it.</li>
<li><strong>What the answers say</strong>: follow-up answers for a reason, so you can spot the real cause.</li>
<li><strong>Offer performance</strong>: how often each offer was shown and accepted.</li>
</ul>
<p>Pick any date range, from Today to All time or your own dates, and compare with the previous period or the same period last year.</p>
""",
    },
]

CANCEL_FAQ = [
    ("When is Vantly Cancellations available?", "It's in development and coming soon to the Shopify App Store. Email support@vantlyapps.com to hear when it launches."),
    ("Can customers cancel only part of an order?", "Yes. Every item starts selected, and customers untick what they want to keep. The refund covers only what they cancel, and the rest ships as planned."),
    ("Can a customer always cancel?", "Yes, as long as your rules allow it. Offers never hide the cancel button."),
    ("Do customers have to give a reason?", "Yes, one reason per product group they're cancelling. Follow-up questions are optional unless you make them required."),
    ("What stops my warehouse from shipping while the customer decides?", "The order goes on a fulfillment hold as soon as the customer starts. It's released if they keep the order."),
    ("Can different products have different reasons?", "Yes. Product groups give snowboards, boots, or any other kind of product their own reasons, questions and offers. There's no limit on groups."),
    ("What if the order has already shipped?", "The portal won't cancel it. You can point customers to your return portal instead."),
    ("Does it work with Vantly Returns?", "Yes. Both share your portal branding, and they're built to be used together."),
    ("Do customers need an account?", "No. They find their order with the order number and email."),
    ("Does Vantly send emails to my customers?", "No. Shopify's own notifications (order cancelled, refund, payment link) go out from your Shopify settings."),
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
.nav .links { margin-left:auto; display:flex; gap:18px; font-size:14px; }
.nav .links a { color:var(--muted); text-decoration:none; }
.nav .links a:hover { color:var(--ink); }
@media (max-width:560px) { .nav .wrap { gap:12px; } .nav .crumb { display:none; } .nav .links { gap:12px; font-size:13px; } }
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
.soon { letter-spacing:0; font-family:"Inter",sans-serif; line-height:1.4; display:inline-block; margin-left:6px; padding:2px 8px; border-radius:99px; font-size:.72rem; font-weight:600; color:var(--teal) !important; background:color-mix(in srgb, var(--teal) 12%, transparent); vertical-align:2px; }
.note { border:1px solid var(--line); background:var(--soft); border-radius:12px; padding:12px 16px; margin:0 0 26px; color:var(--muted); }
details p { margin:10px 0 0; color:var(--muted); }
.more { margin-top:44px; padding-top:22px; border-top:1px solid var(--line); color:var(--muted); }
footer { border-top:1px solid var(--line); padding:28px 0 40px; color:var(--muted); font-size:14px; }
"""

MARK = '<svg viewBox="12 9 40 48" aria-hidden="true"><g transform="translate(1.5 6)"><path d="M16 20 L30 46 L41 25 C45 17 42 11 35 11 L31 11" fill="none" stroke="#0F6E56" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/><path d="M25 11 L32 6 L32 16 Z" fill="#5DCAA5" stroke="#5DCAA5" stroke-width="2" stroke-linejoin="round"/></g></svg>'
CONTACT = "support@vantlyapps.com"


def page(title: str, description: str, body: str, crumb: bool, app: str = "Returns", home: str = "/help") -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{html.escape(title)} · Vantly {app} Help</title>
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
  {f'<a class="crumb" href="{home}">Help center</a>' if crumb else ''}
  <div class="links"><a href="/returns/">Returns</a><a href="/cancellations/">Cancellations</a><a href="/help">Help</a></div>
</div></nav>
<main class="wrap">{body}</main>
<footer><div class="wrap">© 2026 Vantly · <a href="/">vantlyapps.com</a> · <a href="/returns/">Returns</a> · <a href="/cancellations/">Cancellations</a> · <a href="/privacy">Privacy</a></div></footer>
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
<p class="lede">Guides and answers for every Vantly app.</p>
<h2>Vantly Returns</h2>
<div class="grid">{cards}</div>
<h2>Vantly Cancellations <span class="soon">Coming soon</span></h2>
<div class="grid"><a class="card" href="/help/cancellations/"><strong>Cancellations guides</strong><span>Self-serve cancels with save offers. See how it will work.</span></a></div>
<h2 id="faq">Vantly Returns: frequently asked questions</h2>
{faq}
<p class="more">Can't find an answer? Email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
"""
    (out / "index.html").write_text(page("Help center", "Guides and answers for Vantly Returns and Vantly Cancellations.", index, False, "app").replace("· Vantly app Help", "· Vantly Help"))
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
    # Cancellations help
    cdir = out / "cancellations"; cdir.mkdir(exist_ok=True)
    home = "/help/cancellations/"
    note = '<p class="note"><strong>Coming soon.</strong> Vantly Cancellations is in development. These guides show how it will work.</p>'
    ccards = "".join(
        f'<a class="card" href="/help/cancellations/{a["slug"]}"><strong>{html.escape(a["title"])}</strong><span>{html.escape(a["summary"])}</span></a>'
        for a in CANCEL_ARTICLES
    )
    cfaq = "".join(f"<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>" for q, a in CANCEL_FAQ)
    cindex = f"""
<h1>Vantly Cancellations <span class="soon">Coming soon</span></h1>
<p class="lede">Let customers cancel unshipped orders on their own, and save the ones you can.</p>
{note}
<div class="grid">{ccards}</div>
<h2 id="faq">Frequently asked questions</h2>
{cfaq}
<p class="more">Looking for Vantly Returns? <a href="/help">Help center</a> · Questions? <a href="mailto:{CONTACT}">{CONTACT}</a></p>
"""
    (cdir / "index.html").write_text(page("Help center", "Guides and answers for Vantly Cancellations.", cindex, True, "Cancellations", "/help"))
    for i, a in enumerate(CANCEL_ARTICLES):
        nxt = CANCEL_ARTICLES[(i + 1) % len(CANCEL_ARTICLES)]
        body = f"""
<article class="article">
{note}
<h1>{html.escape(a["title"])}</h1>
<p class="lede">{html.escape(a["summary"])}</p>
{a["body"]}
<p class="more">Next: <a href="/help/cancellations/{nxt["slug"]}">{html.escape(nxt["title"])}</a> · <a href="{home}">All Cancellations guides</a> · Questions? <a href="mailto:{CONTACT}">{CONTACT}</a></p>
</article>
"""
        (cdir / f'{a["slug"]}.html').write_text(page(a["title"], a["summary"], body, True, "Cancellations", home))
    print(f"Built {len(ARTICLES)} articles + index, {len(CANCEL_ARTICLES)} Cancellations articles + index")


if __name__ == "__main__":
    build()
