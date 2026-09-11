# Email sequence

Advice. Nothing here carries a dataset figure. Two audiences get different emails during a giveaway: the list that has not entered yet, and the people who have. Sending a last call to someone who entered on day one wastes the send and reads as noise, and the Entrant is the one person who can bring a friend.

## Architecture

- Trigger: the launch date for the existing list, the entry sync for Entrants.
- Goal: entries from the list, referrals from Entrants, and a clean opt-in that survives the Winners email.
- Exit: an address that enters leaves the not-entered branch at the next sync. Unsubscribe or a hard bounce exits everything.
- Suppression: while the giveaway runs, hold the regular promotional sends for the not-entered branch on push days, so nobody gets two emails inside two hours. Existing customers who enter stay on the customer stream and receive the Entrant emails from there.
- Sender: the from name and reply-to the list already knows. A reply-to that a person reads, since Winners and complaints answer this address.

## Not entered yet

| Email | When | Subject line pattern | Preview text | Body |
|---|---|---|---|---|
| Launch | Launch day, within two hours of the first post | "Win [Prize]" or "[Brand] is giving away [Prize]" | "Takes a minute to enter. Closes [date]." | Prize and value in the first line. Three-step entry. Deadline with time zone. Eligibility. One button to the entry page. |
| Mid | Day 4 to 7 of a two-week run | "[Prize detail] and how to win it" | "[N] people are in. Here is what they are playing for." | One thing about the Prize that was not in the launch. Social proof if real (Entrants so far, a partner). Referral reward. Same button. |
| Last call | 24 to 36 hours before close | "Closes tomorrow: [Prize]" | "One minute to enter, then it is gone." | Deadline first. One sentence on the Prize. Button. |

## Entered

| Email | When | Subject line pattern | Preview text | Body |
|---|---|---|---|---|
| Welcome and referral | Within a day of entry, sent by the email provider's automation when the sync lands | "You are in. Want more entries?" | "Your referral link is inside." | Confirm the entry, name the brand so the address is recognised later, give the personal referral link and the reward per friend, and the close date. This is message one of the welcome series in giveaway-winner-communications. |
| Last day nudge | The day before close | "Last day to add entries" | "Every friend you refer counts until [time]." | Referral link again, the close time with zone. Skip it when the campaign has no referral action. |

The platform's own entry confirmation covers the entry itself. The welcome email is the one that carries the brand and the referral link into the inbox the Entrant actually reads, so send it even when the platform confirms.

## Everyone who opted in

| Email | When | Subject line pattern | Preview text | Body |
|---|---|---|---|---|
| Winners | Within a week of the draw | "The [Prize] Winner is..." | "Plus a thank-you for everyone who entered." | First name and city or handle, with consent. Thank everyone. A small offer or a next-campaign teaser. Then the welcome series continues in giveaway-winner-communications. |

## Before the launch email

- Email authentication (SPF, DKIM, DMARC) passes on the sending domain. A launch email that lands in spam sets the open rate for every email after it.
- The integration from the giveaway platform to the email provider is live and tested with an admin entry, so the entered branch triggers during the run and the tag or list name carries the campaign name.
- The entered branch suppresses the not-entered emails. Check it with a test address that enters after the launch send.
- Every link carries the UTM set from the promotion plan, with medium set to email.
- The footer carries the physical address and a one-click unsubscribe. Unsubscribes apply across both branches at once.
- When the giveaway list is new, send it from its own segment or its own stream in the email provider, kept apart from the customer list. Giveaway signups engage differently, and one bad send to a cold list drags the deliverability of everything else down with it.
- A new sending domain or subdomain needs warming before the launch email. Start weeks ahead at a low daily volume with the most engaged addresses, raise it gradually, and watch bounces and complaints at each step.

## Rules for the list

- Send only to people who opted in. Entrants who ticked the newsletter box during entry get the Entrant emails, the Winners email and the welcome series after. Entrants who did not tick it get the Winner notification if they win and nothing else.
- One email per push per branch. Anyone unsubscribing mid-campaign gets nothing more.
- Subject lines under 45 characters, preview text under 90, and the preview says something the subject does not.
- Test the entry link and the close time in every email. The close time reads in the audience's time zone.
- Plain text or one image and a button. Giveaway emails are quick to read and quick to forward.
- Send at the hour the list usually opens. The launch email goes inside two hours of the first post, whatever the hour, so the two land together.

## What to read after each send

- Launch email open share below what the list usually does: check the inbox placement before the copy. Authentication and the sending stream come first.
- Opens fine, clicks low: the button or the entry page. Test the link on a phone.
- Unsubscribes rise on the mid or last-call email: the list is hearing about the giveaway too often. Drop the last call for anyone who opened the mid email and did not enter, or send it as plain text.
- Complaints on the Winners email: the opt-in on the entry form was not obvious. Fix the form before the next campaign, and read the hygiene rules in giveaway-winner-communications.

## Fourth quarter for a store

- The giveaway segment is new and unproven, and Black Friday is the largest send of the year. Send the launch, mid and Winners emails to the giveaway segment before the sale, so the addresses that will never open are known before they can hurt the sale send.
- Close the pre-sale giveaway the day before the sale. The Winners email carries early access to the sale as the non-Winner offer, and the sale email follows the next day to the same segment.
- No giveaway email on the sale days. The timing skill's holiday table shows campaigns live over Black Friday converting about 11% below matched campaigns.
- The December giveaway's last call goes out before the shipping cutoff email, so both promises can be kept.
