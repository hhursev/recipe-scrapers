# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class FifteenSpatulas(AbstractScraper):
    @classmethod
    def host(cls):
        return "fifteenspatulas.com"
