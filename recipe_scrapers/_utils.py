import re

from functools import wraps


TIME_REGEX = re.compile(
    r'(\D*(?P<hours>\d+)\s*(hours|hrs|hr|h|Hours|H))?(\D*(?P<minutes>\d+)\s*(minutes|mins|min|m|Minutes|M))?'
)


def get_minutes(element):
    try:
        tstring = element.get_text()
        if '-' in tstring:
            tstring = tstring.split('-')[1]  # sometimes formats are like this: '12-15 minutes'
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
            '\xa0', ' ').replace(  # &nbsp;
            '\n', ' ').replace(
            '\t', ' ').strip()
    )


def on_exception_return(to_return):
    """
    On unpredicted exception return `to_return` provided in the decorator.
    Still raise some specific errors (as NotImplementedError listed here)

    This is needed due to not being able to predict what elements can be missing
    from the DOM and not being able to foresee all the possible erorrs from bs4
    """
    def decorate(decorated_function):
        @wraps(decorated_function)
        def wrap(*args, **kwargs):
            try:
                result = decorated_function(*args, **kwargs)
                return result
            except NotImplementedError as e:
                raise e
            except Exception:
                return to_return
        return wrap
    return decorate
