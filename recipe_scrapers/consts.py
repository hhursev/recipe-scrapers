import re


TIME_REGEX = re.compile(
    r'\A(\s*(?P<hours>\d+)\s{1}(hrs|hr|h))?((?P<minutes>\s*\d+)\s{1}(mins|min|m))?\Z'
)
