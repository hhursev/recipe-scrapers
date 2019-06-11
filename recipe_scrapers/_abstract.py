import requests

from bs4 import BeautifulSoup

from recipe_scrapers._utils import on_exception_return

# some sites close their content for 'bots', so user-agent must be supplied
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
}


class AbstractScraper():

    def __getattribute__(self, name):
        """
        Decorate custom methods to handle exceptions as we want and as we
        specify in the "on_exception_return" method decorator

        Do not do this META-decorating on testing so to have better traceback
        """
        if not object.__getattribute__(self, 'testing_mode'):
            to_return = None
            decorated_methods = [
                'title',
                'total_time',
                'yields',
                'instructions',
                'ingredients',
                'links'
            ]
            if name in decorated_methods:
                to_return = ''
            if name == 'total_time':
                to_return = 0
            if name == 'yields':
                to_return = ''
            if name == 'ingredients':
                to_return = []
            if name == 'links':
                to_return = []
            if to_return is not None:
                return on_exception_return(to_return)(object.__getattribute__(self, name))

        return object.__getattribute__(self, name)

    def __init__(self, url, test=False):
        if test:  # when testing, we load a file
            with url:
                self.soup = BeautifulSoup(
                    url.read(),
                    "html.parser"
                )
        else:
            self.soup = BeautifulSoup(
                requests.get(
                    url,
                    headers=HEADERS
                ).content,
                "html.parser"
            )
        self.testing_mode = test
        self.url = url

    def url(self):
        return self.url

    def host(self):
        """ get the host of the url, so we can use the correct scraper """
        raise NotImplementedError("This should be implemented.")

    def title(self):
        raise NotImplementedError("This should be implemented.")

    def total_time(self):
        """ total time it takes to preparate the recipe in minutes """
        raise NotImplementedError("This should be implemented.")

    def yields(self):
        """ The number of servings or items in the recipe """
        raise NotImplementedError("This should be implemented.")

    def ingredients(self):
        raise NotImplementedError("This should be implemented.")

    def instructions(self):
        raise NotImplementedError("This should be implemented.")

    def ratings(self):
        raise NotImplementedError("This should be implemented.")

    def reviews(self):
        raise NotImplementedError("This should be implemented.")

    def links(self):
        invalid_href = ('#', '')
        links_html = self.soup.findAll('a', href=True)

        return [
            link.attrs
            for link in links_html
            if link['href'] not in invalid_href
        ]
