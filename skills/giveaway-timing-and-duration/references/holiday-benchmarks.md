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

| Holiday | Date | Launch window | Typical launch |
|---|---|---|---|
| Halloween | Sat 31 Oct 2026 | 01 Oct to 24 Oct | 12 Oct |
| Thanksgiving | Thu 26 Nov 2026 | 30 Oct to 17 Nov | 09 Nov |
| Black Friday and Cyber Monday | Fri 27 Nov 2026 | 11 Nov to 24 Nov | 19 Nov |
| Christmas and advent | Fri 25 Dec 2026 | 27 Nov to 14 Dec | 06 Dec |
| New Year | Fri 01 Jan 2027 | 09 Dec to 27 Dec | 21 Dec |
| Lunar New Year | Mon 01 Feb 2027 | 25 Jan to 31 Jan | 27 Jan |
| Valentine's Day | Sun 14 Feb 2027 | 26 Jan to 08 Feb | 02 Feb |
| Easter | Sun 28 Mar 2027 | 07 Mar to 24 Mar | 18 Mar |
| Mother's Day | Sun 09 May 2027 | 15 Apr to 02 May | 26 Apr |
| Father's Day | Sun 20 Jun 2027 | 01 Jun to 11 Jun | 07 Jun |
| Back to school | Wed 25 Aug 2027 | 23 Jul to 14 Aug | 04 Aug |
| Halloween | Sun 31 Oct 2027 | 01 Oct to 24 Oct | 12 Oct |
| Thanksgiving | Thu 25 Nov 2027 | 29 Oct to 16 Nov | 08 Nov |
| Black Friday and Cyber Monday | Fri 26 Nov 2027 | 10 Nov to 23 Nov | 18 Nov |
| Christmas and advent | Sat 25 Dec 2027 | 27 Nov to 14 Dec | 06 Dec |
| New Year | Sat 01 Jan 2028 | 09 Dec to 27 Dec | 21 Dec |

Ramadan and Eid, Prime Day, Singles' Day, anniversaries and milestones have no fixed date here. Use the theme row above for their shape and the region calendar in `calendar-by-region.md` for the dates that stall a team or an audience.
