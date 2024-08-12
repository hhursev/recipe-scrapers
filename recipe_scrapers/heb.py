from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class HEB(AbstractScraper):
    @classmethod
    def host(cls, domain="com"):
        return f"heb.{domain}"

    def title(self):
        title_tag = self.soup.find("h1", {"data-qe-id": "recipeTitle"})
        return title_tag.get_text()

    def total_time(self):
        total_time_tag = self.soup.find("span", {"data-qe-id": "recipeTotalTime"})
        return get_minutes(total_time_tag.get_text())

    def yields(self):
        yields_tag = self.soup.find("p", {"data-qe-id": "recipeServingSize"})
        return get_yields(yields_tag.get_text())

    def ingredients(self):
        ingredients_container = self.soup.find(
            "div", {"data-qe-id": "recipeIngredientsContainer"}
        )
        ingredients = ingredients_container.findAll("li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def _instructions_list(self):
        instructions_container = self.soup.find(
            "div", {"data-qe-id": "recipeInstructionsContainer"}
        )
        instructions = instructions_container.findAll("li")
        return [
            normalize_string(instruction.get_text()) for instruction in instructions
        ]

    def instructions(self):
        data = self._instructions_list()
        return "\n".join(data) if data else None

    def image(self):
        container = self.soup.find("div", {"class": "recipeimage"})
        if not container:
            return None

        image = container.find("img", {"src": True})
        return image["src"] if image else None
