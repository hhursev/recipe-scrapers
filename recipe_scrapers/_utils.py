import html
import inspect
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
    r"(?:\D*(?P<days>\d+)\s*(?:days|D))?"
    r"(?:\D*(?P<hours>[\d.\s/?¼½¾⅓⅔⅕⅖⅗]+)\s*(?:hours|hrs|hr|h|óra|:))?"
    r"(?:\D*(?P<minutes>\d+)\s*(?:minutes|mins|min|m|perc|$))?"
    r"(?:\D*(?P<seconds>\d+)\s*(?:seconds|secs|sec|s))?",
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


def format_diet_name(diet_input):
    replacements = {
        # https://schema.org/RestrictedDiet
        "DiabeticDiet": "Diabetic Diet",
        "GlutenFreeDiet": "Gluten Free Diet",
        "HalalDiet": "Halal Diet",
        "HinduDiet": "Hindu Diet",
        "KosherDiet": "Kosher Diet",
        "LowCalorieDiet": "Low Calorie Diet",
        "LowFatDiet": "Low Fat Diet",
        "LowLactoseDiet": "Low Lactose Diet",
        "LowSaltDiet": "Low Salt Diet",
        "VeganDiet": "Vegan Diet",
        "VegetarianDiet": "Vegetarian Diet",
    }
    if "https://schema.org/" in diet_input:
        diet_input = diet_input.replace("https://schema.org/", "")

    for key, value in replacements.items():
        if key in diet_input:
            return value

    return diet_input


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

    # If element is a BeautifulSoup Tag, extract its text content
    if hasattr(element, "text"):
        element = element.text

    try:
        return int(element)
    except ValueError:
        pass

    if not isinstance(element, str):
        raise ValueError("Unexpected format for time element")
    time_text = element

    # attempt iso8601 duration parsing
    if "-" in time_text:  # sometimes formats are like this: '12-15 minutes'
        _min, _, time_text = time_text.partition("-")
    if " to " in time_text:  # sometimes formats are like this: '12 to 15 minutes'
        _min, _to, time_text = time_text.partition(" to ")

    if time_text is None:
        return None

    # Attempt ISO8601 duration parsing
    if time_text.startswith("P") and "T" in time_text:
        try:
            duration = isodate.parse_duration(time_text)
            total_minutes = math.ceil(duration.total_seconds() / 60)
            return None if total_minutes == 0 else total_minutes
        except Exception:
            pass

    time_units = TIME_REGEX.search(time_text).groupdict()
    if not any(time_units.values()):
        return None

    minutes_matched = time_units.get("minutes")
    hours_matched = time_units.get("hours")
    days_matched = time_units.get("days")
    seconds_matched = time_units.get("seconds")

    days = float(days_matched) if days_matched else 0
    hours = _extract_fractional(hours_matched) if hours_matched else 0
    minutes = float(minutes_matched) if minutes_matched else 0
    seconds = float(seconds_matched) if seconds_matched else 0

    total_minutes = minutes + (hours * 60) + (days * 24 * 60) + (seconds / 60)
    # Rounding to the nearest whole number, considering seconds
    return round(total_minutes)


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

    best_match = None
    best_match_length = 0

    for singular, plural in RECIPE_YIELD_TYPES:
        if singular in serve_text_lower or plural in serve_text_lower:
            match_length = (
                len(singular) if singular in serve_text_lower else len(plural)
            )
            if match_length > best_match_length:
                best_match_length = match_length
                best_match = f"{matched} {singular if int(matched) == 1 else plural}"

    if best_match:
        return best_match

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
    # Remove HTML tags
    no_html_string = re.sub("<[^>]*>", "", unescaped_string)
    return re.sub(
        r"\s+",
        " ",
        no_html_string.replace("\xc2\xa0", " ")
        .replace("\xa0", " ")
        .replace("\u200b", "")
        .replace("\r\n", " ")
        .replace("\n", " ")  # &nbsp;
        .replace("\t", " ")
        .strip(),
    )


def csv_to_tags(csv, lowercase=False):
    raw_tags = csv.split(",")
    seen = set()
    tags = []
    for raw_tag in raw_tags:
        tag = raw_tag.strip()
        if tag and tag.lower() not in seen:
            seen.add(tag.lower())
            tags.append(tag.lower() if lowercase else tag)
    return tags


def url_path_to_dict(path):
    pattern = (
        r"^"
        r"((?P<schema>.+?)://)?"
        r"((?P<user>.+?)(:(?P<password>.*?))?@)?"
        r"(?P<host>[^:/]+)"
        r"(:(?P<port>\d+?))?"
        r"(?P<path>/.*?)?"
        r"(?P<query>[?].*?)?"
        r"$"
    )
    regex = re.compile(pattern)
    matches = regex.match(path)
    return matches.groupdict() if matches else None


def get_host_name(url):
    return url_path_to_dict(url.replace("://www.", "://"))["host"]


def change_keys(obj, convert):
    """
    Recursively goes through the dictionary obj and replaces keys with the convert function

    Useful for fixing incorrect property keys, e.g. in JSON-LD dictionaries

    Credit: StackOverflow user 'baldr'
    (https://web.archive.org/web/20201022163147/https://stackoverflow.com/questions/11700705/python-recursively-replace
        -character-in-keys-of-nested-dictionary/33668421)

    Note: with modifications applied.
    """
    if isinstance(obj, dict):
        return {convert(k): change_keys(v, convert) for k, v in obj.items()}
    elif isinstance(obj, (list, set, tuple)):
        cls = type(obj)
        return cls(change_keys(item, convert) for item in obj)
    else:
        return obj


def get_url_slug(url):
    path = url_path_to_dict(url).get("path")
    return path.split("/")[-1]


def get_abstract_methods():
    from ._abstract import AbstractScraper

    return [
        name
        for name, value in AbstractScraper.__dict__.items()  # Attributes of the abstract scraper class..
        if not name.startswith("_")  # ... that are not private ...
        and inspect.isfunction(value)  # ... and are functions ...
        and name not in {"links", "to_json"}  # ... and not excluded as special-cases.
        or name == "host"  # ... explicitly include the `host` method.
    ]


def get_nutrition_keys():
    return [
        "servingSize",
        "calories",
        "fatContent",
        "saturatedFatContent",
        "unsaturatedFatContent",
        "transFatContent",
        "carbohydrateContent",
        "sugarContent",
        "proteinContent",
        "sodiumContent",
        "fiberContent",
        "cholesterolContent",
    ]
