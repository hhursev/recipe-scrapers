from ._abstract import AbstractScraper


class TheCookieRookie(AbstractScraper):
    @classmethod
    def host(cls):
        return "thecookierookie.com"
