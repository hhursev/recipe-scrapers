from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class SkinnyTaste(AbstractScraper):
    @classmethod
    def host(cls):
        return "skinnytaste.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_container = self.soup.find(
            "div", class_="wprm-recipe-equipment-container"
        )
        if equipment_container:
            return [
                item.get_text(strip=True)
                for item in equipment_container.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
            ]
        return None
