# mypy: disallow_untyped_defs=False
from __future__ import annotations

import html
import math
import re

import isodate

from ._exceptions import ElementNotFoundInHtml

FRACTIONS = {
    "¼": 0.25,
    "½": 0.50,
    "¾": 0.75,
    "⅓": 0.33,
    "⅔": 0.66,
    "⅕": 0.20,
    "⅖": 0.40,
    "⅗": 0.60,
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
    # ... add more types as needed, in (singular, plural) format ...
)


def _extract_fractional(input_string: str | None):
    if not input_string:
        return

    input_string = input_string.strip()
    if "/" in input_string:
        # for example "1 1/2" is matched
        components = input_string.split(" ")
        if len(components) == 2:
            yield float(components[0])
        numerator, denominator = components[-1:][0].split("/")
        yield float(int(numerator) / int(denominator))
    elif any(symbol in FRACTIONS for symbol in input_string):
        for fraction, amount in FRACTIONS.items():
            if fraction in input_string:
                yield amount
                input_string = input_string.replace(fraction, "")
        yield float(input_string) if input_string else 0
    else:
        yield float(input_string)


def get_minutes(element):
    if element is None:
        return 0

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
        time_text = time_text.split("-", 2)[1]
    if " to " in time_text:  # sometimes formats are like this: '12 to 15 minutes'
        time_text = time_text.split("to", 2)[1]

    time_units = TIME_REGEX.search(time_text).groupdict()
    if not any(time_units.values()):
        return None

    minutes = float(time_units.get("minutes") or 0)
    hours_matched = time_units.get("hours")
    days_matched = time_units.get("days")

    # workaround for formats like: 0D4H45M, that are not a valid iso8601 it seems
    days = float(days_matched) if days_matched else 0
    hours = sum(_extract_fractional(hours_matched))

    hours += round(days * 24)
    minutes += round(hours * 60)
    return minutes


def get_yields(element):
    """
    Will return a string of servings or items, if the recipe is for number of items and not servings
    the method will return the string "x item(s)" where x is the quantity.
    Returns a string of servings or items. If the recipe is for a number of items (not servings),
    it returns "x item(s)" where x is the quantity. This function handles cases where the yield is in dozens,
    such as "4 dozen cookies", returning "4 dozen" instead of "4 servings". Additionally
    accommodates yields specified in batches (e.g., "2 batches of brownies"), returning the yield as stated.
    :param element: Should be BeautifulSoup.TAG, in some cases not feasible and will then be text.
    :return: The number of servings or items.
    :return: The number of servings, items, dozen, batches, etc...
    """
    if element is None:
        raise ElementNotFoundInHtml(element)
    if isinstance(element, str):
        serve_text = element
    else:
        serve_text = element.get_text()

    if SERVE_REGEX_TO.search(serve_text):
        serve_text = serve_text.split(SERVE_REGEX_TO.split(serve_text, 2)[1], 2)[1]

    matched = SERVE_REGEX_NUMBER.search(serve_text).groupdict().get("items") or 0
    serve_text_lower = serve_text.lower()

    for singular, plural in RECIPE_YIELD_TYPES:
        if singular in serve_text_lower:
            return "{} {}".format(matched, singular if int(matched) == 1 else plural)

    if SERVE_REGEX_ITEMS.search(serve_text) is not None:
        return "{} item{}".format(matched, "" if int(matched) == 1 else "s")

    return "{} serving{}".format(matched, "" if int(matched) == 1 else "s")


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
