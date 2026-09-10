# Cost benchmarks and ROI

From the campaigns behind these numbers (35,614 campaigns, 6,394 businesses). Cost figures use the stated USD Prize pool, which is what businesses wrote and the only cost the dataset holds. Real cost is usually lower (own product at cost, sponsored Prizes) and promotion spend is invisible, so treat these as stated value per result. The industry names below fold homepage labels into the ten names this skill uses throughout (gaming is gaming_esports, technology is electronics_tech, fashion_beauty is apparel_fashion, beauty_personal_care and jewelry_watches, and so on). Every figure describes campaigns that reached 1,000 Entrants. Reproduce with `analysis/roi_benchmarks.py`.

## By industry

| Industry | Campaigns | Businesses | Stated pool USD | Share of Entrants | Per email signup | Per follow | Per referral entry | Emails per campaign | Follows per campaign | Conversion Rate (the share of people who saw it and entered) |
|---|---|---|---|---|---|---|---|---|---|---|
| Technology | 7,236 | 1,032 | 1,000 | 39 | 0.44 | 0.35 | 1.66 | 1,719 | 2,975 | 29% |
| Gaming | 6,294 | 1,409 | 836 | 27 | 0.48 | 0.26 | 1.45 | 1,586 | 2,690 | 27% |
| Music and media | 5,223 | 654 | 500 | 17 | 0.15 | 0.15 | 1.76 | 2,244 | 1,815 | 26% |
| Fitness and outdoor | 3,147 | 738 | 1,000 | 39 | 0.41 | 0.72 | 1.99 | 2,152 | 1,023 | 24% |
| Fashion and beauty | 2,175 | 487 | 1,000 | 30 | 0.30 | 0.59 | 2.61 | 2,399 | 1,303 | 31% |
| Food and drink | 1,785 | 419 | 750 | 26 | 0.34 | 0.55 | 2.07 | 1,985 | 1,133 | 29% |
| Home | 1,774 | 328 | 850 | 32 | 0.36 | 0.66 | 2.81 | 1,864 | 1,148 | 31% |
| Kids, family, pets | 1,662 | 350 | 600 | 28 | 0.30 | 0.45 | 3.13 | 1,570 | 1,146 | 27% |
| Travel and events | 1,347 | 261 | 1,156 | 46 | 0.46 | 1.99 | 4.65 | 2,573 | 816 | 29% |
| Software | 548 | 163 | 1,600 | 68 | 0.71 | 0.74 | 3.42 | 2,143 | 2,190 | 26% |

Music and media buys addresses and follows cheapest, typically 0.15 USD for both. Software pays the most per email signup (0.71), and travel and events pays the most per referral entry (4.65).

## Which industries get the most from a giveaway

Crowd per Prize dollar is Entrants against the typical for the stated Prize cost, 1.00 being typical for the money. Email uptake is email signups recorded divided by the campaign's Entrants, so 100% means very nearly everyone who entered signed up, and a figure over 100% means some Entrants signed up more than once. Conversion Rate here is the typical figure among the campaigns we can compare fairly (no repeatable action, run of 14 days or less), a narrower and higher-converting scope than the industry table's full-population Conversion Rate above, so the two are separate figures under similar names. Repeat business means five or more campaigns in the dataset.

[All the campaigns behind these numbers: crowd per Prize dollar 1.00 (typical for the money), Conversion Rate 38%, email uptake 98%, referrals 12% of Entrants, repeat businesses 78%.]

| Industry | Campaigns | Entrants | Conversion Rate | Email uptake | Referrals % of Entrants | Crowd per Prize dollar (valued campaigns) | For the money | Stated USD % of Entrants | Repeat businesses | Own product Prize |
|---|---|---|---|---|---|---|---|---|---|---|
| Music and media | 5,223 | 2,072 | 33% | 101% | 10 | 1.23 (2,133) | 23% above typical | 17 | 87% | 8% |
| Gaming | 6,294 | 2,198 | 37% | 76% | 14 | 1.07 (2,000) | 7% above typical | 27 | 74% | 14% |
| Food and drink | 1,785 | 2,399 | 36% | 88% | 11 | 1.05 (867) | 5% above typical | 26 | 70% | 32% |
| Home | 1,774 | 2,231 | 40% | 90% | 11 | 0.98 (1,016) | 2% below typical | 32 | 79% | 27% |
| Travel and events | 1,347 | 2,736 | 36% | 101% | 9 | 0.97 (455) | 3% below typical | 46 | 76% | 33% |
| Fashion and beauty | 2,175 | 2,440 | 36% | 102% | 12 | 0.95 (895) | 5% below typical | 30 | 72% | 25% |
| Fitness and outdoor | 3,147 | 2,251 | 35% | 100% | 16 | 0.94 (1,516) | 6% below typical | 39 | 71% | 26% |
| Technology | 7,236 | 2,261 | 43% | 84% | 20 | 0.91 (2,345) | 9% below typical | 39 | 84% | 32% |
| Kids, family, pets | 1,662 | 1,825 | 31% | 100% | 11 | 0.89 (524) | 11% below typical | 28 | 73% | 32% |
| Software | 548 | 1,990 | 31% | 102% | 21 | 0.84 (308) | 16% below typical | 68 | 62% | 20% |

Music and media gets the most for its money (23% above typical on crowd per Prize dollar), buys the cheapest Entrants and addresses, and has the most repeat businesses. Gaming holds the second-highest figure, with the most Actions per campaign, Twitch and Discord audiences, and the lowest email uptake of the ten. Software has the highest referral rate and sits lowest on crowd per Prize dollar. Every row is a proxy industry from a homepage label, and none of it says an industry causes a result.

## By industry

The ten industry names above fold several homepage labels each. The individual labels behind the largest ten, same scope and cost figures as the industry table above:

| Industry (raw label) | Campaigns | Businesses | Stated pool USD | Share of Entrants | Per email signup | Per follow | Conversion Rate |
|---|---|---|---|---|---|---|---|
| Electronics and tech | 7,236 | 1,032 | 1,000 | 39 | 0.44 | 0.35 | 29% |
| Gaming and esports | 6,294 | 1,409 | 836 | 27 | 0.48 | 0.26 | 27% |
| Media and entertainment | 5,014 | 592 | 500 | 17 | 0.15 | 0.15 | 26% |
| Sports and outdoors | 2,264 | 536 | 1,000 | 39 | 0.40 | 0.70 | 24% |
| Food and drink | 1,785 | 419 | 750 | 26 | 0.34 | 0.55 | 29% |
| Home and garden | 1,774 | 328 | 850 | 32 | 0.36 | 0.66 | 31% |
| Apparel and fashion | 1,715 | 321 | 1,000 | 31 | 0.29 | 0.67 | 31% |
| Travel and events | 1,347 | 261 | 1,156 | 46 | 0.46 | 1.99 | 29% |
| Automotive | 1,124 | 142 | 1,725 | 32 | 0.26 | 0.51 | 23% |
| Toys, hobbies, collectibles | 985 | 201 | 500 | 24 | 0.28 | 0.42 | 26% |

Electronics and tech is the largest label behind the technology industry name, and gaming and esports behind gaming on its own with no other label folded in. Automotive, the largest label with no dedicated industry name of its own, pays the most typically (1,725 USD) and has the lowest Conversion Rate of the ten (23%).

## Industries

Homepage labels read from each business's own site, across the campaigns behind these numbers: crypto businesses, and the earlier crypto, ambiguous and purchase-opportunity campaigns, are excluded, the same scope as the rest of this repository's default figures. Finance and crypto remains the largest single industry outside this scope, matching `references/evidence-and-limitations.md`. The ten largest industries by campaign count:

| Industry | Campaigns | Businesses | Typical Entrants | Conversion Rate | Actions per Entrant | Days | Methods | Email offered |
|---|---|---|---|---|---|---|---|---|
| Electronics and tech | 7,289 | 1,037 | 2,259 | 30% | 4.93 | 15 | 7 | 24% |
| Gaming and esports | 6,328 | 1,414 | 2,197 | 27% | 5.17 | 14 | 9 | 21% |
| Media and entertainment | 5,019 | 594 | 2,054 | 26% | 4.52 | 22 | 7 | 65% |
| Sports and outdoors | 2,268 | 537 | 2,466 | 24% | 4.40 | 22 | 7 | 56% |
| Food and drink | 1,787 | 419 | 2,399 | 29% | 3.54 | 18 | 6 | 63% |
| Home and garden | 1,777 | 328 | 2,237 | 31% | 3.81 | 16 | 7 | 59% |
| Apparel and fashion | 1,717 | 321 | 2,635 | 31% | 2.71 | 8 | 4 | 74% |
| Travel and events | 1,347 | 261 | 2,736 | 29% | 3.01 | 23 | 6 | 57% |
| Automotive | 1,124 | 142 | 2,776 | 23% | 6.40 | 18 | 10 | 68% |
| Toys, hobbies and collectibles | 989 | 202 | 1,832 | 26% | 3.55 | 20 | 6 | 43% |

Home and garden and apparel and fashion have the highest Conversion Rate among the largest industries (both 31%), apparel and fashion also offers email most often (74%), and automotive asks for the most Entry Methods (10). Reproduce with `analysis/industries.py`.

By business type, on the same scope:

| Business type | Campaigns | Businesses | Typical Entrants | Conversion Rate | Actions per Entrant | Days | Methods | Email offered |
|---|---|---|---|---|---|---|---|---|
| Brand | 10,870 | 2,439 | 2,127 | 26% | 4.46 | 17 | 8 | 52% |
| Retailer | 7,769 | 974 | 2,417 | 29% | 4.21 | 15 | 7 | 50% |
| Media publisher | 4,997 | 584 | 2,006 | 28% | 4.10 | 21 | 6 | 54% |
| Creator | 3,930 | 962 | 2,297 | 38% | 4.17 | 14 | 6 | 8% |
| Software | 3,814 | 641 | 2,457 | 23% | 4.85 | 22 | 10 | 41% |
| Other | 1,548 | 324 | 1,933 | 29% | 5.47 | 18 | 8 | 31% |
| Service business | 1,056 | 237 | 2,208 | 28% | 3.11 | 16 | 7 | 42% |
| Agency | 863 | 131 | 2,265 | 29% | 4.86 | 15 | 8 | 35% |
| Community | 461 | 171 | 1,899 | 28% | 5.45 | 14 | 9 | 17% |
| Nonprofit | 259 | 89 | 2,070 | 28% | 2.98 | 28 | 7 | 41% |

Creators have the highest Conversion Rate (38%), rarely offer email (8%), and run the shortest campaigns (14 days, tied with community). Nonprofits run the longest (28 days).

Source: `analysis/output/prize_timing_cuts.json` (by_industry_ordinary, by_business_type_ordinary), `analysis/output/industries.json` (vertical_mapping).

## By campaign size

| Campaign size | Campaigns | Stated pool USD | Share of Entrants | Per email signup | Per follow | Emails per campaign |
|---|---|---|---|---|---|---|
| 1k-2.5k | 19,911 | 519 | 35 | 0.39 | 0.46 | 1,344 |
| 2.5k-10k | 12,582 | 1,299 | 29 | 0.28 | 0.37 | 3,703 |
| 10k+ | 3,121 | 3,000 | 14 | 0.16 | 0.19 | 16,419 |

Bigger campaigns pay less per result on the stated figure, and they also have the audiences that make them big. A first campaign should budget against the 1,000 to 2,500 Entrant row.

## By start year

| Year | Campaigns | Entrants | Conversion Rate | Actions | Stated pool USD |
|---|---|---|---|---|---|
| 2020 | 454 | 2,679 | 27% | 8 | 1,077 |
| 2021 | 8,749 | 2,470 | 30% | 7 | 688 |
| 2022 | 7,600 | 2,220 | 30% | 7 | 860 |
| 2023 | 6,125 | 2,166 | 27% | 7 | 1,000 |
| 2024 | 5,088 | 2,121 | 24% | 7 | 1,077 |
| 2025 | 5,031 | 2,064 | 26% | 8 | 885 |
| 2026 | 2,531 | 2,027 | 28% | 8 | 802 |

Typical Entrant counts have drifted down since 2021 while Conversion Rate has held near 24% to 30%. Benchmarks from the whole export sit a little above what a campaign started this year would typically see.

## Using the ROI script

`scripts/roi.py` prices a campaign before or after it runs. Give it what the Prizes cost you, the stated value you advertise, promotion and admin spend, and either expected Entrants (with the actions you will offer) or the actual counts of emails, follows and referrals. It prints cost per result, stated value per result beside the benchmark for the industry or campaign size, and either the return per dollar on the per-unit values you supply or the breakeven value per email.

Value per email is the business's number: expected revenue per subscriber over the period they care about, or the price of the same list from another channel. Say so in the answer and never invent one. A breakeven figure with no value attached is still useful: "each address has to be worth 0.79 USD" is a question the business can answer.

## Reading cost per asset as acquisition cost

Cost per email signup or per follow is the giveaway's customer acquisition cost for that asset. It belongs beside what the team already pays for the same thing elsewhere: cost per lead on paid search, cost per follower on paid social, the rate an affiliate or a list rental charges. A giveaway that buys addresses at 0.39 USD is cheap or dear only against that internal number, and the team has it.

The other half is what the asset is worth. Set a window the business can measure, 90 days after the campaign closes being the usual one, and ask what a new subscriber or follower converts to inside it: orders placed, revenue attributed, a trial started. That figure is the lifetime value the acquisition cost is judged against, and it is the business's to supply. The dataset holds none of it, so it can price what a giveaway captured and never what the capture was worth.

Two habits keep the comparison honest. Compare a giveaway list with a paid list, since both are cold. And measure the giveaway group separately in the email tool for those 90 days, because a giveaway group behaves nothing like people who found the business on their own.

## What ROI the dataset cannot show

Revenue, purchases, unsubscribes, unfollows and list quality are not in the dataset. The figures above price participation and the assets captured at the moment of entry. A follow that lapses in a week cost the same as one that stays.
