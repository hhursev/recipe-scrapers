from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients


class AndrewZimmern(AbstractScraper):
    @classmethod
    def host(cls):
        return "andrewzimmern.com"

    def ingredients(self):
        ingredients = []
        ingredient_elements = self.soup.select("div.ingredients_list li")
        for li in ingredient_elements:
            ingredient = li.get_text(strip=True)
            ingredients.append(ingredient)
        return ingredients

    def ingredient_groups(self):
        return group_ingredients(
            self.ingredients(),
            self.soup,
            "div.ingredients_list p strong",
            "div.ingredients_list li",
        )

    def instructions(self):
        instruction_paragraphs = self.soup.select("div.preparation p")
        instructions = [p.get_text(strip=True) for p in instruction_paragraphs]
        return "\n".join(instructions)
