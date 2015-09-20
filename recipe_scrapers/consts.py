import re


TIME_REGEX = re.compile(
    r'\A(\s*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours))?(\s*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes))?\Z'
)


HTML_SYMBOLS = '\xa0'  # &nbsp;
