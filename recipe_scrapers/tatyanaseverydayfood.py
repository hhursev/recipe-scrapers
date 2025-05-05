from ._abstract import AbstractScraper


class TatyanasEverydayFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "tatyanaseverydayfood.com"
