from ._abstract import AbstractScraper


class TasteOfHome(AbstractScraper):
    @classmethod
    def host(cls):
        return "tasteofhome.com"
