from ._abstract import AbstractScraper
from ._utils import get_equipment


class ThePlantBasedSchool(AbstractScraper):
    @classmethod
    def host(cls):
        return "theplantbasedschool.com"

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)

    def instructions(self):
        return "\n".join(
            span.get_text()
            for instruction in self.soup.select(".wprm-recipe-instruction-text")
            for span in instruction.find_all("span", recursive=False)
        )
