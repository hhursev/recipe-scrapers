from ._abstract import AbstractScraper


class OneHundredOneCookBooks(AbstractScraper):
    @classmethod
    def host(cls):
        return "101cookbooks.com"
