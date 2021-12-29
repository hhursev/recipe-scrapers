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
        ingredients = self.soup.find("div", {"class": "recipeIngredients"}).ul.findAll(
            "li"
        )

        return [
            normalize_string(
                ingredient.find("span", {"class": "quantity"}).text
                + " "
                + ingredient.find("span", {"class": "description"}).text
            )
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.find("div", {"class": "recipeSteps"}).ul.findAll("li")

        return "\n".join(
            [
                normalize_string(
                    instruction.find("div", {"class": "stepDescription"}).get_text()
                )
                for instruction in instructions
            ]
        )

    def ratings(self):
        rating = self.soup.find("div", {"class": "ratingCountContainer"}).find(
            "span", {"class": "stars"}
        )["aria-label"]
        return round(float(rating), 2)
