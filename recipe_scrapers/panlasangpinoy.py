from ._abstract import AbstractScraper


class PanlasangPinoy(AbstractScraper):
    @classmethod
    def host(cls):
        return "panlasangpinoy.com"
