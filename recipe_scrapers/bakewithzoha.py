from ._abstract import AbstractScraper


class BakeWithZoha(AbstractScraper):
    @classmethod
    def host(cls):
        return "bakewithzoha.com"
