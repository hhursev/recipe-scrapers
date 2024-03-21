# mypy: disallow_untyped_defs=False

import html
import math
import re

import isodate

from ._exceptions import ElementNotFoundInHtml

FRACTIONS = {
    "½": 0.5,
    "⅓": 1 / 3,
    "⅔": 2 / 3,
    "¼": 0.25,
    "¾": 0.75,
    "⅕": 0.2,
    "⅖": 0.4,
    "⅗": 0.6,
    "⅘": 0.8,
    "⅙": 1 / 6,
    "⅚": 5 / 6,
    "⅛": 0.125,
    "⅜": 0.375,
    "⅝": 0.625,
    "⅞": 0.875,
}

TIME_REGEX = re.compile(
    r"(\D*(?P<days>\d+)\s*(days|D))?(\D*(?P<hours>[\d.\s/?¼½¾⅓⅔⅕⅖⅗]+)\s*(hours|hrs|hr|h|óra|:))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|perc|$))?",
    re.IGNORECASE,
)

SERVE_REGEX_NUMBER = re.compile(r"(\D*(?P<items>\d+)?\D*)")

SERVE_REGEX_ITEMS = re.compile(
    r"\bsandwiches\b |\btacquitos\b | \bmakes\b | \bcups\b | \bappetizer\b | \bporzioni\b | \bcookies\b | \b(large |small )?buns\b",
    flags=re.I | re.X,
)

SERVE_REGEX_TO = re.compile(r"\d+(\s+to\s+|-)\d+", flags=re.I | re.X)

RECIPE_YIELD_TYPES = (
    ("dozen", "dozen"),
    ("batch", "batches"),
    ("cake", "cakes"),
    ("sandwich", "sandwiches"),
    ("bun", "buns"),
    ("cookie", "cookies"),
    ("muffin", "muffins"),
    ("cupcake", "cupcakes"),
    ("loaf", "loaves"),
    ("pie", "pies"),
    ("cup", "cups"),
    ("pint", "pints"),
    ("gallon", "gallons"),
    ("ounce", "ounces"),
    ("pound", "pounds"),
    ("gram", "grams"),
    ("liter", "liters"),
    ("piece", "pieces"),
    ("layer", "layers"),
    ("scoop", "scoops"),
    ("bar", "bars"),
    ("patty", "patties"),
    ("hamburger bun", "hamburger buns"),
    ("pancake", "pancakes"),
    ("item", "items"),
    # ... add more types as needed, in (singular, plural) format ...
)


def _extract_fractional(input_string: str) -> float:
    input_string = input_string.strip()

    # Handling mixed numbers with unicode fractions e.g., '1⅔'
    for unicode_fraction, fraction_part in FRACTIONS.items():
        if unicode_fraction in input_string:
            whole_number_part, _, _ = input_string.partition(unicode_fraction)

            whole_number = float(whole_number_part or 0)
            return whole_number + fraction_part

    if input_string in FRACTIONS:
        return FRACTIONS[input_string]

    try:
        return float(input_string)
    except ValueError:
        pass

    if " " in input_string and "/" in input_string:
        whole_part, fractional_part = input_string.split(" ", 1)
        numerator, denominator = fractional_part.split("/")
        return float(whole_part) + float(numerator) / float(denominator)

    elif "/" in input_string:
        numerator, denominator = input_string.split("/")
        return float(numerator) / float(denominator)

    raise ValueError(f"Unrecognized fraction format: '{input_string}'")

def get_minutes(element):
    if element is None:
        raise ElementNotFoundInHtml(element)

    # handle integer in string literal
    try:
        return int(element)
    except Exception:
        pass

    if isinstance(element, str):
        time_text = element
    else:
        time_text = element.get_text()

    # attempt iso8601 duration parsing
    if time_text.startswith("P") and "T" in time_text:
        try:
            duration = isodate.parse_duration(time_text)
            return math.ceil(duration.total_seconds() / 60)
        except Exception:
            pass

    if "-" in time_text:  # sometimes formats are like this: '12-15 minutes'
        _min, _, time_text = time_text.partition("-")
    if " to " in time_text:  # sometimes formats are like this: '12 to 15 minutes'
        _min, _to, time_text = time_text.partition(" to ")

    time_units = TIME_REGEX.search(time_text).groupdict()
    if not any(time_units.values()):
        return None

    minutes_matched = time_units.get("minutes")
    hours_matched = time_units.get("hours")
    days_matched = time_units.get("days")

    # workaround for formats like: 0D4H45M, that are not a valid iso8601 it seems
    days = float(days_matched) if days_matched else 0
    hours = float(_extract_fractional(hours_matched)) if hours_matched else 0
    minutes = float(minutes_matched) if minutes_matched else 0
    return minutes + round(hours * 60) + round(days * 24 * 60)


def get_yields(element):
    """
    Returns a string indicating the number of servings or items for a recipe. It handles various formats,
    including servings, items, and special cases like dozens and fractions (e.g., "1 ½ dozen cookies").
    If the recipe specifies yields in terms of items (not servings), it returns a string in the format 
    "x item(s)" where x is the quantity. This function also handles yields specified in dozens, returning 
    them appropriately (e.g., "1.5 dozen cookies" instead of "18 items"), and incorporates fractional 
    quantities with proper conversion. Additionally, it accommodates yields specified in other units 
    like batches (e.g., "2 batches of brownies"), returning the yield as specified.

    :param element: Should ideally be BeautifulSoup.TAG. In some cases, where this is not feasible,
                    it will then be plain text.
    :return: The number of servings, items, dozens, batches, etc., formatted as a string.
    """
    if element is None:
        raise ElementNotFoundInHtml(element)
    if isinstance(element, str):
        serve_text = element
    else:
        serve_text = element.get_text()

    if SERVE_REGEX_TO.search(serve_text):
        serve_text = serve_text.split(SERVE_REGEX_TO.split(serve_text, 2)[1], 2)[1]

    fraction_present = any(frac in serve_text for frac in FRACTIONS)
    dozen_present = 'dozen' in serve_text.lower()

    if fraction_present or dozen_present:
        matched = _extract_fractional(" ".join(serve_text.split()[:2]))
    else:
        matched = SERVE_REGEX_NUMBER.search(serve_text).groupdict().get("items") or 0

    matched_str = str(matched).rstrip('0').rstrip('.') if '.' in str(matched) else str(matched)
    serve_text_lower = serve_text.lower()

    best_match = None
    for singular, plural in RECIPE_YIELD_TYPES:
        in_text = singular in serve_text_lower or plural in serve_text_lower
        is_dozen = dozen_present and (singular == 'dozen' or plural == 'dozens')
        if in_text or is_dozen:
            if is_dozen:
                post_dozen = serve_text_lower.split('dozen', 1)[-1].strip()
                for s, p in RECIPE_YIELD_TYPES:
                    if post_dozen.startswith(s) or post_dozen.startswith(p):
                        best_match = f"{matched_str} dozen {p}"
                        break
                if not best_match:
                    best_match = f"{matched_str} dozen"
            else:
                best_match = f"{matched_str} {plural if float(matched) != 1 else singular}"
            break

    if best_match:
        return best_match.strip() 

    if SERVE_REGEX_ITEMS.search(serve_text) is not None:
        return f"{matched_str} item{'s' if float(matched) != 1 else ''}".strip()

    return f"{matched_str} serving{'s' if float(matched) != 1 else ''}".strip()

def get_equipment(equipment_items):
    # Removes duplicates from results and sorts them in order they appear on site.
    seen = set()
    unique_equipment = []
    for item in equipment_items:
        if item not in seen:
            seen.add(item)
            unique_equipment.append(item)
    return unique_equipment


def normalize_string(string):
    # Convert all named and numeric character references (e.g. &gt;, &#62;)
    unescaped_string = html.unescape(string)
    return re.sub(
        r"\s+",
        " ",
        unescaped_string.replace("\xc2\xa0", " ")
        .replace("\xa0", " ")
        .replace("\u200b", "")
        .replace("\n", " ")  # &nbsp;
        .replace("\t", " ")
        .strip(),
    )


def url_path_to_dict(path):
    pattern = (
        r"^"
        r"((?P<schema>.+?)://)?"
        r"((?P<user>.+?)(:(?P<password>.*?))?@)?"
        r"(?P<host>.*?)"
        r"(:(?P<port>\d+?))?"
        r"(?P<path>/.*?)?"
        r"(?P<query>[?].*?)?"
        r"$"
    )
    regex = re.compile(pattern)
    matches = regex.match(path)
    url_dict = matches.groupdict() if matches is not None else None

    return url_dict


def get_host_name(url):
    return url_path_to_dict(url.replace("://www.", "://"))["host"]


def change_keys(obj, convert):
    """
    Recursively goes through the dictionary obj and replaces keys with the convert function

    Useful for fixing incorrect property keys, e.g. in JSON-LD dictionaries

    Credit: StackOverflow user 'baldr'
    (https://web.archive.org/web/20201022163147/https://stackoverflow.com/questions/11700705/python-recursively-replace
        -character-in-keys-of-nested-dictionary/33668421)
    """
    if isinstance(obj, (str, int, float)):
        return obj
    if isinstance(obj, dict):
        new = obj.__class__()
        for k, v in obj.items():
            new[convert(k)] = change_keys(v, convert)
    elif isinstance(obj, (list, set, tuple)):
        new = obj.__class__(change_keys(v, convert) for v in obj)
    else:
        return obj
    return new
