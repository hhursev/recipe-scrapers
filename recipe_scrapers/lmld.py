from ._abstract import AbstractScraper


class Lmld(AbstractScraper):
    @classmethod
    def host(cls):
        return "lmld.org"

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
