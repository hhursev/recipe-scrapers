from ._abstract import AbstractScraper


class SouthernBite(AbstractScraper):
    @classmethod
    def host(cls):
        return "southernbite.com"
