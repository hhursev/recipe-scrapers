from ._abstract import AbstractScraper


class CookWell(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookwell.com"
