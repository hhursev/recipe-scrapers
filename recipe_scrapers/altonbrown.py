from ._abstract import AbstractScraper


class AltonBrown(AbstractScraper):
    @classmethod
    def host(cls):
        return "altonbrown.com"

    def equipment(self):
        return list(
            dict.fromkeys(
                (equip.get_text())
                for equip in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
            )
        )
