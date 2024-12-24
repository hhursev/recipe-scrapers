from ._abstract import AbstractScraper
from ._utils import get_yields, normalize_string


class FoodRepublic(AbstractScraper):
    @classmethod
    def host(cls):
        return "foodrepublic.com"

    def title(self):
        title_div = self.soup.find("div", {"class": "recipe-card-title"})
        return title_div.get_text()

    def total_time(self):
        prep_time_div = self.soup.find("div", {"class": "recipe-card-prep-time"})
        cook_time_div = self.soup.find("div", {"class": "recipe-card-cook-time"})

        prep_time = (
            int(prep_time_div.find("div", {"class": "recipe-card-amount"}).text)
            if prep_time_div
            else 0
        )
        cook_time = (
            int(cook_time_div.find("div", {"class": "recipe-card-amount"}).text)
            if cook_time_div
            else 0
        )

        return prep_time + cook_time

    def yields(self):
        servings_div = self.soup.find("div", {"class": "recipe-card-servings"})
        servings_amount = (
            servings_div.find("div", {"class": "recipe-card-amount"}).text
            if servings_div
            else "0"
        )
        return get_yields(servings_amount)

    def ingredients(self):
        ingredients = self.soup.select("ul.recipe-ingredients li")

        return [normalize_string(ingredient.get_text()) for ingredient in ingredients]

    def instructions(self):
        instruction_list = self.soup.find("ol", {"class": "recipe-directions"})
        instructions = instruction_list.findAll("li") if instruction_list else []

        return "\n".join([instruction.get_text() for instruction in instructions])
