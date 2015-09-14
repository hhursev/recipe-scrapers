import re


TIME_REGEX = re.compile(
    r'\A(\s*(?P<hours>\d+)\s{1}(hours|hrs|hr|h))?((?P<minutes>\s*\d+)\s{1}(minutes|mins|min|m))?\Z'
)


HTML_SYMBOLS = '\xa0'  # &nbsp;
