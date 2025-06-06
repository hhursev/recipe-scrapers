from ._abstract import AbstractScraper
from ._utils import get_equipment


class StaySnatched(AbstractScraper):
    @classmethod
    def host(cls):
        return "staysnatched.com"

    def author(self):
        author_element = self.soup.find(
            "div",
            {
                "class": "wprm-recipe-block-container wprm-recipe-block-container-columns wprm-block-text-normal wprm-recipe-author-container"
            },
        )
        return author_element.find("a").get_text() if author_element else "Unknown"

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
