# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class FoodFidelity(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodfidelity.com"

    def author(self):
        author_tag = self.soup.find("span", {"class": "byline"}).find(
            "a", {"class": "url fn n"}
        )
        return author_tag.get_text() if author_tag else "Food Fidelity"

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
            ".wprm-recipe-ingredient",
        )

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        img_tag = self.soup.find("img", {"data-pin-description": True})
        if img_tag:
            return img_tag["data-pin-description"]
