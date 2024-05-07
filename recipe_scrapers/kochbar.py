# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Kochbar(AbstractScraper):
    @classmethod
    def host(cls):
        return "kochbar.de"
