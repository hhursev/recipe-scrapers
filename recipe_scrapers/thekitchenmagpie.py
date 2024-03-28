# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class TheKitchenMagPie(AbstractScraper):
    @classmethod
    def host(cls):
        return "thekitchenmagpie.com"
