# mypy: allow-untyped-defs

from ._abstract import AbstractScraper


class HerseyLand(AbstractScraper):
    @classmethod
    def host(cls):
        return "hersheyland.com"

    def author(self):
        return "Herseyland"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        return self.schema.instructions()

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()

    def equipment(self):
        return sorted(
            (item.find("span", class_="h6").get_text())
            for item in self.soup.find_all("div", class_="equipment-item")
            if item.find("span", class_="h6")
        )
