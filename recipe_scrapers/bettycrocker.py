# BettyCrocker.com scraper
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 18 January, 2020
# =======================================================


from ._abstract import AbstractScraper
from ._utils import normalize_string


class BettyCrocker(AbstractScraper):
    @classmethod
    def host(cls):
        return "bettycrocker.com"

    def title(self):
        return self.schema.title()

    def total_time(self):
        return self.schema.total_time()

    def yields(self):
        return self.schema.yields()

    def image(self):
        return self.schema.image()

    def ingredients(self):
        ingredients = self.soup.find(
            "div", {"class": "recipePartIngredientGroup"}
        ).ul.findAll("li")

        return [
            normalize_string(
                ingredient.find("div", {"class": "quantity"}).text
                + " "
                + ingredient.find("div", {"class": "description"}).span.text
            )
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll("li", {"class": "recipePartStep"})
        return "\n".join(
            [
                normalize_string(
                    instruction.find(
                        "div", {"class": "recipePartStepDescription"}
                    ).get_text()
                )
                for instruction in instructions
            ]
        )

    def ratings(self):
        rating = self.soup.find("meta", {"itemprop": "ratingValue"})["content"]
        return round(float(rating), 2)
