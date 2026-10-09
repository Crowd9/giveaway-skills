#!/usr/bin/env python3
"""Check saved answers. Exit 0 PASS, 1 FAIL, 2 UNASSESSED or invalid input.

Usage: check_deliverable.py evals.json CASE_ID answer.txt [--review review.json]
Mechanical checks use contains, count/min, or not_count (a forbidden regex).
Meaning checks use review_checks with id, criterion, pass_example, fail_example.
A human or independent reviewer supplies {check_id: {passed: bool, reason: str}}
in review.json after reading the answer. Missing reviews are UNASSESSED. Regex
checks only catch specified forms and do not substitute for meaning review.
"""
import argparse
import json
from pathlib import Path
import re
import sys


def validate_cases(cases):
    ids = [str(case["id"]) for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate case ids")
    for case in cases:
        review_ids = []
        for check in case.get("review_checks", []):
            for key in ("id", "criterion", "pass_example", "fail_example"):
                if not isinstance(check.get(key), str) or not check[key].strip():
                    raise ValueError(f"case {case['id']}: invalid review check {key}")
            review_ids.append(check["id"])
        if len(review_ids) != len(set(review_ids)):
            raise ValueError(f"case {case['id']}: duplicate review check ids")


def run(checks, text):
    miss = []
    for c in checks:
        if "contains" in c:
            if c["contains"] not in text:
                miss.append(f'missing {c["contains"]!r}')
        elif "not_count" in c:
            if re.search(c["not_count"], text, re.M):
                miss.append(f'forbidden recommendation matches {c["not_count"]!r}')
        else:
            n = len(re.findall(c["count"], text, re.M))
            if n < c.get("min", 1):
                miss.append(f'{c["count"]!r}: found {n}, need {c.get("min", 1)}')
    return miss


def assess(case, text, reviews=None):
    checks = case.get("checks", [])
    meaning = case.get("review_checks", [])
    reviews = {} if reviews is None else reviews
    if not isinstance(reviews, dict):
        raise ValueError("review must be an object keyed by review check id")
    unknown = set(reviews) - {c["id"] for c in meaning}
    if unknown:
        raise ValueError(f"unknown review check ids: {', '.join(sorted(unknown))}")
    miss = run(checks, text)
    pending = []
    for check in meaning:
        verdict = reviews.get(check["id"])
        if verdict is None:
            pending.append(check["id"])
            continue
        if (not isinstance(verdict, dict) or type(verdict.get("passed")) is not bool
                or not isinstance(verdict.get("reason"), str) or not verdict["reason"].strip()):
            raise ValueError(f"review {check['id']} needs boolean passed and nonempty reason")
        if not verdict["passed"]:
            miss.append(f"{check['id']}: {verdict['reason']}")
    status = "FAIL" if miss else "UNASSESSED" if pending or not (checks or meaning) else "PASS"
    return status, miss, pending


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("evals")
    parser.add_argument("case")
    parser.add_argument("answer")
    parser.add_argument("--review")
    args = parser.parse_args()
    try:
        cases = json.loads(Path(args.evals).read_text())["evals"]
        validate_cases(cases)
        case = next((e for e in cases if str(e["id"]) == args.case), None)
        if case is None:
            raise ValueError(f"unknown case id {args.case}")
        reviews = json.loads(Path(args.review).read_text()) if args.review else None
        status, miss, pending = assess(case, Path(args.answer).read_text(), reviews)
    except (OSError, ValueError, KeyError, TypeError, re.error) as error:
        print(f"ERROR: {error}")
        return 2
    print(f"case {args.case}: {status} ({len(case.get('checks', []))} mechanical checks)")
    for message in miss:
        print("  " + message)
    for check_id in pending:
        print("  needs meaning review: " + check_id)
    return {"PASS": 0, "FAIL": 1, "UNASSESSED": 2}[status]


if __name__ == "__main__":
    sys.exit(main())
