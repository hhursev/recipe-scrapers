import re
from html.parser import HTMLParser
from io import StringIO

TIME_REGEX = re.compile(
    r"(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|óra))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|perc))?",
    re.IGNORECASE,
)

SERVE_REGEX_NUMBER = re.compile(r"(\D*(?P<items>\d+)?\D*)")

SERVE_REGEX_ITEMS = re.compile(
    r"\bsandwiches\b |\btacquitos\b | \bmakes\b | \bcups\b | \bappetizer\b | \bporzioni\b",
    flags=re.I | re.X,
)

SERVE_REGEX_TO = re.compile(r"\d+(\s+to\s+|-)\d+", flags=re.I | re.X)


def get_minutes(element):
    if element is None:
        return None

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
    if "h" in time_text:
        time_text = time_text.replace("h", "hours") + "minutes"

    matched = TIME_REGEX.search(time_text)

    minutes = int(matched.groupdict().get("minutes") or 0)
    minutes += 60 * int(matched.groupdict().get("hours") or 0)

    return minutes


def get_yields(element):
    """
    Will return a string of servings or items, if the receipt is for number of items and not servings
    the method will return the string "x item(s)" where x is the quantity.
    :param element: Should be BeautifulSoup.TAG, in some cases not feasible and will then be text.
    :return: The number of servings or items.
    """
    if isinstance(element, str):
        serve_text = element
    else:
        serve_text = element.get_text()

    if SERVE_REGEX_TO.search(serve_text):
        serve_text = serve_text.split(SERVE_REGEX_TO.split(serve_text, 2)[1], 2)[1]

    matched = SERVE_REGEX_NUMBER.search(serve_text).groupdict().get("items") or 0
    servings = "{} serving(s)".format(matched)

    if SERVE_REGEX_ITEMS.search(serve_text) is not None:
        # This assumes if object(s), like sandwiches, it is 1 person.
        # Issue: "Makes one 9-inch pie, (realsimple-testcase, gives "9 items")
        servings = "{} item(s)".format(matched)

    return servings


def normalize_string(string, strip_html=True):
    # The goal here is to get this string as clean as possible. Address the following cases
    #  - Remove leading/trailing whitespace
    #  - Remove escaped whitespace characters from whole string (e.g \n, \t)
    #  - Remove HTML Tags
    #  - Convert all named and numeric character references (e.g. &gt;, &#62;)

    # Deal with HTML and HTML Encoded Characters
    string = strip_tags(
        f"<tag>{string}<tag>"
    )  # This is a workaround, since HTMLParser expects valid markup
    string = strip_tags(
        f"<tag>{string}<tag>"
    )  # This is another workaround, handles "&amp;amp;"

    # Clean string of whitespace
    return re.sub(
        r"\s+",
        " ",
        string.replace("\xa0", " ")
        .replace("\n", " ")  # &nbsp;
        .replace("\r", " ")
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


# Taken from https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False  # this setting appears to do nothing
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, d):
        self.text.write(d)

    def get_data(self):
        return self.text.getvalue()


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
