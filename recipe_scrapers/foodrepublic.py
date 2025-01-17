from ._abstract import AbstractScraper
from ._utils import get_yields


class FoodRepublic(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodrepublic.com"

    def yields(self):
        servings_div = self.soup.find("div", {"class": "recipe-card-servings"})
        servings_amount = (
            servings_div.find("div", {"class": "recipe-card-amount"}).text
            if servings_div
            else "0"
        )
        return get_yields(servings_amount)
