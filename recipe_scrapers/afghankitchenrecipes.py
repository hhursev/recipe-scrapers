from ._abstract import AbstractScraper
from ._exceptions import StaticValueException
from ._utils import get_yields


class AfghanKitchenRecipes(AbstractScraper):
    @classmethod
    def host(cls):
        return "afghankitchenrecipes.com"

    def site_name(self):
        raise StaticValueException(return_value="Afghan Kitchen Recipes")

    def author(self):
        given_name = self.soup.find("h5", {"class": "given-name"})
        return given_name and given_name.find("a", {"rel": "author"}).get_text()

    def total_time(self):
        ready_in = self.soup.find("li", {"class": "ready-in"})
        if not ready_in:
            return
        ready_text = ready_in.find("span", {"class": "value"}).get_text()
        if not ready_text or not ready_text.endswith("h"):
            return
        hours, minutes = ready_text[:-2].split(":")
        return int(hours) * 60 + int(minutes)

    def yields(self):
        servings = self.soup.find("li", {"class": "servings"})
        if not servings:
            return
        return get_yields(servings)

    def ingredients(self):
        ingredient_elements = self.soup.findAll("li", {"class": "ingredient"})
        return [
            element.get_text() for element in ingredient_elements if element.get_text()
        ]

    def instructions(self):
        instruction_elements = self.soup.findAll("p", {"class": "instructions"})
        return "\n".join(
            [
                element.get_text().strip()
                for element in instruction_elements
                if element.get_text()
            ]
        )

    def ratings(self):
        rating = self.soup.find("meta", {"itemprop": "ratingValue"})
        return rating and rating.get("content") and round(float(rating["content"]), 2)
