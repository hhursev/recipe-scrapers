# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class USAPears(AbstractScraper):
    @classmethod
    def host(cls):
        return "usapears.org"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        total_time = 0
        recipe_legends = self.soup.find_all("div", {"class": "recipe-legend"})
        for recipe_legend in recipe_legends:
            if recipe_legend.get_text() in ["Prep Time", "Cook Time"]:
                total_time += get_minutes(
                    recipe_legend.parent.find("div", {"class": "recipe-value-data"})
                )
        return total_time

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredient_elements = self.soup.find_all("li", {"itemprop": "ingredients"})

        return [
            normalize_string(paragraph.get_text().strip())
            for paragraph in ingredient_elements
        ]

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
