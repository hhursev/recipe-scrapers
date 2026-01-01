from ._abstract import AbstractScraper
from ._grouping_utils import group_ingredients
from ._utils import get_yields
from ._exceptions import FieldNotProvidedByWebsiteException


class AndrewZimmern(AbstractScraper):
    @classmethod
    def host(cls):
        return "andrewzimmern.com"

    def author(self):
        return "Andrew Zimmern"

    def title(self):
        title_element = self.soup.select_one("div.ingredients h2")
        if title_element:
            return title_element.get_text(strip=True)
        return None

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
        instructions = [p.get_text() for p in instruction_paragraphs]
        return "\n".join(instructions)

    def yields(self):
        servings = self.soup.select_one("div.ingredients div.recipe_meta p")
        if servings is None:
            return None
        text = servings.get_text(strip=True).replace("Servings: ", "")
        return get_yields(text)

    def total_time(self):
        raise FieldNotProvidedByWebsiteException(return_value=None)
