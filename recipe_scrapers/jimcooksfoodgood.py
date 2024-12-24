from ._abstract import AbstractScraper


class JimCooksFoodGood(AbstractScraper):
    @classmethod
    def host(cls):
        return "jimcooksfoodgood.com"
