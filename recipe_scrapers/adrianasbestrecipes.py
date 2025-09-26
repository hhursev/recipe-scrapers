from ._abstract import AbstractScraper
from ._utils import get_equipment


class AdrianasBestRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "adrianasbestrecipes.com"

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)

    def instructions(self):
        instructions = []
        instruction_groups = self.soup.select("div.wprm-recipe-instruction-group")
        for group in instruction_groups:
            steps = group.select("li.wprm-recipe-instruction")
            for step in steps:
                text = step.get_text(strip=True)
                if text:
                    instructions.append(text)
        return "\n".join(instructions)
