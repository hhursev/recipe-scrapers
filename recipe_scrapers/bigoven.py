# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_yields, normalize_string


class BigOven(AbstractScraper):
    @classmethod
    def host(cls):
        return "bigoven.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "yield"}).text)

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "span.ingredient.ingHeading",
            "span.ingredient:not(.ingHeading)",
        )

    def instructions(self):
        ps = self.soup.find("div", {"class": "instructions"}).findAll("p")
        return "\n".join([normalize_string(p.text) for p in ps])

    def ratings(self):
        return self.schema.ratings()
