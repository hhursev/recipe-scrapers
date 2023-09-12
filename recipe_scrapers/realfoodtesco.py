# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class RealFoodTesco(AbstractScraper):
    @classmethod
    def host(cls):
        return "realfood.tesco.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            ingredients_list=self.ingredients(),
            soup=self.soup,
            group_heading="h3.recipe-detail__subheading",
            group_element="li.recipe-detail__list-item",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
