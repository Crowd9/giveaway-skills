# Holiday benchmarks and calendar

Built from the campaigns behind these numbers (116,499 campaigns). A campaign counts for a holiday when its title, incentive name or the first part of its description names it, so the rows are business-declared themes. Lead days is the holiday date minus the start date, for campaigns that started inside the 120 days before it. The Conversion Rate here is from the campaigns we can compare fairly (no repeatable action, 14 days or less). The typical range given is the middle half of campaigns, from the lower quarter to the upper quarter. Every figure describes what businesses chose.

Baseline for comparison across this page. The typical campaign draws 492 Entrants over 14 days, across 116,283 campaigns from 17,603 businesses. Read every Conversion Rate column on this page against 34.5%, the typical figure among the campaigns we can compare fairly, because those columns are counted on that group and carry its campaign count in brackets. The all-campaign Conversion Rate is 26.9%, lower because Impressions count once per visitor per day and a long run collects more of them for the same crowd. The public-holiday table below reads 492 Entrants for every other start across 90,764 campaigns, which is the same baseline arrived at on this page's own data.

These figures were wrong on this page until the benchmark floor moved from 1,000 Entrants to 100. Anything comparing a theme with the typical figure is measured against the numbers above, so check them against the generated tables before trusting a sentence that says above or below.

## By holiday

<!-- generated:hol_by_holiday -->
| Theme | Campaigns | Entrants | Conversion Rate (fair-comparison count) | Entries per Entrant | Duration days | Lead days, typical (range) | Closed on or before the day | Start months |
|---|---|---|---|---|---|---|---|---|
| Christmas and advent | 4,895 | 587 | 39% (2,165) | 4.1 | 10 | 17 (9 to 26) | 75% | Dec, Nov |
| Summer | 3,085 | 623 | 32% (869) | 4.3 | 16 | 27 (10 to 43) | 61% | Jun, Jul |
| New Year | 931 | 774 | 31% (278) | 4.6 | 16 | 11 (4 to 25) | 42% | Jan, Dec |
| Halloween | 837 | 482 | 29% (268) | 4.9 | 14 | 18 (8 to 30) | 52% | Oct, Sep |
| Black Friday and Cyber Monday | 747 | 898 | 30% (360) | 3.8 | 8 | 7 (3 to 14) | 40% | Nov, Dec |
| Valentine's Day | 682 | 550 | 30% (228) | 4.9 | 14 | 13 (6 to 21) | 49% | Feb, Jan |
| Back to school | 477 | 876 | 32% (151) | 3.9 | 14 | 18.5 (10 to 27) | 52% | Aug, Jul |
| Easter | 449 | 605 | 30% (170) | 5.1 | 13 | 10 (4 to 21) | 38% | Mar, Apr |
| Mother's Day | 367 | 601 | 30% (144) | 3.4 | 11 | 12 (6 to 21) | 55% | Apr, May |
| Father's Day | 329 | 823 | 35% (131) | 3.9 | 12 | 12 (7 to 18) | 43% | Jun, May |
| Thanksgiving | 264 | 718 | 27% (87) | 4.6 | 12 | 14 (7 to 24) | 47% | Nov, Oct |
| Lunar New Year | 108 | 584 | 34% (46) | 5.1 | 13 | 5 (1 to 10) | 20% | Feb, Jan |
<!-- /generated -->

Reading it:

- Christmas and advent beats the all-campaign typical figures on both Entrants and Conversion Rate, on 4,895 campaigns, and Father's Day is the only other theme to do the same, on 329. It launches a typical 17 days out and 75% close on or before the day. Three in ten use a repeatable action, the advent calendar shape.
- Every theme except Halloween sits above the typical figure on Entrants, with Black Friday and Cyber Monday at 898 and back to school at 876 the largest. Halloween at 482 is the only one below it.
- Black Friday campaigns are short (8 days) and launch 7 days out. Family days launch about two weeks out and run about two weeks. Back to school launches about two and a half weeks out.
- Roughly half of campaigns for a dated holiday close after the day. A Prize that only makes sense before the day (a gift for Mother's Day) needs a close a week before it, which is the minority pattern.
- For most themes (see the "Closed on or before the day" column above), the majority run through the date and close after it. Those campaigns use the holiday as a hook for attention while people are already looking, and they keep collecting entries through the days around it, when a Christmas campaign would already have drawn. Read a close after the day as the default for those themes, and a close before it as the exception a gift-timed Prize forces.
- Anniversary, birthday and milestone campaigns sit close to the all-campaign typical figures and run all year, so they are a hook to use when the calendar offers nothing.

## Holiday theme against no theme, and how early businesses launch

A separate check, using all runs at their actual length, not the fair-comparison set the table above uses. The all-run JSON comparison records 26.9% entering for campaigns naming no holiday (104,762 campaigns, 16,503 businesses). Its theme definitions differ from the generated fair-comparison rows below. Against that baseline:

<!-- generated:hol_theme -->
| Theme | Campaigns | Businesses | Entrants | Conversion Rate |
|---|---|---|---|---|
| Christmas and advent | 4,895 | 1,559 | 587 | 39.1% |
| Father's Day | 329 | 234 | 823 | 34.7% |
| Lunar New Year | 108 | 81 | 584 | 33.8% |
| Milestone | 1,159 | 765 | 527 | 32.5% |
| Summer | 3,085 | 1,347 | 623 | 32.0% |
| Back to school | 477 | 284 | 876 | 31.8% |
| New Year | 931 | 627 | 774 | 31.3% |
| Anniversary or birthday | 2,187 | 1,151 | 600 | 31.0% |
| Valentine's Day | 682 | 397 | 550 | 30.5% |
| Black Friday and Cyber Monday | 747 | 380 | 898 | 30.5% |
| Mother's Day | 367 | 286 | 601 | 29.8% |
| Easter | 449 | 269 | 605 | 29.6% |
| Halloween | 837 | 508 | 482 | 28.8% |
| Thanksgiving | 264 | 182 | 718 | 27.4% |
| Prime Day and Singles Day | 99 | 60 | 794 | 27.1% |
<!-- /generated -->

In the all-run JSON comparison, Christmas clears the no-theme baseline by 4.7 points, Father's Day by 3.4 and Mother's Day by 1.7. Milestone also sits above it, while Thanksgiving and Prime Day trail it by about three points. These comparisons use `analysis/output/prize_timing_cuts.json` (`by_named_holiday`), across actual run lengths with repeatable actions included. The generated table above retains the separate fair-comparison figures.

Lead time, days before the holiday date businesses started, for campaigns matched to a specific date:

<!-- generated:hol_lead -->
| Theme | Campaigns with a lead figure | Lower quarter | Typical | Upper quarter |
|---|---|---|---|---|
| Summer | 1,628 | 10 days | 27 days | 43 days |
| Back to school | 322 | 10 days | 18.5 days | 27 days |
| Halloween | 776 | 8 days | 18 days | 30 days |
| Christmas and advent | 4,593 | 9 days | 17 days | 26 days |
| Thanksgiving | 251 | 7 days | 14 days | 24 days |
| Valentine's Day | 655 | 6 days | 13 days | 21 days |
| Mother's Day | 361 | 6 days | 12 days | 21 days |
| Father's Day | 292 | 7 days | 12 days | 18 days |
| New Year | 434 | 4 days | 11 days | 25 days |
| Easter | 429 | 4 days | 10 days | 21 days |
| Black Friday and Cyber Monday | 648 | 3 days | 7 days | 14 days |
| Lunar New Year | 76 | 1 day | 5 days | 10 days |
<!-- /generated -->

Black Friday launches closest to its date, a typical 7 days out. Halloween launches furthest ahead of the fixed dates most businesses use, a typical 18 days out, just ahead of Christmas at 17. These lead figures use `analysis/output/holidays.json` (`holidays`), matching the table above. Summer and back to school have no single calendar date behind them, so a share of the lower-quarter figure already sits past the reference point used to measure lead time.

Starting near a public holiday, on its own, does not move the numbers (table below). Both gaps sit under a point.

<!-- generated:hol_public -->
| Start | Entrants | Conversion Rate | Campaigns | Businesses |
|---|---|---|---|---|
| Every other start | 492 | 27.0% | 90,764 | 15,452 |
| Started within 3 days of a public holiday (the organizer's own country) | 493 | 26.4% | 25,705 | 7,125 |
<!-- /generated -->

Source: `analysis/output/prize_timing_cuts.json` (`by_named_holiday`, `holiday_lead_days`, `by_public_holiday_start`).

## Calendar with launch windows

Dates for the next sixteen months. The launch window is the holiday date minus the typical range of lead days businesses used, and the typical launch is the midpoint of that range. Dates for Mother's Day and Father's Day are the US convention (second Sunday in May, third Sunday in June). The UK Mother's Day is the fourth Sunday of Lent and Australia's Father's Day is the first Sunday of September, so shift those for those audiences. Diwali and Lunar New Year dates are entered by hand for each year.

<!-- generated:hol_calendar -->
| Holiday | Date | Launch window | Typical launch | What that week looked like |
|---|---|---|---|---|
| Halloween | Sat 31 Oct 2026 | 01 Oct to 23 Oct | 12 Oct | Halloween week: 2% of starts, 33% entered |
| Thanksgiving | Thu 26 Nov 2026 | 02 Nov to 19 Nov | 10 Nov | Thanksgiving week: 3% of starts, 35% entered |
| Black Friday and Cyber Monday | Fri 27 Nov 2026 | 13 Nov to 24 Nov | 18 Nov | Black Friday and Cyber Monday week: 3% of starts, 35% entered |
| Christmas and advent | Fri 25 Dec 2026 | 29 Nov to 16 Dec | 07 Dec | Christmas and advent week: 1% of starts, 37% entered |
| New Year | Fri 01 Jan 2027 | 07 Dec to 28 Dec | 17 Dec | - |
| Lunar New Year | Sat 06 Feb 2027 | 27 Jan to 05 Feb | 31 Jan | Lunar New Year week: 2% of starts, 33% entered |
| Valentine's Day | Sun 14 Feb 2027 | 24 Jan to 08 Feb | 31 Jan | Valentine's Day week: 2% of starts, 33% entered |
| Easter | Sun 28 Mar 2027 | 07 Mar to 24 Mar | 15 Mar | Easter week: 2% of starts, 35% entered |
| Mother's Day | Sun 09 May 2027 | 18 Apr to 03 May | 25 Apr | Mother's Day week: 2% of starts, 33% entered |
| Father's Day | Sun 20 Jun 2027 | 02 Jun to 13 Jun | 07 Jun | Father's Day week: 2% of starts, 34% entered |
| Back to school | Wed 25 Aug 2027 | 29 Jul to 15 Aug | 06 Aug | Back to school week: 2% of starts, 33% entered |
| Halloween | Sun 31 Oct 2027 | 01 Oct to 23 Oct | 12 Oct | Halloween week: 2% of starts, 33% entered |
| Thanksgiving | Thu 25 Nov 2027 | 01 Nov to 18 Nov | 09 Nov | Thanksgiving week: 2% of starts, 33% entered |
| Black Friday and Cyber Monday | Fri 26 Nov 2027 | 12 Nov to 23 Nov | 17 Nov | Black Friday and Cyber Monday week: 2% of starts, 33% entered |
| Christmas and advent | Sat 25 Dec 2027 | 29 Nov to 16 Dec | 07 Dec | Christmas and advent week: 2% of starts, 41% entered |
| New Year | Sat 01 Jan 2028 | 07 Dec to 28 Dec | 17 Dec | New Year week: 1% of starts, 37% entered |
<!-- /generated -->

The last column names the holiday's own row in the weekly table, never a week number. Week numbers move between years, and this calendar carries both 2026 and 2027 dates, so citing one by number pointed three rows at the wrong week and quoted the wrong figures with them.

Prime Day, Singles' Day, anniversaries and milestones have no fixed date here, so use the theme row above for their shape. Ramadan and Eid have no theme row, only the counts under "Smaller and obscure dates" below. The region calendar in `calendar-by-region.md` gives the dates that stall a team or an audience.

## The season plan for a store

Four dates decide a store's fourth quarter, and the data gives each a shape. Dates below are 2026, the 2027 rows in the calendar move them a day.

Common practice, our data doesn't cover this. For a store building its sale email list, close the giveaway before the sale and leave time to draw and contact Winners. For a US audience, close by the Wednesday before Thanksgiving so the team can handle the draw before the holiday. Other objectives, including an advent launch, can use 27 to 30 November when the audience and team are available. Campaigns live over that weekend recorded an 11% lower Conversion Rate than matched campaigns in the comparison above. That association is a tradeoff to consider, not a reason to reject a requested launch date. The December window below remains an option for those objectives.

| Slot | Window (2026) | What the data says | What the giveaway does for the store |
|---|---|---|---|
| Pre-sale list build | Launch 13 to 24 Nov, close by 25 Nov for a US audience (the day before Thanksgiving) | Black Friday campaigns run 8 days and launch 7 days out (648 campaigns with a lead figure). Campaigns live over Black Friday record an 11% lower Conversion Rate than matched campaigns (Cyber Monday alone 10% fewer), and week 47, the week before Thanksgiving, sits at 33% entered, a point above the year's quietest weeks | Build the list that receives the sale. Close with time for the draw before the sale, contact Winners, then send the sale email to the segment whose recorded consent covers it |
| The sale itself | 27 to 30 Nov | Week 48, Thanksgiving and Black Friday week, holds 3% of starts at 35% entered and week 49, the first week of December, 40% | For a pre-sale list build, use this period for sale emails. For an advent or other objective, a live giveaway is an option if the team can support it and the audience has a reason to enter |
| December | Launch 27 Nov to 14 Dec, 6 Dec typical | Christmas and advent sits above the typical figures on both Entrants and Conversion Rate, and the two weeks before Christmas get the most to enter of any week in the data (figures just below this table). Advent calendars: 602.5 Entrants, 44% entered, six days, six actions | For a pre-sale list plan, launch after the sale period. For a separate advent objective, the window can overlap the sale. Advent or 12 days with a product a day, or one hero Prize from the gift guide, closing before the shipping cutoff so the Winner has it by the day |
| Shipping cutoff | Set by the carrier, usually mid December for domestic | 75% of Christmas campaigns close on or before the day | The Prize ships as an order through the store with tracking. Close the draw a week before the cutoff, or make the Prize a gift card |
| New Year | Launch 9 to 27 Dec, 20 Dec typical | New Year campaigns run 16 days at 31% entered (931 campaigns), and being live over Christmas or New Year came with about the same share entering as matched campaigns, at ratios of 0.99 and 0.98, the two best of any holiday in the table | The restart campaign for the January customer: resolutions, restock, the product that pairs with what they bought in December |

<!-- generated:hol_december -->
Christmas and advent sits above the typical figures on both Entrants (587) and Conversion Rate (39%) on 4,895 campaigns, and weeks 50 and 51, the two weeks before Christmas, get the most to enter of any week in the data at 41% each (1,381 and 1,193 fair-comparison campaigns), with week 49, the first week of December, just behind at 40% on the largest count (1,562).
<!-- /generated -->

The pre-sale list plan separates list building from sale emails. A different objective can justify overlap. December is crowded (about a quarter again a typical month on starts) and has high observed completion. Choose the window around the audience, team capacity and delivery cutoff. A cohort average describes the observed campaigns and leaves that scheduling decision open.

The no-penalty part is not unique to December: across all the campaigns behind these numbers, the busiest quarter of calendar weeks by volume converts a little better than the quietest quarter, not worse (table below). The source does not provide a separate pooled Conversion Rate for the busiest weeks outside the holiday peak, so it cannot isolate how much of the difference comes from holiday weeks.

| Quarter of weeks | Conversion Rate | Campaigns | Businesses |
|---|---|---|---|
| Busiest quarter | 36.3% | 11,947 | unavailable |
| Quietest quarter | 33.9% | 8,235 | unavailable |

All three industries we break out show the same pattern (table below), though both quarters mix in some holiday weeks. Electronics and tech has the widest gap and gaming and esports the smallest. The source does not isolate the holiday-week contribution.

| Industry | Busiest quarter CR | Quietest quarter CR | Busiest (campaigns / businesses) | Quietest (campaigns / businesses) |
|---|---|---|---|---|
| Electronics and tech | 44.0% | 39.0% | 1,931 / unavailable | 1,192 / unavailable |
| Gaming and esports | 35.1% | 33.4% | 2,880 / unavailable | 2,121 / unavailable |
| Media and entertainment | 33.7% | 30.6% | 1,581 / unavailable | 1,111 / unavailable |

These comparisons do not show that a busy launch week reduces conversion. Holiday timing and industry remain part of the comparison. Source: `analysis/output/calendar.json` (`seasonal_crowding`). Counts beside Conversion Rate cover the fair-comparison campaigns (`clean_n`), whose business counts are unavailable. Campaigns outside that subset do not contribute to the rate.

Prime Day and Singles Day draw 794 Entrants, well above the typical figure, on the lowest Conversion Rate of any theme in the table above at 27.1%. The share of week 46 starts naming any holiday is below, from `analysis/output/calendar_names.json` (`holiday_named_share_by_week.46`). This does not isolate Singles Day. Mother's Day and Father's Day launch about two weeks out and run two weeks. For a store the family days are gift days, so the gift guide shape applies.

| Date | Week | Share of that week's starts naming it |
|---|---|---|
| Any named holiday | 46 (11 Nov) | 20% |

Source for the advent-calendar row above: `analysis/output/campaign_types.json` (`types`, Advent or daily calendar).

## Every week of the year (extracted)

All the campaigns behind these numbers, by the calendar week of their start date, whatever their theme. Share of starts is that week's share of all 116,283 campaigns (an even spread would be 1.9%). Conversion Rate is from the campaigns we can compare fairly. The holiday-named column is the share of that week's starts whose title or description names a holiday, which is how the dates and the names were checked against each other. Monday dates are 2026.

<!-- generated:hol_weeks -->
| Week | Monday | Share of starts | Entrants | Conversion Rate (fair-comparison count) | Entries per Entrant | Holiday-named | Holidays in the week |
|---|---|---|---|---|---|---|---|
| 1 | 29 Dec | 1% | 512 | 38% (438) | 4.3 | 17% | - |
| 2 | 05 Jan | 1% | 537 | 33% (441) | 4.4 | 11% | - |
| 3 | 12 Jan | 2% | 453 | 35% (627) | 4.2 | 12% | - |
| 4 | 19 Jan | 2% | 473 | 33% (654) | 4.3 | 10% | - |
| 5 | 26 Jan | 2% | 468 | 33% (810) | 4.5 | 12% | - |
| 6 | 02 Feb | 2% | 475 | 33% (772) | 4.2 | 11% | Super Bowl (US) |
| 7 | 09 Feb | 2% | 482 | 34% (838) | 4.3 | 9% | Valentine's Day |
| 8 | 16 Feb | 2% | 496 | 36% (683) | 4.3 | 5% | Lunar New Year |
| 9 | 23 Feb | 3% | 474 | 36% (809) | 4.7 | 6% | - |
| 10 | 02 Mar | 2% | 457 | 35% (737) | 4.5 | 6% | - |
| 11 | 09 Mar | 2% | 478 | 33% (855) | 4.5 | 7% | - |
| 12 | 16 Mar | 2% | 500 | 35% (760) | 4.4 | 7% | - |
| 13 | 23 Mar | 2% | 484 | 36% (770) | 4.6 | 8% | - |
| 14 | 30 Mar | 2% | 480 | 36% (792) | 4.5 | 9% | Easter |
| 15 | 06 Apr | 2% | 438 | 36% (757) | 4.4 | 7% | - |
| 16 | 13 Apr | 2% | 486 | 33% (819) | 4.4 | 8% | - |
| 17 | 20 Apr | 2% | 480 | 35% (728) | 4.5 | 8% | - |
| 18 | 27 Apr | 2% | 480 | 33% (764) | 4.4 | 10% | - |
| 19 | 04 May | 2% | 470 | 34% (765) | 4.3 | 12% | Mother's Day |
| 20 | 11 May | 2% | 490 | 34% (749) | 4.4 | 10% | - |
| 21 | 18 May | 2% | 442 | 36% (745) | 4.5 | 14% | - |
| 22 | 25 May | 2% | 471 | 34% (764) | 4.5 | 12% | - |
| 23 | 01 Jun | 2% | 533 | 35% (787) | 4.3 | 15% | - |
| 24 | 08 Jun | 2% | 496 | 34% (777) | 4.3 | 15% | - |
| 25 | 15 Jun | 2% | 488 | 33% (734) | 4.4 | 17% | Father's Day |
| 26 | 22 Jun | 2% | 490 | 34% (708) | 4.6 | 14% | - |
| 27 | 29 Jun | 2% | 534 | 34% (626) | 4.4 | 13% | Independence Day (US) |
| 28 | 06 Jul | 2% | 500 | 35% (646) | 4.2 | 14% | Prime Day (mid July, varies) |
| 29 | 13 Jul | 2% | 518 | 33% (749) | 4.3 | 14% | - |
| 30 | 20 Jul | 2% | 459 | 35% (619) | 4.3 | 12% | - |
| 31 | 27 Jul | 2% | 507 | 33% (627) | 4.5 | 11% | - |
| 32 | 03 Aug | 2% | 467 | 34% (666) | 4.3 | 13% | - |
| 33 | 10 Aug | 2% | 511 | 33% (709) | 4.2 | 13% | - |
| 34 | 17 Aug | 2% | 525 | 33% (755) | 4.3 | 10% | - |
| 35 | 24 Aug | 2% | 515 | 35% (683) | 4.6 | 9% | Back to school |
| 36 | 31 Aug | 2% | 502 | 33% (577) | 4.4 | 7% | - |
| 37 | 07 Sep | 2% | 485 | 32% (666) | 4.4 | 7% | - |
| 38 | 14 Sep | 2% | 493 | 33% (689) | 4.3 | 6% | - |
| 39 | 21 Sep | 2% | 493 | 33% (640) | 4.5 | 9% | - |
| 40 | 28 Sep | 2% | 489 | 35% (652) | 4.3 | 11% | - |
| 41 | 05 Oct | 2% | 480 | 34% (696) | 4.4 | 15% | - |
| 42 | 12 Oct | 2% | 447 | 32% (736) | 4.3 | 15% | - |
| 43 | 19 Oct | 2% | 472 | 33% (746) | 4.2 | 15% | - |
| 44 | 26 Oct | 2% | 514 | 33% (727) | 4.6 | 16% | Halloween |
| 45 | 02 Nov | 2% | 471 | 35% (772) | 4.3 | 16% | Diwali |
| 46 | 09 Nov | 2% | 438 | 34% (776) | 4.4 | 20% | Singles Day |
| 47 | 16 Nov | 2% | 491 | 33% (845) | 4.6 | 26% | - |
| 48 | 23 Nov | 3% | 510 | 35% (1,040) | 4.5 | 28% | Black Friday and Cyber Monday, Thanksgiving |
| 49 | 30 Nov | 3% | 557 | 40% (1,562) | 4.1 | 32% | Cyber Monday |
| 50 | 07 Dec | 3% | 572 | 41% (1,381) | 4.2 | 34% | - |
| 51 | 14 Dec | 2% | 567 | 41% (1,193) | 4.2 | 36% | - |
| 52 | 21 Dec | 1% | 558 | 37% (591) | 4.3 | 26% | Christmas and advent |
<!-- /generated -->

Reading it:

- Weeks 48 to 51, late November to mid December, are the launch peak, and they get the most people to enter of any stretch in the year (table above). About a third of those starts name a holiday. Week 52, Christmas week itself, drops back down on both share of starts and Conversion Rate.

| Week | Share of starts (rounded) |
|---|---|
| 48 to 51 | 2.2% to 2.9% each |
| 52 | 1.3% |

- Week 49, the first week of December, has the largest fair-comparison count in the peak stretch. Week 51, the week before Christmas, converts higher still on a smaller count (table above). The advent shape runs through both, and so do plain December campaigns.

- Two clusters stand out from the year's weekly pattern, one high and one low, neither with a holiday attached (table below).

<!-- generated:hol_week_extremes -->
| Weeks | Roughly when | Conversion Rate |
|---|---|---|
| 50, 51 | weeks beginning 07 Dec, 14 Dec | 41% each |
| 37, 42 | weeks beginning 07 Sep, 12 Oct | 32% each |

- Entrants vary little by week. Week 50 is the highest at 572 and weeks 15 and 46 the lowest at 438, a spread narrow enough that no week is worth choosing for it alone.
<!-- /generated -->
- Start day of the month makes no difference: the first week of the month and the last get within a point of each other on Conversion Rate.

## Live over a holiday (extracted)

Campaigns whose run included the holiday date, against campaigns that did not, drawn with the same duration mix so a 45-day campaign is compared with 45-day campaigns. Closed on the day is the count that ended exactly on the holiday.

<!-- generated:hol_liveover -->
| Holiday | Live over it, campaigns | Entrants | Conversion Rate | Not over it, Entrants | Conversion Rate | Entrant ratio | Conversion Rate ratio |
|---|---|---|---|---|---|---|---|
| Black Friday and Cyber Monday | 8,419 | 531 | 29% | 552 | 33% | 0.96 | 0.89 |
| Thanksgiving | 8,394 | 535 | 30% | 552 | 33% | 0.97 | 0.91 |
| Cyber Monday | 8,360 | 529 | 29% | 554 | 32% | 0.95 | 0.90 |
| Halloween | 7,937 | 545 | 30% | 559 | 32% | 0.97 | 0.94 |
| Christmas and advent | 7,862 | 558 | 31% | 548 | 32% | 1.02 | 0.99 |
| Singles Day | 7,814 | 544 | 30% | 550 | 32% | 0.99 | 0.94 |
| Diwali | 7,676 | 546 | 30% | 553 | 32% | 0.99 | 0.93 |
| Father's Day | 7,599 | 566 | 30% | 546 | 32% | 1.04 | 0.95 |
| Back to school | 7,506 | 597 | 28% | 552 | 33% | 1.08 | 0.87 |
| Prime Day (mid July, varies) | 7,400 | 561 | 30% | 553 | 32% | 1.01 | 0.93 |
| Easter | 7,391 | 557 | 30% | 545 | 32% | 1.02 | 0.92 |
| Independence Day (US) | 7,224 | 568 | 30% | 552 | 32% | 1.03 | 0.94 |
| Valentine's Day | 7,194 | 543 | 31% | 538 | 32% | 1.01 | 0.95 |
| Mother's Day | 7,181 | 549 | 30% | 552 | 32% | 0.99 | 0.91 |
| Lunar New Year | 7,076 | 549 | 31% | 542 | 32% | 1.01 | 0.96 |
| Super Bowl (US) | 7,014 | 536 | 30% | 539 | 32% | 0.99 | 0.93 |
| New Year | 6,444 | 576 | 30% | 559 | 31% | 1.03 | 0.98 |
<!-- /generated -->

Reading it:

<!-- generated:hol2_liveover_notes -->
- Being live over Christmas or New Year came with about the same share entering as the same-length campaigns that were not, within 1% for Christmas and 2% for New Year. Every other holiday came with fewer entering, and the two furthest back were Back to school at 13% lower and Black Friday and Cyber Monday at 11% lower. Those are weeks when the audience is being sold to from every direction.
- Entrant counts do not move much with any holiday: every ratio sits between 0.95 and 1.08. A holiday does not add Entrants. It changes how many of the people who arrive decide to enter.
- Closing on the holiday itself is rare (247 to 703 campaigns per holiday that any campaign closed on) and those campaigns look like the rest.
<!-- /generated -->

## Names against dates

For most holidays, most campaigns naming it start within 60 days before the date and end within 14 days after it (table below). New Year is the exception: about half of New Year-named campaigns start in January, after the date, which a before-the-date window does not count, so "new year" shows up in titles and descriptions about as often after 1 January as before it. Back to school and Lunar New Year also run under 70%, both tied to a picked date, not a single day everyone marks the same way.

<!-- generated:hol2_name_date -->
| Holiday | Share started 60 days before to 14 days after | Campaigns |
|---|---|---|
| Christmas and advent | 84% | 4,986 |
| New Year | 39% | 955 |
| Black Friday and Cyber Monday | 83% | 755 |
| Thanksgiving | 90% | 266 |
| Halloween | 84% | 852 |
| Valentine's Day | 83% | 690 |
| Mother's Day | 85% | 367 |
| Father's Day | 81% | 329 |
| Easter | 86% | 459 |
| Back to school | 57% | 479 |
| Lunar New Year | 58% | 110 |
<!-- /generated -->

Source: `analysis/output/calendar_names.json` (`name_date_agreement`).

## Smaller and obscure dates (extracted)

Smaller themes and narrow matches, showing campaigns, typical Entrants and the months they started. Under 50 campaigns the typical figure is a rough read. Start-month buckets are omitted where needed to protect small groups, including cells that would reveal them by subtraction. A dash means no months remain available.

<!-- generated:hol_smaller -->
| Theme | Campaigns | Entrants | Start months |
|---|---|---|---|
| Halloween (narrow match) | 769 | 485 | Oct and Sep |
| Wedding season | 249 | 408 | Jan and Mar |
| Pride | 189 | 380 | Jun and May |
| New Year's resolutions | 173 | 1,168 | Jan and Dec |
| National days | 158 | 918 | Aug and Jan |
| Independence Day (US) | 138 | 708 | Jun and Jul |
| World days | 113 | 456 | Mar and Dec |
| St Patrick's Day | 109 | 591 | Mar |
| World Cup | 88 | 457 | Jun and Nov |
| Gamescom, E3, Summer Game Fest, The Game Awards | 87 | 742 | Aug and Dec |
| Earth Day | 72 | 1,102 | Apr |
| Amazon Prime Day | 70 | 946 | Jul and Jun |
| Labor Day (US) | 69 | 925 | Aug and Sep |
| Carnival | 50 | 468 | Feb and Mar |
| International Women's Day | 46 | 308 | - |
| March Madness | 46 | 474 | Mar |
| Chinese or Lunar New Year | 35 | 538 | Feb |
| Super Bowl | 32 | 821 | Feb and Jan |
| April Fools | 29 | 1,296 | Apr |
| Canada Day | 28 | 1,916 | - |
| Diwali | 27 | 1,008 | Oct |
| Galentine's Day | 25 | 990 | Feb |
| Stocking stuffers | 20 | 296 | Nov and Dec |
| Ramadan or Eid | 18 | 550 | Mar |
| Cinco de Mayo | 15 | 437 | Apr and May |
| Oktoberfest | 15 | 335 | Sep |
| Midsummer | 13 | 726 | Jun |
| Boxing Day | 10 | 980 | - |
| Hanukkah | 9 | 468 | - |
| Day of the Dead | 7 | 609 | - |
| Pi Day | 6 | 894 | Mar |
| Holi | 5 | 2,547 | - |
<!-- /generated -->

Individual named days below the five-business privacy floor are omitted from the campaign analysis. The National days and World days rows combine broader themes. A named day can provide a relevant hook, but these aggregate rows do not establish how much competition a specific date has.

Dates for the ones with a fixed or predictable day:

| Date | When |
|---|---|
| International Women's Day | Sun 08 Mar 2026 and Mon 08 Mar 2027 |
| St Patrick's Day | Tue 17 Mar 2026 and Wed 17 Mar 2027 |
| March Madness | mid March to early April |
| Earth Day | Wed 22 Apr 2026 and Thu 22 Apr 2027 |
| Star Wars Day | Mon 04 May 2026 and Tue 04 May 2027 |
| Canada Day | Wed 01 Jul 2026 and Thu 01 Jul 2027 |
| Independence Day (US) | Sat 04 Jul 2026 and Sun 04 Jul 2027 |
| Amazon Prime Day | mid July, announced by Amazon each year |
| World Photography Day | Wed 19 Aug 2026 |
| National Dog Day | Wed 26 Aug 2026 |
| Labor Day (US) | Mon 07 Sep 2026 |
| National Coffee Day | Tue 29 Sep 2026 in the US, Thu 01 Oct 2026 internationally |
| Super Bowl | Sun 14 Feb 2027, the same day as Valentine's |


The smaller themes below meet the five-business privacy floor. Their typical Entrant counts are rough comparisons on small samples. Every count below comes from one definition, generated with the rest of this page.

<!-- generated:smaller_named -->
| Theme | Campaigns | Businesses | Typical Entrants | Busiest start months |
|---|---|---|---|---|
| Diwali | 27 | 11 | 1,008 | Oct (19) |
| Carnival | 50 | 34 | 468 | Feb (18), Mar (6) |
| Ramadan or Eid | 18 | 12 | 550 | Mar (8) |
| Galentine's Day | 25 | 14 | 990 | Feb (17) |
| Cinco de Mayo | 15 | 12 | 437 | Apr (9), May (6) |
| Oktoberfest | 15 | 11 | 335 | Sep (9) |
| Midsummer | 13 | 11 | 726 | Jun (6) |
| Boxing Day | 10 | 8 | 980 | - |
| Hanukkah | 9 | 6 | 468 | - |
| Day of the Dead | 7 | 5 | 609 | - |
| Pi Day | 6 | 5 | 894 | Mar (6) |
| Holi | 5 | 5 | 2,547 | - |

Matched on the campaign title, the Prize name and the description, across the campaigns these benchmarks describe. Below the five-business floor and so not published: Juneteenth, Giving Tuesday, Small Business Saturday, Australia Day, Eurovision, Black History Month, Bonfire Night, Movember, Bastille Day, Grandparents Day.
<!-- /generated --> Diwali also appears in the week and live-over tables above, which place it by its date and not by its wording. Matches include the campaign title, Prize name and description. These counts describe the matching campaigns in the dataset and do not measure all competition for attention around a date.
