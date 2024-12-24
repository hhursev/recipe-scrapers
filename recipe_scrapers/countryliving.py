from ._abstract import AbstractScraper


class CountryLiving(AbstractScraper):
    @classmethod
    def host(cls):
        return "countryliving.com"
