# BettyCrocker.com scraper
# Written by G.D. Wallters
# Freely released the code to recipe_scraper group
# 18 January, 2020
# =======================================================
from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string, get_yields


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

        out = []
        for ingredient in ingredients:
            quantity = ingredient.find("div", {"class": "quantity"}).text
            description = ingredient.find("div", {"class": "description"}).span.text
            out.append(normalize_string(quantity + " " + description))

        return "\n".join(out)

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
        try:
            cnt = self.soup.find("meta", {"itemprop": "ratingCount"})["content"]
            rating = self.soup.find("meta", {"itemprop": "ratingValue"})["content"]
            return {"count": int(cnt), "rating": round(float(rating), 2)}
        except Exception:
            return None
