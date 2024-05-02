# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Koket(AbstractScraper):
    @classmethod
    def host(cls):
        return "koket.se"
