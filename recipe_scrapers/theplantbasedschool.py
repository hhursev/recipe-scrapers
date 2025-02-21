from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class ThePlantBasedSchool(AbstractScraper):
    @classmethod
    def host(cls):
        return "theplantbasedschool.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_items = [
            item.get_text()
            for item in self.soup.select(
                "li.wprm-recipe-equipment-item div.wprm-recipe-equipment-name"
            )
        ]
        return get_equipment(equipment_items)

    def instructions(self):
        return "\n".join(
            span.get_text()
            for instruction in self.soup.select(".wprm-recipe-instruction-text")
            for span in instruction.find_all("span", recursive=False)
        )
