from ._abstract import AbstractScraper


class NYTimes(AbstractScraper):

    @classmethod
    def host(cls):
        return 'cooking.nytimes.com'
        