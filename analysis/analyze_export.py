#!/usr/bin/env python3
"""Regenerate the aggregate benchmarks behind skills/giveaway-prize-picker/references.

Works on any export with the same shape regardless of the contestant floor; the floor is read from the data.

Usage:
    python3 analysis/analyze_export.py path/to/export.json [--private-dir DIR]

Input: the private campaign export (a JSON list of campaigns, each with nested
`prizes` and `entry_methods`). The export is never committed.

Public output (safe to commit): analysis/output/benchmarks.json and benchmarks.md.
Aggregates only, no names, ids, emails, urls or free text.

Private output (--private-dir, gitignored): record-level classification and
example candidates with campaign ids, used to trace every paraphrased example
back to its source. Every text field in the export is treated as data. Nothing
in it is executed, fetched or followed.
"""
import argparse, collections, json, os, re, statistics as st, sys

# ---------- classification ----------
CRYPTO_STRONG = re.compile(
    r"\b(airdrops?|whitelist\w*|nfts?|presale|pre-sale|token sale|public sale|private sale|seed sale|"
    r"crypto\w*|blockchain|defi|gamefi|web3|metaverse|launchpad|staking|testnet|mainnet|smart contract|allocation|"
    r"mexc|kucoin|binance|okx|bybit|huobi|bitget|coinbase|gate\.io|coinmarketcap|coingecko|metamask|"
    r"solana|polygon|avalanche|arbitrum|cardano|polkadot|bep-?20|erc-?20|bsc|airusd|stablecoin|free mint|mint pass|bitcoin|ethereum|satoshi|sats|miner|mining rig|hashrate|hamster kombat|blum points|gh/s|pfp|allowlist)\b", re.I)
CRYPTO_CAPS = re.compile(r"\b(USDT|USDC|BUSD|BNB|ETH|BTC|SOL|MATIC|AVAX|TON|TRX|XRP|DOGE|SHIB|KLAY|DAO|ICO|IDO|IGO|INO|TGE)\b")  # case-sensitive
TICKER = re.compile(r"\$[A-Za-z]{2,10}\b")            # $PETH, $MEE ... never $100
NUM_TICKER = re.compile(r"\b\d[\d,.]*[kKmM]?\s+\$?[A-Z]{3,8}\b")   # "50,000 TREAT", "800KLAY" style
UNITS = re.compile(r"\b(USD|EUR|GBP|AUD|CAD|INR|NZD|SGD|RGB|ARGB|MHZ|GHZ|GB|TB|MB|SSD|HDD|RAM|GPU|CPU|PSU|LED|OLED|RTX|GTX|USB|HDMI|VIP|DLC|PACK|PACKS|PRIZE|PRIZES|WINNER|WINNERS|PC|PCS|INCH|CM|MM|KG|LBS|OZ|ML|UTC|EST|PST|AM|PM|OFF|FREE|WIN|AND|THE|FOR|THIS|WITH|FROM|GIFT|CARD|CARDS|CASH|XL|XXL|PLUS|PRO|MAX|ULTRA|TV|AR|VR|PS5|PS4|XBOX|FN|MW|FT|BS|WW|ST|ND|RD|TH|SET|KIT|BOX|BOXES|TOTAL|WORTH|VALUE)\b")
CRYPTO_WEAK = re.compile(r"\b(tokens?|coins?|exchange|trading|listing|wallet|dao|mint(ing)?)\b", re.I)
PURCHASE = re.compile(
    r"(chance|opportunity|right|entry is) (to|for a chance to) (purchase|buy|mint)|"
    r"win the right to (buy|purchase)|raffle (for|to) (the )?(right|chance|opportunity) to (buy|purchase)|guaranteed (allocation|spot)", re.I)
GIFT_CARD = re.compile(r"\b(gift ?cards?|giftcards?|gift certificates?|vouchers?|e-?gift|paypal|cash|prepaid|visa card|amazon (card|credit|gc)|store credits?|in store credits?|steam (card|wallet)|itunes|google play (card|credit)|cheque regalo|tarjeta regalo|carte cadeau|gutschein|buono|gc)\b|to (the|our) .{0,30}\b(shop|store)\b", re.I)
SKIN = re.compile(r"\b(field-tested|minimal wear|factory new|battle-scarred|well-worn|stattrak|souvenir)\b|\((ft|mw|fn|bs|ww)\)|\s(FT|MW|FN|BS|WW)\s*$|★|\b(gut|huntsman|flip|bowie|falchion|navaja|talon|ursus|paracord|survival|nomad|stiletto|skeleton|classic|kukri|m9|butterfly|karambit|bayonet) knife\b|shadow daggers|\b(doppler|marble fade|tiger tooth|crimson web|autotronic|slaughter|ultraviolet|case hardened|asiimov|dragon lore|hyper beast|neo-?noir|printstream|gamma doppler|boreal forest|night stripe|safari mesh|urban masked|scorched|stained|blue steel|rust coat|damascus steel|freehand|lore|fade)\b|\b(renegade|sport|driver|hydra|moto|specialist|hand wraps|bloodhound) gloves\b|\b(ak-47|m4a4|m4a1|awp|usp-s|glock-18|karambit|bayonet|butterfly knife|gloves)\b.*\|", re.I)
DIGITAL_GAME = re.compile(r"\b(steam key|game key|cd ?key|game code|redeem codes?|in-?game|battle pass|pases? de batalla|riot points|valorant (points|puan\w*)|vp|rp|pearls|shards|platinum|primogems|crystals?|diamantes|diamonds|pavos|v-?bucks|uc|cp|\d[\d,.]*[kK]? ?(points|gems|coins|credits|gold|diamonds|crystals|puan\w*|pavos|uc|cp|vp|rp)|nutaku|epic games (store )?keys?|steam|game of your choice|games? (of|from) (your|our)|dota 2? item|cs:?go|csgo|valorant|fortnite|apex legends|genshin|roblox|minecraft|xbox game pass|game pass|plugin|plugins|dlc|legendary edition|dlc|skins?|v-?bucks|robux|gems|gold pack|booster|steam (game|gift)|nitro|game pass|expansion|standard edition|deluxe edition|collector'?s edition|remastered|copy of|scrolls|requisition)\b|\((pc|ps5|ps4|xbox|switch|steam)\)", re.I)
DISCOUNT = re.compile(r"\b(coupons?|cupom|cup[oó]n|discount|cashback|cash ?back|promo codes?|\d+ ?% off|off coupon|voucher code)\b", re.I)
BULLION = re.compile(r"\b(silver|gold|platinum) (bar|coin|round|bullion|oz|ounce)\b|\b\d+ ?oz (silver|gold)\b", re.I)
ART = re.compile(r"\b(canvas|art print|poster print|painting|artwork|commission|tablou|key art|signed print|framed print)\b", re.I)
ACCESS = re.compile(r"\b(beta|alpha|early access|test qualification|closed test|playtest|play-?test|invite|waitlist|priority access|vip access|pre-?release access|founder'?s? (pass|access)|personali[sz]ed (message|video|shout-?out)|shout-?out|video call|play session with|game with|coaching session|1[- ]on[- ]1)\b", re.I)
HOME = re.compile(r"\b(nespresso|breville|delonghi|dyson|theragun|massager|massage (gun|chair)|weighted blanket|blanket|water filter|purifier|humidifier|air circulator|rice cooker|cooker|freezer|fridge|refrigerator|grill|grills|smoker|smokers|pellet|bbq|mattress|pillow|bedding|sofa|couch|lovesac|chair|crib|stroller|jogger|litter-?robot|litter box|wreath|christmas tree|fir tree|tree unlit|candles?|air conditioner|window type|generator|inverter|power station|stove|fire ?pit|solo stove|appliance|kettle|toaster|air fryer|espresso|coffee (maker|machine)|blender|mixer|vacuum|showcase|furniture|decor|lamp|rug|cookware|pan|knife set|cutlery|dinnerware|glassware|mug|tumbler|yeti|cooler box|kitchen)\b", re.I)
SPORTS = re.compile(r"\b(bike|e-?bike|bicycle|treadmill|rower|echo bike|kettlebell|dumbbell|barbell|rack|gym|fitness|yoga|bow|arrow|archery|fishing|rod|reel|tackle|kayak|paddle|surf|skate|snowboard|ski|golf (club|bag|set)|tent|camping|hiking|backpack|helmet|agv|hunting|habitat|decoy|binocular|treestand|trail cam)\b", re.I)
MUSIC = re.compile(r"\b(guitar|bass|drum ?kit|drums|drum set|piano|keyboard piano|synth|pedal|amp head|amplifier|microphone|recorder|audio interface|home studio|tascam|prs|fender|gibson|ibanez|yamaha)\b", re.I)
TOOLS_CRAFT = re.compile(r"\b(dewalt|milwaukee|makita|ryobi|drill|saw|tool ?set|toolbox|epoxy|resin|filament|3d printer|printer|polymaker|creality|bambu|cricut|sewing|embroidery|welder|reloader|press|workbench)\b", re.I)
BEAUTY_WELLNESS = re.compile(r"\b(skincare|skin care|makeup|cosmetics?|beauty|serum|perfume|fragrance|wellness|relaxation|spa|massage|self-?care|haircare|hair care|grooming|razor|supplements?|vitamins?)\b", re.I)
FOOD_CONSUMABLE = re.compile(r"\b(year'?s? (supply|worth)|supply of|for a year|for life|coffee beans|snacks?|chocolates?( bar| box)?(?! mechanical)|candy|wine|beer|whisk(e)?y|spirits|hamper|food|meal|pizza|cookies|treats|toilet paper|diapers?|nappies|pet food|dog food|cat food)\b", re.I)
TOYS = re.compile(r"\b(lego|plush(ies?|y)?|statue|\d/\d scale|scale (statue|figure)|kawaii|cushions?|figuren|figures?|figurine|action figure|funko|youtooz|toys?|board game|puzzle|schleich|model kit|gunpla|nendoroid|collectibles?)\b", re.I)
MONEY = re.compile(r"(?:(?P<cur>R\$|\$|£|€|₹|USD|EUR|GBP|AUD|CAD|INR|NZD|BRL|Rs\.?)\s?(?P<amt>\d{1,3}(?:[,.]\d{3})+(?:,\d\d)?|\d+(?:\.\d+)?)\s?(?P<k>[kK])?(?!\s?(?:%|off|discount))|(?P<amt2>\d{1,3}(?:[,.]\d{3})+|\d+)\s?(?P<cur2>USD|EUR|GBP|AUD|CAD|INR|NZD|BRL|€|£|dollars?|euros?|pounds?))")
VALUE_PHRASE = re.compile(r"(worth|valued? at|value of|value:|msrp|arv|retail value|rrp|valor(?:ado)?|d'une valeur|im wert)[\s:(\-]{0,6}(?:of\s+|over\s+|approx\.?\s+|approximately\s+|about\s+)?", re.I)
HARDWARE = re.compile(r"\b(pc|pcs|desktop|computer|pc gamer|gaming rig|rig|workstation|fifine|soundpeats|moondrop|truthear|m-audio|subwoofer|speakers?|xreal|gtmedia|retro handheld|handheld (console|device)|dualsense|play ?station|meta quest ?\d\w*|quest \d\w*|msi|asus|rog|tuf|nzxt|corsair|razer|logitech|logi|steelseries|hyperx|gigabyte|aorus|evga|zotac|sapphire|cooler master|lian li|thermaltake|seasonic|kingston|crucial|seagate|samsung|sony|dell|lenovo|acer|alienware|dji|anker|ugreen|redmi|iqoo|vivo|xiaomi|huawei|honor|oneplus|nokia|motorola|cubot|realme|medion|maingear|skytech|ironside|starforge|cyberpower|ibuypower|nzxt|pichau|terabyteshop|keychron|sennheiser|beyerdynamic|audio-technica|jbl|bose|viewsonic|aoc|benq|lg|cougar|xpg|deepcool|be quiet|fractal|redragon|glorious|ducky|wooting|elgato|shure|rode|webcam|vision pro|apple|airpods|ray-?ban meta|smart ?glasses|fitbit|garmin|fastrack|titan smart|noise|boat|mivi|dizo|rx ?\d{3,4}|\d{4} ?xt|aio|liquid cooler|psu|\d{3,4} ?w\b|power station|power ?bank|charger|charging|argb|\d+ ?mhz|\d+ ?gb|\d+ ?tb|iem|dac|amplifier|rtx|gtx|radeon|rx ?\d{3,4}|geforce|gpu|graphics card|ryzen|intel core|i[579]-\d|cpu|motherboard|ssd|nvme|ram|ddr[45]|gaming pc|pc build|custom pc|built pc|laptop|notebook|macbook|imac|ipad|tablet|iphone|galaxy|pixel \d|oneplus|oppo|realme|xiaomi|poco|smartphone|phone|ps5|playstation|xbox|nintendo switch|steam deck|rog ally|console|monitor|oled|keyboard|mouse|mousepad|headset|headphones|earbuds|buds|speaker|microphone|webcam|chair|desk|router|drone|camera|gopro|smartwatch|watch|tv|projector|cooler|psu|case|fan|controller|gamepad|vr|quest \d|kindle|e-?reader|airpods|printer|3d printer|soundbar|vacuum|blender|air fryer|espresso|coffee machine)\b", re.I)
EXPERIENCE = re.compile(r"\b(trip|vacation|holiday|getaway|escape|flights?|hotel|resort|stay|night stay|weekend break|all-?inclusive|tickets?|concert|festival|vip|meet ?(and|&) ?greet|backstage|experience|tour|cruise|croisi[eè]re|kreuzfahrt|voyage|reise\w*|s[ée]jour|urlaub|viaje|viagem|destination|golf|spa|dinner|masterclass|workshop|retreat|safari|pass(es)? to|ikon pass|epic pass|season pass)\b", re.I)
VEHICLE = re.compile(r"\b(car|truck|lexus|subaru|nissan|hyundai|kia|chevrolet|chevy|dodge|gmc|tundra|tacoma|can-am|polaris|harley|kawasaki|yamaha|suzuki|ducati|mini bike|golf cart|rv|camper|motorcycle|motorbike|scooter|e-?bike|tesla|jeep|ford|toyota|honda|bmw|mercedes|audi|caravan|boat|jet ?ski|atv|utv)\b", re.I)
FIREARM = re.compile(r"\b(rifle|pistol|desert eagle|daniel defense|taurus|beretta|smith & wesson|ruger|springfield armory|cmmg|zenith|blaster|m249|carbine|geissele|century arms|draco|bolt gun|\d+ ?mm cm|\.308|6\.5 (creedmoor|cm)|concealed carry|armory|hevi ?shot|loadout|palmetto|psa|aero precision|trijicon|eotech|vortex|gun|guns|rimfire|rim fire|revolver|mcx|ar build|handgun|shotgun|handgun|firearm|ar-?15|ar-?10|glock|sig sauer|brownells|ammo|ammunition|suppressor|9mm|\.223|5\.56|nato)\b", re.I)
SUBSCRIPTION = re.compile(r"\b(subscriptions?|memberships?|premium|pro plan|license|licence|lifetime|year of|months? of|1-?year|annual|yearly|access pass|season pass|nitro|tier)\b", re.I)
BUNDLE = re.compile(r"\b(bundle|pack|packs|kit|set|box|boxes|package|combo|setup|haul|collection|hamper|basket|crate|mystery)\b", re.I)
MERCH = re.compile(r"\b(signed|autograph\w*|autografad\w*|merch\w*|swag|camiseta|uniforme|sudadera|playera|jersey|forma|trikot|maillot|oficia\w*|dress|crocs|jacket|coat|socks|bag|wallet|watch strap|sunglasses|aj\d|yzy|t-?shirts?|shirts?|hoodies?|jerseys?|caps?|hats?|sneakers?|shoes?|jordan|dunk|yeezy|nike|adidas|apparel|poster|plush|figure|figurine|funko|vinyl|book|copy of)\b", re.I)
PLACEHOLDER = re.compile(r"^\s*(.{0,3}|[\d~\-\s]+|lot \d+|other.*winners?|participation.*|.*referral winner|.*award|most popular.*|back ?up winner.*|gewinn\w* t[äa]glich.*|presenteras.*|retweets.*|object|daily draw.*|\d+(st|nd|rd|th) place( - .*)?|top \d+.*|\d+(st|nd|rd|th) to \d+(st|nd|rd|th)|daily giveaway.*|test( test)*|\d+(st|nd|rd|th)?|(first|second|third|fourth|fifth|sixth|grand|main|runner.?up|daily|weekly|lucky|mystery|secret|bonus|special|top ?\d+|\d+(st|nd|rd|th))\s*(place\s*)?(prizes?|winners?|draw)?|winners?|prizes?|prize ?#?\d+.*|vinst|tickets?|rewards?|giveaway|item|test|lucky draw|\bweek(ly)?\b( ending)?.*|day \d+.*|[\W_]*)\s*$", re.I)
STOP = set("the and for with you your win our from this that will one get are all new have can not out giveaway contest sweepstakes official store shop inc llc ltd co com net org io tv official global world team gaming games game".split())

def text_of(c):
    return " ".join([c.get("name") or "", c.get("incentive_name") or "", c.get("incentive_desc") or ""] +
                    [p.get("name") or "" for p in c.get("prizes") or []])

def prize_text(c):
    return " ".join(p.get("name") or "" for p in c.get("prizes") or [])

SHOE_SIZE = re.compile(r"^\s*(men'?s|women'?s|wmns|gs|kids|youth|uk|us|eu)?\s*\d{1,2}(\.5)?\s*(us|uk|eu)?\s*$", re.I)
SNEAKER = re.compile(r"\b(jordan|aj\d|yeezy|yzy|dunk|nike|adidas|new balance|air max|air force|raffle)\b", re.I)

def classify_campaign(c):
    """Return (segment, reasons). segment in ordinary | crypto | ambiguous | purchase_opportunity."""
    reasons = []
    t = text_of(c); pt = prize_text(c); name = (c.get("name") or "") + " " + (c.get("incentive_name") or "")
    em = {e.get("entry_method_type") for e in c.get("entry_methods") or []}
    strong = 0
    if "wallet_address" in em: strong += 2; reasons.append("wallet_address entry method")
    if any((p.get("currency") or "").upper() in ("USDT", "USDC", "BUSD", "ETH", "BTC", "BNB", "SOL") for p in c.get("prizes") or []): strong += 2; reasons.append("crypto currency code on a prize")
    m = CRYPTO_STRONG.findall(pt + " " + name) + CRYPTO_CAPS.findall(pt + " " + name)
    if m: strong += 2; reasons.append("crypto term in prize/campaign name: " + ",".join(sorted({x[0] if isinstance(x, tuple) else x for x in m}))[:80])
    if TICKER.search(pt + " " + name): strong += 2; reasons.append("$TICKER in prize/campaign name")
    desc = c.get("incentive_desc") or ""
    desc_strong = len(CRYPTO_STRONG.findall(desc)) + len(CRYPTO_CAPS.findall(desc))
    desc_ticker = bool(TICKER.search(desc))
    weak = len(CRYPTO_WEAK.findall(t))
    nt = [x for x in NUM_TICKER.findall(pt) if not UNITS.search(x)]
    if nt and (weak or desc_strong): strong += 1; reasons.append("number+TICKER in prize name with token/coin context: " + nt[0][:30])
    if re.search(r"\btokens?\b", pt, re.I): strong += 1; reasons.append("'token' in prize name")
    m2 = re.search(r"\$[\d,.]+[kK]?\s+(?:in|of|worth of)\s+(?!cash\b|gift\b|store\b|credit\b|prizes?\b|products?\b|gear\b|merch\b|free\b|travel\b|shopping\b|vouchers?\b|value\b|your\b|our\b|the\b|a\b|an\b|any\b)([A-Za-z][\w$]*)", pt)
    if m2 and not re.search(r"gift|card|voucher|credit|cash|shop|store|spree|product|gear|merch|clothing|apparel|fuel|groceries|books?|flights?|travel|jewel", pt, re.I):
        strong += 2; reasons.append("'$N in NAME' prize wording: " + m2.group(1)[:20])
    if re.search(r"\b\d[\d,.]*[kK]?\s+(HEX|ZEC|ETH|BTC|SOL|BNB|USDT|USDC|DOGE|SHIB|PEPE|TON|TRX|XRP|ADA|DOT|AVAX|MATIC|LINK|ATOM|ALGO|APT|SUI|SEI|ARB|OP)\b", pt): strong += 2; reasons.append("amount + known ticker")
    if desc_strong >= 3 or (desc_strong >= 1 and desc_ticker): strong += 1; reasons.append(f"{desc_strong} crypto terms in description")
    pur = PURCHASE.search(t)
    ps = [p.get("name") or "" for p in c.get("prizes") or []]
    if ps and sum(1 for n in ps if SHOE_SIZE.match(n)) >= max(1, len(ps) // 2) and SNEAKER.search(name):
        pur = pur or type("M", (), {"group": lambda self, i=0: "prize names are shoe sizes in a sneaker raffle"})()
        reasons.append("sneaker raffle: prize names are shoe sizes")
    if strong >= 2:
        return "crypto", reasons
    if strong == 1 or (weak >= 2 and desc_strong >= 1):
        reasons.append(f"weak crypto signals only (weak={weak}, desc_strong={desc_strong})")
        return "ambiguous", reasons
    if pur:
        reasons.append("purchase-opportunity phrase: " + pur.group(0)[:60])
        return "purchase_opportunity", reasons
    return "ordinary", reasons

CAMPAIGN_WORDS = re.compile(r"\b(giveaway|giveawe?y|give ?away|sweepstakes?|sorteo|sorteio|concours|gewinnspiel|çekilişi?|konkurs|contest|competition|raffle|worldwide|international|day \d+|round ?\d+|\d{4}|grand prize|prize|winner|edition|official|celebration|anniversary|holiday|christmas|summer|winter|spring|fall|massive|mega|huge|ultimate|lucky|january|february|march|april|may|june|july|august|september|october|november|december)\b", re.I)

def classify_prize(p, c):
    n = (p.get("name") or "").strip()
    if not n or PLACEHOLDER.match(n): return "placeholder_name"
    cat = _classify_name(n)
    if cat == "other_unclassified":
        stripped = CAMPAIGN_WORDS.sub(" ", n)
        stripped = re.sub(r"^[\W_]+|[\W_]+$", "", stripped)
        if len(stripped) < 4 or PLACEHOLDER.match(stripped): return "placeholder_name"
        cat = _classify_name(stripped)
    return cat

def _classify_name(n):
    if SKIN.search(n): return "game_item_or_skin"
    if DISCOUNT.search(n): return "discount_or_coupon"
    if BULLION.search(n): return "bullion_precious_metal"
    if re.search(r"\d+\s?\$(?!\w)", n) and not HARDWARE.search(n): return "gift_card_or_cash"
    if re.search(r"\b(no pix|via pix|boleto pago|saldo (de|na|no)|dinheiro|efectivo|en efectivo|bargeld|contanti)\b", n, re.I): return "gift_card_or_cash"
    if GIFT_CARD.search(n): return "gift_card_or_cash"
    if VEHICLE.search(n) and not HARDWARE.search(n): return "vehicle"
    if DIGITAL_GAME.search(n): return "game_item_or_skin"
    if ACCESS.search(n): return "exclusive_access"
    if EXPERIENCE.search(n): return "experience_travel_tickets"
    if HARDWARE.search(n): return "tech_hardware"
    if FIREARM.search(n): return "regulated_goods_firearm"
    if MUSIC.search(n): return "music_gear"
    if HOME.search(n): return "home_garden_appliance"
    if TOOLS_CRAFT.search(n): return "tools_craft_diy"
    if SPORTS.search(n): return "sports_outdoor_gear"
    if BEAUTY_WELLNESS.search(n): return "beauty_wellness"
    if FOOD_CONSUMABLE.search(n): return "food_drink_consumables"
    if TOYS.search(n): return "toys_collectibles"
    if ART.search(n): return "art_custom"
    if re.search(r"\b(otf|pocket|folding|fixed blade|edc|chef'?s|kitchen|hunting) knife\b|\bknife\b", n, re.I): return "sports_outdoor_gear"
    if SUBSCRIPTION.search(n): return "subscription_membership"
    if BUNDLE.search(n): return "bundle_or_box"
    if MERCH.search(n): return "merch_apparel_collectible"
    if re.search(r"\b(to spend|towards|credit|balance|shopping spree|worth of)\b", n, re.I): return "gift_card_or_cash"
    if MONEY.fullmatch(n.strip()) or re.fullmatch(r"[\W\d.,kK]*(?:usd|dollars?|cash)?[\W]*", n, re.I) and MONEY.search(n): return "gift_card_or_cash"
    return "other_unclassified"

CUR = {"R$": "BRL", "$": "USD?", "£": "GBP", "€": "EUR", "₹": "INR", "Rs": "INR", "Rs.": "INR", "dollar": "USD?", "dollars": "USD?", "euro": "EUR", "euros": "EUR", "pound": "GBP", "pounds": "GBP"}
def _amt(m):
    raw = m.group("amt") or m.group("amt2"); cur = m.group("cur") or m.group("cur2")
    if re.fullmatch(r"\d{1,3}(?:\.\d{3})+,\d\d", raw): raw = raw.replace(".", "").replace(",", ".")   # 5.000,00
    raw = raw.replace(",", "")
    if raw.count(".") == 1 and len(raw.split(".")[1]) == 3: raw = raw.replace(".", "")   # 100.000 European thousands
    try: v = float(raw)
    except ValueError: return None
    if m.group("k"): v *= 1000
    return v, CUR.get(cur, cur.upper())

def parse_value(p, c):
    """Best-effort value from text. Returns (value, currency, source) or None.
    Sources: prize_name (largest amount in the prize name), description_phrase (amount right after 'worth'/'valued at'/'MSRP'...),
    campaign_name (single-prize campaigns only). '$' is recorded as USD? because the symbol is ambiguous."""
    n = p.get("name") or ""
    found = [_amt(m) for m in MONEY.finditer(n)]
    found = [f for f in found if f]
    if found: v, cur = max(found); return v, cur, "prize_name"
    desc = c.get("incentive_desc") or ""
    if len(c.get("prizes") or []) == 1:
        for vm in VALUE_PHRASE.finditer(desc):
            mm = MONEY.match(desc, vm.end())
            if mm and _amt(mm): v, cur = _amt(mm); return v, cur, "description_phrase"
        cn = (c.get("name") or "") + " " + (c.get("incentive_name") or "")
        found = [f for f in (_amt(m) for m in MONEY.finditer(cn)) if f]
        if found: v, cur = max(found); return v, cur, "campaign_name"
    return None

def own_product_signal(p, c):
    site = set(w for w in re.findall(r"[a-z0-9]{3,}", (c.get("site_name") or "").lower()) if w not in STOP)
    prize = set(w for w in re.findall(r"[a-z0-9]{3,}", (p.get("name") or "").lower()) if w not in STOP)
    return bool(site & prize)

# ---------- stats helpers ----------
def q(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(p * len(xs)))] if xs else None

def dist(xs):
    xs = [x for x in xs if x is not None]
    if not xs: return {"n": 0}
    return {"n": len(xs), "min": min(xs), "p25": q(xs, .25), "median": st.median(xs), "p75": q(xs, .75), "p90": q(xs, .9), "max": max(xs)}

def cur(p):
    c = (p.get("currency") or "null").upper().strip()
    return {"EURO": "EUR", "": "null"}.get(c, c)

def value_stated(p):
    v = p.get("value")
    return v is not None and v != 0 and v != ""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("export")
    ap.add_argument("--private-dir", default=None, help="write record-level provenance here (keep out of git)")
    ap.add_argument("--out-dir", default=os.path.join(os.path.dirname(__file__), "output"))
    ap.add_argument("--labels", nargs="*", default=[], help="private JSON label files [{prize, category, note, confidence}] applied only where rules return other_unclassified")
    a = ap.parse_args()
    labels = {}
    for lf in a.labels:
        for item in json.load(open(lf)):
            if item.get("confidence", "high") in ("high", "medium") and item.get("category") not in (None, "other"):
                labels[item["prize"]] = item["category"]
    data = json.load(open(a.export))
    assert isinstance(data, list) and data and "prizes" in data[0], "unexpected export shape"
    nulls = collections.Counter()
    for c in data:
        for k in ("valid_contestants", "valid_entries", "impressions", "duration_in_days"):
            if c.get(k) is None: nulls[k] += 1
        c.setdefault("prizes", None); c["prizes"] = c["prizes"] or []
        c["entry_methods"] = c.get("entry_methods") or []
    data = [c for c in data if c.get("valid_contestants")]   # a null contestant count cannot be benchmarked
    null_fields = dict(nulls)

    rows = []
    for c in data:
        seg, reasons = classify_campaign(c)
        prizes = c.get("prizes") or []
        cats = [classify_prize(p, c) for p in prizes]
        src = ["rule"] * len(cats)
        for i, (p, cat) in enumerate(zip(prizes, cats)):
            lab = labels.get(p.get("name"))
            if cat == "other_unclassified" and lab:
                if lab in ("crypto", "purchase_opportunity"):
                    if seg == "ordinary": seg = "ambiguous"; reasons.append(f"labeler flagged a prize as {lab}")
                    continue
                cats[i] = lab; src[i] = "label"
        rows.append({"c": c, "segment": seg, "reasons": reasons, "cats": cats, "src": src,
                     "own": [own_product_signal(p, c) for p in prizes]})

    seg_counts = collections.Counter(r["segment"] for r in rows)
    all_prizes = [p for c in data for p in c.get("prizes") or []]
    out = {
        "source": {"campaigns": len(data), "prize_records": len(all_prizes),
                   "selection": f"campaigns with >= {min(c['valid_contestants'] for c in data):,} valid contestants only; no comparison group of smaller or failed campaigns",
                   "min_valid_contestants": min(c["valid_contestants"] for c in data),
                   "campaign_start_years": dict(sorted(collections.Counter((c.get("starts_at") or "????")[:4] for c in data).items())),
                   "unique_organizers_sites": len({c["site_id"] for c in data}),
                   "prize_value_missing_null": sum(1 for p in all_prizes if p.get("value") is None),
                   "prize_value_zero": sum(1 for p in all_prizes if p.get("value") == 0),
                   "prize_value_missing_share": round(sum(1 for p in all_prizes if not value_stated(p)) / len(all_prizes), 4),
                   "prize_currency_counts": dict(collections.Counter(cur(p) for p in all_prizes).most_common()),
                   "campaigns_missing_description": sum(1 for c in data if not c.get("incentive_desc")),
                   "campaigns_with_zero_impressions": sum(1 for c in data if not c.get("impressions")),
                   "null_numeric_fields_in_raw_export": null_fields},
        "segments": dict(seg_counts),
        "benchmark_scope": "segment == ordinary (crypto, ambiguous and purchase_opportunity excluded)",
    }

    ord_rows = [r for r in rows if r["segment"] == "ordinary"]
    oc = [r["c"] for r in ord_rows]
    op = [(p, cat, own, r["c"]) for r in ord_rows for p, cat, own in zip(r["c"]["prizes"], r["cats"], r["own"])]

    sites = collections.Counter(c["site_id"] for c in oc)
    repeat = {s for s, n in sites.items() if n >= 5}
    b = {
        "campaigns": len(oc), "prize_records": len(op), "unique_organizers": len(sites),
        "organizers_with_5_plus_campaigns": len(repeat),
        "share_of_campaigns_from_repeat_organizers": round(sum(1 for c in oc if c["site_id"] in repeat) / len(oc), 3),
        "start_years": dict(sorted(collections.Counter((c.get("starts_at") or "????")[:4] for c in oc).items())),
        "tier": dict(collections.Counter(c.get("tier") for c in oc)),
        "valid_contestants": dist([c["valid_contestants"] for c in oc]),
        "valid_entries": dist([c["valid_entries"] for c in oc if c.get("valid_entries") is not None]),
        "entries_per_contestant": dist([round(c["valid_entries"] / c["valid_contestants"], 2) for c in oc if c.get("valid_entries") is not None]),
        "impressions_where_nonzero": dist([c["impressions"] for c in oc if c.get("impressions")]),
        "duration_days": dist([c["duration_in_days"] for c in oc if c.get("duration_in_days") is not None]),
        "prizes_per_campaign": dict(sorted(collections.Counter(min(len(c["prizes"]), 10) for c in oc).items())),
        "single_prize_record_share": round(sum(1 for c in oc if len(c["prizes"]) == 1) / len(oc), 3),
        "any_prize_quantity_gt1_share": round(sum(1 for c in oc if any((p.get("quantity") or 1) > 1 for p in c["prizes"])) / len(oc), 3),
        "prize_value_stated_share": round(sum(1 for p, *_ in op if value_stated(p)) / len(op), 3),
        "own_product_signal_prize_share": round(sum(1 for _, _, own, _ in op if own) / len(op), 3),
    }
    # stated values by currency, never merged
    byc = collections.defaultdict(list)
    for p, *_ in op:
        if value_stated(p): byc[cur(p)].append(p["value"])
    b["stated_prize_value_by_currency"] = {k: dist(v) for k, v in byc.items()}
    # inferred values: parsed from text, validated where a stated value also exists
    parsed = [(p, c, parse_value(p, c)) for p, _, _, c in op]
    both = [(p["value"], pv[0], pv[1]) for p, c, pv in parsed if pv and value_stated(p) and cur(p) == "USD" and pv[1] == "USD?"]
    agree = sum(1 for sv, pv, _ in both if 0.8 <= pv / sv <= 1.25) if both else 0
    src = collections.Counter(pv[2] for _, _, pv in parsed if pv)
    newly = [pv for p, c, pv in parsed if pv and not value_stated(p)]
    b["inferred_value_from_text"] = {
        "method": "regex on prize name, then 'worth/valued at/MSRP' phrases in description and the campaign name (single-prize campaigns only); '$' recorded as USD? (ambiguous symbol)",
        "prize_records_with_parsed_value": sum(1 for _, _, pv in parsed if pv), "by_source": dict(src),
        "records_missing_stated_but_parsed": len(newly),
        "coverage_stated_only": round(sum(1 for p, *_ in op if value_stated(p)) / len(op), 3),
        "coverage_stated_or_parsed": round(sum(1 for p, c, pv in parsed if value_stated(p) or pv) / len(op), 3),
        "validation_overlap_n": len(both), "validation_within_20pct_share": round(agree / len(both), 3) if both else None,
        "parsed_only_values_by_currency": {k: dist([v for v, cur, _ in newly if cur == k]) for k in sorted({cur for _, cur, _ in newly})},
        "caveat": "Parsed values are what organizers wrote in text, often rounded marketing numbers or totals across several prizes; not organizer cost. Never a substitute for a stated value in a record-level claim.",
    }
    # campaign-level total stated value (USD-only campaigns)
    tot = []
    for c in oc:
        ps = c["prizes"]
        if ps and all(value_stated(p) and cur(p) == "USD" for p in ps):
            tot.append(sum(p["value"] * (p.get("quantity") or 1) for p in ps))
    b["campaign_total_stated_value_usd_fully_valued_campaigns"] = dist(tot)
    # categories
    cat_stats = {}
    for cat in sorted({cat for _, cat, _, _ in op}):
        ps = [(p, c) for p, k, _, c in op if k == cat]
        cs = {c["campaign_id"]: c for _, c in ps}.values()
        usd = [p["value"] for p, _ in ps if value_stated(p) and cur(p) == "USD"]
        cat_stats[cat] = {
            "prize_records": len(ps), "campaigns": len(cs), "unique_organizers": len({c["site_id"] for c in cs}),
            "share_of_prize_records": round(len(ps) / len(op), 3),
            "value_stated_share": round(sum(1 for p, _ in ps if value_stated(p)) / len(ps), 3),
            "stated_value_usd": dist(usd),
            "campaign_valid_contestants": dist([c["valid_contestants"] for c in cs]),
            "quantity": dist([p.get("quantity") or 1 for p, _ in ps]),
        }
    b["by_prize_category"] = cat_stats
    b["category_source"] = dict(collections.Counter(sr for r in ord_rows for sr in r["src"]))
    b["category_source"]["note"] = "rule = regex on the prize name; label = private LLM-assisted label applied only where rules failed, high or medium confidence labels only, never committed"
    # primary prize category per campaign (position 0 / first)
    prim = collections.Counter(r["cats"][0] for r in ord_rows if r["cats"])
    b["primary_prize_category_by_campaign"] = dict(prim.most_common())
    # single big prize vs many
    single = [c for c in oc if len(c["prizes"]) == 1 and (c["prizes"][0].get("quantity") or 1) == 1]
    multi = [c for c in oc if sum((p.get("quantity") or 1) for p in c["prizes"]) >= 5]
    b["structure"] = {
        "single_winner_single_prize": {"campaigns": len(single), "valid_contestants": dist([c["valid_contestants"] for c in single])},
        "five_plus_prize_units": {"campaigns": len(multi), "valid_contestants": dist([c["valid_contestants"] for c in multi])},
        "note": "Every campaign passed the export floor, so these medians describe structure and say nothing about effect.",
    }
    # contestant bands: descriptive only, every band is still a selected (>= floor) sample
    def band(v): return "10k+" if v >= 10000 else "2.5k-10k" if v >= 2500 else "1k-2.5k" if v >= 1000 else "<1k"
    bands = {}
    for name in ("1k-2.5k", "2.5k-10k", "10k+"):
        rs = [r for r in ord_rows if band(r["c"]["valid_contestants"]) == name]
        if not rs: continue
        cs = [r["c"] for r in rs]; ps = [(p, k) for r in rs for p, k in zip(r["c"]["prizes"], r["cats"])]
        prim = collections.Counter(r["cats"][0] for r in rs if r["cats"])
        usd = [p["value"] for p, _ in ps if value_stated(p) and cur(p) == "USD"]
        tot = [sum(p["value"] * (p.get("quantity") or 1) for p in c["prizes"]) for c in cs if c["prizes"] and all(value_stated(p) and cur(p) == "USD" for p in c["prizes"])]
        bands[name] = {"campaigns": len(cs), "unique_organizers": len({c["site_id"] for c in cs}),
                       "valid_contestants": dist([c["valid_contestants"] for c in cs]),
                       "entries_per_contestant_median": st.median([round(c["valid_entries"] / c["valid_contestants"], 2) for c in cs if c.get("valid_entries") is not None]),
                       "duration_days_median": st.median([c["duration_in_days"] for c in cs if c.get("duration_in_days") is not None]),
                       "single_prize_record_share": round(sum(1 for c in cs if len(c["prizes"]) == 1) / len(cs), 3),
                       "any_prize_quantity_gt1_share": round(sum(1 for c in cs if any((p.get("quantity") or 1) > 1 for p in c["prizes"])) / len(cs), 3),
                       "prize_value_stated_share": round(sum(1 for p, _ in ps if value_stated(p)) / len(ps), 3),
                       "stated_value_usd": dist(usd), "campaign_total_stated_value_usd": dist(tot),
                       "primary_prize_category_share": {k: round(v / len(rs), 3) for k, v in prim.most_common()},
                       "tier": dict(collections.Counter(c.get("tier") for c in cs).most_common())}
    b["by_contestant_band"] = bands

    # ---- entry methods: generic families, platform-neutral names ----
    FAM = {
        "Visit a page or profile": {"instagram_visit_profile", "facebook_visit", "youtube_visit_channel", "tiktok_visit", "pinterest_visit", "reddit_visit", "patreon_visit", "kickstarter_visit", "indiegogo_visit", "custom_action:visit"},
        "Follow or subscribe (free)": {"twitter_follow", "instagram_follow", "tiktok_follow", "twitchtv_follow", "facebook_like", "linkedin_follow", "spotify_follow", "bluesky_follow", "threads_follow", "kick_follow", "soundcloud_follow", "tumblr_follow", "goodreads_follow", "bandcamp_follow", "podcast_subscribe", "youtube_video", "shop_follow"},
        "Email or newsletter signup": {"email_subscribe", "gleam_subscribe", "substack_subscribe", "messenger_subscribe", "blog_rss"},
        "Join a community": {"discord_join_server", "telegram_join", "steam_join_group", "facebook_join_group"},
        "Share, repost or refer": {"share_action", "promote_campaign", "twitter_retweet", "bluesky_repost", "soundcloud_repost", "linkedin_share"},
        "Post or create content": {"twitter_tweet", "twitter_hashtags", "twitter_media", "instagram_choose", "upload_action", "submit_url", "blog_post", "media_action", "facebook_media", "instagram_mentions_import", "tumblr_hashtag_import", "youtube_hashtag_import"},
        "Engage with a post": {"instagram_view_post", "facebook_view_post", "twitter_view_post", "telegram_view_post", "instagram_comment", "blog_comment", "bluesky_like", "spotify_listen", "spotify_save", "spotify_presave", "vimeo_watch", "wistia_watch", "watch_video", "facebook_check_in", "producthunt_upvote", "twitchtv_channel_reward", "discord_role"},
        "Answer a question or poll": {"custom_action:question", "custom_action:multiple_choice", "custom_action:choose_option", "custom_action:choose_image", "typeform_completed"},
        "Bonus, loyalty or code": {"custom_action:bonus", "loyalty", "timed_bonus", "secret_code", "calendar_add", "coupon_action"},
        "Connect an account to enter": {"facebook_enter", "instagram_enter", "twitter_enter", "pinterest_enter", "reddit_enter", "steam_enter", "twitchtv_enter", "youtube_enter", "telegram_enter", "discord_enter", "snapchat_snapcode"},
        "Download or play": {"download_app", "steam_play_game"},
        "Paid subscription": {"twitchtv_subscribe"},
        "Imported or offline entries": {"csv_import", "api_import", "facebook_import", "instagram_import", "facebook_comments_import", "instagram_comments_import", "youtube_comments_import"},
        "Crypto wallet": {"wallet_address"},
    }
    def fam_of(e):
        t = e.get("entry_method_type") or "unknown"
        key = f"custom_action:{e.get('entry_method_template') or ''}" if t == "custom_action" else t
        for f, ts in FAM.items():
            if key in ts: return f
        return "Custom action (other)" if t == "custom_action" else "Other"
    fam_c = collections.defaultdict(set); fam_up = collections.defaultdict(list); type_c = collections.Counter(); type_up = collections.defaultdict(list)
    for c in oc:
        for e in c.get("entry_methods") or []:
            f = fam_of(e); fam_c[f].add(c["campaign_id"]); type_c[e.get("entry_method_type")] += 1
            if e.get("entry_count") is not None:
                u = min(e["entry_count"] / c["valid_contestants"], 5.0); fam_up[f].append(u); type_up[e.get("entry_method_type")].append(u)
    b["entry_methods"] = {
        "definition": "uptake = entries recorded on the method divided by the campaign's valid contestants, capped at 5 (repeatable methods can exceed 1). Family names are generic, and platform types were mapped to them by hand.",
        "families": {f: {"campaigns": len(ids), "share_of_campaigns": round(len(ids) / len(oc), 3), "uptake": dist(fam_up[f])} for f, ids in sorted(fam_c.items(), key=lambda kv: -len(kv[1]))},
        "methods_per_campaign": dist([len(c.get("entry_methods") or []) for c in oc]),
        "by_band": {name: {"methods_per_campaign_median": st.median([len(c.get("entry_methods") or []) for c in cs]),
                          "share_with_family": {f: round(sum(1 for c in cs if any(fam_of(e) == f for e in c.get("entry_methods") or [])) / len(cs), 3) for f in FAM if f not in ("Crypto wallet",)}}
                    for name, cs in ((n, [r["c"] for r in ord_rows if band(r["c"]["valid_contestants"]) == n]) for n in ("1k-2.5k", "2.5k-10k", "10k+")) if cs},
    }

    # ---- timing ----
    import datetime as _dt
    mon = collections.Counter(); wd = collections.Counter(); dur = collections.Counter(); epc = collections.defaultdict(list)
    def dbucket(d): return "1-3" if d <= 3 else "4-7" if d <= 7 else "8-14" if d <= 14 else "15-30" if d <= 30 else "31-60" if d <= 60 else "61-180" if d <= 180 else "181+"
    for c in oc:
        try:
            t = _dt.datetime.fromisoformat(c["starts_at"].replace("Z", "+00:00")); mon[t.month] += 1; wd[t.strftime("%A")] += 1
        except Exception: pass
        dd = c.get("duration_in_days")
        if dd is not None:
            dur[dbucket(dd)] += 1
            if c.get("valid_entries"): epc[dbucket(dd)].append(c["valid_entries"] / c["valid_contestants"])
    b["timing"] = {
        "duration_days": b["duration_days"],
        "duration_bucket_share": {k: round(v / len(oc), 3) for k, v in sorted(dur.items(), key=lambda kv: ["1-3", "4-7", "8-14", "15-30", "31-60", "61-180", "181+"].index(kv[0]))},
        "start_month_share": {str(m): round(mon[m] / sum(mon.values()), 3) for m in range(1, 13)},
        "start_weekday_share": {d: round(wd[d] / sum(wd.values()), 3) for d in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")},
        "entries_per_contestant_median_by_duration": {k: round(st.median(v), 2) for k, v in epc.items() if v},
        "duration_median_by_band": {k: v["duration_days_median"] for k, v in bands.items()},
        "note": "Descriptive. Duration and start date are organizer choices that co-vary with organizer type and season. Nothing here shows a duration or start day changed participation.",
    }

    # ---- winner structure ----
    units = [sum((p.get("quantity") or 1) for p in c["prizes"]) for c in oc]
    recs = collections.Counter(min(len(c["prizes"]), 6) for c in oc)
    b["structure_detail"] = {
        "prize_records_per_campaign_share": {("6+" if k == 6 else str(k)): round(v / len(oc), 3) for k, v in sorted(recs.items())},
        "total_prize_units": dist(units),
        "share_more_than_one_unit": round(sum(1 for u in units if u > 1) / len(oc), 3),
        "share_tiered_positions": round(sum(1 for c in oc if len(c["prizes"]) > 1 and len({p.get("position") for p in c["prizes"]}) > 1) / len(oc), 3),
        "by_band": {name: {"share_single_unit": round(sum(1 for c in cs if sum((p.get("quantity") or 1) for p in c["prizes"]) == 1) / len(cs), 3),
                          "share_tiered": round(sum(1 for c in cs if len(c["prizes"]) > 1 and len({p.get("position") for p in c["prizes"]}) > 1) / len(cs), 3),
                          "share_ten_plus_units": round(sum(1 for c in cs if sum((p.get("quantity") or 1) for p in c["prizes"]) >= 10) / len(cs), 3)}
                    for name, cs in ((n, [r["c"] for r in ord_rows if band(r["c"]["valid_contestants"]) == n]) for n in ("1k-2.5k", "2.5k-10k", "10k+")) if cs},
        "note": "Quantity is units listed, which may differ from winners. Structure is an organizer choice and says nothing about effect.",
    }
    out["ordinary_benchmark"] = b

    # excluded segments, described only (never blended)
    for seg in ("crypto", "ambiguous", "purchase_opportunity"):
        cs = [r["c"] for r in rows if r["segment"] == seg]
        out[f"excluded_{seg}"] = {"campaigns": len(cs), "unique_organizers": len({c["site_id"] for c in cs}),
                                  "valid_contestants": dist([c["valid_contestants"] for c in cs]),
                                  "start_years": dict(sorted(collections.Counter((c.get("starts_at") or "????")[:4] for c in cs).items())),
                                  "wallet_address_entry_method_share": round(sum(1 for c in cs if any(e.get("entry_method_type") == "wallet_address" for e in c["entry_methods"])) / len(cs), 3) if cs else None}

    os.makedirs(a.out_dir, exist_ok=True)
    json.dump(out, open(os.path.join(a.out_dir, "benchmarks.json"), "w"), indent=1, default=str)
    write_md(out, os.path.join(a.out_dir, "benchmarks.md"))

    if a.private_dir:
        os.makedirs(a.private_dir, exist_ok=True)
        with open(os.path.join(a.private_dir, "classification.jsonl"), "w") as f:
            for r in rows:
                c = r["c"]
                f.write(json.dumps({"campaign_id": c["campaign_id"], "site_id": c["site_id"], "segment": r["segment"], "reasons": r["reasons"],
                                    "prize_cats": r["cats"], "cat_source": r["src"], "own_signal": r["own"], "valid_contestants": c["valid_contestants"],
                                    "prizes": c["prizes"], "name": c["name"], "year": (c.get("starts_at") or "")[:4]}) + "\n")
        # example candidates: ordinary, with a stated value or descriptive name, spread across categories
        with open(os.path.join(a.private_dir, "example_candidates.md"), "w") as f:
            for cat in cat_stats:
                f.write(f"\n## {cat}\n")
                seen = set(); n = 0
                for p, k, own, c in op:
                    if k != cat or c["site_id"] in seen or len(p.get("name") or "") < 12: continue
                    seen.add(c["site_id"]); n += 1
                    f.write(f"- cid={c['campaign_id']} site={c['site_id']} yr={(c.get('starts_at') or '')[:4]} own={own} contestants={c['valid_contestants']} "
                            f"nprizes={len(c['prizes'])} qty={p.get('quantity')} value={p.get('value')} {p.get('currency')} parsed={parse_value(p, c)} :: {p['name'][:120]!r} :: desc={(c.get('incentive_desc') or '')[:200]!r}\n")
                    if n >= 25: break
    print(json.dumps({"segments": out["segments"], "ordinary_campaigns": b["campaigns"], "ordinary_prizes": b["prize_records"]}))

def write_md(o, path):
    s, b = o["source"], o["ordinary_benchmark"]
    L = ["# Dataset benchmarks (generated by analysis/analyze_export.py)", "",
         f"Aggregates only. Source is a private export: {s['selection']}. Nothing here measures the effect of a prize on participation.", "",
         f"- Source campaigns: {s['campaigns']}; prize records: {s['prize_records']}; organizers: {s['unique_organizers_sites']}",
         f"- Prize value missing (null or zero): {s['prize_value_missing_share']:.1%} of prize records ({s['prize_value_missing_null']} null, {s['prize_value_zero']} zero)",
         f"- Prize currencies: {s['prize_currency_counts']}",
         f"- Campaign start years: {s['campaign_start_years']}", "",
         f"## Segments", "", f"- {o['segments']}",
         f"- Benchmark scope: {o['benchmark_scope']}", "",
         "## Ordinary benchmark", ""]
    for k in ("campaigns", "prize_records", "unique_organizers", "organizers_with_5_plus_campaigns", "share_of_campaigns_from_repeat_organizers",
              "start_years", "tier", "valid_contestants", "valid_entries", "entries_per_contestant", "impressions_where_nonzero", "duration_days",
              "prizes_per_campaign", "single_prize_record_share", "any_prize_quantity_gt1_share", "prize_value_stated_share",
              "own_product_signal_prize_share", "stated_prize_value_by_currency", "inferred_value_from_text",
              "campaign_total_stated_value_usd_fully_valued_campaigns", "primary_prize_category_by_campaign", "category_source", "structure", "by_contestant_band", "entry_methods", "timing", "structure_detail"):
        L.append(f"- {k}: {json.dumps(b[k], default=str)}")
    L += ["", "## By prize category (ordinary segment)", "",
          "| category | prize records | campaigns | organizers | value stated | USD value median (n) | campaign contestants median |", "|---|---|---|---|---|---|---|"]
    for k, v in sorted(b["by_prize_category"].items(), key=lambda kv: -kv[1]["prize_records"]):
        sv = v["stated_value_usd"]
        L.append(f"| {k} | {v['prize_records']} | {v['campaigns']} | {v['unique_organizers']} | {v['value_stated_share']:.0%} | "
                 f"{sv.get('median')} ({sv['n']}) | {v['campaign_valid_contestants'].get('median')} |")
    L += ["", "## Excluded segments (described, never blended)", ""]
    for seg in ("crypto", "ambiguous", "purchase_opportunity"):
        L.append(f"- {seg}: {json.dumps(o['excluded_' + seg], default=str)}")
    open(path, "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
