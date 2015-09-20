import re


TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes))?'
)


HTML_SYMBOLS = '\xa0'  # &nbsp;
