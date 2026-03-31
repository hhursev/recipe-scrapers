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
        total_time_element = self.soup.find(
            "span", class_="white-text", string=re.compile("TOTAL TIME")
        )
        if total_time_element:
            total_time = total_time_element.get_text().split(":")[1]
            return get_minutes(total_time)

    def yields(self):
        servings_element = self.soup.find(
            "div", class_="fusion-li-item-content", string=re.compile("SERVINGS")
        )
        if servings_element:
            servings = servings_element.get_text().split(":")[1]
            return get_yields(servings)

    def ingredients(self):
        ingredients_list = []
        ingredients_section = self.soup.find(
            "h3", id=re.compile("ingredients.*")
        ).find_next(name="ul")
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
            instruction_text = normalize_string(step.find_next(name="p").get_text())
            if instruction_text:
                instructions_list.append(instruction_text)
        return "\n".join(instructions_list)

    def prep_time(self):
        prep_time_element = self.soup.find(
            "span", class_="white-text", string=re.compile("PREP TIME")
        )
        if prep_time_element:
            prep_time = prep_time_element.get_text().split(":")[1]
            return get_minutes(prep_time)

    def cook_time(self):
        cook_time_element = self.soup.find(
            "span", class_="white-text", string=re.compile("COOK TIME")
        )
        if cook_time_element:
            cook_time = cook_time_element.get_text().split(":")[1]
            return get_minutes(cook_time)

    def description(self):
        description_text = self.soup.find("h1").find_next(name="p")
        return normalize_string(description_text.get_text()) if description_text else ""
