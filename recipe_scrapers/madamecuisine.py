from ._abstract import AbstractScraper
from ._utils import get_yields


class MadameCuisine(AbstractScraper):
    @classmethod
    def host(cls):
        return "madamecuisine.de"

    def author(self):
        return self.soup.find("meta", {"name": "author"})["content"]

    def title(self):
        return self.soup.find("h2", {"class": "wprm-recipe-name"}).get_text()

    def category(self):
        return self.soup.find("span", {"class": "wprm-recipe-keyword"}).get_text()

    def total_time(self):
        time_elements = self.soup.select(
            ".wprm-recipe-details.wprm-recipe-details-minutes"
        )
        total_time = 0

        for time_element in time_elements:
            total_time += int(time_element.contents[0].strip())

        return total_time

    def yields(self):
        return get_yields(self.soup.find("span", {"class": "wprm-recipe-servings"}))

    def image(self):
        return self.soup.select_one(".wp-block-image img")["src"]

    def ingredients(self):
        ingredients = self.soup.find_all("li", {"class": "wprm-recipe-ingredient"})
        ingredient_list = []

        for ingredient in ingredients:
            ingredient_list.append(ingredient.get_text().strip())

        return ingredient_list

    def instructions(self):
        instructions = self.soup.find_all(
            "div", {"class": "wprm-recipe-instruction-text"}
        )
        instruction_list = []

        for instruction in instructions:
            instruction_list.append(instruction.get_text().strip())

        return "\n".join(instruction_list)

    def cuisine(self):
        return self.soup.find("span", {"class": "wprm-recipe-cuisine"}).get_text()

    def description(self):
        return self.soup.find("div", {"class": "wprm-recipe-summary"}).get_text()
