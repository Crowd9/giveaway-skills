#!/usr/bin/env python3
"""Giveaway budget calculator. Python 3.8+, no dependencies. Every number in is an estimate and every number out is one.

Price one 500 USD grand prize and five 60 USD runner-up prizes that cost us 60% of retail, where one entrant in five is overseas.
  python3 budget.py --currency USD --prize "Grand prize" 500 1 --prize "Runner-up" 60 5 \
     --cost-ratio 0.6 --shipping 25 --international-share 0.2 --international-shipping 60 \
     --duty-rate 0.1 --tax-on-prize 0 --substitute-reserve 1 --admin-hours 6 --hourly 50 --promotion 300 --contingency 0.08
Check the arithmetic still works after an edit.
  python3 budget.py --self-test

--cost-ratio is what a unit costs you as a fraction of retail (1.0 for bought at retail, 0.5 for own product at half).
Shipping and duty apply to physical units only (add --digital to a prize to skip them).
Every figure is in one currency. For a prize bought or shipped in another, convert before you enter it and pass --rate
"1 USD = 0.92 EUR, 9 Sep 2026" so the rate and the date it was taken sit on the printed breakdown.
"""
import argparse, json, sys

def compute(a):
    prizes = []
    for p in a.prize:
        name, retail, units = p[0], float(p[1]), int(p[2]); digital = name.lower().endswith("(digital)")
        prizes.append({"name": name, "retail": retail, "units": units, "digital": digital})
    retail_total = sum(p["retail"] * p["units"] for p in prizes)
    cost_total = retail_total * a.cost_ratio
    phys_units = sum(p["units"] for p in prizes if not p["digital"])
    intl_units = round(phys_units * a.international_share, 2); dom_units = phys_units - intl_units
    shipping = dom_units * a.shipping + intl_units * a.international_shipping
    duty = sum(p["retail"] * p["units"] for p in prizes if not p["digital"]) * a.international_share * a.duty_rate
    winner_tax = retail_total * a.tax_on_prize
    substitute = a.substitute_reserve * (max((p["retail"] for p in prizes), default=0) * a.cost_ratio)
    admin = a.admin_hours * a.hourly
    subtotal = cost_total + shipping + duty + winner_tax + substitute + admin + a.promotion
    contingency = subtotal * a.contingency
    lines = [("Prize cost to you (retail x cost ratio)", cost_total), ("Shipping (domestic + international units)", shipping),
             ("Duties on international units", duty), ("Prize tax you cover", winner_tax), ("Substitute reserve", substitute),
             ("Admin time", admin), ("Promotion", a.promotion), ("Contingency", contingency)]
    total = subtotal + contingency
    return {"currency": a.currency, "prizes": prizes, "retail_value_total": retail_total, "lines": lines, "total_estimate": total,
            "headline_value_you_can_state": retail_total, "cost_per_winner": total / max(1, sum(p["units"] for p in prizes))}

def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--currency", default="USD"); ap.add_argument("--prize", nargs=3, action="append", metavar=("NAME", "RETAIL", "UNITS"), default=[])
    ap.add_argument("--cost-ratio", type=float, default=1.0); ap.add_argument("--shipping", type=float, default=0.0)
    ap.add_argument("--international-share", type=float, default=0.0); ap.add_argument("--international-shipping", type=float, default=0.0)
    ap.add_argument("--duty-rate", type=float, default=0.0); ap.add_argument("--tax-on-prize", type=float, default=0.0)
    ap.add_argument("--substitute-reserve", type=float, default=0.0, help="units of the most expensive prize held back at cost")
    ap.add_argument("--admin-hours", type=float, default=0.0); ap.add_argument("--hourly", type=float, default=0.0)
    ap.add_argument("--promotion", type=float, default=0.0); ap.add_argument("--contingency", type=float, default=0.08)
    ap.add_argument("--rate", help='exchange rate and the date you took it, e.g. "1 USD = 0.92 EUR, 9 Sep 2026"')
    ap.add_argument("--json", action="store_true"); ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test: return self_test()
    if not a.prize: ap.error("at least one --prize NAME RETAIL UNITS")
    r = compute(a)
    if a.json: print(json.dumps(r, indent=2)); return 0
    c = r["currency"]
    print(f"Retail value you can state: {c} {r['retail_value_total']:,.0f}")
    for label, v in r["lines"]: print(f"  {label:44} {c} {v:,.0f}")
    print(f"Total estimate: {c} {r['total_estimate']:,.0f}  (about {c} {r['cost_per_winner']:,.0f} per winner). Estimates only. Confirm prices and shipping quotes before committing.")
    if a.rate: print(f"Converted at {a.rate}. Rates move, so re-check before committing.")
    elif a.international_share: print(f"Multi-region prize with everything priced in {c}. Pass --rate with the exchange rate and the date you took it.")
    return 0

def self_test():
    class A: pass
    a = A(); a.currency = "USD"; a.prize = [["Grand", "500", "1"], ["Runner (digital)", "60", "5"]]; a.cost_ratio = 0.5; a.shipping = 20; a.international_share = 0.5
    a.international_shipping = 60; a.duty_rate = 0.1; a.tax_on_prize = 0; a.substitute_reserve = 1; a.admin_hours = 2; a.hourly = 50; a.promotion = 100; a.contingency = 0.1
    r = compute(a); L = dict(r["lines"])
    assert r["retail_value_total"] == 800 and L["Prize cost to you (retail x cost ratio)"] == 400
    assert abs(L["Shipping (domestic + international units)"] - (0.5 * 20 + 0.5 * 60)) < 1e-9   # one physical unit split
    assert abs(L["Duties on international units"] - 500 * 0.5 * 0.1) < 1e-9 and L["Substitute reserve"] == 250 and L["Admin time"] == 100
    assert abs(r["total_estimate"] - (400 + 40 + 25 + 0 + 250 + 100 + 100) * 1.1) < 1e-6
    print("self-test passed"); return 0

if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
