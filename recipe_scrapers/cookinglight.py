from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class CookingLight(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookinglight.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return get_yields(self.schema.yields())

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find("div", {"class": "ingredients"}).ul.findAll("li")
        return "\n".join(
            [normalize_string(ingredient.get_text()) for ingredient in ingredients]
        )

    def instructions(self):
        instructions = self.soup.find("div", {"class": "recipe-instructions"}).findAll(
            "div", {"class": "step"}
        )
        return "\n".join([normalize_string(instr.get_text()) for instr in instructions])

    def ratings(self):
        try:
            return self.schema.ratings()
        except Exception:
            return None
