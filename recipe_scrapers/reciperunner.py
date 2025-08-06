from ._abstract import AbstractScraper


class RecipeRunner(AbstractScraper):
    @classmethod
    def host(cls):
        return "reciperunner.com"
