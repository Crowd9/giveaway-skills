#!/usr/bin/env python3
# Generated from evals/style_check.py by scripts/render_shared.py. Edit the source, never this copy.
# Run it on a draft answer before sending: python3 scripts/style_check.py draft.txt
"""Count the style tells a giveaway skill's answer must not carry. Usage: python3 style_check.py reply.txt [more.txt ...]

Hard fails: em dashes, semicolons, curly quotes, an assistant opener or closer, a question as a heading, a label opener
(a sentence announcing the next block instead of saying the thing), three or more paragraphs led by the same bold label,
the answer commenting on itself, a closing sentence that carries no number and asks for nothing, a mechanic banned
on the strength of an average when no platform rule, law or money risk is named nearby, a raw pair of decimals the reader
has to divide themselves, analysis jargon that belongs in the reference files, a literary join nobody says out loud,
an answer over sixty words that never once says "you", and any of Gleam's own words written without its capital,
which covers the dashboard names and the product nouns Entrant, Contestant, Prize and Winner. "entries" stays out:
the repo's own prose uses it as a common noun 194 times, so flagging it would fail the references it is drawn from.
Sentence variety is the soft gate: something short, something long, so the answer does not read as one template rhythm.
"""
import re, sys

# Two words came off this list because the product uses them literally. A randomness beacon is the
# published public value a provable draw rests on, from drand or NIST. Mandatory actions unlock the
# rest, which is what campaign-setup.md calls it, so a skill explaining that setting has to say it.
# A checker that bans the product's own vocabulary teaches the skill to be vague about its subject.
FILLER = (r"\b(actually|leverage|robust|comprehensive|streamline|delve|foster|pivotal|landscape|testament|showcase|furthermore"
          r"|moreover|additionally|it is worth noting|generally speaking|in many cases|synergy|holistic|seamless|world-class"
          r"|utilise|utilize|facilitate|empower|cutting-edge|paradigm shift|game changer|transformative|elevate|embark"
          r"|supercharge|harness|ever-evolving|realm|tapestry|multifaceted|meticulous|intricate|paramount"
          r"|crucial|vital|at the end of the day|when it comes to|at its core|in today's world|the reality is|the truth is"
          r"|in terms of|with regard to|going forward|let's dive in|let's take a look)\b")
OPENERS = r"^(great question|here's how i'd think|here is how|let me walk you|certainly|of course|sure[,!])"
CLOSERS = r"(hope this helps|let me know if|feel free to|happy to elaborate)"
# A closing question that offers to do more work. Distinct from a question that asks for a missing fact.
OFFER = (r"\b(want (me|the|a|an|that|one)|shall i|should i|would you like|do you want|can i (draft|write|put|run|send|do)"
         r"|happy to|i can (also )?(draft|write|put together|run|send)|(need|like) (me|anything else))\b")
CONTRAST = r"(, not \w|\bnot \w+(?: \w+){0,4}, (?:but|it's|it is)\b|\brather than\b|\binstead of\b|\binstead\b\s*[.,]|, don't \w)"
# A sentence that announces the next block rather than saying the thing. The commonest slop tell after punctuation.
LABEL_OPENER = ("^(the (reasoning|caveat|point|upshot|short version|catch|tradeoff|takeaway|rule|logic|thinking|context"
                r"|detail|numbers?|figures?|evidence)\b[^.!?]{0,60}[.:]"
                r"|what (i|we|you) (would|will|should|did)\b[^.!?]{0,60}[.:]"
                r"|why (this|that|it) (works|matters|holds)\b[^.!?]{0,40}[.:]"
                r"|here is (what|how|why|the)\b|what follows\b|first, (the|a)\b[^.!?]{0,40}[.:]"
                # a count of things about to be listed, or a thing about to be flagged, is a label wearing a sentence
                r"|(two|three|four|a few|several|other|two other|a couple of) [a-z ]{0,24}(ways?|options?|things?|points?|notes?|angles?|routes?)\b[^.!?]{0,40}[.:]"
                r"|(one|a) (thing|point|note|caveat|risk|detail) worth (flagging|noting|saying|knowing)\b[^.!?]{0,30}[.:]"
                r"|worth (flagging|noting|saying)\b[^.!?]{0,20}[.:])")
# The answer talking about itself instead of answering.
# A finding turned into a ban. The data never licenses a prohibition, only a tradeoff with a condition.
# A raw metric pair the reader has to divide in their head, and jargon that belongs in the reference files.
RAW_PAIR = r"\b\d+\.\d+[^.\n]{0,60}?\b(?:against|vs\.?|versus|compared with)\s+\d+\.\d+"
# Literary joins and stiff constructions. Nobody says these out loud.
# Patterns named by the no-ai-slop skill (github petergyang/no-ai-slop), the ones a regex can see honestly.
FAUX_INSIGHT = r"\b(what (most people|nobody|everyone) (gets? wrong|tells? you|misses)|the part (everyone|most people) (misses|skips)|this is the part most people skip|here is what nobody)\b"
# A colon that sets up a reveal. An ending the skill asks for ("Next call: pick the date") is not one, so let
# a decision verb through.
# The idea generator's concept sheet is a fixed set of labels the skill asks for, so those are not reveals either.
CONCEPT_LABELS = r"Title|Hook|Mechanic|Prize direction|Asset produced|Objective|Budget|Channels"
COLON_REVEAL = (r"(?m)^(?!(?:" + CONCEPT_LABELS + r")\s*:)"
                r"[A-Z](?![^.!?:\n]{0,60}"
                r"(?:day|days|week|weeks|month|months|hour|hours|out|later|before|after|launch|onwards)\s*:)"
                r"[^.!?:\n]{6,60}: "
                r"(?!(?:pick|choose|confirm|decide|set|send|run|draw|write|book|check|start|close|tell|give|use|keep|drop|add|reply|ask)\b)[a-z]")
PUFFERY = r"\b(a testament to|marks? a pivotal|plays? a vital role|solidif\w+ its position|underscor\w+ (its|the) (significance|importance)|speaks? volumes)\b"
WEASEL = r"\b(experts agree|studies show|research shows|industry reports suggest|many argue|widely regarded as|it is (widely )?believed)\b"
SUPERFICIAL = r", (highlighting|underscoring|reflecting|showcasing|demonstrating|signal(l)?ing) (the|its|a|an|how|that)\b"
METADISCOURSE = r"\b(each worth naming|worth naming|the key point is|that last part matters|this distinction matters|as you can see|in other words|which is to say|the important thing here)\b"
RHETORICAL = r"\b(what if i told you|think about it:|plot twist:|here is the thing|here's the thing|let me be clear|the uncomfortable truth)\b"
RECAP = r"(?i)\b(in conclusion|to recap|ultimately,|overall,|to sum up|all in all)\b"
# Gleam's own words must arrive capitalised, because the reader has the dashboard open beside the answer.
APP_LOWER = r"(?<![A-Za-z`\-])(impressions|conversion rate|entry methods?|viral shares?|email subscriptions?|secret code|visit a page|answer a question|chat members?|custom actions?|app downloads?|loyalty bonus(es)?|file uploads?|entrants?|contestants?|prizes?|winners?)\b"
STIFF = r"\b(works the other way|pulls? in the opposite direction|the picture reverses|comes at a cost|on the other hand|that said|conversely|by contrast|it is worth (noting|remembering)|bear in mind|one thing to note)\b"
JARGON = r"\b(contestant band|size band|per contestant|n\s*=\s*\d|stratified|cohort|controlled for|unstratified|clean subset|ordinary segment|uptake|extracted)\b"
BAN = r"\b(so (skip|avoid|drop|do not add|don't add|do not use|don't use)|(skip|avoid) (the|a|an|any) \w+ action|not worth (adding|offering|running|using)|(do not|don't) (bother|add|offer) [a-z]|leave (it|that|the \w+) out)\b"
META = r"\b(this (answer|reply|response|recommendation) (is|does|gives|covers)|(i|we) (sent|gave|listed|showed) (you|above)|as (i|we) (said|noted) above|the (list|table|numbers) above (is|are|shows)|to summari[sz]e|in short,|in summary)\b"



# Gleam's product nouns are checked on prose only. A file name, a flag or a URL carries the word in lower case by
# necessity (`references/prize-taxonomy.md`, `--winners-csv`, /setup/prizes), and flagging those would teach an
# answer to stop citing its sources.
CODEISH = re.compile(r"```.*?```|`[^`]*`|https?://\S+|\B--[a-z][\w-]*|\b[\w./-]+\.(?:md|json|csv|py|txt)\b", re.S)


def prose_only(text):
    return CODEISH.sub(" ", text)


# A fenced block, a markdown table row and a pasted dict are not sentences. Counting them put a "longest
# sentence" of 234 words into a report that then stamped itself PASS, so the variety gate was reading a
# code block as prose and waving through answers that had no long sentence at all.
def sentences(text):
    # A line break ends a sentence here. Answers are markdown, where a paragraph, a bullet, a heading and a
    # template's "Subject:" line each occupy one line, and a subject line carries no full stop. Without this,
    # a subject line merged into the sentence under it and the runaway counter fired on the reference's own
    # template. Wrapped prose would be undercounted, and nothing in this repo wraps a paragraph.
    body = re.sub(r"```.*?```", " ", text, flags=re.S)
    out = []
    for line in body.split("\n"):
        if line.lstrip().startswith("|"): continue
        out += [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", line).strip()) if s]
    return out


def check(text):
    sents = sentences(text)
    lens = [len(s.split()) for s in sents]
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    label = sum(1 for p in paras for first in [re.split(r"(?<=[.!?])\s", p, 1)[0]] if re.match(LABEL_OPENER, first.strip().lstrip("*- "), re.I))
    # An inline bold label runs into the sentence. A bold name alone on its line is a title, which some answers need.
    bold_leads = sum(1 for p in paras if re.match(r"^\*\*[^*]{2,60}\*\*[.:]? +\S", p))
    last = sents[-1] if sents else ""
    ACTION = r"\b(pick|choose|send|run|set|ask|check|start|close|draw|tell|give|use|keep|drop|add|book|write|say|decide|confirm|next decision|next step)\b"
    asks = last.strip().endswith("?") and re.search(r"\byou(r|'ll|'re|'ve)?\b", last, re.I)
    # An offer is not a next step. "Want the DM template?" hands the work back and reads as an assistant
    # touting for more turns, where the reader wanted to be told what to do on Monday. A closing question
    # still earns its place when it asks for the one fact that would change the recommendation.
    offer = int(bool(last.strip().endswith("?") and re.search(OFFER, last, re.I)))
    empty_end = int(bool(last) and not asks and not re.search(r"\d", last) and len(last.split()) < 22 and not re.search(ACTION, last.lower()))
    return {
        "em_dashes": text.count("—"),
        "semicolons": sum(1 for l in text.split("\n") if ";" in l and not l.startswith("|")),
        "curly_quotes": len(re.findall("[“”‘’]", text)),
        "filler_words": len(re.findall(FILLER, text, re.I)),
        "assistant_opener": int(bool(re.search(OPENERS, text.strip(), re.I))),
        "assistant_closer": len(re.findall(CLOSERS, text, re.I)),
        "contrast_sentences": len(re.findall(CONTRAST, text, re.I)),
        "question_headings": len(re.findall(r"^#+ .*\?$|^\*\*[^*]*\?\*\*$", text, re.M)),
        "label_openers": label,
        "bold_lead_ins": bold_leads if bold_leads >= 3 else 0,
        "meta_commentary": len(re.findall(META, text, re.I)),
        "raw_metric_pairs": len(re.findall(RAW_PAIR, text, re.I)),
        "faux_insight": len(re.findall(FAUX_INSIGHT, text, re.I)),
        "colon_reveals": len(re.findall(COLON_REVEAL, text)),
        "puffery": len(re.findall(PUFFERY, text, re.I)),
        "weasel_attribution": len(re.findall(WEASEL, text, re.I)),
        "superficial_analysis": len(re.findall(SUPERFICIAL, text, re.I)),
        "metadiscourse": len(re.findall(METADISCOURSE, text, re.I)),
        "rhetorical_setups": len(re.findall(RHETORICAL, text, re.I)),
        "recap_endings": len(re.findall(RECAP, text)),
        "lowercase_app_terms": len(re.findall(APP_LOWER, prose_only(text))),
        "stiff_phrases": len(re.findall(STIFF, text, re.I)),
        "no_second_person": int(len(re.findall(r"\byou(r|'ll|'re|'ve)?\b", text, re.I)) == 0 and len(text.split()) > 60),
        "reader_facing_jargon": len(re.findall(JARGON, text, re.I)),
        "bans_without_a_reason": len([m for m in re.finditer(BAN, text, re.I) if not re.search(r"(rule|law|legal|jurisdiction|terms of service|platform|prohibit|forbid|fraud|risk|purchase to enter|lottery)", text[max(0,m.start()-260):m.end()+260], re.I)]),
        "empty_ending": empty_end,
        "offer_endings": offer,
        "shortest_sentence": min(lens) if lens else 0,
        "longest_sentence": max(lens) if lens else 0,
        # Past about forty-five words the reader has lost the subject. The variety gate only asks for one
        # long sentence, so with no ceiling it rewarded the runaway it should have caught.
        "runaway_sentences": sum(1 for n in lens if n > 45),
    }

# Same patterns, keyed by the counter they feed, so --show can quote what tripped each one.
SHOW = {"filler_words": (FILLER, re.I), "assistant_closer": (CLOSERS, re.I), "contrast_sentences": (CONTRAST, re.I),
        "meta_commentary": (META, re.I), "raw_metric_pairs": (RAW_PAIR, re.I), "faux_insight": (FAUX_INSIGHT, re.I),
        "colon_reveals": (COLON_REVEAL, 0), "puffery": (PUFFERY, re.I), "weasel_attribution": (WEASEL, re.I),
        "superficial_analysis": (SUPERFICIAL, re.I), "metadiscourse": (METADISCOURSE, re.I),
        "rhetorical_setups": (RHETORICAL, re.I), "recap_endings": (RECAP, 0), "lowercase_app_terms": (APP_LOWER, 0),
        "stiff_phrases": (STIFF, re.I), "reader_facing_jargon": (JARGON, re.I), "bans_without_a_reason": (BAN, re.I)}


def show(text):
    """Quote what tripped each detector, so a fix lands on the sentence rather than on a guess."""
    out = []
    for name, (pat, flags) in SHOW.items():
        for m in re.finditer(pat, text, flags):
            line = text[:m.start()].count("\n") + 1
            out.append((name, line, text[max(0, m.start() - 40):m.end() + 40].replace("\n", " ").strip()))
    paras = [p.strip() for p in text.split("\n\n") if p.strip()]
    for p in paras:
        first = re.split(r"(?<=[.!?])\s", p, 1)[0].strip().lstrip("*- ")
        if re.match(LABEL_OPENER, first, re.I):
            out.append(("label_openers", text[:text.find(p)].count("\n") + 1, first[:90]))
    return sorted(out, key=lambda r: r[1])


def self_test():
    """The two fixtures in evals/fixtures are the contract: one answer that must fail, one that must pass."""
    import os
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")
    if not os.path.isdir(d):
        # A copy of this file ships inside each skill so a folder installed on its own can still lint a
        # draft. The fixtures stay at the repo root, where CI runs the real self-test against them.
        print("no fixtures here, so nothing to self-test. This copy lints a draft: "
              "python3 scripts/style_check.py draft.txt")
        return
    bad, good = check(open(os.path.join(d, "fails.txt")).read()), check(open(os.path.join(d, "passes.txt")).read())
    raw = check(open(os.path.join(d, "fails_raw.txt")).read())
    stiff = check(open(os.path.join(d, "fails_stiff.txt")).read())
    pat = check(open(os.path.join(d, "fails_patterns.txt")).read())
    lc = check(open(os.path.join(d, "fails_lowercase.txt")).read())
    lab = check(open(os.path.join(d, "fails_labels.txt")).read())
    bold = check(open(os.path.join(d, "fails_bold.txt")).read())
    assert bold["bold_lead_ins"] >= 3, bold
    assert lab["label_openers"] >= 2, lab
    assert lc["lowercase_app_terms"] >= 5, lc
    for k in ("faux_insight", "colon_reveals", "puffery", "weasel_attribution", "superficial_analysis",
              "metadiscourse", "rhetorical_setups", "recap_endings"):
        assert pat[k] >= 1, (k, pat)
    assert stiff["stiff_phrases"] >= 1, stiff
    assert raw["raw_metric_pairs"] >= 1 and raw["reader_facing_jargon"] >= 2, raw
    assert bad["label_openers"] == 3 and bad["meta_commentary"] == 1 and bad["bans_without_a_reason"] == 1, bad
    assert all(good[k] == 0 for k in ("em_dashes", "semicolons", "curly_quotes", "assistant_opener", "assistant_closer",
                                      "question_headings", "label_openers", "bold_lead_ins", "meta_commentary",
                                      "bans_without_a_reason", "empty_ending")), good
    assert good["shortest_sentence"] <= 8 and good["longest_sentence"] >= 18, good
    # the verdict must block on the two commonest faults, which it silently did not for a long time
    import subprocess as _sp, tempfile as _tf, os as _os
    with _tf.NamedTemporaryFile("w", suffix=".txt", delete=False) as fh:
        fh.write("Pick the coffee subscription, not the laptop. It pulls buyers.\n"
                 "You get a tighter list. Ask them which matters more to you this quarter.\n")
    out = _sp.run([sys.executable, _os.path.abspath(__file__), fh.name], capture_output=True, text=True).stdout
    assert "FAIL" in out, f"a contrast sentence must block the verdict, got: {out}"
    with open(fh.name, "w") as f2:
        f2.write("This actually leverages a robust approach. You should pick one.\n"
                 "Ask them which matters more to you this quarter.\n")
    out = _sp.run([sys.executable, _os.path.abspath(__file__), fh.name], capture_output=True, text=True).stdout
    assert "FAIL" in out, f"filler words must block the verdict, got: {out}"
    with open(fh.name, "w") as f2:
        f2.write("Run it on 19 November and close on 26 November.\n"
                 "That lands the draw before the shipping cut-off and leaves you nine clear days to promote it.\n"
                 "Want the DM template?\n")
    out = _sp.run([sys.executable, _os.path.abspath(__file__), fh.name], capture_output=True, text=True).stdout
    assert "FAIL" in out, f"an offer ending must block the verdict, got: {out}"
    # a pasted code block must not be read as a long sentence, and a real runaway must fail
    subj = "# Winner notification\n\nSubject: You have won the coffee machine\n\nReply by Friday.\n"
    assert check(subj)["runaway_sentences"] == 0, check(subj)
    fenced = "Pick it. " + "```\n" + " ".join(["word"] * 80) + "\n```\n"
    assert check(fenced)["longest_sentence"] < 45, check(fenced)
    assert check("You " + " ".join(["run"] * 60) + " today.")["runaway_sentences"] == 1
    _os.unlink(fh.name)
    print("self-test passed")

if __name__ == "__main__":
    if "--self-test" in sys.argv[1:]:
        self_test(); sys.exit(0)
    verbose = "--show" in sys.argv[1:]
    for path in [a for a in sys.argv[1:] if not a.startswith("--")]:
        text = open(path).read()
        r = check(text)
        # contrast_sentences and filler_words were left out of this sum, so the two commonest faults in
        # every measured run were the two the checker never failed on. 94 contrast sentences and 38 filler
        # words across forty answers, every one of them reported and none of them blocking.
        hard = (r["contrast_sentences"] + r["filler_words"]
                + r["em_dashes"] + r["semicolons"] + r["curly_quotes"] + r["assistant_opener"] + r["assistant_closer"]
                + r["question_headings"] + r["label_openers"] + r["bold_lead_ins"] + r["meta_commentary"] + r["empty_ending"]
                + r["bans_without_a_reason"] + r["raw_metric_pairs"] + r["reader_facing_jargon"] + r["stiff_phrases"] + r["no_second_person"] + r["lowercase_app_terms"] + r["faux_insight"] + r["colon_reveals"] + r["puffery"]
                + r["weasel_attribution"] + r["superficial_analysis"] + r["metadiscourse"] + r["rhetorical_setups"] + r["recap_endings"]
                + r["runaway_sentences"] + r["offer_endings"])
        varied = r["shortest_sentence"] <= 8 and r["longest_sentence"] >= 18
        print(f"{path}: {'PASS' if hard == 0 and varied else 'FAIL'} {r}")
        if verbose:
            for name, line, quote in show(text):
                print(f"  {name} line {line}: {quote}")
