from ._abstract import AbstractScraper


class TheKitchenMagPie(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchenmagpie.com"
