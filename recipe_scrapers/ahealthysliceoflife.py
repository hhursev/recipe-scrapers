from ._abstract import AbstractScraper
from ._utils import normalize_string


class AHealthySliceOfLife(AbstractScraper):
    @classmethod
    def host(cls):
        return "ahealthysliceoflife.com"

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"class": "tasty-recipes-ingredients-body"}
        ).find_all("p")
        ingredients = [normalize_string(ing.get_text().strip()) for ing in ingredients]
        if not ingredients:
            ingredients = self.schema.ingredients()
        return ingredients
