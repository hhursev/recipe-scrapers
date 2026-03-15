from ._abstract import AbstractScraper


class CookWithDana(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookwithdana.com"
