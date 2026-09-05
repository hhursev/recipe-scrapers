from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class MarieClaire(AbstractScraper):
    @classmethod
    def host(cls):
        return "marieclaire.fr"

    def ingredients(self):
        ing_selector = (
            ".Article-recipeText:has(> ul:not(.Article-recipeItems)) "
            "> ul:not(.Article-recipeItems) > li"
        )
        elements = self.soup.select(ing_selector)
        ingredients = [element.get_text(" ", strip=True) for element in elements]
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".Article-recipeText:has(> ul:not(.Article-recipeItems)) > p > strong",
            ".Article-recipeText:has(> ul:not(.Article-recipeItems)) > ul:not(.Article-recipeItems) > li",
        )
