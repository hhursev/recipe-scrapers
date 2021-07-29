from ._abstract import AbstractScraper
from ._utils import normalize_string


class Koket(AbstractScraper):
    @classmethod
    def host(cls):
        return "koket.se"

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
        ingredients = self.soup.find_all("span", {"class": "ingredient"})
        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instructions = []
        for instruction in self.soup.find("section", {"id": "step-by-step"}).find_all(
            "span"
        ):
            try:
                instructions.append(instruction.find("b").next_sibling.next_sibling)
            except AttributeError:
                instructions.append(instruction.get_text())
        return instructions

    def ratings(self):
        return self.schema.ratings()
