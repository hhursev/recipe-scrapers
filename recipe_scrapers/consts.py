import re


TIME_REGEX = re.compile(
    r'\A(\s*(?P<hours>\d+)\s*(hours|hrs|hr|h))?(\s*(?P<minutes>\d+)\s*(minutes|mins|min|m))?\Z'
)


HTML_SYMBOLS = '\xa0'  # &nbsp;
