import re

from ._abstract import AbstractScraper
from ._utils import get_minutes, get_yields, normalize_string


class KellysCleanKitchen(AbstractScraper):
    @classmethod
    def host(cls):
        return "kellyscleankitchen.com"

    def title(self):
        return normalize_string(
            self.soup.find("h1", class_="fusion-post-title").get_text()
        )

    def total_time(self):
        total_time = (
            self.soup.find_all("div", class_="fusion-li-item-content")[3]
            .get_text()
            .split(":")[1]
            .strip()
        )
        return get_minutes(total_time)

    def yields(self):
        servings = (
            self.soup.find_all("div", class_="fusion-li-item-content")[0]
            .get_text()
            .split(":")[1]
            .strip()
        )
        return get_yields(servings)

    def ingredients(self):
        ingredients_list = []
        ingredients_section = self.soup.find(id=re.compile("ingredients.*")).find_next(
            "ul"
        )
        if ingredients_section:
            ingredients = ingredients_section.find_all("li")
            ingredients_list = [
                normalize_string(ingredient.get_text()) for ingredient in ingredients
            ]
        return ingredients_list

    def instructions(self):
        instructions_list = []
        steps = self.soup.find_all(class_="recipe-steps")
        for step in steps:
            instruction_text = normalize_string(step.find_next("p").get_text())
            if instruction_text:
                instructions_list.append(instruction_text)
        return instructions_list

    def prep_time(self):
        prep_time = (
            self.soup.find_all("div", class_="fusion-li-item-content")[1]
            .get_text()
            .split(":")[1]
            .strip()
        )
        return get_minutes(prep_time)

    def cook_time(self):
        cook_time = (
            self.soup.find_all("div", class_="fusion-li-item-content")[2]
            .get_text()
            .split(":")[1]
            .strip()
        )
        return get_minutes(cook_time)

    def description(self):
        description_text = self.soup.find("h1").find_next("p")
        return normalize_string(description_text.get_text()) if description_text else ""
