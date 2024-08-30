from ._abstract import AbstractScraper
from ._utils import normalize_string


class CookingLight(AbstractScraper):
    @classmethod
    def host(cls):
        return "cookinglight.com"

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
