# Eligibility and Compliance

The decisions that have to be settled before the dates are locked, because changing any of them after launch means changing the terms Entrants already accepted.

This file never states what a law requires. It names who decides a point and the question to put to a lawyer. The figures describe what businesses chose, never what any of them was obliged to do.

## Settle These Before the Dates

- **Which countries entry is open in.** This drives everything below it, and it is the one decision the terms, the shipping plan and the tax question all hang off.
- **Minimum age**, and whether anyone under it could plausibly want this Prize. A kids, family or pets Prize makes this the first question, not the last.
- **Who is excluded.** Staff, their households, agencies, partners, previous Winners.
- **The free entry route**, and whether every way in is genuinely free.
- **What happens to the data**, who else sees it, and how long it is kept after the draw.
- **Whether a permit, registration or notification is needed anywhere entry is open**, and how long it takes to get. This is the one that moves the start date, so it goes to a lawyer first.

## What Businesses Chose

| Choice | Campaigns | Businesses | Typical Entrants | Conversion Rate |
|---|---|---|---|---|
| Entry open to everyone | 86,978 | 14,473 | 439 | 27% |
| Entry restricted by country | 29,521 | 4,919 | 702 | 27% |

Restricting entry by country came with a bigger crowd and the same Conversion Rate, so narrowing the field is not a cost in turnout in this data. Those campaigns also asked for an email address far more often, 54% against 26%, which is the likelier reason they look different. A business that restricts is usually a business that wants a list it can legally mail.

Governing law named in the terms, top five: United States 55,088 campaigns, United Kingdom 14,002, Canada 6,979, Australia 6,580, Brazil 4,739.

39% of campaigns write fully custom terms. The rest run the generated ones.

Draw and response windows sit on the default almost everywhere: 7 days to draw on 108,813 campaigns, 7 days for the Winner to reply on 107,694.

Source: `analysis/output/field_cuts.json` (`terms`, `by_country_rule`).

## The Questions to Put to a Lawyer

Take these with the country list, the Prize value and the entry route already decided. Each one names a decision somebody else makes.

**On where you can run it**
- Which of these countries treats this as a promotion needing a permit, registration or notification at this Prize value, and how long does each take?
- Does any country on the list regulate how the Prize is advertised separately from how it is run?
- Is a skill element needed anywhere on the list, and what counts as one?

**On who can enter**
- What is the minimum age in each country, and does a parent or guardian need to consent or to claim?
- Does excluding a country mid-campaign create a problem with entries already taken from it?

**On the entry route**
- Is every route in genuinely free, including the ones that cost an Entrant time or data?
- Does anything an Entrant has to buy, follow or install change how the promotion is classified?

**On the data**
- What is the lawful basis for collecting these details, and for mailing these people afterwards?
- How long can non-Winner details be kept, and what has to happen at the end of that?
- If a partner receives any of it, who is responsible for it?

**On the Prize**
- Who reports the Prize, and to whom?
- What happens if the Winner is in a country the Prize cannot ship to?

## What This Skill Will Not Do

It will not tell the reader what a law requires, what a threshold is, or what a regulator will accept, however familiar the point feels. `scripts/terms.py` produces a draft with a region note that names who decides and what to ask. The draft is for a lawyer to review before it is published.
