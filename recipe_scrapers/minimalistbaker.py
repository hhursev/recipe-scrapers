from ._abstract import AbstractScraper


class Minimalistbaker(AbstractScraper):
    @classmethod
    def host(cls):
        return "minimalistbaker.com"
