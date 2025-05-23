from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class FortyAprons(AbstractScraper):
    @classmethod
    def host(cls):
        return "40aprons.com"

    def author(self):
        return self.schema.author()

    def description(self):
        return self.schema.description()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def category(self):
        return self.schema.category()

    def cook_time(self):
        return self.schema.cook_time()

    def cuisine(self):
        return self.schema.cuisine()

    def nutrients(self):
        return self.schema.nutrients()

    def prep_time(self):
        return self.schema.prep_time()

    def ratings(self):
        return self.schema.ratings()

    def ratings_count(self):
        return self.schema.ratings_count()

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)

    def keywords(self):
        return self.schema.keywords()

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "h4.wprm-recipe-group-name",
            "li.wprm-recipe-ingredient",
        )
