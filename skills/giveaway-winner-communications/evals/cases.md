# Evaluation cases

Machine-readable form: `evals.json`. Style checks use `evals/style_check.py` at the repo root.

## The 40-Prompt Evaluation, 11 September 2026

Four of the forty prompts in `.omc/skill-loop/evalset.json` were run against this skill on 11 September 2026. Scoring was by an independent grader against `.omc/skill-loop/rubric.md`. Types are S straightforward, U underspecified, H hard realistic, T trap.

These forty prompts are additional to the cases in `evals.json`, which are a different set and were not re-scored in this round. The last recorded run of those cases was 10 September 2026, before this round of corrections landed, so their results are no longer reported here.

`.omc/skill-loop/final-scores.json` was written before iteration 5 was graded, so its final column holds the iteration 3 or iteration 2 score wherever a later grade exists. The table below reports the latest graded run.

| Prompt | Type | Baseline | Latest | Latest graded run |
|---|---|---|---|---|
| comms-1 | S | 74 | 82 | iteration 2 |
| comms-2 | H | 71 | 76 | iteration 2 |
| comms-3 | T | 86 | 86 | iteration 2 |
| comms-4 | U | 81 | 84 | iteration 5 |

### comms-1 (S)

```
We drew our winner this morning. What do I send them, and what do I send the 2,000 people who didn't win?
```

The baseline stopped at the notification, so the verification and address request the organizer needs next was missing. The latest answer delivers both messages ready to send with the code mechanics and the consent split spelled out, and it stops at the notification again.

### comms-2 (H)

```
Winner was drawn 9 days ago, hasn't replied to two emails. Our terms say 7 days to claim. There's a second person in the comments saying they won and posting a fake screenshot. Prize is a 1,200 USD bike. What do I send, to whom, and in what order?
```

The baseline told the lapsed Winner the Prize had passed to a reserve one step before it drew one, which the reference forbids. The latest answer handles the impersonation case properly, with the official-account line pinned to the post, and it states the rule that nothing goes out naming a reserve before one exists and breaks it a line later.

### comms-3 (T)

```
I'll just post the winner's full name and their Instagram handle in a story and tag them, that's how everyone does it. Also I need their address so I'll DM them for it.
```

The baseline stretched the reference's payment-scam warning to cover address requests and stated it as fact. The latest answer corrects both halves without lecturing and leaves a working route on each, and it never says what the terms allow to be published and never hands over the announcement post itself.

### comms-4 (U)

```
winner email template
```

The baseline closed on an offer to send more, which the skill's own style rules ban as a closer. The latest answer quotes the reminder timing from `references/message-templates.md` line 11 word for word, and it writes one message out of six and describes the other four without delivering them.

## Contact and consent regression, 12 September 2026

Added the no-subscription-Action prompt in `evals.json`. The documentation review checked the workflow and reference for separate address, consent and Action-usage decisions. No model response was generated or scored for this new case.

## 9 October 2026, ten-prompt blind comparison

One prompt per skill was answered by Sonnet and assessed by a blind Sonnet pairwise judge. The retained round, r7, beat the pre-restructure round, r4, with eight wins, one loss and one tie overall.

This skill's retained-round verdict was a win. The judge flagged an instruction to count two groups without explaining how, and an unsupported claim that a few hundred answers would provide cheap Prize research.

The rest of `evals.json` was not rerun.

## 9 October 2026, guardrail fixture coverage

These are synthetic checker fixtures, not model answers. Review JSON files contain expected fixture verdicts, not an independent assessment of a model. Each case still needs meaning review for paraphrases and contradictions.

| Case | Guardrail | Model status |
|---|---|---|
| 6 | legal-authority | not yet run against a model |
| 7 | fulfilment-inference | not yet run against a model |
| 8 | platform-compliance | not yet run against a model |
| 9 | plain-reader-language | not yet run against a model |
| 10 | causal-data-claim | not yet run against a model |
| 11 | guaranteed-outcome | not yet run against a model |
| 12 | marketing-consent | not yet run against a model |
| 13 | reserve-not-yet-drawn | not yet run against a model |

The matching pass and fail answers and review verdicts are in `../../../evals/fixtures/giveaway-winner-communications/`. The CLI checks both outcomes with `--review`. Fixture success is not a model-quality score.

Previously unchecked case 4 is now explicitly judgement-only, with a review rubric. It requires a supplied reviewer verdict and has not been rerun against a model.

## Cash requests and third-party delivery, 10 October 2026

Added judgement-only cases for permitted and prohibited third-party delivery. The reference supplies a separate reply for each arrangement and leaves unconfirmed permission on the no-offer path. These cases have not been run against a model.

## Prize substitution branches, 10 October 2026

Added judgement-only regression cases. Reviewed the source instructions and copyable templates for the stated branches. These cases have not been run against a model.

## Answer scope regression, 10 October 2026

Added assertions for the brief's answer corrections to an existing case. Not yet run against a model. Repository checks are recorded in the patch report.

## Email failure diagnosis, 10 October 2026

Added a judgement-only regression case after reviewing the source instructions and Mailchimp bounce documentation. It requires concrete checks before inferring intent or choosing a remedy. This case has not been run against a model. Repository checks are recorded in the patch report.
