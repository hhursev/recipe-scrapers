# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class ForkToSpoon(AbstractScraper):
    @classmethod
    def host(cls):
        return "forktospoon.com"

    def category(self):
        return self.schema.category()

    def ratings(self):
        return self.schema.ratings()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def equipment(self):
        seen = set()
        return [
            equip.get_text()
            for equip in self.soup.find_all("div", class_="wprm-recipe-equipment-name")
            if equip.get_text()
            and (equip.get_text() not in seen and not seen.add(equip.get_text()))
        ]
