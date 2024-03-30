# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_equipment


class Downshiftology(AbstractScraper):
    @classmethod
    def host(cls):
        return "downshiftology.com"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def ratings(self):
        return self.schema.ratings()

    def equipment(self):
        equipment_items = [
            item.find("a", class_="wprm-recipe-equipment-link").get_text()
            for item in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if item.find("a", class_="wprm-recipe-equipment-link")
        ]
        return get_equipment(equipment_items)
