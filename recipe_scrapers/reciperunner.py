# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper


class RecipeRunner(AbstractScraper):
    @classmethod
    def host(cls):
        return "reciperunner.com"

    def ratings(self):
        return self.schema.ratings()
