# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class PrimalEdgeHealth(AbstractScraper):
    @classmethod
    def host(cls):
        return "primaledgehealth.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients_li = self.soup.select(".wprm-recipe-ingredient")
        ingredients_list = [
            normalize_string(
                li.find("span", {"class": "wprm-recipe-ingredient-amount"}).get_text()
            ).replace("\u00C2", "")
            + " "
            + normalize_string(
                li.find("span", {"class": "wprm-recipe-ingredient-unit"}).get_text()
            ).replace("\u00C2", "")
            + " "
            + normalize_string(
                li.find("span", {"class": "wprm-recipe-ingredient-name"}).get_text()
            ).replace("\u00C2", "")
            for li in ingredients_li
        ]
        return ingredients_list

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()
