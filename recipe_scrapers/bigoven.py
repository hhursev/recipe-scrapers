from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_yields, normalize_string


class BigOven(AbstractScraper):
    @classmethod
    def host(cls):
        return "bigoven.com"

    def yields(self):
        return get_yields(self.soup.find("div", {"class": "yield"}).text)

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
