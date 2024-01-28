# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AddAPinch(AbstractScraper):
    @classmethod
    def host(cls):
        return "addapinch.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

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
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient-group li",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def equipment(self):
        return list(
            dict.fromkeys(
                (equip.find("a").get_text())
                for equip in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
                if equip.find("a") and equip.find("a").get_text()
            )
        )
