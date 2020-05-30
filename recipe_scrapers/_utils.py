import html
import re


TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours|H|óra))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes|M|perc))?'
)

SERVE_REGEX_NUMBER = re.compile(
    r'(\D*(?P<items>\d+)?\D*)'
)

SERVE_REGEX_ITEMS = re.compile(
    r'\bsandwiches\b |\btacquitos\b | \bmakes\b', flags=re.I | re.X
)

SERVE_REGEX_TO = re.compile(
    r'\d+(\s+to\s+|-)\d+', flags=re.I | re.X
)


def get_minutes(element):
    if element is None:
        return None

    if isinstance(element, str):
        time_text = element
    else:
        time_text = element.get_text()
    if '-' in time_text:
        time_text = time_text.split('-')[1]  # sometimes formats are like this: '12-15 minutes'
    if 'h' in time_text:
        time_text = time_text.replace('h', 'hours') + 'minutes'

    matched = TIME_REGEX.search(time_text)

    minutes = int(matched.groupdict().get('minutes') or 0)
    minutes += 60 * int(matched.groupdict().get('hours') or 0)

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
        serve_text = serve_text.split(SERVE_REGEX_TO.split(serve_text)[1])[1]

    matched = SERVE_REGEX_NUMBER.search(serve_text).groupdict().get('items') or 0
    servings = "{} serving(s)".format(matched)

    if SERVE_REGEX_ITEMS.search(serve_text) is not None:
        # This assumes if object(s), like sandwiches, it is 1 person.
        # Issue: "Makes one 9-inch pie, (realsimple-testcase, gives "9 items")
        servings = "{} item(s)".format(matched)

    return servings


def normalize_string(string):
    # Convert all named and numeric character references (e.g. &gt;, &#62;)
    unescaped_string = html.unescape(string)
    return re.sub(
        r'\s+', ' ',
        unescaped_string.replace(
            '\xa0', ' ').replace(  # &nbsp;
            '\n', ' ').replace(
            '\t', ' ').strip()
    )
