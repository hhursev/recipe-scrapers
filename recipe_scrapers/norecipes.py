from ._abstract import AbstractScraper


class NoRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "norecipes.com"

    def _cleaned_ingredients(self):
        ingredients_list = self.schema.ingredients()
        return [
            ingredient.replace("((", "(").replace("))", ")")
            for ingredient in ingredients_list
        ]

    def ingredients(self):
        return self._cleaned_ingredients()
