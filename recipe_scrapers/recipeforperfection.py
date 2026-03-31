from ._abstract import AbstractScraper


class RecipeForPerfection(AbstractScraper):
    @classmethod
    def host(cls):
        return "recipeforperfection.com"
