from ._abstract import AbstractScraper
from ._utils import get_equipment


class KrollsKorner(AbstractScraper):
    @classmethod
    def host(cls):
        return "krollskorner.com"

    def author(self):
        author_tag = self.soup.select_one(
            ".wprm-recipe-details.wprm-recipe-author.wprm-block-text-normal a"
        )
        return author_tag.get_text(strip=True)

    def equipment(self):
        equipment_items = [
            text
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if (text := equip.get_text())
        ]
        return get_equipment(equipment_items)
