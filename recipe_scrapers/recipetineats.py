# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class RecipeTinEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipetineats.com"
