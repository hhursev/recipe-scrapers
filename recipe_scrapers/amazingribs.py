# mypy: allow_untyped_defs

from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import normalize_string


class AmazingRibs(AbstractScraper):
    @classmethod
    def host(cls):
        return "amazingribs.com"

    def author(self):
        author_container = self.soup.find("p", {"class": "author-attribution"})
        if author_container and author_container.find("a"):
            return normalize_string(author_container.find("a").text)
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredients li",
        )

    def instructions(self):
        return self.schema.instructions()
