# mypy: disallow_untyped_defs=False
from ._abstract import AbstractScraper
from ._utils import normalize_string


class SimplyCookit(AbstractScraper):
    @classmethod
    def host(cls):
        return "simply-cookit.com"

    def author(self):
        return self.schema.author()

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
