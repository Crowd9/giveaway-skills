#!/usr/bin/env python3
"""Draft giveaway terms from a short questionnaire. Python 3.8+, no dependencies. Output is a draft for a lawyer to check.

  python3 terms.py --promoter "Acme Bakery Pty Ltd" --address "1 Main St, Hobart TAS 7000" --name "Sweet Week Giveaway" \
     --open "2026-10-01 09:00 AEST" --close "2026-10-14 23:59 AEST" --draw "2026-10-15 10:00 AEST" \
     --eligible "Australian residents aged 18 or over" --exclude "employees of the promoter and their immediate families" \
     --prize "One Sweet Week box (seven pastries and a coffee daily for seven days), retail value AUD 70" --winners 5 \
     --method random --notify "email and Instagram direct message" --reply-days 3 --publish "first name and suburb" \
     --delivery "collected in store within 30 days" --cash-alternative no --region AU
"""
import argparse, sys

def draft(a):
    C = [f"Promoter. The promotion is run by {a.promoter}" + (f", {a.address}" if a.address else "") + " (the Promoter).",
         f"Entry period. Entries open at {a.open} and close at {a.close}. Entries received outside this period are invalid.",
         f"Eligibility. Entry is open to {a.eligible}. The following are not eligible: {a.exclude}.",
         "How to enter. Entrants complete the entry steps shown on the entry page. No purchase is necessary to enter. Where an optional step involves a purchase, a free entry route of equal weight is available. Entries that are incomplete, duplicated, automated, or made through multiple accounts are void.",
         f"Prize. {a.prize}. There are {a.winners} winner{'s' if a.winners != 1 else ''}. The prize is " + ("not transferable and no cash alternative is offered" if a.cash_alternative == "no" else "transferable and a cash alternative of equal value may be requested") + ". The Promoter may substitute a prize of equal or greater value if the stated prize becomes unavailable.",
         "Winner selection. Winners are selected " + ("at random from all valid entries" if a.method == "random" else "by the Promoter's judges on the published criteria, and the judges' decision is final") + f" on {a.draw}." + (" The draw method is published in advance and the result can be verified from the published record." if a.method == "random" else ""),
         f"Notification. Winners are notified by {a.notify} within 3 days of selection and must respond within {a.reply_days} day{'s' if a.reply_days != 1 else ''} of notification. If a winner does not respond, cannot be verified as eligible, or declines the prize, the prize is forfeited and a replacement winner is selected the same way.",
         "Verification. Winners may be asked to provide proof of identity, age and residence before the prize is released.",
         f"Delivery. Prizes are {a.delivery}. The Promoter is not responsible for prizes lost or damaged in transit once dispatched to the address the winner supplied." + (" Any tax, duty or charge arising from receipt of the prize is the winner's responsibility unless stated otherwise." if a.region != "none" else ""),
         f"Publicity. Winners consent to the Promoter publishing their {a.publish} for the purpose of announcing the result, and may withdraw that consent by contacting the Promoter.",
         "Personal information. Personal information collected is used to run the promotion, contact winners and deliver prizes, and is handled in accordance with the Promoter's privacy policy. Entrants may request access to or correction of their information by contacting the Promoter."]
    if a.marketing_consent:
        C.append("Marketing consent. Entering the promotion does not subscribe anyone to the Promoter's marketing. Marketing email is sent only to entrants who tick the marketing opt-in box on the entry form, which is a separate consent given at that moment. Consent can be withdrawn at any time through the unsubscribe link in any message or by contacting the Promoter, and withdrawing it has no effect on an entry or on a prize already won.")
    C += ["Platforms. The promotion is in no way sponsored, endorsed, administered by, or associated with Instagram, Facebook, TikTok, X, YouTube, or any other platform on which it is promoted. Entrants release those platforms from any liability connected with the promotion.",
          "General. The Promoter may cancel, suspend or amend the promotion where required by law or where it cannot proceed as planned. The Promoter's decisions are final on matters the terms do not cover. Entry constitutes acceptance of these terms."]
    L = [f"{a.name}: Terms and Conditions", ""] + [f"{i}. {c}" for i, c in enumerate(C, 1)]
    reg = {"AU": "Note for Australia: trade promotion lotteries are regulated by state and territory. Some require a permit above a prize-value threshold (NSW, ACT, SA, NT historically). Confirm permit needs before launch.",
           "UK": "Note for the UK: a free prize draw needs a genuinely free entry route to avoid being a lottery under the Gambling Act 2005, and the CAP Code sections on promotions apply.",
           "US": "Note for the US: sweepstakes must be free to enter (no purchase necessary with an alternate method of entry), official rules and odds statements are expected, and some states require registration and bonding above value thresholds (for example New York and Florida). Prizes may be taxable income to winners.",
           "EU": "Note for the EU: consumer protection and GDPR apply. Some member states regulate promotional games (for example Italy and Portugal require notification). Check the country of every eligible entrant.",
           "CA": "Note for Canada: a skill-testing question is common practice to avoid the lottery provisions of the Criminal Code, and Quebec has its own regime. Confirm before including Quebec residents."}
    L += ["", reg.get(a.region.upper(), "Check the rules of every jurisdiction where entrants live."), "",
          "This draft is generated from the answers supplied and is a starting point for legal review. It is not legal advice."]
    return "\n".join(L)

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for k in ("promoter", "name", "open", "close", "draw", "eligible", "exclude", "prize", "notify", "publish", "delivery"): ap.add_argument("--" + k, required="--self-test" not in argv)
    ap.add_argument("--address", default=""); ap.add_argument("--winners", type=int, default=1); ap.add_argument("--method", choices=["random", "judged"], default="random")
    ap.add_argument("--reply-days", type=int, default=3); ap.add_argument("--cash-alternative", choices=["yes", "no"], default="no"); ap.add_argument("--region", default="none")
    ap.add_argument("--marketing-consent", action="store_true", help="add a marketing-consent clause separate from the personal-information clause: entry alone does not subscribe anyone, and how to unsubscribe")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        a.promoter = "Test Co"; a.name = "Test Draw"; a.open = "1 Jan"; a.close = "2 Jan"; a.draw = "3 Jan"; a.eligible = "adults"; a.exclude = "staff"
        a.prize = "One hat, value 10"; a.notify = "email"; a.publish = "first name"; a.delivery = "posted"; a.region = "AU"
        t = draft(a); assert "1. Promoter. The promotion is run by Test Co" in t and "13. General." in t and "permit" in t and "not legal advice" in t
        assert ";" not in t and "—" not in t; print("self-test passed"); return 0
    print(draft(a)); return 0

if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
