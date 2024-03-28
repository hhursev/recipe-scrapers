# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class MyRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "myrecipes.com"
