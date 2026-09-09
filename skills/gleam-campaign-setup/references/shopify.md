# Gleam on a Shopify store

Load this when the user runs a Shopify store. Read from the official pages on 9 September 2026: [Shopify Installation Guide](https://gleam.io/docs/competitions/installation/shopify) (updated 27 July 2026) and [Shopify Integration](https://gleam.io/docs/integrations/shopify) (updated 10 July 2025). State nothing beyond them, and re-check plan gates before quoting.

## Install

Five minutes.

- Install the Gleam Competitions app from the Shopify app store. It appears in the Shopify admin, and the connection shows under Settings, Integrations in Gleam.
- **Automatically create a page.** When building the competition, the first installation option creates a page in the Shopify store with the competition embedded, titled with the competition name. Edit the page under Pages in the Shopify admin. This is the page to link from the announcement bar and the nav.
- **Open Graph tags** for that page are saved in a metafield. The docs give a snippet for `theme.liquid` before the closing head tag so shares of the page carry the campaign image and title.
- **Manual page.** Paste the embed code from the installation options into a page with the HTML editor on.
- **Tab.** On the Business plan the competition can sit as a tab, with the tab code before the closing body tag in `theme.liquid`.

## Sync entrants to the customer list

- Shopify integrations are on the Pro plan and above. Check the plan first.
- Under Settings, Integrations, Shopify, turn on Sync Gleam subscribers to Shopify customer list. Subscribe actions on Competitions and Rewards campaigns, and Capture emails, then sync to the customer list.
- Add tags in the site settings, or per campaign by changing Use site settings to Add different tags. Tag with the campaign name so the non-winner code, the welcome series and the retargeting segment in giveaway-promotion-plan all filter on it.
- **Test before launch**: create the competition with a Subscribe action linked to Shopify, complete the action from the dashboard, go to the Actions tab and mark the invalidated admin action valid, and the address appears in the customer list within a few minutes.

## What the docs do not cover

Cart and wishlist mechanics, discount codes and the store's own email flows are Shopify and email-tool features. The store campaign formats are in giveaway-idea-generator, the actions in giveaway-entry-method-planner, and the non-winner code in giveaway-winner-communications.

Uninstalling the app from Shopify cancels a plan billed through Shopify. A plan on credit card billing is cancelled inside Gleam first.
