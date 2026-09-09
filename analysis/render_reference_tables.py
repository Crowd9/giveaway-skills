#!/usr/bin/env python3
"""Rewrite the generated tables inside the skill references from analysis/output/benchmarks.json.
Tables sit between <!-- generated:NAME --> and <!-- /generated --> markers; prose around them is untouched."""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFS = [os.path.join(ROOT, "skills", d, "references") for d in os.listdir(os.path.join(ROOT, "skills")) if os.path.isdir(os.path.join(ROOT, "skills", d, "references"))]
b = json.load(open(os.path.join(ROOT, "analysis", "output", "benchmarks.json")))
o, s = b["ordinary_benchmark"], b["source"]

LABELS = {"tech_hardware": ("Tech hardware", "PCs, GPUs, consoles, phones, peripherals, monitors, audio, smart devices"),
 "gift_card_or_cash": ("Gift card or cash", "Store gift cards, vouchers, cash, store credit, shopping sprees"),
 "game_item_or_skin": ("Game items or skins", "Game keys and copies, in-game currency, cosmetic skins, editions"),
 "regulated_goods_firearm": ("Regulated goods (firearms)", "Firearms, ammunition, parts and optics, from specialist retailers"),
 "bundle_or_box": ("Bundle or box", "Packs, kits, setups, boxes, partner bundles, mystery boxes"),
 "merch_apparel_collectible": ("Merch, apparel, collectibles", "Signed items, jerseys, hoodies, sneakers, bags, replicas, comics"),
 "experience_travel_tickets": ("Experience, travel, tickets", "Trips, stays, cruises, event tickets, concerts, guided experiences"),
 "home_garden_appliance": ("Home, garden, appliance", "Grills, kitchen appliances, furniture, decor, power stations, wellness devices"),
 "sports_outdoor_gear": ("Sports and outdoor gear", "Fitness, bikes, fishing, hunting gear, camping, archery, EDC knives"),
 "tools_craft_diy": ("Tools, craft, DIY", "Power tools, 3D printers and filament, crafting machines, epoxy"),
 "subscription_membership": ("Subscription or membership", "Annual plans, lifetime memberships, a year of a product, courses"),
 "vehicle": ("Vehicle", "Cars, trucks, motorcycles, e-bikes, outboard motors"),
 "toys_collectibles": ("Toys and collectibles", "LEGO, figures, statues, plush, board games"),
 "music_gear": ("Music gear", "Guitars, pianos, pedals, recording equipment"),
 "food_drink_consumables": ("Food, drink, consumables", "Food, drink, supplements, a year's supply of consumables"),
 "beauty_wellness": ("Beauty and wellness", "Skincare, grooming, wellness products"),
 "exclusive_access": ("Exclusive access", "Beta keys, playtests, creator interaction, community roles"),
 "services": ("Services", "Car washes, courses, insurance, consultations"),
 "baby_kids": ("Baby and kids", "Cribs, strollers, baby products"),
 "art_custom": ("Art and custom", "Artwork, prints, commissions"),
 "pet_products": ("Pet products", "Pet supplies"),
 "discount_or_coupon": ("Discount or coupon", "Discount codes, coupons, cashback. Requires a purchase, so a weak prize"),
 "bullion_precious_metal": ("Bullion", "Silver and gold bars, rounds, coins"),
 "placeholder_name": ("Placeholder name", "\"1st Prize\", \"Winner\", a campaign title reused: the record does not say what the prize was"),
 "other_unclassified": ("Unclassified", "Neither rules nor the label pass could place them (opaque brand codes, ambiguous short names)")}

def n(x): return f"{x:,}" if isinstance(x, int) else (f"{x:,.0f}" if isinstance(x, float) else str(x))

def taxonomy():
    rows = ["| Category | What it covers | Prize records | Campaigns | Organizers | Value stated | Stated USD median (n) |", "|---|---|---|---|---|---|---|"]
    cats = o["by_prize_category"]
    order = sorted((k for k in cats if k not in ("placeholder_name", "other_unclassified")), key=lambda k: -cats[k]["prize_records"]) + ["placeholder_name", "other_unclassified"]
    for k in order:
        v = cats[k]; lab, desc = LABELS.get(k, (k, "")); sv = v["stated_value_usd"]
        med = f"{n(sv['median'])} ({n(sv['n'])})" if sv["n"] else "none"
        rows.append(f"| {lab} | {desc} | {n(v['prize_records'])} | {n(v['campaigns'])} | {n(v['unique_organizers'])} | {v['value_stated_share']:.0%} | {med} |")
    src = o["category_source"]
    rows.append(f"\nCategories were assigned in two passes: name-pattern rules ({n(src.get('rule', 0))} records) and, only where rules failed, a private LLM-assisted label pass over the leftover names ({n(src.get('label', 0))} records). Small categories are listed for completeness and are too thin to benchmark.")
    return "\n".join(rows)

def segments():
    seg = b["segments"]; ex = {k: b["excluded_" + k] for k in ("crypto", "ambiguous", "purchase_opportunity")}
    return "\n".join(["| Segment | Campaigns | Handling |", "|---|---|---|",
        f"| Ordinary | {n(seg['ordinary'])} ({n(o['prize_records'])} prize records, {n(o['unique_organizers'])} organizers) | Basis for every default figure |",
        f"| Crypto | {n(seg['crypto'])} | Excluded. Described only when a user asks for crypto advice. {ex['crypto']['wallet_address_entry_method_share']:.0%} used a wallet-address entry method |",
        f"| Ambiguous | {n(seg['ambiguous'])} | Excluded and reported separately |",
        f"| Purchase opportunity | {n(seg['purchase_opportunity'])} | Excluded. The prize is the right to buy something |",
        f"\nExcluded campaigns are similar in size to ordinary ones (crypto median {n(ex['crypto']['valid_contestants']['median'])} contestants versus {n(o['valid_contestants']['median'])} ordinary), so exclusion changes who is in the benchmark and leaves the size distribution alone."])

def benchmark():
    v = o["valid_contestants"]; e = o["entries_per_contestant"]; d = o["duration_days"]; u = o["stated_prize_value_by_currency"]; t = o["campaign_total_stated_value_usd_fully_valued_campaigns"]
    rows = ["| Measure | Value | n or note |", "|---|---|---|",
        f"| Valid contestants | median {n(v['median'])}, IQR {n(v['p25'])} to {n(v['p75'])}, 90th pct {n(v['p90'])} | {n(v['n'])}. Floor is {n(v['min'])} by selection |",
        f"| Valid entries | median {n(o['valid_entries']['median'])} | {n(o['valid_entries']['n'])}. Entries count actions, and one person makes many |",
        f"| Entries per contestant | median {e['median']}, IQR {e['p25']} to {e['p75']} | {n(e['n'])} |",
        f"| Impressions | median {n(o['impressions_where_nonzero']['median'])} | {n(o['impressions_where_nonzero']['n'])} with a non-zero value. Zeros treated as unknown |",
        f"| Duration | median {n(d['median'])} days, IQR {n(d['p25'])} to {n(d['p75'])} | {n(d['n'])}. Maximum {n(d['max'])} days (evergreen campaigns) |",
        f"| One prize record | {o['single_prize_record_share']:.1%} of campaigns | quantity may still exceed 1 |",
        f"| Any quantity above 1 | {o['any_prize_quantity_gt1_share']:.1%} of campaigns | |",
        f"| Prize value stated | {o['prize_value_stated_share']:.1%} of prize records | {1 - o['prize_value_stated_share']:.1%} unknown |"]
    for c in sorted(u, key=lambda k: -u[k]["n"]):
        x = u[c]
        if c == "null": continue
        rows.append(f"| Stated {c} values | median {n(x['median'])}, IQR {n(x['p25'])} to {n(x['p75'])}, 90th pct {n(x['p90'])} | {n(x['n'])} records" + (". Too few to use" if x["n"] < 30 else "") + f". Max {n(x['max'])} |")
    rows += [f"| Fully valued campaign totals (USD) | median {n(t['median'])}, IQR {n(t['p25'])} to {n(t['p75'])} | {n(t['n'])} campaigns. Max {n(t['max'])} |",
        f"| Repeat organizers | {n(o['organizers_with_5_plus_campaigns'])} organizers with 5+ campaigns account for {o['share_of_campaigns_from_repeat_organizers']:.1%} of campaigns | patterns can reflect prolific accounts |",
        f"| Plan tier | " + ", ".join(f"{k} {n(v)}" for k, v in o["tier"].items()) + " | tier at export time |"]
    return "\n".join(rows)

def bands():
    bb = o.get("by_contestant_band", {})
    if not bb: return "(no band data)"
    rows = ["| Band (valid contestants) | Campaigns | Organizers | Value stated | Stated USD median (n) | Campaign total USD median (n) | One prize record | Entries per contestant | Duration median |", "|---|---|---|---|---|---|---|---|---|"]
    for k, v in bb.items():
        rows.append(f"| {k} | {n(v['campaigns'])} | {n(v['unique_organizers'])} | {v['prize_value_stated_share']:.0%} | {n(v['stated_value_usd'].get('median'))} ({n(v['stated_value_usd']['n'])}) | {n(v['campaign_total_stated_value_usd'].get('median'))} ({n(v['campaign_total_stated_value_usd']['n'])}) | {v['single_prize_record_share']:.0%} | {v['entries_per_contestant_median']} | {n(v['duration_days_median'])} days |")
    cats = ["tech_hardware", "gift_card_or_cash", "bundle_or_box", "experience_travel_tickets", "game_item_or_skin", "merch_apparel_collectible", "home_garden_appliance", "regulated_goods_firearm", "sports_outdoor_gear", "food_drink_consumables", "subscription_membership", "discount_or_coupon"]
    rows += ["", "Primary prize category (first prize record) by band, share of campaigns:", "", "| Category | " + " | ".join(bb) + " |", "|---|" + "---|" * len(bb)]
    for c in cats:
        rows.append(f"| {LABELS.get(c, (c,))[0]} | " + " | ".join(f"{v['primary_prize_category_share'].get(c, 0):.1%}" for v in bb.values()) + " |")
    return "\n".join(rows)

def entry_families():
    em = o["entry_methods"]
    rows = ["| Action family | Campaigns using it | Share of campaigns | Uptake median (IQR) | n with uptake |", "|---|---|---|---|---|"]
    for f, v in em["families"].items():
        if f in ("Crypto wallet", "Other"): continue
        u = v["uptake"]
        rows.append(f"| {f} | {n(v['campaigns'])} | {v['share_of_campaigns']:.0%} | {u.get('median', 0):.2f} ({u.get('p25', 0):.2f} to {u.get('p75', 0):.2f}) | {n(u['n'])} |")
    m = em["methods_per_campaign"]
    rows.append(f"\nMethods per campaign: median {n(m['median'])}, IQR {n(m['p25'])} to {n(m['p75'])}, 90th percentile {n(m['p90'])} (n={n(m['n'])}). {em['definition']}")
    return "\n".join(rows)

def entry_by_band():
    bb = o["entry_methods"]["by_band"]
    fams = ["Visit a page or profile", "Follow or subscribe (free)", "Share, repost or refer", "Email or newsletter signup", "Bonus, loyalty or code", "Join a community", "Answer a question or poll", "Post or create content", "Connect an account to enter", "Download or play"]
    rows = ["| Action family | " + " | ".join(bb) + " |", "|---|" + "---|" * len(bb)]
    for f in fams: rows.append(f"| {f} | " + " | ".join(f"{v['share_with_family'].get(f, 0):.0%}" for v in bb.values()) + " |")
    rows.append("| Methods per campaign (median) | " + " | ".join(n(v["methods_per_campaign_median"]) for v in bb.values()) + " |")
    return "\n".join(rows)

def timing():
    t = o["timing"]; d = t["duration_days"]
    rows = [f"Duration: median {n(d['median'])} days, IQR {n(d['p25'])} to {n(d['p75'])}, 90th percentile {n(d['p90'])} (n={n(d['n'])}). By campaign size: " + ", ".join(f"{k} {n(v)} days" for k, v in t["duration_median_by_band"].items()) + ".", "",
        "| Duration (days) | Share of campaigns | Entries per contestant, median |", "|---|---|---|"]
    for k, v in t["duration_bucket_share"].items(): rows.append(f"| {k} | {v:.0%} | {t['entries_per_contestant_median_by_duration'].get(k, '')} |")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    rows += ["", "| Start month | " + " | ".join(months) + " |", "|---|" + "---|" * 12, "| Share of campaigns | " + " | ".join(f"{t['start_month_share'][str(i)]:.1%}" for i in range(1, 13)) + " |", "",
        "| Start weekday | " + " | ".join(t["start_weekday_share"]) + " |", "|---|" + "---|" * 7, "| Share of campaigns | " + " | ".join(f"{v:.1%}" for v in t["start_weekday_share"].values()) + " |"]
    return "\n".join(rows)

def structure_detail():
    sd = o["structure_detail"]; u = sd["total_prize_units"]
    rows = ["| Prize records per campaign | Share |", "|---|---|"] + [f"| {k} | {v:.1%} |" for k, v in sd["prize_records_per_campaign_share"].items()]
    rows += ["", f"Total prize units per campaign: median {n(u['median'])}, 75th percentile {n(u['p75'])}, 90th percentile {n(u['p90'])}, maximum {n(u['max'])} (n={n(u['n'])}). {sd['share_more_than_one_unit']:.0%} of campaigns list more than one unit and {sd['share_tiered_positions']:.0%} list tiered prizes (more than one position).", "",
        "| Band | Single unit | Tiered prizes | Ten or more units |", "|---|---|---|---|"]
    for k, v in sd["by_band"].items(): rows.append(f"| {k} | {v['share_single_unit']:.0%} | {v['share_tiered']:.0%} | {v['share_ten_plus_units']:.0%} |")
    return "\n".join(rows)

CMP = json.load(open(os.path.join(ROOT, "analysis", "output", "comparisons.json"))) if os.path.exists(os.path.join(ROOT, "analysis", "output", "comparisons.json")) else None

def cmp_table(key, label):
    if not CMP: return "(comparisons.json missing)"
    g = CMP[key]; rows = [f"| {label} | Campaigns | Contestants | Entries per entrant | Contestants per impression | Impressions per contestant | Methods |", "|---|---|---|---|---|---|---|"]
    base = None
    for k, v in g.items():
        if base is None: base = v
        rel = lambda f: (f" ({(v[f] / base[f] - 1) * 100:+.0f}%)" if v is not base and base.get(f) and v.get(f) else "")
        rows.append(f"| {k} | {n(v['n'])} | {n(v['contestants'])}{rel('contestants')} | {v['entries_per_entrant']:.2f}{rel('entries_per_entrant')} | {v['contestants_per_impression']:.0%}{rel('contestants_per_impression')} | {v['impressions_per_contestant']:.1f} | {n(v['methods'])} |")
    return "\n".join(rows)

def cmp_recency_by_vertical():
    if not CMP: return ""
    rows = ["| Vertical (regex proxy) | First campaigns | Within 30 days | Contestants | Contestants per impression |", "|---|---|---|---|---|"]
    for v, r in CMP["recency_by_vertical_clean"].items(): rows.append(f"| {v} | {n(r['first_n'])} | {n(r['within30_n'])} | {r['contestants_rel']:+.0%} | {r['conversion_rel']:+.0%} |")
    return "\n".join(rows)

GEN = {"taxonomy": taxonomy, "segments": segments, "benchmark": benchmark, "bands": bands, "entry_families": entry_families, "entry_by_band": entry_by_band, "timing": timing, "structure_detail": structure_detail,
       "cmp_repeatable": lambda: cmp_table("repeatable_actions_all", "Repeatable actions"), "cmp_duration": lambda: cmp_table("duration_no_repeatable", "Duration, no repeatable actions"),
       "cmp_methods": lambda: cmp_table("method_count_clean", "Entry methods, clean subset"), "cmp_share": lambda: cmp_table("share_action_clean", "Share action, clean subset"),
       "cmp_email": lambda: cmp_table("email_clean", "Email signup, clean subset"), "cmp_recency": lambda: cmp_table("recency_clean", "Gap since previous campaign, clean subset"),
       "cmp_weekday": lambda: cmp_table("weekday_all", "Start weekday"), "cmp_vertical": lambda: cmp_table("vertical_clean", "Vertical, clean subset"), "cmp_recency_vertical": cmp_recency_by_vertical}
for REF in REFS:
  for f in os.listdir(REF):
    p = os.path.join(REF, f); t = open(p).read()
    def sub(m): return f"<!-- generated:{m.group(1)} -->\n{GEN[m.group(1)]()}\n<!-- /generated -->"
    t2 = re.sub(r"<!-- generated:(\w+) -->\n.*?\n<!-- /generated -->", sub, t, flags=re.S)
    if t2 != t: open(p, "w").write(t2); print("updated", os.path.relpath(p, ROOT))
