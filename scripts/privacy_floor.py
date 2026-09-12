"""Check distinct-business counts at every depth of published aggregate JSON.

This guard checks explicit counts, including subgroup counts on comparison rows.
It cannot recover missing distinct-business counts from campaign counts. Private
generators must calculate those counts and suppress small groups before export.
"""
import re


FLOOR = 5
COUNT_KEY = re.compile(
    r"^(?:(?:n_(?:businesses|organizers|organisers))|"
    r"(?:(?:unique|distinct)_)?(?:business|organizer|organiser)_count|"
    r"(?:(?:unique|distinct|ordinary|clean|valued|collab)_)?"
    r"(?:businesses|organizers|organisers)"
    r"(?:_(?:count|sites|reached|offered|with|with_5_plus_campaigns|"
    r"top|rest|top_stratified|top_raw))?)$"
)


def privacy_problems(value, path="$"):
    """Return failures without printing group labels, which may be private.

Zero-person cohorts may describe an empty exclusion category. They are accepted
only when every numeric statistic in that object is zero and its campaign count
is explicitly zero. A parent count never excuses a smaller nested subgroup.
"""
    problems = []
    if isinstance(value, dict):
        for key, count in value.items():
            if not COUNT_KEY.fullmatch(key):
                continue
            if type(count) is not int or count < 0:
                problems.append(f"{path}: {key} must be a nonnegative integer")
            elif count < FLOOR and not (count == 0 and _empty_cohort(value)):
                problems.append(f"{path}: {key} is below the five-business privacy floor")
        for index, child in enumerate(value.values()):
            problems.extend(privacy_problems(child, f"{path}.object[{index}]"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            problems.extend(privacy_problems(child, f"{path}[{index}]"))
    return problems


def _empty_cohort(value):
    def zero_stats(child):
        if isinstance(child, dict):
            return all(zero_stats(v) for v in child.values())
        if isinstance(child, list):
            return all(zero_stats(v) for v in child)
        if isinstance(child, (int, float)):
            return type(child) is not bool and child == 0
        return child is None

    return value.get("campaigns") == 0 and zero_stats(value)
