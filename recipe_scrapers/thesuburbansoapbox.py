from ._abstract import AbstractScraper
from ._utils import get_equipment


class TheSuburbanSoapBox(AbstractScraper):
    @classmethod
    def host(cls):
        return "thesuburbansoapbox.com"

    def equipment(self):
        items = []
        for equip_div in self.soup.find_all("div", class_="wprm-recipe-equipment-name"):
            if equip_div.find("a"):
                name = equip_div.find("a").get_text(strip=True)
            else:
                name = equip_div.get_text(strip=True)
            if name:
                items.append(name)
        return get_equipment(items)
