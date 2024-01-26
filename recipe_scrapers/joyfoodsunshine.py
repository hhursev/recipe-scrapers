# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import get_equipment, normalize_string


class Joyfoodsunshine(AbstractScraper):
    @classmethod
    def host(cls):
        return "joyfoodsunshine.com"

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
        ingredients = self.soup.findAll("li", {"class": "wprm-recipe-ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

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
