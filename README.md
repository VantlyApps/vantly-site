# vantlyapps.com

The Vantly marketing site, hosted on GitHub Pages at vantlyapps.com (see `CNAME`). Static HTML, no build step except the help center.

## Pages

- `index.html`: Vantly home. One card per app, plus how we build.
- `returns/index.html`: Vantly Returns (live). Pitch, pricing, install buttons.
- `cancellations/index.html`: Vantly Cancellations (coming soon). Pitch and "Get notified".
- `help/`: help center. Edit articles in `help/build.py`, then run `python3 help/build.py`.
- `privacy.html`, `security.html`, `dpa.html`: legal pages.
- `assets/site.css`: shared styles for the home and app pages.

## Install links

Install buttons link to the Shopify App Store listing directly. Vantly Returns:
https://apps.shopify.com/vantly-returns

When Cancellations launches, swap its "Get notified" buttons for an install link to its listing, and change its badges from "Coming soon".
