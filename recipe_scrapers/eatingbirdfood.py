# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class EatingBirdFood(AbstractScraper):
    @classmethod
    def host(cls):
        return "eatingbirdfood.com"
