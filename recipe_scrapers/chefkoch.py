# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Chefkoch(AbstractScraper):
    @classmethod
    def host(cls):
        return "chefkoch.de"
