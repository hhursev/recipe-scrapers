from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class Thinlicious(AbstractScraper):
    @classmethod
    def host(cls):
        return "thinlicious.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-group-name",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_list = self.soup.select(".wprm-recipe-equipment-name")
        return [equipment.get_text() for equipment in equipment_list]
