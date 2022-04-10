from ._abstract import AbstractScraper
from ._utils import normalize_string


class TheHappyFoodie(AbstractScraper):
    @classmethod
    def host(cls):
        return "thehappyfoodie.co.uk"

    def title(self):
        return self.schema.title()

    def category(self):
        return self.schema.category()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"class": "hf-ingredients__container"}
        ).findAll("tr")

        amount = 0
        ingredient_name = 1
        ingredients = [
            (
                ingredient.find_all("td")[amount].get_text(),
                ingredient.find_all("td")[ingredient_name].get_text(),
            )
            for ingredient in ingredients
        ]

        return [
            normalize_string("{} {}".format(amount, name))
            for amount, name in ingredients
        ]

    def instructions(self):
        return self.schema.instructions()

    def author(self):
        return self.schema.author()

    def cuisine(self):
        return self.schema.cuisine()
