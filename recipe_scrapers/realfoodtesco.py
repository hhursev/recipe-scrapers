# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RealFoodTesco(AbstractScraper):
    @classmethod
    def host(cls):
        return "realfood.tesco.com"

    def yields(self):
        return self.schema.yields()

    def ingredient_groups(self):
        return group_ingredients(
            ingredients_list=self.ingredients(),
            soup=self.soup,
            group_heading="h3.recipe-detail__subheading",
            group_element="li.recipe-detail__list-item",
        )

    def ratings(self):
        return self.schema.ratings()
