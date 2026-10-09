#!/usr/bin/env python3
"""Draft giveaway terms from a short questionnaire. Python 3.8+, no dependencies. Output is a draft for a lawyer to check.

  python3 terms.py --promoter "Acme Bakery Pty Ltd" --address "1 Main St, Hobart TAS 7000" --name "Sweet Week Giveaway" \
     --open "2026-10-01 09:00 AEST" --close "2026-10-14 23:59 AEST" --draw "2026-10-15 10:00 AEST" \
     --eligible "Australian residents aged 18 or over" --exclude "employees of the promoter and their immediate families" \
     --prize "One Sweet Week box (seven pastries and a coffee daily for seven days), retail value AUD 70" --winners 5 \
     --method random --notify "email and Instagram direct message" --reply-days 7 --publish "first name and suburb" \
     --delivery "collected in store within 30 days" --cash-alternative no --region AU
"""
import argparse, sys

def draft(a):
    duplicate_policy = (getattr(a, "duplicate_policy", None) or
                        "[Agree the eligibility, duplicate-account and automation rules before publishing.]")
    reserve_policy = (getattr(a, "reserve_policy", None) or
                      "[Agree the reserve procedure before publishing, including the recorded order of any pre-drawn reserves and what happens when they are exhausted.]")
    C = [f"Promoter. The promotion is run by {a.promoter}" + (f", {a.address}" if a.address else "") + " (the Promoter).",
         f"Entry period. Entries open at {a.open} and close at {a.close}. Entries received outside this period are invalid.",
         f"Eligibility. Entry is open to {a.eligible}. The following are not eligible: {a.exclude}.",
         "How to enter. Entrants complete the entry steps shown on the entry page. No purchase is necessary to enter. Where an optional step involves a purchase, a free entry route of equal weight is available. " + duplicate_policy + " Multiple chances legitimately earned under the entry rules remain valid.",
         f"Prize. {a.prize}. There " + ("is 1 Winner" if a.winners == 1 else f"are {a.winners} Winners") + ". The Prize is " + ("transferable" if a.transferable == "yes" else "not transferable") + ". " + ("No cash alternative is offered" if a.cash_alternative == "no" else "A cash alternative of equal value may be requested") + ". The Promoter may substitute a Prize of equal or greater value if the stated Prize becomes unavailable.",
         "Winner selection. Winners are selected " + ("at random from all valid Entries" if a.method == "random" else "by the Promoter's judges on the published criteria, and the judges' decision is final") + f" on {a.draw}." + (" The draw method is published in advance and the result can be verified from the published record." if a.method == "random" else ""),
         f"Notification. Winners are notified by {a.notify} within 3 days of selection and must respond within {a.reply_days} day{'s' if a.reply_days != 1 else ''} of notification. If a Winner does not respond, cannot be verified as eligible, or declines the Prize, the replacement procedure is: " + reserve_policy,
         "Verification. Winners may be asked to provide proof of identity, age and residence before the Prize is released.",
         f"Delivery. Prizes are {a.delivery}. The Promoter is not responsible for Prizes lost or damaged in transit once dispatched to the address the Winner supplied." + (" Any tax, duty or charge arising from receipt of the Prize is the Winner's responsibility unless stated otherwise." if a.region.lower() != "none" else ""),
         f"Publicity. Winners consent to the Promoter publishing their {a.publish} for the purpose of announcing the result, and may withdraw that consent by contacting the Promoter.",
         "Personal information. Personal information collected is used to run the promotion, contact Winners and deliver Prizes, and is handled in accordance with the Promoter's privacy policy. Entrants may request access to or correction of their information by contacting the Promoter."]
    if a.marketing_consent:
        C.append("Marketing consent. Entering the promotion does not subscribe anyone to the Promoter's marketing. Marketing email is sent only to Entrants who tick the marketing opt-in box on the entry form, which is a separate consent given at that moment. Consent can be withdrawn at any time through the unsubscribe link in any message or by contacting the Promoter, and withdrawing it has no effect on an entry or on a Prize already won.")
    C += ["Platforms. The promotion is in no way sponsored, endorsed, administered by, or associated with Instagram, Facebook, TikTok, X, YouTube, or any other platform on which it is promoted. Entrants release those platforms from any liability connected with the promotion.",
          "General. The Promoter may cancel, suspend or amend the promotion where required by law or where it cannot proceed as planned. The Promoter's decisions are final on matters the terms do not cover. Entry constitutes acceptance of these terms."]
    L = [f"{a.name}: Terms and Conditions", ""] + [f"{i}. {c}" for i, c in enumerate(C, 1)]
    # Each note names who decides and the question to put to a lawyer. None of them states what a law requires,
    # which is the rule every skill in this repository carries and which this script used to break.
    reg = {"AU": "Note for Australia: each state and territory decides how a trade promotion is regulated, and a permit can be required. Ask your lawyer which states your Entrants are in, whether a permit applies at your Prize value, and how long one takes to obtain.",
           "UK": "Note for the UK: how a Prize draw must be structured, and how it must be advertised, are decided by the gambling regulator and the advertising codes. Ask your lawyer whether your entry route qualifies as free and what the advertising codes require of your wording.",
           "US": "Note for the US: rules are set federally and state by state, and some states treat registration, bonding and Prize tax differently above certain values. Ask your lawyer which states your Entrants are in, what your Prize value triggers in each, and who reports the Prize as income.",
           "EU": "Note for the EU: consumer protection and data protection are decided at both EU and member-state level, and some member states regulate promotional games separately. Ask your lawyer about the country of every eligible Entrant, and about your lawful basis for the data you collect.",
           "CA": "Note for Canada: federal law and the provinces each have a say, and Quebec is commonly treated separately. Ask your lawyer whether a skill-testing question is needed for your promotion and what including Quebec residents would require of you."}
    asked = [r.strip().upper() for r in a.region.split(",") if r.strip() and r.strip().lower() != "none"]
    notes = [reg[r] for r in asked if r in reg]
    uncovered = [r for r in asked if r not in reg]
    if uncovered:
        notes.append("No note here covers " + ", ".join(uncovered) + ". This script carries notes for "
                     + ", ".join(sorted(reg)) + " only, so treat every other country as unchecked and take advice on it "
                     + "before opening entry there.")
    if not notes:
        notes = ["Check the rules of every jurisdiction where Entrants live."]
    L += [""] + notes + ["",
          "This draft is generated from the answers supplied and is a starting point for legal review. It is not legal advice."]
    return "\n".join(L)

class _Copy:
    """A shallow copy of the parsed args, so a self-test can vary one field."""
    def __init__(self, src):
        self.__dict__.update(src.__dict__ if hasattr(src, "__dict__") else {k: getattr(src, k) for k in dir(src) if not k.startswith("_")})

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    for k in ("promoter", "name", "open", "close", "draw", "eligible", "exclude", "prize", "notify", "publish", "delivery"): ap.add_argument("--" + k, required="--self-test" not in argv)
    ap.add_argument("--address", default=""); ap.add_argument("--winners", type=int, default=1); ap.add_argument("--method", choices=["random", "judged"], default="random")
    ap.add_argument("--reply-days", type=int, default=7); ap.add_argument("--cash-alternative", choices=["yes", "no"], default="no"); ap.add_argument("--region", default="none", help="one or more of AU, UK, US, EU, CA, comma separated. Any other country is named in the output as uncovered")
    ap.add_argument("--transferable", choices=["yes", "no"], default="no", help="whether the Prize can be transferred, independently of a cash alternative")
    ap.add_argument("--marketing-consent", action="store_true", help="add a marketing-consent clause separate from the personal-information clause: entry alone does not subscribe anyone, and how to unsubscribe")
    ap.add_argument("--duplicate-policy", help="settled eligibility, duplicate-account and automation rules, preserving legitimately earned chances. Omit to leave an agreement placeholder")
    ap.add_argument("--reserve-policy", help="settled replacement procedure, using eligible pre-drawn reserves in recorded order before any agreed fresh draw. Omit to leave an agreement placeholder")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.winners < 1: ap.error("--winners must be a positive integer")
    if a.reply_days < 0: ap.error("--reply-days must be a nonnegative integer")
    if a.self_test:
        a.promoter = "Test Co"; a.name = "Test Draw"; a.open = "1 Jan"; a.close = "2 Jan"; a.draw = "3 Jan"; a.eligible = "adults"; a.exclude = "staff"
        a.prize = "One hat, value 10"; a.notify = "email"; a.publish = "first name"; a.delivery = "posted"; a.region = "AU"
        t = draft(a); assert "1. Promoter. The promotion is run by Test Co" in t and "13. General." in t and "Ask your lawyer" in t and "not legal advice" in t
        assert ";" not in t and "\u2014" not in t
        a.region = "UK,DE,JP"
        m = draft(a)
        assert "There is 1 Winner" in t, "one Winner must not read as \"There are 1 Winner\""
        a2 = _Copy(a); a2.winners = 3
        assert "There are 3 Winners" in draft(a2)
        assert "Note for the UK" in m, "a known region in a list must still get its note"
        assert "No note here covers DE, JP" in m, "an uncovered country must be named, never passed over in silence"
        assert "Note for Australia" not in m, "only the regions asked for get a note"
        import contextlib, io
        required = [item for key in ("promoter", "name", "open", "close", "draw", "eligible", "exclude", "prize", "notify", "publish", "delivery") for item in ("--" + key, "test")]
        with contextlib.redirect_stdout(io.StringIO()) as output:
            main(required)
        assert "must respond within 7 days" in output.getvalue()
        assert "[Agree the eligibility, duplicate-account and automation rules before publishing.]" in output.getvalue()
        assert "[Agree the reserve procedure before publishing" in output.getvalue()
        assert "incomplete, duplicated, automated" not in output.getvalue()
        assert "a replacement Winner is selected the same way" not in output.getvalue()
        duplicate_policy = "One valid daily Entry earns one chance. Bonus actions earn the published extra chances. Repeated export rows are removed without removing legitimately earned chances. Automated Entries and duplicate accounts are invalid."
        reserve_policy = "Two reserves are drawn in order with the Winners. Offer the Prize to the first eligible reserve, then the second, allowing each 7 days to respond. If both are exhausted, conduct a fresh draw from the remaining eligible Entrants under the published method."
        with contextlib.redirect_stdout(io.StringIO()) as output:
            main(required + ["--duplicate-policy", duplicate_policy, "--reserve-policy", reserve_policy])
        assert duplicate_policy in output.getvalue() and reserve_policy in output.getvalue()
        assert "Multiple chances legitimately earned under the entry rules remain valid." in output.getvalue()
        assert "[Agree" not in output.getvalue()
        with contextlib.redirect_stdout(io.StringIO()) as output:
            main(required + ["--reply-days", "2"])
        assert "must respond within 2 days" in output.getvalue()
        for cash in ("yes", "no"):
            for transfer in ("yes", "no"):
                with contextlib.redirect_stdout(io.StringIO()) as output:
                    main(required + ["--cash-alternative", cash, "--transferable", transfer])
                text = output.getvalue()
                assert ("The Prize is transferable." in text) == (transfer == "yes")
                assert ("The Prize is not transferable." in text) == (transfer == "no")
                assert ("A cash alternative of equal value may be requested." in text) == (cash == "yes")
                assert ("No cash alternative is offered." in text) == (cash == "no")
        for option, value in (("--winners", "0"), ("--winners", "-1"), ("--reply-days", "-1")):
            with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
                try: main(required + [option, value])
                except SystemExit as error: assert error.code == 2
                else: raise AssertionError("invalid counts must not generate terms: " + option + " " + value)
        print("self-test passed"); return 0
    print(draft(a)); return 0

if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
