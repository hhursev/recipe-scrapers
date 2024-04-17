# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class SimplyCookit(AbstractScraper):
    @classmethod
    def host(cls):
        return "simply-cookit.com"

    def category(self):
        return self.schema.category()

    def ingredients(self):
        ingredients = []
        for li in self.soup.find("ul", {"class": "recipe_ingredients"}).findAll("li"):
            ingredients.append(normalize_string(li.get_text()))

        return ingredients

    def instructions(self):
        instructions = []
        for li in self.soup.find("ul", {"class": "recipe_steps"}).findAll("li"):
            li.find("span", {"class": "number"}).clear()
            instructions.append(normalize_string(li.get_text()))

        return "\n".join(instructions)

    def cuisine(self):
        return self.schema.cuisine()

    def description(self):
        return self.schema.description()
