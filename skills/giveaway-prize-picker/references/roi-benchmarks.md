# Cost benchmarks and ROI

Extracted from the ordinary segment of the export (37,123 campaigns). Cost figures use the stated USD prize pool, which is what organizers wrote and the only cost the export holds. Real cost is usually lower (own product at cost, sponsored prizes) and promotion spend is invisible, so treat these as stated value per result. Verticals are a regex on names. Every figure describes campaigns that reached 1,000 entrants. Reproduce with `analysis/roi_benchmarks.py`.

## By vertical

| Vertical | n | Stated pool USD | Per contestant | Per email signup | Per follow | Per referral entry | Emails per campaign | Follows per campaign | Contestants per impression |
|---|---|---|---|---|---|---|---|---|---|
| Gaming | 6,503 | 1,088 | 0.29 | 0.29 | 0.21 | 2.08 | 2,315 | 3,720 | 26% |
| Technology | 1,717 | 1,038 | 0.38 | 0.40 | 0.53 | 1.28 | 2,079 | 2,133 | 26% |
| Travel and events | 1,758 | 1,497 | 0.48 | 0.50 | 1.15 | 4.90 | 2,505 | 1,170 | 25% |
| Music and media | 1,006 | 420 | 0.21 | 0.14 | 0.48 | 2.15 | 2,311 | 1,217 | 26% |
| Food and drink | 989 | 550 | 0.26 | 0.31 | 0.54 | 2.16 | 1,880 | 968 | 31% |
| Home | 883 | 900 | 0.33 | 0.38 | 0.52 | 2.20 | 1,945 | 1,535 | 31% |
| Fitness and outdoor | 878 | 1,434 | 0.46 | 0.43 | 0.91 | 3.99 | 3,032 | 1,231 | 27% |
| Kids, family, pets | 660 | 999 | 0.39 | 0.43 | 0.68 | 3.64 | 1,903 | 1,156 | 29% |
| Fashion and beauty | 359 | 1,000 | 0.29 | 0.37 | 0.54 | 2.82 | 1,956 | 1,417 | 32% |
| Software | 349 | 1,187 | 0.46 | 0.41 | 0.55 | 4.29 | 1,766 | 1,801 | 26% |

Music and media buys addresses cheapest at the median, travel and events dearest. Gaming buys follows cheapest because Twitch and X follows run high there. Fitness and software pay the most per referral entry.

## By campaign size

| Band | n | Stated pool USD | Per contestant | Per email signup | Per follow | Emails per campaign |
|---|---|---|---|---|---|---|
| 1k-2.5k | 20,839 | 529 | 0.36 | 0.39 | 0.44 | 1,346 |
| 2.5k-10k | 13,074 | 1,299 | 0.29 | 0.29 | 0.35 | 3,703 |
| 10k+ | 3,210 | 3,000 | 0.14 | 0.16 | 0.18 | 16,344 |

Bigger campaigns pay less per result on the stated figure, and they also have the audiences that make them big. A first campaign should budget against the 1k to 2.5k row.

## By start year

| Year | n | Contestants | Contestants per impression | Actions | Stated pool USD |
|---|---|---|---|---|---|
| 2020 | 461 | 2,685 | 27% | 8 | 1,076 |
| 2021 | 9,127 | 2,438 | 30% | 7 | 700 |
| 2022 | 8,161 | 2,201 | 30% | 7 | 899 |
| 2023 | 6,356 | 2,164 | 27% | 7 | 1,000 |
| 2024 | 5,262 | 2,117 | 24% | 7 | 1,037 |
| 2025 | 5,202 | 2,058 | 26% | 8 | 850 |
| 2026 | 2,516 | 2,060 | 27% | 8 | 809 |

Median contestants have drifted down since 2021 while conversion has held near 27% to 30%. Benchmarks from the whole export sit a little above what a campaign started this year would see at the median.

## Using the ROI script

`scripts/roi.py` prices a campaign before or after it runs. Give it what the prizes cost you, the stated value you advertise, promotion and admin spend, and either expected contestants (with the actions you will offer) or the actual counts of emails, follows and referrals. It prints cost per result, stated value per result beside the benchmark for the vertical or band, and either the return per dollar on the per-unit values you supply or the breakeven value per email.

Value per email is the organizer's number: expected revenue per subscriber over the period they care about, or the price of the same list from another channel. Say so in the answer and never invent one. A breakeven figure with no value attached is still useful: "each address has to be worth 0.79 USD" is a question the business can answer.

## What ROI the export cannot show

Revenue, purchases, unsubscribes, unfollows and list quality are not in the export. The figures above price participation and the assets captured at the moment of entry. A follow that lapses in a week cost the same as one that stays.
