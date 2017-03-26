import re


TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours|H))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes|M))?'
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


def normalize_string(string):
    return re.sub(
        r'\s+', ' ',
        string.replace(
            u'\xa0', u' ').replace(  # &nbsp;
            u'\n', u' ').replace(
            u'\t', u' ').strip()
    )
