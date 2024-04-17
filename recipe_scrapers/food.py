# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class Food(AbstractScraper):
    @classmethod
    def host(cls):
        return "food.com"
