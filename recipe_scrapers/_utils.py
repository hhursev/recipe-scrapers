import html
import re

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
    r"(\D*(?P<hours>[\d.\s/?¼½¾⅓⅔⅕⅖⅗]+)\s*(hours|hrs|hr|h|óra))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|perc))?",
    re.IGNORECASE,
)

SERVE_REGEX_NUMBER = re.compile(r"(\D*(?P<items>\d+)?\D*)")

SERVE_REGEX_ITEMS = re.compile(
    r"\bsandwiches\b |\btacquitos\b | \bmakes\b | \bcups\b | \bappetizer\b | \bporzioni\b | \bcookies\b | \b(large |small )?buns\b",
    flags=re.I | re.X,
)

SERVE_REGEX_TO = re.compile(r"\d+(\s+to\s+|-)\d+", flags=re.I | re.X)


def get_minutes(element, return_zero_on_not_found=False):
    if element is None:
        # to be removed
        if return_zero_on_not_found:
            return 0
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
    if time_text.startswith("P") and "T" in time_text:
        time_text = time_text.split("T", 2)[1]
    if "-" in time_text:
        time_text = time_text.split("-", 2)[
            1
        ]  # sometimes formats are like this: '12-15 minutes'
    if " to " in time_text:
        time_text = time_text.split("to", 2)[
            1
        ]  # sometimes formats are like this: '12 to 15 minutes'
    if "h" in time_text:
        time_text = time_text.replace("h", "hours")

    matched = TIME_REGEX.search(time_text)

    minutes = int(matched.groupdict().get("minutes") or 0)
    hours_matched = matched.groupdict().get("hours")

    if hours_matched:
        hours_matched = hours_matched.strip()
        if any([symbol in FRACTIONS.keys() for symbol in hours_matched]):
            hours = 0
            for fraction, value in FRACTIONS.items():
                if fraction in hours_matched:
                    hours += value
                    hours_matched = hours_matched.replace(fraction, "")
            hours += int(hours_matched) if hours_matched else 0
        elif "/" in hours_matched:
            # for example "1 1/2" is matched
            hours_matched_split = hours_matched.split(" ")
            hours = 0
            if len(hours_matched_split) == 2:
                hours += int(hours_matched_split[0])
            fraction = hours_matched_split[-1:][0].split("/")
            hours += float(int(fraction[0]) / int(fraction[1]))
        else:
            hours = float(hours_matched)

        minutes += round(60 * hours, 0)

    return minutes


def get_yields(element):
    """
    Will return a string of servings or items, if the receipt is for number of items and not servings
    the method will return the string "x item(s)" where x is the quantity.
    :param element: Should be BeautifulSoup.TAG, in some cases not feasible and will then be text.
    :return: The number of servings or items.
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
    servings = "{} serving{}".format(matched, "" if int(matched) == 1 else "s")

    if SERVE_REGEX_ITEMS.search(serve_text) is not None:
        # This assumes if object(s), like sandwiches, it is 1 person.
        # Issue: "Makes one 9-inch pie, (realsimple-testcase, gives "9 items")
        servings = "{} item{}".format(matched, "" if int(matched) == 1 else "s")

    return servings


def normalize_string(string):
    # Convert all named and numeric character references (e.g. &gt;, &#62;)
    unescaped_string = html.unescape(string)
    return re.sub(
        r"\s+",
        " ",
        unescaped_string.replace("\xa0", " ")
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
