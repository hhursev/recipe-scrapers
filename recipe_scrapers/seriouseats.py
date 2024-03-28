# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class SeriousEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "seriouseats.com"
