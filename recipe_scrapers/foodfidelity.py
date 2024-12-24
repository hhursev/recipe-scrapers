from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class FoodFidelity(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodfidelity.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def description(self):
        img_tag = self.soup.find("img", {"data-pin-description": True})
        if img_tag:
            return img_tag["data-pin-description"]
