# Gleam on a Shopify store

Load this when the user runs a Shopify store. Read from the official pages on 9 September 2026: [Shopify Installation Guide](https://gleam.io/docs/competitions/installation/shopify) (updated 27 July 2026) and [Shopify Integration](https://gleam.io/docs/integrations/shopify) (updated 10 July 2025). State nothing beyond them, and re-check plan gates before quoting.

## Install

Five minutes.

- Install the Gleam Competitions app from the Shopify app store. It appears in the Shopify admin, and the connection shows under Settings, Integrations in Gleam.
- **Automatically create a page.** When building the competition, the first installation option creates a page in the Shopify store with the competition embedded, titled with the competition name. Edit the page under Pages in the Shopify admin. This is the page to link from the announcement bar and the nav.
- **Open Graph tags** for that page are saved in a metafield. The docs give a snippet for `theme.liquid` before the closing head tag so shares of the page carry the campaign image and title.
- **Manual page.** Paste the embed code from the installation options into a page with the HTML editor on.
- **Tab.** On the Business plan the competition can sit as a tab, with the tab code before the closing body tag in `theme.liquid`.

## Sync Entrants to the customer list

- Shopify integrations are on the Pro plan and above. Check the plan first.
- Under Settings, Integrations, Shopify, turn on Sync Gleam subscribers to Shopify customer list. Subscribe actions on Competitions and Rewards campaigns, and Capture emails, then sync to the customer list.
- Add tags in the site settings, or per campaign by changing Use site settings to Add different tags. Tag with the campaign name so the non-Winner code and welcome series in giveaway-winner-communications, and the retargeting segment in giveaway-promotion-plan, all filter on it.
- **Test before launch**: create the competition with a Subscribe action linked to Shopify, complete the action from the dashboard, go to the Actions tab and mark the invalidated admin action valid, and the address appears in the customer list within a few minutes.

## What the dataset shows for Shopify stores

From the campaign data, stores with a labelled organizer site and 100 or more Entrants. Product count, price and currency comparisons cover Shopify campaigns with that store attribute recorded. The platform comparison covers campaigns labelled Shopify or WooCommerce. Missing attribute coverage is not reported for these cuts.

The 1,000+ product group recorded a typical ten-day run. The under-20 USD price group had longer runs and offered email more often than the 200+ USD group. Australian-currency stores offered email more often than US-currency stores. Shopify campaigns offered email more often than WooCommerce campaigns and recorded fewer Entries per Entrant. That measure does not count Entry Methods or justify shortening an Action list. These are historical comparisons, not predictions of what changing a setting will achieve.

| Comparison | Group | Email offered | Other | Campaigns (businesses) |
|---|---|---|---|---|
| Product count | 1,000+ products | 80.7% | 10-day run | 879 (98) |
| | 50 to 199 products | 48.5% | 11-day run | 892 (245) |
| Price | 200 USD and over | 62.0% | 21-day run | 300 (138) |
| | Under 20 USD | 73.9% | 28-day run | 410 (94) |
| Currency | Australian dollars | 82.9% | - | 251 (112) |
| | US dollars | 51.3% | - | 2,635 (555) |
| Platform | Shopify | 53.3% | 3.76 Entries per Entrant | 3,997 (937) |
| | WooCommerce | 39.6% | 4.54 Entries per Entrant | 7,660 (1,107) |

Source: `analysis/output/industries.json`, shopify_store_size, shopify_price_band, shopify_currency, by_store_platform. Each row counts campaigns and distinct businesses. A median describes the typical campaign in that group.

## What the docs do not cover

Cart and wishlist mechanics, discount codes and the store's own email flows are Shopify and email-tool features. The store campaign formats are in giveaway-idea-generator, the actions in giveaway-entry-method-planner, and the non-Winner code in giveaway-winner-communications.

Uninstalling the app from Shopify cancels a plan billed through Shopify. A plan on credit card billing is cancelled inside Gleam first.
