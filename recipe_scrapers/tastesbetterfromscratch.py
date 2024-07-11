from ._abstract import AbstractScraper


class TastesBetterFromScratch(AbstractScraper):
    @classmethod
    def host(cls):
        return "tastesbetterfromscratch.com"
