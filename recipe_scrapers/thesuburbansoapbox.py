from ._abstract import AbstractScraper


class TheSuburbanSoapBox(AbstractScraper):
    @classmethod
    def host(cls):
        return "thesuburbansoapbox.com"

    def equipment(self):
        equipment = []
        seen = set()
        for equip_div in self.soup.find_all("div", class_="wprm-recipe-equipment-name"):
            if equip_div.find("a"):
                name = equip_div.find("a").get_text(strip=True)
            else:
                name = equip_div.get_text(strip=True)
            if name and name not in seen:
                equipment.append(name)
                seen.add(name)
        return equipment
