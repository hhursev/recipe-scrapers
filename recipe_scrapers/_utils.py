import re
import bs4


TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours|H))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes|M))?'
)

SERVING_REGEX = re.compile(
    r'(\d+)\s*servings|(?:serves|makes)\s*(\d+)?|^\s*(\d+)\s*$'
)

def get_minutes(dom_element):
    try:
        tstring = dom_element.get_text()
        if '-' in tstring:
            tstring = tstring.split('-')[1]  # some time formats are like this: '12-15 minutes'
        matched = TIME_REGEX.search(tstring)
        minutes = int(matched.groupdict().get('minutes') or 0)
        minutes += 60 * int(matched.groupdict().get('hours') or 0)
        return minutes
    except AttributeError:  # if dom_element not found or no matched
        return 0

def get_servings(dom_element):
    try:
        if isinstance(dom_element, bs4.element.Tag):
            tstring = dom_element.get_text()
        else:
            tstring = str(dom_element)
        matched = SERVING_REGEX.search(tstring)
        text = None
        for i in range(1,4):
            if matched.group(i):
                text = matched.group(i)
        servings = int(text or 0)
        return servings
    except AttributeError:
        return 0

def normalize_string(string):
    return re.sub(
        r'\s+', ' ',
        string.replace(
            '\xa0', ' ').replace(  # &nbsp;
            '\n', ' ').replace(
            '\t', ' ').strip()
    )
