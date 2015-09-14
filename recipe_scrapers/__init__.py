import re

from .allrecipes import AllRecipes


SCRAPERS = {
    AllRecipes.host(): AllRecipes,
}


def url_path_to_dict(path):
    pattern = (r'^'
               r'((?P<schema>.+?)://)?'
               r'((?P<user>.+?)(:(?P<password>.*?))?@)?'
               r'(?P<host>.*?)'
               r'(:(?P<port>\d+?))?'
               r'(?P<path>/.*?)?'
               r'(?P<query>[?].*?)?'
               r'$'
               )
    regex = re.compile(pattern)
    matches = regex.match(path)
    url_dict = matches.groupdict() if matches is not None else None

    return url_dict


def scrap_me(url_path):
    return SCRAPERS[url_path_to_dict(url_path)['host']](url_path)


__all__ = ['scrap_me']
