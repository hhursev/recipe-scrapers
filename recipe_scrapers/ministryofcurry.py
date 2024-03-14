# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class MinistryOfCurry(AbstractScraper):
    @classmethod
    def host(cls):
        return "ministryofcurry.com"

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def equipment(self):
        return list(
            {
                (item.get_text())
                for item in self.soup.find_all(
                    "div", class_="wprm-recipe-equipment-name"
                )
            }
        )
