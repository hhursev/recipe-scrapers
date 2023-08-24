# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class LifestyleOfAFoodie(AbstractScraper):
    @classmethod
    def host(cls):
        return "lifestyleofafoodie.com"

    def author(self):
        entry_author = self.soup.find("span", {"class": "entry-author-name"})

        if entry_author:
            return entry_author.get_text()

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

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.wprm-recipe-ingredient-group h4",
            "ul.wprm-recipe-ingredients li",
        )
