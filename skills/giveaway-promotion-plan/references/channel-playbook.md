# Channel playbook

Advice. Formats change, so treat lengths and features as current practice, and check any platform rule in the entry-method planner's compliance notes before using tag-to-enter or share-to-enter.

Extracted: the top fifth of campaigns by Entrants saw a typical 35,505 Impressions against 4,047 for the bottom fifth, with the same Conversion Rate (28% against 28%). Reach is what separates them. A campaign that is not being seen is a promotion problem before it is a Prize problem.

## Measured traffic mix

Direct traffic supplies over half of all Impressions, well ahead of any single channel [across 54,660 campaigns from 10,692 businesses]. The rest splits across smaller traffic sources, none above 1.4%.

| Traffic source | Share of Impressions |
|---|---|
| Direct | 52% |
| Organizer's own site | 7.8% |
| Meta | 7.6% |
| Gleam's own pages | 7.5% |
| YouTube | 4.7% |
| X | 4.7% |
| Giveaway directories | 3.3% |
| Search | 2.6% |
| Gaming communities | 2.2% |
| Deals forums | 1.4% |
| TikTok | 0.7% |

Direct is the largest single line by far. A giveaway link travels through DMs, texts and QR codes that do not show where the click came from, so a large direct share is what real word-of-mouth reach looks like in the data, not a gap in the channel plan.

Hosted pages carried 63% of Impressions and embeds 36%. Even inside a campaign built to sit on the organizer's own site, most of the traffic still lands on the Gleam-hosted page, so the profile-prep and per-channel steps below apply whichever way the campaign is set up.

Source: analysis/output/field_cuts.json (referrer_channel_share, landing_kind_share).

## Where to list a giveaway

Extracted: the giveaway directories, deals forums and gaming communities that reached the most organizers. These are public third-party sites, so the host names are published.

| Giveaway directories | Businesses reached | Impressions |
|---|---|---|
| freestufftimes.com | 3,403 | 952,981 |
| contestgirl.com | 3,253 | 16,721,404 |
| sweepsadvantage.com | 3,080 | 3,409,200 |
| giveawaybase.com | 2,245 | 3,615,998 |
| ozbargain.com.au | 1,661 | 2,441,424 |

| Deals forums | Businesses reached | Impressions |
|---|---|---|
| hardprize.ru | 713 | 21,008 |
| slickdeals.net | 633 | 80,102 |
| lottos.com.au | 501 | 243,549 |
| ofertar.pt | 440 | 21,626 |
| loquax.co.uk | 396 | 1,089,609 |

| Gaming communities | Businesses reached | Impressions |
|---|---|---|
| steamcommunity.com | 692 | 1,403,251 |
| gamingtribe.com | 597 | 31,002 |
| store.steampowered.com | 106 | 43,408 |
| gaming.lenovo.com | 83 | 191,283 |
| gununiversity.com | 81 | 212,522 |

Extracted: outcomes for campaigns where one traffic source supplies over 10% of a campaign's Impressions.

| Traffic source over 10% of Impressions | Conversion Rate | Other figure | Campaigns | Businesses |
|---|---|---|---|---|
| Giveaway directories | 31.7% | 1,827 Entrants at the typical campaign | 6,768 | 2,254 |
| Deals forums | 47% | 1.9 Actions each, 7 referrals per 100 Entrants | 1,383 | 173 |
| YouTube | 41% | - | 5,131 | 1,217 |
| X | 34% | 5.23 actions per Entrant | 10,195 | 2,941 |
| Meta | 27% | 3.58 actions per Entrant | 8,391 | 3,139 |
| Search | 18.5% | - | 1,019 | 407 |
| TikTok | 15% | - | 178 | 102 |

Deals-forum traffic sees the highest Conversion Rate of any well-populated traffic source above, worth the spot on the promotion list for that alone. The audience does the minimum once it lands and rarely refers a friend, well below every other channel on both measures. Comparing like-sized campaigns does not change the picture. Treat deals forums as a source that turns visitors into Entrants, not a place to grow an email list or a referral chain from.

| Measure | Deals forums | Other traffic sources |
|---|---|---|
| Actions per Entrant | 1.9 | 3.6 to 5.9 |
| Referrals per 100 Entrants | 7 (lowest of any source measured) | direct: 32 |
| Actions per Entrant, campaigns of 1,000 to 2,500 Entrants | 1.8 [1,084 campaigns, 145 businesses] | - |
| Actions per Entrant, campaigns of 2,500 to 10,000 Entrants | 2.2 [241 campaigns, 60 businesses] | - |

Meta sees a Conversion Rate close to X's and carries the bigger traffic share of the two. Where it lags is follow-through: Meta runs fewer Actions per Entrant than X, and the gap holds at every campaign size. A campaign leaning on Meta for reach has room to add a referral or bonus-entry push to close that gap.

| Measure | Meta | X |
|---|---|---|
| Conversion Rate | 27% | 34% |
| Share of all Impressions | 7.6% | 4.7% |
| Actions per Entrant, overall | 3.58 | 5.23 |
| Actions per Entrant, 1,000-2,500 Entrants | 3.35 [4,347 campaigns, 1,970 businesses] | 5.11 [6,160 campaigns, 2,093 businesses] |
| Actions per Entrant, 2,500-10,000 Entrants | 3.75 [3,146 campaigns, 1,482 businesses] | 5.27 [3,422 campaigns, 1,328 businesses] |
| Actions per Entrant, 10,000+ Entrants | 4.65 [898 campaigns, 503 businesses] | 5.93 [613 campaigns, 324 businesses] |

Source: analysis/output/field_cuts.json (promotion_sites, outcomes_when_channel_over_10pct, channel_quantity_vs_quality, channel_quality_by_size_band).

## Tagging with UTM

Extracted, same campaign set: only 11% of Impressions carry a utm_source tag. Most traffic arrives untagged, which is exactly why the UTM line under Paid below matters on organic posts too. Tag every link you post, or the results review is left reading the traffic source and nothing about which post, story or email sent the visit.

| Of the tagged slice | Share |
|---|---|
| Email newsletters | 35% |
| Meta | 20% |
| Ad networks | 4.5% |
| TikTok | 3.5% |

Source: analysis/output/field_cuts.json (utm_source_share).

## Mass mail into the campaign

Extracted: among Impressions that carry an email UTM tag, share by provider named in utm_source. This is the organizer's own mass mail arriving at the campaign page, none of it sent by Gleam, and it is a share of the 11% of Impressions that carry any UTM tag at all, not a share of all traffic.

| Provider | Share of tagged email Impressions | Campaigns | Businesses |
|---|---|---|---|
| Unnamed or untagged | 44% | 6,965 | 1,910 |
| Listrak | 18% | 551 | 74 |
| Named newsletter source | 12% | 2,783 | 748 |
| Klaviyo | 11% | 2,215 | 804 |
| HubSpot | 3.5% | 734 | 217 |
| Attentive or SMS | 2.4% | 510 | 170 |
| ActiveCampaign | 1.7% | 318 | 71 |
| Salesforce or ExactTarget | 1.3% | 204 | 51 |
| ConvertKit | 1.4% | 93 | 30 |
| Sailthru | 1.0% | 293 | 23 |
| Omnisend | 0.8% | 277 | 119 |
| Iterable | 0.7% | 146 | 36 |
| MailChimp | 0.7% | 116 | 44 |
| Brevo or Sendinblue | 0.5% | 250 | 103 |
| Braze | 0.3% | 42 | 19 |

Campaigns that draw a tenth or more of their Impressions from their own tagged mass mail behave differently from campaigns with no tagged email traffic at all, though the two groups are not alike: the businesses that tag their email traffic are larger and run longer campaigns, so the gap describes who mails, not what mailing does.

<!-- generated:pp_mail_share -->
| Group | Conversion Rate | Actions per Entrant | Entrants (typical) | Campaigns | Businesses |
|---|---|---|---|---|---|
| Under 2% | 25.8% | 5.03 | 766 | 98,447 | 17,546 |
| No email traffic at all | 35.1% | 3.99 | 240 | 31,973 | 8,079 |
| 2 to 10% | 25.1% | 4.25 | 746 | 14,632 | 3,290 |
| 10 to 25% | 25.0% | 4.35 | 516 | 1,570 | 431 |
| A quarter or more | 27.5% | 4.84 | 440 | 316 | 56 |
<!-- /generated -->

An organizer with a list should tag the campaign link with an email UTM before sending, so the send shows up in this report. Gleam's export cannot see a send with no tag on the link.

## Mail clients: the wider view

Extracted: clicks whose traffic source is a mail client or a webmail page, which catches a send whether or not the link was tagged. 13,527,852 Impressions, 0.83% of all Impressions in the dataset, across 114,965 campaigns and 18,733 businesses. A mail-client source says the click came out of an email, never which email, so a link a friend forwarded counts the same as a newsletter.

| Client | Share of mail-client Impressions | Campaigns | Businesses |
|---|---|---|---|
| Gmail app | 82.7% | 104,961 | 17,468 |
| Gmail web | 7.6% | 66,268 | 12,886 |
| ISP or carrier webmail | 5.7% | 7,130 | 1,938 |
| AOL, GMX, Mail.ru and other free webmail | 1.6% | 11,583 | 2,616 |
| Outlook | 1.0% | 20,277 | 4,948 |
| provider hosted campaign page | 0.9% | 4,476 | 935 |
| Yahoo Mail | 0.4% | 6,715 | 2,215 |

Gmail's Android app alone carries 83% of it. Campaign and business counts are the largest single host in each group, never a sum, because one campaign reaches several.

Mail arrives later than everything else. On the start day and the six days after it, mail's share of its own total sits below traffic's share of its own (13.7% against 14.2% on day one, 6.3% against 7.9% on day three). From day eight it sits above, and stays above for the rest of the run. A list is what keeps a campaign moving after the launch push stops.

| Days a campaign received mail clicks | Campaigns | Businesses | Entrants | Conversion Rate |
|---|---|---|---|---|
| 1 day | 22,679 | 6,749 | 378 | 32% |
| 2 to 3 days | 24,817 | 7,487 | 515 | 29% |
| 4 to 7 days | 27,768 | 7,867 | 782 | 27% |
| 8 days or more | 39,445 | 8,682 | 1,489 | 20% |

Read that as who mails, never as what mailing does. Campaigns collecting mail clicks on eight days or more are four times the size of one-day campaigns and see a lower Conversion Rate, which is what size does to it everywhere in this data.

| Industry | Campaigns | Businesses | Share of campaigns where mail is a tenth of traffic |
|---|---|---|---|
| Health, wellness and fitness | 3,192 | 509 | 11.5% |
| Jewellery and watches | 467 | 173 | 9.6% |
| Local services | 927 | 182 | 3.3% |
| Media and entertainment | 21,848 | 2,115 | 2.2% |
| Education | 1,901 | 370 | 1.7% |
| Marketing agency | 1,243 | 165 | 0.4% |
| Travel and events | 4,028 | 669 | 0.4% |
| Pets | 971 | 211 | 0.3% |
| Apparel and fashion | 4,594 | 834 | 0.2% |

Plan tier tracks the same way, with Premium businesses drawing the most from mail clients and Hobby and Free the least. By organizer country, Argentina leads the share of campaigns drawing a tenth of traffic from mail, well ahead of Italy, Germany and the United States.

| Tier | Typical % of Impressions from mail clients |
|---|---|
| Premium | 0.7% |
| Business | 0.35% |
| Pro | 0.29% |
| Hobby | 0% |
| Free | 0% |

| Country | Share of campaigns drawing a tenth of traffic from mail | Campaigns |
|---|---|---|
| Argentina | 9.7% | 318 |
| Italy | 3.1% | - |
| Germany | 2.3% | - |
| United States | 1.7% | 55,074 |

Source: `analysis/output/email_traffic.json`, keys `totals`, `by_client`, `day_curve`, `days_mail_landed`, `email_share_by_industry`, `email_share_by_plan_tier`, `email_share_by_country`, built by the analysis behind it.


Source: analysis/output/field_cuts.json (email_traffic_by_provider, outcomes_when_email_over_10pct).

## Share clicks by reward size

Offering a Viral Share action is most of the gap in share clicks, before the reward size is even set.

| Group | Share clicks / Impressions | Share clicks per Entrant | Campaigns | Businesses |
|---|---|---|---|---|
| Offers Viral Share | 47% | 1.74 | 29,207 | 6,547 |
| No share action | 1.4% | 0.06 | 25,453 | 5,441 |

Among campaigns that offer it, the entries attached to a share widen the gap further:

| Share worth | Campaigns | Businesses | Share clicks / Impressions | Share clicks % of Entrants |
|---|---|---|---|---|
| 1 entry | 7,655 | 2,274 | 38% | 146 (1.46) |
| 2 to 4 entries | 4,933 | 1,566 | 39% | 163 (1.63) |
| 5 to 9 entries | 4,715 | 1,655 | 48% | 183 (1.83) |
| 10 or more entries | 11,904 | 2,553 | 60% | 190 (1.90) |

Source: analysis/output/field_cuts.json (share_clicks).

Offering a referral action raises Actions per Entrant at every campaign size, but the size of that lift does not grow as the campaign gets bigger. Comparing what campaigns with and without a referral action actually produce against what size and referral status predict on their own, the result lands close to that prediction at every campaign size tested. A referral action is worth building into the mix, but do not plan on the payoff scaling up just because the base to refer from is bigger.

| Campaign size (Entrants) | Predicted-actual ratio | Campaigns | Businesses |
|---|---|---|---|
| 1,000 to 10,000 or more (six bands) | 0.99 to 1.07 | 1,202 to 10,793 per band | 376 to 2,846 per band |

Source: analysis/output/success_profiles.json (interactions.referral_action_by_campaign_size).

## What a shared link is worth

Extracted, viral_click_conversion_excluding_crypto: with finance and crypto organizers removed, 15.8% of Viral Share clicks end in a referred entry, on 18,461 campaigns from 4,011 businesses. The same campaigns turn 24.3% of ordinary Impressions into Entrants, so a shared link converts a visitor at about two thirds the rate of any other visit to the page.

Pooled with crypto organizers back in, the referral rate rises well above the crypto-excluded figure, because crypto campaigns run referral farms (below, `viral_click_conversion`). Use the crypto-excluded figure for an ordinary business's plan, and expect the higher pooled figure if pulling the number straight from the JSON.

| Referral-rate figure | Value | Campaigns | Businesses |
|---|---|---|---|
| Pooled (crypto included) | 22.1% | 29,151 | 6,536 |
| Spread on the pooled figure | lower quarter 11.6%, upper quarter 43.5% | - | - |

| By industry | Referrals per click | Campaigns | Businesses |
|---|---|---|---|
| Software and SaaS | 58% | 918 | 181 |
| Finance and crypto | 44.4% | 10,690 | 2,590 |
| Marketing agency | 23.2% | 235 | 37 |
| Gaming | 18.6% | 2,992 | 808 |
| Baby and kids | 18.3% | 219 | 44 |
| Travel and events | 18.0% | 901 | 178 |
| Pets | 11.9% | 287 | 63 |
| Automotive | 10.6% | 808 | 91 |
| Toys and collectibles | 10.4% | 431 | 108 |

Software, SaaS, finance and crypto sit well above every other industry, crypto because of referral farms and software because sharing fits how that audience already works. Toys and collectibles, automotive and pets sit at the bottom.

By share worth, still on the pooled figures, higher worth goes with a higher referral rate and more clicks per Entrant. Read that as a worth that draws more sharing, not as proof that raising worth causes it, since the businesses that set a high worth differ from the ones that do not.

| Share worth | Referrals per click | Clicks per Entrant |
|---|---|---|
| 1 to 9 | 18.7% to 19.6% | 1.47 at worth 1 |
| 10 or more | 28.1% [11,903 campaigns, 2,555 businesses] | 1.90 |

Clicks are a subset of Impressions on 94% of campaigns. Where clicks exceed the campaign's own Impression count, the campaign is almost always a crypto campaign, a fraud tell worth watching for before crediting a shared link's reach.

Source: analysis/output/field_cuts.json (viral_click_conversion, viral_click_conversion_excluding_crypto, viral_click_conversion_by_worth, viral_click_conversion_by_industry).

## Referral rate by organizer type and channel size

Referrals % of Entrants fall as a YouTube host channel grows. A smaller channel's audience sits closer to the creator and shares more per person, a large channel's audience treats one giveaway post as one post among many.

| YouTube subscribers | Referrals % of Entrants | Campaigns | Businesses |
|---|---|---|---|
| Under 1,000 | 38 (0.38 per Entrant) | 180 | 23 |
| 1 million or more | 8 (0.08 per Entrant) | 643 | 80 |

Software and b2b businesses sit well above the consumer brand and retailer averages on referrals % of Entrants, near 90 per 100 (0.9 per Entrant). That fits an audience used to forwarding a link at work.

| Business type | Campaigns | Businesses |
|---|---|---|
| Software | 18,311 | 4,205 |
| B2B | 6,138 | 1,023 |

Source: analysis/output/industries.json (by_youtube_subscribers, by_business_type, by_audience).

## Traffic mix by country

YouTube supplies far more of India's and Brazil's Impressions than the United States', and Brazil's campaigns land almost entirely on the Gleam-hosted page, not an embed. A campaign built for a Brazilian or Indian audience can lean on a YouTube push harder than the US-only playbook above assumes.

| Country | YouTube share of Impressions | Gleam-hosted landing share | Campaigns | Businesses |
|---|---|---|---|---|
| India | 16% | - | 6,007 | 872 |
| Brazil | 19% | 97% | 5,857 | 562 |
| United States | 2.5% | 44% | 58,742 | 9,091 |

Source: analysis/output/indicators.json (referrer_mix_by_country, landing_kind_by_country).

## Profile prep, the day before launch

- Bio link goes to the entry page for the whole run. On Instagram and TikTok that is the only clickable link, so every caption says "link in bio".
- Pin the launch post. On Instagram add a Giveaway story highlight and keep the link sticker story in it.
- Bio line names the giveaway and the close date while it runs, then goes back to normal the day after.
- Turn on comment and DM notifications for the accounts that will post. Questions land in the first hour.
- Post the eligibility line and the close time in the caption of every giveaway post, so a screenshot still carries them.

## Feed balance

Giveaway posts are promotional content. Keep the rest of the feed running through the run: the giveaway is one post per push per channel plus stories, and the educational and behind-the-scenes posts continue on their usual days. A feed that turns into giveaway reminders for two weeks loses the followers the giveaway was meant to win.

## Hashtags and who they bring

Use the brand's own tags and one or two for the product category. Generic giveaway tags (#giveaway, #win, #competition) and contest directories bring people who enter giveaways as a hobby. They enter, they rarely subscribe, and the results review shows this as few email signups on traffic from those sources. If the objective is followers or a list, leave the generic tags off. If the objective is raw entry count for a partner, use them and expect the difference.

## Per channel

| Channel | Launch format | Mid-run format | Last call | Notes |
|---|---|---|---|---|
| Instagram | Carousel: Prize hero, how to enter, eligibility. Link in bio and in a story with the link sticker | Reel of the Prize in use, story poll about the Prize | Countdown sticker story, feed post with "closes tonight" and the time zone | Pin the launch post. Stories every second day. Use a Collab post for the partner push so it sits on both feeds. Do not require tagging in comments |
| TikTok | Short video: Prize reveal in the first second, entry steps on screen, link in bio | Creator or staff video using the Prize | Video with the close time on screen | Comments are where questions land, answer them |
| X | Post with the Prize image and link. Pin it | Quote-post with a detail about the Prize | Post with the close time, reply thread with FAQ | Ask for a repost as the share action, one account per person |
| Facebook | Page post with link, share to relevant groups you admin | Photo post, live if the Prize suits it | Event-style reminder post | Do not require timeline shares or friend tags to enter |
| YouTube | Mention at the top of the next video plus a pinned comment with the link, community post | Short showing the Prize | Community post with the close time | State that YouTube is not a sponsor in the rules |
| LinkedIn (B2B) | Post from a person, then the company page | Post about the partner or the cause | Reminder from the person | Prizes should suit a professional audience |
| Discord or Telegram | Announcement channel pin, role ping once | Reminder with a screenshot of entries so far | Final ping | One ping per push, no more |
| Email | Launch email | Mid email | Last call email, then Winners | See the email sequence reference |
| Website | Banner or bar with the deadline, entry page linked from the main nav for the run | Update the banner copy at the mid push | "Closes tonight" banner | Remove everything the day after the close |
| Store (Shopify and similar) | Announcement bar with the deadline, a giveaway page in the nav (the Gleam Shopify app creates one), a card on the collection the Prize came from | Order confirmation and thank-you page mention the giveaway, packing slip insert with the entry link | Announcement bar copy changes to the close time | Sync Entrants to the customer list with the campaign tag, so the store's own email flows can pick them up |

## Post template

Prize first, then the ask, then the deadline, then eligibility.

"Win [Prize] (worth [value]). To enter: [required action] and [one supporting action]. Refer a friend for [N] extra entries. Closes [date, time, time zone]. Open to [eligibility]. Link in bio."

Swap the first line at each push: mid run leads with a detail ("The [Prize] arrives in [feature]"), last call leads with the time ("Closes in 24 hours").

## Comments and DMs during the run

Answer in the first hour where you can, and pin one comment with the three questions everyone asks.

| Situation | Reply | Rule |
|---|---|---|
| "How do I enter" | "Link in bio, takes a minute: [action] and [action]. Closes [date, time zone]." | Pinned comment on every giveaway post, same wording |
| "Is this open in [country]" | "Open to [eligibility]. Sorry if that leaves you out this time." | Quote the eligibility line, never widen it in a comment |
| "Is this real" | "It is. Terms and the draw method are on the entry page: [link]." | Link, no argument |
| "I entered but got no confirmation" | "Check the address you used and the spam folder. If it is still missing, DM us the email and we will check the entry list." | Never post someone's email or entry details publicly |
| Fake account announcing Winners or DMing Entrants for a fee | Post and pin: "We contact Winners only from @[official handle] and [official email]. We never ask for payment, card details or a password. Report and block [fake handle]." Name the official handle, not "this account", the warning gets screenshotted and shared past the post it started on | Report the account to the platform, screenshot it, tell the Winner-communications step so the notification names the official account |
| "Rigged" or "same people always win" | "The draw is [method] from [N] valid entries and the record is at [link]. Happy to walk you through it." | Answer once with the record, then stop. The Winner-communications skill has the dispute reply |
| Abuse or spam | Hide or delete, block on repeat | Never delete questions or complaints, only abuse |
| Partner or creator asks to be tagged | Tag them in the next push and the Winner post | Keep to the brief |

Entrants who comment before they enter are the ones to answer first. A reply that lands while they are still on the post converts. Keep the thread going: a question answered publicly saves ten DMs.

## Where the traffic lands across the run

Extracted: typical share of a campaign's Impressions landing on each day since start, for campaigns run about 7, 14 and 30 days. Entries are not in this cut, so it tracks visits per day, not who entered that day.

| Duration | Day one | Peak day | Trough | Close |
|---|---|---|---|---|
| 7 days | 22% (6,148 campaigns, 1,795 businesses) | Day 1 | none, declines straight through | Day 6, 7% (6,002 campaigns, 1,778 businesses) |
| 14 days | 10% (4,851 campaigns, 1,828 businesses) | Day 1 | Day 10, 4.4% (5,173 campaigns, 1,919 businesses) | Day 13, 4.5% (4,663 campaigns, 1,770 businesses) |
| 30 days | 4.1% (7,176 campaigns, 1,988 businesses) | Day 2, 4.7% (7,558 campaigns, 2,049 businesses) | Days 17 to 21, about 2.3% (day 20: 8,094 campaigns, 2,167 businesses) | Day 29, 2.8% (6,672 campaigns, 1,860 businesses) |

Day one carries close to a quarter of a week-long campaign's total traffic and a tenth of a month-long one's. A week-long run falls every day straight through to the close, with no recovery. A two-week or month-long run falls hard through the first week or two, flattens into a long stretch at a quarter to a third of the launch share, and picks up a little in the final days. Both closes stay well under half the launch share.

| Duration | Launch peak | Quiet-stretch share of launch | Late-run uptick |
|---|---|---|---|
| 7 days | Day 1 | none, declines straight through | none |
| 14 days | Day 1 | a quarter to a third | day 13 a couple of points above day 10 |
| 30 days | Days 1-2 (a two-day peak) | a quarter to a third | day 29 about a fifth higher than its trough |

Source: `analysis/output/prize_timing_cuts.json` (`impression_curve_by_duration`).

Share clicks follow a tighter curve than Impressions: on a week-long run they peak on day 1 and day 2, then decay every day to the close. Impressions and shares both crest in the first two days, so the launch and second push carry both.

| Day | Share of total share clicks | Campaigns | Businesses |
|---|---|---|---|
| Day 1 | 18% | 6,380 | 1,727 |
| Day 2 | 17% | 7,666 | 1,923 |

Source: analysis/output/field_cuts.json (share_click_curve_by_duration).

## Turning the curve into pushes

- **Launch, day one.** The biggest traffic day at every length tested. Land the launch post and email inside the same two hours the campaign goes live.
- **Second push, while traffic is still falling.** A week-long run never settles into a flat stretch, so the second push slows a decline that is already underway.
- **The quiet middle.** Traffic sits at a quarter to a third of the launch share and barely moves day to day. A partner or creator post belongs here, to give the flat stretch something to move on.
- **The last days.** On a two-week or month-long run, traffic on the close reads a little above the quiet middle by itself. On a week-long run it does not, the decline runs straight to the end. In every case the close stays a fraction of the launch share, so the last-call post, email and countdown sticker go out on schedule regardless. The close is not going to fill itself in.

| Duration | Second push | Quiet middle |
|---|---|---|
| 7 days | day 3 to 4 | none, declines straight through |
| 14 days | day 4 to 6 | days 10 to 13 |
| 30 days | day 5 to 8 | days 15 to 26 |

## Fourteen-day calendar

A worked example for a two-week run on Instagram plus email, with a partner on day 8. Shift the dates to the timing plan.

| Day | Push | Feed | Story | Email | Other |
|---|---|---|---|---|---|
| -1 | Prep | Pin ready | Highlight created | Segment built, link tested | Bio link set, partner brief sent |
| 1 | Launch | Carousel: Prize, how to enter, eligibility | Link sticker, "just launched" | Launch email within two hours | Pin the post, answer comments for the first hour |
| 2 | - | Usual content | Poll about the Prize | - | - |
| 3 | - | Usual content | Link sticker reminder | - | - |
| 5 | Mid | Reel of the Prize in use | Entries so far, referral reward | Mid email | - |
| 6 | - | Usual content | Question sticker, answer three | - | - |
| 8 | Partner | Collab post with the partner (appears on both feeds) | Repost the partner's story | - | Partner posts in their morning |
| 10 | - | Usual content | Link sticker reminder | - | - |
| 12 | - | Usual content | Countdown sticker set to the close | - | - |
| 13 | Last call | "Closes tomorrow" feed post with the time zone | Countdown reminder | Last call email | - |
| 14 | Close | - | "Closing in [hours]" story at the audience's peak hour | - | Take the banner down the day after |
| 15 to 21 | Draw | Winner post, once the Winner has agreed | Winner story, tag the partner | Winners email | Bio back to normal, highlight stays |

Three feed posts and one collab in fourteen days, with stories carrying the reminders. The feed stays a feed.

## Social figures to record

Write these down at launch, at close and 30 days after close, from the platform's own insights, and hand them to the results review:

- Follower count on each promoted channel. The 30-day figure shows how many follow-to-enter followers stayed.
- Reach and saves on the launch post against your typical post from the previous month.
- Link clicks from the bio link and from each story sticker, and the UTM totals from the entry page.
- Comments answered and the typical time to first reply on the launch post.

None of this is in the campaign dataset, which counts entries and Impressions on the entry page only. The comparison is against your own previous posts.

## Partner and creator brief

One page, sent a week before their date.

- What: one post and one story on [date], plus a repost of the Winner announcement.
- Copy and assets: attached, editable, keep the link and the eligibility line.
- Link: the entry page with their UTM or code, so they can see what they drove.
- What they get: named as the Prize partner on the entry page and in every email, entries data if agreed, product.
- Timing: post between [hours] in their audience's time zone. Tell us when it is live.
- Rules: no purchase claims, no changes to eligibility, disclose the partnership where required.

## Paid

- Schedule organic first. Paid amplifies a plan, it does not replace one.
- Boost the launch post only, to people who look like the email list or the channel's engaged followers, and to the regions in the eligibility line.
- Cap the spend at the cost of one more Winner. If the campaign is producing leads, cost per Entrant against the value of a lead decides whether to add more.
- Never run paid to audiences outside eligibility. Wasted spend and angry Entrants.
- Add a UTM to every link you post, on every channel, paid and organic. Source is the network, medium is the format (post, story, email, partner), campaign is the giveaway name. Without it the results review has traffic sources and no way to separate your posts from a partner's.
- A store with Shopify Audiences or the equivalent can build the retargeting audience from the tagged customer segment without an export.
- After the close, upload the Entrant list as a custom audience on the networks you run ads on. Exclude the Winners and anyone already a customer, then run the launch offer to the rest. Practice, with no dataset figure behind it: the dataset holds no purchase data.
- Build a lookalike audience from that same Entrant list for the next campaign's launch push. Entrants opted in to a Prize, so a lookalike of them is a prospecting audience and should be judged on cost per lead against your usual sources.

## Afterwards

- Announce Winners on every channel used to promote, within a week.
- Thank everyone and give them something small: a code, a guide, early access to the next drop.
- Ask Winners for a photo and use it only with permission.
- Save the creative that got the most entries for every 100 Impressions for the next campaign, and tag the new subscribers with the campaign name so their behaviour can be compared later.
- The non-Winner series and the list hygiene pass that follows it belong to giveaway-winner-communications. Point the plan there and leave the copy to that skill.
