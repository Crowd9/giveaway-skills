# Holiday benchmarks and calendar

Extracted from the ordinary segment (37,123 campaigns). A campaign counts for a holiday when its title, incentive name or the first part of its description names it, so the rows are organizer-declared themes. Lead days is the holiday date minus the start date, for campaigns that started inside the 120 days before it. Conversion is the clean subset (no repeatable action, 14 days or less). Every figure describes what organizers chose. Reproduce with `analysis/holidays.py`.

All ordinary campaigns for comparison: 2,203 contestants, 38% clean conversion, 4.3 entries per entrant, 16 days.

## By holiday

| Theme | n | Contestants | Conversion (clean n) | Entries per entrant | Duration days | Lead days, median (IQR) | Closed on or before the day | Start months |
|---|---|---|---|---|---|---|---|---|
| Christmas and advent | 1,806 | 2,424 | 44% (857) | 3.9 | 10 | 19 (11 to 28) | 78% | Dec, Nov |
| New Year | 411 | 2,390 | 34% (112) | 4.9 | 19 | 11 (5 to 23) | 34% | Jan, Dec |
| Black Friday and Cyber Monday | 364 | 2,241 | 35% (181) | 3.8 | 8 | 8 (3 to 16) | 46% | Nov, Dec |
| Thanksgiving | 111 | 2,324 | 35% (22) | 5.0 | 15 | 17 (9 to 27) | 50% | Nov, Oct |
| Halloween | 256 | 2,008 | 30% (72) | 5.1 | 18 | 19 (7 to 30) | 38% | Oct, Sep |
| Valentine's Day | 223 | 1,952 | 39% (69) | 4.3 | 14 | 12 (6 to 19) | 40% | Feb, Jan |
| Mother's Day | 141 | 1,692 | 37% (42) | 3.8 | 12 | 13 (7 to 24) | 53% | Apr, May |
| Father's Day | 155 | 2,058 | 37% (50) | 4.0 | 14 | 13 (9 to 19) | 34% | Jun, May |
| Easter | 157 | 1,999 | 32% (56) | 4.8 | 14 | 10 (4 to 21) | 41% | Mar, Apr |
| Back to school | 211 | 2,209 | 34% (59) | 4.2 | 14 | 21 (11 to 33) | 55% | Aug, Jul |
| Summer | 1,181 | 2,465 | 36% (291) | 4.0 | 18 | 28 (14 to 47) | 59% | Jun, Jul |
| Lunar New Year | 40 | 2,114 | 34% (17) | 4.1 | 10 | 5 (1 to 7) | 19% | Feb, Jan |
| Prime Day and Singles Day | 43 | 1,802 | 23% (21) | 4.5 | 11 | - | - | Jul, Jun |
| Anniversary or birthday | 815 | 2,323 | 33% (265) | 4.2 | 14 | - | - | Jun, May |
| Milestone | 408 | 2,109 | 34% (110) | 4.5 | 18 | - | - | Jul, Aug |

Reading it:

- Christmas and advent is the only theme that beats the all-campaign medians on both contestants and conversion, on 1,806 campaigns. It launches a median 19 days out and 78% close on or before the day. Three in ten use a repeatable action, the advent calendar shape.
- Summer, New Year, Black Friday, Thanksgiving and back to school sit at or above the median on contestants. Halloween, Valentine's, Mother's Day, Father's Day and Easter sit below, on small samples.
- Black Friday campaigns are short (8 days) and launch 8 days out. Family days launch about two weeks out and run about two weeks. Back to school launches three weeks out.
- Roughly half of campaigns for a dated holiday close after the day. A prize that only makes sense before the day (a gift for Mother's Day) needs a close a week before it, which is the minority pattern.
- Anniversary, birthday and milestone campaigns match the all-campaign medians and run all year, so they are a hook to use when the calendar offers nothing.

## Calendar with launch windows

Dates for the next sixteen months. The launch window is the holiday date minus the interquartile range of lead days organizers used, and the typical launch is the median. Dates for Mother's Day and Father's Day are the US convention (second Sunday in May, third Sunday in June). The UK Mother's Day is the fourth Sunday of Lent and Australia's Father's Day is the first Sunday of September, so shift those for those audiences. Diwali and Lunar New Year dates are entered by hand for each year.

| Holiday | Date | Launch window | Typical launch | That week in the data |
|---|---|---|---|---|
| Halloween | Sat 31 Oct 2026 | 01 Oct to 24 Oct | 12 Oct | week 44: 2% of starts, 37% conversion |
| Thanksgiving | Thu 26 Nov 2026 | 30 Oct to 17 Nov | 09 Nov | week 48: 3% of starts, 40% conversion |
| Black Friday and Cyber Monday | Fri 27 Nov 2026 | 11 Nov to 24 Nov | 19 Nov | week 48: 3% of starts, 40% conversion |
| Christmas and advent | Fri 25 Dec 2026 | 27 Nov to 14 Dec | 06 Dec | week 52: 1% of starts, 41% conversion |
| New Year | Fri 01 Jan 2027 | 09 Dec to 27 Dec | 21 Dec | - |
| Lunar New Year | Mon 01 Feb 2027 | 25 Jan to 31 Jan | 27 Jan | week 5: 2% of starts, 34% conversion |
| Valentine's Day | Sun 14 Feb 2027 | 26 Jan to 08 Feb | 02 Feb | week 6: 2% of starts, 33% conversion |
| Easter | Sun 28 Mar 2027 | 07 Mar to 24 Mar | 18 Mar | week 12: 2% of starts, 33% conversion |
| Mother's Day | Sun 09 May 2027 | 15 Apr to 02 May | 26 Apr | week 18: 2% of starts, 38% conversion |
| Father's Day | Sun 20 Jun 2027 | 01 Jun to 11 Jun | 07 Jun | week 24: 2% of starts, 37% conversion |
| Back to school | Wed 25 Aug 2027 | 23 Jul to 14 Aug | 04 Aug | week 34: 2% of starts, 37% conversion |
| Halloween | Sun 31 Oct 2027 | 01 Oct to 24 Oct | 12 Oct | week 43: 2% of starts, 36% conversion |
| Thanksgiving | Thu 25 Nov 2027 | 29 Oct to 16 Nov | 08 Nov | week 47: 2% of starts, 33% conversion |
| Black Friday and Cyber Monday | Fri 26 Nov 2027 | 10 Nov to 23 Nov | 18 Nov | week 47: 2% of starts, 33% conversion |
| Christmas and advent | Sat 25 Dec 2027 | 27 Nov to 14 Dec | 06 Dec | week 51: 3% of starts, 53% conversion |
| New Year | Sat 01 Jan 2028 | 09 Dec to 27 Dec | 21 Dec | week 52: 1% of starts, 41% conversion |

Ramadan and Eid, Prime Day, Singles' Day, anniversaries and milestones have no fixed date here. Use the theme row above for their shape and the region calendar in `calendar-by-region.md` for the dates that stall a team or an audience.

## Every week of the year (extracted)

All ordinary campaigns by the ISO week of their start date, whatever their theme. Share of starts is that week's share of all 37,123 campaigns (an even spread would be 1.9%). Conversion is the clean subset. The holiday-named column is the share of that week's starts whose title or description names a holiday, which is how the dates and the names were checked against each other. Monday dates are 2026.

| Week | Monday | Share of starts | Contestants | Conversion (clean n) | Entries per entrant | Holiday-named | Holidays in the week |
|---|---|---|---|---|---|---|---|
| 1 | 29 Dec | 1% | 2,072 | 36% (131) | 4.4 | 19% |  |
| 2 | 05 Jan | 1% | 2,244 | 34% (135) | 4.6 | 12% |  |
| 3 | 12 Jan | 1% | 2,178 | 33% (150) | 4.4 | 10% |  |
| 4 | 19 Jan | 2% | 2,163 | 35% (197) | 4.5 | 8% |  |
| 5 | 26 Jan | 2% | 2,146 | 34% (216) | 4.4 | 13% |  |
| 6 | 02 Feb | 2% | 2,250 | 33% (201) | 4.3 | 10% | Super Bowl (US) |
| 7 | 09 Feb | 2% | 2,202 | 35% (212) | 4.3 | 7% | Valentine's Day |
| 8 | 16 Feb | 2% | 2,149 | 37% (178) | 4.2 | 2% | Lunar New Year |
| 9 | 23 Feb | 3% | 2,305 | 38% (222) | 4.6 | 2% |  |
| 10 | 02 Mar | 2% | 2,184 | 38% (198) | 4.3 | 3% |  |
| 11 | 09 Mar | 2% | 2,169 | 37% (217) | 4.5 | 3% |  |
| 12 | 16 Mar | 2% | 2,160 | 33% (211) | 4.3 | 5% |  |
| 13 | 23 Mar | 2% | 2,146 | 36% (208) | 4.6 | 6% |  |
| 14 | 30 Mar | 2% | 2,220 | 36% (212) | 4.4 | 6% | Easter |
| 15 | 06 Apr | 2% | 2,017 | 35% (202) | 4.4 | 4% |  |
| 16 | 13 Apr | 2% | 2,268 | 37% (236) | 4.4 | 4% |  |
| 17 | 20 Apr | 2% | 2,074 | 38% (187) | 4.7 | 5% |  |
| 18 | 27 Apr | 2% | 2,160 | 38% (185) | 4.2 | 4% |  |
| 19 | 04 May | 2% | 2,196 | 37% (212) | 4.0 | 5% | Mother's Day |
| 20 | 11 May | 2% | 2,228 | 40% (201) | 4.3 | 2% |  |
| 21 | 18 May | 2% | 2,212 | 42% (205) | 4.5 | 2% |  |
| 22 | 25 May | 2% | 2,222 | 38% (232) | 4.5 | 4% |  |
| 23 | 01 Jun | 2% | 2,224 | 36% (222) | 4.4 | 7% |  |
| 24 | 08 Jun | 2% | 2,076 | 37% (224) | 4.3 | 4% |  |
| 25 | 15 Jun | 2% | 2,268 | 35% (210) | 4.4 | 2% | Father's Day |
| 26 | 22 Jun | 2% | 2,240 | 37% (222) | 4.7 | 2% |  |
| 27 | 29 Jun | 2% | 2,293 | 33% (167) | 4.3 | 2% | Independence Day (US) |
| 28 | 06 Jul | 2% | 2,062 | 37% (171) | 4.4 | 3% | Prime Day (mid July, varies) |
| 29 | 13 Jul | 2% | 2,273 | 37% (188) | 4.3 | 5% |  |
| 30 | 20 Jul | 2% | 2,190 | 37% (171) | 4.6 | 4% |  |
| 31 | 27 Jul | 2% | 2,102 | 36% (188) | 4.5 | 4% |  |
| 32 | 03 Aug | 2% | 2,239 | 38% (198) | 4.5 | 6% |  |
| 33 | 10 Aug | 2% | 2,210 | 38% (205) | 4.6 | 5% |  |
| 34 | 17 Aug | 2% | 2,409 | 37% (230) | 4.5 | 5% |  |
| 35 | 24 Aug | 2% | 2,193 | 38% (233) | 4.4 | 6% | Back to school |
| 36 | 31 Aug | 2% | 2,188 | 34% (161) | 4.6 | 4% |  |
| 37 | 07 Sep | 2% | 2,275 | 33% (202) | 4.2 | 4% |  |
| 38 | 14 Sep | 2% | 2,228 | 37% (230) | 4.4 | 3% |  |
| 39 | 21 Sep | 2% | 2,226 | 38% (164) | 4.4 | 5% |  |
| 40 | 28 Sep | 2% | 2,099 | 38% (182) | 4.3 | 7% |  |
| 41 | 05 Oct | 2% | 2,162 | 37% (219) | 4.0 | 10% |  |
| 42 | 12 Oct | 2% | 2,008 | 33% (195) | 4.2 | 12% |  |
| 43 | 19 Oct | 2% | 2,005 | 36% (218) | 4.2 | 14% |  |
| 44 | 26 Oct | 2% | 2,092 | 37% (172) | 4.4 | 16% | Halloween |
| 45 | 02 Nov | 2% | 2,180 | 35% (192) | 4.3 | 18% | Diwali |
| 46 | 09 Nov | 2% | 2,094 | 35% (219) | 4.4 | 22% | Singles Day |
| 47 | 16 Nov | 2% | 2,306 | 33% (285) | 4.3 | 32% |  |
| 48 | 23 Nov | 3% | 2,491 | 40% (402) | 4.2 | 35% | Black Friday and Cyber Monday, Thanksgiving |
| 49 | 30 Nov | 3% | 2,372 | 46% (615) | 3.9 | 33% | Cyber Monday |
| 50 | 07 Dec | 3% | 2,240 | 47% (526) | 4.1 | 34% |  |
| 51 | 14 Dec | 3% | 2,234 | 53% (493) | 3.9 | 32% |  |
| 52 | 21 Dec | 1% | 2,375 | 41% (196) | 4.4 | 23% | Christmas and advent |

Reading it:

- Weeks 48 to 51, late November to mid December, are the launch peak at 2.6% to 3.3% of starts each, and they convert best: 40%, 46%, 47%, 53% against 38% for the year. A third of those starts name a holiday. Week 52, Christmas week itself, drops to 1.4% of starts and 41%.
- Week 49, the first week of December, is the single best week in the data on conversion with a large clean sample (615). The advent shape runs through it, and so do plain December campaigns.
- Weeks 20 and 21, mid to late May, convert at 40% and 42% with no holiday attached. Weeks 12, 27, 37, 42 and 47 sit at 33%, the low end. Week 47, the week before Thanksgiving, is the quiet before the peak.
- Contestants barely move by week. Week 34 (late August, back to school) is the high at 2,409, weeks 42 and 43 the low near 2,000.
- Start day of the month makes no difference: the first week of the month and the last convert within a point of each other.

## Live over a holiday (extracted)

Campaigns whose run included the holiday date, against campaigns that did not, drawn with the same duration mix so a 45-day campaign is compared with 45-day campaigns. Closed on the day is the count that ended exactly on the holiday.

| Holiday | Live over it, n | Contestants | Conversion | Not over it, contestants | Conversion | Contestant ratio | Conversion ratio | Closed on the day |
|---|---|---|---|---|---|---|---|---|
| Christmas and advent | 2,874 | 2,335 | 36% | 2,288 | 34% | 1.02 | 1.07 | 148 |
| New Year | 2,405 | 2,335 | 36% | 2,316 | 33% | 1.01 | 1.08 | 0 |
| Black Friday and Cyber Monday | 2,866 | 2,256 | 31% | 2,292 | 36% | 0.98 | 0.85 | 144 |
| Thanksgiving | 2,851 | 2,254 | 31% | 2,300 | 36% | 0.98 | 0.87 | 110 |
| Halloween | 2,798 | 2,236 | 33% | 2,313 | 35% | 0.97 | 0.96 | 228 |
| Valentine's Day | 2,507 | 2,235 | 31% | 2,303 | 34% | 0.97 | 0.93 | 106 |
| Mother's Day | 2,578 | 2,348 | 32% | 2,290 | 35% | 1.03 | 0.93 | 96 |
| Father's Day | 2,781 | 2,316 | 31% | 2,293 | 34% | 1.01 | 0.89 | 90 |
| Easter | 2,671 | 2,292 | 33% | 2,302 | 34% | 1.00 | 0.97 | 115 |
| Back to school | 2,794 | 2,442 | 30% | 2,291 | 35% | 1.07 | 0.88 | 92 |
| Diwali | 2,706 | 2,263 | 32% | 2,311 | 35% | 0.98 | 0.91 | 152 |
| Lunar New Year | 2,470 | 2,281 | 31% | 2,304 | 34% | 0.99 | 0.92 | 134 |
| Prime Day (mid July, varies) | 2,655 | 2,356 | 31% | 2,296 | 34% | 1.03 | 0.92 | 67 |
| Cyber Monday | 2,821 | 2,280 | 33% | 2,294 | 35% | 0.99 | 0.93 | 181 |
| Singles Day | 2,706 | 2,238 | 30% | 2,309 | 34% | 0.97 | 0.88 | 91 |
| Independence Day (US) | 2,627 | 2,351 | 31% | 2,302 | 34% | 1.02 | 0.90 | 77 |
| Super Bowl (US) | 2,425 | 2,245 | 31% | 2,303 | 34% | 0.97 | 0.92 | 63 |

Reading it:

- Being live over Christmas or New Year came with 7% to 8% better conversion than the same-length campaigns that were not. Every other holiday came with the same or lower conversion, and Black Friday, Thanksgiving, back to school and Singles Day sat 12% to 15% lower. Those are weeks when the audience is being sold to from every direction.
- Contestant counts do not move with any holiday: every ratio sits between 0.97 and 1.07. A holiday does not add entrants. It changes how many of the people who arrive decide to enter.
- Closing on the holiday itself is rare (60 to 230 campaigns per holiday) and those campaigns look like the rest.

## Names against dates

For each holiday, the share of campaigns naming it that started in the 60 days before it and ended no more than 14 days after it: Christmas and advent 67% of 1,806, New Year 95% of 411, Black Friday and Cyber Monday 97% of 364, Thanksgiving 80% of 111, Halloween 80% of 256, Valentine's Day 97% of 223, Mother's Day 90% of 141, Father's Day 90% of 155, Easter 90% of 157, Back to school 84% of 211, Lunar New Year 82% of 40. Names and dates agree for nearly every holiday. Christmas is the exception at 67% because a third of Christmas-named campaigns are advent runs that finish on 24 December, "Christmas in July" campaigns, or January runs still carrying the word.

## Smaller and obscure dates (extracted)

Themes that fewer than 100 campaigns named, so the shape only: campaigns, median contestants and the months they started. Under 50 campaigns a median is a rough read.

| Theme | Campaigns | Contestants | Start months |
|---|---|---|---|
| Halloween (also in the main table) | 230 | 2,008 | October |
| New Year's resolutions | 82 | 2,365 | January |
| National days (National Coffee Day, National Sticker Day, National Dog Day and so on) | 71 | 1,808 | August and September |
| Independence Day (US) | 63 | 2,739 | June and July |
| Wedding season | 58 | 2,372 | January and April |
| St Patrick's Day | 44 | 2,362 | March |
| Earth Day | 38 | 1,915 | April |
| Labor Day (US) | 36 | 1,754 | August |
| Gamescom, E3, Summer Game Fest, The Game Awards | 35 | 2,419 | August and December |
| Amazon Prime Day | 33 | 1,686 | June and July |
| World days (World Photography Day, World Book Day, World Sleep Day) | 31 | 2,453 | August and March |
| Chinese or Lunar New Year | 31 | 2,274 | February |
| World Cup | 29 | 1,862 | June |
| Stocking stuffers | 26 | 1,875 | December |
| International Women's Day | 23 | 2,014 | March |
| March Madness | 19 | 2,582 | March |
| Super Bowl | 17 | 3,160 | February |
| April Fools | 17 | 1,671 | April |
| Canada Day | 16 | 4,774 | June |

Named days that organizers used, with the campaign count: National Coffee Day 19, World Photography Day 15, National Sticker Day 13, National 811 Day 13, National Candy Day 9, National Camera Day 8, National Dog Day 7, World Sleep Day 7, World Book Day 7, National Peanut Day 6, National Knife Day 6, National Handwriting Day 6, World Friendship Day 6, World Music Day 6, International Youth Day 6. Most are one brand's annual habit (a sticker company on National Sticker Day, a utility on National 811 Day), which is the point: a named day nobody else in your category uses is a hook with no competition. Canada Day and the Super Bowl carry the largest campaigns in this group on small samples, both tied to national audiences with a single day of attention.

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

Missing from the data at any count worth reporting: Pride, Juneteenth, Cinco de Mayo, Pi Day, Bastille Day, Oktoberfest, Bonfire Night, Movember, Giving Tuesday, Small Business Saturday, Hanukkah, Boxing Day, Australia Day, Eurovision, Ramadan and Eid, Holi, Diwali beyond the main table, Day of the Dead, Carnival, Midsummer, Black History Month, Galentine's, Grandparents Day. Each appeared in under 15 campaigns of 37,123. An organizer who owns one of those has it to themselves.
