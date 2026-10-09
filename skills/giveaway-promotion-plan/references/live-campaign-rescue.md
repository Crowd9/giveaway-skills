# Rescuing a Live Campaign

For a giveaway that is already running and going wrong. Everything on this page is common practice, nothing in the data covers it, with two exceptions. The pace of a typical run is extracted and sits in the channel playbook under "Where the traffic lands across the run". The Gleam notes quote what the Gleam documentation says and stop there.

Every campaign behind the dataset figures reached at least 100 Entrants, so the ones that stalled were filtered out before anything was measured. There is no base rate for how often a stall is a broken page and how often it is a quiet audience, and an answer that offers one has made it up. This paragraph is for you. Keep the reasoning out of the answer and give the reader the checks.

Two rules hold for the whole page:

- Never say what a platform's rules or a law requires. Name who decides and give the reader the question to put to them.
- Never say what a change does on Gleam unless the documentation says so. Where it is silent, say the docs do not cover it and the reader should check in the app.

## The Order of Work (Advice)

1. Write down the facts before touching anything. Impressions and Entrants for each day since the start, the time of the last Entry, every change made so far with its time, the pushes already sent, and what the campaign was for. Impressions by day come from the Reporting tab. Entrants by day come from the When column of the Actions export.
2. Export the Actions tab now. It is the record of what happened before the problem and before any fix.
3. Find the situation below that fits. Often it is two. Take the cheapest check first.
4. Change one thing at a time and write down when. The results review can then split the run into before and after.

## Reach, Conversion or Broken (Advice)

Diagnose before acting. A reader told to promote harder is spending money on a page that may be broken, and a reader told to fix the page is losing days to an audience problem.

| What you see | It is probably | Check first |
|---|---|---|
| Impressions below the typical day-N pattern, Entrants moving with them | Reach | Which source carried day one and whether it has stopped. Which pushes in the schedule are still unsent |
| Impressions on the pattern, Entrants far behind them | Conversion | What the page asks: the mandatory action, a verification step, a login wall, the eligibility line, the Prize |
| Impressions arriving and Entrants flat for hours, or stopping at one clock time | Something broken | The entry link in every place it was posted, the embed, the verification message, the email provider sync, and any change made at that time |
| A burst of Entrants in a short window from one source, one country or similar-looking addresses | Entries that look fake | The section below before anything else |
| Everything on the pattern | Not a fault yet | The objective, then the last section |

Read the pace from the channel playbook and leave memory out of it. On a two-week or month-long run the typical traffic falls hard through the first week or two, and on a week-long run it falls every day to the close. A falling line is the shape of the campaigns measured. Sitting under that line is the thing to diagnose. The curve holds Impressions only. Nothing in the data tracks Entrants by day, so no part of this page can say what an Entrant pace should be.

Run the checks in "When almost nobody has entered" in the playbook first, because they are the cheap ones. How to read a Conversion Rate while the run is still going is not something this skill measures. The results review has a live mode that does it.

## Changing Something Mid-Run (Advice)

Three things decide whether a change is safe. They are the terms Entrants accepted, the law of the country the terms name as governing, and the law of wherever entry is open. This skill states what none of them says. It sorts the change and gives the question.

**Sort the change by what it does to people who have already entered.**

- It adds to what they have: another Entry Method, a longer run, a better Prize.
- It takes something away: a removed Entry Method, a shorter run, a smaller or different Prize, narrower eligibility.
- It touches nothing they were promised: a caption, an image, an email, a partner post.

**Then quote the sentence in the terms that names the thing you want to change.** Dates, the Prize description, who can enter, how entries are earned and how Winners are picked all sit in the terms. If the terms name it, the change is a change to the terms, whatever the campaign page says.

Changes that add still go through the terms check. Changes that take something away go to the lawyer before the campaign is touched. Entries already taken stay counted unless the terms say otherwise, and the announcement says so only when the terms and the lawyer agree.

| Change | The question to put to the lawyer | On Gleam |
|---|---|---|
| Add an Entry Method | Do the terms list the ways to enter, and does a new one need notice or a fresh version of the terms in each country where entry is open? | The docs read do not say what adding one does to entries already taken. Gleam's tips library lists changing a live campaign when an action is not converting, so the vendor lists it as a normal move. Check in the app |
| Remove an Entry Method | Do the terms promise the entries that method earned, and what do they say about changing how entries are earned? | The docs read do not cover what removal does to entries already taken. Check in the app |
| Change or swap the Prize | Do the terms allow a substitute, of what value, and does a change need notice to Entrants? | Nothing read covers editing a Prize on a live campaign. The Prize tab also holds the Winner count, so open the draw settings after any change |
| Extend the end date | Do the terms fix the close, and does anything dated depend on it, such as a permit, a partner's schedule or the Winner contact window? | The Setup tab page says start and end dates can be changed at any point during the contest. Whether the generated terms follow the new date is not in the docs read, so open the terms after the change |
| Shorten the end date | The same, plus whether Entrants who were told the old date are owed notice | As above |
| Narrow or widen who can enter | Does changing eligibility mid-campaign create a problem with entries already taken, in each country involved? | Allowed Locations restricts by country and restricted visitors see a message. What it does to entries already taken from a country is not in the docs read |
| Fraud Level, CAPTCHA, login, verification | None for the terms alone. Ask whether the new step changes who can enter | Turning email or phone verification on mid-campaign leaves earlier unverified entries valid. The docs read do not say what raising the Fraud Level does to entries already collected, and say nothing on turning login or CAPTCHA on or off mid-campaign. The Actions tab is where entries are reviewed before the draw |

The Gleam column quotes the Gleam campaign setup reference, read from the documentation on 9 September 2026. Check the page before quoting it.

**Announce a change everywhere the original was announced.** The entry page description, the pinned comment, the bio link text, scheduled emails, countdown stickers, partner posts and directory listings. Search each of those for the old date and the old wording before you post the update. Write the update the same way every time:

"Update: [what changed], from [date, time, time zone]. [Everything else is unchanged.] Terms: [link]."

## Entries That Look Fake (Advice)

Read the Actions export and leave the Reporting tab for the totals. The Gleam documentation says Invalid entries do not appear in reporting and Entrants are never told, so the Reporting tab can hide exactly what you are trying to see.

1. Rule out the harmless causes. A validated-answer question marks wrong answers Invalid. A referral chain looks like a burst until the referral graph shows a few sharers behind it. A post, a partner, a directory listing or an email that went out at that time explains a burst on its own. Check the push calendar against the burst before suspecting anything.
2. Find the source. The report the results review prints from an export shows the first-touch channel and the invalid rate for each, and the countries and cities. A UTM-tagged link (see the tagging section of the playbook) tells you which of your own sources it was.
3. Look for what the entries share: one referrer, one country the audience is not in, one single Entry Method and nothing else, addresses that follow a pattern, a clock time. These are signs to investigate. None of them proves anything alone, because real people share a country and an Entry Method too.
4. Do not remove anyone yet. The fraud filter marks suspicious entries Invalid on its own, and Gleam's documentation says it may adjust a campaign's level when it blocks legitimate Entrants. Review before the draw, with the whole export in front of you.
5. Write the removal rule before you look at who it removes. "Entries from [source] completing only [method] within [window]" is a rule. "The ones that look wrong" is a verdict.
6. Reduce what is still coming in through the changes table above. Pausing a paid boost touches nothing Entrants were promised. Login before actions, verification and CAPTCHA are documented Gleam settings. The Gleam notes in the changes table apply to each, and the page on login notes it can reduce fraud.
7. Confirm any Winner from this campaign through the checks in the Winner communications step before announcing them.

Say nothing public about it. Do not name Entrants or post addresses, and do not announce that fakes were found. The Winner announcement carries the draw record, which is the answer to anyone who asks.

## Someone Says It Is Rigged or Breaks the Rules (Advice)

Separate what is being claimed, because each one has a different person who decides.

| The claim | Who decides | What to do |
|---|---|---|
| The draw is rigged or "the same people always win" | Nobody can decide it yet if the draw has not happened. After it, the record decides | Answer once with the method and the record, using the reply in the playbook's comments table. If the draw is still ahead, publish the method and the date now and do not bring the draw forward to settle it |
| The giveaway breaks a platform's rules | The platform, under the policy it publishes on the day you read it | Read the platform's current page on promotions yourself and put the question below. Reply with the holding line |
| The giveaway is illegal | A lawyer in the country named as governing law in the terms, and wherever entry is open | Do not argue it in the comments. Put the lawyer's questions in the eligibility reference of the winner structure skill |
| An account is copying yours and contacting Entrants | The platform, on a report | The impersonation row in the playbook's comments table |

**The platform question.** "Does [platform]'s promotions policy allow [the mechanic named: tag a friend, share to enter, comment to enter, follow to enter] on a promotion run through a [post, page, profile], and does it need a disclaimer or a release?" This page does not answer it. The policy changes and only the platform can say.

**The holding line, posted once:** "Thanks for flagging this. We are checking [platform]'s current promotion rules today and will update the post if anything needs to change."

Then do the check that day. If the mechanic is in doubt, take it out from now on through the changes table, keep entries already earned counted unless the terms say otherwise, and post the update line. Weigh the two risks together, the platform's and the Entrants'. Removing a mechanic is a change that takes something away.

In all four cases, screenshot the accusation and the thread with the time showing, never delete a complaint, delete only abuse, and answer in the first hour where you can. If the accuser has found a real mistake, such as a wrong close time, correct it in public and say what changed.

## The Campaign or the Account Was Taken Down (Advice)

Who decides depends on what was actioned. A social post or account is the platform's decision. The campaign page is Gleam's. Find out which before doing anything.

1. Read the notice and screenshot it, with the time. Take the reason from the wording, never from a guess. Export the Actions tab if you can still reach it.
2. Say exactly what was actioned: one post, the account, a link, the campaign page, or the Gleam account.
3. Appeal through the route named in the notice and ask three things: which rule, which content, and what would restore it. Nothing read here covers how long a platform takes to review an appeal, so give no date for it.
4. Do not repost the same content from a second account until you have read what the notice says about it.
5. Move the campaign to channels you still have. The email list is the first of them, then the other social accounts and the website. Post the entry link and the official handle.
6. Open the entry link signed out, on a phone, and enter once yourself. A restricted social account can leave the campaign page working, and a restricted campaign page can leave the social account working. You need to know which.
7. Put the question to the lawyer: "What do the terms let us do if the campaign must pause or stop early, and does the close date need to move?" Then decide extension against the last section.

Nothing read here covers how Gleam handles a campaign it has actioned. Ask Gleam support, and quote only what they send back.

## Extend, Push Harder or Accept (Advice)

Decide in this order. Each step is cheaper than the one after.

| Situation | The call | Why |
|---|---|---|
| Something was broken | Fix it, then judge the audience on days when the page worked. Adding back the days lost is an extension, so it goes through the changes table | A run of days with a broken page says nothing about demand |
| Impressions under the curve and pushes still unsent | Send the scheduled pushes first, the partner next and paid last, capped at what one extra Winner would cost | They are already planned and cost the least |
| Impressions on the curve, Entrants behind an entry target, pushes spent | Change what the page asks, through the changes table, or accept | More traffic into a page that does not convert returns the same rate |
| Everything spent, traffic at the quiet-middle level, objective missed | Extend only with a dated new push at the start of the extension, or accept | Nothing in the data measures what bare added days bring in |
| Objective reached | Accept. Close and draw on the date in the terms | Every date in the terms stays true |

On a run of two weeks or more, the playbook's curve puts the close a little above the quiet middle on its own. The results review's live mode has the closing days by run length. Plan the last-call push for that stretch.

Ask what the campaign was for before calling a number short. Compare the target with purchasing customers, consented subscribers or qualified leads, using the outcome the reader actually wants. Entry records alone establish none of these. With 100 Entrants, 20 consented subscribers and no purchases, a target of 100 purchasing customers remains unmet. An unavailable outcome count stays unknown, so do not call the objective reached. Judge an entry target by Entrants and the audience the reader can reach.

An extension has costs the dataset cannot measure, such as the terms, a permit tied to dates, a partner who posted for the old close, and a Winner contact window that starts later. Put them to the lawyer in one message with the new date.

When the call is accept, take the next steps from the afterwards section of the playbook and send the Entrants the post-close message from the Winner communications step.
