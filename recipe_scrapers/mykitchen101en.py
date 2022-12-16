# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._exceptions import RecipeScrapersExceptions


class MyKitchen101en(AbstractScraper):
    @classmethod
    def host(cls):
        return "mykitchen101en.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        raise RecipeScrapersExceptions(
            f"{self.host()} does not provide time information."
        )

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
