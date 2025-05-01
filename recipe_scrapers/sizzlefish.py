from ._abstract import AbstractScraper


class SizzleFish(AbstractScraper):
    @classmethod
    def host(cls):
        return "sizzlefish.com"
