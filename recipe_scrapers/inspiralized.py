# mypy: allow-untyped-defs

from ._abstract import AbstractScraper
from ._decorators import opengraph_fallback, schemaorg_fallback
from ._utils import get_minutes, get_yields, normalize_string


class Inspiralized(AbstractScraper):
    @classmethod
    def host(cls):
        return "inspiralized.com"

    def title(self):
        return self.soup.find("h2").get_text()

    @schemaorg_fallback
    def author(self):
        if type(self.page_data) == bytes and b"Ali Maffucci" in self.page_data:
            return "Ali Maffucci"
        if type(self.page_data) == str and "Ali Maffucci" in self.page_data:
            return "Ali Maffucci"

    def total_time(self):
        return get_minutes(self.soup.find("span", {"itemprop": "totalTime"}))

    def yields(self):
        return get_yields(self.soup.find("span", {"itemprop": "servingSize"}))

    def ingredients(self):
        ingredients = self.soup.findAll("li", {"class": "ingredient"})

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = self.soup.findAll("li", {"class": "instruction"})

        return "\n".join(
            [normalize_string(instruction.get_text()) for instruction in instructions]
        )

    @opengraph_fallback
    def image(self):
        pass
