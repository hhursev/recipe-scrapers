from ._abstract import AbstractScraper


class LittleFerraroKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "littleferrarokitchen.com"

    def equipment(self):
        return list(
            dict.fromkeys(
                (equip.find("a").get_text())
                for equip in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
                if equip.find("a") and equip.find("a").get_text()
            )
        )
