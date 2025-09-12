from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_equipment


class HersheyLand(AbstractScraper):
    @classmethod
    def host(cls):
        return "hersheyland.com"

    def author(self):
        raise StaticValueException(return_value="Hersheyland")

    def site_name(self):
        raise StaticValueException(return_value="Hersheyland")

    def equipment(self):
        equipment_items = [
            item.find("span", class_="h6").get_text()
            for item in self.soup.find_all("div", class_="equipment-item")
            if item.find("span", class_="h6")
        ]
        return get_equipment(equipment_items)

    def instructions(self):
        instructions = self.schema.instructions()
        filtered_instructions = "\n".join(
            line for line in instructions.split("\n") if not line.startswith("Step")
        )
        return filtered_instructions
