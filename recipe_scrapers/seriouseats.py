# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback
from ._utils import get_yields


class SeriousEats(AbstractScraper):
    @classmethod
    def host(cls):
        return "seriouseats.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        recipe_servings = self.soup.find("div", {"class": "recipe-serving"})
        recipe_yield = self.soup.find("div", {"class": "recipe-yield"})
        return get_yields(
            (recipe_servings or recipe_yield).find("span", {"class": "meta-text__data"})
        )

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    @opengraph_fallback
    def image(self):
        pass

    def ratings(self):
        return self.schema.ratings()
