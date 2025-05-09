from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class LoveAndLemons(AbstractScraper):
    @classmethod
    def host(cls):
        return "loveandlemons.com"

    def ingredients(self):
        ingredients_elements = self.soup.select(".wprm-recipe-ingredient")
        return [element.get_text() for element in ingredients_elements]

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )
