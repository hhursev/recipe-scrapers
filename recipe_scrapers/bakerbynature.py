from ._abstract import AbstractScraper


class BakerByNature(AbstractScraper):
    @classmethod
    def host(cls):
        return "bakerbynature.com"
