# mypy: disallow_untyped_defs=False

from ._abstract import AbstractScraper


class Reishunger(AbstractScraper):
    @classmethod
    def host(cls):
        return "reishunger.de"

    def author(self):
        return self.schema.author()

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        return self.schema.ingredients()

    def instructions(self):
        elements = self.soup.findAll("div", {"class": "flex flex-col"})

        # for recipes that do NOT allow to switch between different cooking methods
        for element in elements:
            if "Zubereitung" in element.get_text():
                return element.get_text().replace("\xa0", " ")

    def ratings(self):
        block = self.soup.find("div", {"class": "nrating"})
        if block:
            cnt = len(block.findAll("span", {"class": "fa-star"}))
            return cnt
        return block
