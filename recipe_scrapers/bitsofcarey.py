from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_equipment


class BitsOfCarey(AbstractScraper):
    @classmethod
    def host(cls):
        return "bitsofcarey.com"

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            ".wprm-recipe-ingredient-group h4",
            ".wprm-recipe-ingredient",
        )

    def equipment(self):
        equipment_items = self.soup.select(
            ".wprm-recipe-equipment-container .wprm-recipe-equipment-item"
        )
        equipment_list = []

        for item in equipment_items:
            name_element = item.select_one(".wprm-recipe-equipment-name")
            note = item.select_one(".wprm-recipe-equipment-notes")

            name = name_element.get_text(strip=True)

            if note:
                note_text = note.get_text(strip=True)
                name = name.replace(note_text, "").strip()
                name += f" (note: {note_text})"

            equipment_list.append(name)

        return get_equipment(equipment_list)
