from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class FoodNetwork(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodnetwork.com"

    def title(self):
        return self.schema.title()

    def author(self):
        return self.schema.author()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()
