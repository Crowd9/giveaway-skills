#!/usr/bin/env python3
"""Count the style tells that eval case 10 forbids. Usage: python3 style_check.py reply.txt [more.txt ...]"""
import re, sys

FILLER = r"\b(actually|leverage|robust|comprehensive|streamline|delve|foster|pivotal|landscape|testament|showcase|furthermore|moreover|additionally|it is worth noting|generally speaking|in many cases)\b"
OPENERS = r"^(great question|here's how i'd think|here is how|let me walk you|certainly|of course|sure[,!])"
CLOSERS = r"(hope this helps|let me know if|feel free to|happy to elaborate)"
CONTRAST = r"(, not \w|\bnot \w+(?: \w+){0,4}, (?:but|it's|it is)\b|\brather than\b|\binstead of\b|, don't \w)"

def check(text):
    sents = [s for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\s+", " ", text)) if s.strip()]
    lens = [len(s.split()) for s in sents]
    return {
        "em_dashes": text.count("—"),
        "semicolons": sum(1 for l in text.split("\n") if ";" in l and not l.startswith("|")),
        "curly_quotes": len(re.findall("[“”‘’]", text)),
        "filler_words": len(re.findall(FILLER, text, re.I)),
        "assistant_opener": int(bool(re.search(OPENERS, text.strip(), re.I))),
        "assistant_closer": len(re.findall(CLOSERS, text, re.I)),
        "contrast_sentences": len(re.findall(CONTRAST, text, re.I)),
        "question_headings": len(re.findall(r"^#+ .*\?$|^\*\*[^*]*\?\*\*$", text, re.M)),
        "shortest_sentence": min(lens) if lens else 0,
        "longest_sentence": max(lens) if lens else 0,
    }

if __name__ == "__main__":
    for path in sys.argv[1:]:
        r = check(open(path).read())
        hard = r["em_dashes"] + r["semicolons"] + r["curly_quotes"] + r["assistant_opener"] + r["assistant_closer"] + r["question_headings"]
        print(f"{path}: {'PASS' if hard == 0 and r['shortest_sentence'] <= 6 and r['longest_sentence'] >= 25 else 'FAIL'} {r}")
