from ._abstract import AbstractScraper


class CookieAndKate(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookieandkate.com"
